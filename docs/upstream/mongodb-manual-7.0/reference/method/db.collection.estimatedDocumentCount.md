<!-- Converted from reference/method/db.collection.estimatedDocumentCount.txt (reStructuredText). Includes are inlined. -->

# db.collection.estimatedDocumentCount() (mongosh method)

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/usage-examples/count/`**

**`https://mongodb.github.io/mongo-java-driver/5.2/apidocs/mongodb-driver-reactivestreams/com/mongodb/reactivestreams/client/MongoCollection.html#estimatedDocumentCount()`**

**`https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/crud/read-operations/count/#estimated-count`**

**`https://mongoc.org/libmongoc/current/mongoc_collection_estimated_document_count.html`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/upcoming/read/count/#retrieve-an-estimated-count`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/read/count/#retrieve-an-estimated-count`**

**`https://www.mongodb.com/docs/drivers/node/current/crud/query/count/`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/crud/read-operations/count/#estimated-count`**

**`https://www.mongodb.com/docs/php-library/current/read/count/#retrieve-an-estimated-count`**

**`https://mongodb.github.io/mongo-java-driver/5.2/apidocs/mongo-scala-driver/org/mongodb/scala/MongoCollection.html#estimatedDocumentCount():org.mongodb.scala.SingleObservable[Long]`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/usage-examples/count/`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/read/count/#retrieve-an-estimated-count`**

**`https://www.mongodb.com/docs/mongoid/current/reference/queries/#additional-query-methods`**

**`https://www.mongodb.com/docs/drivers/rust/current/usage-examples/count/`**

## Definition

**`db.collection.estimatedDocumentCount(options)`**

   `collStats` command

Returns the count of all documents in a collection or view. 

```javascript
db.collection.estimatedDocumentCount( <options> )
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | document | Optional. Extra options that affect the count behavior. |

## Fields

The `options` document can contain the following:

| Field | Type | Description |
|---|---|---|
| `maxTimeMS` | integer | Optional. The maximum amount of time to allow the count to run. |

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

## Behavior

### Mechanics

`db.collection.estimatedDocumentCount()` does not take a query
filter and instead uses metadata to return the count for a collection.

For a view:

- There is no metadata.

- The document count is calculated by executing the aggregation
  pipeline in the view definition.

- There is no fast estimated document count.

### Sharded Clusters

On a sharded cluster, the resulting count will not correctly filter out
orphaned documents.

### Unclean Shutdown

This section only applies to collections.

After an unclean shutdown, the count may be incorrect.

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count statistics reported by
`db.collection.estimatedDocumentCount()` may be inaccurate.

The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, `mongod` instances running
with non-default `--syncdelay` settings may have more or less frequent
checkpoints.

Run `validate` on each collection on the `mongod`
to restore statistics after an unclean shutdown.

After an unclean shutdown:

- `validate` updates the count statistic in the `collStats` output with the latest value.

- Other statistics like the number of documents inserted or removed in
  the `collStats` output are
  estimates.

### Client Disconnection

If the client that issued `db.collection.estimatedDocumentCount()` disconnects before the operation 
completes, MongoDB marks `db.collection.estimatedDocumentCount()` for termination using 
`killOp`.

### Count and Transactions

When you use `db.collection.estimatedDocumentCount()` in a transaction, the resulting count will 
not filter out any uncommitted multi-document transactions.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses
`db.collection.estimatedDocumentCount` to retrieve the count of
all documents in the `movies` collection:

```javascript
```

Output:

```javascript
```

**See also:**

- `db.collection.countDocuments()`
- `count`
- collStats pipeline stage with the count
  option
