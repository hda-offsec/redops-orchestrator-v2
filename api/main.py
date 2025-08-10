# api/main.py
from __future__ import annotations

import os
from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from starlette.responses import JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from api.routers import dirbusting, knowledge, lfi, nmap, orchestrator, vuln, waf, webrecon
from core.auth import api_key
from core.metrics import instrumentator

# ------------------------
# Config
# ------------------------
def _cors_origins_from_env() -> list[str]:
    """
    Lis REDOPS_CORS_ORIGINS=orig1,orig2,...
    Ex: "http://localhost:5173,http://127.0.0.1:5173"
    Valeur par défaut: localhost/127.0.0.1:5173 (Vite) + 5000 (même origine).
    Mettre "*" en dernier recours si besoin.
    """
    env_val = os.getenv("REDOPS_CORS_ORIGINS")
    if env_val:
        return [o.strip() for o in env_val.split(",") if o.strip()]
    # défauts raisonnables pour dev
    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5000",
        "http://127.0.0.1:5000",
    ]


limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])

app = FastAPI(title="RedOps API")
app.state.limiter = limiter

# rate limiting
app.add_exception_handler(
    RateLimitExceeded,
    lambda request, exc: JSONResponse(status_code=429, content={"detail": "rate limit exceeded"}),
)
app.add_middleware(SlowAPIMiddleware)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins_from_env(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers (protégés par X-RedOps-Token)
app.include_router(nmap.router,          prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(webrecon.router,      prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(vuln.router,          prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(dirbusting.router,    prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(lfi.router,           prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(waf.router,           prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(orchestrator.router,  prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(knowledge.router,     prefix="/api/v1", dependencies=[Depends(api_key)])

# Healthcheck public
@app.get("/health")
async def health():
    return {"status": "ok"}

# Prometheus
instrumentator.instrument(app).expose(app)

# ------------------------
# UI statique (si buildée)
# ------------------------
dist_dir = Path(__file__).resolve().parent.parent / "webui" / "dist"
if dist_dir.is_dir():
    # Servez la SPA sous /ui et /webui
    app.mount("/ui",    StaticFiles(directory=str(dist_dir), html=True), name="ui")
    app.mount("/webui", StaticFiles(directory=str(dist_dir), html=True), name="webui")

    @app.get("/")
    async def root_redirect():
        # Page d’accueil => l’UI
        return RedirectResponse(url="/ui")
else:
    @app.get("/")
    async def root_redirect_docs():
        # Pas de build front ? Redirige vers Swagger.
        return RedirectResponse(url="/docs")
