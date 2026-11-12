<!-- Part 6 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## Operation

### Updating / reconfiguring cluster nodes

All the node types - `vminsert`, `vmselect` and `vmstorage` - may be updated via graceful shutdown.
Send `SIGINT` signal to the corresponding process, wait until it finishes and then start new version
with new configs.

There are the following cluster update / upgrade approaches exist:

#### No downtime strategy

Gracefully restart every node in the cluster one-by-one with the updated config / upgraded binary.

It is recommended restarting the nodes in the following order:

1. Restart `vmstorage` nodes.
1. Restart `vminsert` nodes.
1. Restart `vmselect` nodes.

This strategy allows upgrading the cluster without downtime if the following conditions are met:

- The cluster has at least a pair of nodes of each type - `vminsert`, `vmselect` and `vmstorage`,
  so it can continue to accept new data and serve incoming requests when a single node is temporary unavailable
  during its restart. See [cluster availability docs](#cluster-availability) for details.
- The cluster has enough compute resources (CPU, RAM, network bandwidth, disk IO) for processing
  the current workload when a single node of any type (`vminsert`, `vmselect` or `vmstorage`)
  is temporarily unavailable during its restart.
- The updated config / upgraded binary is compatible with the remaining components in the cluster.
  See the [CHANGELOG](https://docs.victoriametrics.com/victoriametrics/changelog/) for compatibility notes between different releases.

If at least a single condition isn't met, then the rolling restart may result in cluster unavailability
during the config update / version upgrade. In this case the following strategy is recommended.

#### Minimum downtime strategy

1. Gracefully stop all the `vminsert` and `vmselect` nodes in parallel.
1. Gracefully restart all the `vmstorage` nodes in parallel.
1. Start all the `vminsert` and `vmselect` nodes in parallel.

The cluster is unavailable for data ingestion and querying when performing the steps above.
The downtime is minimized by restarting cluster nodes in parallel at every step above.
The `minimum downtime` strategy has the following benefits comparing to `no downtime` strategy:

- It allows performing config update / version upgrade with minimum disruption
  when the previous config / version is incompatible with the new config / version.
- It allows performing config update / version upgrade with minimum disruption
  when the cluster has no enough compute resources (CPU, RAM, disk IO, network bandwidth)
  for rolling upgrade.
- It allows minimizing the duration of config update / version upgrade for clusters with big number of nodes
  of for clusters with big `vmstorage` nodes, which may take long time for graceful restart.

> If you'd prefer to avoid managing cluster upgrades yourself, [VictoriaMetrics Cloud](https://console.victoriametrics.cloud/signUp?utm_source=website&utm_campaign=docs_vm_cluster_upgrade)
> handles version upgrades automatically during maintenance windows, and lets you create, resize, or delete deployments with a few clicks from the UI.
> See the [VictoriaMetrics Cloud documentation](https://docs.victoriametrics.com/victoriametrics-cloud/) to get started.

#### Slowness-based re-routing

By default{{% available_from "v1.149.0" %}}, `vminsert` automatically [re-route writes](https://victoriametrics.com/blog/vminsert-how-it-works/#31-rerouting)
away from the slowest `vmstorage` node to preserve maximum ingestion throughput. This prevents a single slow `vmstorage` node
from throttling the entire cluster.

Re-routing occurs only when all of the following conditions hold:
- the storage send buffer is full.
- the saturated vmstorage node is the slowest.
- the vmstorage cluster have much lower saturation overall.
- the vmstorage cluster has at least three ready nodes.

Disable slowness-based re-routing with `-disableRerouting=true` when keeping metrics
perfectly balanced across nodes or minimizing the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series)
matters more than peak write throughput.

Slowness-based re-routing is automatically disabled{{% available_from "v1.149.0" %}} when `-replicationFactor` is greater than `1`,
because rerouting does not guarantee that replicated copies land on distinct storage nodes,
which violates the replication contract.

The rerouting and node saturation could be seen at [VictoriaMetrics - cluster](https://grafana.com/grafana/dashboards/11176) dashboard.

#### Improving re-routing performance during restart

`vmstorage` nodes may experience increased usage for CPU, RAM and disk IO during
[rolling restarts](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#no-downtime-strategy),
since they need to process higher load when some of `vmstorage` nodes are temporarily unavailable in the cluster.

The following approaches can be used for reducing resource usage at `vmstorage` nodes during rolling restart:

- To pass `-disableReroutingOnUnavailable` command-line flag to `vminsert` nodes, so they pause data ingestion when `vmstorage` nodes are restarted
  instead of re-routing the ingested data to other available `vmstorage` nodes.
  Note that the `-disableReroutingOnUnavailable` flag may pause data ingestion for long time when some `vmstorage` nodes are unavailable
  for long time.

- To pass bigger values to `-storage.vminsertConnsShutdownDuration` (available from [v1.95.0](https://docs.victoriametrics.com/victoriametrics/changelog/#v1950))
  command-line flag at `vmstorage` nodes.In this case `vmstorage` increases the interval between gradual closing of `vminsert` connections during graceful shutdown.
  This reduces data ingestion slowdown during rollout restarts.

  Make sure that the `-storage.vminsertConnsShutdownDuration` is smaller than the graceful shutdown timeout configured at the system which manages `vmstorage`
  (e.g. Docker, Kubernetes, systemd, etc.). Otherwise the system may kill `vmstorage` node before it finishes gradual closing of `vminsert` connections.

See also [minimum downtime strategy](#minimum-downtime-strategy).

### Readonly mode

`vmstorage` nodes automatically switch to readonly mode when the directory pointed by `-storageDataPath`
contains less than `-storage.minFreeDiskSpaceBytes` of free space. `vminsert` nodes stop sending data to such nodes
and start re-routing the data to the remaining `vmstorage` nodes.

`vmstorage` sets `vm_storage_is_read_only` metric at `http://vmstorage:8482/metrics` to `1` when it enters read-only mode.
The metric is set to `0` when the `vmstorage` isn't in read-only mode.

### Troubleshooting

- If your VictoriaMetrics cluster experiences data ingestion delays during
  [rolling restarts and configuration updates](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#updating--reconfiguring-cluster-nodes),
  then see [these docs](#improving-re-routing-performance-during-restart).

[Troubleshooting docs for single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/troubleshooting/) apply to VictoriaMetrics cluster as well.

### Rebalancing

Every `vminsert` node [evenly spreads (shards) incoming data](https://victoriametrics.com/blog/vminsert-how-it-works/#3-sharding-and-buffering) among `vmstorage` nodes specified in the `-storageNode` command-line flag.
This guarantees even distribution of the ingested data among `vmstorage` nodes. When new `vmstorage` nodes are added to the `-storageNode`
command-line flag at `vminsert`, then only newly ingested data is distributed evenly among old and new `vmstorage` nodes, while
historical data remains on the old `vmstorage` nodes. This speeds up data ingestion and querying for the majority of production workloads,
since newly ingested data is evenly distributed among all the `vmstorage` nodes, while querying is usually performed over recently ingested data,
which is already stored among all the `vmstorage` nodes. This also provides the following benefits:

- Cluster availability and performance remains stable just after adding new `vmstorage` nodes, since network bandwidth, disk IO and CPU
  isn't spent on data rebalancing among `vmstorage` nodes.
- This eliminates all the possible hard-to-troubleshoot failures which may happen during automatic data rebalancing.
  For example, what happens when some of `vmstorage` nodes become unavailable during data rebalancing?
  Or what happens if new `vmstorage` nodes are added to the cluster while the previous data rebalancing isn't finished yet?
- This allows building flexible cluster schemes when distinct subsets of `vminsert` nodes distribute incoming
  data among different subsets of `vmstorage` nodes with different configs and hardware resources.

There are the following approaches exist for data rebalancing among old and new `vmstorage` nodes:

- To wait until historical data on the old `vmstorage` nodes is automatically deleted according
  to the configured [retention](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention).
- To pass only new `vmstorage` addresses to `-storageNode` command-line flag at `vminsert` nodes, while passing all the `vmstorage`
  addresses to `-storageNode` command-line flag at `vmselect` nodes. This enables writing new data only to new `vmstorage` nodes,
  while historical data from old `vmstorage` nodes remain available for querying via `vmselect` together with the newly ingested data.
  Then wait until data sizes among old and new `vmstorage` nodes become equal and then add old `vmstorage` nodes the `-storageNode`
  command-line flag at `vminsert` nodes.

See also [capacity planning docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#capacity-planning)
and [Why VictoriaMetrics misses automatic data re-balancing among vmstorage nodes?](https://docs.victoriametrics.com/victoriametrics/faq/#why-victoriametrics-misses-automatic-data-re-balancing-between-vmstorage-nodes).

### Backups

For backup configuration, please refer for [vmbackup documentation](https://docs.victoriametrics.com/victoriametrics/vmbackup/).

### Resource usage limits

By default, cluster components of VictoriaMetrics are tuned for an optimal resource usage under typical workloads.
Some workloads may need fine-grained resource usage limits. In these cases the following command-line flags may be useful:

- `-memory.allowedPercent` and `-memory.allowedBytes` limit the amounts of memory, which may be used for various internal caches
  at all the cluster components of VictoriaMetrics - `vminsert`, `vmselect` and `vmstorage`. Note that VictoriaMetrics components may use more memory,
  since these flags don't limit additional memory, which may be needed on a per-query basis.
- `-search.maxMemoryPerQuery` limits the amounts of memory, which can be used for processing a single query at `vmselect` node.
  Queries, which need more memory, are rejected. Heavy queries, which select big number of time series,
  may exceed the per-query memory limit by a small percent. The total memory limit for concurrently executed queries can be estimated
  as `-search.maxMemoryPerQuery` multiplied by `-search.maxConcurrentRequests`.
- `-search.maxUniqueTimeseries` at `vmstorage` component limits the number of unique time series a single query can find and process.
  This means that the maximum memory usage and CPU usage a single query can use at `vmstorage` is proportional to `-search.maxUniqueTimeseries`.
  By default, `vmstorage` calculates this limit automatically based on the available memory and the maximum number of concurrent read requests (see `-search.maxConcurrentRequests`).
  The calculated limit will be printed during process start-up logs and exposed as `vm_search_max_unique_timeseries` metric.
- `-search.maxUniqueTimeseries` at `vmselect` adjusts the limit with the same name at `vmstorage`. The limit cannot exceed the
  value set in vmstorage if the `-search.maxUniqueTimeseries` flag is explicitly defined there. By default, vmselect doesn't apply limit adjustments.
- `-search.maxQueryDuration` at `vmselect` limits the duration of a single query. If the query takes longer than the given duration, then it is canceled.
  This allows saving CPU and RAM at `vmselect` and `vmstorage` when executing unexpectedly heavy queries.
  The limit can be overridden to a smaller value by passing `timeout` GET parameter.
- `-search.maxConcurrentRequests` at `vmselect` and `vmstorage` limits the number of concurrent requests a single `vmselect` / `vmstorage` node can process.
  Bigger number of concurrent requests usually require bigger amounts of memory at both `vmselect` and `vmstorage`.
  For example, if a single query needs 100 MiB of additional memory during its execution, then 100 concurrent queries
  may need `100 * 100 MiB = 10 GiB` of additional memory. So it is better to limit the number of concurrent queries,
  while pausing additional incoming queries if the concurrency limit is reached.
  `vmselect` and `vmstorage` provides `-search.maxQueueDuration` command-line flag for limiting the maximum wait time for paused queries.
  See also `-search.maxMemoryPerQuery` command-line flag at `vmselect`.
- `-search.maxQueueDuration` at `vmselect` and `vmstorage` limits the maximum duration queries may wait for execution when `-search.maxConcurrentRequests`
  concurrent queries are executed.
- `-search.ignoreExtraFiltersAtLabelsAPI` at `vmselect` enables ignoring of `match[]`, [`extra_filters[]` and `extra_label`](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-enhancements)
  query args at [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) and
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues).
  This may be useful for reducing the load on `vmstorage` if the provided extra filters match too many time series.
  The downside is that the endpoints can return labels and series, which do not match the provided extra filters.
- `-search.maxSamplesPerSeries` at `vmselect` limits the number of raw samples the query can process per each time series.
  `vmselect` processes raw samples sequentially per each found time series during the query. It unpacks raw samples on the selected time range
  per each time series into memory and then applies the given [rollup function](https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions).
  The `-search.maxSamplesPerSeries` command-line flag allows limiting memory usage at `vmselect` in the case when the query is executed on a time range,
  which contains hundreds of millions of raw samples per each located time series.
- `-search.maxSamplesPerQuery` at `vmselect` limits the number of raw samples a single query can process. This allows limiting CPU usage at `vmselect` for heavy queries.
- `-search.maxResponseSeries` at `vmselect` limits the number of time series a single query can return
  from [`/api/v1/query`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) and [`/api/v1/query_range`](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
- `-search.maxPointsPerTimeseries` limits the number of calculated points, which can be returned per each
  matching time series from [range query](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
- `-search.maxPointsSubqueryPerTimeseries` limits the number of calculated points, which can be generated
  per each matching time series during [subquery](https://docs.victoriametrics.com/victoriametrics/metricsql/#subqueries) evaluation.
- `-search.maxSeriesPerAggrFunc` limits the number of time series, which can be generated by [MetricsQL aggregate functions](https://docs.victoriametrics.com/victoriametrics/metricsql/#aggregate-functions) in a single query.
- `-search.maxSeries` at `vmselect` limits the number of time series, which may be returned from
  [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series).
  This endpoint is used mostly by Grafana for auto-completion of metric names, label names and label values.
  Queries to this endpoint may take big amounts of CPU time and memory at `vmstorage` and `vmselect` when the database contains
  big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxSeries` to quite low value in order limit CPU and memory usage.
- `-search.maxDeleteSeries` at `vmselect` limits the number of unique time
  series that can be deleted by a single
  [/api/v1/admin/tsdb/delete_series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1admintsdbdelete_series)
  call. The duration is limited via `-search.maxDeleteDuration` flag{{% available_from "v1.110.0" %}}. Deleting too many time series may require big
  amount of CPU and memory at `vmstorage` and this limit guards against unplanned resource usage spikes.
  Also see [How to delete time series](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-delete-time-series) section to
  learn about different ways of deleting series.
- `-search.maxTSDBStatusTopNSeries` at `vmselect` limits the number of unique time
  series that can be queried with topN argument by a single
  [/api/v1/status/tsdb?topN=N](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#tsdb-stats)
  call.
- `-search.maxTagKeys` at `vmstorage` limits the number of items, which may be returned from
  [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels). This endpoint is used mostly by Grafana
  for auto-completion of label names. Queries to this endpoint may take big amounts of CPU time and memory at `vmstorage` and `vmselect`
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxTagKeys` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.maxLabelsAPISeries`.
- `-search.maxTagValues` at `vmstorage` limits the number of items, which may be returned from
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues). This endpoint is used mostly by Grafana
  for auto-completion of label values. Queries to this endpoint may take big amounts of CPU time and memory at `vmstorage` and `vmselect`
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxTagValues` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.maxLabelsAPISeries`.
- `-search.maxLabelsAPISeries` at `vmselect` limits the number of time series, which can be scanned
  when performing [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels) or
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues) requests.
  These endpoints are used mostly by Grafana for auto-completion of label names and label values. Queries to these endpoints may take big amounts of CPU time and memory
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxLabelsAPISeries` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPIDuration` and `-search.ignoreExtraFiltersAtLabelsAPI`.
- `-search.maxLabelsAPIDuration` at `vmselect` limits the duration for requests to [/api/v1/labels](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labels),
  [/api/v1/label/.../values](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1labelvalues)
  or [/api/v1/series](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1series).
  The limit can be overridden to a smaller value by passing `timeout` GET parameter.
  These endpoints are used mostly by Grafana for auto-completion of label names and label values. Queries to these endpoints may take big amounts of CPU time and memory
  when the database contains big number of unique time series because of [high churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate).
  In this case it might be useful to set the `-search.maxLabelsAPIDuration` to quite low value in order to limit CPU and memory usage.
  See also `-search.maxLabelsAPISeries` and `-search.ignoreExtraFiltersAtLabelsAPI`.
- `-search.maxFederateSeries` at `vmselect` limits maximum number of time series, which can be returned via [/federate API](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#federation).
  The duration of the `/federate` queries is limited via `-search.maxQueryDuration` flag. This option allows limiting memory usage.
- `-search.maxExportSeries` at `vmselect` limits maximum number of time series, which can be returned from [/api/v1/export* APIs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-export-data-in-json-line-format).
  The duration of the export queries is limited via `-search.maxExportDuration` flag. This option allows limiting memory usage.
- `-search.maxTSDBStatusSeries` at `vmselect` limits maximum number of time series, which can be processed during the call to [/api/v1/status/tsdb](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#tsdb-stats).
  The duration of the status queries is limited via `-search.maxStatusRequestDuration` flag. This option allows limiting memory usage.
- `-storage.maxDailySeries` at `vmstorage` can be used for limiting the number of time series seen per day aka
  [time series churn rate](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-high-churn-rate). See [cardinality limiter docs](#cardinality-limiter).
- `-storage.maxHourlySeries` at `vmstorage` can be used for limiting the number of [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series).
  See [cardinality limiter docs](#cardinality-limiter).

See also [capacity planning docs](#capacity-planning) and [cardinality limiter in vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter).
