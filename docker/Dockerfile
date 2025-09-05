FROM python:3.12-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y curl

RUN uv sync

CMD ["uv", "run", "rfp-analyzer"]

#CMD ["uv", "run", "opentelemetry-instrument", "--traces_exporter", "console", "--metrics_exporter", "none", "--logs_exporter", "none", "python", "rfp_analyzer.__main__.py"]