<!-- Part 5 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## URL format

The main differences between URL formats of cluster and [Single server](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/)
versions are that cluster has separate components for read and ingestion path, and because of multi-tenancy support.
Also in the cluster version the `/prometheus/api/v1` endpoint ingests  `jsonl`, `csv`, `native` and `prometheus` data formats **not** only `prometheus` data.

> Check practical examples of [VictoriaMetrics API](https://docs.victoriametrics.com/victoriametrics/url-examples/).

- URLs for data ingestion via `vminsert`: `http://<vminsert>:8480/insert/<accountID>/<suffix>`, where:
  - `<accountID>` is an arbitrary 32-bit integer identifying namespace for data ingestion (aka tenant). It is possible to set it as `accountID:projectID`,
    where `projectID` is also arbitrary 32-bit integer. If `projectID` isn't set, then it equals to `0`. See [multitenancy docs](#multitenancy) for more details
    about managing tenants, specifying tenant IDs via HTTP headers or labels.
  - `<suffix>` may have the following values:
    - `prometheus` and `prometheus/api/v1/write` - for ingesting data with [Prometheus remote write API](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write).
    - `prometheus/api/v1/import` - for importing data obtained via `api/v1/export` at `vmselect` (see below), JSON line format.
    - `prometheus/api/v1/import/native` - for importing data obtained via `api/v1/export/native` on `vmselect` (see below).
    - `prometheus/api/v1/import/csv` - for importing arbitrary CSV data. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-csv-data) for details.
    - `prometheus/api/v1/import/prometheus` - for importing data in [Prometheus text exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/#prometheus-text-format) and in [OpenMetrics format](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md). This endpoint also supports [Pushgateway protocol](https://github.com/prometheus/pushgateway#url). See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-prometheus-exposition-format) for details.
    - `opentelemetry/v1/metrics` - for ingesting data via [OpenTelemetry protocol for metrics](https://github.com/open-telemetry/opentelemetry-specification/blob/97c826b70e2f89cfdf655d5150791f3f0c2bae19/specification/metrics/data-model.md). See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/).
    - `datadog/api/v1/series` - for ingesting data with DataDog submit metrics API v1. See [these docs](https://docs.victoriametrics.com/victoriametrics/url-examples/#datadogapiv1series) for details.
    - `datadog/api/v2/series` - for ingesting data with [DataDog submit metrics API](https://docs.datadoghq.com/api/latest/metrics/#submit-metrics). See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/) for details.
    - `datadog/api/beta/sketches` - for ingesting data with [DataDog lambda extension](https://docs.datadoghq.com/serverless/libraries_integrations/extension/).
    - `influx/write` and `influx/api/v2/write` - for ingesting data with [InfluxDB line protocol](https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_tutorial/). TCP and UDP receiver is disabled by default. It is exposed on a distinct TCP address set via `-influxListenAddr` command-line flag. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/) for details.
    - `newrelic/infra/v2/metrics/events/bulk` - for accepting data from [NewRelic infrastructure agent](https://docs.newrelic.com/docs/infrastructure/install-infrastructure-agent). See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/newrelic/#sending-data-from-agent) for details.
    - `opentsdb/api/put` - for accepting [OpenTSDB HTTP /api/put requests](http://opentsdb.net/docs/build/html/api_http/put.html). This handler is disabled by default. It is exposed on a distinct TCP address set via `-opentsdbHTTPListenAddr` command-line flag. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-http) for details.

- URLs for data ingestion via `vmstorage`: `http://<vmstorage>:8482/insert/<accountID>/<suffix>`.
  Direct ingestion into `vmstorage` is disabled by default. It can be enabled with the `-enableIngestionAPI`
  command-line flag.
  - `<accountID>` is an arbitrary 32-bit integer identifying namespace for data ingestion (aka tenant). It is possible to set it as `accountID:projectID`,
    where `projectID` is also arbitrary 32-bit integer. If `projectID` isn't set, then it equals to `0`. See [multitenancy docs](#multitenancy) for more details
    about managing tenants, specifying tenant IDs via HTTP headers or labels.
  - `<suffix>` may have the following values:
    - `prometheus`, `prometheus/api/v1/write` and `prometheus/api/v1/push` - for ingesting data with Prometheus remote write API.

- URLs for [Prometheus querying API](https://prometheus.io/docs/prometheus/latest/querying/api/): `http://<vmselect>:8481/select/<accountID>/prometheus/<suffix>`, where:
  - `<accountID>` is an arbitrary number identifying data namespace for the query (aka tenant). See [multitenancy docs](#multitenancy) for more details
    about managing tenants, specifying tenant IDs via HTTP headers or labels.
  - `<suffix>` may have the following values:
    - `api/v1/query` - performs [PromQL instant query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query).
    - `api/v1/query_range` - performs [PromQL range query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
    - `api/v1/series` - performs [series query](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series).
    - `api/v1/labels` - returns a [list of label names](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels).
    - `api/v1/label/<label_name>/values` - returns values for the given `<label_name>` according [to the API](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues).
    - `federate` - returns [federated metrics](https://prometheus.io/docs/prometheus/latest/federation/).
    - `api/v1/export` - exports raw data in JSON line format. See [this article](https://medium.com/@valyala/analyzing-prometheus-data-with-external-tools-5f3e5e147639) for details.
    - `api/v1/export/native` - exports raw data in native binary format. It may be imported into another VictoriaMetrics via `api/v1/import/native` (see above).
    - `api/v1/export/csv` - exports data in CSV. It may be imported into another VictoriaMetrics via `api/v1/import/csv` (see above).
    - `api/v1/series/count` - returns the total number of series.
    - `api/v1/status/tsdb` - for time series stats. See [these docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#tsdb-stats) for details.
    - `api/v1/status/active_queries` - for currently executed active queries. Note that every `vmselect` maintains an independent list of active queries,
      which is returned in the response.
    - `api/v1/status/top_queries` - for listing the most frequently executed queries and queries taking the most duration.
    - `api/v1/metadata` - for fetching [metrics metadata](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-metric-metadata). See [these docs](#metrics-metadata) for more details.
    - `metric-relabel-debug` - for debugging [relabeling rules](https://docs.victoriametrics.com/victoriametrics/relabeling/).

- URLs for [Graphite Metrics API](https://graphite-api.readthedocs.io/en/latest/api.html#the-metrics-api): `http://<vmselect>:8481/select/<accountID>/graphite/<suffix>`, where:
  - `<accountID>` is an arbitrary number identifying data namespace for query (aka tenant).
    See [multitenancy docs](#multitenancy) for more details about managing tenants, specifying tenant IDs via HTTP headers or labels.
  - `<suffix>` may have the following values:
    - `render` - implements Graphite Render API. See [these docs](https://graphite.readthedocs.io/en/stable/render_api.html).
    - `metrics/find` - searches Graphite metrics. See [these docs](https://graphite-api.readthedocs.io/en/latest/api.html#metrics-find).
    - `metrics/expand` - expands Graphite metrics. See [these docs](https://graphite-api.readthedocs.io/en/latest/api.html#metrics-expand).
    - `metrics/index.json` - returns all the metric names. See [these docs](https://graphite-api.readthedocs.io/en/latest/api.html#metrics-index-json).
    - `tags/tagSeries` - registers time series. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#adding-series-to-the-tagdb).
    - `tags/tagMultiSeries` - register multiple time series. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#adding-series-to-the-tagdb).
    - `tags` - returns tag names. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#exploring-tags).
    - `tags/<tag_name>` - returns tag values for the given `<tag_name>`. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#exploring-tags).
    - `tags/findSeries` - returns series matching the given `expr`. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#exploring-tags).
    - `tags/autoComplete/tags` - returns tags matching the given `tagPrefix` and/or `expr`. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#auto-complete-support).
    - `tags/autoComplete/values` - returns tag values matching the given `valuePrefix` and/or `expr`. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#auto-complete-support).
    - `tags/delSeries` - deletes series matching the given `path`. See [these docs](https://graphite.readthedocs.io/en/stable/tags.html#removing-series-from-the-tagdb).

- URL with basic Web UI: `http://<vmselect>:8481/select/<accountID>/vmui/`.

- URL for query stats across all tenants: `http://<vmselect>:8481/api/v1/status/top_queries`. It lists with the most frequently executed queries and queries taking the most duration.

- URL for time series deletion: `http://<vmselect>:8481/delete/<accountID>/prometheus/api/v1/admin/tsdb/delete_series?match[]=<timeseries_selector_for_delete>`.
  Note that the `delete_series` handler should be used only in exceptional cases such as deletion of accidentally ingested incorrect time series. It shouldn't
  be used on a regular basis, since it carries non-zero overhead.

- URL for listing [tenants](#multitenancy) with the ingested data on the given time range: `http://<vmselect>:8481/admin/tenants?start=...&end=...`.
  The `start` and `end` query args must be specified together. If both are missing, then only the tenants for the current day are returned.
  In order to get all tenants, specify both `start` and `end` so that the resulting time range includes the entire `-retentionPeriod`.

- URL for accessing [vmalerts](https://docs.victoriametrics.com/victoriametrics/vmalert/) UI: `http://<vmselect>:8481/select/<accountID>/prometheus/vmalert/`.
  This URL works only when `-vmalert.proxyURL` flag is set. See more about [vmalert](#vmalert).

- `vmstorage` nodes provide the following HTTP endpoints on `8482` port:
  - `/internal/force_merge` - initiate [forced compactions](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#forced-merge) on the given `vmstorage` node.
  - `/internal/force_flush` - [flush in-memory buffers](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#forced-flush) for recently ingested samples into searchable parts on the given `vmstorage` node.
  - `/snapshot/create` - create [instant snapshot](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282),
    which can be used for backups in background. Snapshots are created in `<storageDataPath>/snapshots` folder, where `<storageDataPath>` is the corresponding
    command-line flag value.
  - `/snapshot/list` - list available snapshots.
  - `/snapshot/delete?snapshot=<id>` - delete the given snapshot.
  - `/snapshot/delete_all` - delete all the snapshots.

  Snapshots may be created independently on each `vmstorage` node. There is no need in synchronizing snapshots' creation
  across `vmstorage` nodes.
