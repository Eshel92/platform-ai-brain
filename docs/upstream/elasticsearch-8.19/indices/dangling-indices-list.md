<!-- Converted from indices/dangling-indices-list.asciidoc (AsciiDoc). Includes are inlined. -->

### List dangling indices API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Lists dangling indices.

#### Request

```console
GET /_dangling
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

If Elasticsearch encounters index data that is absent from the current cluster
state, those indices are considered to be dangling. For example,
this can happen if you delete more than
`cluster.indices.tombstones.size` indices while an Elasticsearch node is offline.

Use this API to list dangling indices, which you can then
import or delete.

#### Examples

The API returns the following response:

```console-result
{
  "dangling_indices": [
   {
    "index_name": "my-index-000001",
    "index_uuid": "zmM4e0JtBkeUjiHD-MihPQ",
    "creation_date_millis": 1589414451372,
    "node_ids": [
      "pL47UN3dAb2d5RCWP6lQ3e"
    ]
   }
  ]
}
```
