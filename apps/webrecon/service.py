from core.logging import logger


def run_scan(params: dict):
    logger.info("webrecon", target=params.get("target"))
    return {"headers": {}, "probable_webapp": True}
