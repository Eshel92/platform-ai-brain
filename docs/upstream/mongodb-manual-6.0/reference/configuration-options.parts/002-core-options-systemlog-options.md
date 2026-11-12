<!-- Part 2 of 7 of reference/configuration-options.md (split because the page is big). -->

### `systemLog` Options

```yaml
systemLog:
   verbosity: <int>
   quiet: <boolean>
   traceAllExceptions: <boolean>
   syslogFacility: <string>
   path: <string>
   logAppend: <boolean>
   logRotate: <string>
   destination: <string>
   timeStampFormat: <string>
   component:
      accessControl:
         verbosity: <int>
      command:
         verbosity: <int>

      # COMMENT additional component verbosity settings omitted for brevity
```

**`systemLog.verbosity`**

*Type*: integer

*Default*: 0

The default log message
verbosity level for components. The
verbosity level determines the amount of Informational and
Debug messages MongoDB outputs. [#log-message]_

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

To use a different verbosity level for a named component, use the
component's verbosity setting. For example, use the
`systemLog.component.accessControl.verbosity` to set the
verbosity level specifically for `ACCESS` components.

See the `systemLog.component.<name>.verbosity` settings for
specific component verbosity settings.

For various ways to set the log verbosity level, see
log-messages-configure-verbosity.

   

**`systemLog.quiet`**

*Type*: boolean

*Default*: false

Run `mongos` or `mongod` in a quiet mode
that attempts to limit the amount of output.

`systemLog.quiet` is **not** recommended for production
systems as it may make tracking problems during particular
connections much more difficult.

**`systemLog.traceAllExceptions`**

*Type*: boolean

*Default*: false

Print verbose information for debugging. Use for additional logging
for support-related troubleshooting.
   

**`systemLog.syslogFacility`**

*Type*: string

*Default*: user

The facility level used when logging messages to syslog.
The value you specify must be supported by your
operating system's implementation of syslog. To use this option, you
must  set `systemLog.destination` to `syslog`.

**`systemLog.path`**

*Type*: string

The path of the log file to which `mongod` or `mongos` should send all diagnostic
logging information, rather than the standard output or the host's
syslog. MongoDB creates the log file at the specified path.

The Linux package init scripts do not expect `systemLog.path` to change from the
defaults. If you use the Linux packages and change `systemLog.path`, you must
use your own init scripts and disable the built-in scripts.

   

**`systemLog.logAppend`**

*Type*: boolean

*Default*: false

When `true`, `mongos` or `mongod`
appends new entries to the end of the existing log file when
the instance restarts. Without this option,
`mongod` or `mongos` backs up the
existing log and create a new file.

**`systemLog.logRotate`**

*Type*: string

*Default*: rename

Determines the behavior for the `logRotate` command when
rotating the server log and/or the audit log. Specify either
`rename` or `reopen`:

- `rename` renames the log file.

- `reopen` closes and reopens the log file following the typical
  Linux/Unix log rotate behavior. Use `reopen` when using the
  Linux/Unix logrotate utility to avoid log loss.

  If you specify `reopen`, you must also set `systemLog.logAppend` to `true`.

**`systemLog.destination`**

*Type*: string

The destination to which MongoDB sends all log output. Specify either
`file` or `syslog`. If you specify `file`, you must also specify
`systemLog.path`.

If you do not specify `systemLog.destination`, MongoDB sends
all log output to standard output.

**Warning:**

The `syslog` daemon generates timestamps when it logs a message, not
when MongoDB issues the message. This can lead to misleading timestamps
for log entries, especially when the system is under heavy load. We
recommend using the `file` option for production systems to ensure
accurate timestamps.

   

**`systemLog.timeStampFormat`**

*Type*: string

*Default*: iso8601-local

The time format for timestamps in log messages. Specify one of the
following values:

| Value | Description |
|---|---|
| `iso8601-utc` | Displays timestamps in Coordinated Universal Time (UTC) in the ISO-8601 format. For example, for New York at the start of the Epoch: `1970-01-01T00:00:00.000Z` |
| `iso8601-local` | Displays timestamps in local time in the ISO-8601 format. For example, for New York at the start of the Epoch: `1969-12-31T19:00:00.000-05:00` |

**Note:**

`systemLog.timeStampFormat` no longer supports `ctime`. An example of `ctime` 
formatted date is: `Wed Dec 31 18:17:54.811`.

#### `systemLog.component` Options

```yaml
systemLog:
   component:
      accessControl:
         verbosity: <int>
      command:
         verbosity: <int>

      # COMMENT some component verbosity settings omitted for brevity

      replication:
         verbosity: <int>
         election:
            verbosity: <int>
         heartbeats:
            verbosity: <int>
         initialSync:
            verbosity: <int>
         rollback:
            verbosity: <int>
      storage:
         verbosity: <int>
         journal:
            verbosity: <int>
         recovery:
            verbosity: <int>
      write:
         verbosity: <int>
```

**Note:**

Starting in version 4.2, MongoDB includes the Debug verbosity level
(1-5) in the log messages. For example,
if the verbosity level is 2, MongoDB logs `D2`. In previous
versions, MongoDB log messages only specified `D` for Debug level.

**`systemLog.component.assert.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for assertions encountered by user operations
in MongoDB. Typically an assertion is triggered when an operation returns an 
error. See `ASSERT` components.

**`systemLog.component.accessControl.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
access control. See `ACCESS` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.command.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
commands. See `COMMAND` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.control.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
control operations. See `CONTROL` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.ftdc.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
diagnostic data collection operations. See `FTDC` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.geo.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
geospatial parsing operations. See `GEO` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.index.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
indexing operations. See `INDEX` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.network.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
networking operations. See `NETWORK` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.query.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
query operations. See `QUERY` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.queryStats.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to invocations of 
`$queryStats`. See `QUERYSTATS` components.

The verbosity level can range from `0` to `5`:

- `0` is the default log verbosity level, and only includes
  informational messages. No `$queryStats` 
  calls are logged at this level. 

- `1` to `2` increases the verbosity level to include `$queryStats` 
  calls where `algorithm` is `"hmac-sha-256"`. Any HMAC keys are 
  redacted. 

- `3` to `5` increases the verbosity level to include 
  `$queryStats` calls where `algorithm` is 
  `"hmac-sha-256"`, and the corresponding results. Each result is its own 
  entry and there is a final entry with the string `"we finished"`.

**`systemLog.component.replication.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
replication. See `REPL` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.replication.election.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
election. See `ELECTION` components.

If `systemLog.component.replication.election.verbosity` is unset,
`systemLog.component.replication.verbosity` level also applies to
election components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.replication.heartbeats.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
heartbeats. See `REPL_HB` components.

If `systemLog.component.replication.heartbeats.verbosity` is unset,
`systemLog.component.replication.verbosity` level also applies to
heartbeats components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.replication.initialSync.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
initialSync. See `INITSYNC` components.

If `systemLog.component.replication.initialSync.verbosity` is unset,
`systemLog.component.replication.verbosity` level also applies to
initialSync components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.replication.rollback.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
rollback. See `ROLLBACK` components.

If `systemLog.component.replication.rollback.verbosity` is unset,
`systemLog.component.replication.verbosity` level also applies to
rollback components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.sharding.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
sharding. See `SHARDING` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.storage.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
storage. See `STORAGE` components.

If `systemLog.component.storage.journal.verbosity` is unset,
`systemLog.component.storage.verbosity` level also applies to
journaling components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.storage.journal.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
journaling. See `JOURNAL` components.

If `systemLog.component.storage.journal.verbosity` is
unset, the journaling components have the same verbosity level as the
parent storage components: i.e. either the
`systemLog.component.storage.verbosity` level if
set or the default verbosity level.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

   

**`systemLog.component.storage.recovery.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
recovery. See `RECOVERY` components.

If `systemLog.component.storage.recovery.verbosity` is unset,
`systemLog.component.storage.verbosity` level also applies to
recovery components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity level for components related to the
WiredTiger
storage engine. See `WT` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtBackup.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity level for components related to backup operations
performed by the WiredTiger storage engine.
See `WTBACKUP` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtCheckpoint.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to checkpoint operations
performed by the WiredTiger storage engine.
See `WTCHKPT` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtCompact.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to compaction operations
performed by the WiredTiger storage engine.
See `WTCMPCT` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtEviction.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to eviction operations
performed by the WiredTiger storage engine.
See `WTEVICT` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtHS.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to history store operations
performed by the WiredTiger storage engine.
See `WTHS` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtRecovery.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to recovery operations
performed by the WiredTiger storage engine.
See `WTRECOV` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtRTS.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to rollback to stable
(RTS) operations performed by the
WiredTiger storage engine.
See `WTRTS` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtSalvage.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to salvage operations
performed by the WiredTiger storage engine.
See `WTSLVG` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtTimestamp.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to timestamps
used by the WiredTiger storage engine.
See `WTTS` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtTransaction.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to transaction operations
performed by the WiredTiger storage engine.
See `WTTXN` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtVerify.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to verification operations
performed by the WiredTiger storage engine.
See `WTVRFY` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.storage.wt.wtWriteLog.verbosity`**

*Type*: integer

*Default*: -1

**New in version:** 5.3

The log message verbosity for components related to log write operations
performed by the WiredTiger storage engine.
See `WTWRTLOG` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.transaction.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
transaction. See `TXN` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

**`systemLog.component.write.verbosity`**

*Type*: integer

*Default*: 0

The log message verbosity level for components related to
write operations. See `WRITE` components.

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.
