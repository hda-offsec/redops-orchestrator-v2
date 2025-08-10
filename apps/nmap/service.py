from pathlib import Path
from core.logging import logger
from core.sanitize import validate_target, sanitize_nmap_options
from core.shell import run
from .parser import parse
from .profiles import PROFILES


def run_scan(params: dict):
    target = params["target"]
    if not validate_target(target):
        return {"error": "invalid target"}
    profile = PROFILES.get(params.get("profile", "normal"), [])
    opts = sanitize_nmap_options(profile + params.get("options", []))
    cmd = ["nmap", target, *opts, "-oX", "out.xml"]
    logger.info("nmap_start", target=target)
    cwd = Path("data/run" ) / "tmp"
    cwd.mkdir(parents=True, exist_ok=True)
    try:
        result = run(cmd, cwd)
        parsed = parse((cwd/"out.xml").read_text()) if (cwd/"out.xml").exists() else {}
        return {"stdout": result.stdout, "stderr": result.stderr, "result": parsed}
    except Exception as e:
        return {"error": str(e)}
