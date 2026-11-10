<!-- Converted from search/search-your-data/search-shard-routing.asciidoc (AsciiDoc). Includes are inlined. -->

### Search shard routing

To protect against hardware failure and increase search capacity, Elasticsearch can store
copies of an index's data across multiple shards on multiple nodes. When running
a search request, Elasticsearch selects a node containing a copy of the index's data and
forwards the search request to that node's shards. This process is known as
_search shard routing_ or _routing_.

#### Adaptive replica selection

By default, Elasticsearch uses _adaptive replica selection_ to route search requests.
This method selects an eligible node using <<shard-allocation-awareness,shard
allocation awareness>> and the following criteria:

* Response time of prior requests between the coordinating node
and the eligible node
* How long the eligible node took to run previous searches
* Queue size of the eligible node's `search` threadpool

Adaptive replica selection is designed to decrease search latency. However, you
can disable adaptive replica selection by setting
`cluster.routing.use_adaptive_replica_selection` to `false` using the
cluster settings API. If disabled, Elasticsearch routes
search requests using a round-robin method, which may result in slower searches.

#### Set a preference

By default, adaptive replica selection chooses from all eligible nodes and
shards. However, you may only want data from a local node or want to route
searches to a specific node based on its hardware. Or you may want to send
repeated searches to the same shard to take advantage of caching.

To limit the set of nodes and shards eligible for a search request, use
the search API's `preference` query parameter.

For example, the following request searches `my-index-000001` with a
`preference` of `_local`. This restricts the search to shards on the
local node. If the local node contains no shard copies of the index's data, the
request uses adaptive replica selection to another eligible node
as a fallback.

```console
GET /my-index-000001/_search?preference=_local
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
```

You can also use the `preference` parameter to route searches to specific shards
based on a provided string. If the cluster state and selected shards
do not change, searches using the same `preference` string are routed to the
same shards in the same order.

We recommend using a unique `preference` string, such as a user name or web
session ID. This string cannot start with a `_`.

**Tip:** You can use this option to serve cached results for frequently used and
resource-intensive searches. If the shard's data doesn't change, repeated
searches with the same `preference` string retrieve results from the same
shard request cache. For time series use cases, such as
logging, data in older indices is rarely updated and can be served directly from
this cache.

The following request searches `my-index-000001` with a `preference` string of
`my-custom-shard-string`.

```console
GET /my-index-000001/_search?preference=my-custom-shard-string
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
```

**Note:** If the cluster state or selected shards change, the same `preference`
string may not route searches to the same shards in the same order. This can
occur for a number of reasons, including shard relocations and shard failures. A
node can also reject a search request, which Elasticsearch would re-route to another
node.

#### Use a routing value

When you index a document, you can specify an optional
routing value, which routes the document to a
specific shard.

For example, the following indexing request routes a document using
`my-routing-value`.

```console
POST /my-index-000001/_doc?routing=my-routing-value
{
  "@timestamp": "2099-11-15T13:12:00",
  "message": "GET /search HTTP/1.1 200 1070000",
  "user": {
    "id": "kimchy"
  }
}
```

You can use the same routing value in the search API's `routing` query
parameter. This ensures the search runs on the same shard used to index the
document.

```console
GET /my-index-000001/_search?routing=my-routing-value
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
```

You can also provide multiple comma-separated routing values:

```console
GET /my-index-000001/_search?routing=my-routing-value,my-routing-value-2
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
```

#### Search concurrency and parallelism

By default, Elasticsearch doesn't reject search requests based on the number of shards
the request hits. However, hitting a large number of shards can significantly
increase CPU and memory usage.

**Tip:** For tips on preventing indices with large numbers of shards, see
size-your-shards.

You can use the `max_concurrent_shard_requests` query parameter to control
maximum number of concurrent shards a search request can hit per node. This
prevents a single request from overloading a cluster. The parameter defaults to
a maximum of `5`.

```console
GET /my-index-000001/_search?max_concurrent_shard_requests=3
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
```

You can also use the `action.search.shard_count.limit` cluster setting to set a
search shard limit and reject requests that hit too many shards. You can
configure `action.search.shard_count.limit` using the
cluster settings API.
