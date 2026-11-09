<!-- Converted from reference/method/Session.txt (reStructuredText). Includes are inlined. -->

# Session

## Definition

**`Session`**

The Session object for the connection in `mongosh`.
To instantiate a session for the connection in
`mongosh`, see `Mongo.startSession()`. For more
information on sessions, see sessions.

### General Session Methods

* - Method
  - Description

* - .. method:: Session.advanceClusterTime()
  - Updates the cluster time tracked by the session.

    This method has the following parameters:

    ```javascript
    Session.advanceClusterTime( { 
       clusterTime: <timestamp>,
       signature: 
          { hash: <BinData>, keyId: <NumberLong> } 
    } )
    ```

* - .. method:: Session.advanceOperationTime(<timestamp>)
  - Updates the operation time.

* - .. method:: Session.endSession()
  - Ends the session.

* - .. method:: Session.getClusterTime()
  - Returns the most recent cluster time as seen by the session.
    Applicable for replica sets and sharded clusters only.

* - .. method:: Session.getDatabase(<database>)
  - Access the specified database from the session in `mongosh`.

* - .. method:: Session.getOptions()
  - Access the options for the session. For the available
    options, see `SessionOptions`.

* - .. method:: Session.getOperationTime()
  - Returns the timestamp of the last acknowledged operation for
    the session.

* - .. method:: Session.hasEnded()
  - Returns a boolean that specifies whether the session has
    ended.

### Session Methods for Transactions

|  |  |
|---|---|
| Method | Description |
| `Session.abortTransaction()` | Aborts the session's transaction. For details, see `Session.abortTransaction()`. |
| `Session.commitTransaction()` | Commits the session's transaction. For details, see `Session.commitTransaction()`. |
| `Session.startTransaction()` | Starts a multi-document transaction for the session. For details, see `Session.startTransaction()`. |
| `Session.withTransaction()` | Runs a specified lambda function within a transaction. For details, see `Session.withTransaction()`. |

## Example

The following example starts a session on the `Mongo`
connection object associated with `mongosh`'s global
`db` variable, and then uses the `Session.getDatabase()`
method to retrieve the database object associated with the session.

```javascript
var session = db.getMongo().startSession();
db = session.getDatabase(db.getName());
```
