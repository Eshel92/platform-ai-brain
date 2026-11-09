<!-- Converted from reference/method/rs.syncFrom.txt (reStructuredText). Includes are inlined. -->

# rs.syncFrom() (mongosh method)

## Definition

**`rs.syncFrom()`**

Temporarily overrides the default sync target for the current member. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetFreeze` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Specify the name of the member you
want to replicate from in the form of `[hostname]:[port]`.

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Limitations

For `replSetSyncFrom` to override the default sync target, 
`settings.chainingAllowed` must be set to `true`.

If `settings.chainingAllowed` is set to `false`, `replSetSyncFrom` returns 
`ok:1` but does not set the sync target.

Starting in MongoDB 5.0.2, you can override `settings.chainingAllowed` 
by setting the server parameter `enableOverrideClusterChainingSetting` 
to `true`. This allows syncing from a Secondary member even if 
`settings.chainingAllowed` is `false`.

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

- If the sync target falls more than
  `maxSyncSourceLagSecs` (default 30) seconds behind another
  member of the replica set.

## Example

To use the `rs.syncFrom()` helper in `mongosh`:

```javascript
rs.syncFrom("myHost:27017");
```

**See also:**

`replSetSyncFrom`
