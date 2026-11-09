<!-- Converted from reference/command/fsync.txt (reStructuredText). Includes are inlined. -->

# fsync (database command)

## Definition

**`fsync`**

Flushes all pending writes from the storage layer to disk. When the `lock`
field is set to `true`, it sets a lock on the server or cluster to prevent
additional writes until the lock is released.

   `fsyncUnlock` commands

Starting in MongoDB 7.0.2 (also available starting in
6.0.11, and 5.0.22) the `fsync` and can run on
`mongos` to lock and unlock a sharded cluster.

As applications write data, MongoDB records the data in the storage layer
and then writes the data to disk.

Run `fsync` when you want to flush writes to disk.

To provide durable data, WiredTiger
uses checkpoints. For more
details, see journaling-wiredTiger.

**Important:**

Servers maintain an fsync lock count.  The `fsync` command with
the `lock` field set to `true` increments the lock count while the
`fsyncUnlock` command decrements it. To enable writes on a locked
server or cluster, call the `fsyncUnlock` command until the lock
count reaches zero.

Use this command to block writes when you want to perform backup
operations.

**Tip:**

In `mongosh`, this command can also be run through the `db.fsyncLock` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     fsync: 1,
     lock: <Boolean>,
     fsyncLockAcquisitionTimeout: <integer>,
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

* - Field
  - Type
  - Description

* - `fsync`
  - integer
  - Enter "1" to apply `fsync`.

* - `fsyncLockAcquisitionTimeoutMillis`
  - integer
  - Optional. Specifies the amount of time in milliseconds to wait to
    acquire locks. If the lock acquisition operation times out, the
    command returns a failed response.

    Default: `90000`

    **New in version:** 7.0.2

* - `lock`
  - boolean
  - Optional. Takes a lock on the server or cluster and blocks all
    write operations. Each `fsync` with `lock` operation
    takes a lock.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

## Considerations

`fsync` command with the `lock` option ensures that the data files are safe to copy
using low-level backup utilities such as `cp`, `scp`, or
`tar`. A `mongod` started using the copied
files contains user-written data that is indistinguishable from the 
user-written data on the locked `mongod`.

The data files of a locked `mongod` may change due to
operations such as journaling syncs or
WiredTiger snapshots.  While
this has no effect on the logical data (e.g. data accessed by
clients), some backup utilities may detect these changes and emit
warnings or fail with errors. For more information on MongoDB-
recommended backup utilities and procedures, see
/core/backups/.

### Impact on Larger Deployments

**New in version:** 7.0.2

When the `fsync` command runs on `mongos`, it performs the fsync
operation on the entire cluster. By setting the `lock` field to `true`,
it sets a lock on the cluster, preventing additional writes.

To take a usable self-managed backup, before locking a sharded cluster:

- Ensure that no chunk migration, resharding, or DDL operations are active.

- Stop the balancer to prevent additional chunk migrations from starting.

**Important:**

`mongod` uses journaling to improve durability.
Use a file system or volume/block level snapshot tool
to create a backup of the data set and the journal together as a single unit.

### Lock Count

The `fsync` command returns a document includes a `lockCount` field. When
run on `mongod`, the count indicates the number of fsync locks set on
the server.

When run on a sharded cluster, `mongos` sends the fsync operation to
each shard and returns the results, which includes the `lockCount` for each.

**Note:**

If the `lockCount` field is greater than zero, all writes
are blocked on the server and cluster. To reduce the lock
count, use the `fsyncUnlock` command.

### Fsync Locks after Failures

Fsync locks execute on the primary in a replica set or sharded cluster.

If the primary goes down or becomes unreachable due to network issues, the
cluster elects a new primary from the available
secondaries. If a primary with an fsync lock goes down, the new primary does
**not** retain the fsync lock and can handle write operations. When elections
occur during backup operations, the resulting backup may be inconsistent or
unusable.

To recover from the primary going down:

#. Run the `fsyncUnlock` command until the lock count reaches zero
   to release the lock on all nodes.

#. Issue the `fsync` command to reestablish the fsync lock on the
   cluster.

#. Restart the backup.

Additionally, fsync locks are persistent. When the old primary comes online
again, you need to use the `fsyncUnlock` command to release the lock
on the node.

## Examples

### Fsync Lock

**Note:**

`fsync` command with the `lock` option ensures that the data files are safe to copy
using low-level backup utilities such as `cp`, `scp`, or
`tar`. A `mongod` started using the copied
files contains user-written data that is indistinguishable from the 
user-written data on the locked `mongod`.

The data files of a locked `mongod` may change due to
operations such as journaling syncs or
WiredTiger snapshots.  While
this has no effect on the logical data (e.g. data accessed by
clients), some backup utilities may detect these changes and emit
warnings or fail with errors. For more information on MongoDB-
recommended backup utilities and procedures, see
/core/backups/.

The `fsync` command can lock an individual `mongod` instance or a
sharded cluster through `mongos`. When run with the `lock` field
set to `true`, the fsync operation flushes all data to the storage layer and
blocks all additional write operations until you unlock the instance or
cluster.

To lock the database, use the `fsync` command to set the `lock` field
to `true`:

```javascript
db.adminCommand( { fsync: 1, lock: true } )
```

The operation returns a document that includes the status of the
operation and the `lockCount`:

```javascript
{
   "info" : "now locked against writes, use db.fsyncUnlock() to unlock",
   "lockCount" : Long(1),
   "seeAlso" : "http://dochub.mongodb.org/core/fsynccommand",
   "ok" : 1
}
```

When locked, write operations are blocked. Separate connections may continue
read operations until the first attempt at a write operation, then they also
wait until the sever or cluster is unlocked.

**Important:**

The fsync lock operation maintains a lock count.

To unlock a server or cluster for writes, the lock count
must be zero. That is, for the given number of times you perform an fsync
lock, you must issue a corresponding number of unlock operations to unlock
the server or cluster for writes.

### Fsync Unlock

To unlock a server of cluster, use the `fsyncUnlock` command:

```javascript
db.adminCommand( { fsyncUnlock: 1 } )
```

Repeat this command as many times as needed to reduce the lock count to zero.
Once the lock count reaches zero, the server or cluster can resume writes.

### Check Lock Status

To check the state of the fsync lock, use `db.currentOp()`. Use
the following JavaScript function in the shell to test if the server or
cluster is currently locked:

```javascript
serverIsLocked = function () {
                     var co = db.currentOp();
                     if (co && co.fsyncLock) {
                         return true;
                     }
                     return false;
                 }
```

After loading this function into your `mongosh` session,
call it with the following syntax:

```javascript
serverIsLocked()
```

This function will return `true` if the server or cluster is
currently locked and `false` if the server or cluster is not locked.
