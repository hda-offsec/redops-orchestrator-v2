from core.logging import logger
from typing import Dict, Any

PROFILES: Dict[str, Dict[str, Any]] = {"default": {}}


def run_scan(params: dict):
    logger.info("waf", target=params.get("target"))
    return {"waf": False}
