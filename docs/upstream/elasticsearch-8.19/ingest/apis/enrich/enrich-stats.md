<!-- Converted from ingest/apis/enrich/enrich-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Enrich stats API

Returns enrich coordinator statistics
and information about enrich policies
that are currently executing.

```console
GET /_enrich/_stats
```

#### Request

`GET /_enrich/_stats`

#### Response body

`executing_policies`::
(Array of objects)
Objects containing information
about each enrich policy
that is currently executing.

Returned parameters include:

`name`::
(String)
Name of the enrich policy.

`task`::
(Task object)
Object containing detailed information
about the policy execution task.

`coordinator_stats`::
(Array of objects)
Objects containing information
about each coordinating ingest node
for configured enrich processors.

Returned parameters include:

`node_id`::
(String)
ID of the ingest node coordinating search requests
for configured enrich processors.

`queue_size`::
(Integer)
Number of search requests in the queue.

`remote_requests_current`::
(Integer)
Current number of outstanding remote requests.

`remote_requests_total`::
(Integer)
Number of outstanding remote requests executed
since node startup.
In most cases,
a remote request includes multiple search requests.
This depends on the number of search requests in the queue
when the remote request is executed.

`executed_searches_total`::
(Integer)
Number of search requests
that enrich processors have executed
since node startup.

`cache_stats`::
(Array of objects)
Objects containing information about the enrich
cache stats on each ingest node.

Returned parameters include:

`node_id`::
(String)
ID of the ingest node with a enrich cache.

`count`::
(Integer)
Number of cached entries.

`hits`::
(Integer)
The number of enrich lookups served from cache.

`misses`::
(Integer)
The number of time enrich lookups couldn't be
served from cache.

`evictions`::
(Integer)
The number cache entries evicted from the cache.

`hits_time_in_millis`::
(Long)
The amount of time in milliseconds spent fetching data from the cache on successful cache hits only.

`misses_time_in_millis`::
(Long)
The amount of time in milliseconds spent fetching data from the enrich index and updating the cache, on cache misses only.

`size_in_bytes`::
(Long)
An _approximation_ of the size in bytes that the enrich cache takes up on the heap.

#### Examples

```console
GET /_enrich/_stats
```

The API returns the following response:

```console-result
{
  "executing_policies": [
    {
      "name": "my-policy",
      "task": {
        "id": 124,
        "type": "direct",
        "action": "cluster:admin/xpack/enrich/execute",
        "start_time_in_millis": 1458585884904,
        "running_time_in_nanos": 47402,
        "cancellable": false,
        "parent_task_id": "oTUltX4IQMOUUVeiohTt8A:123",
        "headers": {
          "X-Opaque-Id": "123456"
        }
      }
    }
  ],
  "coordinator_stats": [
    {
      "node_id": "1sFM8cmSROZYhPxVsiWew",
      "queue_size": 0,
      "remote_requests_current": 0,
      "remote_requests_total": 0,
      "executed_searches_total": 0
    }
  ],
  "cache_stats": [
    {
      "node_id": "1sFM8cmSROZYhPxVsiWew",
      "count": 0,
      "hits": 0,
      "misses": 0,
      "evictions": 0,
      "hits_time_in_millis": 0,
      "misses_time_in_millis": 0,
      "size_in_bytes": 0
    }
  ]
}
```
