<!-- Converted from reference/method/db.fsyncLock.txt (reStructuredText). Includes are inlined. -->

# db.fsyncLock()

## Definition

**`db.fsyncLock()`**

Flushes all pending writes from the storage layer to disk and locks the
server to prevent any additional writes until the lock is released.

   `db.fsyncUnlock` methods

Starting in MongoDB 6.0.11 (also available starting in
5.0.22) the `db.fsyncLock()` and can run on
`mongos` to lock and unlock a sharded cluster.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `fsync` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Servers maintain an fsync lock count.  The `fsyncLock` method
increments the lock count while the `fsyncUnlock` method decrements
it. To unlock writes on a server or cluster, call the `fsyncUnlock`
method until the lock count reaches zero.

`db.fsyncLock()`  has the syntax:

```javascript
db.fsyncLock()
```

The operation returns a document with the following fields:

| Field | Description |
|---|---|
| `info` | Information on the status of the operation. |
| `lockCount` | Number of locks currently on the instance. |
| `seeAlso` | Link to the `fsync` command documentation. |
| `ok` | The status code. |

`db.fsyncLock()` is an administrative command. Use this method to
lock a server or cluster before backup operations.

## Compatibility

This method is available in deployments hosted in the following environments: 

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

`db.fsyncLock()` ensures that the data files are safe to copy
using low-level backup utilities such as `cp`, `scp`, or
`tar`. A `mongod` started using the copied
files contains user-written data that is indistinguishable from the 
user-written data on the locked `mongod`.

The data files of a locked `mongod` may change due to
operations such as journaling syncs or
WiredTiger snapshots.  While
this has no affect on the logical data (e.g. data accessed by
clients), some backup utilities may detect these changes and emit
warnings or fail with errors. For more information on MongoDB-
recommended backup utilities and procedures, see
/core/backups/.

### Fsync Locks after Failures

Fsync locks execute on the primary in a replica set or sharded cluster.

If the primary goes down or becomes unreachable due to network issues, the
cluster elects a new primary from the available
secondaries. If a primary with an fsync lock goes down, the new primary does
**not** retain the fsync lock and can handle write operations. When elections
occur during backup operations, the resulting backup may be inconsistent or
unusable.

To recover from the primary going down:

#. Run the `db.fsyncUnlock` method until the lock count reaches zero
   to release the lock on all nodes.

#. Issue the `db.fsyncLock` command to reestablish the fsync lock on the
   cluster.

#. Restart the backup.

Additionally, fsync locks are persistent. When the old primary comes online
again, you need to run the `db.fsyncUnlock` command to release the
lock on the node.

## Example

The following operation runs `db.fsyncLock()`:

```javascript
db.fsyncLock()
```

The operation returns the following status document that includes the
`lockCount`:

```javascript
{
   "info" : "now locked against writes, use db.fsyncUnlock() to unlock",
   "lockCount" : NumberLong(1),
   "seeAlso" : "http://dochub.mongodb.org/core/fsynccommand",
   "ok" : 1
}
```

If you run `db.fsyncLock()` again, the operation increments the
`lockCount`:

```javascript
{
   "info" : "now locked against writes, use db.fsyncUnlock() to unlock",
   "lockCount" : NumberLong(2),
   "seeAlso" : "http://dochub.mongodb.org/core/fsynccommand",
   "ok" : 1
}
```

To unlock the instance for writes, you must run
`db.fsyncUnlock()` twice to reduce the `lockCount` to 0.
