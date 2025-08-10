from fastapi import FastAPI, Depends
from core.auth import api_key
from core.metrics import instrumentator
from api.routers import nmap, webrecon, vuln, dirbusting, lfi, waf, orchestrator, knowledge

app = FastAPI(title="RedOps API")
app.include_router(nmap.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(webrecon.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(vuln.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(dirbusting.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(lfi.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(waf.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(orchestrator.router, prefix="/api/v1", dependencies=[Depends(api_key)])
app.include_router(knowledge.router, prefix="/api/v1", dependencies=[Depends(api_key)])

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

instrumentator.instrument(app).expose(app)
