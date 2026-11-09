<!-- Converted from reference/command/killAllSessions.txt (reStructuredText). Includes are inlined. -->

# killAllSessions

## Definition

**`killAllSessions`**

The `killAllSessions` command kills all sessions for the
specified users. [#exception]_

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     killAllSessions: [ { user: <user>, db: <dbname> }, ... ]  
   } 
)
```

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, M10+, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

   

## Command Fields

The command takes an array of documents where each document specifies
the user and the user's authentication database. Specify an empty array
to kill all sessions for all users in the system. [#exception]_

## View Existing Sesssions

To view existing sessions, see `$listSessions` operation
or `$listLocalSessions`.

**See also:**

`killAllSessionsByPattern`

## Access Control

If the deployment enforces authentication/authorization, you must have
the `killAnySession` to run the
`killAllSessions` command.

**Note:**

Users can kill their own sessions even without
`killAnySession` privilege action.

## Behavior

### In-progress Operations

Killing a session kills any in-progress operations in the session and
closes any open cursors associated with these operations.

### Killed Session Availability

The killed session may still be listed as a current session, and future
operations may use the killed session. To view existing sessions, see
`$listSessions` operation or `$listLocalSessions`.

### Sessions with Transactions in Prepared State

The `killAllSessions` operation ignores sessions that have transactions in
prepared state. Transactions in prepared state refer to transactions
with write operations that span multiple shards whose commit
coordinator has completed the `"sendingPrepare" action`.

## Examples

### Kill All Sessions

The following operation kills all sessions for all users in the system:

```javascript
db.runCommand( { killAllSessions: [ ] } )
```

### Kill All Sessions for Specific Users

The following operation kills all sessions for the user `appReader`
in the `db1` and the user `reportWriter` in `db2` databases:

```javascript
db.runCommand( { killAllSessions: [ 
   { user: "appReader", db: "db1" },
   { user: "reportWriter", db: "db2" }
] } )
```
