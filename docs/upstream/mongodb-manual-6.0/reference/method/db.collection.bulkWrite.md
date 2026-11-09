<!-- Converted from reference/method/db.collection.bulkWrite.txt (reStructuredText). Includes are inlined. -->

# db.collection.bulkWrite()

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/usage-examples/bulkWrite/`**

**`https://mongodb.github.io/mongo-csharp-driver/2.28.0/api/MongoDB.Driver/MongoDB.Driver.MongoCollectionBase-1.BulkWrite.html`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/write/bulk-write/`**

**`https://www.mongodb.com/docs/drivers/node/current/usage-examples/bulkWrite/`**

**`https://www.mongodb.com/docs/drivers/go/current/usage-examples/bulkWrite/`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-bulkWrite/`**

**`https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/guides/bulk/`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/bulk-writes/`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/usage-examples/bulkWrite/`**

**`https://motor.readthedocs.io/en/stable/examples/bulk.html`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/write/bulk-write/`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/crud/write-operations/bulk/`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/tutorials/bulk-writes/`**

**`https://mongocxx.org/api/current/classmongocxx_1_1v__noabi_1_1collection.html#a875875114020cd4b7a8d3761aa46b612`**

## Definition

**`db.collection.bulkWrite()`**

Performs multiple write operations with controls for order of
execution.

:returns:
   - A boolean `acknowledged` as `true` if the operation ran with
     write concern or `false` if write concern was disabled.
   - A count for each write operation.
   - An array containing an `_id` for each successfully inserted or
     upserted documents.

## Compatibility

`db.collection.bulkWrite()` is available in deployments hosted in the following environments:

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

**Note:**

You can't perform bulk write 
operations in the Atlas UI. 
To insert multiple documents, you must insert an array of documents.
To learn more, see atlas-ui-docs in the Atlas documentation. 

## Syntax

The `bulkWrite()` method has the following form:

```javascript
db.collection.bulkWrite(
    [ <operation 1>, <operation 2>, ... ],
    {
      writeConcern : <document>,
      ordered : <boolean>
    }
)
```

The `bulkWrite()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - `operations`
  - array
  - An array of `bulkWrite()` write
    operations.

    Valid operations are:

    - insertOne
    - updateOne
    - updateMany
    - deleteOne
    - deleteMany
    - replaceOne

    See bulkwrite-write-operations for usage of each operation

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern. Omit to use the default write concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - `ordered`
  - boolean
  - Optional. A boolean specifying whether the `mongod` instance should perform
    an ordered or unordered operation execution. Defaults to `true`.

    See bulkwrite-write-operations-executionofoperations

## Behavior

`bulkWrite()` takes an array of write operations and
executes each of them. By default operations are executed in order.
See bulkwrite-write-operations-executionofoperations for controlling
the order of write operation execution.

### Write Operations

#### insertOne

Inserts a single document into the collection.

```javascript
db.collection.bulkWrite( [
   { insertOne : { "document" : <document> } }
] )
```

See `db.collection.insertOne()`.

#### updateOne and updateMany

tabs:

   - id: updateOne
     name: updateOne
     content: |

        `updateOne` updates a *single* document in the collection that matches the
        filter. If multiple documents match, `updateOne` will update the *first*
        matching document only.

        ```javascript
        db.collection.bulkWrite( [
           { updateOne :
              {
                 "filter": <document>,
                 "update": <document or pipeline>, 
                 "upsert": <boolean>,
                 "collation": <document>,  
                 "arrayFilters": [ <filterdocument1>, ... ], 
                 "hint": <document|string> 
              }
           }
        ] )
        ```

   - id: updateMany
     name: updateMany
     content: |

        `updateMany` updates *all* documents in the collection
        that match the filter.

        ```javascript
        db.collection.bulkWrite( [
           { updateMany :
              {
                 "filter" : <document>,
                 "update" : <document or pipeline>, 
                 "upsert" : <boolean>,
                 "collation": <document>,                  
                 "arrayFilters": [ <filterdocument1>, ... ],
                 "hint": <document|string>
              }
           }
        ] )
        ```

* - Field
  - Notes

* - `filter`

  - The selection criteria for the update. The same query
    selectors as in the
    `db.collection.find()` method are available.

* - `update`

  - The update operation to perform. Can specify either:

    - A document that only contains update operator expressions.

    - An aggregation pipeline ``[
      <stage1>, <stage2>, ... ]`` that specifies the modifications to
      perform.

* - `upsert`

  - Optional. A boolean to indicate whether to perform an upsert.

    By default, `upsert` is `false`.

* - `arrayFilters`

  - Optional. An array of filter documents that determine which
    array elements to modify for an update operation on an array
    field.

* - `collation`

  - Optional. Specifies the collation to use for
    the operation.

* - `hint`

  - Optional. The index to use to support the
    update `filter`. If you specify an index that does not exist,
    the operation errors.

For details, see `db.collection.updateOne()` and
`db.collection.updateMany()`.

#### replaceOne

`replaceOne` replaces a *single* document in the collection that matches the
filter. If multiple documents match, `replaceOne` will replace the *first*
matching document only.

```javascript
db.collection.bulkWrite([
   { replaceOne :
      {
         "filter" : <document>,
         "replacement" : <document>,
         "upsert" : <boolean>,
         "collation": <document>, 
         "hint": <document|string> 
      }
   }
] )
```

| Field | Notes |
|---|---|
| `filter` | The selection criteria for the replacement operation. The same query selectors as in the `db.collection.find()` method are available. |
| `replacement` | The replacement document. The document cannot contain update operators. |
| `upsert` | Optional. A boolean to indicate whether to perform an upsert. By default, `upsert` is `false`. |
| `collation` | Optional. Specifies the collation to use for the operation. |
| `hint` | Optional. The index to use to support the update `filter`. If you specify an index that does not exist, the operation errors. |

For details, see to `db.collection.replaceOne()`.

#### deleteOne and deleteMany

tabs:

   - id: deleteOne
     name: deleteOne
     content: |

        `deleteOne` deletes a *single* document in the collection that match the
        filter. If multiple documents match, `deleteOne` will delete the *first*
        matching document only.

        ```javascript
        db.collection.bulkWrite([
           { deleteOne : {
              "filter" : <document>,
              "collation" : <document>                   // Available starting in 3.4
           } }
        ] )
        ```

   - id: deleteMany
     name: deleteMany
     content: |

        `deleteMany` deletes *all* documents in the collection
        that match the filter.

        ```javascript
        db.collection.bulkWrite([
           { deleteMany: {
              "filter" : <document>,
              "collation" : <document>                    // Available starting in 3.4
           } }
        ] )
        ```

| Field | Notes |
|---|---|
| `filter` | The selection criteria for the delete operation. The same query selectors as in the `db.collection.find()` method are available. |
| `collation` | Optional. Specifies the collation to use for the operation. |

For details, see `db.collection.deleteOne()` and
`db.collection.deleteMany()`.

### `_id` Field

If the document does not specify an _id field, then `mongod`
adds the `_id` field and assign a unique
`ObjectId` for the document before inserting or upserting it.
Most drivers create an ObjectId and insert the `_id` field, but the
`mongod` will create and populate the `_id` if the driver or
application does not.

If the document contains an `_id` field, the `_id` value must be
unique within the collection to avoid duplicate key error.

Update or replace operations cannot specify an `_id` value that differs
from the original document.

### Execution of Operations

The `ordered` parameter specifies whether
`bulkWrite()` will execute operations in order or not.
By default, operations are executed in order.

The following code represents a `bulkWrite()` with
five operations.

```javascript
db.collection.bulkWrite(
   [
      { insertOne : <document> },
      { updateOne : <document> },
      { updateMany : <document> },
      { replaceOne : <document> },
      { deleteOne : <document> },
      { deleteMany : <document> }
   ]
)
```

In the default `ordered : true` state, each operation will
be executed in order, from the first operation `insertOne`
to the last operation `deleteMany`.

If `ordered` is set to false, operations may be reordered by
`mongod` to increase performance.
Applications should not depend on order of operation execution.

The following code represents an unordered
`bulkWrite()` with six operations:

```javascript
db.collection.bulkWrite(
   [
      { insertOne : <document> },
      { updateOne : <document> },
      { updateMany : <document> },
      { replaceOne : <document> },
      { deleteOne : <document> },
      { deleteMany : <document> }
   ],
   { ordered : false }
)
```

With `ordered : false`, the results of the operation may vary. For example,
the `deleteOne` or `deleteMany` may remove more or fewer documents
depending on whether the run before or after the `insertOne`, `updateOne`,
`updateMany`, or `replaceOne` operations.

The number of operations in each group cannot exceed the value of
the `maxWriteBatchSize` of
the database. As of MongoDB 3.6, this value is `100,000`.
This value is shown in the `hello.maxWriteBatchSize` field.

This limit prevents issues with oversized error messages. If a group
exceeds this `limit`,
the client driver divides the group into smaller groups with counts
less than or equal to the value of the limit. For example, with the
`maxWriteBatchSize` value of `100,000`, if the queue consists of
`200,000` operations, the driver creates 2 groups, each with
`100,000` operations.

**Note:**

The driver only divides the group into smaller groups when using
the high-level API. If using
db.runCommand() directly
(for example, when writing a driver), MongoDB throws an error when
attempting to execute a write batch which exceeds the limit.

Starting in MongoDB 3.6, once the error report for a single batch grows
too large, MongoDB truncates all remaining error messages to the empty
string. Currently, begins once there are at least 2 error messages with
total size greater than `1MB`.

The sizes and grouping mechanics are internal performance details and
are subject to change in future versions.

Executing an `ordered` list of operations on a
sharded collection will generally be slower than executing an
`unordered` list
since with an ordered list, each operation must wait for the previous
operation to finish.

### Capped Collections

`bulkWrite()` write operations have restrictions when
used on a capped collection.

`updateOne` and `updateMany` throw a `WriteError` if the
`update` criteria increases the size of the document being modified.

`replaceOne` throws a `WriteError` if the
`replacement` document has a larger size than the original
document.

`deleteOne` and `deleteMany` throw a `WriteError` if used on a
capped collection.

### Time Series Collections

`bulkWrite()` write operations have restrictions
when used on a time series collection. Only `insertOne` can be
used on time series collections. All other operations will return a
`WriteError`.

### Error Handling

`db.collection.bulkWrite()` throws a `BulkWriteError`
exception on errors. See bulkwrite-error-handling-txn.

Excluding /reference/write-concern errors, ordered operations
stop after an error, while unordered operations continue to process any
remaining write operations in the queue, unless when run inside a
transaction. See bulkwrite-error-handling-txn.

Write concern errors are displayed in the `writeConcernErrors` field, while
all other errors are displayed in the `writeErrors` field. If an error is
encountered, the number of successful write operations are displayed instead
of the inserted `_id` values. Ordered operations display the single error
encountered while unordered operations display each error in an array.

#### Schema Validation Errors

If your collection uses schema validation and has `validationAction` set to 
`error`, inserting an invalid document or updating a document with
invalid values throws an error. Operations preceding the invalid 
operation in the `operations` array are executed and written to the 
collection. The `ordered` field determines if the remaining 
operations are executed.

### Transactions

`db.collection.bulkWrite()` can be used inside distributed transactions.

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

#### Inserts and Upserts within Transactions

For feature compatibility version (fcv) `"4.4"`
and greater, if an insert operation or update operation with
`upsert: true` is run in a transaction against a non-existing
collection, the collection is implicitly created.

**Note:**

You cannot create new collections in cross-shard write transactions.
For example, if you write to an existing collection in one shard and
implicitly create a collection in a different shard, MongoDB cannot
perform both operations in the same transaction.

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

#### Error Handling inside Transactions

Starting in MongoDB 4.2, if a `db.collection.bulkWrite()`
operation encounters an error inside a transaction, the method throws a BulkWriteException (same as outside a transaction). 

In 4.0, if the `bulkWrite` operation encounters an error inside a
transaction, the error thrown is not wrapped as a
`BulkWriteException`.

Inside a transaction, the first error in a bulk write causes the
entire bulk write to fail and aborts the transaction, even if the
bulk write is unordered.

## Examples

### Ordered Bulk Write Example

It is important that you understand `bulkWrite()`
operation ordering and error handling. By default,
`bulkWrite()` runs an ordered list of operations:

- Operations run serially.
- If an operation has an error, that operation and any following
  operations are not run.
- Operations listed before the error operation are completed.

The `bulkWrite()` examples use the `pizzas`
collection:

```javascript
db.pizzas.insertMany( [
   { _id: 0, type: "pepperoni", size: "small", price: 4 },
   { _id: 1, type: "cheese", size: "medium", price: 7 },
   { _id: 2, type: "vegan", size: "large", price: 8 }
] )
```

The following `bulkWrite()` example runs
these operations on the `pizzas` collection:

- Adds two documents using `insertOne`.
- Updates a document using `updateOne`.
- Deletes a document using `deleteOne`.
- Replaces a document using `replaceOne`.

```javascript
try {
   db.pizzas.bulkWrite( [
      { insertOne: { document: { _id: 3, type: "beef", size: "medium", price: 6 } } },
      { insertOne: { document: { _id: 4, type: "sausage", size: "large", price: 10 } } },
      { updateOne: {
         filter: { type: "cheese" },
         update: { $set: { price: 8 } }
      } },
      { deleteOne: { filter: { type: "pepperoni"} } },
      { replaceOne: {
         filter: { type: "vegan" },
         replacement: { type: "tofu", size: "small", price: 4 }
      } }
   ] )
} catch( error ) {
   print( error )
}
```

Example output, which includes a summary of the completed operations:

```javascript
{
   acknowledged: true,
   insertedCount: 2,
   insertedIds: { '0': 3, '1': 4 },
   matchedCount: 2,
   modifiedCount: 2,
   deletedCount: 1,
   upsertedCount: 0,
   upsertedIds: {}
}
```

If the collection already contained a document with an `_id` of `4`
before running the previous `bulkWrite()`
example, the following duplicate key exception is returned for the
second `insertOne` operation:

```javascript
writeErrors: [
   WriteError {
      err: {
         index: 1,
         code: 11000,
         errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 4 }',
         op: { _id: 4, type: 'sausage', size: 'large', price: 10 }
      }
   }
],
result: BulkWriteResult {
   result: {
      ok: 1,
      writeErrors: [
         WriteError {
            err: {
               index: 1,
               code: 11000,
               errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 4 }',
               op: { _id: 4, type: 'sausage', size: 'large', price: 10 }
            }
         }
      ],
      writeConcernErrors: [],
      insertedIds: [ { index: 0, _id: 3 }, { index: 1, _id: 4 } ],
      nInserted: 1,
      nUpserted: 0,
      nMatched: 0,
      nModified: 0,
      nRemoved: 0,
      upserted: []
   }
}
```

Because the `bulkWrite()` example is ordered,
only the first `insertOne` operation is completed.

To complete all operations that do not have errors, run
`bulkWrite()` with `ordered` set to `false`.
For an example, see the following section.

### Unordered Bulk Write Example

To specify an unordered `bulkWrite()`, set
`ordered` to `false`.

In an unordered `bulkWrite()` list of operations:

- Operations can run in parallel (not guaranteed). For details. See
  bulk-write-operations-ordered-vs-unordered.
- Operations with errors are not completed.
- All operations without errors are completed.

Continuing the `pizzas` collection example, drop and recreate the
collection:

```javascript
db.pizzas.insertMany( [
   { _id: 0, type: "pepperoni", size: "small", price: 4 },
   { _id: 1, type: "cheese", size: "medium", price: 7 },
   { _id: 2, type: "vegan", size: "large", price: 8 }
] )
```

In the following example:

- `bulkWrite()` runs unordered operations on
  the `pizzas` collection.
- The second `insertOne` operation has the same `_id` as the first
  `insertOne`, which causes a duplicate key error.

```javascript
try {
   db.pizzas.bulkWrite( [
      { insertOne: { document: { _id: 3, type: "beef", size: "medium", price: 6 } } },
      { insertOne: { document: { _id: 3, type: "sausage", size: "large", price: 10 } } },
      { updateOne: {
         filter: { type: "cheese" },
         update: { $set: { price: 8 } }
      } },
      { deleteOne: { filter: { type: "pepperoni"} } },
      { replaceOne: {
         filter: { type: "vegan" },
         replacement: { type: "tofu", size: "small", price: 4 }
      } }
   ],
   { ordered: false } )
} catch( error ) {
   print( error )
}
```

Example output, which includes the duplicate key error and a summary of
the completed operations:

```javascript
writeErrors: [
   WriteError {
      err: {
         index: 1,
         code: 11000,
         errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 3 }',
         op: { _id: 3, type: 'sausage', size: 'large', price: 10 }
      }
   }
],
result: BulkWriteResult {
   result: {
      ok: 1,
      writeErrors: [
         WriteError {
            err: {
               index: 1,
               code: 11000,
               errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 3 }',
               op: { _id: 3, type: 'sausage', size: 'large', price: 10 }
            }
         }
      ],
      writeConcernErrors: [],
      insertedIds: [ { index: 0, _id: 3 }, { index: 1, _id: 3 } ],
      nInserted: 1,
      nUpserted: 0,
      nMatched: 2,
      nModified: 2,
      nRemoved: 1,
      upserted: []
   }
}
```

The second `insertOne` operation fails because of the duplicate key
error. In an unordered `bulkWrite()`, any
operation without an error is completed.

### Bulk Write with Write Concern Example

Continuing the `pizzas` collection example, drop and recreate the
collection:

```javascript
db.pizzas.insertMany( [
   { _id: 0, type: "pepperoni", size: "small", price: 4 },
   { _id: 1, type: "cheese", size: "medium", price: 7 },
   { _id: 2, type: "vegan", size: "large", price: 8 }
] )
```

The following `bulkWrite()` example runs
operations on the `pizzas` collection and sets a `"majority"`
write concern with a 100 millisecond timeout:

```javascript
try {
   db.pizzas.bulkWrite( [
      { updateMany: {
         filter: { size: "medium" },
         update: { $inc: { price: 0.1 } }
      } },
      { updateMany: {
         filter: { size: "small" },
         update: { $inc: { price: -0.25 } }
      } },
      { deleteMany: { filter: { size: "large" } } },
      { insertOne: {
         document: { _id: 4, type: "sausage", size: "small", price: 12 }
      } } ],
      { writeConcern: { w: "majority", wtimeout: 100 } }
   )
} catch( error ) {
   print( error )
}
```

If the time for the majority of replica set members to acknowledge the
operations exceeds `wtimeout`, the example returns a write concern
error and a summary of completed operations:

```javascript
result: BulkWriteResult {
   result: {
      ok: 1,
      writeErrors: [],
      writeConcernErrors: [
         WriteConcernError {
            err: {
               code: 64,
               codeName: 'WriteConcernTimeout',
               errmsg: 'waiting for replication timed out',
               errInfo: { wtimeout: true, writeConcern: [Object] }
            }
         }
      ],
      insertedIds: [ { index: 3, _id: 4 } ],
      nInserted: 0,
      nUpserted: 0,
      nMatched: 2,
      nModified: 2,
      nRemoved: 0,
      upserted: [],
      opTime: { ts: Timestamp({ t: 1660329086, i: 2 }), t: Long("1") }
   }
}
```
