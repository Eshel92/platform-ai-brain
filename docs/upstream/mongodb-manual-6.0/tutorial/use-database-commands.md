<!-- Converted from tutorial/use-database-commands.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Use Database Commands

The MongoDB command interface provides access to all non CRUD database operations. Fetching server statistics, initializing a
replica set, and running an aggregation pipeline or map-reduce job are
all accomplished with commands.

See /reference/command for list of all commands sorted by
function.

## Database Command Form

You specify a command first by constructing a standard BSON
document whose first key is the name of the command. For example,
specify the `hello` command using the following
BSON document:

```javascript
{ hello: 1 }
```

## Issue Commands

`mongosh` provides a helper method for running
commands called `db.runCommand()`. The following operation in
`mongosh` runs the previous command:

```javascript
db.runCommand( { hello: 1 } )
```

Many `Drivers` provide an equivalent for
the `db.runCommand()` method. Internally, running commands
with `db.runCommand()` is equivalent to a special query
against the $cmd collection.

Many common commands have their own shell helpers or wrappers in
`mongosh` and drivers, such as the
`db.hello()` method in `mongosh`.

You can use the `maxTimeMS` option to specify a time limit for the
execution of a command, see terminate-long-running-commands for
more information on operation termination.

## `admin` Database Commands

You must run some commands on the admin database. Normally,
these operations resemble the following:

```javascript
use admin
db.runCommand( {buildInfo: 1} )
```

However, there's also a command helper that automatically runs the
command in the context of the `admin` database:

```javascript
db.adminCommand( {buildInfo: 1} )
```

## Command Responses

For all commands, MongoDB returns a response document that contains the
following fields:

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
