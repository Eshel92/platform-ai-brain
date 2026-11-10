<!-- Converted from indices/dangling-index-delete.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete dangling index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Deletes a dangling index.

#### Request

```console
DELETE /_dangling/<index-uuid>?accept_data_loss=true
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

If Elasticsearch encounters index data that is absent from the current cluster
state, those indices are considered to be dangling. For example,
this can happen if you delete more than
`cluster.indices.tombstones.size` indices while an Elasticsearch node is offline.
Deletes a dangling index by referencing its UUID. Use the
List dangling indices API to locate the UUID of an index.

#### Path parameters

`<index-uuid>`::
(Required, string)
UUID of the index to delete. You can find this using the
List dangling indices API.

#### Query parameters

`accept_data_loss`::
(Optional, Boolean)
This field must be set to `true` in order to carry out the import, since it will
no longer be possible to recover the data from the dangling index.

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
