# run.py
from __future__ import annotations

import json
import shutil
import sys
from importlib import import_module
from typing import Optional

import typer
import uvicorn
from dotenv import load_dotenv

# deps runtime déjà présentes dans le projet
import redis
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from core.jobs import run_worker

cli = typer.Typer(add_completion=False, help="RedOps Orchestrator v2 CLI")

# Chargement .env (silencieux si absent)
load_dotenv(override=False)


def _echo_json(data: dict | list) -> None:
    typer.echo(json.dumps(data, ensure_ascii=False, indent=2))


def _fail(msg: str, code: int = 1) -> None:
    typer.echo(f"ERROR: {msg}", err=True)
    raise typer.Exit(code=code)


@cli.command(help="Démarre l'API FastAPI (uvicorn).")
def api(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host d'écoute"),
    port: int = typer.Option(5000, "--port", "-p", help="Port d'écoute"),
    reload: bool = typer.Option(False, "--reload", help="Auto-reload (dev)"),
    log_level: str = typer.Option("info", "--log-level", help="trace|debug|info|warning|error|critical"),
) -> None:
    # Utilise uvloop/httptools si dispos (via uvicorn[standard])
    uvicorn.run(
        "api.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level=log_level,
        # http="httptools",  # uvicorn choisit auto si installé
        # loop="uvloop",
    )


@cli.command(help="Lance un worker RQ pour une queue.")
def worker(
    queue: str = typer.Argument(..., help="Nom de la queue (ex: nmap)"),
) -> None:
    run_worker(queue)


@cli.command(help="Liste les profils disponibles d'un module.")
def profiles(
    module: str = typer.Argument(..., help="Module (nmap | webrecon | vuln | dirbusting | lfi | waf)"),
) -> None:
    try:
        mod = import_module(f"apps.{module}.profiles")
    except ModuleNotFoundError:
        _fail(f"Module inconnu: {module}")
    profiles_dict = getattr(mod, "PROFILES", None)
    if not isinstance(profiles_dict, dict):
        _fail(f"Aucun PROFILES trouvé pour {module}")
    _echo_json(list(profiles_dict.keys()))


@cli.command(help="Exécute un scan synchrone court (dev).")
def once(
    module: str = typer.Argument(..., help="Module (ex: nmap)"),
    target: str = typer.Option(..., "--target", "-t", help="Cible IP/FQDN"),
    profile: str = typer.Option("normal", "--profile", "-p", help="Profil du module"),
) -> None:
    try:
        svc = import_module(f"apps.{module}.service")
    except ModuleNotFoundError:
        _fail(f"Module inconnu: {module}")
    if not hasattr(svc, "run_scan"):
        _fail(f"apps.{module}.service.run_scan introuvable")
    try:
        res = svc.run_scan(target=target, profile=profile, options=[])
    except Exception as e:  # noqa: BLE001
        _fail(f"Échec run_scan: {e}")
    _echo_json(res if isinstance(res, (dict, list)) else {"result": res})


@cli.command(help="Health check complet: Redis, DB, binaires, disque.")
def health() -> None:
    # Lazy import des settings pour ne pas casser si configuration partielle
    try:
        from core.config import Settings  # pydantic-settings
    except Exception:
        Settings = None  # type: ignore[assignment]

    cfg = Settings() if Settings else None
    checks: dict[str, object] = {"status": "ok", "components": {}}

    # Redis
    try:
        redis_url = (cfg.REDOPS_REDIS_URL if cfg else None) or "redis://localhost:6379/0"
        r = redis.from_url(redis_url)
        r.ping()
        checks["components"]["redis"] = {"status": "ok", "url": redis_url}
    except Exception as e:  # noqa: BLE001
        checks["components"]["redis"] = {"status": "fail", "error": str(e)}
        checks["status"] = "fail"

    # DB
    try:
        db_url = (cfg.REDOPS_DB_URL if cfg else None) or "sqlite:///./data/redops.db"
        engine = create_engine(db_url, pool_pre_ping=True)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        checks["components"]["db"] = {"status": "ok", "url": db_url}
    except SQLAlchemyError as e:
        checks["components"]["db"] = {"status": "fail", "error": str(e)}
        checks["status"] = "fail"

    # Binaries requis (MVP): nmap (obligatoire), nuclei/ffuf optionnels
    bins = {"nmap": "required", "nuclei": "optional", "ffuf": "optional"}
    bin_report = {}
    for b, req in bins.items():
        path = shutil.which(b)
        ok = path is not None
        bin_report[b] = {"found": ok, "path": path, "required": req == "required"}
        if req == "required" and not ok:
            checks["status"] = "fail"
    checks["components"]["binaries"] = bin_report

    # Espace disque data/
    try:
        total, used, free = shutil.disk_usage(".")
        checks["components"]["disk"] = {"total": total, "used": used, "free": free}
    except Exception as e:  # noqa: BLE001
        checks["components"]["disk"] = {"status": "fail", "error": str(e)}
        checks["status"] = "fail"

    _echo_json(checks)
    raise typer.Exit(code=0 if checks["status"] == "ok" else 1)


@cli.command(help="Affiche la version (runtime).")
def version() -> None:
    _echo_json(
        {
            "python": sys.version.split()[0],
            "uvicorn": uvicorn.__version__,
            "typer": typer.__version__,
        }
    )


if __name__ == "__main__":
    cli()
