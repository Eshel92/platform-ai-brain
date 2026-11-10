<!-- Converted from searchable-snapshots/apis/node-cache-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Cache stats API

**New API reference**
For the most up-to-date API details, refer to [Searchable snapshots APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-searchable_snapshots).

Retrieves statistics about the shared cache for <<partially-mounted,partially
mounted indices>>.

#### Request

`GET /_searchable_snapshots/cache/stats` +

`GET /_searchable_snapshots/<node_id>/cache/stats`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the
`manage` cluster privilege to use this API.
For more information, see security-privileges.

#### Path parameters

`<node_id>`::
    (Optional, string) The names of particular nodes in the cluster to target.
    For example, `nodeId1,nodeId2`. For node selection options, see
    cluster-nodes.

#### Response body

`nodes`::
(object)
Contains statistics for the nodes selected by the request.
**Properties of `nodes`**
`<node_id>`::
(object)
Contains statistics for the node with the given identifier.
**Properties of `<node_id>`**
=====
`shared_cache`::
(object)
Contains statistics about the shared cache file.
**Properties of `shared_cache`**
======
`reads`::
(long) Number of times the shared cache is used to read data from.

`bytes_read_in_bytes`::
(long) The total of bytes read from the shared cache.

`writes`::
(long) Number of times data from the blob store repository is written in the shared cache.

`bytes_written_in_bytes`::
(long) The total of bytes written in the shared cache.

`evictions`::
(long) Number of regions evicted from the shared cache file.

`num_regions`::
(integer) Number of regions in the shared cache file.

`size_in_bytes`::
(long) The total size in bytes of the shared cache file.

`region_size_in_bytes`::
(long) The size in bytes of a region in the shared cache file.
======
=====

#### Examples

Gets the statistics about the shared cache for partially mounted indices from
all data nodes:

```console
GET /_searchable_snapshots/cache/stats
```

The API returns the following response:

```console-result
{
  "nodes" : {
    "eerrtBMtQEisohZzxBLUSw" : {
      "shared_cache" : {
        "reads" : 6051,
        "bytes_read_in_bytes" : 5448829,
        "writes" : 37,
        "bytes_written_in_bytes" : 1208320,
        "evictions" : 5,
        "num_regions" : 65536,
        "size_in_bytes" : 1099511627776,
        "region_size_in_bytes" : 16777216
      }
    }
  }
}
```
