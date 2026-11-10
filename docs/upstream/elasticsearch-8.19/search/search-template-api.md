<!-- Converted from search/search-template-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Search template API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Runs a search with a search template.

```console
GET my-index/_search/template
{
  "id": "my-search-template",
  "params": {
    "query_string": "hello world",
    "from": 0,
    "size": 10
  }
}
```

#### Request

`GET <target>/_search/template`

`GET _search/template`

`POST <target>/_search/template`

`POST _search/template`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias. For cross-cluster search, see remote-clusters.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases to
search. Supports wildcards (`*`). To search all data streams and indices, omit
this parameter or use `*`.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

`ccs_minimize_roundtrips`::
(Optional, Boolean) If `true`, network round-trips are minimized for
cross-cluster search requests. Defaults to `true`.

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
`explain`::
(Optional, Boolean) If `true`, the response includes additional details about
score computation as part of a hit. Defaults to `false`.

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `true`.
deprecated:[7.16.0]
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`rest_total_hits_as_int`::
(Optional, Boolean) If `true`, the response returns `hits.total` as an integer.
If false, it returns `hits.total` as an object. Defaults to `false`.

`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`scroll`::
(Optional, time units) Specifies how long a consistent view of
the index should be maintained for scrolled search.
`search_type`::
(Optional, string) The type of the search operation. Available options:
* `query_then_fetch`
* `dfs_query_then_fetch`
`typed_keys`::
(Optional, Boolean) If `true`, the response prefixes aggregation and suggester
names with their respective types. Defaults to `false`.

#### Request body

`explain`::
(Optional, Boolean) If `true`, returns detailed information about score
calculation as part of each hit. Defaults to `false`.
If you specify both this and the `explain` query parameter, the API uses only
the query parameter.

`id`::
(Required*, string) ID of the search template to use. If no `source` is
specified, this parameter is required.

`params`::
(Optional, object) Key-value pairs used to replace Mustache variables in the
template. The key is the variable name. The value is the variable value.

`profile`::
(Optional, Boolean) If `true`, the query execution is profiled. Defaults to
`false`.

`source`::
(Required*, object) An inline search template. Supports the same parameters as
the search API's request body. Also supports
[Mustache](https://mustache.github.io/) variables.
If no `id` is specified, this parameter is required.
