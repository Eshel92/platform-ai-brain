<!-- Converted from cluster/delete-desired-nodes.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete desired nodes API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Delete desired nodes.

#### Request

```console
PUT /_internal/desired_nodes/history/1
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
            "memory" : "58gb",
            "storage" : "2tb"
        }
    ]
}
```

```console
DELETE /_internal/desired_nodes
```

#### Description

This API deletes the desired nodes.

#### Examples

This example deletes the current desired nodes.

```console
DELETE /_internal/desired_nodes
```
