<!-- Converted from modules/cluster/allocation_filtering.asciidoc (AsciiDoc). Includes are inlined. -->

#### Cluster-level shard allocation filtering

You can use cluster-level shard allocation filters to control where Elasticsearch
allocates shards from any index. These cluster wide filters are applied in
conjunction with per-index allocation filtering
and allocation awareness.

Shard allocation filters can be based on custom node attributes or the built-in
`_name`, `_host_ip`, `_publish_ip`, `_ip`, `_host`, `_id` and `_tier` attributes.

The `cluster.routing.allocation` settings are dynamic, enabling live indices to
be moved from one set of nodes to another. Shards are only relocated if it is
possible to do so without breaking another routing constraint, such as never
allocating a primary and replica shard on the same node.

The most common use case for cluster-level shard allocation filtering is when
you want to decommission a node. To move shards off of a node prior to shutting
it down, you could create a filter that excludes the node by its IP address:

```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.routing.allocation.exclude._ip" : "10.0.0.1"
  }
}
```

##### Cluster routing settings

`cluster.routing.allocation.include.{attribute}`::
    (Dynamic)
    Allocate shards to a node whose `{attribute}` has at least one of the
    comma-separated values.

`cluster.routing.allocation.require.{attribute}`::
    (Dynamic)
    Only allocate shards to a node whose `{attribute}` has _all_ of the
    comma-separated values.

`cluster.routing.allocation.exclude.{attribute}`::
    (Dynamic)
    Do not allocate shards to a node whose `{attribute}` has _any_ of the
    comma-separated values.

The cluster allocation settings support the following built-in attributes:

`_name`::       Match nodes by node name
`_host_ip`::    Match nodes by host IP address (IP associated with hostname)
`_publish_ip`:: Match nodes by publish IP address
`_ip`::         Match either `_host_ip` or `_publish_ip`
`_host`::       Match nodes by hostname
`_id`::         Match nodes by node id
`_tier`::       Match nodes by the node's data tier role

**Note:** `_tier` filtering is based on node roles. Only
a subset of roles are data tier roles, and the generic
data role will match any tier filtering.
a subset of roles that are data tier roles, but the generic
data role will match any tier filtering.

You can use wildcards when specifying attribute values, for example:

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.exclude._ip": "192.168.2.*"
  }
}
```
