<!-- Converted from docs/delete-by-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete by query API

Deletes documents that match the specified query.

```console
POST /my-index-000001/_delete_by_query
{
  "query": {
    "match": {
      "user.id": "elkbee"
    }
  }
}
```

#### Request

`POST /<target>/_delete_by_query`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the following
index privileges for the target data stream, index,
or alias:

** `read`
** `delete` or `write`

#### Description

You can specify the query criteria in the request URI or the request body
using the same syntax as the  Search API.

When you submit a delete by query request, Elasticsearch gets a snapshot of the data stream or index
when it begins processing the request and deletes matching documents using
`internal` versioning. If a document changes between the time that the
snapshot is taken and the delete operation is processed, it results in a version
conflict and the delete operation fails.

**Note:** Documents with a version equal to 0 cannot be deleted using delete by
query because `internal` versioning does not support 0 as a valid
version number.

While processing a delete by query request, Elasticsearch performs multiple search
requests sequentially to find all of the matching documents to delete. A bulk
delete request is performed for each batch of matching documents. If a
search or bulk request is rejected, the requests are retried up to 10 times, with
exponential back off. If the maximum retry limit is reached, processing halts
and all failed requests are returned in the response. Any delete requests that
completed successfully still stick, they are not rolled back.

You can opt to count version conflicts instead of halting and returning by
setting `conflicts` to `proceed`. Note that if you opt to count version conflicts
the operation could attempt to delete more documents from the source
than `max_docs` until it has successfully deleted `max_docs` documents, or it has gone through
every document in the source query.

##### Refreshing shards

Specifying the `refresh` parameter refreshes all shards involved in the delete
by query once the request completes. This is different than the delete API's
`refresh` parameter, which causes just the shard that received the delete
request to be refreshed. Unlike the delete API, it does not support
`wait_for`.

##### Running delete by query asynchronously

If the request contains `wait_for_completion=false`, Elasticsearch
performs some preflight checks, launches the request, and returns a
`task` you can use to cancel or get the status of the task. Elasticsearch creates a
record of this task as a document at `.tasks/task/${taskId}`. When you are
done with a task, you should delete the task document so Elasticsearch can reclaim the
space.

##### Waiting for active shards

`wait_for_active_shards` controls how many copies of a shard must be active
before proceeding with the request. See index-wait-for-active-shards
for details. `timeout` controls how long each write request waits for unavailable
shards to become available. Both work exactly the way they work in the
Bulk API. Delete by query uses scrolled searches, so you can also
specify the `scroll` parameter to control how long it keeps the search context
alive, for example `?scroll=10m`. The default is 5 minutes.

##### Throttling delete requests

To control the rate at which delete by query issues batches of delete operations,
you can set `requests_per_second` to any positive decimal number. This pads each
batch with a wait time to throttle the rate. Set `requests_per_second` to `-1`
to disable throttling.

Throttling uses a wait time between batches so that the internal scroll requests
can be given a timeout that takes the request padding into account. The padding
time is the difference between the batch size divided by the
`requests_per_second` and the time spent writing. By default the batch size is
`1000`, so if `requests_per_second` is set to `500`:

```txt
target_time = 1000 / 500 per second = 2 seconds
wait_time = target_time - write_time = 2 seconds - .5 seconds = 1.5 seconds
```

Since the batch is issued as a single `_bulk` request, large batch sizes
cause Elasticsearch to create many requests and wait before starting the next set.
This is "bursty" instead of "smooth".

##### Slicing

Delete by query supports sliced scroll to parallelize the
delete process. This can improve efficiency and provide a
convenient way to break the request down into smaller parts.

Setting `slices` to `auto` chooses a reasonable number for most data streams and indices.
If you're slicing manually or otherwise tuning automatic slicing, keep in mind
that:

* Query performance is most efficient when the number of `slices` is equal to
the number of shards in the index or backing index. If that number is large (for example,
500), choose a lower number as too many `slices` hurts performance. Setting
`slices` higher than the number of shards generally does not improve efficiency
and adds overhead.

* Delete performance scales linearly across available resources with the
number of slices.

Whether query or delete performance dominates the runtime depends on the
documents being reindexed and cluster resources.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases to
search. Supports wildcards (`*`). To search all data streams or indices, omit
this parameter or use `* or `_all`.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

`analyzer`::
(Optional, string) Analyzer to use for the query string.
This parameter can only be used when the `q` query string parameter is
specified.
`analyze_wildcard`::
(Optional, Boolean) If `true`, wildcard and prefix queries are analyzed.
Defaults to `false`.
This parameter can only be used when the `q` query string parameter is
specified.
`conflicts`::
  (Optional, string) What to do if delete by query hits version conflicts:
  `abort` or `proceed`. Defaults to `abort`.

`default_operator`::
(Optional, string) The default operator for query string query: AND or OR.
Defaults to `OR`.
This parameter can only be used when the `q` query string parameter is
specified.
`df`::
(Optional, string) Field to use as default where no field prefix is given in the
query string.
This parameter can only be used when the `q` query string parameter is
specified.
`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`lenient`::
(Optional, Boolean) If `true`, format-based query failures (such as providing
text to a numeric field) in the query string will be ignored. Defaults to
`false`.
This parameter can only be used when the `q` query string parameter is
specified.
`max_docs`::
(Optional, integer) Maximum number of documents to process. Defaults to all
documents. When set to a value less then or equal to `scroll_size` then a
scroll will not be used to retrieve the results for the operation.
`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`q`::
(Optional, string) Query in the Lucene query string syntax.
`request_cache`::
(Optional, Boolean) If `true`, the request cache is used for this request.
Defaults to the index-level setting.
`refresh`::
(Optional, Boolean) If `true`, Elasticsearch refreshes all shards involved in the
delete by query after the request completes. Defaults to `false`.

`requests_per_second`::
(Optional, integer) The throttle for this request in sub-requests per second.
Defaults to `-1` (no throttle).
`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`scroll`::
(Optional, time value)
Period to retain the search context for scrolling. See
scroll-search-results.

`scroll_size`::
(Optional, integer) Size of the scroll request that powers the operation.
Defaults to 1000.
`search_type`::
(Optional, string) The type of the search operation. Available options:
* `query_then_fetch`
* `dfs_query_then_fetch`
`search_timeout`::
(Optional, time units)
Explicit timeout for each search request.
Defaults to no timeout.

`slices`::
(Optional, integer) The number of slices this task should be divided into.
Defaults to 1 meaning the task isn't sliced into subtasks.
`sort`::
(Optional, string) A comma-separated list of <field>:<direction> pairs.
`stats`::
(Optional, string) Specific `tag` of the request for logging and statistical
purposes.
`terminate_after`::
(Optional, integer) Maximum number of documents to collect for each shard. If a
query reaches this limit, Elasticsearch terminates the query early. Elasticsearch collects
documents before sorting.
**Important:** Use with caution. Elasticsearch applies this parameter to each shard handling
the request. When possible, let Elasticsearch perform early termination automatically.
Avoid specifying this parameter for requests that target data streams with
backing indices across multiple data tiers.
`timeout`::
(Optional, time units)
Period each deletion request <<index-wait-for-active-shards,waits for active
shards>>. Defaults to `1m` (one minute).

`version`::
(Optional, Boolean) If `true`, returns the document version as part of a hit.
`wait_for_active_shards`::
(Optional, string) The number of copies of each shard that must be active
before proceeding with the operation. Set to `all` or any non-negative integer
up to the total number of copies of each shard in the index
(`number_of_replicas+1`). Defaults to `1`, meaning to wait just for each
primary shard to be active.

See index-wait-for-active-shards.

#### Request body

`query`::
  (Optional, query object) Specifies the documents to delete
  using the  Query DSL.

#### Response body

```console
POST /my-index-000001/_delete_by_query
{
  "query": { <1>
    "match": {
      "user.id": "elkbee"
    }
  }
}
```

The JSON response looks like this:

```console-result
{
  "took" : 147,
  "timed_out": false,
  "total": 119,
  "deleted": 119,
  "batches": 1,
  "version_conflicts": 0,
  "noops": 0,
  "retries": {
    "bulk": 0,
    "search": 0
  },
  "throttled_millis": 0,
  "requests_per_second": -1.0,
  "throttled_until_millis": 0,
  "failures" : [ ]
}
```

`took`::

The number of milliseconds from start to end of the whole operation.

`timed_out`::

This flag is set to `true` if any of the requests executed during the
delete by query execution has timed out.

`total`::

The number of documents that were successfully processed.

`deleted`::

The number of documents that were successfully deleted.

`batches`::

The number of scroll responses pulled back by the delete by query.

`version_conflicts`::

The number of version conflicts that the delete by query hit.

`noops`::

This field is always equal to zero for delete by query. It only exists
so that delete by query, update by query, and reindex APIs return responses
 with the same structure.

`retries`::

The number of retries attempted by delete by query. `bulk` is the number
of bulk actions retried, and `search` is the number of search actions retried.

`throttled_millis`::

Number of milliseconds the request slept to conform to `requests_per_second`.

`requests_per_second`::

The number of requests per second effectively executed during the delete by query.

`throttled_until_millis`::

This field should always be equal to zero in a `_delete_by_query` response. It only
has meaning when using the Task API, where it
indicates the next time (in milliseconds since epoch) a throttled request will be
executed again in order to conform to `requests_per_second`.

`failures`::

Array of failures if there were any unrecoverable errors during the process. If
this is non-empty then the request aborted because of those failures.
Delete by query is implemented using batches, and any failure causes the entire
process to abort but all failures in the current batch are collected into the
array. You can use the `conflicts` option to prevent reindex from aborting on
version conflicts.

#### Examples

Delete all documents from the `my-index-000001` data stream or index:

```console
POST my-index-000001/_delete_by_query?conflicts=proceed
{
  "query": {
    "match_all": {}
  }
}
```

Delete documents from multiple data streams or indices:

```console
POST /my-index-000001,my-index-000002/_delete_by_query
{
  "query": {
    "match_all": {}
  }
}
```

Limit the delete by query operation to shards that a particular routing
value:

```console
POST my-index-000001/_delete_by_query?routing=1
{
  "query": {
    "range" : {
        "age" : {
           "gte" : 10
        }
    }
  }
}
```

By default `_delete_by_query` uses scroll batches of 1000. You can change the
batch size with the `scroll_size` URL parameter:

```console
POST my-index-000001/_delete_by_query?scroll_size=5000
{
  "query": {
    "term": {
      "user.id": "kimchy"
    }
  }
}
```

Delete a document using a unique attribute:

```console
POST my-index-000001/_delete_by_query
{
  "query": {
    "term": {
      "user.id": "kimchy"
    }
  },
  "max_docs": 1
}
```

##### Slice manually

Slice a delete by query manually by providing a slice id and total number of
slices:

```console
POST my-index-000001/_delete_by_query
{
  "slice": {
    "id": 0,
    "max": 2
  },
  "query": {
    "range": {
      "http.response.bytes": {
        "lt": 2000000
      }
    }
  }
}
POST my-index-000001/_delete_by_query
{
  "slice": {
    "id": 1,
    "max": 2
  },
  "query": {
    "range": {
      "http.response.bytes": {
        "lt": 2000000
      }
    }
  }
}
```

Which you can verify works with:

```console
GET _refresh
POST my-index-000001/_search?size=0&filter_path=hits.total
{
  "query": {
    "range": {
      "http.response.bytes": {
        "lt": 2000000
      }
    }
  }
}
```

Which results in a sensible `total` like this one:

```console-result
{
  "hits": {
    "total" : {
        "value": 0,
        "relation": "eq"
    }
  }
}
```

##### Use automatic slicing

You can also let delete-by-query automatically parallelize using
sliced scroll to slice on `_id`. Use `slices` to specify
the number of slices to use:

```console
POST my-index-000001/_delete_by_query?refresh&slices=5
{
  "query": {
    "range": {
      "http.response.bytes": {
        "lt": 2000000
      }
    }
  }
}
```

Which you also can verify works with:

```console
POST my-index-000001/_search?size=0&filter_path=hits.total
{
  "query": {
    "range": {
      "http.response.bytes": {
        "lt": 2000000
      }
    }
  }
}
```

Which results in a sensible `total` like this one:

```console-result
{
  "hits": {
    "total" : {
        "value": 0,
        "relation": "eq"
    }
  }
}
```

Setting `slices` to `auto` will let Elasticsearch choose the number of slices
to use. This setting will use one slice per shard, up to a certain limit. If
there are multiple source data streams or indices, it will choose the number of slices based
on the index or backing index with the smallest number of shards.

Adding `slices` to `_delete_by_query` just automates the manual process used in
the section above, creating sub-requests which means it has some quirks:

* You can see these requests in the
Tasks APIs. These sub-requests are "child"
tasks of the task for the request with `slices`.
* Fetching the status of the task for the request with `slices` only contains
the status of completed slices.
* These sub-requests are individually addressable for things like cancellation
and rethrottling.
* Rethrottling the request with `slices` will rethrottle the unfinished
sub-request proportionally.
* Canceling the request with `slices` will cancel each sub-request.
* Due to the nature of `slices` each sub-request won't get a perfectly even
portion of the documents. All documents will be addressed, but some slices may
be larger than others. Expect larger slices to have a more even distribution.
* Parameters like `requests_per_second` and `max_docs` on a request with
`slices` are distributed proportionally to each sub-request. Combine that with
the point above about distribution being uneven and you should conclude that
using `max_docs` with `slices` might not result in exactly `max_docs` documents
being deleted.
* Each sub-request gets a slightly different snapshot of the source data stream or index
though these are all taken at approximately the same time.

##### Change throttling for a request

The value of `requests_per_second` can be changed on a running delete by query
using the `_rethrottle` API. Rethrottling that speeds up the
query takes effect immediately but rethrotting that slows down the query
takes effect after completing the current batch to prevent scroll
timeouts.

```console
POST _delete_by_query/r1A2WoRbTwKZ516z6NEs5A:36619/_rethrottle?requests_per_second=-1
```

Use the tasks API to get the task ID. Set `requests_per_second`
to any positive decimal value or `-1` to disable throttling.

##### Get the status of a delete by query operation

Use the tasks API to get the status of a delete by query
operation:

```console
GET _tasks?detailed=true&actions=*/delete/byquery
```

The response looks like:

```console-result
{
  "nodes" : {
    "r1A2WoRbTwKZ516z6NEs5A" : {
      "name" : "r1A2WoR",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1:9300",
      "attributes" : {
        "testattr" : "test",
        "portsfile" : "true"
      },
      "tasks" : {
        "r1A2WoRbTwKZ516z6NEs5A:36619" : {
          "node" : "r1A2WoRbTwKZ516z6NEs5A",
          "id" : 36619,
          "type" : "transport",
          "action" : "indices:data/write/delete/byquery",
          "status" : {    <1>
            "total" : 6154,
            "updated" : 0,
            "created" : 0,
            "deleted" : 3500,
            "batches" : 36,
            "version_conflicts" : 0,
            "noops" : 0,
            "retries": 0,
            "throttled_millis": 0
          },
          "description" : ""
        }
      }
    }
  }
}
```

<1> This object contains the actual status. It is just like the response JSON
with the important addition of the `total` field. `total` is the total number
of operations that the reindex expects to perform. You can estimate the
progress by adding the `updated`, `created`, and `deleted` fields. The request
will finish when their sum is equal to the `total` field.

With the task id you can look up the task directly:

```console
GET /_tasks/r1A2WoRbTwKZ516z6NEs5A:36619
```

The advantage of this API is that it integrates with `wait_for_completion=false`
to transparently return the status of completed tasks. If the task is completed
and `wait_for_completion=false` was set on it then it'll come back with
`results` or an `error` field. The cost of this feature is the document that
`wait_for_completion=false` creates at `.tasks/task/${taskId}`. It is up to
you to delete that document.

##### Cancel a delete by query operation

Any delete by query can be canceled using the task cancel API:

```console
POST _tasks/r1A2WoRbTwKZ516z6NEs5A:36619/_cancel
```

The task ID can be found using the tasks API.

Cancellation should happen quickly but might take a few seconds. The task status
API above will continue to list the delete by query task until this task checks that it
has been cancelled and terminates itself.
