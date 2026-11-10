<!-- Converted from shutdown/apis/shutdown-delete.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete shutdown API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Node lifecycle APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-shutdown).

Cancels shutdown preparations or clears a shutdown request
so a node can resume normal operations.

#### Request

`DELETE _nodes/<node-id>/shutdown`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

* If the {operator-feature} is enabled,
you must be an operator to use this API.

#### Description

Enables a node to resume normal operations following a
put shutdown request.
You must explicitly clear the shutdown request when a node rejoins the cluster,
or when a node has permanently left the cluster. Shutdown requests are never
removed automatically by Elasticsearch.

#### Path parameters

`<node-id>`::
(Optional, string)
The ID of a node that you prepared for shut down.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

Prepare a node to be restarted:

```console
PUT /_nodes/USpTGYaBSIKbgSUJR2Z9lg/shutdown
{
  "type": "restart",
  "reason": "Demonstrating how the node shutdown API works"
}
```

Cancel the shutdown preparations or clear the shutdown request
after restarting:

```console
DELETE /_nodes/USpTGYaBSIKbgSUJR2Z9lg/shutdown
```

Which returns the following response:

```console-result
{
    "acknowledged": true
}
```
