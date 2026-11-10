---
description: Query metrics in Elasticsearch time series data streams with PromQL through the ES|QL runtime and a Prometheus-compatible HTTP API.
navigation_title: PromQL
applies_to:
  stack: preview 9.4, ga 9.5
  serverless: ga
products:
  - id: elasticsearch
---

# PromQL reference [promql-language]

The [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/) is a functional query language to select and aggregate metrics.


## What is PromQL in Elasticsearch? [promql-what]

Elasticsearch supports PromQL queries for metrics in [time series data streams](docs-content://manage-data/data-store/data-streams/time-series-data-stream-tsds.md) (TSDS).
PromQL support is not limited to metrics ingested through [Prometheus remote write](docs-content://manage-data/data-store/data-streams/tsds-ingest-prometheus-remote-write.md).
All TSDS are supported, including metrics ingested through [OpenTelemetry Protocol (OTLP)](docs-content://manage-data/data-store/data-streams/tsds-ingest-otlp.md), and the [bulk API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk).

Elasticsearch supports PromQL in two ways: through a [Prometheus-compatible HTTP API](promql/promql-http-api.md) (for Prometheus-compatible clients) and as a [`PROMQL` source command](/reference/query-languages/esql/commands/promql.md) inside piped ES|QL queries that allow post-processing through regular ES|QL.

## How does it work? [promql-how]

When you use the Prometheus-compatible HTTP API or embed PromQL in an ES|QL query through the `PROMQL` source command, Elasticsearch parses PromQL into ES|QL logical plans and evaluates those plans against TSDS metrics.

Elasticsearch uses the same ES|QL compute engine for PromQL as for the [`TS` source command](/reference/query-languages/esql/commands/ts.md).

## In this section

* [HTTP API](promql/promql-http-api.md): Prometheus-compatible `/_prometheus/` endpoints for queries and discovery.
* [Functions](promql/functions.md): PromQL function reference organized by category, including Elasticsearch-specific differences from Prometheus.
* [Operators](promql/operators.md): PromQL operator reference organized by category, including Elasticsearch-specific differences from Prometheus.
* [Prometheus data source in Grafana](promql/promql-grafana.md): Use Elasticsearch as a Prometheus data source in Grafana for dashboards, autocomplete, and Metrics Drilldown.
* [Limitations](promql/promql-limitations.md): How behavior differs from Prometheus, including unsupported PromQL constructs, HTTP behavior, instant-query nuances, staleness semantics, exemplars, and related topics.

