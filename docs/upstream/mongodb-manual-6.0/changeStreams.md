<!-- Converted from changeStreams.txt (reStructuredText). Includes are inlined. -->

# Change Streams

Change streams allow applications to access real-time data changes
without the prior complexity and risk of manually tailing the oplog.
Applications can use change streams to subscribe to all data changes on
a single collection, a database, or an entire deployment, and
immediately react to them. Because change streams use the aggregation
framework, applications can also filter for specific changes or
transform the notifications at will.

Starting in MongoDB 5.1, change streams are optimized, providing more
efficient resource utilization and faster execution of some aggregation
pipeline stages.

## Availability

Change streams are available for replica sets and
sharded clusters:

- **Storage Engine.** 

  The replica sets and sharded clusters must use the WiredTiger storage engine. Change streams can also be used
  on deployments that employ MongoDB's
  encryption-at-rest feature.
  
- **Replica Set Protocol Version.** 

  The replica sets and sharded clusters must use replica set protocol
  version 1 (`pv1`).

- **Read Concern "majority" Enablement.**  

  Starting in MongoDB 4.2, change streams are
  available regardless of the `"majority"` read concern
  support; that is, read concern `majority` support can be either
  enabled (default) or disabled
  to use change streams.

  In MongoDB 4.0 and earlier, change streams are
  available only if `"majority"` read concern support is
  enabled (default).

### Stable API Support

Change streams are included in Stable API V1.
However, the showExpandedEvents
option is not included in Stable API V1.

## Connect

Connections for a change stream can either use DNS seed lists
with the `+srv` connection option or by listing the servers individually
in the connection string.

If the driver loses the connection to a change stream or the connection goes
down, it attempts to reestablish a connection to the change stream through
another node in the cluster that has a matching 
read preference. If the driver cannot find
a node with the correct read preference, it throws an exception.

For more information, see Connection String URI Format.

## Watch a Collection, Database, or Deployment

You can open change streams against:

| Target | Description |
|---|---|
| A collection | You can open a change stream cursor for a single collection (except `system` collections, or any collections in the `admin`, `local`, and `config` databases). The examples on this page use the MongoDB drivers to open and work with a change stream cursor for a single collection. See also the `mongosh` method `db.collection.watch()`. |
| A database | You can open a change stream cursor for a single database (excluding `admin`, `local`, and `config` database) to watch for changes to all its non-system collections. For the MongoDB driver method, refer to your driver documentation. See also the `mongosh` method `db.watch()`. |
| A deployment | You can open a change stream cursor for a deployment (either a replica set or a sharded cluster) to watch for changes to all non-system collections across all databases except for `admin`, `local`, and `config`. For the MongoDB driver method, refer to your driver documentation. See also the `mongosh` method `Mongo.watch()`. |

**Note:** Change Stream Examples

The examples on this page use the MongoDB drivers to illustrate how
to open a change stream cursor for a collection and work with the
change stream cursor.

## Change Stream Performance Considerations

If the amount of active change streams opened against a database exceeds the 
connection pool size, you may 
experience notification latency. Each change stream uses a connection 
and a getMore 
operation on the change stream for the period of time that it waits for the next event. 
To avoid any latency issues, you should ensure that the pool size is greater than the 
number of opened change streams. For details see the maxPoolSize setting.

## Open A Change Stream

To open a change stream:

- For a replica set, you can issue the open change stream operation
  from any of the data-bearing members.

- For a sharded cluster, you must issue the open change stream
  operation from the `mongos`.

The following example opens a change stream for a collection and
iterates over the cursor to retrieve the change stream documents.
[#start-time]_

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

**python:**

The Python examples below assume that you have `connected to a MongoDB replica set and have accessed a database` that contains an `inventory` collection.

(Code example not available offline: /driver-examples/test_examples.py)

**motor:**

The examples below assume that you have [connected to a MongoDB replica set and have accessed a database](https://motor.readthedocs.io/en/stable/tutorial-asyncio.html#creating-a-client)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/test_examples_motor.py)

**java-sync:**

The Java examples below assume that you have [connected to a MongoDB replica set and have accessed a database](http://mongodb.github.io/mongo-java-driver/3.6/driver/tutorials/databases-collections/)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/DocumentationSamples.java)

**csharp:**

The C# examples below assume that you have [connected to a MongoDB replica set and have accessed a database](http://mongodb.github.io/mongo-csharp-driver/2.4/getting_started/quick_tour/#make-a-connection/)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/ChangeStreamExamples.cs)

**c:**

The C examples below assume that you have [connected to a MongoDB replica set and have accessed a database](https://www.mongodb.com/docs/languages/c/c-driver/current/databases-collections/#access-a-database)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**nodejs:**

The Node.js examples below assume that you have [connected to a MongoDB replica set and have accessed a database](https://mongodb.github.io/node-mongodb-native/api-generated/mongoclient.html#connect)
that contains an `inventory` collection.

The following example uses stream to process the change events.

(Code example not available offline: /driver-examples/node_changestreams.js)

Alternatively, you can also use iterator to process the change events:

(Code example not available offline: /driver-examples/node_changestreams.js)

**php:**

The examples below assume that you have [connected to a MongoDB replica set and have accessed a database](https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBClient__construct/)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**ruby:**

The examples below assume that you have [connected to a MongoDB replica set and have accessed a database](https://www.mongodb.com/docs/ruby-driver/current/reference/create-client/)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/change_stream_examples_spec.rb)

**go:**

The Go examples below assume that you have [connected to a MongoDB replica set and have accessed a database](https://godoc.org/go.mongodb.org/mongo-driver/mongo#NewClient/)
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/go_examples.go)

**swift-sync:**

The Swift (Sync) examples below assume that you have
[connected to a MongoDB replica set and have accessed a database](https://mongodb.github.io/mongo-swift-driver/docs/current/MongoSwiftSync/Classes/MongoClient.html) 
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

The Swift (Async) examples below assume that you have
[connected to a MongoDB replica set and have accessed a database](https://mongodb.github.io/mongo-swift-driver/docs/current/MongoSwift/Classes/MongoClient.html) 
that contains an `inventory` collection.

(Code example not available offline: /driver-examples/swiftAsync.swift)

To retrieve the data change event from
the cursor, iterate the change stream cursor. For information on the
change stream event, see change-stream-output.

The change stream cursor remains open until
one of the following occurs:

- The cursor is explicitly closed.

- An invalidate event occurs; for
  example, a collection drop or rename.

- The connection to the MongoDB deployment closes or times out. 
  See cursor-behaviors for more information.

- .. include:: /includes/extracts/changestream-remove-shard.rst

**Note:**

The lifecycle of an unclosed cursor is language-dependent.

## Modify Change Stream Output

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

**python:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/test_examples.py)

**motor:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/test_examples_motor.py)

**java-sync:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

```java
MongoClient mongoClient = MongoClients.create("mongodb://<username>:<password>@<host>:<port>");

// Select the MongoDB database and collection to open the change stream against

MongoDatabase db = mongoClient.getDatabase("myTargetDatabase");

MongoCollection<Document> collection = db.getCollection("myTargetCollection");

// Create $match pipeline stage.
List<Bson> pipeline = singletonList(Aggregates.match(Filters.or(
   Document.parse("{'fullDocument.username': 'alice'}"),
   Filters.in("operationType", asList("delete")))));

// Create the change stream cursor, passing the pipeline to the
// collection.watch() method

MongoCursor<Document> cursor = collection.watch(pipeline).iterator();
```

The `pipeline` list includes a single `$match` stage that
filters any operations where the `username` is `alice`, or
operations where the `operationType` is `delete`.

Passing the `pipeline` to the `watch()` method directs the
change stream to return notifications after passing them through the
specified `pipeline`.

**csharp:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/ChangeStreamExamples.cs)

**c:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**nodejs:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

The following example uses stream to process the change events.

(Code example not available offline: /driver-examples/node_changestreams.js)

Alternatively, you can also use iterator to process the change events:

(Code example not available offline: /driver-examples/node_changestreams.js)

**php:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**ruby:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

**go:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/go_examples.go)

**swift-sync:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

You can control change stream output by
providing an array of one or more of the following pipeline stages when
configuring the change stream:

- `$addFields`
- `$match`
- `$project`
- `$replaceRoot`
- `$replaceWith` 
- `$redact`
- `$set` 
- `$unset` 

(Code example not available offline: /driver-examples/swiftAsync.swift)

**Tip:**

The _id field of the change stream
event document act as the resume token. Do not use the pipeline to modify or remove
the change stream event's `_id` field. 

Starting in MongoDB 4.2, change streams will throw an exception if
the change stream aggregation pipeline modifies an event's _id field.

See change-stream-output for more information on the change stream
response document format.

## Lookup Full Document for Update Operations

By default, change streams only return the delta of fields during
the update operation. However, you can configure the change stream
to return the most current majority-committed version of the updated
document.

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

**python:**

To return the most current majority-committed version of the updated
document, pass `full_document='updateLookup'` to the
`db.collection.watch()` method.

In the example below, all update operations notifications
include a `full_document` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/test_examples.py)

**motor:**

To return the most current majority-committed version of the updated
document, pass `full_document='updateLookup'` to the
`db.collection.watch()` method.

In the example below, all update operations notifications
include a ``full_document` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/test_examples_motor.py)

**java-sync:**

To return the most current majority-committed version of the updated
document, pass `FullDocument.UPDATE_LOOKUP`  to the
`db.collection.watch.fullDocument()` method.

In the example below, all update operations notifications
include a `FullDocument` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/DocumentationSamples.java)

**c:**

To return the most current majority-committed version of the updated
document, pass the `"fullDocument"` option with the `"updateLookup"` value to the
`mongoc_collection_watch` method.

In the example below, all update operations notifications
include a `fullDocument` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**csharp:**

To return the most current majority-committed version of the updated
document, pass `"FullDocument = ChangeStreamFullDocumentOption.UpdateLookup"` to the
`db.collection.watch()` method.

In the example below, all update operations notifications
include a `FullDocument` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/ChangeStreamExamples.cs)

**nodejs:**

To return the most current majority-committed version of the updated
document, pass `{ fullDocument: 'updateLookup' }` to the
`db.collection.watch()` method.

In the example below, all update operations notifications
include a `fullDocument` field that represents the *current*
version of the document affected by the update operation.

The following example uses stream to process the change events.

(Code example not available offline: /driver-examples/node_changestreams.js)

Alternatively, you can also use iterator to process the change events:

(Code example not available offline: /driver-examples/node_changestreams.js)

**php:**

To return the most current
majority-committed version of the updated document, pass
`"fullDocument' => \MongoDB\Operation\ChangeStreamCommand::FULL_DOCUMENT_UPDATE_LOOKUP"`
to the `db.watch()` method.

In the example below, all update operations notifications
include a `fullDocument` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**ruby:**

To return the most current majority-committed version of the updated
document, pass `full_document: 'updateLookup'` to the
`db.watch()` method.

In the example below, all update operations notifications
include a `full_document` field that represents the *current*
version of the document affected by the update operation.

(Code example not available offline: /driver-examples/change_stream_examples_spec.rb)

**go:**

To return the most current majority-committed version of the
updated document, `SetFullDocument(options.UpdateLookup)`
change stream option.

(Code example not available offline: /driver-examples/go_examples.go)

**swift-sync:**

To return the most current majority-committed version of
the updated document, pass ``options:
ChangeStreamOptions(fullDocument: .updateLookup)`` to the
`watch()` method.

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

To return the most current majority-committed version of
the updated document, pass ``options:
ChangeStreamOptions(fullDocument: .updateLookup)`` to the
`watch()` method.

(Code example not available offline: /driver-examples/swiftAsync.swift)

**Note:**

If there are one or more majority-committed operations that modified
the updated document *after* the update operation but *before* the
lookup, the full document returned may differ significantly from the
document at the time of the update operation.

However, the deltas included in the change stream document always
correctly describe the watched collection changes that applied to
that change stream event.

See change-stream-output for more information on the change
stream response document format.

## Resume a Change Stream

Change streams are resumable by specifying a resume token to either
resumeAfter or
startAfter when opening the cursor.

### `resumeAfter` for Change Streams

You can resume a change stream after a specific event by passing a resume token
to `resumeAfter` when opening the cursor. 

See change-stream-resume-token for more information on the resume token.

**Important:**

- The oplog must have enough history to locate the operation
  associated with the token or the timestamp, if the timestamp is in
  the past.

- .. include:: /includes/extracts/changestream-invalid-events.rst

**python:**

You can use the `resume_after` modifier to resume
notifications after the operation specified in the resume
token. The `resume_after` modifier takes a value that must
resolve to a resume token, e.g. `resume_token` in the
example below.

(Code example not available offline: /driver-examples/test_examples.py)

**motor:**

You can use the `resume_after` modifier to resume
notifications after the operation specified in the resume
token. The `resume_after` modifier takes a value that must
resolve to a resume token, e.g. `resume_token` in the
example below.

(Code example not available offline: /driver-examples/test_examples_motor.py)

**java-sync:**

You can use the `resumeAfter()` method to resume
notifications after the operation specified in the resume
token. The `resumeAfter()` method takes a value that must
resolve to a resume token, e.g. `resumeToken` in the
example below.

(Code example not available offline: /driver-examples/DocumentationSamples.java)

**csharp:**

In the example below, the `resumeToken` is retrieved from the last change stream document
and passed to the `Watch()` method as an option. Passing the `resumeToken`
to the `Watch()` method directs
the change stream to attempt to resume notifications starting after the
operation specified in the resume token.

(Code example not available offline: /driver-examples/ChangeStreamExamples.cs)

**c:**

In the example below, the `resumeAfter` option is appended to the stream options
to recreate the stream after it has been destroyed. Passing the `_id` to
the change stream attempts to resume notifications starting after the
operation specified.

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**nodejs:**

You can use the `resumeAfter` option to resume
notifications after the operation specified in the resume
token. The `resumeAfter` option takes a value that must
resolve to a resume token, e.g. `resumeToken` in the
example below.

(Code example not available offline: /driver-examples/node_changestreams.js)

**php:**

You can use the `resumeAfter` option to resume
notifications after the operation specified in the resume
token. The `resumeAfter` option takes a value that must
resolve to a resume token, e.g. `$resumeToken` in the
example below.

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**ruby:**

You can use the `resume_after` modifier to resume
notifications after the operation specified in the resume
token. The `resume_after` modifier takes a value that must
resolve to a resume token, e.g. `resume_token` in the
example below.

(Code example not available offline: /driver-examples/change_stream_examples_spec.rb)

**go:**

You can use [ChangeStreamOptions.SetResumeAfter](https://godoc.org/go.mongodb.org/mongo-driver/mongo/options#ChangeStreamOptions.SetResumeAfter)
to specify the resume
token for the change stream. If the resumeAfter option is set,
the change stream resumes notifications after the operation
specified in the resume token. The `SetResumeAfter` takes a
value that must resolve to a resume token, e.g.
`resumeToken` in the example below.

(Code example not available offline: /driver-examples/go_examples.go)

**swift-sync:**

You can use the `resumeAfter` option to resume
notifications after the operation specified in the resume
token. The `resumeAfter` option takes a value that must
resolve to a resume token, e.g. `resumeToken` in the
example below.

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

You can use the `resumeAfter` option to resume
notifications after the operation specified in the resume
token. The `resumeAfter` option takes a value that must
resolve to a resume token, e.g. `resumeToken` in the
example below.

(Code example not available offline: /driver-examples/swiftAsync.swift)

### `startAfter` for Change Streams

You can start a new change stream after a specific event by passing a resume
token to `startAfter` when opening the cursor. Unlike
resumeAfter, `startAfter` can
resume notifications after an invalidate event
by creating a new change stream. 

See change-stream-resume-token for more information on the resume token.

**Important:**

- The oplog must have enough history to locate the operation
  associated with the token or the timestamp, if the timestamp is in
  the past.

### Resume Tokens

The resume token is available from multiple sources:

| Source | Description |
|---|---|
| Change Events | Each change event notification includes a resume token on the `_id` field. |
| Aggregation | The `$changeStream` aggregation stage includes a resume token on the `cursor.postBatchResumeToken` field. This field only appears when using the `aggregate` command. |
| Get More | The `getMore` command includes a resume token on the `cursor.postBatchResumeToken` field. |

Starting in MongoDB 4.2, change streams will throw an exception if
the change stream aggregation pipeline modifies an event's _id field.

**Tip:**

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

#### Resume Tokens from Change Events

Change event notifications include a resume token on the `_id` field:

```json
{
   "_id": {
      "_data": "82635019A0000000012B042C0100296E5A1004AB1154ACACD849A48C61756D70D3B21F463C6F7065726174696F6E54797065003C696E736572740046646F63756D656E744B65790046645F69640064635019A078BE67426D7CF4D2000004"
    },
    "operationType": "insert",
    "clusterTime": Timestamp({ "t": 1666193824, "i": 1 }),
    "collectionUUID": new UUID("ab1154ac-acd8-49a4-8c61-756d70d3b21f"),
    "wallTime": ISODate("2022-10-19T15:37:04.604Z"),
    "fullDocument": {
       "_id": ObjectId("635019a078be67426d7cf4d2"'),
       "name": "Giovanni Verga"
    },
    "ns": { 
       "db": "test", 
       "coll": "names" 
    },
    "documentKey": { 
       "_id": ObjectId("635019a078be67426d7cf4d2") 
    }
}
```

#### Resume Tokens from `aggregate`

When using the `aggregate` command, the `$changeStream`
aggregation stage includes a resume token on the  
`cursor.postBatchResumeToken` field:

```json
{
   "cursor": {
      "firstBatch": [],
      "postBatchResumeToken": { 
         "_data": "8263515EAC000000022B0429296E1404" 
      },
      "id": Long("4309380460777152828"),
      "ns": "test.names"
   },
   "ok": 1,
   "$clusterTime": {
      "clusterTime": Timestamp({ "t": 1666277036, "i": 1 }),
      "signature": {
         "hash": Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
         "keyId": Long("0")
      }
   },
   "operationTime": Timestamp({ "t": 1666277036, "i": 1 })
}
```

#### Resume Tokens from `getMore`

The `getMore` command also includes a resume token on the 
`cursor.postBatchResumeToken` field:

```json
{
   "cursor": {
      "nextBatch": [],
      "postBatchResumeToken": { 
         "_data": "8263515979000000022B0429296E1404"
      },
      "id": Long("7049907285270685005"),
      "ns": "test.names"
   }, 
   "ok": 1,
   "$clusterTime": {
      "clusterTime": Timestamp( { "t": 1666275705, "i": 1 } ),
      "signature": {
         "hash": Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
         "keyId": Long("0")
      }
   },
   "operationTime": Timestamp({ "t": 1666275705, "i": 1 })
}
```

## Use Cases

Change streams can benefit architectures with reliant business systems,
informing downstream systems once data changes are durable. For example,
change streams can save time for developers when implementing Extract,
Transform, and Load (ETL) services, cross-platform synchronization,
collaboration functionality, and notification services.

## Access Control

For deployments enforcing authentication and authorization:

- To open a change stream against specific collection, applications
  must have privileges that grant `changeStream` and
  `find` actions on the corresponding collection.

  ```javascript
  { resource: { db: <dbname>, collection: <collection> }, actions: [ "find", "changeStream" ] }
  ```

- To open a change stream on a single database, applications must have
  privileges that grant `changeStream` and
  `find` actions on all non-`system` collections in the
  database.

  ```javascript
  { resource: { db: <dbname>, collection: "" }, actions: [ "find", "changeStream" ] }
  ```

- To open a change stream on an entire deployment, applications must
  have privileges that grant `changeStream` and
  `find` actions on all non-`system` collections for all
  databases in the deployment.

  ```javascript
  { resource: { db: "", collection: "" }, actions: [ "find", "changeStream" ] }
  ```

## Event Notification

Change streams only notify on data changes that have persisted to a majority
of data-bearing members in the replica set. This ensures that notifications are
triggered only by majority-committed changes that are durable in failure
scenarios.

For example, consider a 3-member replica set with a change stream
cursor opened against the primary. If a client issues an insert
operation, the change stream only notifies the application of the data change
once that insert has persisted to a majority of data-bearing members.

If an operation is associated with a transaction, the change event document includes the
`txnNumber` and the `lsid`.

## Collation

Change streams use `simple` binary comparisons unless an explicit collation is 
provided. 

## Change Streams and Orphan Documents

Starting in MongoDB 5.3, during range migration, change stream
events are not generated for updates to orphaned documents.

## Change Streams with Document Pre- and Post-Images

Starting in MongoDB 6.0, you can use change stream events to output the version of a document before and
after changes (the document pre- and post-images):

- The pre-image is the document before it was replaced, updated, or
  deleted. There is no pre-image for an inserted document.

- The post-image is the document after it was inserted, replaced, or
  updated. There is no post-image for a deleted document.

- Enable `changeStreamPreAndPostImages` for a collection using
  `db.createCollection()`, `create`, or
  `collMod`.

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

For complete examples with the change stream output, see
db.collection.watch-change-streams-pre-and-post-images-example.
