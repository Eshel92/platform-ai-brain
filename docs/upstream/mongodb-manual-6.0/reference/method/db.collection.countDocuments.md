<!-- Converted from reference/method/db.collection.countDocuments.txt (reStructuredText). Includes are inlined. -->

# db.collection.countDocuments()

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/usage-examples/count/`**

**`https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/crud/read-operations/count/`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/read/count/`**

**`https://www.mongodb.com/docs/drivers/node/current/usage-examples/count/`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/crud/read-operations/count/`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-countDocuments/`**

**`https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/tutorial/#counting-documents`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/read/count/`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/usage-examples/count/`**

**`https://motor.readthedocs.io/en/stable/api-tornado/motor_collection.html#motor.motor_tornado.MotorCollection.count_documents`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/read/count/`**

**`https://www.mongodb.com/docs/drivers/rust/current/usage-examples/count/`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/read/count-documents/`**

**`https://mongocxx.org/api/current/classmongocxx_1_1v__noabi_1_1collection.html#a03c8eb29bfc93cecaefc0ef9773fced7`**

## Definition

**`db.collection.countDocuments(query, options)`**

Returns an integer for the number of documents that match the query 
of the collection or view.  This method is available for use in 
transactions.

## Compatibility

This method is available in deployments hosted in the following 
environments:

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

The `countDocuments()` method has the following form:

```javascript
db.collection.countDocuments( <query>, <options> )
```

The `countDocuments()` method takes the following
parameters:

| Parameter | Type | Description |
|---|---|---|
| query | document | The query selection criteria. To count all documents, specify an empty document. See also countDocuments-restrictions. |
| options | document | Optional. Extra options that affects the count behavior. |

The `options` document can contain the following:

| Field | Type | Description |
|---|---|---|
| `limit` | integer | Optional. The maximum number of documents to count. |
| `skip` | integer | Optional. The number of documents to skip before counting. |
| `hint` | string or document | Optional. An index name or the index specification to use for the query. |
| `maxTimeMS` | integer | Optional. The maximum amount of time to allow the count to run. |

## Behavior

### Mechanics

Unlike `db.collection.count()`,
`db.collection.countDocuments()` does not use the metadata to
return the count. Instead, it performs an aggregation of the document
to return an accurate count, even after an unclean shutdown or in the
presence of orphaned documents in a sharded
cluster.

`db.collection.countDocuments()` wraps the following
aggregation operation and returns just the value of `n`:

```javascript
db.collection.aggregate([
   { $match: <query> },
   { $group: { _id: null, n: { $sum: 1 } } }
])
```

### Empty or Non-Existing Collections and Views

`db.collection.countDocuments()` returns `0` on an empty or
non-existing collection or view.

### Query Restrictions

You cannot use the following query operators as part of the query
expression for `db.collection.countDocuments()`:

* - Restricted Operator
  - Alternative

* - `$where`

  - As an alternative, use `$expr` instead.

* - `$near`

  - As an alternative, use `$geoWithin` with `$center`; i.e.

    ```javascript
    { $geoWithin: { $center: [ [ <x>, <y> ], <radius> ] } }
    ```

* - `$nearSphere`

  - As an alternative, use `$geoWithin` with `$centerSphere`; i.e.

    ```javascript
    { $geoWithin: { $centerSphere: [ [ <x>, <y> ], <radius> ] } }
    ```

### Transactions

`db.collection.countDocuments()` can be used inside distributed transactions.

When you use `db.collection.countDocuments()` in a transaction, the resulting count will 
not filter out any uncommitted multi-document transactions.

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

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `db.collection.countDocuments()`
disconnects before the operation completes, MongoDB marks `db.collection.countDocuments()` 
for termination using `killOp`.

## Examples

### Count all Documents in a Collection

To count the number of documents in the `orders` collection, use the
following operation:

```javascript
db.orders.countDocuments( {}, { hint: "_id_"} )
```

**Note:**

If you use `db.collection.countDocuments()` with an empty query
filter, MongoDB performs a full collection scan which can be
inefficient. To improve performance, this example specifies a
`hint()` to use the automatically generated `_id`
index. Alternatively, you can use a query filter that finds all
documents such as `{ "_id": { $gte: MinKey } }` to count all
documents using an index. 

### Count all Documents that Match a Query

Count the number of the documents in the `orders`
collection with the field `ord_dt` greater than ``new
Date('01/01/2012')``:

```javascript
db.orders.countDocuments( { ord_dt: { $gt: new Date('01/01/2012') } }, { limit: 100 } )
```

**See also:**

- `db.collection.estimatedDocumentCount()`
- `$group` and `$sum`
- `count`
- collStats pipeline stage with the count
  option
