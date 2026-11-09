<!-- Converted from reference/command/startSession.txt (reStructuredText). Includes are inlined. -->

# startSession

## Definition

**`startSession`**

The `startSession` command starts a new logical
session for a sequence of operations.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `Mongo.startSession`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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
     startSession: 1
   }
)
```

To run `startSession`, use the `db.runCommand( { <command> } )` method.

```javascript
db.runCommand( 
   { 
     startSession: 1 
   } 
)
```

**Important:**

`featureCompatibilityVersion` must be 3.6 or greater to use the
`startSession` command.

**See also:**

`Mongo.startSession()`

## Behavior

If the deployment enforces authentication/authorization, you must be
authenticated to run the `startSession` command. The user
who runs `startSession` owns the created session, and only
that user can use the session.

If the deployment does not enforce authentication/authorization, a
created session has no owner and can be used by any user on any
connection. If the user authenticates and creates a session for a
deployment that does not enforce authentication/authorization, the user
owns the session. However, any user on any connection may use the
session.

If the deployment transitions to auth without any downtime, any
sessions without an owner cannot be used.

A session can only be used with the `MongoClient` object that created
the session. A single session cannot be used concurrently. Operations
that use a single session must be run sequentially.

## Output

In addition to the status and operation time of the command, the
`startSession` returns the following session specific
information:

* - Field
  - Type
  - Description

* - `id`

  - Document

  - The document that contains the 16-byte Universally Unique
    Identifier (UUID) portion of the session's identifier.

    ```javascript
    id: { id: <UUID> }
    ```

    The session's identifier consists of this UUID concatenated with
    the hash of the authenticated user credentials.

* - `timeoutMinutes`

  - number

  - The amount of time, in minutes, since the last client use that a
    session remains active before expiring. By default, sessions
    have an expiration timeout of 30 minutes. To change the value,
    set the `localLogicalSessionTimeoutMinutes` parameter
    when starting up `mongod`. For replica sets and sharded
    clusters, you must specify the same value on every member.
