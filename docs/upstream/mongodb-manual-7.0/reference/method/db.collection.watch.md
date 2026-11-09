<!-- Converted from reference/method/db.collection.watch.txt (reStructuredText). Includes are inlined. -->

# db.collection.watch() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `aggregate` command with the.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.watch( pipeline, options )`**

   `$changeStream` aggregation stage

*For replica sets and sharded clusters only*

Opens a change stream cursor on the 
collection.

:returns:
   A cursor that remains open as long as a connection to the
   MongoDB deployment remains open *and* the collection exists.
   See /reference/change-events for examples of change
   event documents.

### Parameters

* - Parameter
  - Type
  - Description

* - `pipeline`
  - array
  - Optional. An aggregation-pipeline consisting of one
    or more of the following aggregation stages:

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
    `watch()`.

## Fields

The `options` document can contain the following fields and values:

* - Field
  - Type
  - Description

* - `resumeAfter`
  - document
  - Optional. Directs `watch` to attempt resuming
    notifications starting after the operation specified in the resume
    token. 

    Each change stream event document includes a resume token as the
    `_id` field. Pass the *entire* `_id` field of the change event
    document that represents the operation you want to resume after.

    `resumeAfter` is mutually exclusive with `startAfter` and
    `startAtOperationTime`.

* - `startAfter`
  - document
  - Optional. Directs `watch` to attempt starting a new
    change stream after the operation specified in the resume token.
    Allows notifications to resume after an invalidate event.

    Each change stream event document includes a resume token as the
    `_id` field. Pass the *entire* `_id` field of the change event
    document that represents the operation you want to resume after.

    `startAfter` is mutually exclusive with `resumeAfter` and
    `startAtOperationTime`.

* - `fullDocument`   
  - string
  - Optional. By default, `watch()` returns the delta of
    those fields modified by an update operation, instead of the entire
    updated document.

    Set `fullDocument` to `"updateLookup"` to direct
    `watch()` to look up the most current 
    majority-committed version of the updated document.
    `watch()` returns a `fullDocument` field with
    the document lookup in addition to the `updateDescription` delta.

    Starting in MongoDB 6.0, you can set `fullDocument` to:

    - `"whenAvailable"` to output the document post-image, if available,
      after the document was inserted, replaced, or updated.

    - `"required"` to output the document post-image after the document
      was inserted, replaced, or updated. Raises an error if the post-image
      is not available.

* - `fullDocumentBeforeChange`   
  - string
  - Optional.

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
  - Optional. The maximum number of documents that can be returned in each batch of
    a change stream. By default, `watch()`  has an initial
    batch size of the lesser of `101` documents or 16 mebibytes (MiB) worth of
    documents. Subsequent batches have a maximum size of 16 mebibytes.This option
    can enforce a smaller limit than 16 MiB, but not a larger one. When set, the
    `batchSize` is the lesser of `batchSize` documents or 16 MiB worth of
    documents.

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

    Defaults to `simple` binary comparison if omitted.

* - `showExpandedEvents`
  - boolean 
  - Optional. Starting in MongoDB 6.0, change streams support change 
    notifications for DDL events, like the createIndexes 
    and dropIndexes events. To include 
    expanded events in a change stream, create the change stream cursor 
    using the `showExpandedEvents` option.

    **New in version:** 6.0

* - `startAtOperationTime`
  - Timestamp
  - Optional. The starting point for the change stream. If the specified starting
    point is in the past, it must be in the time range of the oplog. To
    check the time range of the oplog, see
    `rs.printReplicationInfo()`.

    `startAtOperationTime` is mutually exclusive with `resumeAfter`
    and `startAfter`.

**See also:**

`db.watch()` and `Mongo.watch()`

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

`db.collection.watch()` is available for replica set and
sharded cluster deployments :

- For a replica set, you can issue `db.collection.watch()` on
  any data-bearing member.

- For a sharded cluster, you must issue `db.collection.watch()`
  on a `mongos` instance.

### Storage Engine

You can only use `db.collection.watch()` with the Wired
Tiger storage engine.

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

- `db.collection.watch()` only notifies on data changes that have
  persisted to a majority of data-bearing members.

- .. include:: /includes/extracts/changestream-cursor-open.rst

### Resumability

Unlike the MongoDB `Drivers`, `mongosh` does
not automatically attempt to resume a change stream cursor after an
error. The MongoDB drivers make *one* attempt to automatically resume
a change stream cursor after certain errors.

`db.collection.watch()` uses information stored in the oplog to produce the
change event description and generate a resume token associated to
that operation. If the operation identified by the resume token
passed to the `resumeAfter` or `startAfter` option has already
dropped off the oplog, `db.collection.watch()` cannot resume the
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
the collection resource. That is, a user must
have a role that grants the following privilege:

```javascript
{ resource: { db: <dbname>, collection: <collection> }, actions: [ "find", "changeStream" ] }
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

## Examples

### Open a Change Stream

The following operation opens a change stream cursor against the 
`data.sensors` collection:

```javascript
watchCursor = db.getSiblingDB("data").sensors.watch()
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

### Change Stream with Full Document Update Lookup

**Warning:**

For situations involving rapid deletions or traffic spikes, configuring
`fullDocument: "updateLookup"` with a `$match` filter can cause
'Resume Token Not Found' errors. This occurs when a document deletion causes
the `fullDocument` field to return a null value, because there is no
matching document, which then prevents the change stream from finding 
the resume token.

Instead, use Pre- and Post-Images with ``fullDocumentBeforeChange:
"whenAvailable"` and `fullDocument: "whenAvailable"``. See the Change Streams with Document Pre- and Post-Images section.

Set the `fullDocument` option to `"updateLookup"` to direct the
change stream cursor to lookup the most current majority-committed
version of the document associated to an update change stream event.

The following operation opens a change stream cursor against
the `data.sensors` collection using the 
`fullDocument : "updateLookup"` option.

```javascript
watchCursor = db.getSiblingDB("data").sensors.watch(
   [],
   { fullDocument : "updateLookup" }
)
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

For any update operation, the change event returns the result of the
document lookup in the `fullDocument` field.

For an example of the full document update output, see  change
stream update event.

For complete documentation on change stream output, see
change-stream-output.

### Change Streams with Document Pre- and Post-Images

Starting in MongoDB 6.0, you can use change stream events to output the version of a document before and
after changes (the document pre- and post-images):

- The pre-image is the document before it was replaced, updated, or
  deleted. There is no pre-image for an inserted document.

- The post-image is the document after it was inserted, replaced, or
  updated. There is no post-image for a deleted document.

- Enable `changeStreamPreAndPostImages` for a collection using
  `db.createCollection()`, `create`, or
  `collMod`. For example, when using the `collMod` command: 

  ```javascript
  db.runCommand( { 
     collMod: <collection>,
     changeStreamPreAndPostImages: { enabled: true }
  } )
  ```

To check the current `changeStreamPreAndPostImages` setting for a
collection, run `db.getCollectionInfos()`:

```javascript
db.getCollectionInfos( {
  name: "<collection>"
} )[0].options.changeStreamPreAndPostImages
```

Output:

```javascript
{ changeStreamPreAndPostImages: { enabled: true } }
```

Pre- and post-images are not available for a change stream event if the images were:

- Not enabled on the collection at the time of a document update or
  delete operation.

- Removed after the pre- and post-image retention time set in
  `expireAfterSeconds`.

  - The following example sets `expireAfterSeconds` to `100`
    seconds on an entire cluster:

    ```javascript
    use admin
    db.runCommand( {
       setClusterParameter:
          { changeStreamOptions: {
             preAndPostImages: { expireAfterSeconds: 100 }
          } }
    } )
    ```

    **Note:**

    The `setClusterParameter` command is not supported in MongoDB 
    Atlas clusters. For information on Atlas support for all commands, see 
    unsupported-commands.

  - The following example returns the current `changeStreamOptions`
    settings, including `expireAfterSeconds`:

    ```javascript
    db.adminCommand( { getClusterParameter: "changeStreamOptions" } )
    ```

  - Setting `expireAfterSeconds` to `off` uses the default retention
    policy: pre- and post-images are retained until the corresponding
    change stream events are removed from the oplog.

  - If a change stream event is removed from the oplog, then the
    corresponding pre- and post-images are also deleted regardless of
    the `expireAfterSeconds` pre- and post-image retention time.

Additional considerations:

- Enabling pre- and post-images consumes storage space and adds
  processing time. Only enable pre- and post-images if you need them.

- Limit the change stream event size to less than 16 mebibytes. To limit
  the event size, you can:

  - Limit the document size to 8 megabytes. You can request pre- and
    post-images simultaneously in the change stream output if other change stream event fields like
    `updateDescription` are not large.

  - Request only post-images in the change stream output for documents
    up to 16 mebibytes if other change stream event fields like
    `updateDescription` are not large.

  - Request only pre-images in the change stream output for documents up
    to 16 mebibytes if:

    - document updates affect only a small fraction of the document
      structure or content, *and*

    - do not cause a `replace` change event. A `replace` event
      always includes the post-image.

- To request a pre-image, you set `fullDocumentBeforeChange` to
  `required` or `whenAvailable` in `db.collection.watch()`.
  To request a post-image, you set `fullDocument` using the same
  method.

- Pre-images are written to the `config.system.preimages` collection.

  - The `config.system.preimages` collection may become large. To
    limit the collection size, you can set `expireAfterSeconds`
    time for the pre-images as shown earlier.

  - To monitor the size of `config.system.preimages`, connect to a
    shard node on a sharded cluster or a `mongod` node
    on a replica set. Then, run the following commands:

    ```javascript
    use config
    db.system.preimages.totalSize()
    db.system.preimages.stats()
    ```

    **Note:**

    You must have the `collStats` privilege action on the
    `config.system.preimages` collection to run these commands.

    To run these commands on an MongoDB Atlas deployment, you must have
    the `atlasAdmin` role.

  - Pre-images are removed asynchronously by a background process.

**Important:** Backward-Incompatible Feature

Starting in MongoDB 6.0, if you are using document pre- and post-images
for change streams, you must disable
changeStreamPreAndPostImages for each collection using
the `collMod` command before you can downgrade to an earlier
MongoDB version.

**See also:**

- For change stream events and output, see
  change-stream-output.

- To watch a collection for changes, see
  `db.collection.watch`.

- For complete examples with the change stream output, see
  db.collection.watch-change-streams-pre-and-post-images-example.

#### Create Collection

Create a `temperatureSensor` collection that has
changeStreamPreAndPostImages enabled:

```javascript
db.createCollection(
   "temperatureSensor",
   { changeStreamPreAndPostImages: { enabled: true } }
)
```

Populate the `temperatureSensor` collection with temperature readings:

```javascript
db.temperatureSensor.insertMany( [
   { "_id" : 0, "reading" : 26.1 },
   { "_id" : 1, "reading" : 25.9 },
   { "_id" : 2, "reading" : 24.3 },
   { "_id" : 3, "reading" : 22.4 },
   { "_id" : 4, "reading" : 24.6 }
] )
```

The following sections show change stream examples for document pre- and
post-images that use the `temperatureSensor` collection.

#### Change Stream with Document Pre-Image

You use the `fullDocumentBeforeChange: "whenAvailable"` setting to
output the document pre-image, if available. The pre-image is the
document before it was replaced, updated, or deleted. There is no
pre-image for an inserted document.

The following example creates a change stream cursor for the
`temperatureSensor` collection using ``fullDocumentBeforeChange:
"whenAvailable"``:

```javascript
watchCursorFullDocumentBeforeChange = db.temperatureSensor.watch(
   [],
   { fullDocumentBeforeChange: "whenAvailable" }
)
```

The following example uses the cursor to check for new change stream
events:

```javascript
while ( !watchCursorFullDocumentBeforeChange.isClosed() ) {
   if ( watchCursorFullDocumentBeforeChange.hasNext() ) {
      printjson( watchCursorFullDocumentBeforeChange.next() );
   }
}
```

In the example:

- The `while` loop runs until the cursor is closed.

- `hasNext()` returns `true` if the cursor has
  documents.

The following example updates the `reading` field for a
`temperatureSensor` document:

```javascript
db.temperatureSensor.updateOne(
   { _id: 2 },
   { $set: { reading: 22.1 } }
)
```

After the `temperatureSensor` document is updated, the change event
outputs the document pre-image in the `fullDocumentBeforeChange`
field. The pre-image contains the `temperatureSensor` document
`reading` field before it was updated. For example:

```javascript
{
   "_id" : {
      "_data" : "82624B21...",
      "_typeBits" : BinData(0,"QA==")
   },
   "operationType" : "update",
   "clusterTime" : Timestamp(1649090957, 1),
   "ns" : {
      "db" : "test",
      "coll" : "temperatureSensor"
   },
   "documentKey" : {
      "_id" : 2
   },
   "updateDescription" : {
      "updatedFields" : {
         "reading" : 22.1
      },
      "removedFields" : [ ],
      "truncatedArrays" : [ ]
   },
   "fullDocumentBeforeChange" : {
      "_id" : 2,
      "reading" : 24.3
   }
}
```

**See also:**

- For document update output details, see change
  stream update events.

- For change stream output details, see change-stream-output.

#### Change Stream with Document Post-Image

You use the `fullDocument: "whenAvailable"` setting to output the
document post-image, if available. The post-image is the document after
it was inserted, replaced, or updated. There is no post-image for a
deleted document.

The following example creates a change stream cursor for the
`temperatureSensor` collection using ``fullDocument:
"whenAvailable"``:

```javascript
watchCursorFullDocument = db.temperatureSensor.watch(
   [],
   { fullDocument: "whenAvailable" }
)
```

The following example uses the cursor to check for new change stream
events:

```javascript
while ( !watchCursorFullDocument.isClosed() ) {
   if ( watchCursorFullDocument.hasNext() ) {
      printjson( watchCursorFullDocument.next() );
   }
}
```

In the example:

- The `while` loop runs until the cursor is closed.

- `hasNext()` returns `true` if the cursor has
  documents.

The following example updates the `reading` field for a
`temperatureSensor` document:

```javascript
db.temperatureSensor.updateOne(
   { _id: 1 },
   { $set: { reading: 29.5 } }
)
```

After the `temperatureSensor` document is updated, the change event
outputs the document post-image in the `fullDocument` field. The
post-image contains the `temperatureSensor` document `reading` field
after it was updated. For example:

```javascript
{
   "_id" : {
      "_data" : "8262474D...",
      "_typeBits" : BinData(0,"QA==")
   },
   "operationType" : "update",
   "clusterTime" : Timestamp(1648840090, 1),
   "fullDocument" : {
      "_id" : 1,
      "reading" : 29.5
   },
   "ns" : {
      "db" : "test",
      "coll" : "temperatureSensor"
   },
   "documentKey" : {
      "_id" : 1
   },
   "updateDescription" : {
      "updatedFields" : {
         "reading" : 29.5
      },
      "removedFields" : [ ],
      "truncatedArrays" : [ ]
   }
}
```

**See also:**

- For document update output details, see change
  stream update events.

- For change stream output details, see change-stream-output.

### Change Stream with Aggregation Pipeline Filter

**Note:**

Starting in MongoDB 4.2, change streams will throw an exception if
the change stream aggregation pipeline modifies an event's _id field.

The following operation opens a change stream cursor against the 
`data.sensors` collection using an aggregation pipeline to
filter only `insert` events:

```javascript
watchCursor = db.getSiblingDB("data").sensors.watch(
   [
      { $match : {"operationType" : "insert" } }
   ]
)
```

Iterate the cursor to check for new events. Use the
`cursor.isClosed()` method with the `cursor.hasNext()`
method to ensure the loop only exits if the change stream cursor is
closed *and* there are no objects remaining in the latest batch:

```javascript
while (!watchCursor.isClosed()){
   if (watchCursor.hasNext()){
      printjson(watchCursor.next());
   }
}
```

The change stream cursor only returns change events where the 
`operationType` is `insert`. For complete documentation on
change stream output, see change-stream-output. 

### Resuming a Change Stream

Every  document returned by a change stream cursor includes a resume
token as the `_id` field. To resume a change stream, pass the entire
`_id` document of the change event you want to resume from to
either the `resumeAfter` or `startAfter` option of
`watch()`.

The following operation resumes a change stream cursor against the 
`data.sensors` collection using a resume token. This
assumes that the operation that generated the resume token has not
rolled off the cluster's oplog. 

```javascript
let watchCursor = db.getSiblingDB("data").sensors.watch();
let firstChange;

while (!watchCursor.isClosed()) {
   if (watchCursor.hasNext()) {
     firstChange = watchCursor.next();
     break;
   }
}

watchCursor.close();

let resumeToken = firstChange._id;

resumedWatchCursor = db.getSiblingDB("data").sensors.watch(
[],
   { resumeAfter : resumeToken }
)
```

Iterate the cursor to check for new events. Use the
`cursor.isClosed()` method with the `cursor.hasNext()`
method to ensure the loop only exits if the change stream cursor is
closed *and* there are no objects remaining in the latest batch:

```javascript
while (!resumedWatchCursor.isClosed()){
   if (resumedWatchCursor.hasNext()){
      print(resumedWatchCursor.next());
   }
}
```

See change-stream-resume for complete documentation on
resuming a change stream.
