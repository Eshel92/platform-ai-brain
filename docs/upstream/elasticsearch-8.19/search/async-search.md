<!-- Converted from search/async-search.asciidoc (AsciiDoc). Includes are inlined. -->

### Async search

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

The async search API let you asynchronously execute a search request, monitor
its progress, and retrieve partial results as they become available.

#### Submit async search API

Executes a search request asynchronously. It accepts the same parameters and
request body as the search API.

```console
POST /sales*/_async_search?size=0
{
  "sort": [
    { "date": { "order": "asc" } }
  ],
  "aggs": {
    "sale_date": {
      "date_histogram": {
        "field": "date",
        "calendar_interval": "1d"
      }
    }
  }
}
```

The response contains an identifier of the search being executed. You can use
this ID to later retrieve the search's final results. The currently available
search results are returned as part of the
`response` object.

```console-result
{
  "id" : "FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=", <1>
  "is_partial" : true, <2>
  "is_running" : true, <3>
  "start_time_in_millis" : 1583945890986,
  "expiration_time_in_millis" : 1584377890986,
  "response" : {
    "took" : 1122,
    "timed_out" : false,
    "num_reduce_phases" : 0,
    "_shards" : {
      "total" : 562, <4>
      "successful" : 3, <5>
      "skipped" : 0,
      "failed" : 0
    },
    "hits" : {
      "total" : {
        "value" : 157483, <6>
        "relation" : "gte"
      },
      "max_score" : null,
      "hits" : [ ]
    }
  }
}
```

<1> Identifier of the async search that can be used to monitor its progress,
retrieve its results, and/or delete it
<2> When the query is no longer running, indicates whether the search failed
or was successfully completed on all shards. While the query is being
executed, `is_partial` is always set to `true`
<3> Whether the search is still being executed or it has completed
<4> How many shards the search will be executed on, overall
<5> How many shards have successfully completed the search
<6> How many documents are currently matching the query, which belong to the
shards that have already completed the search

**Note:** Although the query is no longer running, hence `is_running` is set to
`false`, results may be partial. That happens in case the search failed after
some shards returned their results, or when the node that is coordinating the
 async search dies.

It is possible to block and wait until the search is completed up to a certain
timeout by providing the `wait_for_completion_timeout` parameter, which
defaults to `1` second. When the async search completes within such timeout,
the response won't include the ID as the results are not stored in the cluster.
The `keep_on_completion` parameter, which defaults to `false`, can be set to
`true` to request that results are stored for later retrieval also when the
search completes within the `wait_for_completion_timeout`.

You can also specify how long the async search needs to be available through the
`keep_alive` parameter, which defaults to `5d` (five days). Ongoing async
searches and any saved search results are deleted after this period.

**Note:** When the primary sort of the results is an indexed field, shards get
sorted based on minimum and maximum value that they hold for that field, hence
partial results become available following the sort criteria that was requested.

The submit async search API supports the same
parameters as the search API, though some
have different default values:

* `batched_reduce_size` defaults to `5`: this affects how often partial results
become available, which happens whenever shard results are reduced. A partial
reduction is performed every time the coordinating node has received a certain
number of new shard responses (`5` by default).
* `request_cache` defaults to `true`
* `pre_filter_shard_size` defaults to `1` and cannot be changed: this is to
enforce the execution of a pre-filter roundtrip to retrieve statistics from
each shard so that the ones that surely don't hold any document matching the
query get skipped.
* `ccs_minimize_roundtrips` defaults to `false`. When doing a cross-cluster search, setting
it to `true` may improve overall search latency, particularly when searching
clusters with a large number of shards. However, when set to `true`, the progress
of searches on the remote clusters will not be received until the search finishes
on all clusters. See modules-cross-cluster-search for more information.

**Warning:** Async search does not support scroll
nor search requests that only include the suggest section.

**Warning:** By default, Elasticsearch doesn't allow to store an async search response
larger than 10Mb, and an attempt to do this results in an error. The maximum
allowed size for a stored async search response can be set by changing the
`search.max_async_search_response_size` cluster level setting.

#### Get async search

The get async search API retrieves the results of a previously submitted async
search request given its id.

If the Elasticsearch security features are enabled, the access to the results of a
specific async search is restricted to only
the user or API key that submitted it.

```console
GET /_async_search/FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=
```

```console-result
{
  "id" : "FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=",
  "is_partial" : false, <1>
  "is_running" : false, <2>
  "start_time_in_millis" : 1583945890986,
  "expiration_time_in_millis" : 1584377890986, <3>
  "completion_time_in_millis" : 1583945903130, <4>
  "response" : {
    "took" : 12144,
    "timed_out" : false,
    "num_reduce_phases" : 46, <5>
    "_shards" : {
      "total" : 562,
      "successful" : 188, <6>
      "skipped" : 0,
      "failed" : 0
    },
    "hits" : {
      "total" : {
        "value" : 456433,
        "relation" : "eq"
      },
      "max_score" : null,
      "hits" : [ ]
    },
    "aggregations" : { <7>
      "sale_date" :  {
        "buckets" : []
      }
    }
  }
}
```

<1> When the query is no longer running, indicates whether the search failed
or was successfully completed on all shards. While the query is being
executed, `is_partial` is always set to `true`
<2> Whether the search is still being executed or it has completed
<3> When the async search will expire
<4> When the async search has finished, the completion_time is indicated (start_time + took)
<5> Indicates how many reductions of the results have been performed. If this
number increases compared to the last retrieved results, you can expect
additional results included in the search response
<6> Indicates how many shards have executed the query. Note that in order for
shard results to be included in the search response, they need to be reduced
first.
<7> Partial aggregations results, coming from the shards that have already
completed the execution of the query.

The `wait_for_completion_timeout` parameter can also be provided when calling
the Get Async Search API, in order to wait for the search to be completed up
until the provided timeout. Final results will be returned if available before
the timeout expires, otherwise the currently available results will be returned
once the timeout expires. By default no timeout is set meaning that the
currently available results will be returned without any additional wait.

The `keep_alive` parameter specifies how long the async search should be
available in the cluster. When not specified, the `keep_alive` set with the
corresponding submit async request will be used. Otherwise, it is possible to
override such value and extend the validity of the request. When this period
expires, the search, if still running, is cancelled. If the search is completed,
its saved results are deleted.

#### Get async search status

The get async search status API, without retrieving search results, shows only
the status of a previously submitted async search request given its `id`.

If the Elasticsearch security features are enabled, the access to the status of a
specific async search is restricted to:

* The user or API key that submitted the original async search request.
* Users that have the `monitor` cluster privilege or higher.

You can also specify how long the async search needs to be available through the
`keep_alive` parameter, which defaults to `5d` (five days). Ongoing async
searches and any saved search results are deleted after this period.

```console
GET /_async_search/status/FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=
```

```console-result
{
  "id" : "FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=",
  "is_running" : true,
  "is_partial" : true,
  "start_time_in_millis" : 1583945890986,
  "expiration_time_in_millis" : 1584377890986,
  "_shards" : {
      "total" : 562,
      "successful" : 188, <1>
      "skipped" : 0,
      "failed" : 0
  }
}
```

<1> Indicates how many shards have executed the query so far.

For an async search that has been completed, the status response has an
additional `completion_status` field that shows the status code of the completed
async search.

```console-result
{
  "id" : "FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=",
  "is_running" : false,
  "is_partial" : false,
  "start_time_in_millis" : 1583945890986,
  "expiration_time_in_millis" : 1584377890986,
  "_shards" : {
      "total" : 562,
      "successful" : 562,
      "skipped" : 0,
      "failed" : 0
  },
 "completion_status" : 200 <1>
}
```

<1> Indicates that the async search was successfully completed.

```console-result
{
  "id" : "FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=",
  "is_running" : false,
  "is_partial" : true,
  "start_time_in_millis" : 1583945890986,
  "expiration_time_in_millis" : 1584377890986,
  "_shards" : {
      "total" : 562,
      "successful" : 450,
      "skipped" : 0,
      "failed" : 112
  },
 "completion_status" : 503 <1>
}
```

<1> Indicates that the async search was completed with an error.

#### Delete async search

You can use the delete async search API to manually delete an async search by
ID. If the search is still running, the search request will be cancelled.
Otherwise, the saved search results are deleted.

```console
DELETE /_async_search/FmRldE8zREVEUzA2ZVpUeGs2ejJFUFEaMkZ5QTVrSTZSaVN3WlNFVmtlWHJsdzoxMDc=
```

If the Elasticsearch security features are enabled, the deletion of a specific async
search is restricted to:

  * The user or API key that submitted the original async search request.
  * Users that have the `cancel_task` cluster privilege or higher.
