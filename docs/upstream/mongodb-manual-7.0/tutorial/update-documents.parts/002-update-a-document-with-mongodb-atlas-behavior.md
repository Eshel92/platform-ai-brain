<!-- Part 2 of 2 of tutorial/update-documents.md (split because the page is big). -->

## Update a Document with MongoDB Atlas

**Note:**

You can update only one document at a time in the MongoDB Atlas UI.
To update multiple documents or replace an entire document, 
connect to your Atlas deployment from `mongosh` 
or a MongoDB driver and follow the examples on this page 
for your preferred method.

The example in this section uses the sample supplies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To update a document in MongoDB Atlas, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection.**

a. For the cluster that contains the sample data, click Browse Collections.
#. In the left navigation pane, select the `sample_supplies` database.
#. Select the `sales` collection.

**Step 3: Specify a query filter document.**

You can specify a query filter document
in the Filter field. A query filter document uses 
query operators to specify search conditions.

Copy the following query filter document into the 
Filter search bar and click Apply:

```javascript
{ saleDate: { $gte: { $date: "2016-01-01T00:00-00:00" }, $lte: { $date: "2016-01-02T00:00-00:00" } } }
```

This query filter returns all documents in the `sample_supplies.sales` 
collection where `saleDate` is on or between January 1 and 2, 2016 
UTC time.

**Step 4: Edit a document.**

To edit a document displayed in the query results, hover over the
document and click on the pencil icon. In the document editor, you can:

- Add a new field. 
- Delete an existing field.
- Edit a field's name, value, or type.
- Revert a specific change.

For detailed instructions, see Create, View, Update, and Delete Documents.

**Step 5: Save your changes.**

To confirm and save your changes, click the Update button.


## Behavior

### Atomicity

All write operations in MongoDB are atomic on the level of a single
document. For more information on MongoDB and atomicity, see
/core/write-operations-atomicity.

### `_id` Field

Once set, you cannot update the value of the `_id` field nor can you
replace an existing document with a replacement document that has a
different `_id` field value.

### Idempotent Operations

Use the `updateMany()` method only for idempotent operations.

### Field Order

For write operations, MongoDB preserves the order of the document fields
*except* for the following cases:

- The `_id` field is always the first field in the document.

- Updates that include `renaming` of field names may
  result in the reordering of fields in the document.

### Upsert Option

**compass:**

The upsert option is not available through MongoDB Compass.

**shell:**

If `updateOne()`,
`updateMany()`, or
`replaceOne()` includes `upsert : true`
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**c:**

If [mongoc_collection_update_one](https://mongoc.org/libmongoc/current/mongoc_collection_update_one.html),
[mongoc_collection_update_many](https://mongoc.org/libmongoc/current/mongoc_collection_update_many.html), or
[mongoc_collection_replace_one](https://mongoc.org/libmongoc/current/mongoc_collection_replace_one.html) includes
`upsert : true` **and** no documents match the specified
filter, then the operation creates a new document and inserts
it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual reference
pages for the functions.

**python:**

If `update_one`,
`update_many`, or
`replace_one` includes
`upsert : true` **and** no documents match the specified
filter, then the operation creates a new document and inserts
it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual reference
pages for the methods.

**motor:**

If
`update_one`,
`update_many`,
or
`replace_one`
includes `upsert : true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**java-sync:**

If the update and replace methods include the
com.mongodb.client.model.UpdateOptions_ parameter that
specifies com.mongodb.client.model.UpdateOptions.upsert(true)
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces
the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**java-async:**

If the update and replace methods include the [UpdateOptions](https://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/UpdateOptions.html)
parameter that specifies [UpdateOptions.upsert(true)](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/com/mongodb/client/model/UpdateOptions.html?_ga=2.189375400.2069485991.1506612687-1453986945.1494866912&_gac=1.246606128.1506106401.EAIaIQobChMI3tmcxbu51gIVUrnACh12qwkREAAYASABEgLH4PD_BwE#upsert-boolean-)
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**kotlin-coroutine:**

If the update and replace methods include the
[com.mongodb.client.model.UpdateOptions](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-core/com/mongodb/client/model/UpdateOptions.html)
parameter that specifies `upsert(true)`,
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces
the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**nodejs:**

If `updateOne()`,
`updateMany()`, or
`replaceOne()` include
`upsert : true` in the `options` parameter document **and**
no documents match the specified filter, then the operation
creates a new document and inserts it. If there are matching
documents, then the operation modifies or replaces the matching
document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**php:**

If `updateOne()`,
`updateMany()`, or
`replaceOne()` includes ``upsert =>
true`` **and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**ruby:**

If
`update_one()`,
`update_many()`,
or
`replace_one()`
includes `upsert => true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**scala:**

If
`updateOne()`,
`updateMany()`,
or
`replaceOne()`
includes `upsert => true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**csharp:**

If `UpdateOne()`,
`UpdateMany()`, or
`ReplaceOne()` includes an
`UpdateOptions`
argument instance with the `IsUpsert` option set to `true`
**and** no documents match the specified filter, then the
operation creates a new document and inserts it. If there are
matching documents, then the operation modifies or replaces the
matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

**go:**

If `Collection.UpdateOne`
includes the `Upsert option set to true` **and** no documents match the
specified filter, then the operation creates a new document and
inserts it. If there are matching documents, then the operation
modifies or replaces the matching document or documents.

For details on the new document created, see the individual
reference pages for the methods.

### Write Acknowledgement

With write concerns, you can specify the level of acknowledgment
requested from MongoDB for write operations. For details, see
/reference/write-concern.

**shell:**

**See also:**

- /tutorial/update-documents-with-aggregation-pipeline

- `db.collection.updateOne()`

- `db.collection.updateMany()`

- `db.collection.replaceOne()`

- additional-updates

**compass:**

**See also:**

- `Compass Documents`

- Compass Query Bar

**c:**

**See also:**

- [mongoc_collection_update_one](https://mongoc.org/libmongoc/current/mongoc_collection_update_one.html)

- [mongoc_collection_update_many](https://mongoc.org/libmongoc/current/mongoc_collection_update_many.html)

- [mongoc_collection_replace_one](https://mongoc.org/libmongoc/current/mongoc_collection_replace_one.html)

- additional-updates

**python:**

**See also:**

- `pymongo.collection.Collection.update_one`

- `pymongo.collection.Collection.update_many`

- `pymongo.collection.Collection.replace_one`

- additional-updates

**motor:**

**See also:**

- `motor.motor_asyncio.AsyncIOMotorCollection.update_one`

- `motor.motor_asyncio.AsyncIOMotorCollection.update_many`

- `motor.motor_asyncio.AsyncIOMotorCollection.replace_one`

- additional-updates

**java-sync:**

**See also:**

- com.mongodb.client.MongoCollection.updateOne_

- com.mongodb.client.MongoCollection.updateMany_

- com.mongodb.client.MongoCollection.replaceOne_

- Additional Java Synchronous Driver Write Examples

**java-async:**

**See also:**

- [com.mongodb.reactivestreams.client.MongoCollection.updateOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateOne(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.updateMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#updateMany(org.bson.conversions.Bson,%20org.bson.conversions.Bson))

- [com.mongodb.reactivestreams.client.MongoCollection.replaceOne](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#replaceOne(org.bson.conversions.Bson,%20TDocument))

- [Java Reactive Streams Driver Quick Tour](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/getting-started/quick-tour/)

**kotlin-coroutine:**

**See also:**

- [MongoCollection.updateOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/update-one.html)
- [MongoCollection.updateMany()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/update-many.html)
- [MongoCollection.replaceOne()](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/replace-one.html)

- `Kotlin Coroutine Driver Modify Documents Guide`

**nodejs:**

**See also:**

- `Collection.updateOne()`

- `Collection.updateMany()`

- `Collection.replaceOne()`

- additional-updates

**php:**

**See also:**

- `MongoDBCollection::updateOne()`

- `MongoDBCollection::updateMany()`

- `MongoDBCollection::replaceOne()`

- additional-updates

**ruby:**

**See also:**

- `Mongo::Collection#update_one()`

- `Mongo::Collection#update_many()`

- `Mongo::Collection#replace_one()`

**scala:**

**See also:**

- `collection.updateOne()`

- `collection.updateMany()`

- `collection.replaceOne()`

- additional-updates

**csharp:**

**See also:**

- `IMongoCollection.UpdateOne()`

- `IMongoCollection.UpdateMany()`

- `IMongoCollection.ReplaceOne()`

- additional-updates

**go:**

**See also:**

- `Collection.UpdateOne`

- `Collection.UpdateMany`

- `Collection.ReplaceOne`

- additional-updates
