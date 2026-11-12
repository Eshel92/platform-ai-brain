<!-- Part 4 of 13 of victoriametrics/README.md (split because the page is big). -->

## Forced merge

VictoriaMetrics performs [data compaction in background](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282)
to keep high performance during ingestion. These compactions (merges) are performed independently on per-month partitions.
Partitions that don't receive new data will eventually stop being merged, as they reach an optimal state.
Sometimes it is necessary to trigger merges for old partitions. For example, to free up disk space occupied by [deleted time series](https://docs.victoriametrics.com/victoriametrics/#how-to-delete-time-series).
The user can **force** compaction on the specified per-month partition by sending a request to `/internal/force_merge?partition_prefix=YYYY_MM`,
where `YYYY_MM` is the per-month partition name. For example, `http://victoriametrics:8428/internal/force_merge?partition_prefix=2020_08` would initiate a forced
merge for the August 2020 partition. The call to `/internal/force_merge` returns immediately, while the corresponding forced merge continues running in the background.

Forced merges may require additional CPU, disk I/O, and storage space. It is unnecessary to run a forced merge under normal conditions,
since VictoriaMetrics automatically performs [optimal merges in background](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282)
when new data is ingested into it.

The `/internal/force_merge` endpoint can be protected from unauthorized access via the `--forceMergeAuthKey` command-line flag.
See [General security recommendations](https://docs.victoriametrics.com/victoriametrics/#general-security-recommendations) for more details.


## Forced flush

VictoriaMetrics puts the recently [ingested samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#write-data) into in-memory buffers,
which aren't available for [querying](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-data) for up to a few seconds.
If you need to query the samples immediately after they are ingested, then call the `/internal/force_flush` HTTP endpoint before running your query.
This endpoint converts in-memory buffers containing recently ingested samples into searchable data blocks.

It isn't recommended to force flush on a regular basis, as this increases CPU usage and slows data ingestion.
The `/internal/force_flush` endpoint exists for debug and test purposes (for instance, for automated tests) and should be avoided in production.

> VictoriaMetrics may intentionally hide samples with timestamps close to the current time during querying.
> This behavior is controlled via `-search.latencyOffset` command-line flag. See more details in [Query latency](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-latency) documentation.

The `/internal/force_flush` endpoint can be protected from unauthorized access via `-forceFlushAuthKey` command-line flag.
See [General security recommendations](https://docs.victoriametrics.com/victoriametrics/#general-security-recommendations) for more details.


## How to export time series

VictoriaMetrics provides the following handlers for exporting data:

* `/api/v1/export` for exporting data in JSON line format. See [these docs](#how-to-export-data-in-json-line-format) for details.
* `/api/v1/export/csv` for exporting data in CSV. See [these docs](#how-to-export-csv-data) for details.
* `/api/v1/export/native` for exporting data in native binary format. This is the most efficient format for data export.
  See [these docs](#how-to-export-data-in-native-format) for details.

### How to export data in JSON line format

Send a request to `http://<victoriametrics-addr>:8428/api/v1/export?match[]=<timeseries_selector_for_export>`,
where `<timeseries_selector_for_export>` may contain any [time series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors)
for metrics to export. Use `{__name__!=""}` selector for fetching all the time series.

The response would contain all the data for the selected time series in JSON line format - see [these docs](#json-line-format) for details on this format.

Each JSON line contains samples for a single time series. An example output:

```json
{"metric":{"__name__":"up","job":"node_exporter","instance":"localhost:9100"},"values":[0,0,0],"timestamps":[1549891472010,1549891487724,1549891503438]}
{"metric":{"__name__":"up","job":"prometheus","instance":"localhost:9090"},"values":[1,1,1],"timestamps":[1549891461511,1549891476511,1549891491511]}
```

Optional `start` and `end` args may be added to the request in order to limit the time frame for the exported data.
See [allowed formats](#timestamp-formats) for these args.

For example:

```sh
curl http://<victoriametrics-addr>:8428/api/v1/export -d 'match[]=<timeseries_selector_for_export>' -d 'start=1654543486' -d 'end=1654543486'
curl http://<victoriametrics-addr>:8428/api/v1/export -d 'match[]=<timeseries_selector_for_export>' -d 'start=2022-06-06T19:25:48' -d 'end=2022-06-06T19:29:07'
```

Optional `max_rows_per_line` arg may be added to the request for limiting the maximum number of rows exported per each JSON line.
Optional `reduce_mem_usage=1` arg may be added to the request for reducing memory usage when exporting big number of time series.
In this case the output may contain multiple lines with samples for the same time series.

Pass `Accept-Encoding: gzip` HTTP header in the request to `/api/v1/export` in order to reduce network bandwidth during exporting big amounts
of time series data. This enables gzip compression for the exported data. Example for exporting gzipped data:

```sh
curl -H 'Accept-Encoding: gzip' http://localhost:8428/api/v1/export -d 'match[]={__name__!=""}' > data.jsonl.gz
```

The maximum duration for each request to `/api/v1/export` is limited by `-search.maxExportDuration` command-line flag.

Exported data can be imported via POST'ing it to [/api/v1/import](#how-to-import-data-in-json-line-format).

By default, data exported via `/api/v1/export` is deduplicated according to [-dedup.minScrapeInterval](#deduplication) setting.
Pass GET param `reduce_mem_usage=1` in export request to disable deduplication for recently written data.
After [background merges](#storage) deduplication becomes permanent.

### How to export CSV data

Send a request to `http://<victoriametrics-addr>:8428/api/v1/export/csv?format=<format>&match=<timeseries_selector_for_export>`,
where:

* `<format>` must contain comma-delimited label names for the exported CSV. The following special label names are supported:
  * `__name__` - metric name
  * `__value__` - sample value
  * `__timestamp__:<ts_format>` - sample timestamp. `<ts_format>` can have the following values:
    * `unix_s` - unix seconds
    * `unix_ms` - unix milliseconds
    * `unix_ns` - unix nanoseconds
    * `rfc3339` - [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) time (in the timezone of the server)
    * `custom:<layout>` - custom layout for time that is supported by [time.Format](https://golang.org/pkg/time/#Time.Format) function from Go.

* `<timeseries_selector_for_export>` may contain any [time series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors)
for metrics to export.

Optional `start` and `end` args may be added to the request in order to limit the time frame for the exported data.
See [allowed formats](#timestamp-formats) for these args.

For example:

```sh
curl http://<victoriametrics-addr>:8428/api/v1/export/csv -d 'format=<format>' -d 'match[]=<timeseries_selector_for_export>' -d 'start=1654543486' -d 'end=1654543486'
curl http://<victoriametrics-addr>:8428/api/v1/export/csv -d 'format=<format>' -d 'match[]=<timeseries_selector_for_export>' -d 'start=2022-06-06T19:25:48' -d 'end=2022-06-06T19:29:07'
```

The exported CSV data can be imported to VictoriaMetrics via [/api/v1/import/csv](#how-to-import-csv-data).
The first line of the file is a header row derived from the `format` parameter.

The [deduplication](#deduplication) is applied for the data exported in CSV by default. It is possible to export raw data without de-duplication by passing `reduce_mem_usage=1` query arg to `/api/v1/export/csv`.

### How to export data in native format

Send a request to `http://<victoriametrics-addr>:8428/api/v1/export/native?match[]=<timeseries_selector_for_export>`,
where `<timeseries_selector_for_export>` may contain any [time series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors)
for metrics to export. Use `{__name__=~".*"}` selector for fetching all the time series.

On large databases you may experience problems with limit on the number of time series, which can be exported. In this case you need to adjust `-search.maxExportSeries` command-line flag:

```sh
# count unique time series in database
wget -O- -q 'http://your_victoriametrics_instance:8428/api/v1/series/count' | jq '.data[0]'

# relaunch victoriametrics with search.maxExportSeries more than value from previous command
```

Optional `start` and `end` args may be added to the request in order to limit the time frame for the exported data.
See [allowed formats](#timestamp-formats) for these args.

For example:

```sh
curl http://<victoriametrics-addr>:8428/api/v1/export/native -d 'match[]=<timeseries_selector_for_export>' -d 'start=1654543486' -d 'end=1654543486'
curl http://<victoriametrics-addr>:8428/api/v1/export/native -d 'match[]=<timeseries_selector_for_export>' -d 'start=2022-06-06T19:25:48' -d 'end=2022-06-06T19:29:07'
```

The exported data can be imported to VictoriaMetrics via [/api/v1/import/native](#how-to-import-data-in-native-format).
The native export format may change in incompatible way between VictoriaMetrics releases, so the data exported from the release X
can fail to be imported into VictoriaMetrics release Y.

The [deduplication](#deduplication) isn't applied for the data exported in native format. It is expected that the de-duplication is performed during data import.
