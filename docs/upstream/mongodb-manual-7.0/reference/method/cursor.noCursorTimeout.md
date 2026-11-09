<!-- Converted from reference/method/cursor.noCursorTimeout.txt (reStructuredText). Includes are inlined. -->

# cursor.noCursorTimeout() (mongosh method)

## Definition

**`cursor.noCursorTimeout()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Instructs the server to avoid closing a cursor automatically after a period
of inactivity.

The `noCursorTimeout()` method has the following
prototype form:

```javascript
db.collection.find(<query>).noCursorTimeout()
```

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Session Idle Timeout Overrides `noCursorTimeout`

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

Consider an application that issues a `db.collection.find()`
with `cursor.noCursorTimeout`. The server returns a cursor along
with a batch of documents defined by the `cursor.batchSize()` of
the `find()`. The session refreshes each time the
application requests a new batch of documents from the server. However,
if the application takes longer than 30 minutes to process the current
batch of documents, the session is marked as expired and closed. When
the server closes the session, it also kills the cursor *despite* the
cursor being configured with `noCursorTimeout`. When the
application requests the next batch of documents, the server returns an
error.

### Refresh a Cursor with `refreshSessions`

For operations that return a cursor, if the cursor may be idle for
longer than 30 minutes, issue the operation within an explicit session
using `Mongo.startSession()` and periodically refresh the
session using the `refreshSessions` command. For example:

```bash
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
`cursor.noCursorTimeout()` to prevent the server from closing
the cursor if idle. The `while` loop includes a block that uses
`refreshSessions` to refresh the session every 5 minutes.
Since the session will never exceed the 30 minute idle timeout, the
cursor can remain open indefinitely.

For MongoDB drivers, defer to the `driver documentation` for instructions and syntax for creating sessions.
