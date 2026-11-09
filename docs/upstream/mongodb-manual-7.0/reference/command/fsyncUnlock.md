<!-- Converted from reference/command/fsyncUnlock.txt (reStructuredText). Includes are inlined. -->

# fsyncUnlock (database command)

## Definition

**`fsyncUnlock`**

Reduces the lock count on the server or cluster. To enable write operations,
the lock count must be zero.

   `fsyncUnlock` commands

Starting in MongoDB 7.0.2 (also available starting in
6.0.11, and 5.0.22) the `fsync` and can run on
`mongos` to lock and unlock a sharded cluster.

Use this command to unblock writes after you finish a backup operation.

**Important:**

Servers maintain an fsync lock count.  The `fsync` command with
the `lock` field set to `true` increments the lock count while the
`fsyncUnlock` command decrements it. To enable writes on a locked
server or cluster, call the `fsyncUnlock` command until the lock
count reaches zero.

`fsyncUnlock` is an administrative operation. Typically
you will use `fsyncUnlock` following a database
backup operation.

**Tip:**

In `mongosh`, this command can also be run through the `db.fsyncUnlock` helper method.

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
     fsyncUnlock: 1,
     comment: <any>
   }
)
```

The `comment` field is optional and may contain a comment of any data
type.

## Results

The operation returns a document with the following fields:

| Field | Description |
|---|---|
| `info` | Information on the status of the operation |
| `lockCount` | The number of locks remaining on the instance after the operation. |
| `ok` | The status code. |

## Examples

Consider a situation where `db.fsyncLock()` has been issued two
times. The following `fsyncUnlock` operation reduces the
locks taken by `db.fsyncLock()` by 1:

```javascript
db.adminCommand( { fsyncUnlock: 1 } )
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(1), "ok" : 1 }
```

As the `lockCount` is greater than 0, the `mongod` instance
is locked against writes. To unlock the instance for writes, run the
unlock operation again:

```javascript
db.adminCommand( { fsyncUnlock: 1 } )
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(0), "ok" : 1 }
```

The `mongod` instance is unlocked for writes.
