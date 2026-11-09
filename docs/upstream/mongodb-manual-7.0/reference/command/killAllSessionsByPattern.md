<!-- Converted from reference/command/killAllSessionsByPattern.txt (reStructuredText). Includes are inlined. -->

# killAllSessionsByPattern (database command)

## Definition

**`killAllSessionsByPattern`**

The `killAllSessionsByPattern` command kills all sessions
that match any of the specified patterns. [#exception]_

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     killAllSessionsByPattern: [ <pattern>, ... ] 
   } 
)
```

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

   

## Command Fields

The command takes an array of documents that specify the patterns to
match:

| Pattern | Description |
|---|---|
| `{ lsid: { id : <UUID> } }` | Specify the UUID portion of the session ID to kill. |
| `{ uid: <BinData> }` | Specifies the hash of the owner of the sessions to kill. |
| `{ users: [ { user: <user>, db: <dbname> }, ... ] }` | Specifies the owners of the sessions to kill. Requires additional privileges. See killAllSessionsByPattern-auth. |
| `{ roles: [ { role: <role>, db: <dbname> }, ... ] }` | Specifies the roles assigned to the owners of the sessions to kill. Requires additional privileges. See killAllSessionsByPattern-auth. |

Specify an empty array to kill all sessions. [#exception]_

To view existing sessions, see `$listSessions` operation or
`$listLocalSessions`.

**See also:**

`killAllSessions`

## Behavior

### In-progress Operations

Killing a session kills any in-progress operations in the session and
closes any open cursors associated with these operations.

### Killed Session Availability

The killed session may still be listed as a current session, and future
operations may use the killed session. To view existing sessions, see
`$listSessions` operation or `$listLocalSessions`.

### Sessions with Transactions in Prepared State

The `killAllSessionsByPattern` operation ignores sessions that have transactions in
prepared state. Transactions in prepared state refer to transactions
with write operations that span multiple shards whose commit
coordinator has completed the `"sendingPrepare" action`.

## Access Control

If the deployment enforces authentication/authorization, you must have
the `killAnySession` privilege action to run the
`killAllSessionsByPattern` command.

For patterns that include `users` or `roles`, you must also have
privileges that grant `impersonate` action on the cluster
resource.

**Note:**

Users can kill their own sessions even without the
`killAnySession` privilege action.

## Examples

### Kill All Sessions

The following operation kills all sessions:

```javascript
db.runCommand( { killAllSessionsByPattern: [ ] } )
```

### Kill All Sessions for Specific Users

The following operation kills all sessions that have the specified
`uid` and whose owner has the specified role:

```javascript
db.runCommand( { killAllSessionsByPattern: [ 
   { "uid" : BinData(0,"oBRA45vMY78p1tv6kChjQPTdYsnCHi/kA/fFMZTIV1o=") },
   { roles: [ { role: "readWrite", db: "test" } ] }
] } )
```
