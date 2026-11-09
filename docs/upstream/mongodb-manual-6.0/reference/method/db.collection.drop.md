<!-- Converted from reference/method/db.collection.drop.txt (reStructuredText). Includes are inlined. -->

# db.collection.drop()

## Definition

**`db.collection.drop(<options>)`**

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://mongodb.github.io/mongo-java-driver/5.1/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#drop()`**

**`https://mongodb.github.io/mongo-java-driver/5.1/apidocs/mongodb-driver-reactivestreams/com/mongodb/reactivestreams/client/gridfs/GridFSBucket.html#drop()`**

**`https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/database-collection/#drop-a-collection`**

**`https://mongoc.org/libmongoc/current/mongoc_collection_drop.html`**

**`https://mongocxx.org/api/mongocxx-3.0.2/classmongocxx_1_1collection.html#a2e6f9689b531a0be1e5b202177bb163d`**

**`https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.drop`**

**`https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#drop`**

**`https://www.mongodb.com/blog/post/quick-start-golang--mongodb--how-to-delete-documents`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-drop/`**

**`https://mongodb.github.io/mongo-scala-driver/2.0/scaladoc/org/mongodb/scala/SingleObservable.html`**

**`https://mongodb.github.io/mongo-java-driver/5.1/apidocs/mongodb-driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/drop.html`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/databases-collections/#drop-a-collection`**

**`https://www.rubydoc.info/gems/mongoid/2.8.1/Mongoid/Collection#drop-instance_method`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/database-collection/#drop-a-database`**

Removes a collection or view from the database.
The method also removes any indexes associated with the dropped
collection. The method provides a wrapper around the
`drop` command.

:returns:
  - `true` when successfully drops a collection.
  - `false` when collection to drop does not exist.

**Note:**

When run on a sharded cluster, `db.collection.drop()` always returns `true`.

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

## Syntax

The `drop()` method has the following form:

```javascript
db.collection.drop( { writeConcern: <document> } )
```

The `drop()` method takes an 
optional document with the following field:

| Field | Description |
|---|---|
| writeConcern | Optional. A document expressing the write concern of the `db.collection.drop()` operation. Omit to use the default write concern. When issued on a sharded cluster, `mongos` converts the write concern of the `drop` command and its helper `db.collection.drop()` to `"majority"`. |

         

## Behavior

- The `db.collection.drop()` method and `drop`
  command create an change-event-invalidate for any
  /changeStreams opened on dropped collection.

- .. include:: /includes/extracts/4.4-changes-drop-in-progress-indexes.rst

- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

- .. include:: /includes/extracts/5.0-changes-drop-sharding.rst

- Starting in MongoDB 6.0, the `db.collection.drop()` method 
  drops the specified collection and any internal collections related 
  to encrypted fields. 

  **Warning:**

  The `db.collection.drop()` method's behavior differs from
  the driver's `drop` method's behavior. The driver's connection 
  must have automatic encryption enabled in order to drop both the 
  specified collection and any internal collections related to
  encrypted fields. `mongosh` *always* drops the specified 
  collection and any internal collections related to encrypted
  fields.

### Reusing Dropped Collection Names on Sharded Clusters

On a sharded cluster, if you create a collection that has the same name 
as a previously deleted collection prior to MongoDB 5.0, 
`mongos` may forward operations to the wrong shard.
To avoid this situation use the version-specific instructions below:

For a sharded cluster running **MongoDB 5.0 or later**, 
no special action is required. Use the `drop()` method
and then create a new collection with the same name.

For a sharded cluster, if you use the `drop()` method and then create a new 
collection with the same name, you must either:

-  Flush the cached routing table on every `mongos`
   using `flushRouterConfig`.

-  Use `db.collection.remove()` to remove the existing
   documents and reuse the collection.

Flushing the cached routing tables is the preferred procedure because it
is faster than removing sharded collections with 
`db.collection.remove()`. Only use the `remove()` approach if 
you want to avoid flushing the cache.

### Resource Locking

`db.collection.drop()` obtains an exclusive lock on the specified collection
for the duration of the operation. All subsequent operations on the
collection must wait until `db.collection.drop()` releases the
lock.

## Example

### Drop a Collection Using Default Write Concern

The following operation drops the `students` collection in the
current database.

```javascript
db.students.drop()
```

### Drop a Collection Using `w: 1` Write Concern

`db.collection.drop()` accepts an options document.

The following operation drops the `students` collection in the
current database. The operation uses the
`1 <` write concern:

```javascript
db.students.drop( { writeConcern: { w: 1 } } )
```
