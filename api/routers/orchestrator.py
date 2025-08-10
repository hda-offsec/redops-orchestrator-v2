from fastapi import APIRouter
from pydantic import BaseModel

from apps.orchestrator.service import run_dag
from core.jobs import enqueue, get_job

router = APIRouter(prefix="/orchestrator", tags=["orchestrator"])

class DagRequest(BaseModel):
    dag: dict

@router.post("/start", status_code=202)
async def start(req: DagRequest):
    job_id = enqueue(run_dag, req.dag, queue_name="orchestrator")
    return {"job_id": job_id}

@router.get("/status/{job_id}")
async def status(job_id: str):
    job = get_job(job_id, "orchestrator")
    if not job:
        return {"status": "unknown"}
    return {"status": job.get_status(), "result": job.result}
