import typer
from api.main import app
from core.jobs import run_worker
from core.config import settings
import uvicorn

cli = typer.Typer()

@cli.command()
def api(host: str = "0.0.0.0", port: int = 5000):
    uvicorn.run("api.main:app", host=host, port=port, reload=False)

@cli.command()
def worker(queue: str):
    run_worker(queue)

@cli.command()
def profiles(module: str):
    from importlib import import_module
    mod = import_module(f"apps.{module}.profiles")
    typer.echo(list(mod.PROFILES.keys()))

@cli.command()
def health():
    typer.echo("ok")

if __name__ == "__main__":
    cli()
