<!-- Converted from tutorial/configure-replica-set-secondary-sync-target.txt (reStructuredText). Includes are inlined. -->

# Configure a Self-Managed Secondary's Sync Target

## Overview

Secondaries capture data from the primary member to maintain an up to date
copy of the sets' data. However, by default secondaries may automatically
change their sync targets to secondary members based on changes in the
ping time between members and the state of other members’ replication. See
/core/replica-set-sync and
/tutorial/manage-chained-replication for more information.

For some deployments, implementing a custom replication sync topology may
be more effective than the default sync target selection logic. MongoDB
provides the ability to specify a host to use as a sync target.

To temporarily override the default sync target selection logic, you
may manually configure a secondary member's sync target to
temporarily pull oplog entries. The following provide access to
this functionality:

- `replSetSyncFrom` command, or

- `rs.syncFrom()` helper in `mongosh`

## Considerations

### Limitations

For `replSetSyncFrom`/`rs.syncFrom()` to override the default sync target, 
`settings.chainingAllowed` must be set to `true`.

If `settings.chainingAllowed` is set to `false`, `replSetSyncFrom`/`rs.syncFrom()` returns 
`ok:1` but does not set the sync target.

### Sync Logic

If an initial sync operation is in progress when you run
`replSetSyncFrom`/`rs.syncFrom()`, `replSetSyncFrom`/`rs.syncFrom()` stops the in-progress initial sync and
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

`replSetSyncFrom`/`rs.syncFrom()` provide a temporary override of default behavior.
`mongod` will revert to the default sync behavior in the
following situations:

- The `mongod` instance restarts.

- The connection between the `mongod` and the sync target
  closes.

- If the sync target falls more than 30 seconds behind another
  member of the replica set.

## Procedure

To use the `replSetSyncFrom` command in `mongosh`:

```javascript
db.adminCommand( { replSetSyncFrom: "hostname<:port>" } );
```

To use the `rs.syncFrom()` helper in `mongosh`:

```javascript
rs.syncFrom("hostname<:port>");
```
