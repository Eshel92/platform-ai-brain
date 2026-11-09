<!-- Converted from reference/command/refreshSessions.txt (reStructuredText). Includes are inlined. -->

# refreshSessions

## Definition

**`refreshSessions`**

The `refreshSessions` command updates the last use time
for the specified sessions, thereby extending the active state of
the sessions.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     refreshSessions: [ 
       { id : <UUID> }, ... 
     ] 
   } 
 )
```

To run `refreshSessions`, use the `db.runCommand( { <command> } )` method.

```javascript
db.runCommand( 
   { 
     refreshSessions: [ 
       { id : <UUID> }, ... 
     ] 
   } 
)
```

## Behavior

### Session Identification

MongoDB concatenates each of the specified UUIDs with the hash of the
authenticated user credentials to identify the user's sessions to refresh.
If the user has no session that match, the `refreshSessions`
has no effect.

## Access Control

If the deployment enforces authentication/authorization, you must be
authenticated to run the `refreshSessions` command.

A user can only refresh sessions belonging to the user.

**See also:**

- `startSession`
- `$listLocalSessions`
-  `$listSessions`
