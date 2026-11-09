<!-- Converted from reference/operator/aggregation/changeStream.txt (reStructuredText). Includes are inlined. -->

# $changeStream (aggregation stage)

## Definition

**`$changeStream`**

Returns a Change Stream cursor on a collection, a database,
or an entire cluster. Must be used as the first stage in an aggregation pipeline.

The `$changeStream` stage has the following syntax:

```text
{
  $changeStream: {
    allChangesForCluster: <boolean>,
    fullDocument: <string>,
    fullDocumentBeforeChange: <string>,
    resumeAfter: <document>
    showExpandedEvents: <boolean>,
    startAfter: <document>
    startAtOperationTime: <timestamp>
  }
}
```

* - Parameter
  - Description

* - `allChangesForCluster`
  - Optional: Sets whether the change stream should include all changes
    in the cluster. May only be opened on the `admin` database.

* - `fullDocument`
  - Optional: Specifies whether change notifications include a copy of the
    full document when modified by `update` operations.

    * `default`: Change notifications do not include the full document
      for `update` operations.

    * `required`: Change notifications includes a copy of the modified
      document as it appeared immediately after the change. If the
      document cannot be found, the change stream throws an error.

      To use this option, you must first use the `collMod`
      command to enable the `changeStreamPreAndPostImages` option.

      **New in version:** 6.0

    * `updateLookup`: Change notifications includes a copy of the
      document modified by the change.  This document is the current
      majority-committed document or `null` if it no longer exists.

    * `whenAvailable`: Change notification includes a copy of the
      modified document as it appeared immediately after the change or
      `null` if the document is unavailable.

      To use this option, you must first use the `collMod`
      command to enable the `changeStreamPreAndPostImages` option.

      **New in version:** 6.0

    In the case of partial updates, the change notification also
    provides a description of the change.

* - `fullDocumentBeforeChange`
  - Include the full document from before the change.
    This field accepts the following values:

    * `off`: Disables inclusion of the document from before the change.
    * `whenAvailable`: Includes document from before the change.
      The query does not fail if the unmodified document is not available.
    * `required`: Includes document from before the change. The query
      fails if the unmodified document is not available.

* - `resumeAfter`
  - .. include:: /includes/change-stream/resume-after-description.rst

* - `showExpandedEvents`
  - Specifies whether to include additional change events, such as
    such as DDL and index operations.

    **New in version:** 6.0

* - `startAfter`
  - .. include:: /includes/change-stream/start-after-description.rst

* - `startAtOperationTime`
  - Specifies a time as the logical starting point for the change stream.
    Cannot be used with `resumeAfter` or `startAfter` fields.

## Stable API Support

Change streams are included in Stable API V1.
However, the showExpandedEvents
option is not included in Stable API V1.

## Examples

**shell:**

To create a change stream cursor using the aggregation stage, run
the `aggregate` command.

```javascript
var cur = db.names.aggregate( [
   { $changeStream: {} }
] )
```

To open the cursor, run `cur`.

When the change stream detects a change, the `next()` method returns
a change event notification. For example, after running `cur.next()`,
MongoDB returns a document similar to the following:

```json
{
   "_id": {
      _data: "8262E2EE54000000022B022C0100296E5A100448E5E3DD01364019AE8FE8C6859527E046645F6964006462E2EE54C8756C0D5CF6F0720004"
   },
   "operationType": "insert",
   "clusterTime": Timestamp({ t: 1659039316, i: 2 }),
   "wallTime": ISODate("2022-07-28T20:15:16.148Z"),
   "fullDocument": {
      "_id": ObjectId("62e2ee54c8756c0d5cf6f072"),
      "name": "Walker Percy"
   },
   "ns": {
      "db": "test",
      "coll": "names"
   },
   "documentKey": { _id: ObjectId("62e2ee54c8756c0d5cf6f072") }
}
```

**csharp:**

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/method-intro.rst)

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .ChangeStream();
```

You can use a [ChangeStreamStageOptions](https://mongodb.github.io/mongo-csharp-driver/{+csharp-driver-version+}.0/api/MongoDB.Driver/MongoDB.Driver.ChangeStreamStageOptions.html)
object to customize the behavior of the change stream.
The following example performs the same `$changeStream` operation as the previous
example, but specifies the following options:

- The `FullDocument` option specifies that change notifications don't include a
  copy of the full document when modified by update operations.
- The `StartAtOperationTime` option specifies the logical starting point for the
  change stream.

```csharp
var changeStreamOptions = new ChangeStreamStageOptions()
{
    FullDocument = ChangeStreamFullDocumentOption.Default,
    StartAtOperationTime = new BsonTimestamp(300),
};

var pipeline = new EmptyPipelineDefinition<Movie>()
    .ChangeStream(changeStreamOptions);
```

**Note:** Prefer the `Watch()` Method

Where possible, use the `IMongoCollection<TDocument>.Watch()` method instead
of this aggregation stage. Use the `ChangeStream()` method
only if subsequent stages project away the resume token (`_id`) or if you don't
want the resulting cursor to automatically resume.

**nodejs:**

You can use both the `watch()` method and the `aggregate()` method to
execute a `$changeStream` operation. `$changeStream` returns a
`ChangeStreamCursor` when you pass the aggregation pipeline to the
[watch()](https://mongodb.github.io/node-mongodb-native/Next/classes/Collection.html#watch) method on a
MongoDB `Collection` object. `$changeStream` returns an
`AggregationCursor` when you pass the aggregation pipeline to the
[aggregate()](https://mongodb.github.io/node-mongodb-native/Next/classes/Collection.html#aggregate)
method.

**Important:** `$changeStream` Resumability

If you pass a change stream to the [aggregate()](https://mongodb.github.io/node-mongodb-native/Next/classes/Collection.html#aggregate) method, the
change stream can not resume. A change stream only resumes if you pass
it to the [watch()](https://mongodb.github.io/node-mongodb-native/Next/classes/Collection.html#watch)
method. To learn more about resumability, see Resume a Change
Stream.

The following example creates and executes a pipeline that returns a
`ChangeStreamCursor`:

```javascript
const pipeline = [{ $changeStream: {} }];

const changeStream = collection.watch(pipeline);
return changeStream;
```

You can use a [ChangeStreamOptions](https://mongodb.github.io/node-mongodb-native/Next/interfaces/ChangeStreamOptions.html)
object to customize the behavior of the change stream.
The following example performs the same `$changeStream` operation as the previous
example, but specifies the following options:

- The `fullDocument` option specifies that if an update operation
  modifies a document, the change notifications include a copy of the full
  document.
- The `startAtOperationTime` option specifies the logical starting point
  for the change stream. 

```javascript
const pipeline = [
  {
    $changeStream: {
      fullDocument: 'updateLookup',
      startAtOperationTime: 3000
    }
  }
];

const changeStream = collection.watch(pipeline);
return changeStream;
```

## Learn More

For more information on change stream notifications, see Change Events.

To learn more about related pipeline stages, see the
`$changeStreamSplitLargeEvent` guide.
