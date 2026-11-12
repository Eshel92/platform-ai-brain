<!-- Part 2 of 4 of cluster/nodes-stats.md (split because the page is big). -->

#### Response body

`_nodes`::
(object) Contains statistics about the number of nodes selected by the request.
**Properties of `_nodes`**
`total`::
(integer) Total number of nodes selected by the request.

`successful`::
(integer) Number of nodes that responded successfully to the request.

`failed`::
(integer) Number of nodes that rejected the request or failed to respond.
If this value is not `0`, a reason for the rejection or failure is included in the response.

`cluster_name`::
(string) Name of the cluster.
Based on the cluster-name setting.

`nodes`::
(object) Contains statistics for the nodes selected by the request.
**Properties of `nodes`**

`<node_id>`::
(object) Contains statistics for the node.
**Properties of `<node_id>`**
=====
`timestamp`::
(integer) Time the node stats were collected for this response.
Recorded in milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`name`::
(string) Human-readable identifier for the node.
Based on the node-name setting.

`transport_address`::
(string) Host and port for the transport layer, used for internal communication between nodes in a cluster.

`host`::
(string) Network host for the node, based on the network.host setting.

`ip`::
(string) IP address and port for the node.

`roles`::
(array of strings) Roles assigned to the node.
See modules-node.

`attributes`::
(object) Contains a list of attributes for the node.

`indices`::
(object) Contains statistics about indices with shards assigned to the node.
**Properties of `indices`**
======
`docs`::
(object) Contains statistics about documents across all primary shards assigned to the node.
**Properties of `docs`**
=======
`count`::
(integer)
The number of documents as reported by Lucene. This excludes deleted documents
and counts any nested documents separately from their parents. It
also excludes documents which were indexed recently and do not yet belong to a
segment.
`deleted`::
(integer)
The number of deleted documents as reported by Lucene, which may be higher or
lower than the number of delete operations you have performed. This number
excludes deletes that were performed recently and do not yet belong to a
segment. Deleted documents are cleaned up by the
automatic merge process if it makes sense to do so.
Also, Elasticsearch creates extra deleted documents to internally track the recent
history of operations on a shard.
=======

`store`::
(object) Contains statistics about the size of shards assigned to the node.
**Properties of `store`**
=======

`size`::
(byte value) Total size of all shards assigned to the node.

`size_in_bytes`::
(integer) Total size, in bytes, of all shards assigned to the node.

`total_data_set_size`::
(byte value) Total data set size of all shards assigned to the node.
This includes the size of shards not stored fully on the node, such as the cache for partially mounted indices.

`total_data_set_size_in_bytes`::
(integer) Total data set size, in bytes, of all shards assigned to the node.
This includes the size of shards not stored fully on the node, such as the cache for partially mounted indices.

`reserved`::
(byte value) A prediction of how much larger the shard stores on this node will eventually grow due to ongoing peer recoveries, restoring snapshots, and similar activities.
A value of `-1b` indicates that this is not available.

`reserved_in_bytes`::
(integer) A prediction, in bytes, of how much larger the shard stores on this node will eventually grow due to ongoing peer recoveries, restoring snapshots, and similar activities.
A value of `-1` indicates that this is not available.

=======

`indexing`::
(object) Contains statistics about indexing operations for the node.
**Properties of `indexing`**
=======

`index_total`::
(integer) Total number of indexing operations.

`index_time`::
(time value) Total time spent performing indexing operations.

`index_time_in_millis`::
(integer) Total time in milliseconds spent performing indexing operations.

`index_current`::
(integer) Number of indexing operations currently running.

`index_failed`::
(integer) Number of failed indexing operations.

`delete_total`::
(integer) Total number of deletion operations.

`delete_time`::
(time value) Time spent performing deletion operations.

`delete_time_in_millis`::
(integer) Time in milliseconds spent performing deletion operations.

`delete_current`::
(integer) Number of deletion operations currently running.

`noop_update_total`::
(integer) Total number of noop operations.

`is_throttled`::
(Boolean) Number of times operations were throttled.

`throttle_time`::
(time value) Total time spent throttling operations.

`throttle_time_in_millis`::
(integer) Total time in milliseconds spent throttling operations.

`write_load`::
(double) Average number of write threads used while indexing documents.

=======

`get`::
(object) Contains statistics about get operations for the node.
**Properties of `get`**
=======

`total`::
(integer) Total number of get operations.

`getTime`::
(time value) Time spent performing get operations.

`time_in_millis`::
(integer) Time in milliseconds spent performing get operations.

`exists_total`::
(integer) Total number of successful get operations.

`exists_time`::
(time value) Time spent performing successful get operations.

`exists_time_in_millis`::
(integer) Time in milliseconds spent performing successful get operations.

`missing_total`::
(integer) Total number of failed get operations.

`missing_time`::
(time value) Time spent performing failed get operations.

`missing_time_in_millis`::
(integer) Time in milliseconds spent performing failed get operations.

`current`::
(integer) Number of get operations currently running.

=======

`search`::
(object) Contains statistics about search operations for the node.
**Properties of `search`**
=======

`open_contexts`::
(integer) Number of open search contexts.

`query_total`::
(integer) Total number of query operations.

`query_time`::
(time value) Time spent performing query operations.

`query_time_in_millis`::
(integer) Time in milliseconds spent performing query operations.

`query_current`::
(integer) Number of query operations currently running.

`fetch_total`::
(integer) Total number of fetch operations.

`fetch_time`::
(time value) Time spent performing fetch operations.

`fetch_time_in_millis`::
(integer) Time in milliseconds spent performing fetch operations.

`fetch_current`::
(integer) Number of fetch operations currently running.

`scroll_total`::
(integer) Total number of scroll operations.

`scroll_time`::
(time value) Time spent performing scroll operations.

`scroll_time_in_millis`::
(integer) Time in milliseconds spent performing scroll operations.

`scroll_current`::
(integer) Number of scroll operations currently running.

`suggest_total`::
(integer) Total number of suggest operations.

`suggest_time`::
(time value) Time spent performing suggest operations.

`suggest_time_in_millis`::
(integer) Time in milliseconds spent performing suggest operations.

`suggest_current`::
(integer) Number of suggest operations currently running.

=======

`merges`::
(object) Contains statistics about merge operations for the node.
**Properties of `merges`**
=======

`current`::
(integer) Number of merge operations currently running.

`current_docs`::
(integer) Number of document merges currently running.

`current_size`::
(byte value) Memory used performing current document merges.

`current_size_in_bytes`::
(integer) Memory, in bytes, used performing current document merges.

`total`::
(integer) Total number of merge operations.

`total_time`::
(time value) Total time spent performing merge operations.

`total_time_in_millis`::
(integer) Total time in milliseconds spent performing merge operations.

`total_docs`::
(integer) Total number of merged documents.

`total_size`::
(byte value) Total size of document merges.

`total_size_in_bytes`::
(integer) Total size of document merges in bytes.

`total_stopped_time`::
(time value) Total time spent stopping merge operations.

`total_stopped_time_in_millis`::
(integer) Total time in milliseconds spent stopping merge operations.

`total_throttled_time`::
(time value) Total time spent throttling merge operations.

`total_throttled_time_in_millis`::
(integer) Total time in milliseconds spent throttling merge operations.

`total_auto_throttle`::
(byte value) Size of automatically throttled merge operations.

`total_auto_throttle_in_bytes`::
(integer) Size, in bytes, of automatically throttled merge operations.

=======

`refresh`::
(object) Contains statistics about refresh operations for the node.
**Properties of `refresh`**
=======

`total`::
(integer) Total number of refresh operations.

`total_time`::
(time value) Total time spent performing refresh operations.

`total_time_in_millis`::
(integer) Total time in milliseconds spent performing refresh operations.

`external_total`::
(integer) Total number of external refresh operations.

`external_total_time`::
(time value) Total time spent performing external operations.

`external_total_time_in_millis`::
(integer) Total time in milliseconds spent performing external operations.

`listeners`::
(integer) Number of refresh listeners.

=======

`flush`::
(object) Contains statistics about flush operations for the node.
**Properties of `flush`**
=======

`total`::
(integer) Number of flush operations.

`periodic`::
(integer) Number of flush periodic operations.

`total_time`::
(time value) Total time spent performing flush operations.

`total_time_in_millis`::
(integer) Total time in milliseconds spent performing flush operations.

=======

`warmer`::
(object) Contains statistics about index warming operations for the node.
**Properties of `warmer`**
=======

`current`::
(integer) Number of active index warmers.

`total`::
(integer) Total number of index warmers.

`total_time`::
(time value) Total time spent performing index warming operations.

`total_time_in_millis`::
(integer) Total time in milliseconds spent performing index warming operations.

=======

`query_cache`::
(object) Contains statistics about the query cache across all shards assigned to the node.
**Properties of `query_cache`**
=======

`memory_size`::
(byte value) Total amount of memory used for the query cache across all shards assigned to the node.

`memory_size_in_bytes`::
(integer) Total amount of memory, in bytes, used for the query cache across all shards assigned to the node.

`total_count`::
(integer) Total count of hits, misses, and cached queries in the query cache.

`hit_count`::
(integer) Number of query cache hits.

`miss_count`::
(integer) Number of query cache misses.

`cache_size`::
(integer) Current number of cached queries.

`cache_count`::
(integer) Total number of all queries that have been cached.

`evictions`::
(integer) Number of query cache evictions.

=======

`fielddata`::
(object) Contains statistics about the field data cache across all shards assigned to the node.
**Properties of `fielddata`**
=======

`memory_size`::
(byte value) Total amount of memory used for the field data cache across all shards assigned to the node.

`memory_size_in_bytes`::
(integer) Total amount of memory, in bytes, used for the field data cache across all shards assigned to the node.

`evictions`::
(integer) Number of fielddata evictions.

=======

`completion`::
(object) Contains statistics about completions across all shards assigned to the node.
**Properties of `completion`**
=======

`size`::
(byte value) Total amount of memory used for completion across all shards assigned to the node.

`size_in_bytes`::
(integer) Total amount of memory, in bytes, used for completion across all shards assigned to the node.

=======

`segments`::
(object) Contains statistics about segments across all shards assigned to the node.
**Properties of `segments`**
=======

`count`::
(integer) Number of segments.

`memory`::
(byte value) Total amount of memory used for segments across all shards assigned to the node.

`memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for segments across all shards assigned to the node.

`terms_memory`::
(byte value) Total amount of memory used for terms across all shards assigned to the node.

`terms_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for terms across all shards assigned to the node.

`stored_fields_memory`::
(byte value) Total amount of memory used for stored fields across all shards assigned to the node.

`stored_fields_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for stored fields across all shards assigned to the node.

`term_vectors_memory`::
(byte value) Total amount of memory used for term vectors across all shards assigned to the node.

`term_vectors_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for term vectors across all shards assigned to the node.

`norms_memory`::
(byte value) Total amount of memory used for normalization factors across all shards assigned to the node.

`norms_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for normalization factors across all shards assigned to the node.

`points_memory`::
(byte value) Total amount of memory used for points across all shards assigned to the node.

`points_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for points across all shards assigned to the node.

`doc_values_memory`::
(byte value) Total amount of memory used for doc values across all shards assigned to the node.

`doc_values_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used for doc values across all shards assigned to the node.

`index_writer_memory`::
(byte value) Total amount of memory used by all index writers across all shards assigned to the node.

`index_writer_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used by all index writers across all shards assigned to the node.

`version_map_memory`::
(byte value) Total amount of memory used by all version maps across all shards assigned to the node.

`version_map_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used by all version maps across all shards assigned to the node.

`fixed_bit_set`::
(byte value) Total amount of memory used by fixed bit sets across all shards assigned to the node.
Fixed bit sets are used for nested object field types and type filters for join fields.

`fixed_bit_set_memory_in_bytes`::
(integer) Total amount of memory, in bytes, used by fixed bit sets across all shards assigned to the node.
Fixed bit sets are used for nested object field types and type filters for join fields.

`max_unsafe_auto_id_timestamp`::
(integer) Time of the most recently retried indexing request.
Recorded in milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`file_sizes`::
(object) Contains statistics about the size of the segment file.
**Properties of `file_sizes`**
========
`size`::
(byte value) Size of the segment file.

`size_in_bytes`::
(integer) Size, in bytes, of the segment file.

`description`::
(string) Description of the segment file.

========
=======

`translog`::
(object) Contains statistics about transaction log operations for the node.
**Properties of `translog`**
=======

`operations`::
(integer) Number of transaction log operations.

`size`::
(byte value) Size of the transaction log.

`size_in_bytes`::
(integer) Size, in bytes, of the transaction log.

`uncommitted_operations`::
(integer) Number of uncommitted transaction log operations.

`uncommitted_size`::
(byte value) Size of uncommitted transaction log operations.

`uncommitted_size_in_bytes`::
(integer) Size, in bytes, of uncommitted transaction log operations.

`earliest_last_modified_age`::
(integer) Earliest last modified age for the transaction log.

=======

`request_cache`::
(object) Contains statistics about the request cache across all shards assigned to the node.
**Properties of `request_cache`**
=======

`memory_size`::
(byte value) Memory used by the request cache.

`memory_size_in_bytes`::
(integer) Memory, in bytes, used by the request cache.

`evictions`::
(integer) Number of request cache operations.

`hit_count`::
(integer) Number of request cache hits.

`miss_count`::
(integer) Number of request cache misses.

=======

`recovery`::
(object) Contains statistics about recovery operations for the node.
**Properties of `recovery`**
=======

`current_as_source`::
(integer) Number of recoveries that used an index shard as a source.

`current_as_target`::
(integer) Number of recoveries that used an index shard as a target.

`throttle_time`::
(time value) Time by which recovery operations were delayed due to throttling.

`throttle_time_in_millis`::
(integer) Time in milliseconds recovery operations were delayed due to throttling.

=======

`shard_stats`::
(object) Contains statistics about all shards assigned to the node.
**Properties of `shard_stats`**
=======

`total_count`::
(integer) The total number of shards assigned to the node.

=======

`mappings`::
(object) Contains statistics about the mappings for the node.
This is not shown for the `shards` level, since mappings may be shared across the shards of an index on a node.
**Properties of `mappings`**
=======

`total_count`::
(integer) Number of mappings, including runtime and object fields.

`total_estimated_overhead`::
(byte value) Estimated heap overhead of mappings on this node, which allows for 1kiB of heap for every mapped field.

`total_estimated_overhead_in_bytes`::
(integer) Estimated heap overhead, in bytes, of mappings on this node, which allows for 1kiB of heap for every mapped field.

`total_segments`::
(integer) Estimated number of Lucene segments on this node

`total_segment_fields`::
(integer) Estimated number of fields at the segment level on this node

`average_fields_per_segment`::
(integer) Estimated average number of fields per segment on this node
=======

`dense_vector`::
(object) Contains statistics about dense_vector across all shards assigned to the node.
**Properties of `dense_vector`**
=======

`value_count`::
(integer) Total number of dense vector indexed across all shards assigned to the node.

=======

`sparse_vector`::
(object) Contains statistics about sparse_vector across all shards assigned to the node.
**Properties of `sparse_vector`**
=======

`value_count`::
(integer) Total number of sparse vector indexed across all shards assigned to the node.

=======

`shards`::
(object) When the `shards` level is requested, contains the aforementioned `indices` statistics for every shard (per
index, and then per shard ID), as well as the following shard-specific statistics (which are not shown when the
requested level is higher than `shards`):
**Additional shard-specific statistics for the `shards` level**
=======

`routing`::
(object) Contains routing information about the shard.
**Properties of `routing`**
========

`state`::
(string) State of the shard. Returned values are:
* `INITIALIZING`: The shard is initializing/recovering.
* `RELOCATING`: The shard is relocating.
* `STARTED`: The shard has started.
* `UNASSIGNED`: The shard is not assigned to any node.

`primary`::
(Boolean) Whether the shard is a primary shard or not.

`node`::
(string) ID of the node the shard is allocated to.

`relocating_node`::
(string) ID of the node the shard is either relocating to or relocating from, or null if shard is not relocating.

========

`commit`::
(object) Contains information regarding the last commit point of the shard.
**Properties of `commit`**
========

`id`::
(string) Base64 version of the commit ID.

`generation`::
(integer) Lucene generation of the commit.

`user_data`::
(object) Contains additional technical information about the commit.

`num_docs`::
(integer) The number of docs in the commit.

========

`seq_no`::
(object) Contains information about sequence numbers and checkpoints for the shard.
**Properties of `seq_no`**
========

`max_seq_no`::
(integer) The maximum sequence number issued so far.

`local_checkpoint`::
(integer) The current local checkpoint of the shard.

`global_checkpoint`::
(integer) The current global checkpoint of the shard.

========

`retention_leases`::
(object) Contains information about history retention leases.
**Properties of `retention_leases`**
========

`primary_term`::
(integer) The primary term of this retention lease collection.

`version`::
(integer) The current version of the retention lease collection.

`leases`::
(array of objects) List of current leases for this shard.
**Properties of `leases`**
=========

`id`::
(string) The ID of the lease.

`retaining_seq_no`::
(integer) The minimum sequence number to be retained by the lease.

`timestamp`::
(integer) The timestamp of when the lease was created or renewed.
Recorded in milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`source`::
(string) The source of the lease.

=========
========

`shard_path`::
(object)
**Properties of `shard_path`**
========

`state_path`::
(string) The state-path root, without the index name and the shard ID.

`data_path`::
(string) The data-path root, without the index name and the shard ID.

`is_custom_data_path`::
(boolean) Whether the data path is a custom data location and therefore outside of the nodes configured data paths.

========

`search_idle`::
(boolean) Whether the shard is search idle or not.

`search_idle_time`::
(integer) Time since previous searcher access.
Recorded in milliseconds.

=======
======

`os`::
(object) Contains statistics about the operating system for the node.
**Properties of `os`**
======

`timestamp`::
(integer) Last time the operating system statistics were refreshed.
Recorded in milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`cpu`::
(object) Contains statistics about CPU usage for the node.
**Properties of `cpu`**
=======

`percent`::
(integer) Recent CPU usage for the whole system, or `-1` if not supported.

`load_average`::
(object) Contains statistics about load averages on the system.
**Properties of `load_average`**
========

`1m`::
(float) One-minute load average on the system (field is not present if one-minute load average is not available).

`5m`::
(float) Five-minute load average on the system (field is not present if five-minute load average is not available).

`15m`::
(float) Fifteen-minute load average on the system (field is not present if fifteen-minute load average is not available).

========
=======

`mem`::
(object) Contains statistics about memory usage for the node.
**Properties of `mem`**
=======

`total`::
(byte value) Total amount of physical memory.

`total_in_bytes`::
(integer) Total amount of physical memory in bytes.

`adjusted_total`::
(byte value) If the amount of physical memory has been overridden using the `es.total_memory_bytes`
system property then this reports the overridden value.
Otherwise it reports the same value as `total`.

`adjusted_total_in_bytes`::
(integer) If the amount of physical memory has been overridden using the `es.total_memory_bytes`
system property then this reports the overridden value in bytes.
Otherwise it reports the same value as `total_in_bytes`.

`free`::
(byte value) Amount of free physical memory.

`free_in_bytes`::
(integer) Amount of free physical memory in bytes.

`used`::
(byte value) Amount of used physical memory.

`used_in_bytes`::
(integer) Amount of used physical memory in bytes.

`free_percent`::
(integer) Percentage of free memory.

`used_percent`::
(integer) Percentage of used memory.

=======

`swap`::
(object) Contains statistics about swap space for the node.
**Properties of `swap`**
=======

`total`::
(byte value) Total amount of swap space.

`total_in_bytes`::
(integer) Total amount of swap space in bytes.

`free`::
(byte value) Amount of free swap space.

`free_in_bytes`::
(integer) Amount of free swap space in bytes.

`used`::
(byte value) Amount of used swap space.

`used_in_bytes`::
(integer) Amount of used swap space in bytes.

=======

`cgroup` (Linux only)::
(object) Contains cgroup statistics for the node.
**Note:** For the cgroup stats to be visible, cgroups must be compiled into the kernel, the `cpu` and `cpuacct` cgroup subsystems must be configured and stats must be readable from `/sys/fs/cgroup/cpu` and `/sys/fs/cgroup/cpuacct`.
**Properties of `cgroup`**
=======

`cpuacct` (Linux only)::
(object) Contains statistics about `cpuacct` control group for the node.
**Properties of `cpuacct`**
========

`control_group` (Linux only)::
(string) The `cpuacct` control group to which the Elasticsearch process belongs.

`usage_nanos` (Linux only)::
(integer) The total CPU time (in nanoseconds) consumed by all tasks in the same cgroup as the Elasticsearch process.

========

`cpu` (Linux only)::
(object) Contains statistics about `cpu` control group for the node.
**Properties of `cpu`**
========

`control_group` (Linux only)::
(string) The `cpu` control group to which the Elasticsearch process belongs.

`cfs_period_micros` (Linux only)::
(integer) The period of time (in microseconds) for how regularly all tasks in the same cgroup as the Elasticsearch process should have their access to CPU resources reallocated.

`cfs_quota_micros` (Linux only)::
(integer) The total amount of time (in microseconds) for which all tasks in the same cgroup as the Elasticsearch process can run during one period
`cfs_period_micros`.

`stat` (Linux only)::
(object) Contains CPU statistics for the node.
**Properties of `stat`**
=========
`number_of_elapsed_periods` (Linux only)::
(integer) The number of reporting periods (as specified by
`cfs_period_micros`) that have elapsed.

`number_of_times_throttled` (Linux only)::
(integer) The number of times all tasks in the same cgroup as the Elasticsearch process have been throttled.

`time_throttled_nanos` (Linux only)::
(integer) The total amount of time (in nanoseconds) for which all tasks in the same cgroup as the Elasticsearch process have been throttled.

=========
========

`memory` (Linux only)::
(object) Contains statistics about the `memory` control group for the node.
**Properties of `memory`**
========

`control_group` (Linux only)::
(string) The `memory` control group to which the Elasticsearch process belongs.

`limit_in_bytes` (Linux only)::
(string) The maximum amount of user memory (including file cache) allowed for all tasks in the same cgroup as the Elasticsearch process.
This value can be too big to store in a `long`, so is returned as a string so that the value returned can exactly match what the underlying operating system interface returns.
Any value that is too large to parse into a `long` almost certainly means no limit has been set for the cgroup.

`usage_in_bytes` (Linux only)::
(string) The total current memory usage by processes in the cgroup (in bytes) by all tasks in the same cgroup as the Elasticsearch process.
This value is stored as a string for consistency with `limit_in_bytes`.

========
=======
======

`process`::
(object) Contains process statistics for the node.
**Properties of `process`**
======

`timestamp`::
(integer) Last time the statistics were refreshed.
Recorded in milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`open_file_descriptors`::
(integer) Number of opened file descriptors associated with the current or
`-1` if not supported.

`max_file_descriptors`::
(integer) Maximum number of file descriptors allowed on the system, or `-1` if not supported.

`cpu`::
(object) Contains CPU statistics for the node.
**Properties of `cpu`**
=======

`percent`::
(integer) CPU usage in percent, or `-1` if not known at the time the stats are computed.

`total`::
(time value) CPU time used by the process on which the Java virtual machine is running.

`total_in_millis`::
(integer) CPU time (in milliseconds) used by the process on which the Java virtual machine is running, or `-1` if not supported.

=======

`mem`::
(object) Contains virtual memory statistics for the node.
**Properties of `mem`**
=======

`total_virtual`::
(byte value) Size of virtual memory that is guaranteed to be available to the running process.

`total_virtual_in_bytes`::
(integer) Size in bytes of virtual memory that is guaranteed to be available to the running process.

=======
======

`jvm`::
(object) Contains Java Virtual Machine (JVM) statistics for the node.
**Properties of `jvm`**
======

`timestamp`::
(integer) Last time JVM statistics were refreshed.

`uptime`::
(time value) Human-readable JVM uptime.
Only returned if the
`human` query parameter is `true`.

`uptime_in_millis`::
(integer) JVM uptime in milliseconds.

`mem`::
(object) Contains JVM memory usage statistics for the node.
**Properties of `mem`**
=======

`heap_used`::
(byte value) Memory currently in use by the heap.

`heap_used_in_bytes`::
(integer) Memory, in bytes, currently in use by the heap.

`heap_used_percent`::
(integer) Percentage of memory currently in use by the heap.

`heap_committed`::
(byte value) Amount of memory available for use by the heap.

`heap_committed_in_bytes`::
(integer) Amount of memory, in bytes, available for use by the heap.

`heap_max`::
(byte value) Maximum amount of memory available for use by the heap.

`heap_max_in_bytes`::
(integer) Maximum amount of memory, in bytes, available for use by the heap.

`non_heap_used`::
(byte value) Non-heap memory used.

`non_heap_used_in_bytes`::
(integer) Non-heap memory used, in bytes.

`non_heap_committed`::
(byte value) Amount of non-heap memory available.

`non_heap_committed_in_bytes`::
(integer) Amount of non-heap memory available, in bytes.

`pools`::
(object) Contains statistics about heap memory usage for the node.
**Properties of `pools`**
========

`young`::
(object) Contains statistics about memory usage by the young generation heap for the node.
**Properties of `young`**
=========

`used`::
(byte value) Memory used by the young generation heap.

`used_in_bytes`::
(integer) Memory, in bytes, used by the young generation heap.

`max`::
(byte value) Maximum amount of memory available for use by the young generation heap.

`max_in_bytes`::
(integer) Maximum amount of memory, in bytes, available for use by the young generation heap.

`peak_used`::
(byte value) Largest amount of memory historically used by the young generation heap.

`peak_used_in_bytes`::
(integer) Largest amount of memory, in bytes, historically used by the young generation heap.

`peak_max`::
(byte value) Largest amount of memory historically used by the young generation heap.

`peak_max_in_bytes`::
(integer) Largest amount of memory, in bytes, historically used by the young generation heap.

=========

`survivor`::
(object) Contains statistics about memory usage by the survivor space for the node.
**Properties of `survivor`**
=========

`used`::
(byte value) Memory used by the survivor space.

`used_in_bytes`::
(integer) Memory, in bytes, used by the survivor space.

`max`::
(byte value) Maximum amount of memory available for use by the survivor space.

`max_in_bytes`::
(integer) Maximum amount of memory, in bytes, available for use by the survivor space.

`peak_used`::
(byte value) Largest amount of memory historically used by the survivor space.

`peak_used_in_bytes`::
(integer) Largest amount of memory, in bytes, historically used by the survivor space.

`peak_max`::
(byte value) Largest amount of memory historically used by the survivor space.

`peak_max_in_bytes`::
(integer) Largest amount of memory, in bytes, historically used by the survivor space.

=========

`old`::
(object) Contains statistics about memory usage by the old generation heap for the node.
**Properties of `old`**
=========

`used`::
(byte value) Memory used by the old generation heap.

`used_in_bytes`::
(integer) Memory, in bytes, used by the old generation heap.

`max`::
(byte value) Maximum amount of memory available for use by the old generation heap.

`max_in_bytes`::
(integer) Maximum amount of memory, in bytes, available for use by the old generation heap.

`peak_used`::
(byte value) Largest amount of memory historically used by the old generation heap.

`peak_used_in_bytes`::
(integer) Largest amount of memory, in bytes, historically used by the old generation heap.

`peak_max`::
(byte value) Highest memory limit historically available for use by the old generation heap.

`peak_max_in_bytes`::
(integer) Highest memory limit, in bytes, historically available for use by the old generation heap.

=========
========
=======

`threads`::
(object) Contains statistics about JVM thread usage for the node.
**Properties of `threads`**
=======

`count`::
(integer) Number of active threads in use by JVM.

`peak_count`::
(integer) Highest number of threads used by JVM.

=======

`gc`::
(object) Contains statistics about JVM garbage collectors for the node.
**Properties of `gc`**
=======

`collectors`::
(object) Contains statistics about JVM garbage collectors for the node.
**Properties of `collectors`**
========

`young`::
(object) Contains statistics about JVM garbage collectors that collect young generation objects for the node.
**Properties of `young`**
=========

`collection_count`::
(integer) Number of JVM garbage collectors that collect young generation objects.

`collection_time`::
(time value) Total time spent by JVM collecting young generation objects.

`collection_time_in_millis`::
(integer) Total time in milliseconds spent by JVM collecting young generation objects.

=========

`old`::
(object) Contains statistics about JVM garbage collectors that collect old generation objects for the node.
**Properties of `old`**
=========

`collection_count`::
(integer) Number of JVM garbage collectors that collect old generation objects.

`collection_time`::
(time value) Total time spent by JVM collecting old generation objects.

`collection_time_in_millis`::
(integer) Total time in milliseconds spent by JVM collecting old generation objects.

=========
========
=======

`buffer_pools`::
(object) Contains statistics about JVM buffer pools for the node.
**Properties of `buffer_pools`**
=======

`mapped`::
(object) Contains statistics about mapped JVM buffer pools for the node.
**Properties of `mapped`**
========

`count`::
(integer) Number of mapped buffer pools.

`used`::
(byte value) Size of mapped buffer pools.

`used_in_bytes`::
(integer) Size, in bytes, of mapped buffer pools.

`total_capacity`::
(byte value) Total capacity of mapped buffer pools.

`total_capacity_in_bytes`::
(integer) Total capacity, in bytes, of mapped buffer pools.

========

`direct`::
(object) Contains statistics about direct JVM buffer pools for the node.
**Properties of `direct`**
========

`count`::
(integer) Number of direct buffer pools.

`used`::
(byte value) Size of direct buffer pools.

`used_in_bytes`::
(integer) Size, in bytes, of direct buffer pools.

`total_capacity`::
(byte value) Total capacity of direct buffer pools.

`total_capacity_in_bytes`::
(integer) Total capacity, in bytes, of direct buffer pools.

========
=======

`classes`::
(object) Contains statistics about classes loaded by JVM for the node.
**Properties of `classes`**
=======

`current_loaded_count`::
(integer) Number of classes currently loaded by JVM.

`total_loaded_count`::
(integer) Total number of classes loaded since the JVM started.

`total_unloaded_count`::
(integer) Total number of classes unloaded since the JVM started.

=======
======

`repositories`::
(object) Statistics about snapshot repositories.
**Properties of `repositories`**
======

`<repository_name>`::
(object) Contains repository throttling statistics for the node.
**Properties of `<repository_name>`**
=======

`total_read_throttled_time_nanos`::
(integer) Total number of nanos which node had to wait during recovery.

`total_write_throttled_time_nanos`::
(integer) Total number of nanos which node had to wait during snapshotting.

=======
======

`thread_pool`::
(object) Contains thread pool statistics for the node
**Properties of `thread_pool`**
======

`<thread_pool_name>`::
(object) Contains statistics about the thread pool for the node.
**Properties of `<thread_pool_name>`**
=======

`threads`::
(integer) Number of threads in the thread pool.

`queue`::
(integer) Number of tasks in queue for the thread pool.

`active`::
(integer) Number of active threads in the thread pool.

`rejected`::
(integer) Number of tasks rejected by the thread pool executor.

`largest`::
(integer) Highest number of active threads in the thread pool.

`completed`::
(integer) Number of tasks completed by the thread pool executor.

=======
======

`fs`::
(object) Contains file store statistics for the node.
**Properties of `fs`**
======

`timestamp`::
(integer) Last time the file stores statistics were refreshed.
Recorded in milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`total`::
(object) Contains statistics for all file stores of the node.
**Properties of `total`**
=======

`total`::
(byte value) Total size of all file stores.

`total_in_bytes`::
(integer) Total size (in bytes) of all file stores.

`free`::
(byte value) Total unallocated disk space in all file stores.

`free_in_bytes`::
(integer) Total number of unallocated bytes in all file stores.

`available`::
(byte value) Total disk space available to this Java virtual machine on all file stores.
Depending on OS or process level restrictions (e.g. XFS quotas), this might appear less than `free`.
This is the actual amount of free disk space the Elasticsearch node can utilise.

`available_in_bytes`::
(integer) Total number of bytes available to this Java virtual machine on all file stores.
Depending on OS or process level restrictions (e.g. XFS quotas), this might appear less than `free_in_bytes`.
This is the actual amount of free disk space the Elasticsearch node can utilise.

=======

`data`::
(array of objects) List of all file stores.
**Properties of `data`**
=======

`path`::
(string) Path to the file store.

`mount`::
(string) Mount point of the file store (ex: /dev/sda2).

`type`::
(string) Type of the file store (ex: ext4).

`total`::
(byte value) Total size of the file store.

`total_in_bytes`::
(integer) Total size (in bytes) of the file store.

`free`::
(byte value) Total amount of unallocated disk space in the file store.

`free_in_bytes`::
(integer) Total number of unallocated bytes in the file store.

`available`::
(byte value) Total amount of disk space available to this Java virtual machine on this file store.

`available_in_bytes`::
(integer) Total number of bytes available to this Java virtual machine on this file store.

`low_watermark_free_space`::
(byte value) The effective low disk watermark for this data path on this node: when a node has less free space than this value for at least one data path, its disk usage has exceeded the low watermark.
See disk-based-shard-allocation for more information about disk watermarks and their effects on shard allocation.

`low_watermark_free_space_in_bytes`::
(integer) The effective low disk watermark, in bytes, for this data path on this node:
when a node has less free space than this value for at least one data path, its disk usage has exceeded the low watermark.
See disk-based-shard-allocation
for more information about disk watermarks and their effects on shard allocation.

`high_watermark_free_space`::
(byte value) The effective high disk watermark for this data path on this node: when a node has less free space than this value for at least one data path, its disk usage has exceeded the high watermark.
See disk-based-shard-allocation for more information about disk watermarks and their effects on shard allocation.

`high_watermark_free_space_in_bytes`::
(integer) The effective high disk watermark, in bytes, for this data path on this node:
when a node has less free space than this value for at least one data path, its disk usage has exceeded the high watermark.
See disk-based-shard-allocation
