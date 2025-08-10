from core.logging import logger


def run_scan(params: dict):
    logger.info("dirbusting", target=params.get("target"))
    return {"entries": []}
