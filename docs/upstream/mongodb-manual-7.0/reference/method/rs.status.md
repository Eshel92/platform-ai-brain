<!-- Converted from reference/method/rs.status.txt (reStructuredText). Includes are inlined. -->

# rs.status() (mongosh method)

## Definition

**`rs.status()`**

Returns the replica set status from the point of view of the member
where the method is run. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetGetStatus` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

This output reflects the current status of the replica set, using
data derived from the heartbeat packets sent by the other members
of the replica set.

## Compatibility

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Output

For an example and details on the output, see replSetGetStatus.

If you run the `mongosh` helper method `rs.status()` 
(or the `replSetGetStatus` command) on a member during its 
initial sync (i.e. `STARTUP2` 
state), the command returns `replSetGetStatus.initialSyncStatus`
metrics.
      
Once the member completes its initial sync, the
`replSetGetStatus.initialSyncStatus` metrics becomes unavailable.
