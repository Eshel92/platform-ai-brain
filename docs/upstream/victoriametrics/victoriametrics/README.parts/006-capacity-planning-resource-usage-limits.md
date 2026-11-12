<!-- Part 6 of 13 of victoriametrics/README.md (split because the page is big). -->

## Capacity planning

VictoriaMetrics uses lower amounts of CPU, RAM and storage space on production workloads compared to competing solutions (Prometheus, Thanos, Cortex, TimescaleDB, InfluxDB, QuestDB, M3DB) according to [our case studies](https://docs.victoriametrics.com/victoriametrics/casestudies/).

VictoriaMetrics capacity scales linearly with the available resources. The needed amounts of CPU and RAM highly depends on the workload - the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series), series [churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate), query types, query qps, etc. It is recommended setting up a test VictoriaMetrics for your production workload and iteratively scaling CPU and RAM resources until it becomes stable according to [troubleshooting docs](#troubleshooting). A single-node VictoriaMetrics works perfectly with the following production workload according to [our case studies](https://docs.victoriametrics.com/victoriametrics/casestudies/):

* Ingestion rate: 1.5+ million samples per second
* Active time series: 50+ million
* Total time series: 5+ billion
* Time series churn rate: 150+ million of new series per day
* Total number of samples: 10+ trillion
* Queries: 200+ qps
* Query latency (99th percentile): 1 second

The needed storage space for the given retention (the retention is set via `-retentionPeriod` command-line flag) can be extrapolated from disk space usage in a test run. For example, if `-storageDataPath` directory size becomes 10GB after a day-long test run on a production workload, then it will need at least `10GB*100=1TB` of disk space for `-retentionPeriod=100d` (100-days retention period).

It is recommended leaving the following amounts of spare resources:

* 50% of free RAM for reducing the probability of OOM (out of memory) crashes. Exceeding 50% of free RAM may cause cache evictions, excessive I/O and overall slowdown (see [#9895-comment](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/9895#issuecomment-3442491150) for more details).
* 50% of spare CPU for reducing the probability of slowdowns during temporary spikes in workload.
* At least [20% of free storage space](#storage) at the directory pointed by `-storageDataPath` command-line flag. See also `-storage.minFreeDiskSpaceBytes` command-line [flag description](#list-of-command-line-flags).

See also [resource usage limits docs](#resource-usage-limits).


## Resource usage limits

By default, VictoriaMetrics is tuned for an optimal resource usage under typical workloads. Some workloads may need fine-grained resource usage limits. In these cases the following command-line flags may be useful:

* `-maxIngestionRate` limits samples/second ingested. This may be useful when CPU resources are limited or overloaded.
* `-memory.allowedPercent` and `-memory.allowedBytes` limit the amounts of memory, which may be used for various internal caches at VictoriaMetrics.
  Note that VictoriaMetrics may use more memory, since these flags don't limit additional memory, which may be needed on a per-query basis.
* `-search.maxMemoryPerQuery` limits the amounts of memory, which can be used for processing a single query. Queries, which need more memory, are rejected.
  Heavy queries, which select big number of time series, may exceed the per-query memory limit by a small percent. The total memory limit
  for concurrently executed queries can be estimated as `-search.maxMemoryPerQuery` multiplied by `-search.maxConcurrentRequests`.
* `-search.maxUniqueTimeseries` limits the number of unique time series a single query can find and process. By default, VictoriaMetrics calculates the limit automatically
  based on the available memory and the maximum number of concurrent requests it can process (see `-search.maxConcurrentRequests`). VictoriaMetrics keeps in memory
  some metainformation about the time series located by each query and spends some CPU time for processing the found time series.
  This means that the maximum memory usage and CPU usage a single query can use is proportional to `-search.maxUniqueTimeseries`.
* `-search.maxQueryDuration` limits the duration of a single query. If the query takes longer than the given duration, then it is canceled.
  This allows saving CPU and RAM when executing unexpected heavy queries.
  The limit can be overridden to a smaller value by passing `timeout` GET parameter.
* `-search.maxConcurrentRequests` limits the number of concurrent requests VictoriaMetrics can process. Bigger number of concurrent requests usually means
  bigger memory usage. For example, if a single query needs 100 MiB of additional memory during its execution, then 100 concurrent queries may need `100 * 100 MiB = 10 GiB`
  of additional memory. So it is better to limit the number of concurrent queries, while pausing additional incoming queries if the concurrency limit is reached.
  VictoriaMetrics provides `-search.maxQueueDuration` command-line flag for limiting the max wait time for paused queries. See also `-search.maxMemoryPerQuery` command-line flag.
* `-search.maxQueueDuration` limits the maximum duration queries may wait for execution when `-search.maxConcurrentRequests` concurrent queries are executed.
* `-search.ignoreExtraFiltersAtLabelsAPI` enables ignoring of `match[]`, [`extra_filters[]` and `extra_label`](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-enhancements)
  query args at [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) and
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues).
  This may be useful for reducing the load on VictoriaMetrics if the provided extra filters match too many time series.
  The downside is that the endpoints can return labels and series, which do not match the provided extra filters.
* `-search.maxSamplesPerSeries` limits the number of raw samples the query can process per each time series. VictoriaMetrics sequentially processes
  raw samples per each found time series during the query. It unpacks raw samples on the selected time range per each time series into memory
  and then applies the given [rollup function](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions). The `-search.maxSamplesPerSeries` command-line flag
  allows limiting memory usage in the case when the query is executed on a time range, which contains hundreds of millions of raw samples per each located time series.
* `-search.maxSamplesPerQuery` limits the number of raw samples a single query can process. This allows limiting CPU usage for heavy queries.
* `-search.maxResponseSeries` limits the number of time series a single query can return from [`/api/v1/query`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query)
  and [`/api/v1/query_range`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
* `-search.maxPointsPerTimeseries` limits the number of calculated points, which can be returned per each matching time series
  from [range query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
* `-search.maxPointsSubqueryPerTimeseries` limits the number of calculated points, which can be generated per each matching time series
  during [subquery](https://docs.victoriametrics.com/victoriametrics/metricsql/#subqueries) evaluation.
* `-search.maxSeriesPerAggrFunc` limits the number of time series, which can be generated by [MetricsQL aggregate functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions)
  in a single query.
* `-search.maxSeries` limits the number of time series, which may be returned from [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series).
  This endpoint is used mostly by Grafana for auto-completion of metric names, label names and label values. Queries to this endpoint may take big amounts
  of CPU time and memory when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxSeries` to quite low value in order limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.maxLabelsAPISeries`.
* `-search.maxDeleteSeries` limits the number of unique time series that can be
  deleted by a single
  [/api/v1/admin/tsdb/delete_series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1admintsdbdelete_series)
  call. The duration is limited via `-search.maxDeleteDuration` flag{{% available_from "v1.110.0" %}}. Deleting too many time series may require big
  amount of CPU and memory and this limit guards against unplanned resource usage spikes. Also see
  [How to delete time series](#how-to-delete-time-series) section to learn about
  different ways of deleting series.
* `-search.maxTSDBStatusTopNSeries` at `vmselect` limits the number of unique time
  series that can be queried with topN argument by a single
  [/api/v1/status/tsdb?topN=N](#tsdb-stats)
  call.
* `-search.maxTagKeys` limits the number of items, which may be returned from [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels).
  This endpoint is used mostly by Grafana for auto-completion of label names. Queries to this endpoint may take big amounts of CPU time and memory
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxTagKeys` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.maxLabelsAPISeries`.
* `-search.maxTagValues` limits the number of items, which may be returned from [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues).
  This endpoint is used mostly by Grafana for auto-completion of label values. Queries to this endpoint may take big amounts of CPU time and memory
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxTagValues` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.maxLabelsAPISeries`.
* `-search.maxLabelsAPISeries` limits the number of time series, which can be scanned when performing [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) or
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues) requests.
  These endpoints are used mostly by Grafana for auto-completion of label names and label values. Queries to these endpoints may take big amounts of CPU time and memory
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxLabelsAPISeries` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.ignoreExtraFiltersAtLabelsAPI`.
* `-search.maxLabelsAPIDuration` limits the duration for requests to [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels),
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues)
  or [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series).
  The limit can be overridden to a smaller value by passing `timeout` GET parameter.
  These endpoints are used mostly by Grafana for auto-completion of label names and label values. Queries to these endpoints may take big amounts of CPU time and memory
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxLabelsAPIDuration` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPISeries` and `-search.ignoreExtraFiltersAtLabelsAPI`.
* `-search.maxTagValueSuffixesPerSearch` limits the number of entries, which may be returned from `/metrics/find` endpoint. See [Graphite Metrics API usage docs](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#metrics-api).
* `-search.maxFederateSeries` limits maximum number of time series, which can be returned via [/federate API](#federation).
  The duration of the `/federate` queries is limited via `-search.maxQueryDuration` flag. This option allows limiting memory usage.
* `-search.maxExportSeries` limits maximum number of time series, which can be returned from [/api/v1/export* APIs](#how-to-export-data-in-json-line-format).
  The duration of the export queries is limited via `-search.maxExportDuration` flag. This option allows limiting memory usage.
* `-search.maxTSDBStatusSeries` limits maximum number of time series, which can be processed during the call to [/api/v1/status/tsdb](#tsdb-stats).
  The duration of the status queries is limited via `-search.maxStatusRequestDuration` flag. This option allows limiting memory usage.

See also [resource usage limits at VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#resource-usage-limits),
[cardinality limiter](#cardinality-limiter) and [capacity planning docs](#capacity-planning).
