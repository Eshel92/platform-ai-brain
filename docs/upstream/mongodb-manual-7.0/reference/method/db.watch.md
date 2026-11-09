<!-- Converted from reference/method/db.watch.txt (reStructuredText). Includes are inlined. -->

# db.watch() (mongosh method)

## Definition

**`db.watch( pipeline, options )`**

*For replica sets and sharded clusters only*

Opens a change stream cursor for a database
to report on all its non-`system` collections.

* - Parameter
  - Type
  - Description

* - `pipeline`
  - array
  - Optional. An aggregation-pipeline consisting
    of one or more of the following aggregation stages:

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
    `db.watch()`.

The `options` document can contain the following fields and values:

* - Field

  - Type

  - Description

* - `resumeAfter`

  - document

  - .. include:: /includes/change-stream/resume-after-description.rst

* - `startAfter`

  - document

  - .. include:: /includes/change-stream/start-after-description.rst

* - `fullDocument`

  - string

  - Optional. By default, `db.watch()` returns the delta of
    those fields modified by an update operation, instead of the entire
    updated document.

    Set `fullDocument` to `"updateLookup"` to direct
    `db.watch()` to look up the most current 
    majority-committed version of the updated document.
    `db.watch()` returns a `fullDocument` field with
    the document lookup in addition to the `updateDescription` delta.

    Starting in MongoDB 6.0, you can set `fullDocument` to:

    - `"whenAvailable"` to output the document post-image, if available,
      after the document was inserted, replaced, or updated.

    - `"required"` to output the document post-image after the document
      was inserted, replaced, or updated. Raises an error if the post-image
      is not available.

* - `fullDocumentBeforeChange`   
  - string
  - Optional. Default is `"off"`.

    Starting in MongoDB 6.0, you can use the new
    `fullDocumentBeforeChange` field and set it to:

    - `"whenAvailable"` to output the document pre-image, if available,
      before the document was replaced, updated, or deleted.

    - `"required"` to output the document pre-image before the document
      was replaced, updated, or deleted. Raises an error if the pre-image
      is not available.

    - `"off"` to suppress the document pre-image. `"off"` is the
      default.

* - `batchSize`

  - int

  - Optional. Specifies the maximum number of change events to return in each
    batch of the response from the MongoDB cluster. 

    Has the same functionality as `cursor.batchSize()`.

* - `maxAwaitTimeMS`

  - int

  - Optional. The maximum amount of time in milliseconds the server waits for new
    data changes to report to the change stream cursor before returning an
    empty batch.

    Defaults to `1000` milliseconds.

* - `collation`

  - document

  - Optional. Pass a collation document 
    to specify a collation for the change stream cursor.

    If omitted, defaults to `simple` binary comparison.

* - `startAtOperationTime`

  - Timestamp

  - Optional. The starting point for the change stream. If the specified starting
    point is in the past, it must be in the time range of the oplog. To
    check the time range of the oplog, see
    `rs.printReplicationInfo()`.

    `startAtOperationTime` is mutually exclusive with `resumeAfter`
    and `startAfter`.

:returns:
   A cursor over the change event documents.
   See /reference/change-events for examples of change
   event documents.

**See also:**

`db.collection.watch()` and `Mongo.watch()`

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

## Availability

### Deployment

`db.watch()` is available for replica sets and sharded
clusters:

- For a replica set, you can issue `db.watch()` on any
  data-bearing member.

- For a sharded cluster, you must issue `db.watch()` on a
  `mongos` instance.

### Storage Engine

You can only use `db.watch()` with the Wired Tiger
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

- You cannot run `db.watch()` on the `admin`, `local`, or
  `config` database.

- `db.watch()` only notifies on data changes that have
  persisted to a majority of data-bearing members.

- .. include:: /includes/extracts/changestream-cursor-open.rst

- You can run `db.watch()` for a database that does not exist.
  However, once the database is created and you drop the database, the
  change stream cursor closes.

### Resumability

Unlike the MongoDB `Drivers`, `mongosh` does
not automatically attempt to resume a change stream cursor after an
error. The MongoDB drivers make *one* attempt to automatically resume
a change stream cursor after certain errors.

`db.watch()` uses information stored in the oplog to produce the
change event description and generate a resume token associated to
that operation. If the operation identified by the resume token
passed to the `resumeAfter` or `startAfter` option has already
dropped off the oplog, `db.watch()` cannot resume the
change stream.

See change-stream-resume for more information on
resuming a change stream.

**Note:**

- .. include:: /includes/extracts/changestream-invalid-events.rst

- .. include:: /includes/extracts/changestream-remove-shard.rst

**Note:**

You cannot use `resumeAfter` to resume a change stream after an
invalidate event (for example, a collection
drop or rename) closes the stream. Instead, you can use 
startAfter to start a new change
stream after an invalidate event.

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

## Access Control

When running with access control, the user must have the
`find` and `changeStream` privilege actions on
the database resource. That is, a user must
have a role that grants the following privilege:

```javascript
{ resource: { db: <dbname>, collection: "" }, actions: [ "find", "changeStream"] }
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
change stream cursor on the `hr` database. The returned cursor
reports on data changes to all the non-`system` collections in that
database.

```javascript
watchCursor = db.getSiblingDB("hr").watch()
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
