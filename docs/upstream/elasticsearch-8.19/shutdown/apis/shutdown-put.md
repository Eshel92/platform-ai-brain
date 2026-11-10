<!-- Converted from shutdown/apis/shutdown-put.asciidoc (AsciiDoc). Includes are inlined. -->

### Put shutdown API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Node lifecycle APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-shutdown).

Prepares a node to be shut down.

#### Request

`PUT _nodes/<node-id>/shutdown`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

* If the {operator-feature} is enabled, you must be an operator
to use this API.

#### Description

Migrates ongoing tasks and index shards to other nodes as needed
to prepare a node to be restarted or shut down and removed from the cluster.
This ensures that Elasticsearch can be stopped safely with minimal disruption to the cluster.

You must specify the type of shutdown: `restart`, `remove`, or `replace`.
If a node is already being prepared for shutdown,
you can use this API to change the shutdown type.

**Important:** This API does *NOT* terminate the Elasticsearch process.
Monitor the node shutdown status to determine
when it  is safe to stop Elasticsearch.

#### Path parameters

`<node-id>`::
(Required, string)
The ID of the node you want to prepare for shutdown.
If you specify a node that is offline,
it will be prepared for shut down when it rejoins the cluster.

**Important:** This parameter is *NOT* validated against the cluster's active nodes.
This enables you to register a node for shut down while it is offline.
No error is thrown if you specify an invalid node ID.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`type`::
(Required, string)
Valid values are `restart`, `remove`, or `replace`.
Use `restart` when you need to temporarily shut down a node to perform an upgrade,
make configuration changes, or perform other maintenance.
Because the node is expected to rejoin the cluster, data is not migrated off of the node.
Use `remove` when you need to permanently remove a node from the cluster.
The node is not marked ready for shutdown until data is migrated off of the node.
Use `replace` to do a 1:1 replacement of a node with another node. Certain allocation decisions will
be ignored (such as disk watermarks) in the interest of true replacement of the source node with the
target node. During a replace-type shutdown, rollover and index creation may result in unassigned
shards, and shrink may fail until the replacement is complete.

`reason`::
(Required, string)
A human-readable reason that the node is being shut down.
This field provides information for other cluster operators;
it does not affect the shut down process.

`allocation_delay`::
(Optional, string)
Only valid if `type` is `restart`. Controls how long Elasticsearch will wait for the node to restart and join the cluster before reassigning its shards to other nodes. This works the same as
delaying allocation with the `index.unassigned.node_left.delayed_timeout` setting. If you specify both a restart allocation delay and an index-level allocation delay, the longer of the two is used.

`target_node_name`::
(Optional, string)
Only valid if `type` is `replace`. Specifies the name of the node that is replacing the node being
shut down. Shards from the shut down node are only allowed to be allocated to the target node, and
no other data will be allocated to the target node. During relocation of data certain allocation
rules are ignored, such as disk watermarks or user attribute filtering rules.

#### Examples

Register a node for shutdown:

```console
PUT /_nodes/USpTGYaBSIKbgSUJR2Z9lg/shutdown
{
  "type": "restart", <1>
  "reason": "Demonstrating how the node shutdown API works",
  "allocation_delay": "20m"
}
```

<1> Prepares the node to be restarted.
Use `remove` for nodes that will be permanently removed from the cluster.
