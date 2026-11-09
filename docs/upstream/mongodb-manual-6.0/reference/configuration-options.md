<!-- Converted from reference/configuration-options.txt (reStructuredText). Includes are inlined. -->

# Self-Managed Configuration File Options

The following page describes the configuration options available in
MongoDB 6.0. For configuration file options for other 
versions of MongoDB, see the appropriate version of the MongoDB Manual.

**Note:**

If you're using MongoDB Atlas to manage your MongoDB deployments in the
cloud, you don't need to create a configuration file. To learn how 
to configure settings for your MongoDB Atlas deployment, see 
Configure Additional Settings.

In addition to using the configuration file options, the default
configuration for the MongoDB binaries also uses the operating system
environment variables.

## Configuration File

You can configure `mongod` and `mongos` instances at
startup using a configuration file. The configuration file contains
settings that are equivalent to the `mongod` and
`mongos` command-line options. See conf-file-command-line-mapping.

Using a configuration file makes managing `mongod` and
`mongos` options easier, especially for large-scale
deployments. You can also add comments to the configuration file to
explain the server's settings.

- If you installed MongoDB with a package manager
  such as `yum` or `apt` on Linux or `brew` on macOS, or with the
  MSI installer on Windows, a default configuration file has been provided as part of your
  installation:

  | Platform | Method | Configuration File |
  |---|---|---|
  | Linux | `apt`, `yum`, or `zypper` Package Manager | `/etc/mongod.conf` |
  | macOS | `brew` Package Manager | `/usr/local/etc/mongod.conf` (on Intel processors), or `/opt/homebrew/etc/mongod.conf` (on [Apple Silicon processors](https://support.apple.com/en-us/HT211814)) |
  | Windows | MSI Installer | `<install directory>\bin\mongod.cfg` |

- If you installed MongoDB
  through a downloaded `TGZ` or `ZIP` file, you must create
  your own configuration file. The basic example
  configuration is a good place to start.

### File Format

MongoDB configuration files use the [YAML](http://www.yaml.org) format
[#yaml-json]_.

The following sample configuration file contains several `mongod`
settings that you may adapt to your local configuration:

**Note:**

YAML does not support tab characters for indentation: use spaces instead.

```yaml
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
storage:
   journal:
      enabled: true
processManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
...
```

The Linux package init scripts included in the official MongoDB packages depend
on specific values for `systemLog.path`, `storage.dbPath`, and
`processManagement.fork`. If you modify these settings in the default
configuration file, `mongod` may not start.

#### Externally Sourced Values

**Note:**

MongoDB supports using 
expansion directives in configuration 
files to load externally sourced values. Expansion directives can
load values for specific 
configuration file options *or* load the 
entire configuration file.

The following expansion directives are available:

| Expansion Directive | Description |
|---|---|
| `__rest` | Allows users to specify a `REST` endpoint as the external source for configuration file options *or* the full configuration file. If the configuration file includes the `__rest` expansion, on Linux/macOS, the read access to the configuration file must be limited to the user running the `mongod` / `mongos` process only. |
| `__exec` | Allows users to specify a shell or terminal command as the external source for configuration file options *or* the full configuration file. If the configuration file includes the `__exec` expansion, on Linux/macOS, the write access to the configuration file must be limited to the user running the `mongod` / `mongos` process only. |

For complete documentation, see externally-sourced-values.

### Use the Configuration File

To configure `mongod` or `mongos` using a config file,
specify the config file with the `--config` option or the
`-f` option, as in the following examples:

For example, the following uses `mongod --config
<configuration file>` `mongos --config
<configuration file>`:

```bash
mongod --config /etc/mongod.conf

mongos --config /etc/mongos.conf
```

You can also use the `-f` alias to specify the configuration
file, as in the following:

```bash
mongod -f /etc/mongod.conf

mongos -f /etc/mongos.conf
```

If you installed from a package and have started MongoDB using your
system's init script, you are already using a configuration
file.

#### Expansion Directives and `--configExpand`

If you are using expansion directives
in the configuration file, you must include the
`--configExpand` option when starting
the `mongod` or `mongos`. For example:

```bash
mongod --config /etc/mongod.conf  --configExpand "rest,exec"
mongos --config /etc/mongos.conf  --configExpand "rest,exec"
```

If the configuration file includes an expansion directive and you start
the `mongod` / `mongos` without specifying
that directive in the `--configExpand`
option, the `mongod` / `mongos` fails to start.

For complete documentation, see externally-sourced-values.

## Core Options

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

   

### `processManagement` Options

```yaml
processManagement:
   fork: <boolean>
   pidFilePath: <string>
   timeZoneInfo: <string>
```

**`processManagement.fork`**

*Type*: boolean

*Default*: false

Enable a daemon mode that runs the `mongos` or
`mongod` process in the background. By default 
`mongos` or `mongod` does not run as a daemon.
To use `mongos` or `mongod` as a daemon, set 
`processManagement.fork` or use a controlling process that 
handles the daemonization process (for example, `systemd`).

The `processManagement.fork` option is not supported on Windows.

The Linux package init scripts do not expect `processManagement.fork` to change from the
defaults. If you use the Linux packages and change `processManagement.fork`, you must
use your own init scripts and disable the built-in scripts.

   

**`processManagement.pidFilePath`**

*Type*: string

Specifies a file location to store the process ID (PID) of the `mongos` or `mongod`
process. The user running the `mongod` or `mongos`
process must be able to write to this path. If the `processManagement.pidFilePath` option is not
specified, the process does not create a PID file. This option is generally
only useful in combination with the `processManagement.fork` setting.

**Note:** Linux

On Linux, PID file management is generally the responsibility of
your distro's init system: usually a service file in the `/etc/init.d`
directory, or a systemd unit file registered with `systemctl`. Only
use the `processManagement.pidFilePath` option if you are not using one of these init
systems. For more information, please see the respective
Installation Guide for your operating system.

**Note:** macOS

On macOS, PID file management is generally handled by `brew`. Only use
the `processManagement.pidFilePath` option if you are not using `brew` on your macOS system. 
For more information, please see the respective
Installation Guide for your operating system.

**`processManagement.timeZoneInfo`**

*Type*: string

The full path from which to load the time zone database. If this option
is not provided, then MongoDB uses its built-in time zone database.

The configuration file included with Linux and macOS packages sets the
time zone database path to `/usr/share/zoneinfo` by default.

The built-in time zone database is a copy of the [Olson/IANA time zone database](https://www.iana.org/time-zones). It is updated along with
MongoDB releases, but the time zone database release cycle
differs from the MongoDB release cycle. The most recent release of
the time zone database is available on our [download site](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).

**Warning:**

MongoDB uses the third party [timelib](https://github.com/derickr/timelib) library to provide accurate
conversions between timezones. Due to a recent update, `timelib`
could create inaccurate time zone conversions in older versions of
MongoDB.

To explicitly link to the time zone database in versions of MongoDB
prior to 5.0, download the [time zone database](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).
and use the `timeZoneInfo` parameter.

### `net` Options

**Changed in version:** 5.0

MongoDB removes the `net.serviceExecutor` configuration option and the
corresponding `--serviceExecutor` command-line option.

```yaml
net:
   port: <int>
   bindIp: <string>
   bindIpAll: <boolean>
   maxIncomingConnections: <int>
   wireObjectCheck: <boolean>
   ipv6: <boolean>
   unixDomainSocket:
      enabled: <boolean>
      pathPrefix: <string>
      filePermissions: <int>
   tls:
      certificateSelector: <string>
      clusterCertificateSelector: <string>
      mode: <string>
      certificateKeyFile: <string>
      certificateKeyFilePassword: <string>
      clusterFile: <string>
      clusterPassword: <string>
      CAFile: <string>
      clusterCAFile: <string>
      CRLFile: <string>
      allowConnectionsWithoutCertificates: <boolean>
      allowInvalidCertificates: <boolean>
      allowInvalidHostnames: <boolean>
      disabledProtocols: <string>
      FIPSMode: <boolean>
      logVersions: <string>
   compression:
      compressors: <string>
```

**`net.port`**

*Type*: integer

*Default*:

- 27017 for `mongod` (if not a shard member or a config server
  member) or `mongos` instance

- 27018 if `mongod` is a `shard member`

- 27019 if `mongod` is a `config server member`

The TCP port on which the MongoDB instance listens for
client connections.

**Changed in version:** 6.0.12

The `net.port` option accepts a range of values between `0` and `65535`.
Setting the port to `0` configures `mongos` or `mongod` to use an arbitrary
port assigned by the operating system.

**`net.bindIp`**

*Type*: string

*Default*: localhost

The hostnames and/or IP addresses and/or full Unix domain socket
paths on which `mongos` or `mongod` should
listen for client connections. You may attach `mongos`
or `mongod` to any interface. To bind to multiple
addresses, enter a list of comma-separated values.

**Example:**

`localhost,/tmp/mongod.sock`

You can specify both IPv4 and IPv6 addresses, or hostnames that
resolve to an IPv4 or IPv6 address.

**Example:**

`localhost, 2001:0DB8:e132:ba26:0d5c:2774:e7f9:d513`

**Note:**

If specifying an IPv6 address *or* a hostname that resolves to an
IPv6 address to `net.bindIp`, you must start
`mongos` or `mongod` with
`net.ipv6 : true` to enable IPv6 support.
Specifying an IPv6 address to `net.bindIp` does not
enable IPv6 support.

If specifying a 
[link-local IPv6 address](https://en.wikipedia.org/wiki/Link-local_address#IPv6)
(`fe80::/10`), you must append the 
[zone index](https://en.wikipedia.org/wiki/IPv6_address#Scoped_literal_IPv6_addresses_(with_zone_index))
to that address (i.e. `fe80::<address>%<adapter-name>`). 

**Example:**

`localhost,fe80::a00:27ff:fee0:1fcf%enp0s3`

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information about IP Binding, refer to the
/core/security-mongodb-configuration documentation.

To bind to all IPv4 addresses, enter `0.0.0.0`.

To bind to all IPv4 and IPv6 addresses, enter `::,0.0.0.0` or
an asterisk `"*"` (enclose the asterisk in quotes to distinguish from 
[YAML alias nodes](https://yaml.org/spec/1.2/spec.html#alias/)). 
Alternatively, use the `net.bindIpAll` setting.

**Note:**

- `net.bindIp` and `net.bindIpAll` are mutually
  exclusive. That is, you can specify one or the other, but not
  both.

- The command-line option `--bind_ip` overrides the configuration
  file setting `net.bindIp`.

To configure cluster nodes for [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS), use host names
instead of IP addresses. 

Starting in MongoDB v5.0, `replSetInitiate` and 
`replSetReconfig` reject configurations that use IP
addresses instead of hostnames.

Use `disableSplitHorizonIPCheck` to modify nodes that
cannot be updated to use host names. The parameter only applies to the
configuration commands. 

`mongod` and `mongos` do not rely on
`disableSplitHorizonIPCheck` for validation at startup.
Legacy `mongod` and `mongos` instances that use IP
addresses instead of host names can start after an upgrade. 

Instances that are configured with IP addresses log a warning to use
host names instead of IP addresses. 

**`net.bindIpAll`**

*Type*: boolean

*Default*: false

If true, the `mongos` or `mongod` instance binds to all IPv4
addresses (i.e. `0.0.0.0`). If `mongos` or `mongod` starts with
`net.ipv6 : true`, `net.bindIpAll` also binds to all IPv6 addresses
(i.e. `::`). 

`mongos` or `mongod` only supports IPv6 if started with `net.ipv6 : true`. Specifying
`net.bindIpAll` alone does not enable IPv6 support.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information about IP Binding, refer to the
/core/security-mongodb-configuration documentation.

Alternatively, set `net.bindIp` to `::,0.0.0.0` or to an asterisk 
`"*"` (enclose the asterisk in quotes to distinguish from [YAML alias nodes](https://yaml.org/spec/1.2/spec.html#alias/)) to bind to all IP
addresses.

**Note:**

`net.bindIp` and `net.bindIpAll` are mutually
exclusive. Specifying both options causes `mongos` or `mongod` to throw
an error and terminate.

**`net.maxIncomingConnections`**

*Type*: integer

| *Default (Windows):* 1,000,000
| *Default (Linux):* ([RLIMIT_NOFILE](https://man7.org/linux/man-pages/man2/getrlimit.2.html)) * 0.8

The maximum number of simultaneous connections that `mongos` or `mongod`
accepts. This setting has no effect if it is higher than your operating
system's configured maximum connection tracking threshold.

Do not assign too low of a value to this option, or you may 
encounter errors during normal application operation.

This is particularly useful for a `mongos` if you have a client
that creates multiple connections and allows them to timeout rather
than closing them.

In this case, set `maxIncomingConnections` to a value slightly
higher than the maximum number of connections that the client creates, or the
maximum size of the connection pool.

This setting prevents the `mongos` from causing connection spikes on
the individual shards. Spikes like these may disrupt the
operation and memory allocation of the sharded cluster.

**`net.wireObjectCheck`**

*Type*: boolean

*Default*: true

When `true`, the `mongod` or `mongos` instance  validates
all requests from clients upon receipt to prevent clients from inserting
malformed or invalid BSON into a MongoDB database.

For objects with a high degree of sub-document nesting, `net.wireObjectCheck` can
have a small impact on performance.

**`net.ipv6`**

*Type*: boolean

*Default*: false

Set `net.ipv6` to `true` to enable IPv6 support. `mongos`/`mongod` disables IPv6 support by default.

Setting `net.ipv6` does *not* direct the `mongos`/`mongod` to listen on any
local IPv6 addresses or interfaces. To configure the `mongos`/`mongod` to
listen on an IPv6 interface, you must either:

- Configure `net.bindIp` with one or more IPv6 addresses or
  hostnames that resolve to IPv6 addresses, **or**
- Set `net.bindIpAll` to `true`.

#### `net.unixDomainSocket` Options

```yaml
net:
   unixDomainSocket:
      enabled: <boolean>
      pathPrefix: <string>
      filePermissions: <int>
```

**`net.unixDomainSocket.enabled`**

*Type*: boolean

*Default*: true

Enable or disable listening on the UNIX domain socket. `net.unixDomainSocket.enabled` applies only
to Unix-based systems.

When `net.unixDomainSocket.enabled` is `true`, `mongos` or `mongod` listens on the UNIX socket.

The `mongos` or `mongod` process always listens on the UNIX socket unless
one of the following is true:

- `net.unixDomainSocket.enabled` is `false`

- `--nounixsocket` is set. The command
  line option takes precedence over the configuration file setting.

- `net.bindIp` is not set

- `net.bindIp` does not specify `localhost` or its associated IP address

`mongos` or `mongod` installed from official install-mdb-community-debian 
and install-mdb-community-redhat-centos packages
have the `bind_ip` configuration set to `127.0.0.1` by
default.

**`net.unixDomainSocket.pathPrefix`**

*Type*: string

*Default*: /tmp

The path for the UNIX socket. `net.unixDomainSocket.pathPrefix` applies only
to Unix-based systems.

If this option has no value, the
`mongos` or `mongod` process creates a socket with `/tmp` as a prefix. MongoDB
creates and listens on a UNIX socket unless one of the following is true:

- `net.unixDomainSocket.enabled` is `false`

- `--nounixsocket` is set

- `net.bindIp` is not set

- `net.bindIp` does not specify `localhost` or its associated IP address

**`net.unixDomainSocket.filePermissions`**

*Type*: int

*Default*: `0700`

Sets the permission for the UNIX domain socket file.

`net.unixDomainSocket.filePermissions` applies only to Unix-based systems.

#### `net.tls` Options

**Note:**

The `tls` options provide identical functionality as the
previous `ssl` options.

```yaml
net:
   tls:
      mode: <string>
      certificateKeyFile: <string>
      certificateKeyFilePassword: <string>
      certificateSelector: <string>
      clusterCertificateSelector: <string>
      clusterFile: <string>
      clusterPassword: <string>
      CAFile: <string>
      clusterCAFile: <string>
      CRLFile: <string>
      allowConnectionsWithoutCertificates: <boolean>
      allowInvalidCertificates: <boolean>
      allowInvalidHostnames: <boolean>
      disabledProtocols: <string>
      FIPSMode: <boolean>
      logVersions: <string>
```

**`net.tls.mode`**

*Type*: string

Enables TLS used for all network connections. The
argument to the `net.tls.mode` setting can be one of the following:

| Value | Description |
|---|---|
| `disabled` | The server does not use TLS. |
| `allowTLS` | Connections between servers do not use TLS. For incoming connections, the server accepts both TLS and non-TLS. |
| `preferTLS` | Connections between servers use TLS. For incoming connections, the server accepts both TLS and non-TLS. |
| `requireTLS` | The server uses and accepts only TLS encrypted connections. |

If `--tlsCAFile` or `tls.CAFile` is not
specified and you are not using X.509 authentication, you must set the 
`tlsUseSystemCA` parameter to `true`. This makes MongoDB use 
the system-wide CA certificate store when connecting to a TLS-enabled server.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.certificateKeyFile`**

*Type*: string

The `.pem` file that contains both the TLS certificate
and key.

On macOS or Windows, you can use the `net.tls.certificateSelector` 
setting to specify a certificate from the operating system's secure 
certificate store instead of a PEM key file. 
`certificateKeyFile` and
`net.tls.certificateSelector` are mutually exclusive.
You can only specify one.

- On Linux/BSD, you must specify
  `net.tls.certificateKeyFile` when TLS is enabled.

- On Windows or macOS, you must specify either
  `net.tls.certificateKeyFile` or
  `net.tls.certificateSelector` when TLS is enabled.

  **Important:**

  For Windows **only**, MongoDB does not support
  encrypted PEM files. The `mongod` fails to start if
  it encounters an encrypted PEM file. To securely store and
  access a certificate for use with TLS on Windows,
  use `net.tls.certificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.certificateKeyFilePassword`**

*Type*: string

The password to de-crypt the certificate-key file (i.e.
`certificateKeyFile`). Use the
`net.tls.certificateKeyFilePassword` option only if the
certificate-key file is encrypted. In all cases, the
`mongos` or `mongod` redacts the
password from all logging and reporting output.

On Linux/BSD, if the private key in the PEM file is encrypted and
you do not specify the `net.tls.certificateKeyFilePassword` 
option, MongoDB prompts for a passphrase. 

For more information, see ssl-certificate-password.

On macOS, if the private key in the PEM file is encrypted, you must
explicitly specify the `net.tls.certificateKeyFilePassword` option.
Alternatively, you can use a certificate from the secure system
store (see `net.tls.certificateSelector`) instead of a PEM
key file or use an unencrypted PEM file.

On Windows, MongoDB does not support encrypted certificates. 
The `mongod` fails if it encounters an encrypted
PEM file. Use `net.tls.certificateSelector` instead.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.certificateSelector`**

*Type*: string

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store to use
for TLS/SSL. Available on Windows and macOS as an alternative to
`net.tls.certificateKeyFile`.

`net.tls.certificateKeyFile` and
`net.tls.certificateSelector` options are mutually
exclusive. You can only specify one.

`net.tls.certificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

When using the system SSL certificate store, OCSP (Online
Certificate Status Protocol) is used to validate the revocation
status of certificates.

The `mongod` searches the operating system's secure
certificate store for the CA certificates required to validate the
full certificate chain of the specified TLS certificate.
Specifically, the secure certificate store must contain the root CA
and any intermediate CA certificates required to build the full
certificate chain to the TLS certificate. 

**Warning:**

If you use `net.tls.certificateSelector` and/or 
`net.tls.clusterCertificateSelector`, we **do not** recommend 
using `net.tls.CAFile` or `net.tls.clusterFile` to
specify the root and intermediate CA certificate

For example, if the TLS certificate was signed with a single root
CA certificate, the secure certificate store must contain that root
CA certificate. If the TLS certificate was signed with an
intermediate CA certificate, the secure certificate store must
contain the intermedia CA certificate *and* the root CA certificate.

**Note:**

You cannot use the `rotateCertificates` command or the
`db.rotateCertificates()` shell method when using
`net.tls.certificateSelector` or
`--tlsCertificateSelector`
set to `thumbprint`

**`net.tls.clusterCertificateSelector`**

*Type*: string

Specifies a certificate property to select a matching certificate
from the operating system's secure certificate store to use for
internal X.509 membership authentication. 

Available on Windows and macOS as an alternative to
`net.tls.clusterFile`.

`net.tls.clusterFile` and
`net.tls.clusterCertificateSelector` options are mutually
exclusive. You can only specify one.

`net.tls.clusterCertificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

The `mongod` searches the operating system's secure
certificate store for the CA certificates required to validate the
full certificate chain of the specified cluster certificate.
Specifically, the secure certificate store must contain the root CA
and any intermediate CA certificates required to build the full
certificate chain to the cluster certificate. 

**Warning:**

If you use `net.tls.certificateSelector` and/or 
`net.tls.clusterCertificateSelector`, we **do not** recommend using 
`net.tls.CAFile` or `net.tls.clusterCAFile` to specify 
the root and intermediate CA certificate.

For example, if the cluster certificate was signed with a single root
CA certificate, the secure certificate store must contain that root
CA certificate. If the cluster certificate was signed with an
intermediate CA certificate, the secure certificate store must
contain the intermediate CA certificate *and* the root CA
certificate.

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

**`net.tls.clusterFile`**

*Type*: string

The `.pem` file that contains the X.509 certificate-key file
for membership authentication for the 
cluster or replica set.

On macOS or Windows, you can use the
`net.tls.clusterCertificateSelector` option to specify a
certificate from the operating system's secure certificate store
instead of a PEM key file. `net.tls.clusterFile` and
`net.tls.clusterCertificateSelector` options are mutually
exclusive. You can only specify one.   

If `net.tls.clusterFile` does not specify the `.pem` file
for internal cluster authentication or the alternative
`net.tls.clusterCertificateSelector`, the cluster uses the
`.pem` file specified in the `certificateKeyFile`
setting or the certificate returned by the
`net.tls.certificateSelector`.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**Important:**

For Windows **only**, MongoDB does not support encrypted PEM files. 
The `mongod` fails to start if it encounters an encrypted 
PEM file. To securely store and access a certificate for use with 
membership authentication on Windows, use 
`net.tls.clusterCertificateSelector`.

**`net.tls.clusterPassword`**

*Type*: string

The password to de-crypt the X.509 certificate-key file specified
with `--sslClusterFile`. Use the `net.tls.clusterPassword` option 
only if the certificate-key file is encrypted. In all cases,
`mongos` or `mongod` redacts the
password from all logging and reporting output.

On Linux/BSD, if the private key in the X.509 file is encrypted and
you do not specify the `net.tls.clusterPassword` option,
MongoDB prompts for a passphrase. 

For more information, see ssl-certificate-password.

On macOS, if the private key in the X.509 file is encrypted, you
must explicitly specify the `net.tls.clusterPassword`
option. Alternatively, you can either use a certificate from the
secure system store (see `net.tls.clusterCertificateSelector`) 
instead of a cluster PEM file or use an unencrypted PEM file.

On Windows, MongoDB does not support encrypted certificates. The 
`mongod` fails if it encounters an encrypted PEM file.
Use `net.tls.clusterCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.CAFile`**

*Type*: string

The `.pem` file that contains the root certificate chain
from the Certificate Authority. Specify the file name of the
`.pem` file using relative or absolute paths.

Windows/macOS Only
  If using `net.tls.certificateSelector` and/or
  `net.tls.clusterCertificateSelector`, do **not** use
  `net.tls.CAFile` to specify the root and intermediate CA
  certificates. Store all CA certificates required to validate the
  full trust chain of the `net.tls.certificateSelector`
  and/or `net.tls.clusterCertificateSelector` certificates
  in the secure certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.clusterCAFile`**

*Type*: string

The `.pem` file that contains the root certificate chain
from the Certificate Authority used to validate the certificate
presented by a client establishing a connection. Specify the file
name of the `.pem` file using relative or absolute paths.
`net.tls.clusterCAFile` requires that
`net.tls.CAFile` is set.

If `net.tls.clusterCAFile` does not specify the `.pem`
file for validating the certificate from a client establishing a
connection, the cluster uses the `.pem` file specified in the
`net.tls.CAFile` option.

`net.tls.clusterCAFile` lets you use separate Certificate
Authorities to verify the client to server and server to client
portions of the TLS handshake.

Starting in 4.0, on macOS or Windows, you can use a certificate from
the operating system's secure store instead of a PEM key file. See
`net.tls.clusterCertificateSelector`. When using the secure
store, you do not need to, but can, also specify the
`net.tls.clusterCAFile`.

Windows/macOS Only
  If using `net.tls.certificateSelector` and/or
  `net.tls.clusterCertificateSelector`, do **not** use
  `net.tls.clusterCAFile` to specify the root and
  intermediate CA certificates. Store all CA certificates required to
  validate the full trust chain of the
  `net.tls.certificateSelector` and/or
  `net.tls.clusterCertificateSelector` certificates in the
  secure certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.CRLFile`**

*Type*: string

The `.pem` file that contains the Certificate Revocation
List. Specify the file name of the `.pem` file using relative or
absolute paths.

**Note:**

- You cannot specify `net.tls.CRLFile` on macOS. Instead, you can 
  use the system SSL certificate store, which uses OCSP (Online
  Certificate Status Protocol) to validate the revocation status
  of certificates. See `net.tls.certificateSelector` to use the 
  system SSL certificate store.

- To check for certificate revocation, MongoDB 
  `enables` the use of OCSP
  (Online Certificate Status Protocol) by default as an alternative
  to specifying a CRL file or using the system SSL certificate
  store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.allowConnectionsWithoutCertificates`**

*Type*: boolean

*Default*: false

If `false`, all clients must provide client TLS certificates. If `true`, 
clients don't need to provide client certificates, but `mongod` 
or `mongos` encrypts the TLS/SSL connection.

If a client provides a client certificate, regardless of what value you set 
for `net.tls.allowConnectionsWithoutCertificates`, `mongos` or 
`mongod` performs certificate validation using the root 
certificate chain specified by `CAFile`, or the system 
CA store if `tlsUseSystemCA` is `true`,  and rejects 
clients with invalid certificates.

Use the `net.tls.allowConnectionsWithoutCertificates` option if you 
have a mixed deployment that includes clients that do not or cannot present 
certificates to the `mongos` or `mongod`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.allowInvalidCertificates`**

*Type*: boolean

*Default*: false

Enable or disable the validation checks for TLS certificates on other
servers in the cluster and allows the use of invalid certificates to
connect.

**Note:**

If you specify
`--tlsAllowInvalidCertificates` or ``tls.allowInvalidCertificates:
true`` when using X.509 authentication, an invalid certificate is
only sufficient to establish a TLS connection but is
*insufficient* for authentication.

When using the `net.tls.allowInvalidCertificates` setting, MongoDB
logs a warning regarding the use of the invalid certificate.

For more information about TLS and MongoDB, see 
configure-mongod-mongos-for-tls-ssl and inter-process-auth.

**`net.tls.allowInvalidHostnames`**

*Type*: boolean

*Default*: false

When `net.tls.allowInvalidHostnames` is `true`, MongoDB disables 
the validation of the hostnames in TLS certificates. This allows 
`mongod` or `mongos` to connect to other MongoDB 
instances in the cluster, even if the hostname of their certificates does not 
match the specified hostname.

For more information about TLS and MongoDB, see 
configure-mongod-mongos-for-tls-ssl.

**`net.tls.disabledProtocols`**

*Type*: string

Prevents a MongoDB server running with TLS from accepting
incoming connections that use a specific protocol or protocols. To
specify multiple protocols, use a comma separated list of protocols,
but do not use spaces after the commas. If you include a space before
a protocol name, the server interprets it as an unrecognized protocol
and doesn't start.

`net.tls.disabledProtocols` recognizes the following protocols: `TLS1_0`, `TLS1_1`,
`TLS1_2`, and `TLS1_3`.

- On macOS, you cannot disable `TLS1_1` and leave both `TLS1_0` and
  `TLS1_2` enabled. You must disable at least one of the other
  two, for example, `TLS1_0,TLS1_1`.

- To list multiple protocols, specify as a comma separated list of
  protocols without spaces after the commas. For example `TLS1_0,TLS1_1`.

- Specifying an unrecognized protocol or including a space after a
  comma prevents the server from starting.

- The specified disabled protocols overrides any default disabled
  protocols.

MongoDB disables the use of TLS 1.0 if TLS 1.1+ is available on the
system. To enable TLS 1.0, specify `none` to `net.tls.disabledProtocols`. 

Members of replica sets and sharded clusters must speak at least one
protocol in common.

**See also:**

ssl-disallow-protocols

**`net.tls.FIPSMode`**

*Type*: boolean

*Default*: false

Enable or disable the use of the FIPS mode of the  TLS
library for the `mongos` or `mongod`. Your system must have a FIPS
compliant library to use the `net.tls.FIPSMode` option.

**Note:** FIPS-compatible TLS/SSL is

available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server). See
configure-mdb-for-fips for more information.

**`net.tls.logVersions`**

*Type*: string

Instructs `mongos` or `mongod` to log a
message when a client connects using a specified TLS version.

Specify either a single TLS version or a comma-separated list of
multiple TLS versions.

**Example:**

To instruct `mongos` or `mongod` to
log a message when a client connects using either TLS 1.2 or
TLS 1.3, set `net.tls.logVersions` to
`"TLS1_2,TLS1_3"`.

#### `net.compression` Option

```yaml
net:
   compression:
      compressors: <string>
```

**`net.compression.compressors`**

*Default*: snappy,zstd,zlib

Specifies the default compressor(s) to use for
communication between this `mongod` or `mongos` instance and:

- other members of the deployment if the instance is part of a replica set or a sharded cluster

- `mongosh`

- drivers that support the `OP_COMPRESSED` message format.

MongoDB supports the following compressors:

- snappy

- zlib 

- zstd 

To disable network compression, set the value to `disabled`.

**Important:**

Messages are compressed when both parties enable network
compression. Otherwise, messages between the parties are
uncompressed.

If you specify multiple compressors, then the order in which you list
the compressors matter as well as the communication initiator. For
example, if `mongosh` specifies the following network
compressors `zlib,snappy` and the `mongod` specifies
`snappy,zlib`, messages between `mongosh` and
`mongod` uses `zlib`.

If the parties do not share at least one common compressor, messages
between the parties are uncompressed. For example, if
`mongosh` specifies the network compressor
`zlib` and `mongod` specifies `snappy`, messages
between `mongosh` and `mongod` are not
compressed.

### `security` Options

```yaml
security:
   keyFile: <string>
   clusterAuthMode: <string>
   authorization: <string>
   transitionToAuth: <boolean>
   javascriptEnabled:  <boolean>
   redactClientLogData: <boolean>
   clusterIpSourceAllowlist:
     - <string>
   sasl:
      hostName: <string>
      serviceName: <string>
      saslauthdSocketPath: <string>
   enableEncryption: <boolean>
   encryptionCipherMode: <string>
   encryptionKeyFile: <string>
   kmip:
      keyIdentifier: <string>
      rotateMasterKey: <boolean>
      serverName: <string>
      port: <string>
      clientCertificateFile: <string>
      clientCertificatePassword: <string>
      clientCertificateSelector: <string>
      serverCAFile: <string>
      connectRetries: <int>
      connectTimeoutMS: <int>
   ldap:
      servers: <string>
      bind:
         method: <string>
         saslMechanisms: <string>
         queryUser: <string>
         queryPassword: <string | array>
         useOSDefaults: <boolean>
      transportSecurity: <string>
      timeoutMS: <int>
      userToDNMapping: <string>
      authz:
         queryTemplate: <string>
      validateLDAPServerConfig: <boolean>
```

**`security.keyFile`**

*Type*: string

The path to a key file that stores the shared secret
that MongoDB instances use to authenticate to each other in a
sharded cluster or replica set. `keyFile` implies
`security.authorization`. See inter-process-auth for more
information.

Keyfiles for internal membership authentication use YAML format to allow for multiple keys in a 
keyfile. The YAML format accepts either:

- A single key string (same as in earlier versions)

- A sequence of key strings

The YAML format is compatible with the existing single-key
keyfiles that use the text file format.

**`security.clusterAuthMode`**

*Type*: string

*Default*: keyFile

The authentication mode used for cluster authentication. If you use
internal X.509 authentication,
specify so here. This option can have one of the following values:

| Value | Description |
|---|---|
| `keyFile` | Use a keyfile for authentication. Accept only keyfiles. |
| `sendKeyFile` | For rolling upgrade purposes. Send a keyfile for authentication but can accept both keyfiles and X.509 certificates. |
| `sendX509` | For rolling upgrade purposes. Send the X.509 certificate for authentication but can accept both keyfiles and X.509 certificates. |
| `x509` | Recommended. Send the X.509 certificate for authentication and accept only X.509 certificates. |

If `--tlsCAFile` or `tls.CAFile` is not
specified and you are not using X.509 authentication, you must set the 
`tlsUseSystemCA` parameter to `true`. This makes MongoDB use 
the system-wide CA certificate store when connecting to a TLS-enabled server.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

   

**`security.authorization`**

*Type*: string

*Default*: disabled

Enable or disable Role-Based Access Control (RBAC) to govern each
user's access to database resources and operations.

Set this option to one of the following:

| Value | Description |
|---|---|
| `enabled` | A user can access only the database resources and actions for which they have been granted privileges. |
| `disabled` | A user can access any database and perform any action. |

See /core/authorization for more information.

The `security.authorization` setting is available only for `mongod`.

**`security.transitionToAuth`**

*Type*: boolean

*Default*: false

Allows the `mongod` or `mongos` to accept and 
create authenticated and non-authenticated connections to and from other 
`mongod` and `mongos` instances in the deployment. 
Used for performing rolling transition of replica sets or sharded clusters
from a no-auth configuration to internal authentication.
Requires specifying a internal authentication mechanism such as
`security.keyFile`.

For example, if using keyfiles for
internal authentication, the `mongod` or `mongos` creates
an authenticated connection with any `mongod` or `mongos`
in the deployment using a matching keyfile. If the security mechanisms do
not match, the `mongod` or `mongos` utilizes a non-authenticated connection instead.

A `mongod` or `mongos` running with `security.transitionToAuth` does not enforce user access
controls. Users may connect to your deployment without any
access control checks and perform read, write, and administrative operations.

**Note:**

A `mongod` or `mongos` running with internal authentication and *without* `security.transitionToAuth` requires clients to connect
using user access controls. Update clients to
connect to the `mongod` or `mongos` using the appropriate user
prior to restarting `mongod` or `mongos` without `security.transitionToAuth`.

**`security.javascriptEnabled`**

*Type*: boolean

*Default*: true

Enables or disables server-side JavaScript execution. When disabled, you cannot use
operations that perform server-side execution of JavaScript code,
such as the `$where` query operator, `mapReduce`
command, `$accumulator`, and `$function`.

If you do not use these operations, disable server-side scripting.

The `security.javascriptEnabled` is available for both 
`mongod` and `mongos`. In earlier versions, the 
setting is only available for `mongod`.

**`security.redactClientLogData`**

*Type*: boolean

*Available in MongoDB Enterprise only.*

A `mongod` or `mongos` running with `security.redactClientLogData` redacts any message accompanying a given
log event before logging. This prevents the `mongod` or `mongos` from writing
potentially sensitive data stored on the database to the diagnostic log.
Metadata such as error or operation codes, line numbers, and source file
names are still visible in the logs.

Use `security.redactClientLogData` in conjunction with
/core/security-encryption-at-rest and
/core/security-transport-encryption to assist compliance with
regulatory requirements.

For example, a MongoDB deployment might store Personally Identifiable
Information (PII) in one or more collections. The `mongod` or `mongos` logs events
such as those related to CRUD operations, sharding metadata, etc. It is
possible that the `mongod` or `mongos` may expose PII as a part of these logging
operations. A `mongod` or `mongos` running with `security.redactClientLogData` removes any message
accompanying these events before being output to the log, effectively
removing the PII.

Diagnostics on a `mongod` or `mongos` running with `security.redactClientLogData` may be more difficult
due to the lack of data related to a log event. See the
process logging manual page for an
example of the effect of `security.redactClientLogData` on log output.

On a running `mongod` or `mongos`, use `setParameter` with the
`redactClientLogData` parameter to configure this setting.

**`security.clusterIpSourceAllowlist`**

*Type*: list

**New in version:** 5.0

**Changed in version:** 5.2

A list of IP addresses/CIDR ([Classless Inter-Domain Routing](https://tools.ietf.org/html/rfc4632)) ranges against which the
`mongod` validates authentication requests from other 
members of the replica set and, if part of a sharded cluster, the 
`mongos` instances. The `mongod` verifies 
that the originating IP is either explicitly in the list or belongs 
to a CIDR range in the list. If the IP address is not present, the 
server does not authenticate the `mongod` or `mongos`.

`security.clusterIpSourceAllowlist` has no effect on a `mongod`
started without authentication.

Starting in MongoDB 5.2, you can configure
`security.clusterIpSourceAllowlist` on a running `mongod` or
`mongos` using `setParameter`.

This example updates `security.clusterIpSourceAllowlist`
during runtime to include the IP addresses `"1.1.1.1/24"`, 
`"2.2.2.2/16"`, and `"3.3.3.3"`.

```javascript
db.adminCommand( {
   setParameter: 1,
   "clusterIpSourceAllowlist": ["1.1.1.1/24", "2.2.2.2/16", "3.3.3.3"]
} );
```

This example updates `security.clusterIpSourceAllowlist` during
runtime to exclude all IP addresses:

```javascript
 db.adminCommand( {
    setParameter: 1,
    "clusterIpSourceAllowlist": null
} );
```

`security.clusterIpSourceAllowlist` has no effect on a 
`mongod` started without
authentication.

`security.clusterIpSourceAllowlist` requires specifying each 
IPv4/6 address or Classless Inter-Domain Routing 
([CIDR](https://tools.ietf.org/html/rfc4632)) range as a YAML list:

```yaml
security:
  clusterIpSourceAllowlist:
    - 192.0.2.0/24
    - 127.0.0.1
    - ::1
```

**Important:**

Ensure `security.clusterIpSourceAllowlist` includes the 
IP address *or* CIDR ranges that include the IP address of each 
replica set member or `mongos` in the deployment to 
ensure healthy communication between cluster components.

#### Key Management Configuration Options

```yaml
security:
   enableEncryption: <boolean>
   encryptionCipherMode: <string>
   encryptionKeyFile: <string>
   kmip:
      keyIdentifier: <string>
      rotateMasterKey: <boolean>
      serverName: <string>
      port: <string>
      clientCertificateFile: <string>
      clientCertificatePassword: <string>
      clientCertificateSelector: <string>
      serverCAFile: <string>
      connectRetries: <int>
      connectTimeoutMS: <int>
      activateKeys: <boolean>
      keyStatePollingSeconds: <int>
```

**`security.enableEncryption`**

*Type*: boolean

*Default*: false

Enables encryption for the WiredTiger storage engine. You must set
to `true` to pass in encryption keys and configurations.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.encryptionCipherMode`**

*Type*: string

*Default*: `AES256-CBC`

The cipher mode to use for encryption at rest:

| Mode | Description |
|---|---|
| `AES256-CBC` | 256-bit Advanced Encryption Standard in Cipher Block Chaining Mode |
| `AES256-GCM` | 256-bit Advanced Encryption Standard in Galois/Counter Mode Available only on Linux. MongoDB Enterprise on Windows no longer supports `AES256-GCM` as a block cipher for encryption at rest. This usage is only supported on Linux. |

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.encryptionKeyFile`**

*Type*: string

The path to the local keyfile when managing keys through a process *other
than* KMIP. Only set when managing keys through a process other than KMIP.
If data is already encrypted using KMIP, MongoDB throws an error.

Requires `security.enableEncryption` to be `true`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.keyIdentifier`**

*Type*: string

Unique KMIP identifier for an existing key within the KMIP server.
Include to use the key associated with the identifier as the system
key. You can only use the setting the first time you enable
encryption for the `mongod` instance. Requires
`security.enableEncryption` to be true.

If unspecified, MongoDB requests that the KMIP server create a
new key to utilize as the system key.

If the KMIP server cannot locate a key with the specified identifier
or the data is already encrypted with a key, MongoDB throws an error.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.rotateMasterKey`**

*Type*: boolean

*Default*: false

If true, rotate the master key and re-encrypt the internal
keystore.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**See also:**

kmip-master-key-rotation

   

**`security.kmip.serverName`**

*Type*: string

Hostname or IP address of the KMIP server to connect to. Requires
`security.enableEncryption` to be true.

You can specify multiple KMIP servers as a comma-separated list, for example
`server1.example.com,server2.example.com`. On startup, the
`mongod` attempts to establish a connection to each
server in the order listed, and selects the first server to
which it can successfully establish a connection. KMIP server
selection occurs only at startup.

`mongod` verifies the connection to the KMIP server on startup.

The server name specified in `--kmipServerName` must match either the Subject Alternative
Name `SAN` or the Common Name `CN` on the certificate presented by
the KMIP server. `SAN` can be a system name or an IP address. 

If `SAN` is present, `mongod` does not try to match against `CN`.

If the hostname or IP address of the KMIP server does does not match
either `SAN` or `CN`, `mongod` does not start.

Starting in MongoDB 4.2, when performing comparison of SAN, MongoDB
supports comparison of DNS names or IP addresses. In previous versions,
MongoDB only supports comparisons of DNS names.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.port`**

*Type*: string

*Default*: 5696

Port number to use to communicate with the KMIP server. Requires
`security.kmip.serverName`. Requires
`security.enableEncryption` to be true.

If specifying multiple KMIP servers with
`security.kmip.serverName`, the `mongod`
uses the port specified with `security.kmip.port` for all
provided KMIP servers.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.clientCertificateFile`**

*Type*: string

Path to the `.pem` file used to authenticate MongoDB to the KMIP
server. The specified `.pem` file must contain both the TLS/SSL
certificate and key. 

To use this setting, you must also specify the
`security.kmip.serverName` setting.

**Note:**

Starting in 4.0, on macOS or Windows, you can use a certificate
from the operating system's secure store instead of a PEM key
file. See `security.kmip.clientCertificateSelector`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.clientCertificatePassword`**

*Type*: string

The password to decrypt the Private Key of the Client Certificate that
connects to the KMIP server. This option authenticates
MongoDB to the KMIP server and requires that you provide a
`--kmipClientCertificateFile`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.clientCertificateSelector`**

*Type*: string

**New in version:** 5.0

Available on Windows and macOS as an alternative to
`security.kmip.clientCertificateFile`. 

`security.kmip.clientCertificateFile` and `security.kmip.clientCertificateSelector` options are mutually exclusive. You can only
specify one.

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store to
authenticate MongoDB to the KMIP server.

`security.kmip.clientCertificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.serverCAFile`**

*Type*: string

Path to CA File. Used for validating secure client connection to
KMIP server.

**Note:**

Starting in 4.0, on macOS or Windows, you can use a certificate
from the operating system's secure store instead of a PEM key
file. See `security.kmip.clientCertificateSelector`. When using the secure store, you do not
need to, but can, also specify the `security.kmip.serverCAFile`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.connectRetries`**

*Type*: int

*Default*: 0

How many times to retry the initial connection to the KMIP server.
Use together with `connectTimeoutMS` to
control how long the `mongod` waits for a response
between each retry.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.connectTimeoutMS`**

*Type*: int

*Default*: 5000

Timeout in milliseconds to wait for a response from the KMIP server.
If the `connectRetries` setting is specified,
the `mongod` waits up to the value specified with
`connectTimeoutMS` for each retry.

Value must be `1000` or greater.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.activateKeys`**

*Type*: boolean

*Default*: true

**New in version:** 5.3

Activates all newly created KMIP keys upon creation and then periodically 
checks those keys are in an active state.  

When `security.kmip.activateKeys` is `true` and you have existing keys 
on a KMIP server, the key must be activated first or the `mongod` 
node fails to start.

If the key being used by the mongod transitions into a non-active state, 
the `mongod` node shuts down unless `kmipActivateKeys` is 
false. To ensure you have an active key, rotate the KMIP master key by 
using `security.kmip.rotateMasterKey`.

**`security.kmip.keyStatePollingSeconds`**

*Type*: int

*Default*: 900 seconds

**New in version:** 5.3

Frequency in seconds at which mongod polls the KMIP server for active keys. 

To disable disable polling, set the value to `-1`. 

**`security.kmip.useLegacyProtocol`**

*Type*: boolean

*Default*: false

**New in version:** 6.0.6

When `true`, `mongod` uses KMIP protocol version 1.0 or 1.1 instead
of the default version. The default KMIP protocol is version 1.2.

To use audit log encryption
with KMIP version 1.0 or 1.1, you must specify
`auditEncryptKeyWithKMIPGet` at startup.

To use KMIP protocol version 1.0 or 1.1, substitute your local values
and add an entry like this to your `mongod` configuration file:

```bash
security:
  enableEncryption: true
  kmip:
    serverName: "mdbhost.somecompany.com"
    serverCAFile: "security/libs/trusted-ca.pem"
    clientCertificateFile: "security/libs/trusted-client.pem"
    useLegacyProtocol: true
```

#### `security.sasl` Options

```yaml
security:
   sasl:
      hostName: <string>
      serviceName: <string>
      saslauthdSocketPath: <string>
```

**`security.sasl.hostName`**

*Type*: string

A fully qualified server domain name for the purpose of configuring SASL
and Kerberos authentication. The SASL hostname overrides the hostname
only for the configuration of SASL and Kerberos.
   

**`security.sasl.serviceName`**

*Type*: string

Registered name of the service using SASL. This option allows you to
override the default Kerberos
service name component of the Kerberos
principal name, on a per-instance basis. If unspecified, the default
value is `mongodb`.

MongoDB permits setting this option only at startup. The
`setParameter` can not change this setting.

This option is available only in MongoDB Enterprise.

**Important:**

Ensure that your driver supports alternate service names.
For `mongosh` and other MongoDB tools to
connect to the new `serviceName`, see the
`gssapiServiceName` option.

**`security.sasl.saslauthdSocketPath`**

*Type*: string

The path to the UNIX domain socket file for `saslauthd`.
   

#### `security.ldap` Options

```yaml
security:
   ldap:
      servers: <string>
      bind:
         method: <string>
         saslMechanisms: <string>
         queryUser: <string>
         queryPassword: <string | array>
         useOSDefaults: <boolean>
      transportSecurity: <string>
      timeoutMS: <int>
      userToDNMapping: <string>
      authz:
         queryTemplate: <string>
      validateLDAPServerConfig: <boolean>
```

**`security.ldap.servers`**

*Type*: string

*Available in MongoDB Enterprise only.*

The LDAP server against which the `mongod` or `mongos` authenticates users or
determines what actions a user is authorized to perform on a given
database. If the LDAP server specified has any replicated instances,
you may specify the host and port of each replicated server in a
comma-delimited list.

If your LDAP infrastructure partitions the LDAP directory over multiple LDAP
servers, specify *one* LDAP server or any of its replicated instances to
`security.ldap.servers`. MongoDB supports following LDAP referrals as defined in [RFC 4511 4.1.10](https://www.rfc-editor.org/rfc/rfc4511.txt). Do not use `security.ldap.servers`
for listing every LDAP server in your infrastructure.

You can prefix LDAP servers with `srv:` and `srv_raw:`.

If your connection string specifies `"srv:<DNS_NAME>"`, `mongod`
verifies that `"_ldap._tcp.gc._msdcs.<DNS_NAME>"` exists for SRV to
support Active Directory. If not found, `mongod` verifies that
`"_ldap._tcp.<DNS_NAME>"` exists for SRV. If an SRV record cannot be
found, `mongod` warns you to use `"srv_raw:<DNS_NAME>"` instead.

If your connection string specifies `"srv_raw:<DNS_NAME>"`,
`mongod` performs an SRV record lookup for `"<DNS NAME>"`.

This setting can be configured on a running `mongod` or `mongos` using
`setParameter`.

If unset, `mongod` or `mongos` cannot use LDAP authentication or authorization.

**`security.ldap.bind.queryUser`**

*Type*: string

*Available in MongoDB Enterprise only.*

The identity with which `mongod` or `mongos` binds as, when connecting to or
performing queries on an LDAP server.

Only required if any of the following are true:

- Using LDAP authorization.
- Using an LDAP query for `security.ldap.userToDNMapping`.
- The LDAP server disallows anonymous binds

You must use `queryUser` with
`queryPassword`.

If unset, `mongod` or `mongos` does not
attempt to bind to the LDAP server.

This setting can be configured on a running
`mongod` or `mongos` using
`setParameter`.

**Note:**

Windows MongoDB deployments can use `useOSDefaults`
instead of `queryUser` and `queryPassword`. You cannot specify
both `queryUser` and `useOSDefaults` at the same time.

**`security.ldap.bind.queryPassword`**

*Type*: string or array

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`queryUser`. You must use 
`queryPassword` with
`queryUser`.

If not set, `mongod` or `mongos` does not attempt to
bind to the LDAP server.

You can configure this setting on a running `mongod` or 
`mongos` using `setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `useOSDefaults`
instead of `queryUser` and 
`queryPassword`. You cannot specify both 
`queryPassword` and 
`useOSDefaults` at the same time.

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`--ldapQueryUser`. You must use `--ldapQueryPassword` with
`--ldapQueryUser`.

If not set, `mongod` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongod` using
`setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. 
You cannot specify both `--ldapQueryPassword` and 
`--ldapBindWithOSDefaults` at the same time.

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`--ldapQueryUser`. You must use `--ldapQueryPassword` with
`--ldapQueryUser`.

If not set, `mongoldap` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongoldap` using
`setParameter`.

The `ldapQueryPassword``setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. 
You cannot specify both `--ldapQueryPassword` and 
`--ldapBindWithOSDefaults` at the same time.

**`security.ldap.bind.useOSDefaults`**

*Type*: boolean

*Default*: false

Available in MongoDB Enterprise for the Windows platform only.

Allows `mongod` or `mongos` to authenticate, or bind, using your Windows login
credentials when connecting to the LDAP server.

Only required if:

- Using LDAP authorization.
- Using an LDAP query for `username transformation`.
- The LDAP server disallows anonymous binds

Use `useOSDefaults` to replace `queryUser` and
`queryPassword`.

**`security.ldap.bind.method`**

*Type*: string

*Default*: simple

*Available in MongoDB Enterprise only.*

The method `mongod` or `mongos` uses to authenticate to an LDAP server.
Use with `queryUser` and
`queryPassword` to
connect to the LDAP server.

`method` supports the following values:

* `simple` - `mongod` or `mongos` uses simple authentication.

* `sasl` - `mongod` or `mongos` uses SASL protocol for authentication

If you specify `sasl`, you can configure the available SASL mechanisms
using `security.ldap.bind.saslMechanisms`. `mongod` or `mongos` defaults to
using `DIGEST-MD5` mechanism.

**`security.ldap.bind.saslMechanisms`**

*Type*: string

*Default*: DIGEST-MD5

*Available in MongoDB Enterprise only.*

A comma-separated list of SASL mechanisms `mongod` or `mongos` can
use when authenticating to the LDAP server. The `mongod` or `mongos` and the
LDAP server must agree on at least one mechanism. The `mongod` or `mongos`
dynamically loads any SASL mechanism libraries installed on the host
machine at runtime.

Install and configure the appropriate libraries for the selected
SASL mechanism(s) on both the `mongod` or `mongos` host and the remote
LDAP server host. Your operating system may include certain SASL
libraries by default. Defer to the documentation associated with each
SASL mechanism for guidance on installation and configuration.

If using the `GSSAPI` SASL mechanism for use with
security-kerberos, verify the following for the
`mongod` or `mongos` host machine:

`Linux`
  - The `KRB5_CLIENT_KTNAME` environment
    variable resolves to the name of the client keytab-files
    for the host machine. For more on Kerberos environment
    variables, please defer to the
    [Kerberos documentation](https://web.mit.edu/kerberos/krb5-1.13/doc/admin/env_variables.html).
  - The client keytab includes a
    kerberos-user-principal for the `mongod` or `mongos` to use when
    connecting to the LDAP server and execute LDAP queries.

`Windows`
  If connecting to an Active Directory server, the Windows
  Kerberos configuration automatically generates a
  [Ticket-Granting-Ticket](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380510(v=vs.85).aspx)
  when the user logs onto the system. Set `useOSDefaults` to
  `true` to allow `mongod` or `mongos` to use the generated credentials when
  connecting to the Active Directory server and execute queries.

Set `method` to `sasl` to use this option.

**Note:**

For a complete list of SASL mechanisms see the
[IANA listing](http://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml).
Defer to the documentation for your LDAP or Active Directory
service for identifying the SASL mechanisms compatible with the
service.

MongoDB is not a source of SASL mechanism libraries, nor
is the MongoDB documentation a definitive source for
installing or configuring any given SASL mechanism. For
documentation and support, defer to the SASL mechanism
library vendor or owner.

For more information on SASL, defer to the following resources:

- For Linux, please see the [Cyrus SASL documentation](https://www.cyrusimap.org/sasl/).
- For Windows, please see the [Windows SASL documentation](https://msdn.microsoft.com/en-us/library/cc223500.aspx).

**`security.ldap.transportSecurity`**

*Type*: string

*Default*: tls

*Available in MongoDB Enterprise only.*

By default, `mongod` or `mongos` creates a TLS/SSL secured connection to the LDAP
server.

For Linux deployments, you must configure the appropriate TLS Options in
`/etc/openldap/ldap.conf` file. Your operating system's package manager
creates this file as part of the MongoDB Enterprise installation, through the
`libldap` dependency. See the documentation for `TLS Options` in the
[ldap.conf OpenLDAP documentation](http://www.openldap.org/software/man.cgi?query=ldap.conf&manpath=OpenLDAP+2.4-Release)
for more complete instructions.

For Windows deployment, you must add the LDAP server CA certificates to the
Windows certificate management tool. The exact name and functionality of the
tool may vary depending on operating system version. Please see the
documentation for your version of Windows for more information on
certificate management.

Set `transportSecurity` to `none` to disable TLS/SSL between `mongod` or `mongos` and the LDAP
server.

**Warning:**

Setting `transportSecurity` to `none` transmits plaintext information and possibly
credentials between `mongod` or `mongos` and the LDAP server.

**`security.ldap.timeoutMS`**

*Type*: int

*Default*: 10000

*Available in MongoDB Enterprise only.*

The amount of time in milliseconds `mongod` or `mongos` should wait for an LDAP server
to respond to a request.

Increasing the value of `timeoutMS` may prevent connection failure between the
MongoDB server and the LDAP server, if the source of the failure is a
connection timeout. Decreasing the value of `timeoutMS` reduces the time
MongoDB waits for a response from the LDAP server.

This setting can be configured on a running `mongod` or `mongos` using
`setParameter`.

**`security.ldap.userToDNMapping`**

*Type*: string

*Available in MongoDB Enterprise only.*

Maps the username provided to `mongod` or `mongos` for authentication to a LDAP
Distinguished Name (DN). You may need to use `userToDNMapping` to transform a
username into an LDAP DN in the following scenarios:

- Performing LDAP authentication with simple LDAP binding, where users
  authenticate to MongoDB with usernames that are not full LDAP DNs.

- Using an `LDAP authorization query template` that requires a DN.

- Transforming the usernames of clients authenticating to Mongo DB using
  different authentication mechanisms (for example, X.509, kerberos) to a full LDAP
  DN for authorization.

`userToDNMapping` expects a quote-enclosed JSON-string representing an ordered array
of documents. Each document contains a regular expression `match` and
either a `substitution` or `ldapQuery` template used for transforming the
incoming username.

Each document in the array has the following form:

```javascript
{
  match: "<regex>"
  substitution: "<LDAP DN>" | ldapQuery: "<LDAP Query>"
}
```

| Field | Description | Example |
|---|---|---|
| `match` | An ECMAScript-formatted regular expression (regex) to match against a provided username. Each parenthesis-enclosed section represents a regex capture group used by `substitution` or `ldapQuery`. | `"(.+)ENGINEERING"` `"(.+)DBA"` |
| `substitution` | An LDAP distinguished name (DN) formatting template that converts the authentication name matched by the `match` regex into a LDAP DN. Each curly bracket-enclosed numeric value is replaced by the corresponding [regex capture group](http://www.regular-expressions.info/refcapture.html) extracted from the authentication username through the `match` regex. The result of the substitution must be an [RFC4514](https://www.ietf.org/rfc/rfc4514.txt) escaped string. | `"cn={0},ou=engineering, dc=example,dc=com"` |
| `ldapQuery` | A LDAP query formatting template that inserts the authentication name matched by the `match` regex into an LDAP query URI encoded respecting RFC4515 and RFC4516. Each curly bracket-enclosed numeric value is replaced by the corresponding [regex capture group](http://www.regular-expressions.info/refcapture.html) extracted from the authentication username through the `match` expression. `mongod` or `mongos` executes the query against the LDAP server to retrieve the LDAP DN for the authenticated user. `mongod` or `mongos` requires exactly one returned result for the transformation to be successful, or `mongod` or `mongos` skips this transformation. | `"ou=engineering,dc=example, dc=com??one?(user={0})"` |

**Note:**

An explanation of  [RFC4514](https://www.ietf.org/rfc/rfc4514.txt),
[RFC4515](https://tools.ietf.org/html/rfc4515),
[RFC4516](https://tools.ietf.org/html/rfc4516), or LDAP queries is out
of scope for the MongoDB Documentation. Please review the RFC directly or
use your preferred LDAP resource.

For each document in the array, you must use either `substitution` or
`ldapQuery`. You *cannot* specify both in the same document.

When performing authentication or authorization, `mongod` or `mongos` steps through
each document in the array in the given order, checking the authentication
username against the `match` filter.  If a match is found,
`mongod` or `mongos` applies the transformation and uses the output for
authenticating the user. `mongod` or `mongos` does not check the remaining documents
in the array.

If the given document does not match the provided authentication
name, `mongod` or `mongos` continues
through the list of documents to find additional matches. If no
matches are found in any document, or the transformation the document
describes fails, `mongod` or `mongos`
returns an error. 

`mongod` or `mongos` also returns an error if one 
of the transformations cannot be evaluated due to networking or
authentication failures to the LDAP server. `mongod` or
`mongos` rejects the connection request and does not
check the remaining documents in the array.

Starting in MongoDB 5.0, `userToDNMapping`
accepts an empty string `""` or empty array `[ ]` in place of a
mapping document. If providing an empty string or empty array to
`userToDNMapping`, MongoDB maps the
authenticated username as the LDAP DN. Previously, providing an
empty mapping document would cause mapping to fail.

**Example:**

The following shows two transformation documents. The first
document matches against any string ending in `@ENGINEERING`, placing
anything preceding the suffix into a regex capture group. The
second document matches against any string ending in `@DBA`, placing
anything preceding the suffix into a regex capture group.

**Important:** You must pass the array to `userToDNMapping` as a string.

```text
"[
   {
      match: "(.+)@ENGINEERING.EXAMPLE.COM",
      substitution: "cn={0},ou=engineering,dc=example,dc=com"
   },
   {
      match: "(.+)@DBA.EXAMPLE.COM",
      ldapQuery: "ou=dba,dc=example,dc=com??one?(user={0})"

   }

]"
```

A user with username `alice@ENGINEERING.EXAMPLE.COM` matches the first
document. The regex capture group `{0}` corresponds to the string
`alice`. The resulting output is the DN
`"cn=alice,ou=engineering,dc=example,dc=com"`.

A user with username `bob@DBA.EXAMPLE.COM` matches the second document.
The regex capture group `{0}` corresponds to the string `bob`.  The
resulting output is the LDAP query
`"ou=dba,dc=example,dc=com??one?(user=bob)"`. `mongod` or `mongos` executes this
query against the LDAP server, returning the result
`"cn=bob,ou=dba,dc=example,dc=com"`.

If `userToDNMapping` is unset, `mongod` or `mongos` applies no transformations to the username
when attempting to authenticate or authorize a user against the LDAP server.

This setting can be configured on a running `mongod` or `mongos` using the
`setParameter` database command.

**`security.ldap.authz.queryTemplate`**

*Type*: string

*Available in MongoDB Enterprise only.*

A relative LDAP query URL formatted conforming to [RFC4515](https://tools.ietf.org/html/rfc4515) and [RFC4516](https://tools.ietf.org/html/rfc4516) that `mongod` executes to obtain
the LDAP groups to which the authenticated user belongs to. The query is
relative to the host or hosts specified in `security.ldap.servers`.

**Note:**

For better performance, consider placing the LDAP groups used for
MongoDB authorization into their own Organizational Unit (`OU`).

In the URL, you can use the following substitution tokens:

| Substitution Token | Description |
|---|---|
| `{USER}` | Substitutes the authenticated username, or the `transformed` username if a `userToDNMapping` is specified. |
| `{PROVIDED_USER}` | Substitutes the supplied username, i.e. before either authentication or `LDAP transformation`. |

When constructing the query URL, ensure that the order of LDAP parameters
respects RFC4516:

```bash
[ dn  [ ? [attributes] [ ? [scope] [ ? [filter] [ ? [Extensions] ] ] ] ] ]
```

If your query includes an attribute, `mongod` assumes that the query
retrieves a list of the DNs which this entity is a member of.

If your query does not include an attribute, `mongod` assumes
the query retrieves all entities which the user is member of.

For each LDAP DN returned by the query, `mongod` assigns the authorized
user a corresponding role on the `admin` database. If a role on the on the
`admin` database exactly matches the DN, `mongod` grants the user the
roles and privileges assigned to that role. See the
`db.createRole()` method for more information on creating roles.

**Example:**

This LDAP query returns any groups listed in the LDAP user object's
`memberOf` attribute.

```bash
"{USER}?memberOf?base"
```

Your LDAP configuration may not include the `memberOf` attribute as part
of the user schema, may possess a different attribute for reporting group
membership, or may not track group membership through attributes.
Configure your query with respect to your own unique LDAP configuration.

If unset, `mongod` cannot authorize users using LDAP.

This setting can be configured on a running `mongod` using the
`setParameter` database command.

**Note:**

An explanation of [RFC4515](https://tools.ietf.org/html/rfc4515),
[RFC4516](https://tools.ietf.org/html/rfc4516) or LDAP queries is out
of scope for the MongoDB Documentation. Please review the RFC directly or
use your preferred LDAP resource.

**`security.ldap.validateLDAPServerConfig`**

*Type*: boolean

*Default*: true

*Available in MongoDB Enterprise*

A flag that determines if the `mongod` or
`mongos` instance checks the availability of the
`LDAP server(s)` as part of its
startup:

- If `true`, the `mongod` or `mongos`
  instance performs the availability check and only continues to
  start up if the LDAP server is available.

- If `false`, the `mongod` or `mongos`
  instance skips the availability check; i.e. the instance starts up
  even if the LDAP server is unavailable.
   

### `setParameter` Option

**`setParameter`**

Set MongoDB parameter or parameters described in
/reference/parameters

To set parameters in the YAML configuration file, use the following
format:

```yaml
setParameter:
   <parameter1>: <value1>
   <parameter2>: <value2>
```

For example, to specify the `enableLocalhostAuthBypass` in
the configuration file:

```yaml
setParameter:
   enableLocalhostAuthBypass: false
```

   

#### LDAP Parameters

**`setParameter.ldapUserCacheInvalidationInterval`**

*Type*: int

*Default*: 30

For use with `mongod` servers using security-ldap-external.

The interval (in seconds) `mongod` waits
between external user cache flushes. After `mongod` flushes the external
user cache, MongoDB
reacquires authorization data from the LDAP server the
next time an LDAP-authorized user issues an operation.

Increasing the value specified increases the amount of time
`mongod` and the LDAP server can be out of sync, but reduces the load on
the LDAP server. Conversely, decreasing the value specified
decreases the time `mongod` and the LDAP server can be out of sync while
increasing the load on the LDAP server.

```yaml
setParameter:
   ldapUserCacheInvalidationInterval: <int>
```

### `storage` Options

**Changed in version:** 4.4

- MongoDB removes the `storage.indexBuildRetry` option and the
  corresponding `--noIndexBuildRetry` command-line option.

- MongoDB deprecates
  `storage.wiredTiger.engineConfig.maxCacheOverflowFileSizeGB`
  option. The option has no effect starting in MongoDB 4.4.

```yaml
storage:
   dbPath: <string>
   journal:
      enabled: <boolean>
      commitIntervalMs: <num>
   directoryPerDB: <boolean>
   syncPeriodSecs: <int>
   engine: <string>
   wiredTiger:
      engineConfig:
         cacheSizeGB: <number>
         journalCompressor: <string>
         directoryForIndexes: <boolean>
         maxCacheOverflowFileSizeGB: <number> 
      collectionConfig:
         blockCompressor: <string>
      indexConfig:
         prefixCompression: <boolean>
   inMemory:
      engineConfig:
         inMemorySizeGB: <number>
   oplogMinRetentionHours: <double>
```

**`storage.dbPath`**

*Type*: string

*Default*:

- `/data/db` on Linux and macOS
- `\data\db` on Windows

The directory where the `mongod` instance stores its
data.

The `storage.dbPath` setting is available only for
`mongod`.

**Note:** Configuration Files

The default `mongod.conf` configuration file included with
package manager installations uses the following platform-specific
default values for `storage.dbPath`:

| Platform | Package Manager | Default `storage.dbPath` |
|---|---|---|
| RHEL (Red Hat Enterprise Linux) / CentOS and Amazon | `yum` | `/var/lib/mongo` |
| SUSE | `zypper` | `/var/lib/mongo` |
| Ubuntu and Debian | `apt` | `/var/lib/mongodb` |
| macOS | `brew` | `/usr/local/var/mongodb` |

The Linux package init scripts do not expect `storage.dbPath` to change from the
defaults. If you use the Linux packages and change `storage.dbPath`, you must
use your own init scripts and disable the built-in scripts.

**`storage.journal.enabled`**

*Type*: boolean

*Default*: `true` on 64-bit systems, `false` on 32-bit systems

Enable or disable the durability journal to ensure data files remain valid
and recoverable. This option applies only when you specify the
`storage.dbPath` setting. `mongod` enables journaling by default.

The `storage.journal.enabled` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

You cannot specify `--nojournal` option or `storage.journal.enabled: false` 
for replica set members that use the WiredTiger storage engine.

**`storage.journal.commitIntervalMs`**

*Type*: number

*Default*: 100

The maximum amount of time in milliseconds that
the `mongod` process allows between
journal operations. Values can range from 1 to 500 milliseconds. Lower
values increase the durability of the journal, at the expense of disk
performance.

On WiredTiger, the default journal commit interval is 100
milliseconds. Additionally, a write that includes or implies
`j:true` causes an immediate sync of the journal. For details
or additional conditions that affect the frequency of the sync, see
journal-process.

The `storage.journal.commitIntervalMs` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

**`storage.directoryPerDB`**

*Type*: boolean

*Default*: false

When `true`, MongoDB uses a separate directory to store data for each database. The
directories are under the `storage.dbPath` directory, and each subdirectory
name corresponds to the database name.

The `storage.directoryPerDB` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

Starting in MongoDB 5.0, dropping the final collection in a database
(or dropping the database itself) when
`storage.directoryPerDB` is enabled deletes the newly empty
subdirectory for that database.

To change the `storage.directoryPerDB` option for existing
deployments:

- For standalone instances:

  #. Use `mongodump` on the existing
     `mongod` instance to generate a backup.
  #. Stop the `mongod` instance.
  #. Add the `storage.directoryPerDB` value **and**
     configure a new data directory
  #. Restart the `mongod` instance.
  #. Use `mongorestore` to populate the new data
     directory.

- For replica sets:

  #. Stop a secondary member.
  #. Add the `storage.directoryPerDB` value **and**
     configure a new data directory to that secondary member.
  #. Restart that secondary.
  #. Use initial sync to populate
     the new data directory.
  #. Update remaining secondaries in the same fashion.
  #. Step down the primary, and update the stepped-down member in the
     same fashion.

**`storage.syncPeriodSecs`**

*Type*: number

*Default*: 60

The amount of time that can pass before MongoDB flushes data to the data
files.

**Do not set this value on
production systems.** In almost every situation, you should use the
default setting.

The `mongod` process writes data very quickly to the journal and
lazily to the data files. `storage.syncPeriodSecs` has no effect on 
journaling-internals, but if `storage.syncPeriodSecs` is 
set to `0` the journal eventually consumes all available disk space. 

The `storage.syncPeriodSecs` setting is available only for `mongod`.

Not available for `mongod` instances that use the
in-memory storage engine.

To provide durable data, WiredTiger
uses checkpoints. For more
details, see journaling-wiredTiger.

**`storage.engine`**

*Default*: `wiredTiger`

The storage engine for the `mongod` database. Available
values include:

| Value | Description |
|---|---|
| `wiredTiger` | To specify the /core/wiredtiger. |
| `inMemory` | To specify the /core/inmemory. Available in MongoDB Enterprise only. If you attempt to start a `mongod` with a `storage.dbPath` that contains data files produced by a storage engine other than the one specified by `storage.engine`, `mongod` refuses to start. |

**`storage.oplogMinRetentionHours`**

*Type*: double

Specifies the minimum number of hours to preserve an oplog entry,
where the decimal values represent the fractions of an hour. For
example, a value of `1.5` represents one hour and thirty
minutes.

The value must be greater than or equal to `0`. A value of `0`
indicates that the `mongod` should truncate the oplog
starting with the oldest entries to maintain the configured
maximum oplog size.

Defaults to `0`.

A `mongod` started with `oplogMinRetentionHours` only
removes an oplog entry *if*:

- The oplog has reached the maximum configured oplog size *and*

- The oplog entry is older than the configured number of hours based
  on the host system clock.

The `mongod` has the following behavior when configured
with a minimum oplog retention period:

- The oplog can grow without constraint so as to retain oplog entries
  for the configured number of hours. This may result in reduction or
  exhaustion of system disk space due to a combination of high write
  volume and large retention period.

- If the oplog grows beyond its maximum size, the `mongod` 
  may continue to hold that disk space even if the oplog returns to its
  maximum size *or* is configured for a smaller maximum size. See
  replSetResizeOplog-cmd-compact.

- The `mongod` compares the system wall clock to an 
  oplog entries creation wall clock time when enforcing oplog entry
  retention. Clock drift between cluster components may result in
  unexpected oplog retention behavior. See
  production-notes-clock-synchronization for more information on
  clock synchronization across cluster members.

To change the minimum oplog retention period after starting the
`mongod`, use `replSetResizeOplog`.
`replSetResizeOplog` enables you to resize the oplog
dynamically without restarting the `mongod` process. To
persist the changes made using `replSetResizeOplog`
through a restart, update the value of
`oplogMinRetentionHours`.

#### `storage.wiredTiger` Options

```yaml
storage:
   wiredTiger:
      engineConfig:
         cacheSizeGB: <number>
         journalCompressor: <string>
         directoryForIndexes: <boolean>
         maxCacheOverflowFileSizeGB: <number> 
      collectionConfig:
         blockCompressor: <string>
      indexConfig:
         prefixCompression: <boolean>
```

**`storage.wiredTiger.engineConfig.cacheSizeGB`**

*Type*: float

Defines the maximum size of the internal cache that WiredTiger
uses for all data. The memory consumed by an index build (see
`maxIndexBuildMemoryUsageMegabytes`) is separate from the
WiredTiger cache memory. 

Values can range from `0.25` GB to `10000` GB.

The default WiredTiger internal cache size is the larger of either:

- 50% of (RAM - 1 GB), or

- 256 MB.

For example, on a system with a total of 4GB of RAM the
WiredTiger cache uses 1.5GB of RAM (``0.5 * (4 GB - 1 GB) =
1.5 GB``). Conversely, on a system with a total of 1.25 GB of
RAM WiredTiger allocates 256 MB to the WiredTiger cache
because that is more than half of the total RAM minus one
gigabyte (`0.5 * (1.25 GB - 1 GB) = 128 MB < 256 MB`).

**Note:**

In some instances, such as when running in a container, the database
can have memory constraints that are lower than the total system
memory. In such instances, this memory limit, rather than the total
system memory, is used as the maximum RAM available.

To see the memory limit, see `hostInfo.system.memLimitMB`.

Avoid increasing the WiredTiger internal cache size above its
default value.

With WiredTiger, MongoDB utilizes both the WiredTiger internal cache
and the filesystem cache.

With the filesystem cache, MongoDB automatically uses all free memory
that is not used by the WiredTiger cache or by other processes.

**Note:**

The `storage.wiredTiger.engineConfig.cacheSizeGB` limits the size of the WiredTiger internal
cache. The operating system uses the available free memory
for filesystem cache, which allows the compressed MongoDB data
files to stay in memory. In addition, the operating system 
uses any free RAM to buffer file system blocks and file system
cache.

To accommodate the additional consumers of RAM, you may have to
decrease WiredTiger internal cache size.

The default WiredTiger internal cache size value assumes that there is a
single `mongod` instance per machine. If a single machine
contains multiple MongoDB instances, then you should decrease the setting to
accommodate the other `mongod`
instances.

If you run `mongod` in a container (for example, `lxc`,
`cgroups`, Docker, etc.) that does *not* have access to all of the
RAM available in a system, you must set `storage.wiredTiger.engineConfig.cacheSizeGB` to a value
less than the amount of RAM available in the container. The exact
amount depends on the other processes running in the container. See
`memLimitMB`.

   

**`storage.wiredTiger.engineConfig.journalCompressor`**

*Default*: snappy

Specifies the type of compression to use to compress WiredTiger
journal data.

Available compressors are:

- `none`

- snappy

- zlib

- zstd
   

**`storage.wiredTiger.engineConfig.directoryForIndexes`**

*Type*: boolean

*Default*: false

When `storage.wiredTiger.engineConfig.directoryForIndexes` is `true`, `mongod` stores indexes and collections in separate
subdirectories under the data (i.e. `storage.dbPath`) directory.
Specifically, `mongod` stores the indexes in a subdirectory named
`index` and the collection data in a subdirectory named
`collection`.

By using a symbolic link, you can specify a different location for
the indexes. Specifically, when `mongod` instance is **not**
running, move the `index` subdirectory to the destination and
create a symbolic link named `index` under the data directory to
the new destination.

   

**`storage.wiredTiger.engineConfig.zstdCompressionLevel`**

*Type*: integer

*Default*: 6

Specifies the level of compression applied when using
the zstd compressor.

Values can range from 1 to 22.

The higher the specified value for `zstdCompressionLevel`
the higher the compression which is applied.

Only applicable when either
`blockCompressor` 
or `journalCompressor` (or both) are
set to `zstd`.

*Available starting in MongoDB 5.0*

**`storage.wiredTiger.collectionConfig.blockCompressor`**

*Default*: snappy

Specifies the default compression for collection data. You can
override this on a per-collection basis when creating collections.

Available compressors are:

- `none`

- snappy

- zlib

- zstd

`storage.wiredTiger.collectionConfig.blockCompressor` affects all collections created. If you change
the value of `storage.wiredTiger.collectionConfig.blockCompressor` on an existing MongoDB deployment, all new
collections uses the specified compressor. Existing collections
continue to use the compressor specified when they were
created, or the default compressor at that time.

**`storage.wiredTiger.indexConfig.prefixCompression`**

*Default*: true

Enables or disables prefix compression for index data.

Specify `true` for `storage.wiredTiger.indexConfig.prefixCompression` to enable prefix compression for
index data, or `false` to disable prefix compression for index data.

The `storage.wiredTiger.indexConfig.prefixCompression` setting affects all indexes created. If you change
the value of `storage.wiredTiger.indexConfig.prefixCompression` on an existing MongoDB deployment, all new
indexes uses prefix compression. Existing indexes
are not affected.

#### `storage.inmemory` Options

```yaml
storage:
   inMemory:
      engineConfig:
         inMemorySizeGB: <number>
```

**`storage.inMemory.engineConfig.inMemorySizeGB`**

*Type*: float

*Default*: 50% of physical RAM less 1 GB

Values can range from 256MB to 10TB and can be a float.

Maximum amount of memory to allocate for in-memory storage
engine data, including indexes, oplog if the
`mongod` is part of replica set, replica set or sharded
cluster metadata, etc.

By default, the in-memory storage engine uses 50% of physical RAM minus
1 GB.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

### `operationProfiling` Options

```yaml
operationProfiling:
   mode: <string>
   slowOpThresholdMs: <int>
   slowOpSampleRate: <double>
   filter: <string>
```

**`operationProfiling.mode`**

*Type*: string

*Default*: `off`

Specifies which operations should be profiled.
The following profiler levels are available:

| Level | Description |
|---|---|
| `off` | The profiler is off and does not collect any data. This is the default profiler level. This level corresponds to profiler level 0. |
| `slowOp` | The profiler collects data for operations that take longer than the value of `slowms`. This level corresponds to profiler level 1. |
| `all` | The profiler collects data for all operations. This level corresponds to profiler level 2. |

**Warning:**

Profiling can degrade performance and expose unencrypted query data in the
system log. Carefully consider any performance and security implications
before configuring and enabling the profiler on a production deployment.

See database-profiling-overhead for more information on
potential performance degradation.

   

**`operationProfiling.slowOpThresholdMs`**

*Type*: integer

*Default*: 100

The *slow* operation time threshold, in milliseconds. Operations
that run for longer than this threshold are considered *slow*.

When `logLevel` is set to `0`, MongoDB records *slow*
operations to the diagnostic log at a rate determined by
`slowOpSampleRate`.

At higher `logLevel` settings, all operations appear in
the diagnostic log regardless of their latency with the following
exception: the logging of slow oplog entry messages by the
secondaries. The secondaries log only the slow oplog
entries; increasing the `logLevel` does not log all
oplog entries.

This setting is available for `mongod` and `mongos`.

- For `mongod` instances, the setting affects both
  the diagnostic log and, if enabled, the profiler.

- For `mongos` instances, the setting affects the
  diagnostic log only and not the profiler, since profiling is not
  available on `mongos`.
   

**`operationProfiling.slowOpSampleRate`**

*Type*: double

*Default*: 1.0

The fraction of *slow* operations that should be profiled or logged.
`operationProfiling.slowOpSampleRate` accepts values between
0 and 1, inclusive.

The `slowOpSampleRate` setting is
available for `mongod` and `mongos`. 

- For `mongod` instances, the setting affects both
  the diagnostic log and, if enabled, the profiler.

- For `mongos` instances, the setting affects the
  diagnostic log only and not the profiler since profiling is not
  available on `mongos`.

**`operationProfiling.filter`**

*Type*: string representation of a query document

A filter expression that controls which operations are profiled and
logged.

When `filter` is set,
`slowOpThresholdMs` and
`slowOpSampleRate` are not used for
profiling and slow-query log lines.

When you set a profile filter in the configuration file, the filter
applies to all databases in the deployment. To set a profile filter
for a specific database, use the `db.setProfilingLevel()`
method.

The option takes a string representation of a query document
of the form:

```javascript
{ <field1>: <expression1>, ... }
```

The `<field>` can be any field in the profiler output. The `<expression>` is a query condition
expression.

To specify a profiling filter in a configuration file, you must:

- Enclose the filter document in single quotes to pass the document
  as a string.

- Use the YAML format of the configuration file.

For example, the following `filter` configures the profiler to
log `query` operations that take longer than 2 seconds:

```yaml
operationProfiling:
   mode: all
   filter: '{ op: "query", millis: { $gt: 2000 } }'
```

### `replication` Options

```yaml
replication:
   oplogSizeMB: <int>
   replSetName: <string>
   enableMajorityReadConcern: <boolean>  
```

**`replication.oplogSizeMB`**

*Type*: integer

The maximum size in megabytes for the oplog. The
`oplogSizeMB` setting configures the uncompressed size of the
oplog, not the size on disk.

**Note:**

The oplog can grow past its configured size
limit to avoid deleting the `majority commit point`.

By default, the `mongod` process creates an oplog based
on the maximum amount of space available. For 64-bit systems, the
oplog is typically 5% of available disk space.

Once the `mongod` has created the oplog for the first
time, changing the `replication.oplogSizeMB` option does not
affect the size of the oplog. To change the maximum oplog size after
starting the `mongod`, use
`replSetResizeOplog`. `replSetResizeOplog`
enables you to resize the oplog dynamically without restarting the
`mongod` process. To persist the changes made using
`replSetResizeOplog` through a restart, update the value
of `oplogSizeMB`.

See replica-set-oplog-sizing for more information.

The `replication.oplogSizeMB` setting is available only for `mongod`.

**`replication.replSetName`**

*Type*: string

The name of the replica set that the `mongod` is part of. All hosts
in the replica set must have the same set name.

If your application connects to more than one replica set, each set must
have a distinct name. Some drivers group replica set connections by 
replica set name.

The `replication.replSetName` setting is available only for `mongod`.

`replication.replSetName` cannot be used in conjunction with
`storage.indexBuildRetry`.

For the WiredTiger storage engine, `storage.journal.enabled: false` cannot be used in conjunction with
`replication.replSetName`.

**`replication.enableMajorityReadConcern`**

*Default*: true

Configures support for `"majority"` read concern.

Starting in MongoDB 5.0, 
`enableMajorityReadConcern` cannot be changed 
and is always set to `true`. Attempting to start a storage engine 
that does not support majority read concern with the 
`--enableMajorityReadConcern` option fails and return an error
message.

In earlier versions of MongoDB, 
`enableMajorityReadConcern` was configurable.

**Warning:**

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.

### `sharding` Options

```yaml
sharding:
   clusterRole: <string>
   archiveMovedChunks: <boolean>
```

**`sharding.clusterRole`**

*Type*: string

The role that the `mongod` instance has in the sharded
cluster. Set this setting to one of the following:

| Value | Description |
|---|---|
| `configsvr` | Start this instance as a config server. The instance starts on port `27019` by default. When you configure a MongoDB instance as clusterRole `configsvr` you must also specify a `replSetName`. |
| `shardsvr` | Start this instance as a shard. The instance starts on port `27018` by default. When you configure a MongoDB instance as a a clusterRole `shardsvr` you must also specify a `replSetName`. |

**Note:**

Setting `sharding.clusterRole` requires the `mongod`
instance to be running with replication. To deploy the instance as
a replica set member, use the `replSetName`
setting and specify the name of the replica set.

The `sharding.clusterRole` setting is available only for `mongod`.

**`sharding.archiveMovedChunks`**

*Type*: boolean

*Default*: false.

During chunk migration, a shard does not save documents migrated from
the shard.

### `auditLog` Options

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

```yaml
auditLog:
   destination: <string>
   format: <string>
   path: <string>
   filter: <string>
```

**`auditLog.auditEncryptionKeyIdentifier`**

*Type*: string

**New in version:** 6.0

Specifies the unique identifier of the Key Management
Interoperability Protocol (KMIP) key for audit log encryption.

You cannot use `auditLog.auditEncryptionKeyIdentifier` and
`auditLog.localAuditKeyFile` together.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`auditLog.compressionMode`**

*Type*: string

**New in version:** 5.3

Specifies the compression mode for audit log encryption. You must also enable audit log
encryption using either `auditLog.auditEncryptionKeyIdentifier` or
`auditLog.localAuditKeyFile`.

`auditLog.compressionMode` can be set to one of these values:

| Value | Description |
|---|---|
| `zstd` | Use the zstd algorithm to compress the audit log. |
| `none` *(default)* | Do not compress the audit log. |

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`auditLog.destination`**

*Type*: string

When set, `auditLog.destination` enables auditing and
specifies where `mongos` or `mongod` sends all audit events.

`auditLog.destination` can have one of the following values:

| Value | Description |
|---|---|
| `syslog` | Output the audit events to syslog in JSON format. Not available on Windows. Audit messages have a syslog severity level of `info` and a facility level of `user`. The syslog message limit can result in the truncation of audit messages. The auditing system neither detects the truncation nor errors upon its occurrence. |
| `console` | Output the audit events to `stdout` in JSON format. |
| `file` | Output the audit events to the file specified in `auditLog.path` in the format specified in `auditLog.format`. |

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`auditLog.filter`**

*Type*: string representation of a document

The filter to limit the types of operations the audit system records. The option takes a string representation
of a query document of the form:

```javascript
{ <field1>: <expression1>, ... }
```

The `<field>` can be any field in the audit message, including fields returned in the
param document. The
`<expression>` is a query condition expression.

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`auditLog.format`**

*Type*: string

The format of the output file for auditing if `destination` is `file`. The
`auditLog.format` option can have one of the following values:

| Value | Description |
|---|---|
| `JSON` | Output the audit events in JSON format to the file specified in `auditLog.path`. |
| `BSON` | Output the audit events in BSON binary format to the file specified in `auditLog.path`. |

Printing audit events to a file in JSON format degrades server
performance more than printing to a file in BSON format.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`auditLog.localAuditKeyFile`**

*Type*: string

**New in version:** 5.3

Specifies the path and file name for a local audit key file for
audit log encryption.

**Note:**

Only use `auditLog.localAuditKeyFile` for testing because the key is
not secured. To secure the key, use
`auditLog.auditEncryptionKeyIdentifier` and an external Key
Management Interoperability Protocol (KMIP) server.

You cannot use `auditLog.localAuditKeyFile` and
`auditLog.auditEncryptionKeyIdentifier` together.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`auditLog.path`**

*Type*: string

The output file for auditing if
`destination` has value of `file`. The `auditLog.path`
option can take either a full path name or a relative path name.

**`auditLog.runtimeConfiguration`**

*Type*: boolean

Specifies if a node allows runtime configuration of audit filters
and the auditAuthorizationSuccess variable. If `true` the node
can take part in Online Audit Filter Management. 

### `snmp` Options

**Note:**

MongoDB Enterprise on macOS does *not* include support for SNMP due
to SERVER-29352.

```yaml
snmp:
   disabled: <boolean>
   subagent: <boolean>
   master: <boolean>
```

**`snmp.disabled`**

*Type*: boolean

*Default*: false

Disables SNMP access to `mongod`. The option is incompatible
with `snmp.subagent` and `snmp.master`.

Set to `true` to disable SNMP access.

The `snmp.disabled` setting is available only for `mongod`.

**New in version:** 4.0.6

**`snmp.subagent`**

*Type*: boolean

When `snmp.subagent` is `true`, SNMP runs as a subagent. The option is incompatible with `snmp.disabled` set to `true`.

The `snmp.subagent` setting is available only for `mongod`.

**`snmp.master`**

*Type*: boolean

When `snmp.master` is `true`, SNMP runs as a master. The option is incompatible with `snmp.disabled` set to `true`.

The `snmp.master` setting is available only for `mongod`.

**See also:**

- /tutorial/monitor-with-snmp
- /tutorial/monitor-with-snmp-on-windows
- /tutorial/troubleshoot-snmp

   

## `mongos`-only Options

```yaml
replication:
   localPingThresholdMs: <int>

sharding:
   configDB: <string>
```

**`replication.localPingThresholdMs`**

*Type*: integer

*Default*: 15

The ping time, in milliseconds, that `mongos` uses
to determine which secondary replica set members to pass read
operations from clients. The default value of `15` corresponds to
the default value in all of the client `drivers`.

When `mongos` receives a request that permits reads to
secondary members, the `mongos`:

- Finds the member of the set with the lowest ping time.

- Constructs a list of replica set members that is within a ping time of
  15 milliseconds of the nearest suitable member of the set.

  If you specify a value for the
  `replication.localPingThresholdMs` option, 
  `mongos` construct the list of replica members that are
  within the latency allowed by this value.

- Selects a member to read from at random from this list.

The ping time used for a member compared by the `replication.localPingThresholdMs` setting is a
moving average of recent ping times, calculated at most every 10
seconds. As a result, some queries may reach members above the threshold
until the `mongos` recalculates the average.

See the replica-set-read-preference-behavior-member-selection
section of the read preference
documentation for more information.

**`sharding.configDB`**

*Type*: string

The configuration servers for the
sharded cluster.

Config servers for sharded clusters are 
deployed as a replica set. The
replica set config servers must run the WiredTiger storage engine.

Specify the config server replica set name and the hostname and port of
at least one of the members of the config server replica set.

```javascript
sharding:
  configDB: <configReplSetName>/cfg1.example.net:27019, cfg2.example.net:27019,...
```

The `mongos` instances for the sharded cluster must specify
the same config server replica set name but can specify hostname and
port of different members of the replica set.

## Windows Service Options

```yaml
processManagement:
   windowsService:
      serviceName: <string>
      displayName: <string>
      description: <string>
      serviceUser: <string>
      servicePassword: <string>
```

**`processManagement.windowsService.serviceName`**

*Type*: string

*Default*: MongoDB

The service name of `mongos` or `mongod` when running as a
Windows Service. Use this name with the `net start <name>` and
`net stop <name>` operations.

You must use `processManagement.windowsService.serviceName` in conjunction with either
the `--install` or `--remove` option.

**`processManagement.windowsService.displayName`**

*Type*: string

*Default*: MongoDB

The name listed for MongoDB on the Services administrative
application.

**`processManagement.windowsService.description`**

*Type*: string

*Default*: MongoDB Server

Run `mongos` or `mongod` service description.

You must use `processManagement.windowsService.description` in conjunction with the
`--install` option.

For descriptions that contain spaces, you must enclose the
description in quotes.

**`processManagement.windowsService.serviceUser`**

*Type*: string

The `mongos` or `mongod` service in the context of a certain user. This
user must have "Log on as a service" privileges.

You must use `processManagement.windowsService.serviceUser` in conjunction with the
`--install` option.

**`processManagement.windowsService.servicePassword`**

*Type*: string

The password for `<user>` for `mongos` or `mongod` when running with
the `processManagement.windowsService.serviceUser` option.

You must use `processManagement.windowsService.servicePassword` in conjunction with the
`--install` option.

## Removed MMAPv1 Options

MongoDB removed the deprecated MMAPv1 storage engine and the MMAPv1-specific 
configuration options:

| Removed Configuration File Setting | Removed Command-line Option |
|---|---|
| `storage.mmapv1.journal.commitIntervalMs` |  |
| `storage.mmapv1.journal.debugFlags` | `mongod --journalOptions` |
| `storage.mmapv1.nsSize` | `mongod --nssize` |
| `storage.mmapv1.preallocDataFiles` | `mongod --noprealloc` |
| `storage.mmapv1.quota.enforced` | `mongod --quota` |
| `storage.mmapv1.quota.maxFilesPerDB` | `mongod --quotaFiles` |
| `storage.mmapv1.smallFiles` | `mongod --smallfiles` |
| `storage.repairPath` | `mongod --repairpath` |
| `replication.secondaryIndexPrefetch` | `mongod --replIndexPrefetch` |

For earlier versions of MongoDB, refer to the [legacy documentation](https://www.mongodb.com/docs/legacy/?site=docs).
