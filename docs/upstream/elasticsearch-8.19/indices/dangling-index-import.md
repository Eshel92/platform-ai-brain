<!-- Converted from indices/dangling-index-import.asciidoc (AsciiDoc). Includes are inlined. -->

### Import dangling index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Imports a dangling index.

#### Request

```console
POST /_dangling/<index-uuid>?accept_data_loss=true
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

If Elasticsearch encounters index data that is absent from the current cluster
state, those indices are considered to be dangling. For example,
this can happen if you delete more than
`cluster.indices.tombstones.size` indices while an Elasticsearch node is offline.
Import a single index into the cluster by referencing its UUID. Use the
List dangling indices API to locate the UUID of an index.

#### Path parameters

`<index-uuid>`::
(Required, string)
UUID of the index to import, which you can find using the
List dangling indices API.

#### Query parameters

`accept_data_loss`::
(Required, Boolean)
This field must be set to `true` to import a dangling index. Because Elasticsearch
cannot know where the dangling index data came from or determine which shard
copies are fresh and which are stale, it cannot guarantee that the imported data
represents the latest state of the index when it was last in the cluster.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

The following example shows how to import a dangling index:

```console
POST /_dangling/zmM4e0JtBkeUjiHD-MihPQ?accept_data_loss=true
```

The API returns following response:

```console-result
{
  "acknowledged" : true
}
```
