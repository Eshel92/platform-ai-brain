<!-- Converted from reference/method/db.runCommand.txt (reStructuredText). Includes are inlined. -->

# db.runCommand() (mongosh method)

## Definition

**`db.runCommand(command, [options])`**

Provides a helper to run specified database commands. This is the preferred method to issue
database commands, as it provides a consistent interface between
the shell and drivers.

* - Parameter
  - Type
  - Description

* - `command`
  - document or string
  - Document or string that specifies the 
    command. If specified as a string, `db.runCommand()`
    transforms the string into a document.

* - `options`
  - document
  - Starting in mongosh 2.0, options that specify how `mongosh` 
    runs the command.

* - `options.readPreference` 

  - read preference
  - Read preference to run the command with. If not specified, 
    defaults to `primary`. `db.runCommand()` ignores 
    any other read preference global configuration set, including 
    using `setReadPref()` or by specifying 
    `readPreference` in a connection string.

    In mongosh 1.x, `db.runCommand()` does not take an 
    `options` argument. To set the read preference, use
    `Mongo.setReadPref()` or specify `readPreference` in the 
    connection string.

To specify a time limit in milliseconds, see
terminate-running-ops.

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

`db.runCommand()` runs the command in the context of the
current database. Some commands are only applicable in the context of
the `admin` database, and you must change your `db` object
before running these commands or use `db.adminCommand()`.

### Read Preference

Starting in mongosh 2.0, you can specify the read preference for a
command with the options 
argument. If you do not specify a read preference, `db.runCommand()`
defaults to `primary`. 

**Warning:**

In mongosh 2.0, `db.runCommand()` ignores any other read preference 
global configuration set, including using `Mongo.setReadPref()` or 
by specifying `readPreference` in a connection string.

In mongosh 1.x, `db.runCommand()` does not take an `options` 
argument. `db.runCommand()` uses the read preference specified either
by using `Mongo.setReadPref()` or by specifying `readPreference` in 
the connection string.

## Examples

The following examples show how to use `db.runCommand()` to run
database commands.

### hello Command Without Specified Read Preference

This example shows how to use `db.runCommand()` to run the 
`hello` command.

```javascript
db.runCommand( { hello: 1 } )
```

For details on output, see hello Output.

For details on read preference behavior, see 
runCommand-read-pref-behavior.

### hello Command with readPreference: secondaryPreferred

This example shows how to use `db.runCommand()` to run the 
`hello` command with the `secondaryPreferred` 
read preference. 

```javascript
db.runCommand( { hello: 1 }, { readPreference: "secondaryPreferred" } )
```

For details on output, see hello Output.

For details on read preference behavior, see 
runCommand-read-pref-behavior.

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
