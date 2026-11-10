<!-- Converted from modules/cluster.asciidoc (AsciiDoc). Includes are inlined. -->

### Cluster-level shard allocation and routing settings

Shard allocation is the process of assigning shard copies to nodes. This can
happen during initial recovery, replica allocation, rebalancing, when nodes are added to or removed from the cluster, or when cluster or index settings that impact allocation are updated.
One of the main roles of the master is to decide which shards to allocate to
which nodes, and when to move shards between nodes in order to rebalance the
cluster.

There are a number of settings available to control the shard allocation process:

*   cluster-shard-allocation-settings control allocation and
    rebalancing operations.

*   disk-based-shard-allocation explains how Elasticsearch takes available
    disk space into account, and the related settings.

*   shard-allocation-awareness and forced-awareness control how shards
    can be distributed across different racks or availability zones.

*   cluster-shard-allocation-filtering allows certain nodes or groups of
    nodes excluded from allocation so that they can be decommissioned.

*   node-allocation-stats-cache control the node allocation statistics cache on the master node.

Besides these, there are a few other miscellaneous cluster-level settings.

(See `modules/cluster/shards_allocation.md`)
(See `modules/cluster/disk_allocator.md`)

#### Shard allocation awareness settings

You can use custom node attributes as _awareness attributes_ to enable Elasticsearch
to take your physical hardware configuration into account when allocating shards.
If Elasticsearch knows which nodes are on the same physical server, in the same rack, or
in the same zone, it can distribute the primary shard and its replica shards to
minimize the risk of losing all shard copies in the event of a failure. Learn more about shard allocation awareness.

`cluster.routing.allocation.awareness.attributes`::
      (Dynamic)
      The node attributes that Elasticsearch should use as awareness attributes. For example, if you have a `rack_id` attribute that specifies the rack in which each node resides, you can set this setting to `rack_id` to ensure that primary and replica shards are not allocated on the same rack. You can specify multiple attributes as a comma-separated list.

`cluster.routing.allocation.awareness.force.*`:: 
        (Dynamic)
        The shard allocation awareness values that must exist for shards to be reallocated in case of location failure. Learn more about forced awareness.
      

(See `modules/cluster/allocation_filtering.md`)

#### Cluster-level node allocation stats cache settings

`cluster.routing.allocation.stats.cache.ttl`::
      (Dynamic)
      Calculating the node allocation stats for a Get node statistics API call can become expensive on the master for clusters with a high number of nodes. To prevent overloading the master the node allocation stats are cached on the master for 1 minute `1m` by default.  This setting can be used to adjust the cache time to live value, if necessary, keeping in mind the tradeoff between the freshness of the statistics and the processing costs on the master.  The cache can be disabled (not recommended) by setting the value to `0s` (the minimum value). The maximum value is 10 minutes `10m`.

(See `modules/cluster/misc.md`)
