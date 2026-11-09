<!-- Converted from tutorial/manage-mongodb-processes.txt (reStructuredText). Includes are inlined. -->

# Configure Self-Managed `mongod` Processes

MongoDB runs as a standard program. You can start MongoDB from a
command line by issuing the `mongod` command and specifying
options.  For a list of options, see the `mongod`
reference. MongoDB can also run as a Windows service. For details, see
manually-create-windows-service. To install MongoDB, see
/installation.

The following examples assume the directory containing the
`mongod` process is in your system paths. The
`mongod` process is the primary database process that runs on
an individual server. `mongos` provides a coherent MongoDB
interface equivalent to a `mongod` from the perspective of a
client. The `mongosh` binary provides the administrative
shell.

This document discusses the `mongod` process; however,
some portions of this document may be applicable to `mongos`
instances.

## Start `mongod` Processes

By default, MongoDB listens for connections from clients on port
`27017`, and stores data in the `/data/db` directory.

On Windows, this path is on the drive from which you start MongoDB. For
example, if you do not specify a `--dbpath`, starting a MongoDB
server on the `C:\` drive stores all data files in `C:\data\db`.

To start MongoDB using all defaults, issue the following command at
the system shell:

```bash
mongod
```

### Specify a Data Directory

If you want `mongod` to store data files at a path *other
than* `/data/db` you can specify a `dbPath`. The
`dbPath` must exist before you start `mongod`. If it
does not exist, create the directory and the permissions so that
`mongod` can read and write data to this path. For more
information on permissions, see the security operations
documentation.

To specify a `dbPath` for `mongod` to use as a data
directory, use the `--dbpath` option. The
following invocation will start a `mongod` instance and store
data in the `/srv/mongodb` path

```bash
mongod --dbpath /srv/mongodb/
```

**Note:**

`mongod` includes a Full Time Diagnostic Data Capture mechanism to assist MongoDB engineers with troubleshooting
deployments. If this thread fails, it terminates the originating process.
To avoid the most common failures, confirm that the user running the
process has permissions to create the FTDC `diagnostic.data`
directory. For `mongod` the directory is within
`storage.dbPath`. For `mongos` it is parallel to `systemLog.path`.

### Specify a TCP Port

Only a single process can listen for connections on a network
interface at a time. If you run multiple `mongod` processes
on a single machine, or have other processes that must use this port,
you must assign each a different port to listen on for client
connections.

To specify a port to `mongod`, use the `--port` option on the command line. The following command
starts `mongod` listening on port `12345`:

```bash
mongod --port 12345
```

Use the default port number when possible, to avoid confusion.

### Start `mongod` as a Daemon

To run a `mongod` process as a daemon (i.e. `fork`),
*and* write its output to a log file, use the `--fork` and `--logpath`
options. You must create the log directory; however, `mongod`
creates the log file if it does not exist.

The following command starts `mongod` as a daemon and records log
output to `/var/log/mongodb/mongod.log`.

```bash
mongod --fork --logpath /var/log/mongodb/mongod.log
```

### Additional Configuration Options

For an overview of common configurations and deployments
for common use cases, see
/administration/configuration.

## Stop `mongod` Processes

In a clean shutdown a `mongod` completes all pending
operations, flushes all data to data files, and closes all data
files. Other shutdowns are *unclean* and can compromise the validity of the
data files.

To ensure a clean shutdown, always shutdown `mongod`
instances using one of the following methods:

### Use `shutdownServer()`

Shut down the `mongod` from `mongosh` using
the `db.shutdownServer()` method as follows:

```javascript
use admin
db.shutdownServer()
```

Calling the same method from a init script accomplishes the same result.

For systems with `authorization` enabled, users may only issue
`db.shutdownServer()` when authenticated to the `admin`
database or via the localhost interface on systems without
authentication enabled.

### Use `--shutdown`

Supported on Linux only. From the command line, shut down the 
`mongod` using the `--shutdown`
option:

```bash
mongod --shutdown
```

### Use `CTRL-C`

When running the `mongod` instance in interactive mode
(i.e. without `--fork`), issue `Control-C`
to perform a clean shutdown.

### Use `kill`

Supported on Linux and macOS only. From the command line, shut down a 
specific `mongod` instance using one of the following 
commands:

```none
kill <mongod process ID>
kill -2 <mongod process ID>
```

#### `SIGTERM` and Replica Sets

If a replica set primary receives a `SIGTERM`, the primary attempts 
to step down before shutting down. 

- If the step down succeeds, the instance does not vote in the ensuing
  election of the new primary, and continues its shutdown.

- If the step down fails, the instance continues its shutdown.

#### `SIGKILL`

**Warning:**

Never use `kill -9` (i.e. `SIGKILL`) to terminate a mongod instance.

## Troubleshoot `mongod` Processes

### Generate a Backtrace

For MongoDB instances running on Linux:

- When the `mongod` and `mongos` processes
  receive a `SIGUSR2` signal, backtrace details are added to the logs
  for each process thread.

- Backtrace details show the function calls for the process, which can
  be used for diagnostics and provided to MongoDB Support if required.

The backtrace functionality is available for these architectures:

- `x86_64`
- `arm64` (starting in MongoDB 5.0.10, and 6.0)

To issue a `SIGUSR2` signal to a running `mongod`
process, use the following command:

```none
kill -SIGUSR2 <mongod process ID>
```

The resulting backtrace data is written to the `mongod`
logfile as configured with `--logpath`.

## Stop a Replica Set

### Procedure

If the `mongod` is the primary in a replica
set, the shutdown process for this `mongod` instance has
the following steps:

#. Check how up-to-date the secondaries are.

#. If no secondary is within 10 seconds of the primary,
   `mongod` will return a message that it will not shut down.
   You can pass the `shutdown` command a `timeoutSecs`
   argument to wait for a secondary to catch up.

#. If there is a secondary within 10 seconds of the primary, the primary
   will step down and wait for the secondary to catch up.

#. After 60 seconds or once the secondary has caught up, the primary
   will shut down.

### Force Replica Set Shutdown

If there is no up-to-date secondary and you want the primary to shut
down, issue the `shutdown` command with the `force`
argument, as in the following `mongosh` operation:

```javascript
db.adminCommand({shutdown : 1, force : true})
```

To keep checking the secondaries for a specified number of seconds if
none are immediately up-to-date, issue `shutdown` with the
`timeoutSecs` argument. MongoDB will keep checking the secondaries for
the specified number of seconds if none are immediately up-to-date. If
any of the secondaries catch up within the allotted time, the primary
will shut down. If no secondaries catch up, it will not shut down.

The following command issues `shutdown` with `timeoutSecs`
set to `5`:

```javascript
db.adminCommand({shutdown : 1, timeoutSecs : 5})
```

Alternately you can use the `timeoutSecs` argument with the
`db.shutdownServer()` method:

```javascript
db.shutdownServer({timeoutSecs : 5})
```
