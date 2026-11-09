<!-- Converted from reference/method/cursor.maxTimeMS.txt (reStructuredText). Includes are inlined. -->

# cursor.maxTimeMS()

## Definition

**`cursor.maxTimeMS(<time limit>)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Specifies a cumulative time limit in milliseconds for processing
operations on a cursor.

The `maxTimeMS()` method has the following prototype
form:

```javascript
db.collection.find(
   { <query> },
   { <projection> }
).maxTimeMS( <milliseconds> )
```

The `maxTimeMS()` method has the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| `milliseconds` | integer | Specifies a cumulative time limit in milliseconds for processing operations on the cursor. |

**Important:**

`maxTimeMS()` is not related to the
`NoCursorTimeout` query flag. `maxTimeMS()`
relates to processing time, while `NoCursorTimeout` relates
to idle time. A cursor's idle time does not contribute towards its
processing time.

The `maxAwaitTimeMS()` method sets a limit on how
long a tailable cursor waits
for the next response. It does not set a limit on total processing
time.

## Compatibility

This method is available in deployments hosted in the following environments: 

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

## Behaviors

MongoDB targets operations for termination if the associated cursor
exceeds its allotted time limit. MongoDB terminates operations that
exceed their allotted time limit using the same mechanism as
`db.killOp()`. MongoDB only terminates an operation at one of
its designated interrupt points.

MongoDB does not count network latency between the client and the
server towards a cursor's time limit. For a sharded cluster, however,
MongoDB does include the latency between the `mongos` and
`mongod` instances towards this time limit.

Queries that generate multiple batches of results continue to return
batches until the cursor exceeds its allotted time limit.

### Session Idle Timeout Overrides `maxTimeMS`

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

For example, consider a `find()` operation with
the `maxTimeMS` configured for a timeout of 31 minutes.
The server returns a cursor along with a batch of documents defined by
the `cursor.batchSize()` of the `find()`.
The session refreshes each time the application requests a new batch of
documents from the server. However, if the application takes longer than
30 minutes to process the current batch of documents, the session is
marked as expired and closed. When the server closes the session, it
also kills the cursor *despite* the cursor being configured with
`maxTimeMS` greater than 30 minutes. When the
application requests the next batch of documents, the server returns an
error.

For operations that return a cursor, if the cursor may be idle for
longer than 30 minutes, issue the operation within an explicit session
using `Mongo.startSession()` and periodically refresh the
session using the `refreshSessions` command. For example:

```javascript
var session = db.getMongo().startSession()
var sessionId = session
sessionId  // show the sessionId

var cursor = session.getDatabase("examples").getCollection("data").find().noCursorTimeout()
var refreshTimestamp = new Date() // take note of time at operation start

while (cursor.hasNext()) {

  // Check if more than 5 minutes have passed since the last refresh
  if ( (new Date()-refreshTimestamp)/1000 > 300 ) { 
    print("refreshing session")
    db.adminCommand({"refreshSessions" : [sessionId]})
    refreshTimestamp = new Date()
  }

  // process cursor normally

}
```

In the example operation, the `db.collection.find()` method is
associated with an explicit session. The cursor is configured with
`cursor.maxTimeMS()` to keep the cursor open for at least 31
minutes. The `while` loop includes a block that uses
`refreshSessions` to refresh the session every 5 minutes.
Since the session will never exceed the 30 minute idle timeout, the
cursor can remain open up to the configured
`maxTimeMS()`.

For MongoDB drivers, defer to the `driver documentation` for instructions and syntax for creating sessions. 

**See also:**

`Session Idle Timeout`

## Examples

**Example:** The following query specifies a time limit of 50 milliseconds:

```javascript
db.collection.find({description: /August [0-9]+, 1969/}).maxTimeMS(50)
```
