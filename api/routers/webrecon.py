from fastapi import APIRouter
from pydantic import BaseModel
from core.jobs import enqueue, get_job
from apps.webrecon.service import run_scan, PROFILES

router = APIRouter(prefix="/webrecon", tags=["webrecon"])

class ScanRequest(BaseModel):
    target: str
    profile: str = "default"

@router.get("/profiles")
async def profiles():
    return list(PROFILES.keys())

@router.post("/scans", status_code=202)
async def start_scan(req: ScanRequest):
    job_id = enqueue(run_scan, req.model_dump(), queue_name="webrecon")
    return {"job_id": job_id}

@router.get("/scans/{job_id}")
async def scan_status(job_id: str):
    job = get_job(job_id, "webrecon")
    if not job:
        return {"status": "unknown"}
    return {"status": job.get_status(), "result": job.result}
