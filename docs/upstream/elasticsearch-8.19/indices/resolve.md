<!-- Converted from indices/resolve.asciidoc (AsciiDoc). Includes are inlined. -->

### Resolve index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Resolves the specified name(s) and/or index patterns for indices, aliases, and
data streams. Multiple patterns and remote clusters are supported.

```console
GET /_resolve/index/my-index-*
```

#### Request

`GET /_resolve/index/<name>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the target data stream, index, or index alias.

#### Path parameters

`<name>`::
(Required, string) Comma-separated name(s) or index pattern(s) of the
indices, aliases, and data streams to resolve, using api-multi-index.
Resources on remote clusters can be specified using the
`<cluster>:<name>` syntax.

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
Defaults to `open`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
Defaults to `false`.

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `false`.
deprecated:[7.16.0]

#### Examples

```console
GET /_resolve/index/f*,remoteCluster1:bar*?expand_wildcards=all
```

The API returns the following response:

```console-result
{
  "indices": [                                 <1>
    {
      "name": "foo_closed",
      "attributes": [
        "closed"                               <2>
      ]
    },
    {
      "name": "freeze-index",
      "aliases": [
        "f-alias"
      ],
      "attributes": [
        "open"
      ]
    },
    {
      "name": "remoteCluster1:bar-01",
      "attributes": [
        "open"
      ]
    }
  ],
  "aliases": [                                 <3>
    {
      "name": "f-alias",
      "indices": [
        "freeze-index",
        "my-index-000001"
      ]
    }
  ],
  "data_streams": [                            <4>
    {
      "name": "foo",
      "backing_indices": [
        ".ds-foo-2099.03.07-000001"
      ],
      "timestamp_field": "@timestamp"
    }
  ]
}
```

<1> All indices matching the supplied names or expressions
<2> Possible index attributes are `open`, `closed`, `hidden`, `system`, and `frozen`
<3> All aliases matching the supplied names or expressions
<4> All data streams matching the supplied names or expressions
