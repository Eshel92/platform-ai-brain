<!-- Converted from search/count.asciidoc (AsciiDoc). Includes are inlined. -->

### Count API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Gets the number of matches for a search query.

```console
GET /my-index-000001/_count?q=user:kimchy
```

#### Request

`GET /<target>/_count`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias.

#### Description

The count API allows you to execute a query and get the number of matches for
that query. You can provide the query by either:

* Including the `q` query string parameter 
* Defining Query DSL within the request body 

Using both returns an error.

The count API supports multi-target syntax. You can run a single
count API search across multiple data streams and indices.

The operation is broadcast across all shards. For each shard id group, a replica
is chosen and executed against it. This means that replicas increase the
scalability of count.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases to
search. Supports wildcards (`*`). To search all data streams and indices, omit
this parameter or use `*` or `_all`.

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

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `true`.
deprecated:[7.16.0]
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`lenient`::
(Optional, Boolean) If `true`, format-based query failures (such as providing
text to a numeric field) in the query string will be ignored. Defaults to
`false`.
This parameter can only be used when the `q` query string parameter is
specified.
`min_score`::
(Optional, float)
  Sets the minimum `_score` value that documents must have to be included in the
  result.

`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`q`::
(Optional, string) Query in the Lucene query string syntax.
**Note:** If the `q` parameter is specified, the count API does not accept a request body.

`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`terminate_after`::
(Optional, integer) Maximum number of documents to collect for each shard. If a
query reaches this limit, Elasticsearch terminates the query early. Elasticsearch collects
documents before sorting.
**Important:** Use with caution. Elasticsearch applies this parameter to each shard handling
the request. When possible, let Elasticsearch perform early termination automatically.
Avoid specifying this parameter for requests that target data streams with
backing indices across multiple data tiers.

#### Request body

`query`::
(Optional, query object) Defines the search query using
Query DSL.

#### Examples

```console
PUT /my-index-000001/_doc/1?refresh
{
  "user.id": "kimchy"
}

GET /my-index-000001/_count?q=user:kimchy

GET /my-index-000001/_count
{
  "query" : {
    "term" : { "user.id" : "kimchy" }
  }
}
```

Both examples above do the same: count the number of documents in
`my-index-000001` with a `user.id` of `kimchy`. The API returns the following response:

```console-result
{
  "count": 1,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  }
}
```

The query is optional. When no query is provided, the API uses `match_all` to
count all the documents.
