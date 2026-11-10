<!-- Converted from searchable-snapshots/apis/shard-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Searchable snapshot statistics API

**New API reference**
For the most up-to-date API details, refer to [Searchable snapshots APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-searchable_snapshots).

experimental::[]

Retrieves statistics about searchable snapshots.

#### Request

`GET /_searchable_snapshots/stats`

`GET /<target>/_searchable_snapshots/stats`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API. You must also
have the `manage` index privileges for the target
data stream or index.

#### Description

#### Path parameters

`<target>`::
(Optional, string)
Comma-separated list of data streams and indices to retrieve statistics for. To
retrieve statistics for all data streams and indices, omit this parameter.

#### Examples

Retrieves the statistics of the index `my-index`:

```console
GET /my-index/_searchable_snapshots/stats
```
