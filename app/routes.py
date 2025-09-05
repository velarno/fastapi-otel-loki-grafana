from fastapi import FastAPI

from app.log import get_logger

app = FastAPI(
    title="fastapi-otel-loki-grafana",
    description="FastAPI App with OpenTelemetry, Loki and Grafana",
)

logger = get_logger(__name__)

@app.get("/")
def read_root():
    logger.info("Hello, world!")
    return {"message": "Hello, world!"}

@app.get("/health")
def health():
    logger.info("Health check")
    return {"status": "healthy"}