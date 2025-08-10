from core.logging import logger


def run_dag(dag: dict):
    logger.info("orchestrator", dag=dag)
    return {"status": "done"}
