from core.logging import logger
from .profiles import PROFILES
from .detection import detect


def run_scan(params: dict):
    logger.info("lfi", target=params.get("target"))
    return {"checks": detect(params.get("target", ""))}
