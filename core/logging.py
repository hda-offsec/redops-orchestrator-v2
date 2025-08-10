import structlog

structlog.configure(
    processors=[structlog.processors.TimeStamper(fmt="iso"), structlog.processors.JSONRenderer()],
)

logger = structlog.get_logger()
