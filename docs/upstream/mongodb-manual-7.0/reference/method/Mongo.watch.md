<!-- Converted from reference/method/Mongo.watch.txt (reStructuredText). Includes are inlined. -->

# Mongo.watch() (mongosh method)

## Definition

**`Mongo.watch( pipeline, options )`**

*For replica sets and sharded clusters only*

Opens a change stream cursor for a replica
set or a sharded cluster to report on all its non-`system`
collections across its databases, with the exception of the
`admin`, `local`, and the `config` databases.

* - Parameter
  - Type
  - Description

* - `pipeline`
  - array
  - Optional. An aggregation-pipeline consisting of one or
    more of the following aggregation stages:

    - `$addFields`
    - `$match`
    - `$project`
    - `$replaceRoot`
    - `$replaceWith` 
    - `$redact`
    - `$set` 
    - `$unset` 

    Specify a pipeline to filter/modify the change events output.

    Starting in MongoDB 4.2, change streams will throw an exception if
    the change stream aggregation pipeline modifies an event's _id field.

* - `options`
  - document
  - Optional. Additional options that modify the behavior of
    `Mongo.watch()`.

The `options` document can contain the following fields and values:

| Field | Type | Description |
|---|---|---|
| `resumeAfter` | document | Optional. Directs `Mongo.watch()` to attempt resuming notifications starting after the operation specified in the resume token. Each change stream event document includes a resume token as the `_id` field. Pass the *entire* `_id` field of the change event document that represents the operation you want to resume after. `resumeAfter` is mutually exclusive with `startAfter` and `startAtOperationTime`. |
| `startAfter` | document | Optional. Directs `Mongo.watch()` to attempt starting a new change stream after the operation specified in the resume token. Allows notifications to resume after an invalidate event. Each change stream event document includes a resume token as the `_id` field. Pass the *entire* `_id` field of the change event document that represents the operation you want to resume after. `startAfter` is mutually exclusive with `resumeAfter` and `startAtOperationTime`. |
| `fullDocument` | string | Optional. By default, `Mongo.watch()` returns the delta of those fields modified by an update operation, instead of the entire updated document. Set `fullDocument` to `"updateLookup"` to direct `Mongo.watch()` to look up the most current majority-committed version of the updated document. `Mongo.watch()` returns a `fullDocument` field with the document lookup in addition to the `updateDescription` delta. |
| `batchSize` | int | Optional. Specifies the maximum number of change events to return in each batch of the response from the MongoDB cluster. Has the same functionality as `cursor.batchSize()`. |
| `maxAwaitTimeMS` | int | Optional. The maximum amount of time in milliseconds the server waits for new data changes to report to the change stream cursor before returning an empty batch. Defaults to `1000` milliseconds. |
| `collation` | document | Optional. Pass a collation document to specify collation for the change stream cursor. If omitted, defaults to `simple` binary comparison. |
| `startAtOperationTime` | Timestamp | Optional. The starting point for the change stream. If the specified starting point is in the past, it must be in the time range of the oplog. To check the time range of the oplog, see `rs.printReplicationInfo()`. `startAtOperationTime` is mutually exclusive with `resumeAfter` and `startAfter`. |

:returns:
   A cursor over the change event documents.
   See /reference/change-events for examples of change
   event documents.

**See also:**

`db.collection.watch()` and `db.watch()`

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Availability

### Deployment

`Mongo.watch()` is available for replica sets and sharded
clusters:

- For a replica set, you can issue `Mongo.watch()` on any
  data-bearing member.

- For a sharded cluster, you must issue `Mongo.watch()` on a
  `mongos` instance.

### Storage Engine

You can only use `Mongo.watch()` with the Wired Tiger
storage engine.

### Read Concern `majority` Support

Starting in MongoDB 4.2, change streams are
available regardless of the `"majority"` read concern
support; that is, read concern `majority` support can be either
enabled (default) or disabled
to use change streams.

In MongoDB 4.0 and earlier, change streams are
available only if `"majority"` read concern support is
enabled (default).

## Behavior

- `Mongo.watch()` only notifies on data changes that have
  persisted to a majority of data-bearing members.

- .. include:: /includes/extracts/changestream-cursor-open.rst

### Resumability

Unlike the MongoDB `Drivers`, `mongosh` does
not automatically attempt to resume a change stream cursor after an
error. The MongoDB drivers make *one* attempt to automatically resume
a change stream cursor after certain errors.

`Mongo.watch()` uses information stored in the oplog to produce the
change event description and generate a resume token associated to
that operation. If the operation identified by the resume token
passed to the `resumeAfter` or `startAfter` option has already
dropped off the oplog, `Mongo.watch()` cannot resume the
change stream.

See change-stream-resume for more information on
resuming a change stream.

**Note:**

- .. include:: /includes/extracts/changestream-invalid-events.rst

- .. include:: /includes/extracts/changestream-remove-shard.rst

**Note:** Resume Token

#### Hex Encoded Tokens

With hex-encoded string resume tokens, you can compare and sort the
resume tokens. You can use either BinData resume tokens or hex 
string resume tokens to resume a change stream.

New resume token formats introduced in a MongoDB version
cannot be consumed by earlier MongoDB versions.

#### Decode Resume Tokens

MongoDB provides a "snippet", an 
extension to `mongosh`, that decodes hex-encoded
resume tokens.

You can install and run the [resumetoken](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets/resumetoken)
snippet from `mongosh`:

```javascript
snippet install resumetoken
decodeResumeToken('<RESUME TOKEN>')
```

You can also run [resumetoken](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets/resumetoken)
from the command line (without using `mongosh`) if `npm`
is installed on your system:

```javascript
npx mongodb-resumetoken-decoder <RESUME TOKEN>
```

See the following for more details on:

- [resumetoken](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets/resumetoken)
- using snippets in `mongosh`.

### Full Document Lookup of Update Operations

By default, the change stream cursor returns
specific field changes/deltas for update operations. You can also
configure the change stream to look up and return the current
majority-committed version of the changed document. Depending on other
write operations that may have occurred between the update and the
lookup, the returned document may differ significantly from the
document at the time of the update.

Depending on the number of changes applied during the update operation
and the size of the full document, there is a risk that the size of the
change event document for an update operation is greater than the 16MB
BSON document limit. If this occurs, the server closes the change stream
cursor and returns an error.

### Availability

Starting in MongoDB 4.2, change streams are
available regardless of the `"majority"` read concern
support; that is, read concern `majority` support can be either
enabled (default) or disabled
to use change streams.

In MongoDB 4.0 and earlier, change streams are
available only if `"majority"` read concern support is
enabled (default).

## Access Control

When running with access control, the user must have the
`find` and `changeStream` privilege actions on
all non-systems collections across all
databases.. That is, a user must
have a role that grants the following privilege:

```javascript
{ resource: { db: "", collection: "" }, actions: [ "find", "changeStream" ] }
```

The built-in `read` role provides the appropriate
privileges.

## Cursor Iteration

MongoDB provides multiple ways to iterate on a cursor. 

The `cursor.hasNext()` method blocks and waits for the next
event. To monitor the `watchCursor` cursor and iterate over the
events, use `hasNext()` like this:

```javascript
while (!watchCursor.isClosed()) {
   if (watchCursor.hasNext()) {
     firstChange = watchCursor.next();
     break;
   }
}
```

The `cursor.tryNext()` method is non-blocking. To monitor
the `watchCursor` cursor and iterate over the events, use
`tryNext()` like this:

```javascript
while (!watchCursor.isClosed()) {
  let next = watchCursor.tryNext()
  while (next !== null) {
    printjson(next);
    next = watchCursor.tryNext()
  }
}
```

## Example

The following operation in `mongosh` opens a
change stream cursor on a replica set. The returned cursor reports on
data changes to all the non-`system` collections across all databases
except for the `admin`, `local`, and the `config` databases.

```javascript
watchCursor = db.getMongo().watch()
```

Iterate the cursor to check for new events. Use the
`cursor.isClosed()` method with the `cursor.tryNext()`
method to ensure the loop only exits if the change stream cursor is
closed *and* there are no objects remaining in the latest batch:

```javascript
while (!watchCursor.isClosed()) {
  let next = watchCursor.tryNext()
  while (next !== null) {
    printjson(next);
    next = watchCursor.tryNext()
  }
}
```

For complete documentation on change stream output, see
change-stream-output.

**Note:**

You cannot use `isExhausted()` with change streams.
