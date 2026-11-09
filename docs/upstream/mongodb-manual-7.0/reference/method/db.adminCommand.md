<!-- Converted from reference/method/db.adminCommand.txt (reStructuredText). Includes are inlined. -->

# db.adminCommand() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.adminCommand(command)`**

Provides a helper to run specified database commands against the `admin` database.

| Parameter | Type | Description |
|---|---|---|
| `command` | document or string | A database command, specified either in document form or as a string. If specified as a string, the command cannot include any arguments. |

          

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

`db.adminCommand` runs commands against the `admin`
database regardless of the database context in which it runs.
The following commands are equivalent:

```javascript
db.getSiblingDB("admin").runCommand(<command>)

db.adminCommand(<command>)
```

For a list of available administrative database commands, see
database-commands.

**Note:**

For a `mongod` or `mongos` running with
`authorization`, the authorized user must have
the appropriate privileges to run the database command. See the
reference documentation for the command for more information on
security requirements.

## Response

The method returns a response document that contains the following
fields:

* - Field
  - Description

* - *<command result>*

  - Result fields specific to the `command` that ran.

* - `ok`

  - A number that indicates if the command succeeded (`1`)
    or failed (`0`).

* - `operationTime`

  - The logical time of the operation. MongoDB uses the logical time 
    to order operations. *Only for replica sets and sharded 
    clusters.*

    If the command does not generate an oplog entry, for example, a
    read operation, then the operation does not advance the logical
    clock. In this case, `operationTime` returns:

    - For read concern `"local"`,
      `"snapshot"`, and `"linearizable"`,
      the timestamp of the most recent entry in the oplog.

    - For read concern `"majority"`, the timestamp of
      the most recent `majority-acknowledged` entry in the oplog.

    For operations associated with causally consistent sessions, the MongoDB drivers use the logical time
    to automatically set the afterClusterTime period.

* - `$clusterTime`

  - A document that returns the signed cluster time. Cluster time is a
    logical time used for ordering of operations. *Only for replica
    sets and sharded clusters. For internal use only.*

    The document contains the following fields:

    - `clusterTime`: timestamp of the highest known cluster time for the member.

    - `signature`: a document that contains the hash of the cluster time and the id
      of the key used to sign the cluster time.

## Examples

### killOp

The following example uses the `db.adminCommand()`
method to execute a `killOp` command to terminate an
operation with `opid 724`. `killOp` is an administrative
command and must be run against the `admin` database.

```javascript
db.adminCommand( { "killOp": 1, "op": 724 } )
```

### renameCollection

The following example uses `db.adminCommand()` to execute
the `renameCollection` administrative database command
to rename the `orders` collection in the `test` database to
`orders-2016`.

```javascript
db.adminCommand(
  {
     renameCollection: "test.orders",
     to: "test.orders-2016"
  }
)
```

### createUser

The following example uses the `db.adminCommand()` method to
create a user named `bruce` with the `dbOwner` role on the
`admin` database.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.adminCommand(
  {
    createUser: "bruce",
    pwd: passwordPrompt(),  // or <cleartext password>
    roles: [
      { role: "dbOwner", db: "admin" }
    ]
  }
)
```
