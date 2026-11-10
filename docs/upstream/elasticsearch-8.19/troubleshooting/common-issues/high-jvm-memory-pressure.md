<!-- Converted from troubleshooting/common-issues/high-jvm-memory-pressure.asciidoc (AsciiDoc). Includes are inlined. -->

### High JVM memory pressure

High JVM memory usage can degrade cluster performance and trigger
circuit breaker errors. To prevent this, we recommend
taking steps to reduce memory pressure if a node's JVM memory usage consistently
exceeds 85%.

****
If you're using Elastic Cloud Hosted, then you can use AutoOps to monitor your cluster. AutoOps significantly simplifies cluster management with performance recommendations, resource utilization visibility, real-time issue detection and resolution paths. For more information, refer to [Monitor with AutoOps](https://www.elastic.co/guide/en/cloud/current/ec-autoops.html).
****

#### Diagnose high JVM memory pressure

**Check JVM memory pressure**

From your deployment menu, click **Elasticsearch**. Under **Instances**, each
instance displays a **JVM memory pressure** indicator. When the JVM memory
pressure reaches 75%, the indicator turns red.

You can also use the nodes stats API to calculate the
current JVM memory pressure for each node.

```console
GET _nodes/stats?filter_path=nodes.*.jvm.mem.pools.old
```

Use the response to calculate memory pressure as follows:

JVM Memory Pressure = `used_in_bytes` / `max_in_bytes`

To calculate the current JVM memory pressure for each node, use the
nodes stats API.

```console
GET _nodes/stats?filter_path=nodes.*.jvm.mem.pools.old
```

Use the response to calculate memory pressure as follows:

JVM Memory Pressure = `used_in_bytes` / `max_in_bytes`

**Check garbage collection logs**

As memory usage increases, garbage collection becomes more frequent and takes
longer. You can track the frequency and length of garbage collection events in
`elasticsearch.log`. For example, the following event states Elasticsearch
spent more than 50% (21 seconds) of the last 40 seconds performing garbage
collection.

```log
[timestamp_short_interval_from_last][INFO ][o.e.m.j.JvmGcMonitorService] [node_id] [gc][number] overhead, spent [21s] collecting in the last [40s]
```

**Capture a JVM heap dump**

To determine the exact reason for the high JVM memory pressure, capture a heap
dump of the JVM while its memory usage is high, and also capture the
garbage collector logs covering the same time period.

#### Reduce JVM memory pressure

This section contains some common suggestions for reducing JVM memory pressure.

**Reduce your shard count**

Every shard uses memory. In most cases, a small set of large shards uses fewer
resources than many small shards. For tips on reducing your shard count, see
size-your-shards.

**Avoid expensive searches**

Expensive searches can use large amounts of memory. To better track expensive
searches on your cluster, enable slow logs.

Expensive searches may have a large `size` argument,
use aggregations with a large number of buckets, or include
expensive queries. To prevent expensive
searches, consider the following setting changes:

* Lower the `size` limit using the
`index.max_result_window` index setting.

* Decrease the maximum number of allowed aggregation buckets using the
search.max_buckets cluster setting.

* Disable expensive queries using the
`search.allow_expensive_queries` cluster
setting.

* Set a default search timeout using the `search.default_search_timeout` cluster setting. 

```console
PUT _settings
{
  "index.max_result_window": 5000
}

PUT _cluster/settings
{
  "persistent": {
    "search.max_buckets": 20000,
    "search.allow_expensive_queries": false
  }
}
```

**Prevent mapping explosions**

Defining too many fields or nesting fields too deeply can lead to
mapping explosions that use large amounts of memory.
To prevent mapping explosions, use the <<mapping-settings-limit,mapping limit
settings>> to limit the number of field mappings.

**Spread out bulk requests**

While more efficient than individual requests, large bulk indexing
or multi-search requests can still create high JVM
memory pressure. If possible, submit smaller requests and allow more time
between them.

**Upgrade node memory**

Heavy indexing and search loads can cause high JVM memory pressure. To better
handle heavy workloads, upgrade your nodes to increase their memory capacity.
