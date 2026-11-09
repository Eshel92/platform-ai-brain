<!-- Converted from reference/command/dropIndexes.txt (reStructuredText). Includes are inlined. -->

# dropIndexes

## Definition

**`dropIndexes`**

**Changed in version:** 6.0

The `dropIndexes` command drops one or more indexes
(except the index on the `_id` field and the last remaining shard
key index, if one exists) from the specified collection.

   `db.collection.dropIndexes()` helper methods.

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.dropIndex()` and.

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

The command has the following syntax:
   

```javascript
db.runCommand(
   { 
     dropIndexes: <string>, 
     index: <string|document|arrayofstrings>, 
     writeConcern: <document>, comment: <any> 
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - dropIndexes
  - String
  - The name of the collection whose indexes to drop.

* - index
  - string or document or array of strings
  - The index or indexes to drop.

    - To drop all indexes except the `_id` index and the last 
      remaining shard key index from the collection if one 
      exists, specify `"*"`.

    - To drop a single index, specify either the index name,
      the index specification document (unless the index is a
      text index), or an array of the
      index name. To drop a text index,
      specify the index names instead of the index specification
      document. If this index is the last remaining shard key 
      index, `dropIndexes` raises an error.

    - To drop multiple indexes, specify an array of the index names.

* - writeConcern
  - document
  - Optional. A document expressing the write concern of the `drop` command.
    Omit to use the default write concern.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

## Behavior

Starting in MongoDB 6.0, `dropIndexes` raises an error if you attempt
to use it to remove the last remaining shard key compatible index. 
Passing `"*"` to `dropIndexes` drops all indexes except 
the `_id` index and the last remaining shard key compatible index, 
if one exists.

Starting in MongoDB 5.2, you can use `dropIndexes` to drop existing 
indexes on the same collection even if there is a build in progress on 
another index. In earlier versions, attempting to drop a different 
index during an in-progress index build results in a 
`BackgroundOperationInProgressForNamespace` error.    

### Kill related queries only

The `dropIndexes` operation only kills queries that are using the index being 
dropped. This may include queries considering the index as part of   
query planning.

### Resource Locking

`dropIndexes` obtains an exclusive lock on the specified collection
for the duration of the operation. All subsequent operations on the
collection must wait until `dropIndexes` releases the
lock.

### Index Names

If the method is passed an array of index names that includes a
non-existent index, the method errors without dropping any of the
specified indexes.

### `_id` Index

You cannot drop the default index on the `_id` field.

### text Indexes

To drop a text index, specify the index name
instead of the index specification document.

### Stop In-Progress Index Builds

If an index specified to `dropIndexes` is still building, `dropIndexes` attempts 
to stop the in-progress build. Stopping an index build has the same effect as 
dropping the built index.

For replica sets, run `dropIndexes` on the primary. 
The primary stops the index build and creates an associated 
"abortIndexBuild" oplog entry. Secondaries which replicate
the "abortIndexBuild" oplog entry stop the in-progress index build and
discard the build job. See index-build-process for detailed
documentation on the index build process.

Use `currentOp` to identify the index builds associated with 
a `createIndexes` or `db.collection.createIndexes()`
operation. See currentOp-cmd-index-creation for an example.

### Hidden Indexes

MongoDB offers the ability to hide or unhide indexes from the query planner. 
By hiding an index from the planner, you can evaluate the potential impact of 
dropping an index without actually dropping the index. 

If after the evaluation, the user decides to drop the index, you
can drop the hidden index; i.e. you do not need to unhide it first to
drop it.

If, however, the impact is negative, the user can unhide the index
instead of having to recreate a dropped index. And because indexes are
fully maintained while hidden, the indexes are immediately available
for use once unhidden.

For more information on hidden indexes, see /core/index-hidden.

## Examples

- To drop all non-`_id` indexes , specify `"*"` for the `index`.

  ```javascript
  db.runCommand( { dropIndexes: "collection", index: "*" } )
  ```

- To drop a single index, issue the command by specifying the name of
  the index you want to drop. For example, to drop the index named
  `age_1`, use the following command:

  ```javascript
  db.runCommand( { dropIndexes: "collection", index: "age_1" })
  ```

  `mongosh` provides the helper methods
  `db.collection.dropIndex()` and
  `db.collection.dropIndexes()`:

  ```javascript
  db.collection.dropIndex("age_1");
  ```

- To drop multiple indexes, issue the command by specifying an array of
  the index names: 

  ```javascript
  db.runCommand( { dropIndexes: "collection", index: [ "age_1", "age_1_status_1" ] } )
  ```

**See also:**

- `db.collection.dropIndexes()`
- `db.collection.dropIndex()`
