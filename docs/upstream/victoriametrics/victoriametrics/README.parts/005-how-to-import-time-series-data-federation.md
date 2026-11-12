<!-- Part 5 of 13 of victoriametrics/README.md (split because the page is big). -->

## How to import time series data

VictoriaMetrics can discover and scrape metrics from Prometheus-compatible targets (aka "pull" protocol) -
see [these docs](#how-to-scrape-prometheus-exporters-such-as-node-exporter).
Additionally, VictoriaMetrics can accept metrics via the following popular data ingestion protocols (aka "push" protocols):

* [Prometheus remote_write API](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write). See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/prometheus/) for details.
* DataDog `submit metrics` API. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/) for details.
* InfluxDB line protocol. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/#influxdb-compatible-agents-such-as-telegraf) for details.
* Graphite plaintext protocol. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting) for details.
* OpenTelemetry http API. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) for details.
* OpenTSDB telnet put protocol. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet) for details.
* OpenTSDB http `/api/put` protocol. See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-http) for details.
* `/api/v1/import` for importing data obtained from [/api/v1/export](#how-to-export-data-in-json-line-format).
  See [these docs](#how-to-import-data-in-json-line-format) for details.
* `/api/v1/import/native` for importing data obtained from [/api/v1/export/native](#how-to-export-data-in-native-format).
  See [these docs](#how-to-import-data-in-native-format) for details.
* `/api/v1/import/csv` for importing arbitrary CSV data. See [these docs](#how-to-import-csv-data) for details.
* `/api/v1/import/prometheus` for importing data in Prometheus exposition format and in [Pushgateway format](https://github.com/prometheus/pushgateway#url).
  See [these docs](#how-to-import-data-in-prometheus-exposition-format) for details.

Please note, most of the ingestion APIs (except [Prometheus remote_write API](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write), [OpenTelemetry](https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/) and [Influx Line Protocol](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/#influxdb-compatible-agents-such-as-telegraf))
are optimized for performance and processes data in a streaming fashion.
It means that client can transfer unlimited amount of data through the open connection. Because of this, import APIs
may not return parsing errors to the client, as it is expected for data stream to be not interrupted.
Instead, look for parsing errors on the server side (VictoriaMetrics single-node or vminsert) or
check for changes in `vm_rows_invalid_total` (exported by server side) metric.

### How to import data in JSON line format

VictoriaMetrics accepts metrics data in JSON line format at `/api/v1/import` endpoint. See [these docs](#json-line-format) for details on this format.

Example for importing data obtained via [/api/v1/export](#how-to-export-data-in-json-line-format):

```sh
# Export the data from <source-victoriametrics>:
curl http://source-victoriametrics:8428/api/v1/export -d 'match={__name__!=""}' > exported_data.jsonl

# Import the data to <destination-victoriametrics>:
curl -X POST http://destination-victoriametrics:8428/api/v1/import -T exported_data.jsonl
```

Pass `Content-Encoding: gzip` HTTP request header to `/api/v1/import` for importing gzipped data:

```sh
# Export gzipped data from <source-victoriametrics>:
curl -H 'Accept-Encoding: gzip' http://source-victoriametrics:8428/api/v1/export -d 'match={__name__!=""}' > exported_data.jsonl.gz

# Import gzipped data to <destination-victoriametrics>:
curl -X POST -H 'Content-Encoding: gzip' http://destination-victoriametrics:8428/api/v1/import -T exported_data.jsonl.gz
```

Extra labels may be added to all the imported time series by passing `extra_label=name=value` query args.
For example, `/api/v1/import?extra_label=foo=bar` would add `"foo":"bar"` label to all the imported time series.

Note that it could be required to flush response cache after importing historical data. See [these docs](#backfilling) for detail.

VictoriaMetrics parses input JSON lines one-by-one. It loads the whole JSON line in memory, then parses it and then saves the parsed samples into persistent storage.
This means that VictoriaMetrics can occupy big amounts of RAM when importing too long JSON lines.
The solution is to split too long JSON lines into shorter lines. It is OK if samples for a single time series are split among multiple JSON lines.
JSON line length can be limited via `max_rows_per_line` query arg when exporting via [/api/v1/export](#how-to-export-data-in-json-line-format).

The maximum JSON line length, which can be parsed by VictoriaMetrics, is limited by `-import.maxLineLen` command-line flag value.

### How to import data in native format

The specification of VictoriaMetrics' native format may yet change and is not formally documented yet. So currently we do not recommend that external clients attempt to pack their own metrics in native format file.

If you have a native format file obtained via [/api/v1/export/native](#how-to-export-data-in-native-format) however this is the most efficient protocol for importing data in.

```sh
# Export the data from <source-victoriametrics>:
curl http://source-victoriametrics:8428/api/v1/export/native -d 'match={__name__!=""}' > exported_data.bin

# Import the data to <destination-victoriametrics>:
curl -X POST http://destination-victoriametrics:8428/api/v1/import/native -T exported_data.bin
```

Extra labels may be added to all the imported time series by passing `extra_label=name=value` query args.
For example, `/api/v1/import/native?extra_label=foo=bar` would add `"foo":"bar"` label to all the imported time series.

Note that it could be required to flush response cache after importing historical data. See [these docs](#backfilling) for detail.

### How to import CSV data

Arbitrary CSV data can be imported via `/api/v1/import/csv`. The CSV data is imported according to the provided `format` query arg.
The `format` query arg must contain comma-separated list of parsing rules for CSV fields. Each rule consists of three parts delimited by a colon:

```text
<column_pos>:<type>:<context>
```

* `<column_pos>` is the position of the CSV column (field). Column numbering starts from 1. The order of parsing rules may be arbitrary.
* `<type>` describes the column type. Supported types are:
  * `metric` - the corresponding CSV column at `<column_pos>` contains metric value, which must be integer or floating-point number.
    The metric name is read from the `<context>`. CSV line must have at least a single metric field. Multiple metric fields per CSV line is OK.
  * `label` - the corresponding CSV column at `<column_pos>` contains label value. The label name is read from the `<context>`.
    CSV line may have arbitrary number of label fields. All these labels are attached to all the configured metrics.
  * `time` - the corresponding CSV column at `<column_pos>` contains metric time. CSV line may contain either one or zero columns with time.
    If CSV line has no time, then the current time is used. The time is applied to all the configured metrics.
    The format of the time is configured via `<context>`. Supported time formats are:
    * `unix_s` - unix timestamp in seconds.
    * `unix_ms` - unix timestamp in milliseconds.
    * `unix_ns` - unix timestamp in nanoseconds. Note that VictoriaMetrics rounds the timestamp to milliseconds.
    * `rfc3339` - timestamp in [RFC3339](https://tools.ietf.org/html/rfc3339) format, i.e. `2006-01-02T15:04:05Z`.
    * `custom:<layout>` - custom layout for the timestamp. The `<layout>` may contain arbitrary time layout according to [time.Parse rules in Go](https://golang.org/pkg/time/#Parse).

The first row is treated as a header but can be skipped if any `time` or `metric` column contains a non-numeric value.

Each request to `/api/v1/import/csv` may contain arbitrary number of CSV lines.

Example for importing CSV data via `/api/v1/import/csv`:

```sh
# Import via POST data:
curl -d "GOOG,1.23,4.56,NYSE" 'http://localhost:8428/api/v1/import/csv?format=2:metric:ask,3:metric:bid,1:label:ticker,4:label:market'
curl -d "MSFT,3.21,1.67,NASDAQ" 'http://localhost:8428/api/v1/import/csv?format=2:metric:ask,3:metric:bid,1:label:ticker,4:label:market'

# Import via file upload:
curl -X POST 'http://localhost:8428/api/v1/import/csv?format=2:metric:ask,3:metric:bid,1:label:ticker,4:label:market' -T exported_data.csv
```

After that the data may be read via [/api/v1/export](#how-to-export-data-in-json-line-format) endpoint:

```sh
curl -G 'http://localhost:8428/api/v1/export' -d 'match[]={ticker!=""}'
```

The following response should be returned:

```json
{"metric":{"__name__":"bid","market":"NASDAQ","ticker":"MSFT"},"values":[1.67],"timestamps":[1583865146520]}
{"metric":{"__name__":"bid","market":"NYSE","ticker":"GOOG"},"values":[4.56],"timestamps":[1583865146495]}
{"metric":{"__name__":"ask","market":"NASDAQ","ticker":"MSFT"},"values":[3.21],"timestamps":[1583865146520]}
{"metric":{"__name__":"ask","market":"NYSE","ticker":"GOOG"},"values":[1.23],"timestamps":[1583865146495]}
```

Extra labels may be added to all the imported lines by passing `extra_label=name=value` query args.
For example, `/api/v1/import/csv?extra_label=foo=bar` would add `"foo":"bar"` label to all the imported lines.

Note that it could be required to flush response cache after importing historical data. See [these docs](#backfilling) for detail.

### How to import data in Prometheus exposition format

VictoriaMetrics accepts data in [Prometheus exposition format](https://github.com/prometheus/docs/blob/main/docs/instrumenting/exposition_formats.md),
in [OpenMetrics format](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md)
and in [Pushgateway format](https://github.com/prometheus/pushgateway#url) via `/api/v1/import/prometheus` path.

For example, the following command imports a single line in Prometheus exposition format into VictoriaMetrics:

```sh
curl -d 'foo{bar="baz"} 123' -X POST 'http://localhost:8428/api/v1/import/prometheus'
```

The following command may be used for verifying the imported data:

```sh
curl -G 'http://localhost:8428/api/v1/export' -d 'match={__name__=~"foo"}'
```

It should return something like the following:

```json
{"metric":{"__name__":"foo","bar":"baz"},"values":[123],"timestamps":[1594370496905]}
```

The following command imports a single metric via [Pushgateway format](https://github.com/prometheus/pushgateway#url) with `{job="my_app",instance="host123"}` labels:

```sh
curl -d 'metric{label="abc"} 123' -X POST 'http://localhost:8428/api/v1/import/prometheus/metrics/job/my_app/instance/host123'
```

Pass `Content-Encoding: gzip` HTTP request header to `/api/v1/import/prometheus` for importing gzipped data:

```sh
# Import gzipped data to <destination-victoriametrics>:
curl -X POST -H 'Content-Encoding: gzip' http://destination-victoriametrics:8428/api/v1/import/prometheus -T prometheus_data.gz
```

Extra labels may be added to all the imported metrics either via [Pushgateway format](https://github.com/prometheus/pushgateway#url)
or by passing `extra_label=name=value` query args. For example, `/api/v1/import/prometheus?extra_label=foo=bar` would add `{foo="bar"}` label to all the imported metrics.

If timestamp is missing in `<metric> <value> <timestamp>` Prometheus exposition format line, then the current timestamp is used during data ingestion.
It can be overridden by passing unix timestamp in *milliseconds* via `timestamp` query arg. For example, `/api/v1/import/prometheus?timestamp=1594370496905`.

VictoriaMetrics accepts arbitrary number of lines in a single request to `/api/v1/import/prometheus`, i.e. it supports data streaming.

Note that it could be required to flush response cache after importing historical data. See [these docs](#backfilling) for detail.

VictoriaMetrics also may scrape Prometheus targets - see [these docs](#how-to-scrape-prometheus-exporters-such-as-node-exporter).


## JSON line format

VictoriaMetrics accepts data in JSON line format at [/api/v1/import](#how-to-import-data-in-json-line-format)
and exports data in this format at [/api/v1/export](#how-to-export-data-in-json-line-format).

The format follows [JSON streaming concept](https://jsonlines.org/), e.g. each line contains JSON object with metrics data in the following format:

```json
{
  // metric contains metric name plus labels for a particular time series
  "metric":{
    "__name__": "metric_name",  // <- this is metric name

    // Other labels for the time series

    "label1": "value1",
    "label2": "value2",
    ...
    "labelN": "valueN"
  },

  // values contains raw sample values for the given time series
  "values": [1, 2.345, -678],

  // timestamps contains raw sample UNIX timestamps in milliseconds for the given time series
  // every timestamp is associated with the value at the corresponding position
  "timestamps": [1549891472010,1549891487724,1549891503438]
}
```

Note that every JSON object must be written in a single line, e.g. all the newline chars must be removed from it.
[/api/v1/import](#how-to-import-data-in-json-line-format) handler doesn't accept JSON lines longer than the value
passed to `-import.maxLineLen` command-line flag (by default this is 10MB).

It is recommended passing 1K-10K samples per line for achieving the maximum data ingestion performance at [/api/v1/import](#how-to-import-data-in-json-line-format).
Too long JSON lines may increase RAM usage at VictoriaMetrics side.

[/api/v1/export](#how-to-export-data-in-json-line-format) handler accepts `max_rows_per_line` query arg, which allows limiting the number of samples per each exported line.

It is OK to split [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples)
for the same [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series) across multiple lines.

The number of lines in the request to [/api/v1/import](#how-to-import-data-in-json-line-format) can be arbitrary - they are imported in streaming manner.


## Relabeling

VictoriaMetrics supports Prometheus-compatible relabeling for all the ingested metrics if `-relabelConfig` command-line flag points
to a file containing a list of [relabel_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config) entries.
The `-relabelConfig` also can point to http or https url. For example, `-relabelConfig=https://config-server/relabel_config.yml`.

The following docs can be useful in understanding the relabeling:

* [Cookbook for common relabeling tasks](https://docs.victoriametrics.com/victoriametrics/relabeling/).
* [Relabeling tips and tricks](https://valyala.medium.com/how-to-use-relabeling-in-prometheus-and-victoriametrics-8b90fc22c4b2).

The `-relabelConfig` files can contain special placeholders in the form `%{ENV_VAR}`, which are replaced by the corresponding environment variable values.

Example contents for `-relabelConfig` file:

```yaml
# Add {cluster="dev"} label.
- target_label: cluster
  replacement: dev

# Drop the metric (or scrape target) with `{__meta_kubernetes_pod_container_init="true"}` label.
- action: drop
  source_labels: [__meta_kubernetes_pod_container_init]
  regex: true
```

VictoriaMetrics provides additional relabeling features such as Graphite-style relabeling.
See [these docs](https://docs.victoriametrics.com/victoriametrics/relabeling/) for more details.

The relabeling can be debugged at `http://victoriametrics:8428/metric-relabel-debug` page
or at our [public demo playground](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/relabeling).
See [these docs](https://docs.victoriametrics.com/victoriametrics/relabeling/#relabel-debugging) for more details.


## Federation

VictoriaMetrics exports [Prometheus-compatible federation data](https://prometheus.io/docs/prometheus/latest/federation/)
at `http://<victoriametrics-addr>:8428/federate?match[]=<timeseries_selector_for_federation>`.

Optional `start` and `end` args may be added to the request in order to scrape the last point for each selected time series on the `[start ... end]` interval.
See [allowed formats](#timestamp-formats) for these args.

For example:

```sh
curl http://<victoriametrics-addr>:8428/federate -d 'match[]=<timeseries_selector_for_export>' -d 'start=1654543486' -d 'end=1654543486'
curl http://<victoriametrics-addr>:8428/federate -d 'match[]=<timeseries_selector_for_export>' -d 'start=2022-06-06T19:25:48' -d 'end=2022-06-06T19:29:07'
```

By default, the last point on the interval `[now - max_lookback ... now]` is scraped for each time series. The default value for `max_lookback` is `5m` (5 minutes), but it can be overridden with `max_lookback` query arg.
For instance, `/federate?match[]=up&max_lookback=1h` would return last points on the `[now - 1h ... now]` interval. This may be useful for time series federation
with scrape intervals exceeding `5m`.

 VictoriaMetrics supports Prometheus v3.0 utf-8 content encoding with `Accept` header. If `Accept: allow-utf-8` HTTP header provided, `/federate` API response changes according to [Prometheus utf-8](https://prometheus.io/docs/guides/utf8/#querying) specification - `metric_name{tag="value"}` transforms into `{"metric_name","tag"="value"}`.
