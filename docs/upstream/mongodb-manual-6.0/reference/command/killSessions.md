<!-- Converted from reference/command/killSessions.txt (reStructuredText). Includes are inlined. -->

# killSessions

## Definition

**`killSessions`**

The `killSessions` command kills the specified sessions.
If access control is enabled, the command only kills the sessions
owned by the user. [#exception]_

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     killSessions: [ { id : <UUID> }, ... ] 
   } 
)
```

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Command Fields

The command takes an array of documents that specify the UUID portion
of the session id. Specify an empty array `[ ]` to kill all sessions,
or if access control is enabled, all sessions owned by the user.
[#exception]_

## View Existing Sessions

To view existing sessions, see `$listSessions` operation or
`$listLocalSessions`.

## Behavior

### Session Identification

MongoDB concatenates each of the specified UUIDs with the hash of the
authenticated user credentials to identify the user's sessions to kill.
If the user has no session that match, the `killSessions`
has no effect.

### In-progress Operations

Killing a session kills any in-progress operations in the session and
closes any open cursors associated with these operations.

### Killed Session Availability

The killed session may still be listed as a current session, and future
operations may use the killed session. To view existing sessions, see
`$listSessions` operation or `$listLocalSessions`.

### Sessions with Transactions in Prepared State

The `killSessions` operation ignores sessions that have transactions in
prepared state. Transactions in prepared state refer to transactions
with write operations that span multiple shards whose commit
coordinator has completed the `"sendingPrepare" action`.

   

## Example

The following operation kills the specified session for the user:

```javascript
db.runCommand( { killSessions: [ { id: UUID("f9b3d8d9-9496-4fff-868f-04a6196fc58a") } ] } )
```

**See also:**

kill-write-ops-sharded-cluster
