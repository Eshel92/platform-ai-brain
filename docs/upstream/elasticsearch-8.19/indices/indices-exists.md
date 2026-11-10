<!-- Converted from indices/indices-exists.asciidoc (AsciiDoc). Includes are inlined. -->

### Exists API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Checks if a data stream, index, or alias exists.

```console
HEAD my-data-stream
```

#### Request

`HEAD <target>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the target.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases.
Supports wildcards (`*`).

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

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

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`include_defaults`::
(Optional, Boolean) If `true`, return all default settings in the response.
Defaults to `false`.
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.

#### Response codes

`200`::
All targets exist.

`404`::
One or more specified targets do not exist.
