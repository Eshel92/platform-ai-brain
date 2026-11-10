<!-- Converted from indices/data-stream-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Data stream stats API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Retrieves statistics for one or more data streams.

```console
GET /_data_stream/my-data-stream/_stats
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`monitor` or `manage` index privilege
for the data stream.

#### Request

`GET /_data_stream/<data-stream>/_stats`

#### Path parameters

`<data-stream>`::
(Optional, string)
Comma-separated list of data streams used to limit the request. Wildcard
expressions (`*`) are supported.
To target all data streams in a cluster, omit this parameter or use `*`.

#### Query parameters

`expand_wildcards`::
(Optional, string)
Type of data stream that wildcard patterns can match. Supports
comma-separated values, such as `open,hidden`. Valid values are:

`all`, `hidden`::
Match any data stream, including hidden ones.

`open`, `closed`::
Matches any non-hidden data stream. Data streams cannot be closed.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

`human`::
(Optional, Boolean)
If `true`, the response includes statistics in human-readable <<byte-units,byte
values>>. Defaults to `false`.

#### Response body

`_shards`::
(object)
Contains information about shards that attempted to execute the request.
**Properties of `_shards`**
`total`::
(integer)
Total number of shards that attempted to execute the request.

`successful`::
(integer)
Number of shards that successfully executed the request.

`failed`::
(integer)
Number of shards that failed to execute the request.

`data_stream_count`::
(integer)
Total number of selected data streams.

`backing_indices`::
(integer)
Total number of backing indices for the selected data streams.

`total_store_size`::
(byte value)
Total size of all shards for the selected data streams.
This property is included only if the `human` query parameter is `true`.

`total_store_size_bytes`::
(integer)
Total size, in bytes, of all shards for the selected data streams.

`data_streams`::
(array of objects)
Contains statistics for the selected data streams.
**Properties of objects in `data_streams`**
`data_stream`::
(string)
Name of the data stream.

`backing_indices`::
(integer)
Current number of backing indices for the data stream.

`store_size`::
(byte value)
Total size of all shards for the data stream's backing indices.
This parameter is only returned if the `human` query parameter is `true`.

`store_size_bytes`::
(integer)
Total size, in bytes, of all shards for the data stream's backing indices.

`maximum_timestamp`::
(integer)
The data stream's highest `@timestamp` value, converted to milliseconds since
the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time).
=====
The data stream may contain `@timestamp` values higher than this if one or more
of the following conditions are met:

* The stream contains closed backing indices.
* Backing indices with a lower generation contain
higher `@timestamp` values.
=====

**Note:**

#### Examples

```console
GET /_data_stream/my-data-stream*/_stats?human=true
```

The API returns the following response.

```console-result
{
  "_shards": {
    "total": 10,
    "successful": 5,
    "failed": 0
  },
  "data_stream_count": 2,
  "backing_indices": 5,
  "total_store_size": "7kb",
  "total_store_size_bytes": 7268,
  "data_streams": [
    {
      "data_stream": "my-data-stream",
      "backing_indices": 3,
      "store_size": "3.7kb",
      "store_size_bytes": 3772,
      "maximum_timestamp": 1607512028000
    },
    {
      "data_stream": "my-data-stream-two",
      "backing_indices": 2,
      "store_size": "3.4kb",
      "store_size_bytes": 3496,
      "maximum_timestamp": 1607425567000
    }
  ]
}
```
