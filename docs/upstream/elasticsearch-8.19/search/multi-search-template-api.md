<!-- Converted from search/multi-search-template-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Multi search template API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Runs multiple templated searches with a single
request.

```console
GET my-index/_msearch/template
{ }
{ "id": "my-search-template", "params": { "query_string": "hello world", "from": 0, "size": 10 }}
{ }
{ "id": "my-other-search-template", "params": { "query_type": "match_all" }}
```

#### Request

`GET <target>/_msearch/template`

`GET _msearch/template`

`POST <target>/_msearch/template`

`POST _msearch/template`

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

`ccs_minimize_roundtrips`::
(Optional, Boolean) If `true`, network round-trips are minimized for
cross-cluster search requests. Defaults to `true`.

`max_concurrent_searches`::
(Optional, integer) Maximum number of concurrent searches the API can run.
Defaults to +max(1, (# of data nodes *
min(search thread pool size, 10)))+.

`rest_total_hits_as_int`::
(Optional, Boolean) If `true`, the response returns `hits.total` as an integer.
If false, it returns `hits.total` as an object. Defaults to `false`.

`search_type`::
(Optional, string) The type of the search operation. Available options:
* `query_then_fetch`
* `dfs_query_then_fetch`
`typed_keys`::
(Optional, Boolean) If `true`, the response prefixes aggregation and suggester
names with their respective types. Defaults to `false`.

#### Request body

The request body must be newline-delimited JSON (NDJSON) in the following
format:

```js
<header>\n
<body>\n
<header>\n
<body>\n
```

Each `<header>` and `<body>` pair represents a search request.

The `<header>` supports the same parameters as the <<search-multi-search,multi
search API>>'s `<header>`. The `<body>` supports the same parameters as the
search template API's request body.

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
(Request, object) Parameters for the search.
=====
`explain`::
(Optional, Boolean) If `true`, returns detailed information about score
calculation as part of each hit. Defaults to `false`.
=====

#### Response codes

The API returns a `400` status code only if the request itself fails. If one or
more searches in the request fail, the API returns a `200` status code with an
`error` object for each failed search in the response.

#### Response body

`responses`::
(array of objects) Results for each search, returned in the order submitted.
Each object uses the same properties as the search API's
response.
If a search fails, the response includes an `error` object containing an error
message.

#### curl requests

If a providing text file or text input to `curl`, use the `--data-binary` flag
instead of `-d` to preserve newlines.

```sh
$ cat requests
{ "index": "my-index" }
{ "id": "my-search-template", "params": { "query_string": "hello world", "from": 0, "size": 10 }}
{ "index": "my-other-index" }
{ "id": "my-other-search-template", "params": { "query_type": "match_all" }}

$ curl -H "Content-Type: application/x-ndjson" -XGET localhost:9200/_msearch/template --data-binary "@requests"; echo
```
