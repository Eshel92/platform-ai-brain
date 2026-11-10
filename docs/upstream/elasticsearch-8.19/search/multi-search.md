<!-- Converted from search/multi-search.asciidoc (AsciiDoc). Includes are inlined. -->

### Multi search API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Executes several searches with a single API request.

```console
GET my-index-000001/_msearch
{ }
{"query" : {"match" : { "message": "this is a test"}}}
{"index": "my-index-000002"}
{"query" : {"match_all" : {}}}
```

#### Request

`GET /<target>/_msearch`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias. For cross-cluster search, see remote-clusters.

#### Description

The multi search API executes several searches from a single API request.
The format of the request is similar to the bulk API format and makes use
of the newline delimited JSON (NDJSON) format.

The structure is as follows:

```js
header\n
body\n
header\n
body\n
```

This structure is specifically optimized to reduce parsing if a specific search
ends up redirected to another node.

**Important:**
The final line of data must end with a newline character `\n`. Each newline
character may be preceded by a carriage return `\r`. When sending requests to
this endpoint the `Content-Type` header should be set to `application/x-ndjson`.

#### Path parameters

`<target>`::
(Optional, string)
Comma-separated list of data streams, indices, and aliases to search.
This list acts as a fallback if a search in the request body does not specify an
`index` target.
Wildcard (`*`) expressions are supported. To search all data streams and indices
in a cluster, omit this parameter or use `_all` or `*`.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
`ccs_minimize_roundtrips`::
(Optional, Boolean)
If `true`, network roundtrips between the coordinating node and remote clusters
are minimized for cross-cluster search requests. Defaults to `true`. See
ccs-network-delays.

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

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `true`.
deprecated:[7.16.0]
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`max_concurrent_searches`::
(Optional, integer)
Maximum number of concurrent searches the multi search API can execute. Defaults
to max(1, (# of data nodes * min(search thread pool size, 10))).

`max_concurrent_shard_requests`::
(Optional, integer)
Maximum number of concurrent shard requests that each sub-search request
executes per node. Defaults to `5`.

You can use this parameter to prevent a request from overloading a cluster. For
example, a default request hits all data streams and indices in a cluster. This
could cause shard request rejections if the number of shards per node is high.

In certain scenarios, parallelism isn't achieved through concurrent requests. In
those cases, a low value in this parameter could result in poor performance.
For example, in an environment where a very low number of concurrent search
requests are expected, a higher value in this parameter may improve performance.

`pre_filter_shard_size`::
(Optional, integer)
Defines a threshold that enforces a pre-filter roundtrip to prefilter search
shards based on query rewriting if the number of shards the search request
expands to exceeds the threshold. This filter roundtrip can limit the number of
shards significantly if for instance a shard can not match any documents based
on its rewrite method i.e., if date filters are mandatory to match but the
shard bounds and the query are disjoint.
When unspecified, the pre-filter phase is executed if any of these
conditions is met:
  - The request targets more than `128` shards.
  - The request targets one or more read-only index.
  - The primary sort of the query targets an indexed field.

`rest_total_hits_as_int`::
(Optional, Boolean)
If `true`, `hits.total` are returned as an integer in the
response. Defaults to `false`, which returns an object.

`routing`::
(Optional, string)
Custom routing value used to route search operations
to a specific shard.

`search_type`::
(Optional, string)
Indicates whether global term and document frequencies should be used when
scoring returned documents.

Options are:

`query_then_fetch`::
(default)
Documents are scored using local term and document frequencies for the shard.
This is usually faster but less accurate.

`dfs_query_then_fetch`::
Documents are scored using global term and document frequencies across all
shards. This is usually slower but more accurate.

`typed_keys`::
(Optional, Boolean)
Specifies whether aggregation and suggester names should be prefixed by their
respective types in the response.

#### Request body

The request body contains a newline-delimited list of search `<header>` and
search `<body>` objects.

`<header>`::
(Required, object)
Parameters used to limit or change the search.
This object is required for each search body but can be empty (`{}`) or a blank
line.
**Properties of `<header>` objects**
`allow_no_indices`::
(Optional, Boolean)
If `true`, the request does *not* return an error if a wildcard expression or
`_all` value retrieves only missing or closed indices.
This parameter also applies to aliases that point to a missing
or index.

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
(Optional, Boolean) If `true`, documents from missing or closed indices are not
included in the response. Defaults to `false`.

`index`::
(Optional, string or array of strings)
Data streams, indices, and aliases to search. Supports wildcards (`*`). Specify
multiple targets as an array.
If this parameter is not specified, the `<target>` request path parameter
is used as a fallback.

`preference`::
(Optional, string)
Node or shard used to perform the search. Random by default.

`request_cache`::
(Optional, Boolean)
If `true`, the request cache can be used for this search. Defaults to
index-level settings. See shard-request-cache.

`routing`::
(Optional, string)
Custom routing value used to route search operations
to a specific shard.

`search_type`::
(Optional, string)
Indicates whether global term and document frequencies should be used when
scoring returned documents.

Options are:

`query_then_fetch`:::
(default)
Documents are scored using local term and document frequencies for the shard.
This is usually faster but less accurate.

`dfs_query_then_fetch`:::
Documents are scored using global term and document frequencies across all
shards. This is usually slower but more accurate.

`<body>`::
(Optional, object)
Contains parameters for a search request:
**Properties of `<body>` objects**
`aggregations`::
(Optional, aggregation object)
Aggregations you wish to run during the search. See search-aggregations.

`query`::
(Optional, Query DSL object) Query you wish to run during the
search. Hits matching this query are returned in the response.

`from`::
(Optional, integer)
Starting offset for returned hits. Defaults to `0`.

`size`::
(Optional, integer)
Number of hits to return. Defaults to `10`.

#### Response body

`responses`::
  (array) Includes the search response and status code for each search request
  matching its order in the original multi search request. If there was a
  complete failure for a specific search request, an object with `error` message
  and corresponding status code will be returned in place of the actual search
  response.

#### Examples

The header includes the data streams, indices, and aliases to search. The header
also indicates the `search_type`, `preference`, and `routing`. The body includes
the typical search body request (including the `query`, `aggregations`, `from`,
`size`, and so on).

```js
$ cat requests
{"index" : "test"}
{"query" : {"match_all" : {}}, "from" : 0, "size" : 10}
{"index" : "test", "search_type" : "dfs_query_then_fetch"}
{"query" : {"match_all" : {}}}
{}
{"query" : {"match_all" : {}}}

{"query" : {"match_all" : {}}}
{"search_type" : "dfs_query_then_fetch"}
{"query" : {"match_all" : {}}}
```

```js
$ curl -H "Content-Type: application/x-ndjson" -XGET localhost:9200/_msearch --data-binary "@requests"; echo
```

Note, the above includes an example of an empty header (can also be just
without any content) which is supported as well.

The endpoint also allows you to search against data streams, indices, and
aliases in the request path. In this case, it will be used as the default target
unless explicitly specified in the header's `index` parameter. For example:

```console
GET my-index-000001/_msearch
{}
{"query" : {"match_all" : {}}, "from" : 0, "size" : 10}
{}
{"query" : {"match_all" : {}}}
{"index" : "my-index-000002"}
{"query" : {"match_all" : {}}}
```

The above will execute the search against the `my-index-000001` index for all the
requests that don't define an `index` target in the request body. The last
search will be executed against the `my-index-000002` index.

The `search_type` can be set in a similar manner to globally apply to
all search requests.

#### Security

See api-url-access-control

#### Partial responses

To ensure fast responses, the multi search API will respond with partial results
if one or more shards fail. See Shard failures for more
information.

#### Search Cancellation

Multi searches can be cancelled using standard task cancellation
mechanism and are also automatically cancelled when the http connection used to
perform the request is closed by the client. It is fundamental that the http
client sending requests closes connections whenever requests time out or are
aborted. Cancelling an msearch request will also cancel all of the corresponding
sub search requests.
