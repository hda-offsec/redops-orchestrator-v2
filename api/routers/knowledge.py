from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.get("/tips")
async def tips():
    path = Path("data/knowledge/oscp_tips.json")
    if path.exists():
        return json.loads(path.read_text())
    return {}
