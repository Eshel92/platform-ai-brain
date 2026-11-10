<!-- Converted from cluster/get-desired-nodes.asciidoc (AsciiDoc). Includes are inlined. -->

### Get desired nodes API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Get desired nodes.

#### Request

```console
PUT /_internal/desired_nodes/my_history/1
{
    "nodes" : [
        {
            "settings" : {
                 "node.name" : "instance-000187",
                 "node.external_id": "instance-000187",
                 "node.roles" : ["data_hot", "master"],
                 "node.attr.data" : "hot",
                 "node.attr.logical_availability_zone" : "zone-0"
            },
            "processors" : 8.0,
            "memory" : "59gb",
            "storage" : "2tb"
        }
    ]
}
```

```console
DELETE /_internal/desired_nodes
```

```console
GET /_internal/desired_nodes/_latest
```

#### Description

This API gets the latest desired nodes.

#### Examples

This example gets the latest desired nodes.

```console
GET /_internal/desired_nodes/_latest
```

The API returns the following result:

```console-result
{
    "history_id": <history_id>,
    "version": <version>,
    "nodes": [
        {
            "settings": <node_settings>,
            "processors": <node_processors>,
            "memory": "<node_memory>",
            "storage": "<node_storage>"
        }
    ]
}
```
