<!-- Converted from indices/get-mapping.asciidoc (AsciiDoc). Includes are inlined. -->

### Get mapping API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Retrieves mapping definitions for one or more indices. For data
streams, the API retrieves mappings for the stream's backing indices.

```console
GET /my-index-000001/_mapping
```

#### Request

`GET /_mapping`

`GET /<target>/_mapping`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the target data stream, index, or alias.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

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

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

##### Multiple data streams and indices

The get mapping API can be used to get more than one data stream or index with a
single call. General usage of the API follows the following syntax:
`host:port/<target>/_mapping` where `<target>` can accept a comma-separated
list of names. To get mappings for all data streams and indices in a cluster, use `_all` or `*` for `<target>`
or omit the `<target>` parameter.
The following are some examples:

```console
GET /my-index-000001,my-index-000002/_mapping
```

If you want to get mappings of all indices in a cluster, the following
examples are equivalent:

```console
GET /*/_mapping

GET /_all/_mapping

GET /_mapping
```
