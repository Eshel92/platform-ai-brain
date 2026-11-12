<!-- Part 3 of 4 of cluster/nodes-stats.md (split because the page is big). -->

for more information about disk watermarks and their effects on shard allocation.

`flood_stage_free_space`::
(byte value) The effective flood stage disk watermark for this data path on this node: when a node has less free space than this value for at least one data path, its disk usage has exceeded the flood stage watermark.
See
disk-based-shard-allocation for more information about disk watermarks and their effects on shard allocation.

`flood_stage_free_space_in_bytes`::
(integer) The effective flood stage disk watermark, in bytes, for this data path on this node: when a node has less free space than this value for at least one data path, its disk usage has exceeded the flood stage watermark.
See
disk-based-shard-allocation for more information about disk watermarks and their effects on shard allocation.

`frozen_flood_stage_free_space`::
(byte value) The effective flood stage disk watermark for this data path on a dedicated frozen node: when a dedicated frozen node has less free space than this value for at least one data path, its disk usage has exceeded the flood stage watermark.
See disk-based-shard-allocation for more information about disk watermarks and their effects on shard allocation.

`frozen_flood_stage_free_space_in_bytes`::
(integer) The effective flood stage disk watermark, in bytes, for this data path on a dedicated frozen node: when a dedicated frozen node has less free space than this value for at least one data path, its disk usage has exceeded the flood stage watermark.
See disk-based-shard-allocation for more information about disk watermarks and their effects on shard allocation.

=======

`io_stats` (Linux only)::
(objects) Contains I/O statistics for the node.

**Note:** These statistics are derived from the `/proc/diskstats` kernel interface.
This interface accounts for IO performed by all processes on the system, even
if you are running Elasticsearch within a container.
**Properties of `io_stats`**
=======

`devices` (Linux only)::
(array) Array of disk metrics for each device that is backing an Elasticsearch data path.
These disk metrics are probed periodically and averages between the last probe and the current probe are computed.
**Properties of `devices`**
========

`device_name` (Linux only)::
(string) The Linux device name.

`operations` (Linux only)::
(integer) The total number of read and write operations for the device completed since starting Elasticsearch.

`read_operations` (Linux only)::
(integer) The total number of read operations for the device completed since starting
Elasticsearch.

`write_operations` (Linux only)::
(integer) The total number of write operations for the device completed since starting
Elasticsearch.

`read_kilobytes` (Linux only)::
(integer) The total number of kilobytes read for the device since starting Elasticsearch.

`write_kilobytes` (Linux only)::
(integer) The total number of kilobytes written for the device since starting Elasticsearch.

`io_time_in_millis` (Linux only)::
(integer) The total time in milliseconds spent performing I/O operations for the device since starting Elasticsearch.

========

`total` (Linux only)::
(object) The sum of the disk metrics for all devices that back an Elasticsearch data path.
**Properties of `total`**
========

`operations` (Linux only)::
(integer) The total number of read and write operations across all devices used by
Elasticsearch completed since starting Elasticsearch.

`read_operations` (Linux only)::
(integer) The total number of read operations for across all devices used by Elasticsearch
completed since starting Elasticsearch.

`write_operations` (Linux only)::
(integer) The total number of write operations across all devices used by Elasticsearch
completed since starting Elasticsearch.

`read_kilobytes` (Linux only)::
(integer) The total number of kilobytes read across all devices used by Elasticsearch since starting Elasticsearch.

`write_kilobytes` (Linux only)::
(integer) The total number of kilobytes written across all devices used by Elasticsearch since starting Elasticsearch.

`io_time_in_millis` (Linux only)::
(integer) The total time in milliseconds spent performing I/O operations across all devices used by Elasticsearch since starting Elasticsearch.

========

=======
======

`transport`::
(object) Contains transport statistics for the node.
**Properties of `transport`**
======

`server_open`::
(integer) Current number of inbound TCP connections used for internal communication between nodes.

`total_outbound_connections`::
(integer) The cumulative number of outbound transport connections that this node has opened since it started.
Each transport connection may comprise multiple TCP connections but is only counted once in this statistic.
Transport connections are typically long-lived so this statistic should remain constant in a stable cluster.

`rx_count`::
(integer) Total number of RX (receive) packets received by the node during internal cluster communication.

`rx_size`::
(byte value) Size of RX packets received by the node during internal cluster communication.

`rx_size_in_bytes`::
(integer) Size, in bytes, of RX packets received by the node during internal cluster communication.

`tx_count`::
(integer) Total number of TX (transmit) packets sent by the node during internal cluster communication.

`tx_size`::
(byte value) Size of TX packets sent by the node during internal cluster communication.

`tx_size_in_bytes`::
(integer) Size, in bytes, of TX packets sent by the node during internal cluster communication.

`inbound_handling_time_histogram`::
(array) The distribution of the time spent handling each inbound message on a transport thread, represented as a histogram.
**Properties of `inbound_handling_time_histogram`**
=======

`ge`::
(string) The inclusive lower bound of the bucket as a human-readable string.
May be omitted on the first bucket if this bucket has no lower bound.

`ge_millis`::
(integer) The inclusive lower bound of the bucket in milliseconds.
May be omitted on the first bucket if this bucket has no lower bound.

`lt`::
(string) The exclusive upper bound of the bucket as a human-readable string.
May be omitted on the last bucket if this bucket has no upper bound.

`lt_millis`::
(integer) The exclusive upper bound of the bucket in milliseconds.
May be omitted on the last bucket if this bucket has no upper bound.

`count`::
(integer) The number of times a transport thread took a period of time within the bounds of this bucket to handle an inbound message.

=======

`outbound_handling_time_histogram`::
(array) The distribution of the time spent sending each outbound transport message on a transport thread, represented as a histogram.
**Properties of `outbound_handling_time_histogram`**
=======

`ge`::
(string) The inclusive lower bound of the bucket as a human-readable string.
May be omitted on the first bucket if this bucket has no lower bound.

`ge_millis`::
(integer) The inclusive lower bound of the bucket in milliseconds.
May be omitted on the first bucket if this bucket has no lower bound.

`lt`::
(string) The exclusive upper bound of the bucket as a human-readable string.
May be omitted on the last bucket if this bucket has no upper bound.

`lt_millis`::
(integer) The exclusive upper bound of the bucket in milliseconds.
May be omitted on the last bucket if this bucket has no upper bound.

`count`::
(integer) The number of times a transport thread took a period of time within the bounds of this bucket to send a transport message.

=======

`actions`::
(object) An action-by-action breakdown of the transport traffic handled by this node, showing the total amount of traffic and a histogram of message sizes for incoming requests and outgoing responses.
**Properties of `actions.*.requests` and `actions.*.responses`**
=======

`count`::
(integer) The total number of requests received, or responses sent, for the current action.

`total_size`::
(byte value) The total size (as a human-readable string) of all requests received, or responses sent, for the current action.

`total_size_in_bytes`::
(integer) The total size in bytes of all requests received, or responses sent, for the current action.

`histogram`::
(array) A breakdown of the distribution of sizes of requests received, or responses sent, for the current action.
**Properties of `histogram`**
========

`ge`::
(byte value) The inclusive lower bound of the bucket as a human-readable string.
May be omitted on the first bucket if this bucket has no lower bound.

`ge_bytes`::
(integer) The inclusive lower bound of the bucket in bytes.
May be omitted on the first bucket if this bucket has no lower bound.

`lt`::
(byte value) The exclusive upper bound of the bucket as a human-readable string.
May be omitted on the last bucket if this bucket has no upper bound.

`lt_bytes`::
(integer) The exclusive upper bound of the bucket in bytes.
May be omitted on the last bucket if this bucket has no upper bound.

`count`::
(integer) The number of times a request was received, or a response sent, with a size within the bounds of this bucket.

========
=======

======

`http`::
(object) Contains http statistics for the node.
**Properties of `http`**
======

`current_open`::
(integer) Current number of open HTTP connections for the node.

`total_opened`::
(integer) Total number of HTTP connections opened for the node.

`clients`::
(array of objects) Information on current and recently-closed HTTP client connections.
Clients that have been closed longer than the http.client_stats.closed_channels.max_age
setting will not be represented here.
**Properties of `clients`**
=======

`id`::
(integer) Unique ID for the HTTP client.

`agent`::
(string) Reported agent for the HTTP client.
If unavailable, this property is not included in the response.

`local_address`::
(string) Local address for the HTTP connection.

`remote_address`::
(string) Remote address for the HTTP connection.

`last_uri`::
(string) The URI of the client's most recent request.

`x_forwarded_for`::
(string) Value from the client's `x-forwarded-for` HTTP header.
If unavailable, this property is not included in the response.

`x_opaque_id`::
(string) Value from the client's `x-opaque-id` HTTP header.
If unavailable, this property is not included in the response.

`opened_time_millis`::
(integer) Time at which the client opened the connection.

`closed_time_millis`::
(integer) Time at which the client closed the connection if the connection is closed.

`last_request_time_millis`::
(integer) Time of the most recent request from this client.

`request_count`::
(integer) Number of requests from this client.

`request_size_bytes`::
(integer) Cumulative size in bytes of all requests from this client.

=======
======

`breakers`::
(object) Contains circuit breaker statistics for the node.
**Properties of `breakers`**
======

`<circuit_breaker_name>`::
(object) Contains statistics for the circuit breaker.
**Properties of `<circuit_breaker_name>`**
=======

`limit_size_in_bytes`::
(integer) Memory limit, in bytes, for the circuit breaker.

`limit_size`::
(byte value) Memory limit for the circuit breaker.

`estimated_size_in_bytes`::
(integer) Estimated memory used, in bytes, for the operation.

`estimated_size`::
(byte value) Estimated memory used for the operation.

`overhead`::
(float) A constant that all estimates for the circuit breaker are multiplied with to calculate a final estimate.

`tripped`::
(integer) Total number of times the circuit breaker has been triggered and prevented an out of memory error.

=======
======

`script`::
(object) Contains script statistics for the node.
**Properties of `script`**
======

`compilations`::
(integer) Total number of inline script compilations performed by the node.

`compilations_history`::
(object) Contains this recent history of script compilations

**Properties of `compilations_history`**
=======

`5m`::
(long) The number of script compilations in the last five minutes.
`15m`::
(long) The number of script compilations in the last fifteen minutes.
`24h`::
(long) The number of script compilations in the last twenty-four hours.

=======

`cache_evictions`::
(integer) Total number of times the script cache has evicted old data.

`cache_evictions_history`::
(object) Contains this recent history of script cache evictions

**Properties of `cache_evictions`**
=======
`5m`::
(long) The number of script cache evictions in the last five minutes.
`15m`::
(long) The number of script cache evictions in the last fifteen minutes.
`24h`::
(long) The number of script cache evictions in the last twenty-four hours.
=======

`compilation_limit_triggered`::
(integer) Total number of times the script compilation circuit breaker has limited inline script compilations.

======

`discovery`::
(object) Contains node discovery statistics for the node.
**Properties of `discovery`**
======

`cluster_state_queue`::
(object) Contains statistics for the cluster state queue of the node.
**Properties of `cluster_state_queue`**
=======
`total`::
(integer) Total number of cluster states in queue.

`pending`::
(integer) Number of pending cluster states in queue.

`committed`::
(integer) Number of committed cluster states in queue.

=======

`published_cluster_states`::
(object) Contains statistics for the published cluster states of the node.
**Properties of `published_cluster_states`**
=======

`full_states`::
(integer) Number of published cluster states.

`incompatible_diffs`::
(integer) Number of incompatible differences between published cluster states.

`compatible_diffs`::
(integer) Number of compatible differences between published cluster states.

=======

`cluster_state_update`::
(object) Contains low-level statistics about how long various activities took during cluster state updates while the node was the elected master.
Omitted if the node is not master-eligible.
Every field whose name ends in `_time` within this object is also represented as a raw number of milliseconds in a field whose name ends in `_time_millis`.
The human-readable fields with a `_time` suffix are only returned if requested with the `?human=true` query parameter.
**Properties of `cluster_state_update`**
=======

`unchanged`::
(object) Contains statistics about cluster state update attempts that did not change the cluster state.
**Properties of `unchanged`**
========

`count`::
(long) The number of cluster state update attempts that did not change the cluster state since the node started.

`computation_time`::
(time value) The cumulative amount of time spent computing no-op cluster state updates since the node started.

`notification_time`::
(time value) The cumulative amount of time spent notifying listeners of a no-op cluster state update since the node started.

========

`success`::
(object) Contains statistics about cluster state update attempts that successfully changed the cluster state.
**Properties of `success`**
========

`count`::
(long) The number of cluster state update attempts that successfully changed the cluster state since the node started.

`computation_time`::
(time value) The cumulative amount of time spent computing cluster state updates that were ultimately successful since the node started.

`publication_time`::
(time value) The cumulative amount of time spent publishing cluster state updates which ultimately succeeded, which includes everything from the start of the publication (i.e. just after the computation of the new cluster state) until the publication has finished and the master node is ready to start processing the next state update.
This includes the time measured by
`context_construction_time`, `commit_time`, `completion_time` and
`master_apply_time`.

`context_construction_time`::
(time value) The cumulative amount of time spent constructing a _publication context_ since the node started for publications that ultimately succeeded.
This statistic includes the time spent computing the difference between the current and new cluster state preparing a serialized representation of this difference.

`commit_time`::
(time value) The cumulative amount of time spent waiting for a successful cluster state update to _commit_, which measures the time from the start of each publication until a majority of the master-eligible nodes have written the state to disk and confirmed the write to the elected master.

`completion_time`::
(time value) The cumulative amount of time spent waiting for a successful cluster state update to _complete_, which measures the time from the start of each publication until all the other nodes have notified the elected master that they have applied the cluster state.

`master_apply_time`::
(time value) The cumulative amount of time spent successfully applying cluster state updates on the elected master since the node started.

`notification_time`::
(time value) The cumulative amount of time spent notifying listeners of a successful cluster state update since the node started.

========

`failure`::
(object) Contains statistics about cluster state update attempts that did not successfully change the cluster state, typically because a new master node was elected before completion.
**Properties of `failure`**
========

`count`::
(long) The number of cluster state update attempts that failed to change the cluster state since the node started.

`computation_time`::
(time value) The cumulative amount of time spent computing cluster state updates that were ultimately unsuccessful since the node started.

`publication_time`::
(time value) The cumulative amount of time spent publishing cluster state updates which ultimately failed, which includes everything from the start of the publication (i.e. just after the computation of the new cluster state) until the publication has finished and the master node is ready to start processing the next state update.
This includes the time measured by
`context_construction_time`, `commit_time`, `completion_time` and
`master_apply_time`.

`context_construction_time`::
(time value) The cumulative amount of time spent constructing a _publication context_ since the node started for publications that ultimately failed.
This statistic includes the time spent computing the difference between the current and new cluster state preparing a serialized representation of this difference.

`commit_time`::
(time value) The cumulative amount of time spent waiting for an unsuccessful cluster state update to _commit_, which measures the time from the start of each publication until a majority of the master-eligible nodes have written the state to disk and confirmed the write to the elected master.

`completion_time`::
(time value) The cumulative amount of time spent waiting for an unsuccessful cluster state update to _complete_, which measures the time from the start of each publication until all the other nodes have notified the elected master that they have applied the cluster state.

`master_apply_time`::
(time value) The cumulative amount of time spent unsuccessfully applying cluster state updates on the elected master since the node started.

`notification_time`::
(time value) The cumulative amount of time spent notifying listeners of a failed cluster state update since the node started.

========
=======
======

`ingest`::
(object) Contains ingest statistics for the node.
**Properties of `ingest`**
======

`total`::
(object) Contains statistics about ingest operations for the node.
**Properties of `total`**
=======

`count`::
(integer) Total number of documents ingested during the lifetime of this node.

`time`::
(time value) Total time spent preprocessing ingest documents during the lifetime of this node.

`time_in_millis`::
(integer) Total time, in milliseconds, spent preprocessing ingest documents during the lifetime of this node.

`current`::
(integer) Total number of documents currently being ingested.

`failed`::
(integer) Total number of failed ingest operations during the lifetime of this node.

=======

`pipelines`::
(object) Contains statistics about ingest pipelines for the node.
**Properties of `pipelines`**
=======

`<pipeline_id>`::
(object) Contains statistics about the ingest pipeline.
**Properties of `<pipeline_id>`**
========

`count`::
(integer) Number of documents preprocessed by the ingest pipeline.

`time`::
(time value) Total time spent preprocessing documents in the ingest pipeline.

`time_in_millis`::
(integer) Total time, in milliseconds, spent preprocessing documents in the ingest pipeline.

`failed`::
(integer) Total number of failed operations for the ingest pipeline.

`ingested_as_first_pipeline`::
(byte value)
Total ingested size of all documents which were first processed by this pipeline.
A document is not added to the stat value for this pipeline if it is a final pipeline after a default pipeline, a pipeline
run after a reroute processor, or is within a pipeline processor.
Instead, the document size is added to the stat value of the pipeline which initially ingested the document.

`ingested_as_first_pipeline_in_bytes`::
(integer)
Total ingested size, in bytes, of all documents which were first processed by this pipeline.
A document is not added to the stat value for this pipeline if it is a final pipeline after a default pipeline, a pipeline
run after a reroute processor, or is within a pipeline processor.
Instead, the document size is added to the stat value of the pipeline which initially ingested the document.

`produced_as_first_pipeline`::
(byte value)
Total produced size of all documents which were first processed by this pipeline.
A document is not added to the stat value for this pipeline if it is a final pipeline after a default pipeline, a pipeline
run after a reroute processor, or is within a pipeline processor.
Instead, the document size is added to the stat value of the pipeline which initially ingested the document.

`produced_as_first_pipeline_in_bytes`::
(integer)
Total produced size, in bytes, of all documents which were first processed by this pipeline.
A document is not added to the stat value for this pipeline if it is a final pipeline after a default pipeline, a pipeline
run after a reroute processor, or is within a pipeline processor.
Instead, the document size is added to the stat value of the pipeline which initially ingested the document.

`processors`::
(array of objects) Contains statistics for the ingest processors for the ingest pipeline.
**Properties of `processors`**
=========

`<processor>`::
(object) Contains statistics for the ingest processor.
**Properties of `<processor>`**
==========
`count`::
(integer) Number of documents transformed by the processor.

`time`::
(time value) Time spent by the processor transforming documents.

`time_in_millis`::
(integer) Time, in milliseconds, spent by the processor transforming documents.

`current`::
(integer) Number of documents currently being transformed by the processor.

`failed`::
(integer) Number of failed operations for the processor.

==========
=========
========
=======
======

`indexing_pressure`::
(object) Contains indexing pressure statistics for the node.
**Properties of `indexing_pressure`**
======

`memory`::
(object) Contains statistics for memory consumption from indexing load.
**Properties of `<memory>`**
=======

`current`::
(object) Contains statistics for current indexing load.
**Properties of `<current>`**
========

`combined_coordinating_and_primary`::
(byte value) Memory consumed by indexing requests in the coordinating or primary stage.
This value is not the sum of coordinating and primary as a node can reuse the coordinating memory if the primary stage is executed locally.

`combined_coordinating_and_primary_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the coordinating or primary stage.
This value is not the sum of coordinating and primary as a node can reuse the coordinating memory if the primary stage is executed locally.

`coordinating`::
(byte value) Memory consumed by indexing requests in the coordinating stage.

`coordinating_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the coordinating stage.

`primary`::
(byte value) Memory consumed by indexing requests in the primary stage.

`primary_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the primary stage.

`replica`::
(byte value) Memory consumed by indexing requests in the replica stage.

`replica_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the replica stage.

`all`::
(byte value) Memory consumed by indexing requests in the coordinating, primary, or replica stage.

`all_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the coordinating, primary, or replica stage.

========
`total`::
(object) Contains statistics for the cumulative indexing load since the node started.
**Properties of `<total>`**
========

`combined_coordinating_and_primary`::
(byte value) Memory consumed by indexing requests in the coordinating or primary stage.
This value is not the sum of coordinating and primary as a node can reuse the coordinating memory if the primary stage is executed locally.

`combined_coordinating_and_primary_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the coordinating or primary stage.
This value is not the sum of coordinating and primary as a node can reuse the coordinating memory if the primary stage is executed locally.

`coordinating`::
(byte value) Memory consumed by indexing requests in the coordinating stage.

`coordinating_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the coordinating stage.

`primary`::
(byte value) Memory consumed by indexing requests in the primary stage.

`primary_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the primary stage.

`replica`::
(byte value) Memory consumed by indexing requests in the replica stage.

`replica_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the replica stage.

`all`::
(byte value) Memory consumed by indexing requests in the coordinating, primary, or replica stage.

`all_in_bytes`::
(integer) Memory consumed, in bytes, by indexing requests in the coordinating, primary, or replica stage.

`coordinating_rejections`::
(integer) Number of indexing requests rejected in the coordinating stage.

`primary_rejections`::
(integer) Number of indexing requests rejected in the primary stage.

`replica_rejections`::
(integer) Number of indexing requests rejected in the replica stage.

========
`limit`::
(byte value) Configured memory limit for the indexing requests.
Replica requests have an automatic limit that is 1.5x this value.

`limit_in_bytes`::
(integer) Configured memory limit, in bytes, for the indexing requests.
Replica requests have an automatic limit that is 1.5x this value.

=======
======

`adaptive_selection`::
(object) Contains adaptive selection statistics for the node.
**Properties of `adaptive_selection`**
======

`outgoing_searches`::
(integer) The number of outstanding search requests from the node these stats are for to the keyed node.

`avg_queue_size`::
(integer) The exponentially weighted moving average queue size of search requests on the keyed node.

`avg_service_time`::
(time value) The exponentially weighted moving average service time of search requests on the keyed node.

`avg_service_time_ns`::
(integer) The exponentially weighted moving average service time, in nanoseconds, of search requests on the keyed node.

`avg_response_time`::
(time value) The exponentially weighted moving average response time of search requests on the keyed node.

`avg_response_time_ns`::
(integer) The exponentially weighted moving average response time, in nanoseconds, of search requests on the keyed node.

`rank`::
(string) The rank of this node; used for shard selection when routing search requests.

======

`allocations`::
(object) Contains allocations statistics for the node.
**Properties of `allocations`**
======

`shards`::
(integer) The number of shards currently allocated to this node

`undesired_shards`::
(integer) The amount of shards that are scheduled to be moved elsewhere in the cluster if desired balance allocator is used or -1 if any other allocator is used.

`forecasted_ingest_load`::
(double) Total forecasted ingest load of all shards assigned to this node

`forecasted_disk_usage`::
(byte value) Forecasted size of all shards assigned to the node

`forecasted_disk_usage_bytes`::
(integer) Forecasted size, in bytes, of all shards assigned to the node

`current_disk_usage`::
(byte value) Current size of all shards assigned to the node

`current_disk_usage_bytes`::
(integer) Current size, in bytes, of all shards assigned to the node

======
=====
