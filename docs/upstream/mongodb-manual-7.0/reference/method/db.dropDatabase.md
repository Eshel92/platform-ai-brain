<!-- Converted from reference/method/db.dropDatabase.txt (reStructuredText). Includes are inlined. -->

# db.dropDatabase() (mongosh method)

## Definition

**`db.dropDatabase(<writeConcern>)`**

Removes the current database, deleting the associated data files.

## Compatibility

This method is available in deployments hosted in the following environments: 

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

## Syntax

`db.dropDatabase()` takes an optional parameter:

* - Field
  - Description

* - writeConcern

  - Optional. A document expressing the write concern to use if greater than
    `"majority"`.

    ```javascript
    { w: <value>, j: <boolean>, wtimeout: <number> }
    ```

    Omit to use the default/minimum write concern of
    `"majority"`.

    When issued on a replica set, if the specified write concern
    results in fewer member acknowledgments than write concern
    `"majority"`, the operation uses
    `"majority"`. Otherwise, the specified write
    concern is used.

    When issued on a sharded cluster, MongoDB converts the specified
    write concern to
    `"majority"`.

    See also Behavior.

## Behavior

`dropDatabase()` wraps the `dropDatabase` command.

### Locks

The operation takes an exclusive (X)
database lock only.

### User Management

This command does not delete the
users associated with the current
database. To drop the associated users, run the
`dropAllUsersFromDatabase` command in the database you are
deleting.

### Indexes

The `db.dropDatabase()` method and `dropDatabase` command 
abort any in-progress index builds on collections in the target database 
before dropping the database. Aborting an index build has the same effect as 
dropping the built index. 

For replica sets or shard replica sets, aborting an index on the primary
does not simultaneously abort secondary index builds. MongoDB attempts
to abort the in-progress builds for the specified indexes on the
primary and if successful creates an associated `abort`
oplog entry. Secondary members with
replicated in-progress builds wait for a commit or abort oplog entry
from the primary before either committing or aborting the index build.

### Replica Set and Sharded Clusters

Replica Sets
   At minimum, `dropDatabase()` waits until all collection drops in
   the database have propagated to a majority of the replica set
   members, using write concern `"majority"`.

   You can specify a write concern to the method. If you specify a write concern 
   that requires acknowledgment from fewer than the majority, the method uses 
   write concern `"majority"`.

   If you specify a write concern that requires acknowledgment from
   more than the majority, the method uses the specified write concern.

Sharded Clusters

   When issued on a sharded cluster, MongoDB converts the specified
   write concern to
   `"majority"`.

   If you intend to create a new database with the same name as the dropped
   database, you must run the `dropDatabase` command on a 
   `mongos`.

   This ensures that all cluster nodes refresh their metadata cache,
   which includes the location of the primary shard
   for the new database. Otherwise, you may miss data on reads, and may not
   write data to the correct shard. To recover, you must manually
   intervene.

   Starting in MongoDB 5.0, the `dropDatabase` command and
   the `db.dropDatabase()` method return an error if you try to
   drop the admin database or the config database from a
   `mongos`.

   **Warning:**

   Dropping the admin database or the config database
   can leave your cluster in an unusable state.

### Change Streams

The `db.dropDatabase()` method and `dropDatabase`
command create an change-event-invalidate for any
/changeStreams opened on the dropped database or its
collections.

## Example

The following example in `mongosh` uses the ``use
<database>` operation to switch the current database to the `temp``
database and then uses `dropDatabase()` to drop the `temp`
database:

```javascript
use temp
db.dropDatabase()
```

**See also:**

`dropDatabase`
