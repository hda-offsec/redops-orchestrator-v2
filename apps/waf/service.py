from typing import Any, Dict

from core.logging import logger

PROFILES: Dict[str, Dict[str, Any]] = {"default": {}}


def run_scan(params: dict):
    logger.info("waf", target=params.get("target"))
    return {"waf": False}
