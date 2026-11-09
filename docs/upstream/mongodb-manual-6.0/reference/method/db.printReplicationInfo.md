<!-- Converted from reference/method/db.printReplicationInfo.txt (reStructuredText). Includes are inlined. -->

# db.printReplicationInfo()

## Definition

**`db.printReplicationInfo()`**

Prints a formatted report of the replica set member's oplog.
The displayed report formats the data returned by
`db.getReplicationInfo()`.

The output of `db.printReplicationInfo()` is identical to
that of `rs.printReplicationInfo()`.

**Note:**

The `db.printReplicationInfo()` method run in `mongosh` does
**not** return JSON. Use `db.printReplicationInfo()` for manual inspection, and
`db.getReplicationInfo()` in scripts.

## Output Example

The following example is a sample output from the
`db.printReplicationInfo()` method run on the primary:

```none
configured oplog size:   192MB
log length start to end: 65422secs (18.17hrs)
oplog first event time:  Mon Jun 23 2014 17:47:18 GMT-0400 (EDT)
oplog last event time:   Tue Jun 24 2014 11:57:40 GMT-0400 (EDT)
now:                     Thu Jun 26 2014 14:24:39 GMT-0400 (EDT)
```

## Output Fields

`db.printReplicationInfo()` formats and prints the data returned by
`db.getReplicationInfo()`:

configured oplog size
   Displays the `db.getReplicationInfo.logSizeMB` value.

log length start to end
   Displays the `db.getReplicationInfo.timeDiff` and
   `db.getReplicationInfo.timeDiffHours` values.

oplog first event time
   Displays the `db.getReplicationInfo.tFirst`.

oplog last event time
   Displays the `db.getReplicationInfo.tLast`.

now
   Displays the `db.getReplicationInfo.now`.

See `db.getReplicationInfo()` for description of the data.

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
