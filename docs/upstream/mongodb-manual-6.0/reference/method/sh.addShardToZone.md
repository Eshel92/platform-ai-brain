<!-- Converted from reference/method/sh.addShardToZone.txt (reStructuredText). Includes are inlined. -->

# sh.addShardToZone()

## Definition

**`sh.addShardToZone(shard, zone)`**

Associates a shard with a zone. MongoDB associates this shard
with the given zone. Chunks that are covered by the zone are assigned to
shards associated with the zone.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `addShardToZone` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

This method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| shard | string | .. _method-addShardToZone-shard: The name of the shard to which to associate the zone. |
| zone | string | .. _method-addShardToZone-zone: The name of the zone to associate with the shard. |

Only issue `sh.addShardToZone()` when connected to a
`mongos` instance.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

You can associate a zone with multiple shards, and a shard can associate with
multiple zones.

See the zone manual page for more information on zones
in sharded clusters.

### Ranges

MongoDB effectively ignores zones that do not have at least one range of
shard key values associated with it.

To associate a range of shard key values with a zone, use the
`sh.updateZoneKeyRange()` method.

You can run `updateZoneKeyRange` database command and its helpers
`sh.updateZoneKeyRange()` and `sh.addTagRange()` on
an unsharded collection or a non-existing collection.

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

## Security

For sharded clusters that enforce access control, you must authenticate as a user
whose privileges include either:

- `update` on the `shards` collection in the `config`
  database; or, alternatively,

- `enableSharding` on the cluster resource.

The `clusterAdmin` or `clusterManager` built-in roles have
the appropriate permissions for issuing `sh.addShardToZone()`. See the
Role-Based Access Control manual page for more
information.

## Example

The following example adds three zones, `NYC`, `LAX`, and `NRT`,
associating each to a shard:

```javascript
sh.addShardToZone("shard0000", "JFK")
sh.addShardToZone("shard0001", "LAX")
sh.addShardToZone("shard0002", "NRT")
```

A shard can associate with multiple zones. The following example associates
`LGA` to `shard0000`:

```javascript
sh.addShardToZone("shard0000", "LGA")
```

`shard0000` associates with both the `LGA` zone and the `JFK` zone. In a
balanced cluster, MongoDB routes reads and writes covered by either zone to
`shard0000`.

**See also:**

- `sh.updateZoneKeyRange()`
- `sh.removeShardFromZone()`
