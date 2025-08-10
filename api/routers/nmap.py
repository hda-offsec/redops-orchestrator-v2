from fastapi import APIRouter
from pydantic import BaseModel

from apps.nmap.profiles import PROFILES
from apps.nmap.service import run_scan
from core.jobs import enqueue, get_job
from core.events import stream_job_events

router = APIRouter(prefix="/nmap", tags=["nmap"])

class ScanRequest(BaseModel):
    target: str
    profile: str = "normal"
    options: list[str] = []

@router.get("/profiles")
async def profiles():
    return list(PROFILES.keys())

@router.post("/scans", status_code=202)
async def start_scan(req: ScanRequest):
    job_id = enqueue(run_scan, req.model_dump(), queue_name="nmap")
    return {"job_id": job_id}

@router.get("/scans/{job_id}")
async def scan_status(job_id: str):
    job = get_job(job_id, "nmap")
    if not job:
        return {"status": "unknown"}
    return {"status": job.get_status(), "result": job.result}


@router.get("/streams/{job_id}")
async def scan_stream(job_id: str):
    """Server-sent events stream for job status."""
    return stream_job_events(job_id, "nmap")
