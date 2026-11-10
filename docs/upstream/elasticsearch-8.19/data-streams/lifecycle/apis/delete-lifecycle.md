<!-- Converted from data-streams/lifecycle/apis/delete-lifecycle.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete the lifecycle of a data stream

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Deletes the lifecycle from a set of data streams.

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_data_stream_lifecycle` index privilege or higher to
use this API. For more information, see security-privileges.

#### Request

`DELETE _data_stream/<data-stream>/_lifecycle`

#### Description

Deletes the lifecycle from the specified data streams. If multiple data streams are provided but at least one of them
does not exist, then the deletion of the lifecycle will fail for all of them and the API will respond with `404`.

#### Path parameters

`<data-stream>`::
(Required, string) Comma-separated list of data streams used to limit the request. Supports wildcards (`*`).
To target all data streams use `*` or `_all`.

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

#### Examples

The following example deletes the lifecycle of `my-data-stream`:

```console
DELETE _data_stream/my-data-stream/_lifecycle
```

When the policy is successfully deleted from all selected data streams, you receive the following result:

```console-result
{
  "acknowledged": true
}
```
