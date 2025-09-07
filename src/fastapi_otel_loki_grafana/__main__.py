from fastapi_otel_loki_grafana.routes import app
from fastapi_otel_loki_grafana.log import get_logger
from uvicorn import run

def main() -> None:
    logger = get_logger(__name__)
    logger.debug("Starting server")
    run(app, host="0.0.0.0", port=8000)