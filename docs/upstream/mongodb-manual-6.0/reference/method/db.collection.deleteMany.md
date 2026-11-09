<!-- Converted from reference/method/db.collection.deleteMany.txt (reStructuredText). Includes are inlined. -->

# db.collection.deleteMany()

## Definition

**`db.collection.deleteMany()`**

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/usage-examples/deleteMany/`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/write/write-delete-documents/#delete-multiple-documents`**

**`https://www.mongodb.com/docs/drivers/csharp/current/usage-examples/deleteMany/`**

**`https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/tutorial/#deleting-a-document`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/upcoming/write/delete/#delete-operations`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/write/delete/#delete-multiple-documents`**

**`https://www.mongodb.com/docs/drivers/node/current/usage-examples/deleteMany/`**

**`https://www.mongodb.com/docs/drivers/go/current/usage-examples/deleteMany/`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-deleteMany/`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/write/delete/#delete-multiple-documents`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/crud/write-operations/delete/#delete-documents`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/write/delete/`**

**`https://www.mongodb.com/docs/mongoid/current/reference/crud/`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/crud/write-operations/delete/`**

Removes all documents that match the `filter` from a collection.

:returns:

  A document containing:

  - A boolean `acknowledged` as `true` if the operation ran with 
    write concern or `false` if write concern was disabled

  - `deletedCount` containing the number of deleted documents

**Note:**

If you are deleting all documents in a large collection, it may be faster 
to drop the collection and recreate it. Before dropping the collection, 
note all indexes on the collection. You must recreate any 
indexes that existed in the original 
collection. If the original collection was sharded, you must also 
shard the recreated collection.

For more information on dropping a collection, see 
`db.collection.drop()`.

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

The `deleteMany()` method has the following
syntax:

```javascript
db.collection.deleteMany(
   <filter>,
   {
      writeConcern: <document>,
      collation: <document>
   }
)
```

* - Parameter

  - Type

  - Description

* - filter

  - document

  - .. _deleteMany-filter:

    Specifies deletion criteria using query operators. 

    To delete all documents in a collection, pass in an empty
    document (`{ }`).

* - writeConcern

  - document

  - .. _deleteMany-wc:

    Optional. A document expressing the write concern. Omit to use the default write concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - collation

  - document

  - .. _deleteMany-collation:

    Optional. 

    Specifies the collation  to use for the operation.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    The collation option has the following syntax:

    ```none
    collation: {
       locale: <string>,
       caseLevel: <boolean>,
       caseFirst: <string>,
       strength: <int>,
       numericOrdering: <boolean>,
       alternate: <string>,
       maxVariable: <string>,
       backwards: <boolean>
    }
    ```

    When specifying collation, the `locale` field is mandatory; all
    other collation fields are optional. For descriptions of the fields,
    see collation-document-fields.

    If the collation is unspecified but the collection has a
    default collation (see `db.createCollection()`), the
    operation uses the collation specified for the collection.

    If no collation is specified for the collection or for the
    operations, MongoDB uses the simple binary comparison used in prior
    versions for string comparisons.

    You cannot specify multiple collations for an operation. For
    example, you cannot specify different collations per field, or if
    performing a find with a sort, you cannot use one collation for the
    find and another for the sort.

* - hint

  - document

  - .. _deleteMany-hint:

    Optional. A document or string that specifies the index 
    to use to support the query predicate.

    The option can take an index specification document or the
    index name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-deleteMany-hint.

## Behavior

### Sharded Collections

- If `deleteMany()` is run outside a transaction, operations that target more 
  than one shard broadcast the operation to all shards in the cluster. 

- If `deleteMany()` is run inside a transaction, operations that target more
  than one shard only target the relevant shards.

### Time Series Collections

`db.collection.deleteMany()` throws a `WriteError` exception
if used on a time series collection. To remove all documents
from a time series collection, use `db.collection.drop()`.

### Delete a Single Document

To delete a single document, use `db.collection.deleteOne()` instead. 

Alternatively, use a field that is a part of a unique index such as 
`_id`. 

### Transactions

`db.collection.deleteMany()` can be used inside distributed transactions.

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

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
/core/transactions-production-consideration.

### Primary Node Failure

`db.collection.deleteMany()` deletes documents one at a time. 
If the primary node fails during a `db.collection.deleteMany()`
operation, documents that were not yet deleted from secondary nodes are
not deleted from the collection.

### Oplog Entries

If a `db.collection.deleteMany()` operation successfully deletes one
or more documents, the operation adds an entry for each deleted document
on the oplog (operations log). If the operation fails or does
not find any documents to delete, the operation does not add an entry on
the oplog. 

## Examples

### Delete Multiple Documents

The `orders` collection has documents with the following structure:

```javascript
db.orders.insertOne(
   {
      _id: ObjectId("563237a41a4d68582c2509da"),
      stock: "Brent Crude Futures",
      qty: 250,
      type: "buy-limit",
      limit: 48.90,
      creationts: ISODate("2015-11-01T12:30:15Z"),
      expiryts: ISODate("2015-11-01T12:35:15Z"),
      client: "Crude Traders Inc."
   }
)
```

   
The following operation deletes all documents where ``client : "Crude Traders 
Inc."``:

```javascript
try {
   db.orders.deleteMany( { "client" : "Crude Traders Inc." } );
} catch (e) {
   print (e);
}
```

   
The operation returns:

```javascript
{ "acknowledged" : true, "deletedCount" : 10 }
```

   
The following operation deletes all documents where ``stock : "Brent Crude 
Futures"` and `limit` is greater than `48.88``:

```javascript
try {
   db.orders.deleteMany( { "stock" : "Brent Crude Futures", "limit" : { $gt : 48.88 } } );
} catch (e) {
   print (e);
}
```

The operation returns:

```javascript
{ "acknowledged" : true, "deletedCount" : 8 }
```

### deleteMany() with Write Concern

Given a three member replica set, the following operation specifies a 
`w` of `majority` and `wtimeout` of `100`:

```javascript
try {
   db.orders.deleteMany(
       { "client" : "Crude Traders Inc." },
       { writeConcern: { w : "majority", wtimeout : 100 }}
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

**See also:**

`WriteResult.writeConcernError`

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `restaurants` has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
] )
```

The following operation includes the collation
option:

```javascript
db.restaurants.deleteMany( 
   { category: "cafe", status: "A" }, 
   { collation: { locale: "fr", strength: 1 } }
)
```

### Specify `hint` for Delete Operations

In `mongosh`, create a `members` collection
with the following documents:

```javascript
db.members.insertMany([
   { "_id" : 1, "member" : "abc123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 2, "member" : "xyz123", "status" : "A", "points" : 60,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" },
   { "_id" : 3, "member" : "lmn123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 4, "member" : "pqr123", "status" : "D", "points" : 20,  "misc1" : "Deactivated", "misc2" : null },
   { "_id" : 5, "member" : "ijk123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 6, "member" : "cde123", "status" : "A", "points" : 86,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" }
])
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following delete operation explicitly hints to use the index
`{ status: 1 }`:

```javascript
db.members.deleteMany(
   { "points": { $lte: 20 }, "status": "P" }, 
   { hint: { status: 1 } }
)
```

**Note:**

If you specify an index that does not exist, the operation errors.

The delete command returns the following:

```javascript
{ "acknowledged" : true, "deletedCount" : 3 }
```

To view the indexes used, you can use the `$indexStats` pipeline:

```javascript
db.members.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } } ] )
```

The `accesses.ops` field in the `$indexStats` output
indicates the number of operations that used the index.
