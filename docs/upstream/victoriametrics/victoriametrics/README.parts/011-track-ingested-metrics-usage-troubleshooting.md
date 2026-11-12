<!-- Part 11 of 13 of victoriametrics/README.md (split because the page is big). -->

## Track ingested metrics usage

VictoriaMetrics can track statistics of fetched [metric names](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#structure-of-a-metric)
during [querying](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-data) {{% available_from "v1.113.0" %}}. It tracks
only metric names, as the number of names is usually limited (thousands) compared to time series (millions or billions).
This feature can be disabled via the flag `--storage.trackMetricNamesStats=false` (**enabled by default**) on a single-node
VictoriaMetrics or [vmstorage](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#architecture-overview).

During querying, VictoriaMetrics tracks how many times the requested metric name was fetched from the database and
when was the last time it happened. In this way, it is possible to identify metric names that were never queried.
Or if metric was queried occasionally - when the last time it happened.

The usage stats for a metric won't update in these two cases:

* Querying a metric with non-matching filters. For example, querying for `vm_log_messages_total{level!="info"}` won't update usage stats
  for `vm_log_messages_total` if there is no `{level!="info"}` series yet.
* The query response is fully cached in the [rollup result cache](https://docs.victoriametrics.com/victoriametrics/#rollup-result-cache).

To get metric names usage statistics, use the `/prometheus/api/v1/status/metric_names_stats` API endpoint for
a single-node VictoriaMetrics (or at `http://<vmselect>:8481/select/<accountID>/prometheus/api/v1/status/metric_names_stats` in [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/)).
It accepts the following query parameters:

* `limit` - integer value to limit the number of metric names in response. By default, API returns 1000 records.
* `le` - `less than or equal`, is an integer threshold for filtering metric names by their usage count in queries.
  For example, with `?le=1` API returns metric names that were queried <=1 times.
* `match_pattern` - a regex pattern to match metric names. For example, `?match_pattern=vm_` will match any metric
  names with `vm_` pattern, like `vm_http_requests`, `max_vm_memory_available`.

The API endpoint returns the following `JSON` response:

```json
{
  "status": "success",
  "statsCollectedSince": 1737534094,
  "statsCollectedRecordsTotal": 2,
  "records": [
    {
      "metricName": "node_disk_writes_completed_total",
      "queryRequestsCount": 50,
      "lastRequestTimestamp": 1737534262
    },
    {
      "metricName": "node_network_transmit_errs_total",
      "queryRequestsCount": 100,
      "lastRequestTimestamp": 1737534262
    }
  ]
}
```

* `statsCollectedSince` is a timestamp since tracker was enabled (or reset, see below);
* `statsCollectedRecordsTotal` total number of metric names it contains;
* `records`:
  * `metricName` a metric name;
  * `queryRequestsCount` a cumulative counter of times the metric was fetched. If metric name `foo` has 10 time series,
    then one read query `foo` will increment counter by 10.
  * `lastRequestTimestamp` a timestamp when last time this statistic was updated.

**VictoriaMetrics tracks metric names query statistics for `/api/v1/query`, `/api/v1/query_range`, `/render`, `/federate` and `/api/v1/export` API calls.**

VictoriaMetrics stores tracked metric names in memory and saves the state to disk in the `<-storageDataPath>/cache` folder during restarts.
The size of the in-memory state is limited to **1%** of the available memory by default.
This limit can be adjusted using the `-storage.cacheSizeMetricNamesStats` flag.

When the maximum state capacity is reached, VictoriaMetrics will stop tracking stats for newly registered time series.
However, read request statistics for already tracked time series will continue to work as expected.

VictoriaMetrics exposes the following metrics for the metric name tracker:

* `vm_cache_size_bytes{type="storage/metricNamesStatsTracker"}`
* `vm_cache_size{type="storage/metricNamesStatsTracker"}`
* `vm_cache_size_max_bytes{type="storage/metricNamesStatsTracker"}`

An alerting rule with query `vm_cache_size_bytes{type="storage/metricNamesStatsTracker"} \ vm_cache_size_max_bytes{type="storage/metricNamesStatsTracker"} > 0.9`
can be used to notify the user of cache utilization exceeding 90%.

The metric name tracker state can be **reset** via the API endpoint `/api/v1/admin/status/metric_names_stats/reset`
for a single-node VictoriaMetrics (or at `http://<vmselect>:8481/admin/api/v1/admin/status/metric_names_stats/reset`
in [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/)) or
via [cache removal](https://docs.victoriametrics.com/victoriametrics/#cache-removal) procedure. This reset state endpoint can be protected via `-metricNamesStatsResetAuthKey`
cmd-line flag. See [Security](https://docs.victoriametrics.com/victoriametrics/#security) for details.

See [skills/victoriametrics-unused-metrics-analysis](https://github.com/VictoriaMetrics/skills/blob/main/plugins/diagnostics/skills/victoriametrics-unused-metrics-analysis/SKILL.md)
for [agent-assisted](https://docs.victoriametrics.com/ai-tools/#agent-skills) analysis of unused metrics.


## Query tracing

VictoriaMetrics supports query tracing, which can be used for determining bottlenecks during query processing.
This is like `EXPLAIN ANALYZE` from Postgresql.

Query tracing can be enabled for a specific query by passing `trace=1` query arg.
In this case VictoriaMetrics puts query trace into `trace` field in the output JSON.

For example, the following command:

```sh
curl http://localhost:8428/api/v1/query_range -d 'query=2*rand()' -d 'start=-1h' -d 'step=1m' -d 'trace=1' | jq '.trace'
```

would return the following trace:

```json
{
  "duration_msec": 0.099,
  "message": "/api/v1/query_range: start=1654034340000, end=1654037880000, step=60000, query=\"2*rand()\": series=1",
  "children": [
    {
      "duration_msec": 0.034,
      "message": "eval: query=2 * rand(), timeRange=[1654034340000..1654037880000], step=60000, mayCache=true: series=1, points=60, pointsPerSeries=60",
      "children": [
        {
          "duration_msec": 0.032,
          "message": "binary op \"*\": series=1",
          "children": [
            {
              "duration_msec": 0.009,
              "message": "eval: query=2, timeRange=[1654034340000..1654037880000], step=60000, mayCache=true: series=1, points=60, pointsPerSeries=60"
            },
            {
              "duration_msec": 0.017,
              "message": "eval: query=rand(), timeRange=[1654034340000..1654037880000], step=60000, mayCache=true: series=1, points=60, pointsPerSeries=60",
              "children": [
                {
                  "duration_msec": 0.015,
                  "message": "transform rand(): series=1"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "duration_msec": 0.004,
      "message": "sort series by metric name and labels"
    },
    {
      "duration_msec": 0.044,
      "message": "generate /api/v1/query_range response for series=1, points=60"
    }
  ]
}
```

All the durations and timestamps in traces are in milliseconds.

Query tracing is allowed by default. It can be denied by passing `-denyQueryTracing` command-line flag to VictoriaMetrics.

[VMUI](#vmui) provides an UI:

* for query tracing - just click `Trace query` checkbox and re-run the query in order to investigate its' trace.
* for exploring custom trace - go to the tab `Trace analyzer` and upload or paste JSON with trace information.

See also [skills/vm-trace-analyzer](https://github.com/VictoriaMetrics/skills/blob/main/plugins/diagnostics/skills/vm-trace-analyzer/SKILL.md)
for [agent-assisted](https://docs.victoriametrics.com/ai-tools/#agent-skills) analysis.


## Cardinality limiter

By default, VictoriaMetrics doesn't limit the number of stored time series. The limit can be enforced by setting the following command-line flags:

* `-storage.maxHourlySeries` - limits the number of time series that can be added during the last hour. Useful for limiting the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series).
* `-storage.maxDailySeries` - limits the number of time series that can be added during the last day. Useful for limiting daily [churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).

Both limits can be set simultaneously. If any of these limits is reached, then incoming samples for new time series are dropped. A sample of dropped series is put in the log with `WARNING` level.

It is possible to use `-1` as a value for these flags{{% available_from "v1.140.0" %}} in order to enable series tracking but set limit to maximum possible value.
This is useful in order to estimate the number of unique series which is written to VictoriaMetrics single without enforcing limits.

The exceeded limits can be [monitored](#monitoring) with the following metrics:

* `vm_hourly_series_limit_rows_dropped_total` - the number of metrics dropped due to exceeded hourly limit on the number of unique time series.

* `vm_hourly_series_limit_max_series` - the hourly series limit set via `-storage.maxHourlySeries` command-line flag.

* `vm_hourly_series_limit_current_series` - the current number of unique series during the last hour.
  The following query can be useful for alerting when the number of unique series during the last hour exceeds 90% of the `-storage.maxHourlySeries`:

  ```metricsql
  vm_hourly_series_limit_current_series / vm_hourly_series_limit_max_series > 0.9
  ```

* `vm_daily_series_limit_rows_dropped_total` - the number of metrics dropped due to exceeded daily limit on the number of unique time series.

* `vm_daily_series_limit_max_series` - the daily series limit set via `-storage.maxDailySeries` command-line flag.

* `vm_daily_series_limit_current_series` - the current number of unique series during the last day.
  The following query can be useful for alerting when the number of unique series during the last day exceeds 90% of the `-storage.maxDailySeries`:

  ```metricsql
  vm_daily_series_limit_current_series / vm_daily_series_limit_max_series > 0.9
  ```

These limits are approximate, so VictoriaMetrics can underflow/overflow the limit by a small percentage (usually less than 1%).

See also:
- [vmagent - Cardinality Limiter](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter).
- [Cardinality Explorer](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-explorer).
- [vmestimator](https://docs.victoriametrics.com/victoriametrics/vmestimator/).


## Troubleshooting

* It is recommended to use default command-line flag values (i.e. don't set them explicitly) until the need
  of tweaking these flag values arises.

* It is recommended inspecting logs during troubleshooting, since they may contain useful information.

* It is recommended upgrading to the latest available release from [this page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest),
  since the encountered issue could be already fixed there.

* It is recommended to have at least 50% of spare resources for CPU, disk IO and RAM, so VictoriaMetrics could handle short spikes in the workload without performance issues.

* VictoriaMetrics requires free disk space for [merging data files to bigger ones](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).
  It may slow down when there is no enough free space left. So make sure `-storageDataPath` directory
  has at least 20% of free space. The remaining amount of free space
  can be [monitored](#monitoring) via `vm_free_disk_space_bytes` metric. The total size of data
  stored on the disk can be monitored via sum of `vm_data_size_bytes` metrics.

* If you run VictoriaMetrics on a host with 16 or more CPU cores, then it may be needed to tune the `-search.maxWorkersPerQuery` command-line flag
  in order to improve query performance. If VictoriaMetrics serves big number of concurrent `select` queries, then try reducing the value for this flag.
  If VictoriaMetrics serves heavy queries, which select `>10K` of [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series) and/or process `>100M`
  of [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples) per query, then try setting the value for this flag to the number of available CPU cores.

* VictoriaMetrics buffers incoming data in memory for up to a few seconds before flushing it to persistent storage.
  This may lead to the following "issues":
  * Data becomes available for querying in a few seconds after inserting. It is possible to flush in-memory buffers to searchable parts
    by requesting `/internal/force_flush` http handler. This handler is mostly needed for testing and debugging purposes.
  * The last few seconds of inserted data may be lost on unclean shutdown (i.e. OOM, `kill -9` or hardware reset).
    The `-inmemoryDataFlushInterval` command-line flag allows controlling the frequency of in-memory data flush to persistent storage.
    See [storage docs](#storage) and [this article](https://valyala.medium.com/wal-usage-looks-broken-in-modern-time-series-databases-b62a627ab704) for more details.

* If VictoriaMetrics works slowly and eats more than a CPU core per 100K ingested data points per second,
  then it is likely you have too many [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series) for the current amount of RAM.
  VictoriaMetrics [exposes](#monitoring) `vm_slow_*` metrics such as `vm_slow_row_inserts_total` and `vm_slow_metric_name_loads_total`, which could be used
  as an indicator of low amounts of RAM. It is recommended increasing the amount of RAM on the node with VictoriaMetrics in order to improve
  ingestion and query performance in this case.

* If the order of labels for the same metrics can change over time (e.g. if `metric{k1="v1",k2="v2"}` may become `metric{k2="v2",k1="v1"}`),
  then it is recommended running VictoriaMetrics with `-sortLabels` command-line flag in order to reduce memory usage and CPU usage.

* VictoriaMetrics prioritizes data ingestion over data querying. So if it has no enough resources for data ingestion,
  then data querying may slow down significantly.

* If VictoriaMetrics doesn't work because of certain parts are corrupted due to disk errors,
  then just remove directories with broken parts. It is safe removing subdirectories under `<-storageDataPath>/data/{big,small}/YYYY_MM` directories
  when VictoriaMetrics isn't running. This recovers VictoriaMetrics at the cost of data loss stored in the deleted broken parts.
  The names of broken parts should be present in the error message. If you see that error message is truncated and doesn't contain all the information
  try increasing `-loggerMaxArgLen` cmd-line flag to higher values to avoid error messages truncation.

* If you see gaps on the graphs, try resetting the cache by sending request to `/internal/resetRollupResultCache`.
  If this removes gaps on the graphs, then it is likely data with timestamps older than `-search.cacheTimestampOffset`
  is ingested into VictoriaMetrics. Make sure that data sources have synchronized time with VictoriaMetrics.

  If the gaps are related to irregular intervals between samples, then try adjusting `-search.minStalenessInterval` command-line flag
  to value close to the maximum interval between samples.

* If you are switching from InfluxDB or TimescaleDB, then it may be needed to set `-search.setLookbackToStep` command-line flag.
  This suppresses default gap filling algorithm used by VictoriaMetrics - by default it assumes
  each time series is continuous instead of discrete, so it fills gaps between real samples with regular intervals.

* Metrics and labels leading to [high cardinality](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-cardinality)
  or [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate) can be determined
  via [cardinality explorer](#cardinality-explorer) and via [/api/v1/status/tsdb](#tsdb-stats) endpoint.

* New time series can be logged if `-logNewSeries` command-line flag is passed to VictoriaMetrics or temporary enabled via `/internal/log_new_series` API call.
  `/internal/log_new_series` API accepts query parameter `seconds`, with default value of `60`, which defines a duration for logging newly created series.

* VictoriaMetrics limits the number of labels per each series, label name length and label value length
  via `-maxLabelsPerTimeseries`, `-maxLabelNameLen` and `-maxLabelValueLen` command-line flags respectively.
  Series that exceed the limits are ignored on ingestion. This prevents from ingesting malformed series.
  It is recommended [monitoring](#monitoring) `vm_rows_ignored_total` metric and VictoriaMetrics logs in order
  to determine whether limits must be adjusted for your workload.
  Alternatively, you can use [relabeling](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#relabeling) to change metric target labels.

* If you store Graphite metrics like `foo.bar.baz` in VictoriaMetrics, then `{__graphite__="foo.*.baz"}` filter can be used for selecting such metrics.
  See [these docs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#selecting-graphite-metrics) for details. You can also query Graphite metrics with [Graphite querying API](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api).

* VictoriaMetrics ignores `NaN` values during data ingestion.

See also:

* [Snapshot troubleshooting](#snapshot-troubleshooting).
* [General troubleshooting docs](https://docs.victoriametrics.com/victoriametrics/troubleshooting/).
