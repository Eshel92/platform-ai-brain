<!-- Converted from reference/method/db.getReplicationInfo.txt (reStructuredText). Includes are inlined. -->

# db.getReplicationInfo()

## Definition

**`db.getReplicationInfo()`**

Returns a document with the status of the replica set, using data
polled from the oplog. Use this output when diagnosing
issues with replication.
   

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

**`db.getReplicationInfo.logSizeMB`**

Returns the total size of the oplog in megabytes. This refers
to the total amount of space allocated to the oplog rather than the
current size of operations stored in the oplog.

The oplog can grow past its configured size
limit to avoid deleting the `majority commit point`.

**`db.getReplicationInfo.usedMB`**

Returns the total amount of space used by the oplog in
megabytes. This refers to the total amount of space currently used by
operations stored in the oplog rather than the total amount of space
allocated.

**`db.getReplicationInfo.errmsg`**

Returns an error message if there are no entries in the oplog.

**`db.getReplicationInfo.oplogMainRowCount`**

Only present when there are no entries in the oplog. Reports a the
number of items or rows in the oplog (e.g. `0`).

**`db.getReplicationInfo.timeDiff`**

Returns the difference between the first and
last operation in the oplog, represented in seconds.

Only present if there are entries in the oplog.

**`db.getReplicationInfo.timeDiffHours`**

Returns the difference between the first and last
operation in the oplog, rounded and represented in hours.

Only present if there are entries in the oplog.

**`db.getReplicationInfo.tFirst`**

Returns a time stamp for the first (i.e. earliest)
operation in the oplog. Compare this value to the last write
operation issued against the server.

Only present if there are entries in the oplog.

**`db.getReplicationInfo.tLast`**

Returns a time stamp for the last (i.e. latest)
operation in the oplog. Compare this value to the last write
operation issued against the server.

Only present if there are entries in the oplog.

**`db.getReplicationInfo.now`**

Returns a timestamp that reflects the current time.
The shell process generates this value, and the datum may differ
slightly from the server time if you're connecting from a remote host
as a result. Equivalent to `Date()`.

Only present if there are entries in the oplog.
