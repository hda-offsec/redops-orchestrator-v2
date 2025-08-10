from core.logging import logger
from .profiles import PROFILES


def run_scan(params: dict):
    logger.info("dirbusting", target=params.get("target"))
    return {"entries": []}
