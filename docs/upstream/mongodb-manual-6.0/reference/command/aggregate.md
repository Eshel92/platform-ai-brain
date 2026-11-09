<!-- Converted from reference/command/aggregate.txt (reStructuredText). Includes are inlined. -->

# aggregate

## Definition

**`aggregate`**

Performs aggregation operation using the aggregation pipeline. The pipeline allows users 
to process data from a collection or other source with a sequence of 
stage-based manipulations.

   `db.collection.aggregate` helper methods or with the
   `watch` helper method

**Tip:**

In `mongosh`, this command can also be run through the `db.aggregate` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**Changed in version:** 5.0

The command has the following syntax:

```javascript
db.runCommand(
   {
     aggregate: "<collection>" || 1,
     pipeline: [ <stage>, <...> ],
     explain: <boolean>,
     allowDiskUse: <boolean>,
     cursor: <document>,
     maxTimeMS: <int>,
     bypassDocumentValidation: <boolean>,
     readConcern: <document>,
     collation: <document>,
     hint: <string or document>,
     comment: <any>,
     writeConcern: <document>,
     let: <document> // Added in MongoDB 5.0
   }
)
```

### Command Fields

The `aggregate` command takes the following fields as
arguments:

* - Field

  - Type

  - Description

* - `aggregate`

  - string

  - The name of the collection or view that acts as the input for the
    aggregation pipeline. Use `1` for collection agnostic commands.

* - `pipeline`

  - array

  - An array of aggregation pipeline stages that process and
    transform the document stream as part of the aggregation
    pipeline.

* - `explain`

  - boolean

  - Optional. Specifies to return the information on the processing of the pipeline.

    Not available in multi-document transactions.

* - .. _aggregate-cmd-allowDiskUse:

    `allowDiskUse`

  - boolean

  - Optional.

    Use this option to override `allowDiskUseByDefault` 
    for a specific query. You can use this option to either:

    - Prohibit disk use on a system where disk use is allowed by 
      default.
    - Allow disk use on a system where disk use is prohibited by 
      default.

    Starting in MongoDB 6.0, if `allowDiskUseByDefault` is set 
    to `true` and the server requires more than 100 megabytes of memory 
    for a pipeline execution stage, MongoDB automatically writes 
    temporary files to disk unless the query specifies 
    `{ allowDiskUse: false }`.

    For details, see `allowDiskUseByDefault`.

    The profiler log messages and diagnostic log
    messages includes a `usedDisk`
    indicator if any aggregation stage wrote data to temporary files due
    to memory restrictions.

* - `cursor`

  - document

  - Specify a document that contains options that control the creation
    of the cursor object.

    MongoDB removes the use of `aggregate` command
    **without** the `cursor` option unless the command includes the
    `explain` option. Unless you include the `explain` option, you must
    specify the cursor option.

    - To indicate a cursor with the default batch size, specify ``cursor:
      {}``.

    - To indicate a cursor with a non-default batch size, use ``cursor: {
      batchSize: <num> }``.

* - `maxTimeMS`

  - non-negative integer

  - Optional.

    Specifies a time limit in milliseconds. 
    If you do not specify a value for `maxTimeMS`, operations will not time out. 
    A value of `0` explicitly specifies the default unbounded behavior.

    MongoDB terminates operations that exceed their allotted time limit
    using the same mechanism as `db.killOp()`. MongoDB only
    terminates an operation at one of its designated interrupt 
    points.

* - `bypassDocumentValidation`

  - boolean

  - Optional. Applicable only if you specify the `$out` or `$merge` aggregation
    stages.

    Enables `aggregate` to bypass schema validation
    during the operation. This lets you insert documents that do not
    meet the validation requirements.

* - `readConcern`

  - document

  - Optional. Specifies the read concern.

    The `readConcern` option has the following syntax: 
    `readConcern: { level: <value> }`

    Possible read concern levels are:

    - `"local"`. This is the default read concern level for
      read operations against the primary and secondaries.

    - `"available"`. Available for read operations against
      the primary and secondaries. `"available"` behaves the 
      same as `"local"` against the primary and non-sharded
      secondaries. The query returns the instance's most recent data.

    - `"majority"`. Available for replica sets that use
      WiredTiger storage engine.

    - `"linearizable"`. Available for read operations on the
      `primary` only.

    - `"snapshot"`. Available for multi-document
      transactions, and starting in MongoDB 5.0, certain
      read operations outside of multi-document transactions.

    For more formation on the read concern levels, see
    read-concern-levels.

    The `$out` stage cannot be used in conjunction with read concern 
    `"linearizable"`. If you specify `"linearizable"` 
    read concern for `db.collection.aggregate()`, you cannot include the
    `$out` stage in the pipeline.

    The `$merge` stage cannot be used in conjunction with read
    concern `"linearizable"`. That is, if you specify
    `"linearizable"` read concern for
    `db.collection.aggregate()`, you cannot include the
    `$merge` stage in the pipeline.

* - `collation`

  - document

  - Optional.

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

* - `hint`

  - string or document

  - Optional. The index to use for the aggregation. The index is on the initial
    collection/view against which the aggregation is run.

    Specify the index either by the index name or by the index
    specification document.

    The `hint` does not apply to `$lookup` and
    `$graphLookup` stages.

* - `comment`

  - any

  - .. include:: /includes/extracts/comment-content.rst

    Any comment set on a `aggregate` command is inherited
    by any subsequent `getMore` commands run on the
    `aggregate` cursor.

* - `writeConcern`

  - document

  - Optional. A document that expresses the write concern
    to use with the `$out` or `$merge` stage. 

    Omit to use the default write concern with the `$out` or
    `$merge` stage.

* - `let`

  - document

  - .. _aggregate-let-option:

    Optional.

    Specifies a document with a list of variables. This allows you to
    improve command readability by separating the variables from the query
    text.

    The document syntax is:

    ```javascript
    { 
      <variable_name_1>: <expression_1>,
      ...,
      <variable_name_n>: <expression_n>
    }
    ```

    The variable is set to the value returned by the expression, and cannot
    be changed afterwards.

    To access the value of a variable in the command, use the double
    dollar sign prefix (`$$`) together with your variable name in the form
    `$$<variable_name>`. For example: `$$targetTotal`.

    To use a variable to filter results in a pipeline `$match`
    stage, you must access the variable within the `$expr`
    operator.

    For a complete example using `let` and variables, see
    aggregate-let-example.

    **New in version:** 5.0

MongoDB removes the use of `aggregate` command
**without** the `cursor` option unless the command includes the
`explain` option. Unless you include the `explain` option, you must
specify the cursor option.

- To indicate a cursor with the default batch size, specify ``cursor:
  {}``.

- To indicate a cursor with a non-default batch size, use ``cursor: {
  batchSize: <num> }``.

For more information about the aggregation pipeline
/core/aggregation-pipeline, /reference/aggregation, and
/core/aggregation-pipeline-limits.

## Sessions

For cursors created inside a session, you cannot call
`getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call
`getMore` inside a session.

### Session Idle Timeout

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

## Transactions

`aggregate` can be used inside distributed transactions.

However, the following stages are not allowed within transactions:

- `$collStats`
- `$currentOp`
- `$indexStats`
- `$listLocalSessions`
- `$listSessions`
- `$merge`
- `$out`
- `$planCacheStats`
- `$unionWith`

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
/core/transactions-production-consideration.

### Client Disconnection

For `aggregate` operation that do not include the
`$out` or `$merge` stages:

Starting in MongoDB 4.2, if the client that issued `aggregate`
disconnects before the operation completes, MongoDB marks `aggregate` 
for termination using `killOp`.

## Stable API

When using Stable API V1:

- You cannot use the following stages in an `aggregate`
  command:

  - `$currentOp`
  - `$indexStats`
  - `$listLocalSessions`
  - `$listSessions`
  - `$planCacheStats`
  - `$search`

- Don't include the `explain` field in an `aggregate`
  command. If you do, the server returns an APIStrictError error.

- When using the `$collStats` stage, you can only use the
  `count` field. No other `$collStats` fields are
  available.

## Example

MongoDB removes the use of `aggregate` command
**without** the `cursor` option unless the command includes the
`explain` option. Unless you include the `explain` option, you must
specify the cursor option.

- To indicate a cursor with the default batch size, specify ``cursor:
  {}``.

- To indicate a cursor with a non-default batch size, use ``cursor: {
  batchSize: <num> }``.

Rather than run the `aggregate` command directly, most
users should use the `db.collection.aggregate()` helper
provided in `mongosh` or the equivalent helper in
their driver. In 2.6 and later, the
`db.collection.aggregate()` helper always returns a cursor.

Except for the first two examples which demonstrate the command 
syntax, the examples in this page use the
`db.collection.aggregate()` helper.

### Aggregate Data with Multi-Stage Pipeline

A collection `articles` contains documents such as the following:

```javascript
{
   _id: ObjectId("52769ea0f3dc6ead47c9a1b2"),
   author: "abc123",
   title: "zzz",
   tags: [ "programming", "database", "mongodb" ]
}
```

The following example performs an `aggregate` operation on
the `articles` collection to calculate the count of each distinct
element in the `tags` array that appears in the collection.

```javascript
db.runCommand( {
   aggregate: "articles", 
   pipeline: [
      { $project: { tags: 1 } },
      { $unwind: "$tags" },
      { $group: { _id: "$tags", count: { $sum : 1 } } }
   ],
   cursor: { }
} )
```

In `mongosh`, this operation can use the
`db.collection.aggregate()` helper as in the following:

```javascript
db.articles.aggregate( [
   { $project: { tags: 1 } },
   { $unwind: "$tags" },
   { $group: { _id: "$tags", count: { $sum : 1 } } }
] )
```

### Use $currentOp on an Admin Database

The following example runs a pipeline with two stages on the admin
database. The first stage runs the `$currentOp` operation 
and the second stage filters the results of that operation. 

```javascript
db.adminCommand( { 
   aggregate : 1, 
   pipeline : [ { 
      $currentOp : { allUsers : true, idleConnections : true } }, { 
      $match : { shard : "shard01" } 
      } 
   ], 
   cursor : { } 
} )
```

**Note:**

The `aggregate` command does not specify a collection and
instead takes the form `{aggregate: 1}`. This is because the initial 
`$currentOp` stage does not draw input from a collection. It
produces its own data that the rest of the pipeline uses. 

The new `db.aggregate()` helper has been added to assist in
running collectionless aggregations such as this. The above aggregation
could also be run like this example.

   

### Return Information on the Aggregation Operation

The following aggregation operation sets the optional field `explain`
to `true` to return information about the aggregation operation.

```javascript
db.orders.aggregate([
      { $match: { status: "A" } },
      { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
      { $sort: { total: -1 } }
   ],
   { explain: true }
)
```

**Note:** The `explain` output is subject to change between releases.

**See also:**

`db.collection.aggregate()` method

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

**See also:**

- `db.collection.aggregate()`
- /core/aggregation-pipeline-limits

### Aggregate Data Specifying Batch Size

To specify an *initial* batch size, specify the `batchSize` in the
`cursor` field, as in the following example:

```javascript
db.orders.aggregate( [
      { $match: { status: "A" } },
      { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
      { $sort: { total: -1 } },
      { $limit: 2 }
   ],
   { cursor: { batchSize: 0 } }
)
```

      
The `{ cursor: { batchSize: 0 } }` document, which specifies the size of the 
*initial* batch size, indicates an empty first batch. This batch size is useful 
for quickly returning a cursor or failure message without doing significant 
server-side work. 

To specify batch size for subsequent `getMore` operations 
(after the initial batch), use the `batchSize` field when running the 
`getMore` command. 

### Specify a Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following aggregation operation includes the collation
option:

```javascript
db.myColl.aggregate(
   [ { $match: { status: "A" } }, { $group: { _id: "$category", count: { $sum: 1 } } } ],
   { collation: { locale: "fr", strength: 1 } }
);
```

For descriptions on the collation fields, see
collation-document-fields.

### Hint an Index

Create a collection `foodColl` with the following documents:

```javascript
db.foodColl.insertMany( [
   { _id: 1, category: "cake", type: "chocolate", qty: 10 },
   { _id: 2, category: "cake", type: "ice cream", qty: 25 },
   { _id: 3, category: "pie", type: "boston cream", qty: 20 },
   { _id: 4, category: "pie", type: "blueberry", qty: 15 }
] )
```

Create the following indexes:

```javascript
db.foodColl.createIndex( { qty: 1, type: 1 } );
db.foodColl.createIndex( { qty: 1, category: 1 } );
```

The following aggregation operation includes the `hint` option to
force the usage of the specified index:

```javascript
db.foodColl.aggregate(
   [ { $sort: { qty: 1 }}, { $match: { category: "cake", qty: 10  } }, { $sort: { type: -1 } } ],
   { hint: { qty: 1, category: 1 } }
)
```

### Override Default Read Concern

To override the default read concern level, use the `readConcern`
option. The `getMore` command uses the `readConcern` level
specified in the originating `aggregate` command.

You cannot use the `$out` or the `$merge` stage
in conjunction with read concern `"linearizable"`. That
is, if you specify `"linearizable"` read concern for
`db.collection.aggregate()`, you cannot include either
stages in the pipeline.

The following operation on a replica set specifies a read concern of `"majority"` to read the
most recent copy of the data confirmed as having been written to a
majority of the nodes.

**Important:**

- .. include:: /includes/fact-aggregate-readConcern.rst

- .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

```javascript
db.restaurants.aggregate(
   [ { $match: { rating: { $lt: 5 } } } ],
   { readConcern: { level: "majority" } }
)
```

To ensure that a single thread can read its own writes, use
`"majority"` read concern and `"majority"`
write concern against the primary of the replica set.

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
db.runCommand( {
   aggregate: db.cakeSales.getName(),
   pipeline: [
      { $match: {
           $expr: { $gt: [ "$salesTotal", "$$targetTotal" ] }
      } },
    ],
    cursor: {},
    let: { targetTotal: 3000 }
} )
```

**See also:**

`db.collection.aggregate()`
