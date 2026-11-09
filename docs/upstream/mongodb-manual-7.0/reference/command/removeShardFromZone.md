<!-- Converted from reference/command/removeShardFromZone.txt (reStructuredText). Includes are inlined. -->

# removeShardFromZone (database command)

## Definition

**`removeShardFromZone`**

The `removeShardFromZone` administrative command removes the
association between a shard and a zone.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.removeShardFromZone`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

You can only run `removeShardFromZone` on the `admin` database
from a `mongos` instance.

The command has the following syntax:

```javascript
db.adminCommand(
   {
     removeShardFromZone: <string>,
     zone: <string>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| removeShardFromZone | string | .. _cmd-removeShardFromZone-shard: The name of the shard from which to remove the zone association. |
| zone | string | .. _cmd-removeShardFromZone-zone: The name of the zone whose association with the shard you want to remove. |

       
`mongosh` provides the helper method
`sh.removeShardFromZone()`.

## Behavior

`removeShardFromZone` does not remove ranges associated with the
zone.

To completely remove a zone from the cluster, you must run 
`removeShardFromZone` on each shard associated with the zone.

If the shard specified is the last shard associated with the zone, you must
ensure there are no remaining shard key ranges associated with the zone. Use
`updateZoneKeyRange` to remove any existing ranges associated with
the zone before running `removeShardFromZone`.

See the zone manual page for more information on zones
in sharded clusters.

### Security

For sharded clusters that enforce access control, you must authenticate either as:

- a user whose privileges include:

  - `update` on the `shards` collection in the `config`
    database, and

  - `find` on the `tags` collection in the `config`
    database;
    
  or, alternatively

- a user whose privileges include `enableSharding` on the
  cluster resource.

The `clusterAdmin` or `clusterManager` built-in roles have
the appropriate permissions for issuing `removeShardFromZone`. See
the Role-Based Access Control manual page for more
information.

## Example

The following example removes the association between `shard0000` and zone
`NYC`:

```javascript
db.adminCommand( { removeShardFromZone : "shard0000" , zone : "NYC" } )
```
