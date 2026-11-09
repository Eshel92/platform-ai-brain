<!-- Converted from reference/method/sh.removeShardFromZone.txt (reStructuredText). Includes are inlined. -->

# sh.removeShardFromZone() (mongosh method)

## Definition

**`sh.removeShardFromZone(shard, zone)`**

Removes the association between a zone and a shard.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `removeShardFromZone` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

This method has the following parameters:

| Parameter | Type | Description |
|---|---|---|
| shard | string | .. _method-removeShardFromZone-shard: The name of the shard from which to remove the zone association. |
| zone | string | .. _method-removeShardFromZone-zone: The name of the zone whose association with the shard  you want to remove. |

Only issue `sh.removeShardFromZone()` when connected to a
`mongos` instance.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

`sh.removeShardFromZone()` does not remove ranges associated with the
zone.

To completely remove a zone from the cluster, you must run
`sh.removeShardFromZone()` on each shard associated with the zone.

If the shard specified is the last shard associated with the zone, you
must ensure there are no remaining ranges associated with the zone. Use
`updateZoneKeyRange` to remove any existing ranges associated to
the zone before running `sh.removeShardFromZone()`.

See the zone manual page for more information on zones
in sharded clusters.

### Balancer

Removing the association between a zone and a shard removes the constraints
keeping chunks covered by the zone on the shard. During the next balancer
round, the balancer may migrate chunks that previously covered by the zone.

See the sharded cluster balancer manual page
for more information on how migrations work in a sharded cluster.

### Security

For sharded clusters that enforce access control, you must authenticate either as:

- a user whose privileges include:

  - `update` on the `shards` collection in the `config`
    database, and

  - `find` on the `tags` collection in the `config`
    database;

  or, alternatively,

- a user whose privileges include `enableSharding` on the
  cluster resource.

The `clusterAdmin` or `clusterManager` built-in roles have
the appropriate permissions for issuing `sh.removeShardFromZone()`.
See the Role-Based Access Control manual page for more
information.

## Example

The following example removes the association between `shard0000` and the
`NYC` zone:

```javascript
sh.removeShardFromZone("shard0000", "NYC")
```

**See also:**

`sh.addShardToZone()`
`sh.updateZoneKeyRange()`
`sh.removeRangeFromZone()`
