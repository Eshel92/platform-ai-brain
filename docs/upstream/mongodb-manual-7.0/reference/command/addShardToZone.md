<!-- Converted from reference/command/addShardToZone.txt (reStructuredText). Includes are inlined. -->

# addShardToZone (database command)

## Definition

**`addShardToZone`**

Associates a shard with a zone. MongoDB associates this shard with
the given zone. Chunks that are covered by the zone are assigned to shards
associated with the zone.

**Tip:**

In `mongosh`, this command can also be run through the `sh.addShardToZone` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

You can only run `addShardToZone` on the `admin` database
from a `mongos` instance.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

    
The command has the following syntax:

```javascript
db.adminCommand(
   {
     addShardToZone: <string>,
     zone: <string>
   }
)
```

### Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| addShardtoZone | string | .. _cmd-addShardToZone-shard: The name of the shard to associate with the zone. |
| zone | string | .. _cmd-addShardToZone-zone: The name of the zone to associate with the shard. |

`mongosh` provides the helper method
`sh.addShardToZone()`.

## Behavior

You can associate a zone with multiple shards, and a shard can associate with
multiple zones.

See the zone manual page for more information on zones
in a sharded cluster.

### Ranges

MongoDB effectively ignores zones that do not have at least one range of
shard key values associated with it. 

To associate a range of shard key values with a zone, use the
`updateZoneKeyRange` database command, or the
`sh.updateZoneKeyRange()` shell helper.

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
the appropriate permissions for issuing `addShardToZone`. See the
documentation page for Role-Based Access Control for
more information.

## Example

The following example associates `shard0000` with zone `JFK`:

```javascript
db.adminCommand( { addShardToZone : "shard0000" , zone : "JFK" } )
```

A shard can associate with multiple zones. The following example associates
`LGA` to `shard0000`:

```javascript
db.adminCommand( { addShardToZone : "shard0000" , zone : "LGA" } )
```

`shard0000` associates with both the `LGA` zone and the `JFK` zone. In a
balanced cluster, MongoDB routes reads and writes covered by either zone to
`shard0000`.
