<!-- Converted from indices/alias-exists.asciidoc (AsciiDoc). Includes are inlined. -->

### Alias exists API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Checks if an alias exists.

```console
HEAD _alias/my-alias
```

#### Request

`HEAD _alias/<alias>`

`HEAD <target>/_alias/<alias>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the alias. If you specify a target, you must also have the
`view_index_metadata` or `manage` index privilege for the target.

#### Path parameters

`<alias>`::
(Optional, string) Comma-separated list of aliases to check. Supports wildcards
(`*`).

`<target>`::
(Optional, string) Comma-separated list of data streams or indices used to limit
the request. Supports wildcards (`*`). To target all data streams and indices,
omit this parameter or use `*` or `_all`.

#### Query parameters

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
Defaults to `all`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, requests that include a missing data stream or
index in the `<target>` return an error. Defaults to `false`.

`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.

#### Response codes

`200`::
All specified aliases exist.

`404`::
One or more of the specified aliases don't exist.
