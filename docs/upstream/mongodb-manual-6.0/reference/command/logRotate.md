<!-- Converted from reference/command/logRotate.txt (reStructuredText). Includes are inlined. -->

# logRotate

## Definition

**`logRotate`**

The `logRotate` command is an administrative command that
allows you to rotate the MongoDB server log and/or audit log to
prevent a single logfile from consuming too much disk space.

You must issue the `logRotate` command against the
admin database.

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
     logRotate: <integer or string>,
     comment: <string>
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `logRotate`
  - integer or string
  - The log or logs to rotate, according to the following:

    - `1`  -- Rotates both the server and audit logs
    - `"server"` -- Rotates only the server log
    - `"audit"`  -- Rotates only the audit log

* - `comment`
  - string
  - *Optional.* A message logged by the server to the log file and
    audit file at time of log rotation.
 
You may also rotate the logs by sending a `SIGUSR1` signal to the
`mongod` process.

For example, if a running `mongod` instance has a
process ID (PID) of `2200`, the following command rotates the log
file for that instance on Linux:

```bash
kill -SIGUSR1 2200
```

## Limitations

- Your `mongod` instance needs to be running with the
  `--logpath [file]` option in order to use
  `logRotate`

- Auditing must be enabled in order to rotate
  the audit log.

## Behavior

The `systemLog.logRotate` setting or
`--logRotate` option specify
`logRotate`'s behavior.

When `systemLog.logRotate` or `--logRotate` are set to `rename`, `logRotate`
renames the existing log file by appending the current timestamp to the
filename. The appended timestamp has the following form:

```none
<YYYY>-<mm>-<DD>T<HH>-<MM>-<SS>
```

Then `logRotate` creates a new log file with the same
name as originally specified by the `systemLog.path` setting to
`mongod` or `mongos`.

When `systemLog.logRotate` or `--logRotate` are set to `reopen`, `logRotate`
follows the typical Linux/Unix behavior, and simply closes the log file
then reopens a log file with the same name. With `reopen`,
`mongod` expects that another process renames the file
prior to the rotation, and that the reopen results in the creation of a
new file.

## Examples

The following example rotates both the server log and the audit log:

```javascript
db.adminCommand( { logRotate: 1 } )
```

The following example rotates only the audit log, and provides a custom
message to the log file at time of rotation:

```javascript
db.adminCommand( { logRotate: "audit", comment: "Rotating audit log" } )
```
