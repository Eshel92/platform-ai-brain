<!-- Converted from snapshot-restore/apis/clean-up-repo-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Clean up snapshot repository API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Triggers the review of a snapshot repository's contents and deletes any stale
data that is not referenced by existing snapshots. See
snapshots-repository-cleanup.

```console
POST /_snapshot/my_repository/_cleanup
```

#### Request

`POST /_snapshot/<repository>/_cleanup`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<repository>`::
(Required, string)
Name of the snapshot repository to review and clean up.

#### Query parameters

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

#### Response body

`results`::
(object)
Contains statistics for cleanup operations.
**Properties of `results`**
`deleted_bytes`::
(integer)
Number of bytes freed by cleanup operations.

`deleted_blobs`::
(integer)
Number of binary large objects (blobs) removed from the snapshot repository
during cleanup operations. Any non-zero value implies that unreferenced blobs
were found and subsequently cleaned up.

#### Examples

```console
POST /_snapshot/my_repository/_cleanup
```

The API returns the following response:

```console-result
{
  "results": {
    "deleted_bytes": 20,
    "deleted_blobs": 5
  }
}
```
