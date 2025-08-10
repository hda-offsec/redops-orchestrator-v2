import typer
import uvicorn

from core.jobs import run_worker

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


@cli.command()
def once(module: str, target: str, profile: str = "normal"):
    from importlib import import_module

    svc = import_module(f"apps.{module}.service")
    res = svc.run_scan(target=target, profile=profile, options=[])
    typer.echo(res)

if __name__ == "__main__":
    cli()
