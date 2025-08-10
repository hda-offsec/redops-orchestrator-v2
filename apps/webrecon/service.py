from core.logging import logger
from .profiles import PROFILES


def run_scan(params: dict):
    logger.info("webrecon", target=params.get("target"))
    return {"headers": {}, "probable_webapp": True}
