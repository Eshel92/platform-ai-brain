<!-- Part 1 of 4 of cluster/nodes-stats.md (split because the page is big). -->

#### Request

`GET /_nodes/stats` +

`GET /_nodes/<node_id>/stats` +

`GET /_nodes/stats/<metric>` +

`GET /_nodes/<node_id>/stats/<metric>` +

`GET /_nodes/stats/<metric>/<index_metric>` +

`GET /_nodes/<node_id>/stats/<metric>/<index_metric>`


#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.


#### Description

You can use the cluster nodes stats API to retrieve statistics for nodes in a cluster.

All the nodes selective options are explained here.

By default, all stats are returned.
You can limit the returned information by using metrics.


#### Path parameters

`<metric>`::
(Optional, string) Limits the information returned to the specific metrics.
A comma-separated list of the following options:
`adaptive_selection`::
Statistics about adaptive replica selection.

`allocations`::
Statistics about allocated shards

`breaker`::
Statistics about the field data circuit breaker.

`discovery`::
Statistics about the discovery.

`fs`::
File system information, data path, free disk space, read/write stats.

`http`::
HTTP connection information.

`indexing_pressure`::
Statistics about the node's indexing load and related rejections.

`indices`::
Indices stats about size, document count, indexing and deletion times, search times, field cache size, merges and flushes.

`ingest`::
Statistics about ingest preprocessing.

`jvm`::
JVM stats, memory pool information, garbage collection, buffer pools, number of loaded/unloaded classes.

`os`::
Operating system stats, load average, mem, swap.

`process`::
Process statistics, memory consumption, cpu usage, open file descriptors.

`repositories`::
Statistics about snapshot repositories.

`thread_pool`::
Statistics about each thread pool, including current size, queue and rejected tasks.

`transport`::
Transport statistics about sent and received bytes in cluster communication.

`<index_metric>`::
(Optional, string) Limit the information returned for `indices` metric to the specific index metrics.
It can be used only if `indices` (or `all`) metric is specified.
Supported metrics are:
* `bulk`
* `completion`
* `docs`
* `fielddata`
* `flush`
* `get`
* `indexing`
* `mappings`
* `merge`
* `query_cache`
* `recovery`
* `refresh`
* `request_cache`
* `search`
* `segments`
* `shard_stats`
* `store`
* `translog`
* `warmer`
* `dense_vector`
* `sparse_vector`

`<node_id>`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.


#### Query parameters

`completion_fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in `fielddata` and `suggest` statistics.
`fielddata_fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in `fielddata` statistics.
`fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in the statistics.

Used as the default list
unless a specific field list is provided
in the `completion_fields` or `fielddata_fields` parameters.
`groups`::
(Optional, string)
Comma-separated list of search groups
to include in the `search` statistics.
`level`::
(Optional, string)
Indicates whether statistics are aggregated at the cluster, index, or shard level.
If the shards level is requested, some additional
shard-specific statistics are shown.

Valid values are:

*   `cluster`
*   `indices`
*   `shards`
`types`::
(Optional, string) A comma-separated list of document types for the
`indexing` index metric.

`timeout`::
(Optional, time units)
Period to wait for each node to respond. If a node does not respond before its
timeout expires, the response does not include its information. However, timed out
nodes are included in the response's `_nodes.failed` property. Defaults to no
timeout.
`include_segment_file_sizes`::
(Optional, Boolean)
If `true`, the call reports the aggregated disk usage of
each one of the Lucene index files (only applies if segment stats are
requested). Defaults to `false`.
`include_unloaded_segments`::
(Optional, Boolean) If `true`, the response includes information from segments
that are **not** loaded into memory. Defaults to `false`.
