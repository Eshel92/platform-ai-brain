<!-- Converted from reference/method/db.collection.deleteOne.txt (reStructuredText). Includes are inlined. -->

# db.collection.deleteOne()

## Definition

**`db.collection.deleteOne()`**

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/usage-examples/deleteOne/`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/write/write-delete-documents/#delete-one-document`**

**`https://www.mongodb.com/docs/drivers/csharp/current/usage-examples/deleteOne/`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/upcoming/write/delete/#delete-operations`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/write/delete/#delete-one-document`**

**`https://www.mongodb.com/docs/drivers/node/current/usage-examples/deleteOne/`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/crud/write-operations/delete`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-deleteOne/`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/write/delete/#delete-one-document`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/crud/write-operations/delete/#delete-documents`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/write/delete/`**

**`https://www.mongodb.com/docs/mongoid/current/reference/crud/`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/crud/write-operations/delete/`**

Removes a single document from a collection.

:returns:

   A document containing:

   - A boolean `acknowledged` as `true` if the operation ran with 
     write concern or `false` if write concern was disabled    
   - `deletedCount` containing the number of deleted documents

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

The `deleteOne()` method has the following form:

```javascript
db.collection.deleteOne(
    <filter>,
    {
      writeConcern: <document>,
      collation: <document>,
      hint: <document|string>  
    }
)
```

The `deleteOne()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - filter
  - document
  - .. _deleteOne-filter:

    Specifies deletion criteria using query operators. 

    Specify an empty document `{ }` to delete the first document returned in 
    the collection.

* - writeConcern
  - document
  - .. _deleteOne-wc:

    Optional. A document expressing the write concern. Omit to use the default write concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - collation
  - document
  - .. _deleteOne-collation:

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
  - .. _deleteOne-hint:

    Optional. A document or string that specifies the index to use to support the query predicate.

    The option can take an index specification document or the
    index name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-deleteOne-hint.

## Behavior

### Deletion Order

`db.collection.deleteOne` deletes the first document that matches 
the filter. Use a field that is part of a unique index such as `_id` 
for precise deletions.

### Time Series Collections

`db.collection.deleteOne()` returns a `WriteError` exception
if used on a time series collection.

### Sharded Collections

To use `db.collection.deleteOne` on a sharded collection:

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the shard key or the `_id` field in the query
  specification.

### Transactions

`db.collection.deleteOne()` can be used inside distributed transactions.

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

### Oplog Entries

If a `db.collection.deleteOne()` operation successfully deletes a
document, the operation adds an entry on the oplog (operations
log). If the operation fails or does not find a document to delete, the
operation does not add an entry on the oplog. 

## Examples

### Delete a Single Document

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

   
The following operation deletes the order with ``_id: 
ObjectId("563237a41a4d68582c2509da")`` : 

```javascript
try {
   db.orders.deleteOne( { _id: ObjectId("563237a41a4d68582c2509da") } );
} catch (e) {
   print(e);
}
```

   
The operation returns:

```javascript
{ acknowledged: true, deletedCount: 1 }
```

   
The following operation deletes the first document with `expiryts` greater 
than `ISODate("2015-11-01T12:40:15Z")`

```javascript
try {
   db.orders.deleteOne( { expiryts: { $lt: ISODate("2015-11-01T12:40:15Z") } } );
} catch (e) {
   print(e);
}
```

The operation returns:

```javascript
{ acknowledged: true, deletedCount: 1 }
```

   

### deleteOne() with Write Concern

Given a three member replica set, the following operation specifies a 
`w` of `majority`, `wtimeout` of `100`:

```javascript
try {
   db.orders.deleteOne(
       { _id: ObjectId("563237a41a4d68582c2509da") },
       { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print (e);
}
```

If the acknowledgment takes longer than the `wtimeout` limit, the following 
exception is thrown:

```javascript
WriteConcernError({
   code: 64,
   errmsg: "waiting for replication timed out",
   errInfo: {
     wtimeout: true,
     writeConcern: {  
       w: "majority",
       wtimeout: 100,
       provenance: "getLastErrorDefaults"
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

A `restaurants` collection has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The following operation includes the collation
option:

```javascript
db.restaurants.deleteOne( 
   { category: "cafe", status: "Open" }, 
   { collation: { locale: "fr", strength: 1 } }
)
```

The delete filter specifies a collation with `strength: 1`, which
means the collation ignores differences between case and letter
variants. As a result, even though there is not a document that has an
exact match with the specified case and letter variants in the filter,
the operation still matches and deletes a document.

### Specify `hint` for Delete Operations

In `mongosh`, create a `students` collection
with the following documents:

```javascript
db.members.insertMany( [
   { _id: 1, student: "Richard", grade: "F", points: 0 },
   { _id: 2, student: "Jane", grade: "A", points: 60 },
   { _id: 3, student: "Adam", grade: "F", points:  0 },
   { _id: 4, student: "Ronan", grade: "D", points: 20 },
   { _id: 5, student: "Noah", grade: "F", points:  0 },
   { _id: 6, student: "Henry", grade: "A", points: 86 }
] )
```

Create the following index on the collection:

```javascript
db.members.createIndex( { grade: 1 } )
```

The following delete operation explicitly hints to use the index
`{ grade: 1 }`:

```javascript
db.members.deleteOne(
   { points: { $lte: 20 }, grade: "F" }, 
   { hint: { grade: 1 } }
)
```

**Note:**

If you specify an index that does not exist, the operation errors.

The delete command returns the following:

```javascript
{ acknowledged: true, deletedCount: 1 }
```

To view the indexes used, you can use the `$indexStats` pipeline:

```javascript
db.members.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } } ] )
```

The `accesses.ops` field in the `$indexStats` output
indicates the number of operations that used the index.

**See also:**

To delete multiple documents, see 
`db.collection.deleteMany()`
