<!-- Converted from tutorial/sharding-distribute-collections-with-zones.txt (reStructuredText). Includes are inlined. -->

# Distribute Collections Using Zones

In sharded clusters, you can create zones of sharded data
based on the shard key. You can associate each zone with one or
more shards in the cluster. A shard can associate with any number of
zones. In a balanced cluster, MongoDB migrates chunks
covered by a zone only to those shards associated with the zone. 

You can use zone sharding to distribute
collections across a sharded cluster and designate which shards store
data for each collection. You can distribute collections based on shard
properties, such as physical resources and available memory, to ensure
that each collection is stored on the optimal shard for that data.

## Prerequisites

To complete this tutorial, you must:

- Deploy a sharded cluster. This
  tutorial uses a sharded cluster with three shards.

- Connect to a `mongos`. You cannot create zones or zone ranges
  by connecting directly to a shard.

- Authenticate as a user with at least the `clusterManager`
  role on the `admin` database. To view user permissions, use the
  `db.getUser()` method.

## Scenario

You have a database called `shardDistributionDB` that contains two
sharded collections:

- `bigData`, which contains a large amount of data.

- `manyIndexes`, which contains many large indexes.

You want to limit each collection to a subset of shards so that each
collection can use the shards' different physical resources.

### Architecture

The sharded cluster has three shards. Each shard has unique physical
resources:

| Shard Name | Physical Resources |
|---|---|
| `shard0` | High memory capacity |
| `shard1` | Fast flash storage |
| `shard2` | High memory capacity **and** fast flash storage |

### Zones

To distribute collections based on physical resources, use shard zones.
A shard zone associates collections with a specific subset of shards,
which restricts the shards that store the collection's data. In this
example, you need two shard zones:

| Zone Name | Description | Collections in this Zone |
|---|---|---|
| `HI_RAM` | Servers with high memory capacity. | Collections requiring more memory, such as collections with large indexes, should be on the `HI_RAM` shards. |
| `FLASH` | Servers with flash drives for fast storage speeds. | Large collections requiring fast data retrieval should be on the `FLASH` shards. |

### Shard Key

In this tutorial, the shard key you will use to shard
each collection is `{ _id: "hashed" }`. You will configure shard zones
**before** you shard the collections. As a result, each collection's
data only ever exists on the shards in the corresponding zone.

With hashed sharding, if you shard
collections before you configure zones, MongoDB assigns chunks evenly between all shards when sharding is enabled. This means
that chunks may be temporarily assigned to a shard poorly suited to
handle that chunk's data.

### Balancer

The balancer migrates chunks to the
appropriate shard, respecting any configured zones. When balancing is
complete, shards only contain chunks whose ranges match its assigned
zones.

**Important:** Performance

Adding, removing, or changing zones or zone ranges can result in
chunk migrations. Depending on the size of your dataset and the
number of chunks a zone or zone range affects, these migrations may
impact cluster performance. Consider running the balancer during
specific scheduled windows. To learn how to set a scheduling window,
see sharding-schedule-balancing-window.

## Steps

Use the following procedure to configure shard zones and distribute
collections based on shard physical resources.

**Step 1: Add each shard to the appropriate zone.**

To configure the shards in each zone, use the
`addShardToZone` command.

Add `shard0` and `shard2` to the `HI_RAM` zone:

```javascript
sh.addShardToZone("shard0", "HI_RAM")

sh.addShardToZone("shard2", "HI_RAM")
```

Add `shard1` and `shard2` to the `FLASH` zone:

```javascript
sh.addShardToZone("shard1", "FLASH")

sh.addShardToZone("shard2", "FLASH")
```

**Step 2: Add zone ranges for the relevant collections.**

To associate a range of
shard keys to a zone, use `sh.updateZoneKeyRange()`. 

In this scenario, you want to associate all documents in a
collection to the appropriate zone. To associate all collection
documents to a zone, specify the following zone range:

- a lower bound of `{ "_id" : MinKey }`
- an upper bound of `{ "_id" : MaxKey }`

For the `bigData` collection, set:

- The namespace to `shardDistributionDB.bigData`,
- The lower bound to `MinKey`,
- The upper bound to `MaxKey`, 
- The zone to `FLASH`

```javascript
sh.updateZoneKeyRange(
   "shardDistributionDB.bigData",
   { "_id" : MinKey },
   { "_id" : MaxKey },
   "FLASH"
)
```

For the `manyIndexes` collection, set:

- The namespace to `shardDistributionDB.manyIndexes`,
- The lower bound to `MinKey`,
- The upper bound to `MaxKey`, 
- The zone to `HI_RAM`

```javascript
sh.updateZoneKeyRange(
   "shardDistributionDB.manyIndexes",
   { "_id" : MinKey },
   { "_id" : MaxKey },
   "HI_RAM"
)
```

**Step 3: Shard the collections.**

To shard both collections (`bigData` and `manyIndexes`),
specify a shard key of `{ _id: "hashed" }`.

Run the following commands:

```javascript
sh.shardCollection(
   "shardDistributionDB.bigData", { _id: "hashed" }
)

sh.shardCollection(
   "shardDistributionDB.manyIndexes", { _id: "hashed" }
)
```

**Step 4: Review the changes.**

To view chunk distribution and shard zones, use the
`sh.status()` method:

```javascript
sh.status()
```

The next time the balancer runs, it
splits chunks where necessary and migrates chunks across the
shards, respecting the configured zones. The amount of time the
balancer takes to complete depends on several factors, including
number of shards, available memory, and
IOPS (Input/Output Operations Per Second).

When balancing finishes:

- Chunks for documents in the `manyIndexes` collection reside on
  `shard0` and `shard2`

- Chunks for documents in the `bigData` collection reside on
  `shard1` and `shard2`.

## Learn More

To learn more about sharding and balancing, see the following pages:

- sharding-data-partitioning
- index-type-hashed
- sharding-manage-zones
- sharding-shards
