from fastapi import APIRouter
from pydantic import BaseModel

from apps.lfi.profiles import PROFILES
from apps.lfi.service import run_scan
from core.jobs import enqueue, get_job

router = APIRouter(prefix="/lfi", tags=["lfi"])

class ScanRequest(BaseModel):
    target: str
    profile: str = "quick_signatures"

@router.get("/profiles")
async def profiles():
    return list(PROFILES.keys())

@router.post("/scans", status_code=202)
async def start_scan(req: ScanRequest):
    job_id = enqueue(run_scan, req.model_dump(), queue_name="lfi")
    return {"job_id": job_id}

@router.get("/scans/{job_id}")
async def scan_status(job_id: str):
    job = get_job(job_id, "lfi")
    if not job:
        return {"status": "unknown"}
    return {"status": job.get_status(), "result": job.result}
