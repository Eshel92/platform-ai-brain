<!-- Converted from reference/command/replSetSyncFrom.txt (reStructuredText). Includes are inlined. -->

# replSetSyncFrom

## Description

**`replSetSyncFrom`**

Temporarily overrides the default sync target for the current
`mongod`. This operation is useful for testing different
patterns and in situations where a set member is not replicating
from the desired host.

**Tip:**

In `mongosh`, this command can also be run through the `rs.syncFrom` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

Run `replSetSyncFrom` in the `admin` database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, M10+, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     replSetSyncFrom: "hostname<:port>" 
   }
 )
```

## Command Fields

The command takes the following field:

| Field | Type | Description |
|---|---|---|
| `replSetSyncFrom` | string | The name and port number of the replica set member that this member should replicate from. Use the `[hostname]:[port]` form. Replica set members with `1 vote` cannot sync from members with  `0 votes`. |

           

## Behavior

### Limitations

For `replSetSyncFrom` to override the default sync target, 
`settings.chainingAllowed` must be set to `true`.

If `settings.chainingAllowed` is set to `false`, `replSetSyncFrom` returns 
`ok:1` but does not set the sync target.

### Sync Logic

If an initial sync operation is in progress when you run
`replSetSyncFrom`, `replSetSyncFrom` stops the in-progress initial sync and
restarts the sync process with the new target. 

Only modify the default sync logic as needed, and always exercise
caution. 

### Target

The member to sync from must be a valid source for data in the set.
To sync from a member, the member must:

- Have data. It cannot be an arbiter, in startup or recovering mode, and
  must be able to answer data queries.

- Be accessible.

- Be a member of the same set in the replica set configuration.

- Build indexes with the
  `members[n].buildIndexes` setting.

- A different member of the set, to prevent syncing from itself.

If you attempt to replicate from a member that is more than 10 seconds
behind the current member, `mongod` will log a warning but will
still replicate from the lagging member.  See also 
replication-flow-control.

### Persistence

`replSetSyncFrom` provide a temporary override of default behavior.
`mongod` will revert to the default sync behavior in the
following situations:

- The `mongod` instance restarts.

- The connection between the `mongod` and the sync target
  closes.

- If the sync target falls more than 30 seconds behind another
  member of the replica set.

For more information the use of `replSetSyncFrom`, see
/tutorial/configure-replica-set-secondary-sync-target.
