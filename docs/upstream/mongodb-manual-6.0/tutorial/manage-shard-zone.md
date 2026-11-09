<!-- Converted from tutorial/manage-shard-zone.txt (reStructuredText). Includes are inlined. -->

# Manage Shard Zones

In sharded clusters, you can create zones that represent a group of shards and
associate one or more ranges of shard key values to that zone. MongoDB
routes reads and writes that fall into a zone range only to those shards
inside of the zone.

**Tip:**

By defining the zones and the zone ranges *before* sharding an empty
or a non-existing collection, the shard collection operation creates
chunks for the defined zone ranges as well as any additional chunks
to cover the entire range of the shard key values and performs an
initial chunk distribution based on the zone ranges. This initial
creation and distribution of chunks allows for faster setup of zoned
sharding. After the initial distribution, the balancer manages the
chunk distribution going forward.

See pre-define-zone-range-example for an example.

## Add Shards to a Zone

Associate a Zone with a particular shard using the
`sh.addShardToZone()` method when connected to a `mongos`
instance. A single shard may have multiple zones, and multiple shards
may also have the same zone.

**Example:**

The following example adds the zone `NYC` to two shards, and the zones
`SFO` and `NRT` to a third shard:

```javascript
sh.addShardToZone("shard0000", "NYC")
sh.addShardToZone("shard0001", "NYC")
sh.addShardToZone("shard0002", "SFO")
sh.addShardToZone("shard0002", "NRT")
```

You may remove zone from a particular shard using the
`sh.removeShardFromZone()` method when connected to a
`mongos` instance, as in the following example, which removes
the `NRT` zone from a shard:

```javascript
sh.removeShardFromZone("shard0002", "NRT")
```

## Create a Zone Range

To define the zone's range of shard keys, use the `sh.updateZoneKeyRange()`
method when connected to a `mongos` instance. Any given shard key
range may only have *one* assigned zone. You cannot overlap defined ranges.

**Example:**

Given a collection named `users` in the `records` database,
sharded by the `zipcode` field. The following operations assign:

- two ranges of zip codes in Manhattan and Brooklyn the `NYC` zone

- one range of zip codes in San Francisco the `SFO` zone

```javascript
sh.updateZoneKeyRange("records.users", { zipcode: "10001" }, { zipcode: "10281" }, "NYC")
sh.updateZoneKeyRange("records.users", { zipcode: "11201" }, { zipcode: "11240" }, "NYC")
sh.updateZoneKeyRange("records.users", { zipcode: "94102" }, { zipcode: "94135" }, "SFO")
```

**Note:**

- .. include:: /includes/fact-shard-ranges-inclusive-exclusive.rst

- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

## Remove a Zone Range

Use the shell helper method `sh.removeRangeFromZone()` to
remove a range from a zone.

**Example:**

The following example removes the `NYC` zone assignment for the
range of zip codes within Manhattan:

```javascript
sh.removeRangeFromZone("records.user", {zipcode: "10001"}, {zipcode: "10281"})
```

**Note:**

Dropping a collection deletes its associated zone/tag ranges.

   

## View Existing Zones

Use `sh.status()` to list the zones associated to each shard in the
cluster. You can also view a shards zones by querying the
`shards` collection in the `config` database. 

The following example uses the `find()` method to
return all shards with the `NYC` zone.

```javascript
use config
db.shards.find({ tags: "NYC" })
```

You can find zone ranges for all namespaces in the
`tags` collection of the `config` database. The output
of `sh.status()` also displays all zone ranges.

The following example uses the `find()` method to
return any range associated to the `NYC` zone.

```javascript
use config
db.tags.find({ tag: "NYC" })
```
