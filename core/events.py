import asyncio
import datetime as dt
import json

from fastapi.responses import StreamingResponse

from .jobs import get_job


def _format(event: str, payload: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(payload)}\n\n"


def stream_job_events(job_id: str, queue_name: str) -> StreamingResponse:
    """Return a StreamingResponse yielding job status events.

    This function polls the RQ job status and emits SSE messages whenever the
    status changes. It also gracefully handles connection errors or missing jobs
    so that the stream always yields at least one event.
    """

    async def event_generator():
        status_map = {
            "queued": "job_queued",
            "started": "job_started",
            "finished": "job_finished",
            "failed": "job_failed",
        }
        prev_status = None
        while True:
            try:
                job = get_job(job_id, queue_name)
            except Exception as exc:  # pragma: no cover - redis not available
                now = dt.datetime.utcnow().isoformat()
                payload = {
                    "event": "job_failed",
                    "timestamp": now,
                    "data": {"error": str(exc)},
                }
                yield _format("job_failed", payload)
                break
            if job is None:
                now = dt.datetime.utcnow().isoformat()
                payload = {"event": "job_not_found", "timestamp": now, "data": {}}
                yield _format("job_not_found", payload)
                break
            status = job.get_status()
            if status != prev_status:
                event = status_map.get(status, "progress")
                now = dt.datetime.utcnow().isoformat()
                data = {
                    "event": event,
                    "timestamp": now,
                    "data": {"status": status},
                }
                if status == "finished":
                    data["data"]["result"] = job.result
                yield _format(event, data)
                prev_status = status
                if status in {"finished", "failed"}:
                    break
            await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
