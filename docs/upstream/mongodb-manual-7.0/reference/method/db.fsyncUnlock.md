<!-- Converted from reference/method/db.fsyncUnlock.txt (reStructuredText). Includes are inlined. -->

# db.fsyncUnlock() (mongosh method)

## Definition

**`db.fsyncUnlock()`**

Reduces the lock count on the server to renable write operations.

   `db.fsyncUnlock()` methods

Starting in MongoDB 7.0.2 (also available starting in
6.0.11, and 5.0.22) the `db.fsyncLock` and can run on
`mongos` to lock and unlock a sharded cluster.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `fsyncUnlock` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Servers maintain an fsync lock count.  The `fsyncLock` method
increments the lock count while the `fsyncUnlock` method decrements
it. To unlock writes on a server or cluster, call the `fsyncUnlock`
method until the lock count reaches zero.

`db.fsyncUnlock()` is an administrative operation. Use this method
to unlock a server or cluster after a backup operation

`db.fsyncUnlock()`  has the syntax:

```javascript
db.fsyncUnlock()
```

The operation returns a document with the following fields:

|  |  |
|---|---|
| `info` | Information on the status of the operation. |
| `lockCount` | The number of locks remaining on the instance after the operation. |
| `ok` | The status code. |

The `db.fsyncUnlock()` method wraps the
`fsyncUnlock` command.

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

### Compatibility with WiredTiger

`db.fsyncLock()` ensures that the data files are safe to copy
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

## Example

Consider a situation where `db.fsyncLock()` has been issued two
times. The following `db.fsyncUnlock()` operation reduces the
locks taken by `db.fsyncLock()` by 1:

```javascript
db.fsyncUnlock()
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(1), "ok" : 1 }
```

As the `lockCount` is greater than 0, the `mongod` instance
is locked against writes. To unlock the instance for writes, run
`db.fsyncLock()` again:

```javascript
db.fsyncUnlock()
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(0), "ok" : 1 }
```

The `mongod` instance is unlocked for writes.
