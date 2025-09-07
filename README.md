# Python Observability Setup

This repo is a way for me to not forget the basics of setting up an observability stack with OTEL.
The structure is similar to the officiel [Otel tutorial's "expert grogu" level](https://opentelemetry.io/blog/2023/logs-collection/#expert-grogu-level), i.e it relies on a `filelog` receiver to avoid the complexity of dedicated endpoints.

This is built with [uv](https://astral.sh/uv), the components are roughly:

* Server:
  - [FastAPI](https://fastapi.tiangolo.com) for the python ASGI server
  - [python-json-logger](https://github.com/nhairs/python-json-logger) to output python's `logging` to JSON
* Observability:
 - [OTel Collector](https://opentelemetry.io/) collects the JSON logs and sends them to any storage backend you need
 - [Loki](https://grafana.com/docs/loki/latest/) is the store for log data, and is [configured](./config/otel-config.yaml) on the OTel collector as a `receiver`
 - [Grafana](https://grafana.com/docs/grafana/latest/) is the dashboard/ui/query layer, which allows easy inspection of log data

 ## Logging config for python

 You have many options, but I ended up with the new [yaml config file format](./config/logging_config.yaml), as usual with the python logging utility, you have 3 main components:

 - **Logger:** who emits the log, what level, etc
 - **Formatter:** how to output the logs (string formatting, json formatting, etc)
 - **Handler:** how is the log stream handled (e.g. stored, displayed, etc)

As of now, simple config: JSON formatter, and console+file handlers.

## Docker

### Building the API component

Nothing too fancy, check [the dockerfile](./docker/Dockerfile) to see for yourself.

**One caveat:** the python-slim docker image did not have `curl` installed, so the `healthcheck` commands would fail.

### Docker compose

For such a small template, the compose file is already quite complex (4 services, one shared volume, multiple config files).

One aspect that made me lose time is sharing a volume between containers, and getting each container's filesystem right in terms of where to map the shared volume: the python container had everything under `/app`, the otel container required the volume to be mapped to `/usr/src/app`

## OTel

For now, basic config where a single log file is available to the OTel collector, which sends it to Loki's `otlhttp` endpoint at `http://loki:3100/oltp`, and grafana connects to loki to display logs.