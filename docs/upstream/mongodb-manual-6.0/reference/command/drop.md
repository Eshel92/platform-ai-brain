<!-- Converted from reference/command/drop.txt (reStructuredText). Includes are inlined. -->

# drop

## Definition

**`drop`**

The `drop` command removes an entire collection from a
database. 

**Tip:**

In `mongosh`, this command can also be run through the `drop` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

                

## Syntax

The command has following syntax:

```javascript
db.runCommand(
   { 
     drop: <collection_name>, 
     writeConcern: <document>, 
     comment: <any> 
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Description |
|---|---|
| `drop` | The name of the collection to drop. |
| `writeConcern` | Optional. A document expressing the write concern of the `drop` command. Omit to use the default write concern. When issued on a sharded cluster, `mongos` converts the write concern of the `drop` command and its helper `db.collection.drop()` to `"majority"`. |
| `comment` | .. include:: /includes/extracts/comment-content.rst |

`mongosh` provides the equivalent helper method
`db.collection.drop()`.

## Behavior

- Starting in MongoDB 5.0, the `drop` command and the
  `db.collection.drop()` method will raise an error if passed an
  unrecognized parameter.

- This command also removes any indexes associated with the dropped
  collection.

- .. include:: /includes/extracts/4.4-changes-drop-in-progress-indexes.rst

- The `drop` command and its helper
  `db.collection.drop()` create an change-event-invalidate
  for any /changeStreams opened on the dropped collection.

- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

- .. include:: /includes/extracts/5.0-changes-drop-sharding.rst

### Resource Locking

`drop` obtains an exclusive lock on the specified collection
for the duration of the operation. All subsequent operations on the
collection must wait until `drop` releases the
lock.
