<!-- Converted from cat/indices.asciidoc (AsciiDoc). Includes are inlined. -->

### cat indices API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana
console. They are _not_ intended for use by applications. For application
consumption, use the get index API.

Returns high-level information about indices in a cluster, including backing
indices for data streams.

#### Request

`GET /_cat/indices/<target>`

`GET /_cat/indices`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API. You must
also have the `monitor` or `manage` index privilege
for any data stream, index, or alias you retrieve.

#### Description

Use the cat indices API to get the following information for each index in a
cluster:

* Shard count
* Document count
* Deleted document count
* Primary store size
* Total store size of all shards, including shard replicas

These metrics are retrieved directly from
[Lucene](https://lucene.apache.org/core/), which Elasticsearch uses internally to power
indexing and search. As a result, all document counts include hidden
nested documents.

To get an accurate count of Elasticsearch documents, use the cat count or
count APIs.

Note that information such as document count, deleted document count and store size are not shown for
indices restored from source-only snapshots since these indices
do not contain the relevant data structures to retrieve this information from.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`bytes`::
(Optional, byte size units) Unit used to display byte values.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
`health`::
(Optional, string) Health status used to limit returned indices. Valid values
are:

* `green`
* `yellow`
* `red`

By default, the response includes indices of any health status.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`include_unloaded_segments`::
(Optional, Boolean) If `true`, the response includes information from segments
that are **not** loaded into memory. Defaults to `false`.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`pri` (primary shards)::
(Optional, Boolean) If `true`, the response only includes information from
primary shards. Defaults to `false`.

`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.
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

#### Examples

```console
GET /_cat/indices/my-index-*?v=true&s=index
```

The API returns the following response:

```txt
health status index            uuid                   pri rep docs.count docs.deleted store.size pri.store.size dataset.size
yellow open   my-index-000001  u8FNjxh8Rfy_awN11oDKYQ   1   1       1200            0     88.1kb         88.1kb       88.1kb
green  open   my-index-000002  nYFWZEO7TUiOjLQXBaYJpA   1   0          0            0       260b           260b         260b
```
