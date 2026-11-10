<!-- Converted from snapshot-restore/apis/delete-repo-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete snapshot repository API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Unregisters one or more snapshot repositories.

When a repository is unregistered, Elasticsearch only removes the reference to the
location where the repository is storing the snapshots. The snapshots themselves
are left untouched and in place.

```console
DELETE /_snapshot/my_repository
```

#### Request

`DELETE /_snapshot/<repository>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<repository>`::
(Required, string)
Name of the snapshot repository to unregister. Wildcard (`*`) patterns are
supported.

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
