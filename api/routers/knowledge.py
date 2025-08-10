import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.get("/tips")
async def tips():
    path = Path("data/knowledge/oscp_tips.json")
    if path.exists():
        return json.loads(path.read_text())
    return {}
