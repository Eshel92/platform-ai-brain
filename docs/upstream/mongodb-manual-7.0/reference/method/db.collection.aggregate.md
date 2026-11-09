<!-- Converted from reference/method/db.collection.aggregate.txt (reStructuredText). Includes are inlined. -->

# db.collection.aggregate() (mongosh method)

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/aggregation/`**

**`https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/aggregation/`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/`**

**`https://www.mongodb.com/docs/drivers/node/current/fundamentals/aggregation/`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/aggregation/`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-aggregate/`**

**`https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/guides/aggregate/`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/aggregation/`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/aggregation/`**

**`https://www.mongodb.com/docs/mongoid/current/reference/aggregation/`**

**`https://motor.readthedocs.io/en/stable/api-asyncio/asyncio_motor_database.html#motor.motor_asyncio.AsyncIOMotorDatabase.aggregate`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/aggregation/`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/aggregation/`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/tutorials/aggregation/`**

**`https://mongocxx.org/api/current/classmongocxx_1_1v__noabi_1_1collection.html#a480f6d0f9986d43b1d17d6ed8876941d`**

## Definition

**`db.collection.aggregate(pipeline, options)`**

Calculates aggregate values for the data in a collection or a view.

:returns:

   - A cursor for the documents produced by the final stage of
     the aggregation pipeline.

   - If the pipeline includes the `explain` option, the query returns 
     a document that provides details on the processing of the 
     aggregation operation.

   - If the pipeline includes the `$out` or
     `$merge` operators, the query returns an empty cursor.

## Compatibility

You can use `db.collection.aggregate()` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`db.collection.aggregate()` has the following form:

```javascript
db.collection.aggregate( <pipeline>, <options> )
```

### Parameters

`db.collection.aggregate()` takes the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `pipeline` | array | A sequence of data aggregation operations or stages. See the aggregation pipeline operators for details. The method can still accept the pipeline stages as separate arguments instead of as elements in an array; however, if you do not specify the `pipeline` as an array, you cannot specify the `options` parameter. |
| `options` | document | .. _db.collection.aggregate-let-option: Optional. Additional options that `aggregate()` passes to the `aggregate` command. Available only if you specify the `pipeline` as an array. To see available options, see [AggregateOptions](https://mongodb.github.io/node-mongodb-native/Next/interfaces/AggregateOptions.html). |

## Behavior

### Error Handling

If an error occurs, the `aggregate()` helper
throws an exception.

### Cursor Behavior

In `mongosh`, if the `aggregate()` cursor is not
assigned to a variable using the `var` keyword,
`mongosh` automatically iterates the cursor up to
20 times. See
/tutorial/iterate-a-cursor for handling cursors in
`mongosh`.

Cursors returned from aggregation only supports cursor methods that
operate on evaluated cursors (i.e. cursors whose first batch has been
retrieved), such as the following methods:

* `cursor.hasNext()`
* `cursor.next()`
* `cursor.toArray()`
* `cursor.forEach()`
* `cursor.map()`
* `cursor.objsLeftInBatch()`
* `cursor.itcount()`
* `cursor.pretty()`

For more information, see:

- aggregation-pipeline
- /reference/aggregation
- /core/aggregation-pipeline-limits
- `aggregate`

### Sessions

For cursors created inside a session, you cannot call
`getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call
`getMore` inside a session.

#### Session Idle Timeout

MongoDB drivers and `mongosh`
associate all operations with a server session, with the exception of unacknowledged
write operations. For operations not explicitly associated with a
session (i.e. using `Mongo.startSession()`), MongoDB drivers
and `mongosh` create an implicit session and associate it
with the operation.

If a session is idle for longer than 30 minutes, the MongoDB server
marks that session as expired and may close it at any time. When the
MongoDB server closes the session, it also kills any in-progress
operations and open cursors associated with the session. This
includes cursors configured with `noCursorTimeout` or
a `maxTimeMS` greater than 30 minutes.

For operations that return a cursor, if the cursor may be idle for
longer than 30 minutes, issue the operation within an explicit session
using `Mongo.startSession()` and periodically refresh the
session using the `refreshSessions` command. See
`Session Idle Timeout` for more information.

### Transactions

`aggregate()` can be used inside distributed transactions.

However, the following stages are not allowed within transactions:

- `$collStats`
- `$currentOp`
- `$indexStats`
- `$listLocalSessions`
- `$listSessions`
- `$out`
- `$merge`
- `$planCacheStats`

You also cannot specify the `explain` option.

- For cursors created outside of a transaction, you cannot call
  `getMore` inside the transaction.

- For cursors created in a transaction, you cannot call
  `getMore` outside the transaction.

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

### Client Disconnection

For `aggregate()` operations that do not include the
`$out` or `$merge` stages:

If the client that issued `aggregate()` disconnects before the operation 
completes, MongoDB marks `aggregate()` for termination using 
`killOp`.

## Examples

The following examples use the collection `orders` that contains the
following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, cust_id: "abc1", ord_date: ISODate("2012-11-02T17:04:11.102Z"), status: "A", amount: 50 },
   { _id: 2, cust_id: "xyz1", ord_date: ISODate("2013-10-01T17:04:11.102Z"), status: "A", amount: 100 },
   { _id: 3, cust_id: "xyz1", ord_date: ISODate("2013-10-12T17:04:11.102Z"), status: "D", amount: 25 },
   { _id: 4, cust_id: "xyz1", ord_date: ISODate("2013-10-11T17:04:11.102Z"), status: "D", amount: 125 },
   { _id: 5, cust_id: "abc1", ord_date: ISODate("2013-11-12T17:04:11.102Z"), status: "A", amount: 25 }
] )
```

### Group by and Calculate a Sum

The following aggregation operation selects documents with status equal
to `"A"`, groups the matching documents by the `cust_id` field and
calculates the `total` for each `cust_id` field from the sum of the
`amount` field, and sorts the results by the `total` field in
descending order:

```javascript
db.orders.aggregate( [
   { $match: { status: "A" } },
   { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
   { $sort: { total: -1 } }
] )
```

The operation returns a cursor with the following documents:

```javascript
[
   { _id: "xyz1", total: 100 },
   { _id: "abc1", total: 75 }
]
```

`mongosh` iterates the returned cursor automatically
to print the results. See /tutorial/iterate-a-cursor for
handling cursors manually in `mongosh`.

### Return Information on Aggregation Pipeline Operation

The following example uses `db.collection.explain()` to view
detailed information regarding the execution plan of the aggregation
pipeline.

```javascript
db.orders.explain().aggregate( [
   { $match: { status: "A" } },
   { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
   { $sort: { total: -1 } }
] )
```

The operation returns a document that details the processing of the
aggregation pipeline. For example, the document may show, among other
details, which index, if any, the operation used. [#agg-index-filters]_
If the `orders` collection is a sharded collection, the document
would also show the division of labor between the shards and the merge
operation, and for targeted queries, the targeted shards.

**Note:** The intended readers of the `explain` output document are humans, and

not machines, and the output format is subject to change between
releases.

You can view more verbose explain output by passing the
`executionStats` or `allPlansExecution` explain modes to the
`db.collection.explain()` method.

### Interaction with `allowDiskUseByDefault`

Starting in MongoDB 6.0, pipeline stages that require more than 100 
megabytes of memory to execute write temporary files to disk by 
default. These temporary files last for the duration of the pipeline 
execution and can influence storage space on your instance. In earlier 
versions of MongoDB, you must pass  `{ allowDiskUse: true }` to 
individual `find` and `aggregate` commands to enable this 
behavior.

Individual `find` and `aggregate` commands can override the 
`allowDiskUseByDefault` parameter by either:

- Using `{ allowDiskUse: true }` to allow writing temporary files out 
  to disk when `allowDiskUseByDefault` is set to `false`

- Using `{ allowDiskUse: false }` to prohibit writing temporary files
  out to disk when `allowDiskUseByDefault` is set to `true`

The profiler log messages and diagnostic log
messages includes a `usedDisk`
indicator if any aggregation stage wrote data to temporary files due
to memory restrictions.

For more information, see agg-pipeline-limits.

### Specify an Initial Batch Size

To specify an initial batch size for the cursor, use the following
syntax for the `cursor` option:

```javascript
cursor: { batchSize: <int> }
```

For example, the following aggregation operation specifies the
*initial* batch size of `0` for the cursor:

```javascript
db.orders.aggregate(
                     [
                       { $match: { status: "A" } },
                       { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
                       { $sort: { total: -1 } },
                       { $limit: 2 }
                     ],
                     {
                       cursor: { batchSize: 0 }
                     }
                   )
```

The `{ cursor: { batchSize: 0 } }` document, which specifies the size of the 
*initial* batch size, indicates an empty first batch. This batch size is useful 
for quickly returning a cursor or failure message without doing significant 
server-side work. 

To specify batch size for subsequent `getMore` operations 
(after the initial batch), use the `batchSize` field when running the 
`getMore` command. 

`mongosh` iterates the returned cursor automatically
to print the results. See /tutorial/iterate-a-cursor for
handling cursors manually in `mongosh`.

### Specify a Collation

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

The following aggregation operation includes the collation option:

```javascript
db.restaurants.aggregate(
   [
      { $match: { status: "Open" } },
      {
         $group: {
            _id: "$category",
            count: { $sum: 1 }
         }
      }
   ],
   { collation: { locale: "fr", strength: 1 } }
)
```

Output:

```javascript
[ { _id: 'café', count: 3 } ]
```

The aggregation specifies a collation with `strength: 1`, which
means the collation ignores differences between case and letter
variants. As a result:

- The `$match` filter matches all documents in the collection and
  passes those documents to the `$group` stage.
  
- The `$group` stage ignores differences in letter variants in the
  `category` field and puts all documents in a single group.

**Note:**

If performing an aggregation that involves multiple views, such as
with `$lookup` or `$graphLookup`, the views must
have the same collation.

For descriptions on the collation fields, see
collation-document-fields.

### Hint an Index

Create a collection `food` with the following documents:

```javascript
db.food.insertMany( [
   { _id: 1, category: "cake", type: "chocolate", qty: 10 },
   { _id: 2, category: "cake", type: "ice cream", qty: 25 },
   { _id: 3, category: "pie", type: "boston cream", qty: 20 },
   { _id: 4, category: "pie", type: "blueberry", qty: 15 }
] )
```

Create the following indexes:

```javascript
db.food.createIndex( { qty: 1, type: 1 } );
db.food.createIndex( { qty: 1, category: 1 } );
```

The following aggregation operation includes the `hint` option to
force the usage of the specified index:

```javascript
db.food.aggregate(
   [ { $sort: { qty: 1 }}, { $match: { category: "cake", qty: 10  } }, { $sort: { type: -1 } } ],
   { hint: { qty: 1, category: 1 } }
)
```

### Override `readConcern`

Use the `readConcern` option to specify the read concern for
the operation.

You cannot use the `$out` or the `$merge` stage
in conjunction with read concern `"linearizable"`. That
is, if you specify `"linearizable"` read concern for
`db.collection.aggregate()`, you cannot include either
stages in the pipeline.

The following operation on a replica set specifies a
/reference/read-concern of `"majority"` to read the
most recent copy of the data confirmed as having been written to a
majority of the nodes.

**Note:**

- .. include:: /includes/usage-read-concern-majority.rst

- .. include:: /includes/fact-aggregate-readConcern.rst

- .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

```javascript
db.restaurants.aggregate(
   [ { $match: { rating: { $lt: 5 } } } ],
   { readConcern: { level: "majority" } }
)
```

### Specify a Comment

A collection named `movies` contains documents formatted as such:

```javascript
db.movies.insertOne(
   {
      _id: ObjectId("599b3b54b8ffff5d1cd323d8"),
      title: "Jaws",
      year: 1975,
      imdb: "tt0073195"
   }
)
```

The following aggregation operation finds movies created in 1995 and includes
the `comment` option to provide tracking information in the `logs`,
the `db.system.profile` collection, and `db.currentOp`.

```javascript
db.movies.aggregate( [ { $match: { year : 1995 } } ], { comment : "match_all_movies_from_1995" } ).pretty()
```

On a system with profiling enabled, you can then query the `system.profile`
collection to see all recent similar aggregations, as shown below:

```javascript
db.system.profile.find( { "command.aggregate": "movies", "command.comment" : "match_all_movies_from_1995" } ).sort( { ts : -1 } ).pretty()
```

This will return a set of profiler results in the following format:

```javascript
{
  "op" : "command",
  "ns" : "video.movies",
  "command" : {
    "aggregate" : "movies",
    "pipeline" : [
      {
        "$match" : {
          "year" : 1995
        }
      }
    ],
    "comment" : "match_all_movies_from_1995",
    "cursor" : {

    },
    "$db" : "video"
  },
  ...
}
```

An application can encode any arbitrary information in the comment in order
to more easily trace or identify specific operations through the system.
For instance, an application might attach a string comment incorporating its
process ID, thread ID, client hostname, and the user who issued the command.

### Use Variables in `let`

**New in version:** 5.0

To define variables that you can access elsewhere in the command, use
the let option.

**Note:**

To filter results using a variable in a pipeline `$match`
stage, you must access the variable within the `$expr`
operator.

Create a collection `cakeSales` containing sales for cake flavors:

```javascript
db.cakeSales.insertMany( [
   { _id: 1, flavor: "chocolate", salesTotal: 1580 },
   { _id: 2, flavor: "strawberry", salesTotal: 4350 },
   { _id: 3, flavor: "cherry", salesTotal: 2150 }
] )
```

The following example:

- retrieves the cake that has a `salesTotal` greater than 3000, which
  is the cake with an `_id` of 2

- defines a `targetTotal` variable in `let`, which is referenced in
  `$gt` as `$$targetTotal`

```javascript
db.cakeSales.aggregate(
   [
      { $match: {
         $expr: { $gt: [ "$salesTotal", "$$targetTotal" ] }
      } }
   ],
   { let: { targetTotal: 3000 } }
)
```
