from fastapi import Header, HTTPException, status
from core.config import settings

async def api_key(x_redops_token: str = Header(...)):
    if x_redops_token != settings.api_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
