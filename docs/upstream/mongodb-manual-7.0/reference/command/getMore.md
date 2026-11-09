<!-- Converted from reference/command/getMore.txt (reStructuredText). Includes are inlined. -->

# getMore (database command)

## Definition

**`getMore`**

Use with commands that return a cursor, such as `find`
and `aggregate`, to return the next document batches
from a cursor.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

The command has the following syntax:

```javascript
db.runCommand(
   {
      getMore: <long>,
      collection: <string>,
      batchSize: <int>,
      maxTimeMS: <int>,
      comment: <any>
   }
)
```

## Command Fields

The command accepts the following fields:

* - Field
  - Type
  - Description

* - `getMore`
  - long
  - The cursor identifier.

* - `collection`
  - string
  - The name of the collection over which the cursor is operating.

* - `batchSize`
  - positive integer
  - Optional. The maximum number of documents returned for each batch.

    If `batchSize` is not set, `getMore` returns up to 16
    mebibytes (MiB) for each batch. If `batchSize` is set,
    `getMore` returns the lesser of `batchSize` documents
    or 16 MiB.

* - `maxTimeMS`
  - non-negative integer
  - Optional. 

    Specifies how long the server waits for new documents matching a
    tailable cursor query on
    a capped collection.
    `maxTimeMS` on a `getMore` for a tailable `awaitData`
    cursor is equivalent to `maxAwaitTimeMS()`.

    Drivers set this value only for tailable cursors on capped
    collections where `awaitData` is `true`. Otherwise, the
    command that creates the cursor sets `maxTimeMS` as the
    cumulative time limit for the initial operation and all
    subsequent `getMore` operations. For tailable cursors with `awaitData` set to `true`, 
    the following is true:

    - If no value is provided, the wait time defaults to `1` (1000 milliseconds).
    - `maxTimeMS` on `getMore` specifies the maximum amount of time 
      MongoDB waits for new documents to be inserted into the capped 
      collection for that specific `getMore` command. 
    - `maxTimeMS` is set individually by the driver for each call to `getMore`.     

    MongoDB terminates operations that exceed their time limit using
    the same mechanism as `db.killOp()`, but only at
    designated interrupt points.

    - You cannot set `maxTimeMS` when calling `getMore` on a
      non-tailable cursor. Instead, set it using
      `maxTimeMS()` when you create the cursor.
    - To use `getMore` with `maxTimeMS` on a tailable cursor, 
      enable `awaitData` when you create the cursor using `cursor.tailable()`.
    - Setting `maxTimeMS` on the command that creates a cursor only
      sets the time limit for that operation. Use `getMore` to set
      a limit on further operations.
    - You can set or omit `maxTimeMS` for each call to 
      `getMore`, and you don't have to use the same value.
    - For a tailable cursor, a timeout on `getMore` retains the
      documents accumulated before the timeout occurred in the
      cursor. For a non-tailable cursor, a timeout raises an error.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

    If omitted, `getMore` inherits any `comment` set on the
    originating `find` or `aggregate` command.

## Output

The command returns a document that contains the cursor information
and the next batch.

For example, running `getMore` on a cursor created by a 
`find` operation on a sharded cluster returns a document 
similar to this output:

```javascript
{
   "cursor" : {
      "id" : Long("678960441858272731"),
      "ns" : "test.contacts",
      "nextBatch" : [
         {
            "_id" : ObjectId("5e8e501e1a32d227f9085857"),
            "zipcode" : "220000"
         }
      ],
      "partialResultsReturned" : true,
      "postBatchResumeToken": "< Resume Token >"
   },
   "ok" : 1,
   "operationTime" : Timestamp(1586385239, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1586385239, 2),
      "signature" : {
         "hash" : BinData(0,"lLjejeW6AQGReR9x1PD8xU+tP+A="),
         "keyId" : Long("6813467763969884181")
      }
   }
}
```

| Field | Description |
|---|---|
| `cursor` | Contains the cursor information, including the cursor ID and the `nextBatch` of documents. If `find` (or subsequent `getMore` commands) returns partial results because the queried shard(s) aren't available, the find output includes a `partialResultsReturned` indicator field. If the queried shards are available for the initial `find` command, but one or more shards become unavailable for subsequent `getMore` commands, only the `getMore` commands that run while the shards aren't available include `partialResultsReturned` in their output. The `postBatchResumeToken` field can be used with the `$changeStream` pipeline to start or resume a change stream from this point. |
| `"ok"` | Indicates whether the command has succeeded (`1`) or failed (`0`). |

In addition to these fields, the `db.runCommand()` response
includes the following information for replica sets and sharded 
clusters:

- `$clusterTime`
  
- `operationTime`

See db.runCommand() Response for details.

## Behavior

### Access Control

If authentication is enabled, you can 
only run `getMore` against cursors you created.

### Sessions

For cursors created inside a session, you cannot call
`getMore` outside the session.

For cursors created outside a session, you cannot call
`getMore` inside a session.

#### Transactions

For multi-document transactions:

- For cursors created outside of a transaction, you cannot call
  `getMore` inside the transaction.

- For cursors created in a transaction, you cannot call
  `getMore` outside the transaction.

### Slow Queries

Starting in MongoDB 5.1, when a `getMore` command is logged
as a slow query, the queryHash and planCacheKey fields are added
to the slow query log message and the
profiler log message.

## Learn More

read-operations-cursors
