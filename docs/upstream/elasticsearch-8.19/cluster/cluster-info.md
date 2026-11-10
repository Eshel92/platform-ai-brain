<!-- Converted from cluster/cluster-info.asciidoc (AsciiDoc). Includes are inlined. -->

### Cluster Info API

experimental::[]

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns cluster information.

#### Request

`GET /_info/<target>` +

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

You can use the Cluster Info API to retrieve information of a cluster.

#### Path parameters

`<target>`::
(String) Limits the information returned to the specific `target`.
A comma-separated list of the following options:
`_all`::
All the information available. Can not be mixed with other targets.

`http`::
HTTP connection information.

`ingest`::
Ingest information.

`thread_pool`::
Statistics about each thread pool, including current size, queue size and rejected tasks.

`script`::
Contains script statistics of the cluster.

#### Response body

`cluster_name`::
(string)
Name of the cluster. Based on the cluster-name setting.

`http`::
(object)
Contains http information for the cluster.
**Properties of `http`**
======
`current_open`::
(integer)
Current number of open HTTP connections for the cluster.

`total_opened`::
(integer)
Total number of HTTP connections opened for the cluster.

`clients`::
(array of objects)
Information on current and recently-closed HTTP client connections.
Clients that have been closed longer than the http.client_stats.closed_channels.max_age
setting will not be represented here.
**Properties of `clients`**
=======
`id`::
(integer)
Unique ID for the HTTP client.

`agent`::
(string)
Reported agent for the HTTP client. If unavailable, this property is not
included in the response.

`local_address`::
(string)
Local address for the HTTP connection.

`remote_address`::
(string)
Remote address for the HTTP connection.

`last_uri`::
(string)
The URI of the client's most recent request.

`x_forwarded_for`::
(string)
Value from the client's `x-forwarded-for` HTTP header. If unavailable, this
property is not included in the response.

`x_opaque_id`::
(string)
Value from the client's `x-opaque-id` HTTP header. If unavailable, this property
is not included in the response.

`opened_time_millis`::
(integer)
Time at which the client opened the connection.

`closed_time_millis`::
(integer)
Time at which the client closed the connection if the connection is closed.

`last_request_time_millis`::
(integer)
Time of the most recent request from this client.

`request_count`::
(integer)
Number of requests from this client.

`request_size_bytes`::
(integer)
Cumulative size in bytes of all requests from this client.
=======
======

`ingest`::
(object)
Contains ingest information for the cluster.
**Properties of `ingest`**
======
`total`::
(object)
Contains information about ingest operations for the cluster.
**Properties of `total`**
=======
`count`::
(integer)
Total number of documents ingested across the cluster.

`time`::
(time value)
Total time spent preprocessing ingest documents across the cluster.

`time_in_millis`::
(integer)
Total time, in milliseconds, spent preprocessing ingest documents across the cluster.

`current`::
(integer)
Total number of documents currently being ingested.

`failed`::
(integer)
Total number of failed ingest operations across the cluster.
=======

`pipelines`::
(object)
Contains information about ingest pipelines for the cluster.
**Properties of `pipelines`**
=======
`<pipeline_id>`::
(object)
Contains information about the ingest pipeline.
**Properties of `<pipeline_id>`**
========
`count`::
(integer)
Number of documents preprocessed by the ingest pipeline.

`time`::
(time value)
Total time spent preprocessing documents in the ingest pipeline.

`time_in_millis`::
(integer)
Total time, in milliseconds, spent preprocessing documents in the ingest
pipeline.

`failed`::
(integer)
Total number of failed operations for the ingest pipeline.

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
(array of objects)
Contains information for the ingest processors for the ingest pipeline.
**Properties of `processors`**
=========
`<processor>`::
(object)
Contains information for the ingest processor.
**Properties of `<processor>`**
==========
`count`::
(integer)
Number of documents transformed by the processor.

`time`::
(time value)
Time spent by the processor transforming documents.

`time_in_millis`::
(integer)
Time, in milliseconds, spent by the processor transforming documents.

`current`::
(integer)
Number of documents currently being transformed by the processor.

`failed`::
(integer)
Number of failed operations for the processor.
==========
=========
========
=======
======

`thread_pool`::
(object)
Contains information about the thread pools of the cluster.
**Properties of `thread_pool`**
======
`<thread_pool_name>`::
(object)
Contains information about the thread pool of the cluster with name `<thread_pool_name>`.
**Properties of `<thread_pool_name>`**
=======
`threads`::
(integer)
Number of threads in the thread pool.

`queue`::
(integer)
Number of tasks in queue for the thread pool.

`active`::
(integer)
Number of active threads in the thread pool.

`rejected`::
(integer)
Number of tasks rejected by the thread pool executor.

`largest`::
(integer)
Highest number of active threads in the thread pool.

`completed`::
(integer)
Number of tasks completed by the thread pool executor.
=======
======

`script`::
(object)
Contains script statistics of the cluster.
**Properties of `script`**
======
`compilations`::
(integer)
Total number of inline script compilations performed by the cluster.

`compilations_history`::
(object)
Contains the recent history of script compilations.

**Properties of `compilations_history`**
=======
`5m`::
(long)
The number of script compilations in the last five minutes.
`15m`::
(long)
The number of script compilations in the last fifteen minutes.
`24h`::
(long)
The number of script compilations in the last twenty-four hours.
=======

`cache_evictions`::
(integer)
Total number of times the script cache has evicted old data.

`cache_evictions_history`::
(object)
Contains the recent history of script cache evictions.

**Properties of `cache_evictions`**
=======
`5m`::
(long)
The number of script cache evictions in the last five minutes.
`15m`::
(long)
The number of script cache evictions in the last fifteen minutes.
`24h`::
(long)
The number of script cache evictions in the last twenty-four hours.
=======

`compilation_limit_triggered`::
(integer)
Total number of times the <<script-compilation-circuit-breaker,script
compilation>> circuit breaker has limited inline script compilations.
======

#### Examples

```console
# returns all stats info of the cluster
GET /_info/_all

# returns the http info of the cluster
GET /_info/http

# returns the http info of the cluster
GET /_info/ingest

# returns the thread_pool info of the cluster
GET /_info/thread_pool

# returns the script info of the cluster
GET /_info/script

# returns the http and ingest info of the cluster
GET /_info/http,ingest
```
