<!-- Converted from indices/delete-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete data stream API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Deletes one or more data streams and their backing
indices. See delete-data-stream.

```console
DELETE /_data_stream/my-data-stream
```

#### Request

`DELETE /_data_stream/<data-stream>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `delete_index`
or `manage` index privilege for the data stream.

#### Path parameters

`<data-stream>`::
(Required, string)
Comma-separated list of data streams to delete.
Wildcard (`*`) expressions are supported.

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
