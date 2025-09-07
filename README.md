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