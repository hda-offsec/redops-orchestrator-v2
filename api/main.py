from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from starlette.responses import JSONResponse

from api.routers import dirbusting, knowledge, lfi, nmap, orchestrator, vuln, waf, webrecon
from core.auth import api_key
from core.metrics import instrumentator

limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])

app = FastAPI(title="RedOps API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exc: JSONResponse(status_code=429, content={"detail": "rate limit exceeded"}))
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(nmap.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(webrecon.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(vuln.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(dirbusting.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(lfi.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(waf.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(orchestrator.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(knowledge.router, prefix="/api/v1", dependencies=[Depends(api_key)])

@app.get("/health")
async def health():
    return {"status": "ok"}

instrumentator.instrument(app).expose(app)
