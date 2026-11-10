<!-- Converted from shutdown/apis/shutdown-get.asciidoc (AsciiDoc). Includes are inlined. -->

### Get shutdown API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Node lifecycle APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-shutdown).

Retrieves the status of a node that's being prepared for shutdown.

#### Request

`GET _nodes/shutdown`

`GET _nodes/<node-id>/shutdown`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

* If the {operator-feature} is enabled,
you must be an operator to use this API.

#### Description

Indicates whether a node is ready to be shut down, or if shut down preparations
are still in progress or have stalled.
Returns status information for each part of the shut down process.
Use to monitor the shut down process after calling put shutdown.

#### Path parameters

`<node-id>`::
(Optional, string)
The ID of a node that is being prepared for shutdown.
If no ID is specified, returns the status of all nodes being prepared for shutdown.

#### Examples

Prepare a node to be restarted:

```console
PUT /_nodes/USpTGYaBSIKbgSUJR2Z9lg/shutdown
{
  "type": "restart",
  "reason": "Demonstrating how the node shutdown API works",
  "allocation_delay": "10m"
}
```

Get the status of the shutdown preparations:

```console
GET /_nodes/USpTGYaBSIKbgSUJR2Z9lg/shutdown
```

The response shows information about the shutdown preparations,
including the status of shard migration, task migration, and plugin cleanup:

```console-result
{
    "nodes": [
        {
            "node_id": "USpTGYaBSIKbgSUJR2Z9lg",
            "node_ephemeral_id": null,
            "type": "RESTART",
            "reason": "Demonstrating how the node shutdown API works",
            "shutdown_started_millis": 1624406108685,
            "allocation_delay": "10m",
            "status": "COMPLETE",
            "shard_migration": {
                "status": "COMPLETE",
                "shard_migrations_remaining": 0,
                "explanation": "no shard relocation is necessary for a node restart"
            },
            "persistent_tasks": {
                "status": "COMPLETE"
            },
            "plugins": {
                "status": "COMPLETE"
            }
        }
    ]
}
```
