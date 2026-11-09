<!-- Converted from reference/command/find.txt (reStructuredText). Includes are inlined. -->

# find

## Definition

**`find`**

Executes a query and returns the first batch of results and the
cursor id, from which the client can construct a cursor.

   `db.collection.findOne()` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.find()` or.

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

The `find` command has the following syntax:

**Changed in version:** 5.0

```javascript
db.runCommand(
   {
      find: <string>,
      filter: <document>,
      sort: <document>,
      projection: <document>,
      hint: <document or string>,
      skip: <int>,
      limit: <int>,
      batchSize: <int>,
      singleBatch: <bool>,
      comment: <any>,
      maxTimeMS: <int>,
      readConcern: <document>,
      max: <document>,
      min: <document>,
      returnKey: <bool>,
      showRecordId: <bool>,
      tailable: <bool>,
      oplogReplay: <bool>,
      noCursorTimeout: <bool>,
      awaitData: <bool>,
      allowPartialResults: <bool>,
      collation: <document>,
      allowDiskUse : <bool>,
      let: <document> // Added in MongoDB 5.0
   }
)
```

### Command Fields

The command accepts the following fields:

* - Field
  - Type
  - Description

* - `find`
  - string
  - The name of the collection or view to query.

* - `filter`
  - document
  - Optional. The query predicate. If unspecified, then all documents in
    the collection will match the predicate.

* - .. _find-cmd-sort:

    sort
  - document
  - Optional. The sort specification for the ordering of the results.

* - `projection`
  - document
  - Optional. The projection specification to
    determine which fields to include in the returned documents. See
    find-projection and /reference/operator/projection.

    `find()` operations on views do not support
    the following projection
    operators:

    - `$`
    - `$elemMatch`
    - `$slice`
    - `$meta`

* - `hint`
  - string or document
  - Optional. Index specification. Specify either the index name as a
    string or the index key pattern. If specified, then the query system
    will only consider plans using the hinted index.

    With the following exception, `hint` is required if the command 
    includes the `min` and/or `max` fields; `hint` is not required 
    with `min` and/or `max` if the `filter` is an equality condition 
    on the `_id` field `{ _id: <value> }`.

* - `skip`
  - Positive integer
  - Optional. Number of documents to skip. Defaults to 0.

* - `limit`
  - Non-negative integer
  - Optional. The maximum number of documents to return. If unspecified,
    then defaults to no limit. A limit of 0 is equivalent to setting no
    limit.

* - `batchSize`
  - non-negative integer
  - Optional. The maximum number of documents that can be returned in each batch of a
    query result. By default, the `find` command has an initial `batchSize` of
    the lesser of `101` documents or 16 mebibytes (MiB) worth of documents.
    Subsequent batches have a maximum size of 16 MiB. This option can enforce a smaller
    limit than 16 MiB, but not a larger one. When set, the `batchSize` is the lesser
    of `batchSize` documents or 16 MiB worth of documents.

    A `batchSize` of `0` means that the cursor is established, 
    but no documents are returned in the first batch.

    Unlike the previous wire protocol version, a batchSize of 1 for
    the `find` command does not close the cursor.

* - `singleBatch`
  - boolean
  - Optional. Determines whether to close the cursor after the first
    batch. Defaults to false.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

    Any comment set on a `find` command is inherited
    by any subsequent `getMore` commands run on the
    `find` cursor.

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

    When specifying `linearizable read concern`, always use `maxTimeMS` in case a majority of
    data bearing members are unavailable. `maxTimeMS` ensures that
    the operation does not block indefinitely and instead returns
    an error if the read concern cannot be fulfilled.

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

    The `getMore` command uses the `readConcern` level
    specified in the originating `find` command.

* - `max`
  - document
  - Optional. The *exclusive* upper bound for a specific index. See
    `cursor.max()` for details.

    To use the `max` field, the command must also use `hint` unless the 
    specified `filter` is an equality condition on the `_id` field 
    `{ _id: <value> }`.

* - `min`
  - document
  - Optional. The *inclusive* lower bound for a specific index. See
    `cursor.min()` for details.

    To use the `min` field, the command must also use `hint` unless the
    specified `filter` is an equality condition on the `_id` field 
    `{ _id: <value> }`.

* - `returnKey`
  - boolean
  - Optional. If true, returns only the index keys in the resulting documents.
    Default value is false. If returnKey is true and the `find`
    command does not use an index, the returned documents will be empty.

* - `showRecordId`
  - boolean
  - Optional. Determines whether to return the record identifier for each document.
    If true, adds a field $recordId to the returned documents.

* - `tailable`
  - boolean
  - Optional. Returns a tailable cursor for a capped collections.

* - `awaitData`
  - boolean
  - Optional. Use in conjunction with the tailable option to block a
    `getMore` command on the cursor temporarily at the end
    of data rather than returning no data. After a timeout period,
    `find` returns as normal.

* - `noCursorTimeout`
  - boolean
  - Optional. Prevents the server from timing out non-session idle cursors 
    after an inactivity period of 30 minutes. Ignored for cursors that are 
    part of a session. For more information, refer to 
    Session Idle Timeout.

* - allowPartialResults
  - boolean
  - .. _cmd-find-allowPartialResults:

    Optional. For queries against a sharded collection, allows the
    command (or subsequent `getMore` commands) to return
    partial results, rather than an error, if one or more queried
    shards are unavailable.

    If `find` (or subsequent `getMore` commands)
    returns partial results because the queried shard(s) aren't available,
    the find output includes a
    `partialResultsReturned` indicator field. If the queried shards are
    available for the initial `find` command, but one or more shards
    become unavailable for subsequent `getMore` commands, only the
    `getMore` commands that run while the shards aren't available include
    `partialResultsReturned` in their output.

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

* - .. _find-cmd-allowDiskUse: 

    allowDiskUse

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

    `allowDiskUse` has no effect if MongoDB can satisfy the
    specified sort using an index, *or* if the
    in-memory sort requires less than 100 megabytes of memory.

    For more complete documentation on `allowDiskUse`, 
    see `cursor.allowDiskUse()`.

    For more information on memory restrictions for large in-memory
    sorts, see sort-index-use.

* - let
  - document
  - .. _find-let-syntax:

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

    To use a variable to filter results, you must access the variable
    within the `$expr` operator.

    For a complete example using `let` and variables, see
    find-let-example.

    **New in version:** 5.0

### Output

The command returns a document that contains the cursor information,
including the cursor ID and the first batch of documents. For example,
the following document is returned when run against a sharded
collection:

```javascript
{
   "cursor" : {
      "firstBatch" : [
         {
            "_id" : ObjectId("5e8e2ca217b5324fa9847435"),
            "zipcode" : "20001",
            "x" : 1
         },
         {
            "_id" : ObjectId("5e8e2ca517b5324fa9847436"),
            "zipcode" : "30001",
            "x" : 1
         }
      ],
      "partialResultsReturned" : true, 
      "id" : NumberLong("668860441858272439"),
      "ns" : "test.contacts"
   },
   "ok" : 1,
   "operationTime" : Timestamp(1586380205, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1586380225, 2),
      "signature" : {
         "hash" : BinData(0,"aI/jWsUVUSkMw8id+A+AVVTQh9Y="),
         "keyId" : NumberLong("6813364731999420435")
      }
   }
}
```

| Field | Description |
|---|---|
| `cursor` | Contains the cursor information, including the cursor `id` and the `firstBatch` of documents. If the operation against a sharded collection returns partial results due to the unavailability of the queried shard(s), the `cursor` document includes a `partialResultsReturned` field. To return partial results, rather than error, due to the unavailability of the queried shard(s), the `find` command must run with allowPartialResults set to `true`. See allowPartialResults. If the queried shards are initially available for the `find` command but one or more shards become unavailable in subsequent `getMore` commands, only the `getMore` commands run when a queried shard or shards are unavailable include the `partialResultsReturned` flag in the output. |
| `"ok"` | Indicates whether the command has succeeded (`1`) or failed (`0`). |

In addition to the aforementioned `find`-specific fields,
the `db.runCommand()` includes the following information for
replica sets and sharded clusters:

- `$clusterTime`
  
- `operationTime`

See db.runCommand() Results for details.

## Behavior

### `$regex` Find Queries No Longer Ignore Invalid Regex

Starting in MongoDB 5.1, invalid `$regex options` 
options are no longer ignored. This change makes 
`$regex options` more consistent with 
the use of `$regex` in the `aggregate` command and
projection queries.

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

`find` can be used inside distributed transactions.

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

Starting in MongoDB 4.2, if the client that issued `find`
disconnects before the operation completes, MongoDB marks `find` 
for termination using `killOp`.

### Stable API

When using Stable API V1, the following
`find` command fields are not supported:

- `awaitData`
- `max`
- `min`
- `noCursorTimeout`
- `oplogReplay`
- `returnKey`
- `showRecordId`
- `tailable`

### Index Filters and Collations

Starting in MongoDB 6.0, an index filter uses the collation previously set using the `planCacheSetFilter`
command.

## Examples

### Specify a Sort and Limit

The following command runs the `find`
command filtering on the `rating` field and the `cuisine` field.
The command includes a `projection` to only return the
following fields in the matching documents: `_id`, `name`,
`rating`, and `address` fields.

The command sorts the documents in the result set by the `name`
field and limits the result set to 5 documents.

```javascript
db.runCommand(
   {
     find: "restaurants",
     filter: { rating: { $gte: 9 }, cuisine: "italian" },
     projection: { name: 1, rating: 1, address: 1 },
     sort: { name: 1 },
     limit: 5
   }
)
```

### Override Default Read Concern

To override the default read concern level of `"local"`,
use the `readConcern` option.

The following operation on a replica set specifies a read
concern of `"majority"` to read the most recent copy of
the data confirmed as having been written to a majority of the nodes.

```javascript
db.runCommand(
   {
     find: "restaurants",
     filter: { rating: { $lt: 5 } },
     readConcern: { level: "majority" }
   }
)
```

Regardless of the read concern level, the most recent data on a
node may not reflect the most recent version of the data in the system.

The `getMore` command uses the `readConcern` level
specified in the originating `find` command.

A `readConcern` can be specified for the `mongosh` method
`db.collection.find()` using the `cursor.readConcern`
method:

```javascript
db.restaurants.find( { rating: { $lt: 5 } } ).readConcern("majority")
```

For more information on available read concerns, see
read-concern.

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

The following operation runs the `find`
command with the collation specified:

```javascript
db.runCommand(
   {
     find: "myColl",
     filter: { category: "cafe", status: "a" },
     sort: { category: 1 },
     collation: { locale: "fr", strength: 1 }
   }
)
```

`mongosh` provides the `cursor.collation()` to
specify collation for a
`db.collection.find()` operation.

### Use Variables in `let`

**New in version:** 5.0

To define variables that you can access elsewhere in the command, use
the let option.

**Note:**

To filter results using a variable, you must access the variable
within the `$expr` operator.

Create a collection `cakeFlavors`:

```javascript
db.cakeFlavors.insertMany( [
   { _id: 1, flavor: "chocolate" },
   { _id: 2, flavor: "strawberry" },
   { _id: 3, flavor: "cherry" }
] )
```

The following example defines a `targetFlavor` variable in `let` and
uses the variable to retrieve the chocolate cake flavor:

```javascript
db.cakeFlavors.runCommand( {
   find: db.cakeFlavors.getName(),
   filter: { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   let : { targetFlavor: "chocolate" }
} )
```
