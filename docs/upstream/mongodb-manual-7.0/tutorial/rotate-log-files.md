<!-- Converted from tutorial/rotate-log-files.txt (reStructuredText). Includes are inlined. -->

# Rotate Log Files

## Overview

When used with the `--logpath` option or `systemLog.path`
setting, `mongod` and `mongos` instances
report a live account of all activity and operations to a log file. 
When reporting activity data to a log file, by default, MongoDB only
rotates logs in response to the `logRotate` command, or when
the `mongod` or `mongos` process receives a
`SIGUSR1` signal from the operating system. Both server logs and
audit logs may be rotated with the
`logRotate` command, either together or independently.

MongoDB's standard log rotation approach archives the current
log file and starts a new one. To do this, the `mongod` or
`mongos` instance renames the current log file by appending
a UTC timestamp to the filename, in ISODate format. It then
opens a new log file, closes the old log file, and sends all new log
entries to the new log file.

You can also configure MongoDB to support the Linux/Unix `logrotate`
utility by setting `systemLog.logRotate` or
`--logRotate` to `reopen`. With `reopen`, `mongod`
or `mongos` closes the log file, and
then reopens a log file with the same name, expecting that another
process renamed the file prior to rotation.

Finally, you can configure `mongod` to send log data to the
`syslog` using the `--syslog` option. In
this case, you can take advantage of alternate log rotation tools.

**Note:**

`logRotate` isn't a replicated command. You must connect 
to each instance of a replica set and run `logRotate` 
to rotate the logs for replica set members.

To rotate the log files, you must perform one of these steps:

- Send a `SIGUSR1` signal to the `mongod` or
  `mongos` process.

- Run the MongoDB `logRotate` command.

- Run the Linux/Unix `logrotate` utility.

See the examples later on this page.

**See also:**

For information on logging, see the
monitoring-standard-loggging section.

## Default Log Rotation Behavior

By default, MongoDB uses the
`--logRotate rename` behavior. 
With `rename`, `mongod` or
`mongos` renames the current log file by appending a UTC 
timestamp to the filename, opens a new log file, closes the old log
file, and sends all new log entries to the new log file.

**Step 1: Start a `mongod` instance.**

```sh
mongod -v --logpath /var/log/mongodb/server1.log
```

You can also explicitly specify `--logRotate rename`.

**Step 2: List the log files**

In a separate terminal, list the matching files:

```sh
ls /var/log/mongodb/server1.log*
```

The results should include one log file, `server1.log`.

**Step 3: Rotate the log file.**

Rotate the log file by issuing the `logRotate` command
from the `admin` database in `mongosh`:

```sh
db.adminCommand( { logRotate : "server" } )
```

If auditing is enabled, you can specify `1`
to `logRotate` (instead of  `server`) to rotate both the server
and audit logs at the same time, if desired. The audit log will be
rotated in the same fashion as the server log, according to the
`--logRotate` setting.

**Note:**

You can't run this command on an arbiter for an authenticated
replica set.

**Step 4: View the new log files**

List the new log files to view the newly-created log:

```sh
ls /var/log/mongodb/server1.log*
```

There should be two log files listed: `server1.log`, which is the
log file that `mongod` or `mongos` made when it 
reopened  the log file, and `server1.log.<timestamp>`, the renamed
original log file.

Rotating log files does not modify the "old" rotated log files. When
you rotate a log, you rename the `server1.log` file to include
the timestamp, and a new, empty `server1.log` file receives all
new log input.

## Log Rotation with `--logRotate reopen`

Log rotation with `--logRotate reopen` closes and opens
the log file following the typical Linux/Unix log rotate behavior.

**Step 1: Start a `mongod` instance, specifying the `reopen` `--logRotate` behavior.**

```sh
mongod -v --logpath /var/log/mongodb/server1.log --logRotate reopen --logappend
```

You must use the `--logappend` option with
`--logRotate reopen`.

**Step 2: List the log files**

In a separate terminal, list the matching files:

```sh
ls /var/log/mongodb/server1.log*
```

The results should include one log file, `server1.log`.

**Step 3: Rotate the log file.**

Rotate the log file by issuing the `logRotate` command
from the `admin` database in `mongosh`:

```sh
db.adminCommand( { logRotate : "server" } )
```

You should rename the log file using an external process, following
the typical Linux/Unix log rotate behavior.

## Syslog Log Rotation

With syslog log rotation, `mongod` sends log data to the
syslog rather than writing it to a file.

MongoDB includes the component in its log 
messages to `syslog`.

**Step 1: Start a `mongod` instance with the `--syslog` option**

```sh
mongod --syslog
```

Do not include `--logpath`. Since `--syslog` tells
`mongod` to send log data to the syslog, specifying a
`--logpath` will causes an error.

To specify the facility level used when logging messages to the syslog,
use the `--syslogFacility` option or
`systemLog.syslogFacility` configuration setting.

**Step 2: Rotate the log.**

Store and rotate the log output using your systems default log
rotation mechanism.

## Forcing a Log Rotation with `SIGUSR1`

For Linux and Unix-based systems, you can use the `SIGUSR1` signal
to rotate the logs for a single process.

For example, if a running `mongod` instance has a
process ID (PID) of `2200`, the following command rotates the log
file for that instance on Linux:

```bash
kill -SIGUSR1 2200
```
