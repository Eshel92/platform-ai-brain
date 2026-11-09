<!-- Converted from reference/command/endSessions.txt (reStructuredText). Includes are inlined. -->

# endSessions

## Definition

**`endSessions`**

The `endSessions` command expires the specified sessions.
The command overrides the timeout period that sessions wait before
expiring.

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
     endSessions: [ { id : <UUID> }, ... ] 
   }
)
```

To run `endSessions`, use the `db.runCommand( { <command> } )` method.

```javascript
db.runCommand( 
   { 
     endSessions: [ { id : <UUID> }, ... ] 
   } 
 )
```

## Behavior

### Session Identification

MongoDB concatenates each of the specified UUIDs with the hash of the
authenticated user credentials to identify the user's sessions to end.
If the user has no session that match, the `endSessions`
has no effect.

## Access Control

If the deployment enforces authentication/authorization, you must be
authenticated to run the `endSessions` command.

A user can only end sessions belonging to the user.

**See also:**

- `startSession`
- `$listLocalSessions`
- `$listSessions`
