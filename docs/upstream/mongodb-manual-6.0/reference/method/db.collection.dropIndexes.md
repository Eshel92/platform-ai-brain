<!-- Converted from reference/method/db.collection.dropIndexes.txt (reStructuredText). Includes are inlined. -->

# db.collection.dropIndexes()

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/v5.2/fundamentals/indexes/#remove-an-index-using-a-wildcard-character`**

**`https://mongodb.github.io/mongo-java-driver/5.2/apidocs/mongodb-driver-reactivestreams/com/mongodb/reactivestreams/client/MongoCollection.html#dropIndexes()`**

**`https://mongodb.github.io/mongo-csharp-driver/2.29.0/api/MongoDB.Driver/MongoDB.Driver.IMongoIndexManager-1.DropAll.html`**

**`https://mongoc.org/libmongoc/current/mongoc_collection_drop_index.html`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/upcoming/work-with-indexes/#remove-all-indexes`**

**`https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.drop_indexes`**

**`https://mongodb.github.io/node-mongodb-native/6.9/classes/Collection.html#dropIndexes`**

**`https://pkg.go.dev/go.mongodb.org/mongo-driver@v1.17.0/mongo#IndexView.DropAll`**

**`https://www.mongodb.com/docs/php-library/current/indexes/index-mgmt/#delete-all-indexes`**

**`https://mongodb.github.io/mongo-java-driver/5.2/apidocs/mongo-scala-driver/org/mongodb/scala/MongoCollection.html#dropIndexes():org.mongodb.scala.SingleObservable[Unit]`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/indexes/#remove-an-index-using-a-wildcard-character`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/work-with-indexes/#delete-all-indexes`**

**`https://www.mongodb.com/docs/mongoid/current/reference/indexes/#index-management-rake-tasks`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/indexes/#remove-an-index`**

## Definition

**`db.collection.dropIndexes()`**

Drops the specified index or indexes (except the index on the
`_id` field and the last remaining shard key index) from a 
collection.

You can use the method to:

- Drop all but the `_id` index from a collection.

  ```javascript
  db.collection.dropIndexes()
  ```

- Drop a specified index from a collection. To specify the index,
  you can pass the method either:

  - The index specification document (unless the index is a
    text index in which case, use the
    index name to drop):

    ```javascript
    db.collection.dropIndexes( { a: 1, b: 1 } )
    ```

  - The index name:

    ```javascript
    db.collection.dropIndexes( "a_1_b_1" )
    ```

    **Tip:**

    To get the names of the indexes, use the
    `db.collection.getIndexes()` method.

- Drop specified indexes from a collection. To specify multiple indexes to 
  drop, pass the method an array of index names:

  ```javascript
  db.collection.dropIndexes( [ "a_1_b_1", "a_1", "a_1__id_-1" ] )
  ```

  If the array of index
  names includes a non-existent index, the method errors without
  dropping any of the specified indexes.

  **Tip:**

  To get the names of the indexes, use the
  `db.collection.getIndexes()` method.

The `db.collection.dropIndexes()` method takes the following
optional parameter:

| Parameter | Type | Description |
|---|---|---|
| `indexes` | string or document or array of strings | Optional. Specifies the index or indexes to drop. **To drop all but the _id index from the collection**, omit the parameter. **To drop a single index**, specify either the index name, the index specification document (unless the index is a text index), or an array of the index name. To drop a text index, specify the index name or an array of the index name instead of the index specification document. **To drop multiple indexes**, specify an array of the index names. |

   

## Behavior

Starting in MongoDB 6.0, `db.collection.dropIndexes()` raises an error if you attempt
to use it to remove the last remaining shard key compatible index. 
Passing `"*"` to `db.collection.dropIndexes()` drops all indexes except 
the `_id` index and the last remaining shard key compatible index, 
if one exists.

Starting in MongoDB 5.2, you can use `db.collection.dropIndexes()` to drop existing 
indexes on the same collection even if there is a build in progress on 
another index. In earlier versions, attempting to drop a different 
index during an in-progress index build results in a 
`BackgroundOperationInProgressForNamespace` error.    

### Kill related queries only

The `dropIndexes()` operation only kills queries that are using the index being 
dropped. This may include queries considering the index as part of   
query planning.

### Resource Locking

`db.collection.dropIndexes()` obtains an exclusive lock on the specified collection
for the duration of the operation. All subsequent operations on the
collection must wait until `db.collection.dropIndexes()` releases the
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

If an index specified to `db.collection.dropIndexes()` is still building, `db.collection.dropIndexes()` attempts 
to stop the in-progress build. Stopping an index build has the same effect as 
dropping the built index.

For replica sets, run `db.collection.dropIndexes()` on the primary. 
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
