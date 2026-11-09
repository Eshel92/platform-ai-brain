<!-- Converted from reference/operator/aggregation/listSessions.txt (reStructuredText). Includes are inlined. -->

# $listSessions (aggregation stage)

## Definition

**`$listSessions`**

Lists all sessions stored in the `system.sessions` collection in the `config` database.
These sessions are visible to all members of the MongoDB deployment.

**Important:**

When a user creates a session on a `mongod` or
`mongos` instance, the record of the session initially
exists only in-memory on the instance; i.e. the record is local
to the instance. Periodically, the instance will sync its cached
sessions to the `system.sessions`
collection in the `config` database, at which time, they are
visible to `$listSessions` and all members of the
deployment. Until the session record exists in the
`system.sessions` collection, you can only list the session via
the `$listLocalSessions` operation.

To run `$listSessions`, it must be the first stage in the pipeline.

The stage has the following syntax:

```javascript
{ $listSessions: <document> }
```

The `$listSessions` stage takes a document with one
of the following contents:

| Field | Description |
|---|---|
| `{ }` | If running with access control, returns all sessions for the current authenticated user. If running without access control, returns all sessions. |
| `{ users: [ { user: <user>, db: <db> }, ... ] }` | Returns all sessions for the specified users. If running with access control, the authenticated user must have privileges with `listSessions` action on the cluster to list sessions for other users. |
| `{ allUsers: true }` | Returns all sessions for all users. If running with access control, the authenticated user must have privileges with `listSessions` action on the cluster. |

## Restrictions

`$listSessions` is not allowed in transactions.

## Examples

**shell:**

### List All Sessions

From the `system.sessions` collection,
the following aggregation operation lists all sessions:

**Note:**

If running with access control, the current user must have
privileges with `listSessions` action on the cluster.

```javascript
use config

db.system.sessions.aggregate( [  { $listSessions: { allUsers: true } } ] )
```

### List All Sessions for the Specified Users

From the `system.sessions` collection,
the following aggregation operation lists all sessions for the
specified user `myAppReader@test`:

**Note:**

If running with access control and the current user is not the
specified user, the current user must
have privileges with `listSessions` action on the cluster.

```javascript
use config

db.system.sessions.aggregate( [ { $listSessions: { users: [ {user: "myAppReader", db: "test" } ] } } ] )
```

### List All Sessions for the Current User

From the `system.sessions` collection,
the following aggregation operation lists all sessions for the current
user **if** run with access control:

```javascript
use config

db.system.sessions.aggregate( [ { $listSessions: { } } ] )
```

If run **without** access control, the operation lists all sessions.

**nodejs:**

To use the MongoDB Node.js driver to add a `$listSessions` stage to an
aggregation pipeline, use the `$listSessions` operator in a pipeline
object. Run the pipeline on the `system.sessions` collection.

### List All Sessions

The following aggregation operation lists all sessions:

```javascript
const db = client.db("config");
const collection = db.collection("system.sessions");

const pipeline = [{ $listSessions: { allUsers: true } }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

**Note:**

If running with access control, the current user must have
privileges with `listSessions` action on the cluster.

### List All Sessions for the Specified Users

The following aggregation operation lists all sessions for the specified
user `myAppReader@test`:

```javascript
const db = client.db("config");
const collection = db.collection("system.sessions");

const pipeline = [
  { 
    $listSessions: { 
      users: [{ user: "myAppReader", db: "test"}] 
    } 
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

**Note:**

If running with access control and the current user is not the
specified user, the current user must
have privileges with `listSessions` action on the cluster.

### List All Sessions for the Current User

If run with access control, the following aggregation operation lists 
all sessions for the current user:

```javascript
const db = client.db("config");
const collection = db.collection("system.sessions");

const pipeline = [{ $listSessions: {} }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

If run without access control, the operation lists all sessions.

## Output

`$listSessions` returns a cursor with one document per
session. Each document has the following prototype:

```none
{
   _id: {
      id: <UUID>,
      uid: <BinData>
   },
   lastUse: <date>
}
```

| Field | Type | Description |
|---|---|---|
| `_id.id` | UUID | The universally unique identifier (UUID) of the session. |
| `_id.uid` | BinData | A hash of the authenticated user's credentials associated with the session. |
| `lastUse` | date | The date and time the session was last used. |
