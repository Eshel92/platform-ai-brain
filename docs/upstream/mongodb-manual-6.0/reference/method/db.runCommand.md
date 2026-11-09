<!-- Converted from reference/method/db.runCommand.txt (reStructuredText). Includes are inlined. -->

# db.runCommand()

## Definition

**`db.runCommand(command)`**

Provides a helper to run specified database commands. This is the preferred method to issue
database commands, as it provides a consistent interface between
the shell and drivers.

| Parameter | Type | Description |
|---|---|---|
| `command` | document or string | "A database command, specified either in document form or as a string. If specified as a string, `db.runCommand()` transforms the string into a document." |

To specify a time limit in milliseconds, see
/tutorial/terminate-running-operations.

## Compatibility

This method is available in deployments hosted in the following environments: 

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

## Behavior

`db.runCommand()` runs the command in the context of the
current database. Some commands are only applicable in the context of
the `admin` database, and you must change your `db` object to
before running these commands or use `db.adminCommand()`.

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
