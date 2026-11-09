<!-- Converted from reference/method/db.collection.dropIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.dropIndex()

## Definition

**`db.collection.dropIndex(index)`**

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/indexes/#remove-an-index-using-an-index-specification-document`**

**`https://mongodb.github.io/mongo-java-driver/5.1/apidocs/mongodb-driver-reactivestreams/com/mongodb/reactivestreams/client/MongoCollection.html#dropIndex(org.bson.conversions.Bson)`**

**`https://www.mongodb.com/docs/drivers/csharp/upcoming/fundamentals/indexes/#drop-a-search-index`**

**`https://mongoc.org/libmongoc/current/mongoc_collection_drop_index.html`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/upcoming/work-with-indexes/#remove-an-index`**

**`https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.drop_index`**

**`https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#dropIndex`**

**`https://pkg.go.dev/github.com/GabrielHCataldo/go-mongo-template/mongo/option#DropIndex`**

**`https://www.mongodb.com/docs/php-library/current/tutorial/indexes/#drop-indexes`**

**`https://mongodb.github.io/mongo-scala-driver/2.0/scaladoc/org/mongodb/scala/MongoCollection.html#dropIndex(indexName:String):org.mongodb.scala.SingleObservable[org.mongodb.scala.Completed]`**

**`https://mongodb.github.io/mongo-scala-driver/2.0/scaladoc/org/mongodb/scala/MongoCollection.html#dropIndex(indexName:String):org.mongodb.scala.SingleObservable[org.mongodb.scala.Completed]`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/work-with-indexes/#delete-a-single-index`**

**`https://www.rubydoc.info/gems/mongoid/3.1.6/Rails%2FMongoid:remove_indexes`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/indexes/#remove-an-index`**

Drops or removes the specified index from a collection. 

**Note:**

- You cannot drop the default index on the `_id` field.

- You cannot specify `db.collection.dropIndex("*")` to drop all non-`_id` indexes. Use
  `db.collection.dropIndexes()` instead.

To get the index name or the index specification document for the
`db.collection.dropIndex()` method, use the
`db.collection.getIndexes()` method.

The `db.collection.dropIndex()` method takes the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| `index` | string or document | Optional. Specifies the index to drop. You can specify the index either by the index name or by the index specification document. To drop a text index, specify the index name. You cannot specify `"*"` to drop all non-`_id` indexes. Use `db.collection.dropIndexes()` instead. If an index specified to `db.collection.dropIndex()` is still building, `db.collection.dropIndex()` attempts to stop the in-progress build. Stopping an index build has the same effect as dropping the built index. See dropIndex-method-index-builds for more complete documentation. |

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

## Behavior

Starting in MongoDB 5.2, you can use `db.collection.dropIndex()` to drop existing 
indexes on the same collection even if there is a build in progress on 
another index. In earlier versions, attempting to drop a different 
index during an in-progress index build results in a 
`BackgroundOperationInProgressForNamespace` error.    

### Resource Locking

`db.collection.dropIndex()` obtains an exclusive lock on the specified collection
for the duration of the operation. All subsequent operations on the
collection must wait until `db.collection.dropIndex()` releases the
lock.

### Stop In-Progress Index Builds

If an index specified to `db.collection.dropIndex()` is still building, `db.collection.dropIndex()` attempts 
to stop the in-progress build. Stopping an index build has the same effect as 
dropping the built index.

For replica sets, run `db.collection.dropIndex()` on the primary. 
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

## Example

In a `pets` collection, create a descending index on the `cat` field:

```javascript
db.pets.createIndex( { cat: -1 }, { name: "catIdx" } )
```

To see the indexes in the `pets` collection, run the
`getIndexes()` method:

```javascript
db.pets.getIndexes()
```

Output:

```
[
   { v: 2, key: { _id: 1 }, name: '_id_' },
   { v: 2, key: { cat: -1 }, name: 'catIdx' }
]
```

   
The single field index on the field `cat` has the user-specified name
of `catIdx` and the index specification document of
`{ "cat" : -1 }`.

To drop the index `catIdx`, you can use either the index name:

```javascript
db.pets.dropIndex( "catIdx" )
```

Or you can use the index specification document `{ "cat" : -1 }`:

```javascript
db.pets.dropIndex( { "cat" : -1 } )
```

The `dropIndex` command returns the number of indexes in the
collection prior to the command being run, and indicates whether the
command was successful:

```javascript
{ nIndexesWas: 2, ok: 1 }
```

To confirm that the index was dropped, run the `getIndexes()` method
again:

```javascript
db.pets.getIndexes()
```

Output:

```
[ { v: 2, key: { _id: 1 }, name: '_id_' } ]
```
