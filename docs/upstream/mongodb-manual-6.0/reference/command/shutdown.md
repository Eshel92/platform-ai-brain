<!-- Converted from reference/command/shutdown.txt (reStructuredText). Includes are inlined. -->

# shutdown

**Changed in version:** 5.0

**`shutdown`**

The `shutdown` command cleans up all database resources
and then terminates the process.  You must issue
the `shutdown` command against the admin database.

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

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     shutdown: 1,
     force: <boolean>
     timeoutSecs: <int>,
     comment: <any>
   }
)
```

## Command Fields

The command takes these fields:

* - Field
  - Description

* - shutdown

  - .. _shutdown-cmd-shutdown:

    Specify `1`.

* - force
  - .. _shutdown-cmd-force:

    Optional. Specify `true` to force the `mongod`
    or `mongos` to shut down. Force shutdown
    interrupts any ongoing operations on the `mongod`
    or `mongos` and may result in unexpected
    behavior.

    You can pause and resume in-progress index builds using 
    `force`. See cmd-shutdown-replica-set for more 
    information.

* - timeoutSecs
  - .. _shutdown-cmd-timeoutSecs:

    Optional.

    Starting in MongoDB 5.0, `mongod` and `mongos`
    enter a quiesce period to allow any ongoing database operations to
    complete before shutting down.

    If a `mongod` primary receives a shut down request,
    the primary:

    #. Attempts to step down to a secondary.

       If the step down fails and a:

       - `shutdown` or `db.shutdownServer()` command
         was run, `mongod` only continues the shut down steps
         if the force field is true, or a

       - `SIGTERM` signal was sent to `mongod`,
         `mongod` always continues the shut down steps.

    #. Enters the quiesce period.

    #. Ends any remaining database operations.

    #. Shuts down.

    For a `mongod` secondary or `mongos`
    shut down request, the quiesce period is entered after a shut down was
    requested.

    The quiesce period is specified by the:

    - timeoutSecs field if a `shutdown` or
      `db.shutdownServer()` command was run, or

    - `shutdownTimeoutMillisForSignaledShutdown` server
      parameter if a `SIGTERM` signal was sent to `mongod`,
      or

    - `mongosShutdownTimeoutMillisForSignaledShutdown` server
      parameter if a `SIGTERM` signal was sent to `mongos`.

    Clients cannot open new connections to a `mongod` or
    `mongos` that is shutting down.

    timeoutSecs specifies a time period in seconds. The default is:

    - 15 seconds starting in MongoDB 5.0.
    - 10 seconds in MongoDB versions earlier than 5.0.

    `mongod` uses timeoutSecs as follows:

    - If the current node is the primary node of a replica set,
      `mongod` waits for a period of up to the number of seconds specified
      by the timeoutSecs field for an electable node to catch up before
      stepping down the primary node. For details about the catch up time,
      see replication lag.
    - If the current node is in the `SECONDARY` state after
      stepping down from being the primary, any remaining time specified in
      timeoutSecs is used for a quiesce period, which allows existing
      operations to complete. New operations are sent to other replica set
      nodes.

    Starting in MongoDB 5.0, `mongos` uses timeoutSecs as a
    quiesce period, which allows existing operations to complete. New
    operations are sent to other `mongos` nodes. In MongoDB
    versions earlier than 5.0, `mongos` shuts down immediately
    and does not use timeoutSecs.

    In MongoDB 4.4 and earlier, for a `mongod`
    primary, timeoutSecs
    is the number of seconds the primary should wait for a
    secondary to catch up. If no secondaries catch up within the
    specified time, the command fails. Defaults to `10` seconds.

* - `comment`
  - .. include:: /includes/extracts/comment-content.rst

**See also:**

`db.shutdownServer()`

## Behavior

For a `mongod` started *with* authentication, 
you must run `shutdown` over an authenticated connection. 
See cmd-shutdown-access-control for more information.

For a `mongod` started *without* authentication,
you must run `shutdown` from a client connected to the 
localhost interface. For example, run `mongosh` with 
the `--host "127.0.0.1"` option on the
same host machine as the `mongod`.

### `shutdown` on Replica Set Members

`shutdown` fails if the replica set member is running
certain operations such as index builds. You can specify 
force: true to force the member 
to save index build progress to disk. The `mongod` 
recovers the index build when it restarts and continues from the 
saved checkpoint.

#### Shutting Down the Replica Set Primary, Secondary, or `mongos`

Starting in MongoDB 5.0, `mongod` and `mongos`
enter a quiesce period to allow any ongoing database operations to
complete before shutting down.

If a `mongod` primary receives a shut down request,
the primary:

#. Attempts to step down to a secondary.

   If the step down fails and a:

   - `shutdown` or `db.shutdownServer()` command
     was run, `mongod` only continues the shut down steps
     if the force field is true, or a

   - `SIGTERM` signal was sent to `mongod`,
     `mongod` always continues the shut down steps.

#. Enters the quiesce period.

#. Ends any remaining database operations.

#. Shuts down.

For a `mongod` secondary or `mongos`
shut down request, the quiesce period is entered after a shut down was
requested.

The quiesce period is specified by the:

- timeoutSecs field if a `shutdown` or
  `db.shutdownServer()` command was run, or

- `shutdownTimeoutMillisForSignaledShutdown` server
  parameter if a `SIGTERM` signal was sent to `mongod`,
  or

- `mongosShutdownTimeoutMillisForSignaledShutdown` server
  parameter if a `SIGTERM` signal was sent to `mongos`.

Clients cannot open new connections to a `mongod` or
`mongos` that is shutting down.

timeoutSecs specifies a time period in seconds. The default is:

- 15 seconds starting in MongoDB 5.0.
- 10 seconds in MongoDB versions earlier than 5.0.

`mongod` uses timeoutSecs as follows:

- If the current node is the primary node of a replica set,
  `mongod` waits for a period of up to the number of seconds specified
  by the timeoutSecs field for an electable node to catch up before
  stepping down the primary node. For details about the catch up time,
  see replication lag.
- If the current node is in the `SECONDARY` state after
  stepping down from being the primary, any remaining time specified in
  timeoutSecs is used for a quiesce period, which allows existing
  operations to complete. New operations are sent to other replica set
  nodes.

Starting in MongoDB 5.0, `mongos` uses timeoutSecs as a
quiesce period, which allows existing operations to complete. New
operations are sent to other `mongos` nodes. In MongoDB
versions earlier than 5.0, `mongos` shuts down immediately
and does not use timeoutSecs.

**Warning:**

Force shutdown of the primary can result in the 
rollback of any writes not 
yet replicated to a secondary. 

## Access Control

To run `shutdown` on a `mongod` enforcing 
authentication, the authenticated user *must* have the 
`shutdown` privilege. For example, a user with the 
built-in role `hostManager` has the appropriate permissions.

## Examples

### Shut down a `mongod`

```javascript
db.adminCommand({ "shutdown" : 1 })
```

### Force Shut Down a `mongod`

```javascript
db.adminCommand({ "shutdown" : 1, "force" : true })
```

### Shut Down a Primary `mongod` With Longer Timeout

```javascript
db.adminCommand({ "shutdown" : 1, timeoutSecs: 60 })
```
