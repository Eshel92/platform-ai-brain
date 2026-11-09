<!-- Converted from reference/method/db.collection.insertOne.txt (reStructuredText). Includes are inlined. -->

# db.collection.insertOne() (mongosh method)

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/crud/write-operations/insert/#insert-a-single-document`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/write/insert-documents/#insert-one-document`**

**`https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/crud/write-operations/insert/#insert-one-document`**

**`https://mongoc.org/libmongoc/current/mongoc_collection_insert_one.html`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/write/insert/#insert-one-document`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/write/insert/#insert-one-document`**

**`https://www.mongodb.com/docs/drivers/node/current/fundamentals/crud/write-operations/insert/#insert-a-single-document`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/crud/write-operations/insert/#insert-a-document-1`**

**`https://www.mongodb.com/docs/php-library/current/write/insert/#insert-one-document`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/write-ops/#insert-a-document`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/crud/write-operations/insert/#insert-a-single-document`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/write/insert/#insert-one-document`**

**`https://www.mongodb.com/docs/mongoid/current/reference/crud/#standard`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/crud/write-operations/insert/#insert-a-document`**

## Definition

**`db.collection.insertOne()`**

Inserts a single document into a collection.

:returns:

   A document containing:

   - A boolean `acknowledged` as `true` if the operation ran with
     write concern or `false` if write concern was disabled.
   - A field `insertedId` with the `_id` value of the
     inserted document.

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

`db.collection.insertOne()` has the following
form:

```javascript
db.collection.insertOne(
    <document>,
    {
      writeConcern: <document>
    }
)
```

### Parameters

`insertOne()` takes the following
parameters:

| Parameter | Type | Description |
|---|---|---|
| `document` | document | A document to insert into the collection. |
| `writeConcern` | document | Optional. A document expressing the write concern. Omit to use the default write concern. Do not explicitly set the write concern for the operation if run in a transaction. To use write concern with transactions, see transactions-write-concern. |

## Behaviors

### Collection and `_id` Field Creation

If the collection does not exist, then `insertOne()` creates the collection.

If the document to insert does not specify an _id field, then `mongod`
adds the `_id` field and assigns a unique
`ObjectId` for the document. Most
drivers create an ObjectId and insert the `_id` field, but the
`mongod` will create and populate the `_id` if the driver or
application does not.

If the document contains an `_id` field, the `_id` value must be
unique within the collection to avoid duplicate key error.

### Explainability

`insertOne()` is not compatible with
`db.collection.explain()`.

### Error Handling

On error, `insertOne()` throws either a `writeError`
or `writeConcernError` exception.

#### Schema Validation Errors

If your collection uses schema validation and has `validationAction` set to 
`error`, inserting an invalid document throws a 
`MongoServerError` and `insertOne()` fails.

### Transactions

`insertOne()` can be used inside distributed transactions.

**Important:**

In most cases, a distributed transaction incurs a greater
performance cost over single document writes, and the
availability of distributed transactions should not be a
replacement for effective schema design. For many scenarios, the
denormalized data model (embedded documents and arrays) will continue to be optimal for your
data and use cases. That is, for many scenarios, modeling your data
appropriately will minimize the need for distributed
transactions. 

For additional transactions usage considerations
(such as runtime limit and oplog size limit), see also
production-considerations.

#### Collection Creation in Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

If you specify an insert on a non-existing collection
in a transaction, MongoDB creates the collection implicitly.

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Oplog Entries

If an `insertOne()` operation successfully inserts a
document, the operation adds an entry on the oplog (operations
log). If the operation fails, the operation does not add an entry on the
oplog. 

## Examples

### Insert a Document without Specifying an `_id` Field

In the following example, the document passed to `insertOne()` does not contain the `_id`
field:

```javascript
try {
   db.products.insertOne( { item: "card", qty: 15 } );
} catch (e) {
   print (e);
};
```

The operation returns the following document:

```javascript
{
   "acknowledged" : true,
   "insertedId" : ObjectId("56fc40f9d735c28df206d078")
}
```

Because the documents did not include `_id`,
`mongod` creates and adds the `_id` field and
assigns it a unique `ObjectId` value.

The `ObjectId` values are specific to the machine and time when the
operation is run. As such, your values may differ from those in the
example.

### Insert a Document Specifying an `_id` Field

In the following example, the document passed to `insertOne()` includes the `_id` field.
The value of `_id` must be unique within the collection to avoid
duplicate key error.

```javascript
try {
   db.products.insertOne( { _id: 10, item: "box", qty: 20 } );
} catch (e) {
   print (e);
}
```

The operation returns the following:

```javascript
{ "acknowledged" : true, "insertedId" : 10 }
```

Inserting an duplicate value for any key that is part of a unique
index, such as `_id`, throws an exception. The following attempts to insert
a document with a `_id` value that already exists:

```javascript
try {
   db.products.insertOne( { _id: 10, "item" : "packing peanuts", "qty" : 200 } );
} catch (e) {
   print (e);
}
```

Since `_id: 10` already exists, the following exception is thrown:

```javascript
WriteError({
   "index" : 0,
   "code" : 11000,
   "errmsg" : "E11000 duplicate key error collection: inventory.products index: _id_ dup key: { : 10.0 }",
   "op" : {
      "_id" : 10,
      "item" : "packing peanuts",
      "qty" : 200
   }
})
```

### Increase Write Concern

Given a three member replica set, the following operation specifies a
`w` of `majority`, `wtimeout` of `100`:

```javascript
try {
   db.products.insertOne(
       { "item": "envelopes", "qty": 100, type: "Self-Sealing" },
       { writeConcern: { w : "majority", wtimeout : 100 } }
   );
} catch (e) {
   print (e);
}
```

If the acknowledgment takes longer than the `wtimeout` limit, the following
exception is thrown:

```javascript
WriteConcernError({
   "code" : 64,
   "errmsg" : "waiting for replication timed out",
   "errInfo" : {
     "wtimeout" : true,
     "writeConcern" : { 
       "w" : "majority",
       "wtimeout" : 100,
       "provenance" : "getLastErrorDefaults"
     }
   }
})
```
