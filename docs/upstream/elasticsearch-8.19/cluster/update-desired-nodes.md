<!-- Converted from cluster/update-desired-nodes.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update desired nodes API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Creates or updates the desired nodes.

#### Request

```console
PUT /_internal/desired_nodes/<history_id>/<version>
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

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`dry_run`::
    (Optional, Boolean) If `true`, then the request simulates the update and
    returns a response with `dry_run` field set to `true`.

#### Description

This API creates or update the desired nodes. External orchestrators can use
this API to let Elasticsearch know about the cluster topology, including future
changes such as adding or removing nodes. Using this information, the system is
able to take better decisions.

It's possible to run the update in "dry run" mode by adding the
`?dry_run` query parameter. This will validate the request result, but will not actually perform the update.

#### Examples

In this example, a new version for the desired nodes with history `Ywkh3INLQcuPT49f6kcppA` is created.
This API only accepts monotonically increasing versions.

```console
PUT /_internal/desired_nodes/Ywkh3INLQcuPT49f6kcppA/100
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

The API returns the following result:

```console-result
{
  "replaced_existing_history_id": false,
  "dry_run": false
}
```

Additionally, it is possible to specify a processors range.
This is helpful in environments where Elasticsearch nodes can
be deployed in hosts where the number of processors that the
Elasticsearch process can use is guaranteed to be at least the
lower range and up to the upper range. This is a common scenario
in Linux deployments where cgroups is used.
```console
PUT /_internal/desired_nodes/Ywkh3INLQcuPT49f6kcppA/101
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
            "processors_range" : {"min": 8.0, "max": 10.0},
            "memory" : "58gb",
            "storage" : "2tb"
        }
    ]
}
```

```console
DELETE /_internal/desired_nodes
```
