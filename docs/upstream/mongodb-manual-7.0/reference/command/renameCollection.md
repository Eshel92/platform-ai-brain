<!-- Converted from reference/command/renameCollection.txt (reStructuredText). Includes are inlined. -->

# renameCollection (database command)

## Definition

**`renameCollection`**

Changes the name of an existing collection. Specify collection names
to `renameCollection` in the form of a complete
namespace (`<database>.<collection>`).

**Tip:**

In `mongosh`, this command can also be run through the `renameCollection` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

Issue the `renameCollection` command against the
admin database.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

The command has the following syntax:

```javascript
db.runCommand(
   { 
     renameCollection: "<source_namespace>",
     to: "<target_namespace>",
     dropTarget: <true|false>,
     writeConcern: <document>,
     comment: <any> 
   }
)
```

## Command Fields

The command contains the following fields:

| Field | Type | Description |
|---|---|---|
| `renameCollection` | string | The namespace of the collection to rename. The namespace is a combination of the database name and the name of the collection. |
| `to` | string | The new namespace of the collection. If the new namespace specifies a different database, the `renameCollection` command copies the collection to the new database and drops the source collection. See restrictions-on-db-names. On MongoDB Atlas deployments, the `atlasAdmin` role grants only the `renameCollectionSameDB` privilege action, so you cannot rename a collection to a different database. |
| `dropTarget` | boolean | Optional. If `true`, `mongod` will drop the `target` of `renameCollection` prior to renaming the collection. The default value is `false`. |
| `writeConcern` | document | Optional. A document that expresses the write concern for the operation. Omit to use the default write concern. When issued on a sharded cluster, `mongos` converts the write concern of the `renameCollection` command and its helper `db.collection.renameCollection()` to `"majority"`. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Behavior

### Sharded Collections

Starting in MongoDB 5.0, you can use the `renameCollection` 
command to change the name of a sharded collection. The target 
database must be the same as the source database.

### Unsharded Collections

You can use `renameCollection` to rename an unsharded 
collection in a sharded cluster as long as the source and target 
databases are on the same primary shard. 

### Time Series Collections

You **cannot** use `renameCollection` to rename a time series 
collection. For more information, see Time Series Collection Limitations. 

### Existing Target Collection

`renameCollection` fails if `target` is the name of an existing
collection *and* you do not specify `dropTarget: true`.

### In-Progress Index Builds

The rename operation fails with a
`BackgroundOperationInProgressForNamespace` error if an index build
is in progress on the source collection. The operation also fails if
an index build is in progress on the target collection and you specify
`dropTarget: true`.

To rename the collection, wait for the index build to finish and then
retry the operation. To check for in-progress index builds, use the
`db.currentOp()` method.

### Performance

**Changed in version:** 3.6

`renameCollection` has different performance implications depending
on the target namespace.

If the target database is the same as the source database,
`renameCollection` simply changes the namespace. This is a
quick operation.

If the target database differs from the source database,
`renameCollection` copies all documents from the source
collection to the target collection. Depending on the size of the
collection, this may take longer to complete.

### Resource Locking in Sharded Clusters

**Changed in version:** 5.0

When renaming a sharded or unsharded collection in a sharded cluster,
the source and target collections are exclusively locked on every shard.
Subsequent operations on the source and target collections must wait
until the rename operation completes.

For more information on locking in MongoDB, see /faq/concurrency.

### Resource Locking in Replica Sets

If renaming a collection within the same database, 
`renameCollection` obtains an exclusive lock on 
the source and target collections for the duration of the operation. 
All subsequent operations on the collections must wait until
`renameCollection` completes. 

If renaming a collection between different databases, 
`renameCollection` obtains an exclusive (W) lock on the target 
database, an intent shared (r) lock on the source database, and a shared (S) 
lock on the source collection. Subsequent operations on the target database
must wait until `renameCollection` releases the exclusive database 
lock.

For more information on locking in MongoDB, see /faq/concurrency.

### `local` Database

- You cannot rename a collection from a replicated database to the
  `local` database, which is not replicated.

- You cannot rename a collection from the `local` database, which is
  not replicated, to a replicated database.

### Open Cursors

**Warning:**

The `db.collection.renameCollection()` method and
`renameCollection` command will invalidate open cursors
which interrupts queries that are currently returning data.

### Change Streams

For /changeStreams, the
`db.collection.renameCollection()` method and
`renameCollection` command create an
change-event-invalidate for any existing /changeStreams
opened on the source or target collection.

### Interaction with `mongodump`

A `mongodump` started with 
`--oplog` fails if a client issues the
`renameCollection` command during the 
dump process. See `mongodump.--oplog` for more information.

## Example

The following example renames a collection named `orders` in the
`test` database to `orders2014` in the `test` database.

```javascript
db.adminCommand( { renameCollection: "test.orders", to: "test.orders2014" } )
```

`mongosh` provides the
`db.collection.renameCollection()` helper for the command to
rename collections within the *same* database. The following is
equivalent to the previous example:

```javascript
use test
db.orders.renameCollection( "orders2014" )
```
