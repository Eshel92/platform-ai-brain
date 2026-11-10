<!-- Converted from snapshot-restore/apis/verify-repo-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Verify snapshot repository API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Checks for common misconfigurations in a snapshot repository. See
snapshots-repository-verification.

```console
POST /_snapshot/my_repository/_verify
```

#### Request

`POST /_snapshot/<repository>/_verify`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<repository>`::
(Required, string)
Name of the snapshot repository to verify.

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

`nodes`::
(object)
**Properties of `nodes` objects**
`<node_id>`::
(object)
Contains information about a node connected to the snapshot repository.
The key is the ID of the node.
**Properties of `<node_id>`**
=====
`name`::
(string)
Human-readable name for the node.
You can set this name using the `node.name` property in
`elasticsearch.yml`. Defaults to the machine's hostname.
=====
