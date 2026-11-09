<!-- Converted from reference/log-messages.txt (reStructuredText). Includes are inlined. -->

# Log Messages

## Overview

As part of normal operation, MongoDB maintains a running log of events,
including entries such as incoming connections, commands run, and issues
encountered. Generally, log messages are useful for diagnosing issues,
monitoring your deployment, and tuning performance.

To get your log messages, you can use any of the 
following methods:

- View logs in your configured log destination.
- Run the `getLog` command.
- Download logs through MongoDB Atlas.
  To learn more, see log-messages-atlas.

## Structured Logging

`mongod` / `mongos` instances output all log messages 
in structured JSON format. Log entries 
are written as a series of key-value pairs, where each key indicates a log 
message field type, such as "severity", and each corresponding value records 
the associated logging information for that field type, such as "informational".
Previously, log entries were output as plaintext.

**Example:**

The following is an example log message in JSON format as it would
appear in the MongoDB log file:

```javascript
{"t":{"$date":"2020-05-01T15:16:17.180+00:00"},"s":"I", "c":"NETWORK", "id":12345, "ctx":"listener", "msg":"Listening on","attr":{"address":"127.0.0.1"}}
```

JSON log entries can be pretty-printed for readability. Here is the same log
entry pretty-printed:

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

In this log entry, for example, the key `s`, representing
severity, has a corresponding value of
`I`, representing "Informational", and the key `c`, representing
component, has a corresponding value
of `NETWORK`, indicating that the "network" component was
responsible for this particular message. The various field types are
presented in detail in the log-message-field-types section.

Structured logging with key-value pairs allows for efficient parsing
by automated tools or log ingestion services, and makes programmatic
search and analysis of log messages easier to perform. Examples of
analyzing structured log messages can be found in the
log-message-parsing section.

### JSON Log Output Format

All log output is in JSON format including output sent to:

- Log file
- Syslog
- Stdout (standard out) log destinations

Output from the `getLog` command is also in JSON format.

Each log entry is output as a self-contained JSON object which follows
the Relaxed Extended JSON v2.0
specification, and has the following layout and field order:

```javascript
{
  "t": <Datetime>, // timestamp
  "s": <String>, // severity
  "c": <String>, // component
  "id": <Integer>, // unique identifier
  "ctx": <String>, // context
  "msg": <String>, // message body
  "attr": <Object> // additional attributes (optional)
  "tags": <Array of strings> // tags (optional)
  "truncated": <Object> // truncation info (if truncated)
  "size": <Object> // original size of entry (if truncated)
}
```

Field descriptions:

| Field Name | Type | Description |
|---|---|---|
| `t` | Datetime | Timestamp of the log message in ISO-8601 format. For an example, see log-message-timestamp. |
| `s` | String | Short severity code of the log message. For an example, see log-severity-levels. |
| `c` | String | Full component string for the log message. For an example, see log-message-components. |
| `id` | Integer | Unique identifier for the log statement. For an example, see log-message-parsing-example-filter-id. |
| `ctx` | String | Name of the thread that caused the log statement. |
| `msg` | String | Log output message passed from the server or driver. If necessary, the message is escaped according to the JSON specification. |
| `attr` | Object | One or more key-value pairs for additional log attributes. If a log message does not include any additional attributes, the `attr` object is omitted. Attribute values may be referenced by their key name in the `msg` message body, depending on the message. If necessary, the attributes are escaped according to the JSON specification. |
| `tags` | Array of strings | Strings representing any tags applicable to the log statement. For example, `["startupWarnings"]`. |
| `truncated` | Object | Information about the log message truncation, if applicable. Only included if the log entry contains at least one truncated `attr` attribute. |
| `size` | Object | Original size of a log entry if it has been truncated. Only included if the log entry contains at least one truncated `attr` attribute. |

#### Escaping

The **message** and **attributes** fields will escape control
characters as necessary according to the
Relaxed Extended JSON v2.0
specification:

| Character Represented | Escape Sequence |
|---|---|
| Quotation Mark (`"`) | `\"` |
| Backslash (`\`) | `\\` |
| Backspace (`0x08`) | `\b` |
| Formfeed (`0x0C`) | `\f` |
| Newline (`0x0A`) | `\n` |
| Carriage return (`0x0D`) | `\r` |
| Horizontal tab (`0x09`) | `\t` |

Control characters not listed above are escaped with `\uXXXX` where
"XXXX" is the unicode codepoint in hexadecimal. Bytes with invalid
UTF-8 encoding are replaced with the unicode replacement character
represented by `\ufffd`.

An example of message escaping is provided in the
examples section.

#### Truncation

Any **attributes** that exceed the maximum size defined with
`maxLogSizeKB` (default: 10 KB) are truncated. Truncated
attributes omit log data beyond the configured limit, but retain the
JSON formatting of the entry to ensure that the entry remains parsable.

Here is an example of a log entry with a truncated attribute:

```javascript
{"t":{"$date":"2020-05-19T18:12:05.702+00:00"},"s":"I",  "c":"SHARDING", "id":22104,   "ctx":"conn33",
"msg":"Received splitChunk request","attr":{"request":{"splitChunk":"config.system.sessions",
"from":"production-shard1","keyPattern":{"_id":1},"epoch":{"$oid":"5ec42172996456771753a59e"},
"shardVersion":[{"$timestamp":{"t":1,"i":0}},{"$oid":"5ec42172996456771753a59e"}],"min":{"_id":{"$minKey":1}},
"max":{"_id":{"$maxKey":1}},"splitKeys":[{"_id":{"id":{"$uuid":"00400000-0000-0000-0000-000000000000"}}},
{"_id":{"id":{"$uuid":"00800000-0000-0000-0000-000000000000"}}},

...

{"_id":{"id":{"$uuid":"26c00000-0000-0000-0000-000000000000"}}},{"_id":{}}]}},
"truncated":{"request":{"splitKeys":{"155":{"_id":{"id":{"type":"binData","size":21}}}}}},
"size":{"request":46328}}
```

In this case, the `request` attribute has been truncated and the
specific instance of its subfield `_id` that triggered truncation
(i.e. caused the attribute to overrun `maxLogSizeKB`) is
printed without data as `{"_id":{}}`. The remainder of the `request`
attribute is then omitted.

Log entries containing one or more truncated attributes include a
`truncated` object which provides the following information for each
truncated attribute in the log entry:

- the attribute that was truncated
- the specific subobject of that attribute that triggered truncation, if
  applicable.
- the data `type` of the truncated field
- the `size` of the truncated field

Log entries with truncated attributes may also include an additional
`size` field at the end of the entry which indicates the original
size of the attribute before truncation, in this case `46328` or about
46KB. This final `size` field is only shown if it is different from
the `size` field in the `truncated` object, i.e. if the total object
size of the attribute is different from the size of the truncated
subobject, as is the case in the example above.

#### Padding

When output to the *file* or the *syslog* log destinations, padding is
added after the **severity**, **context**, and **id** fields to increase
readability when viewed with a fixed-width font.

The following MongoDB log file excerpt demonstrates this padding:

```javascript
{"t":{"$date":"2020-05-18T20:18:12.724+00:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-05-18T20:18:12.734+00:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-05-18T20:18:12.734+00:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-05-18T20:18:12.814+00:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":10111,"port":27001,"dbPath":"/var/lib/mongo","architecture":"64-bit","host":"centos8"}}
{"t":{"$date":"2020-05-18T20:18:12.814+00:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.0","gitVersion":"328c35e4b883540675fb4b626c53a08f74e43cf0","openSSLVersion":"OpenSSL 1.1.1c FIPS  28 May 2019","modules":[],"allocator":"tcmalloc","environment":{"distmod":"rhel80","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-05-18T20:18:12.814+00:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"CentOS Linux release 8.0.1905 (Core) ","version":"Kernel 4.18.0-80.11.2.el8_0.x86_64"}}}
```

#### Pretty Printing

When working with MongoDB structured logging, you can use the third-party
[jq command-line utility](https://stedolan.github.io/jq/) for easy 
pretty-printing of log entries, and powerful key-based matching and filtering.

`jq` is an open-source JSON parser, and is available for
Linux, Windows, and macOS.

You can use `jq` to pretty-print log entries as follows:

- Pretty-print the entire log file:

  ```javascript
  cat mongod.log | jq
  ```

- Pretty-print the most recent log entry:

  ```javascript
  cat mongod.log | tail -1 | jq
  ```

More examples of working with MongoDB structured logs are available in
the log-message-parsing section.

### Configuring Log Message Destinations

MongoDB log messages can be output to *file*, *syslog*, or *stdout*
(standard output).

To configure the log output destination, use one of the following
settings, either in the configuration file or on the command-line:

**Configuration file:**
  - The `systemLog.destination` option for *file* or *syslog*

**Command-line:**
  - the `--logpath` option for
    `mongod` for *file*
  - the `--syslog` option for
    `mongod` for *syslog*
  - the `--logpath` option for
    `mongos` for *file*
  - the `--syslog` option for
    `mongos` for *syslog*

Not specifying either *file* or *syslog* sends all logging output to
*stdout*.

For the full list of logging settings and options see:

**Configuration file:**
  - systemLog options list

**Command-line:**
  - Log options list for
    `mongod`
  - Log options list for
    `mongos`

**Note:**

Error messages sent to `stderr` (standard error), such as fatal
errors during startup when not using the *file* or *syslog* log
destinations, or messages having to do with misconfigured logging
settings, are not affected by the log output destination setting, and
are printed to `stderr` in plaintext format.

## Log Message Field Types

### Timestamp

The timestamp field type indicates the precise date and time at which
the logged event occurred.

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

When logging to *file* or to *syslog* [#syslog-ts]_, the default
format for the timestamp is `iso8601-local`. To modify the
timestamp format, use the `--timeStampFormat` runtime option or the
`systemLog.timeStampFormat` setting.

See log-message-parsing-example-filter-timestamp for log parsing
examples that filter on the timestamp field.

**Note:**

The `ctime` timestamp format is no longer supported.

### Severity

The severity field type indicates the severity level associated with the
logged event.

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

Severity levels range from "Fatal" (most severe) to "Debug" (least
severe):

| Level | Description |
|---|---|
| `F` | Fatal |
| `E` | Error |
| `W` | Warning |
| `I` | Informational, for verbosity level `0` |
| `D1` - `D5` | Debug, for verbosity levels > `0` Starting in version 4.2, MongoDB indicates the specific debug verbosity level. For example, if verbosity level is 2, MongoDB indicates `D2`. In previous versions, MongoDB log messages specified `D` for all debug verbosity levels. |

You can specify the verbosity level of various components to determine
the amount of **Informational** and **Debug** messages MongoDB outputs.
Severity categories above these levels are always shown. [#slow-oplogs]_
To set verbosity levels, see log-messages-configure-verbosity.

### Components

The component field type indicates the category a logged event is a
member of, such as **NETWORK** or **COMMAND**.

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

Each component is individually configurable via its own
verbosity filter. The
available components are as follows:

**`ACCESS`**

Messages related to access control, such as authentication. To
specify the log level for `ACCESS` components, use the
`systemLog.component.accessControl.verbosity` setting.

**`ASSERT`**

An assertion is triggered when an operation returns an error. The default 
verbosity level is `0`. However, the verbosity setting must be at least 
`1` in order for operations that return errors to be included in the
system logs.  To specify the log level for `ACCESS` components, use the 
`assert` setting. 

**`COMMAND`**

Messages related to database commands,
such as `count`. To specify the log level for
`COMMAND` components, use the
`systemLog.component.command.verbosity` setting.

**`CONTROL`**

Messages related to control activities, such as initialization. To
specify the log level for `CONTROL` components, use the
`systemLog.component.control.verbosity` setting.

**`ELECTION`**

Messages related specifically to replica set elections. To specify
the log level for `ELECTION` components, set the
`systemLog.component.replication.election.verbosity`
parameter.

`REPL` is the parent component of `ELECTION`. If
`systemLog.component.replication.election.verbosity` is
unset, MongoDB uses the `REPL` verbosity level for
`ELECTION` components.

**`FTDC`**

Messages related to the diagnostic data collection mechanism, such 
as server statistics and status messages. To specify the log level
for `FTDC` components, use the 
`systemLog.component.ftdc.verbosity` setting.

**`GEO`**

Messages related to the parsing of geospatial shapes, such as
verifying the GeoJSON shapes. To specify the log level for
`GEO` components, set the
`systemLog.component.geo.verbosity` parameter.

**`INDEX`**

Messages related to indexing operations, such as
creating indexes. To specify the log level for
`INDEX` components, set the
`systemLog.component.index.verbosity` parameter.

**`INITSYNC`**

Messages related to initial sync operation. To specify the log level
for `INITSYNC` components, set the
`systemLog.component.replication.initialSync.verbosity`
parameter.

`REPL` is the parent component of `INITSYNC`. If
`systemLog.component.replication.initialSync.verbosity` is
unset, MongoDB uses the `REPL` verbosity level for
`INITSYNC` components.

**`JOURNAL`**

Messages related specifically to storage journaling activities. To
specify the log level for `JOURNAL` components, use the
`systemLog.component.storage.journal.verbosity` setting.

`STORAGE` is the parent component of `JOURNAL`. If
`systemLog.component.storage.journal.verbosity` is
unset, MongoDB uses the `STORAGE` verbosity level for
`JOURNAL` components.

**`NETWORK`**

Messages related to network activities, such as accepting
connections. To specify the log level for `NETWORK`
components, set the
`systemLog.component.network.verbosity` parameter.

**`QUERY`**

Messages related to queries, including query planner activities.
To specify the log level for `QUERY` components, set the
`systemLog.component.query.verbosity` parameter.

**`QUERYSTATS`**

Messages related to `$queryStats` operations. To specify the log 
level for `QUERYSTATS` components, set the 
`systemLog.component.queryStats.verbosity` parameter.

**`RECOVERY`**

Messages related to storage recovery activities. To specify the log
level for `RECOVERY` components, use the
`systemLog.component.storage.recovery.verbosity` setting.

`STORAGE` is the parent component of `RECOVERY`. If
`systemLog.component.storage.recovery.verbosity` is
unset, MongoDB uses the `STORAGE` verbosity level for
`RECOVERY` components.

**`REPL`**

Messages related to replica sets, such as initial sync, heartbeats,
steady state replication, and rollback. [#slow-oplogs]_ To specify
the log level for `REPL` components, set the
`systemLog.component.replication.verbosity` parameter.

`REPL` is the parent component of the `ELECTION`,
`INITSYNC`, `REPL_HB`, and `ROLLBACK` components.

**`REPL_HB`**

Messages related specifically to replica set heartbeats. To specify
the log level for `REPL_HB` components, set the
`systemLog.component.replication.heartbeats.verbosity`
parameter.

`REPL` is the parent component of `REPL_HB`. If
`systemLog.component.replication.heartbeats.verbosity` is
unset, MongoDB uses the `REPL` verbosity level for
`REPL_HB` components.

**`ROLLBACK`**

Messages related to rollback
operations. To specify the log level for `ROLLBACK` components,
set the `systemLog.component.replication.rollback.verbosity`
parameter.

`REPL` is the parent component of `ROLLBACK`. If
`systemLog.component.replication.rollback.verbosity` is
unset, MongoDB uses the `REPL` verbosity level for
`ROLLBACK` components.

**`SHARDING`**

Messages related to sharding activities, such as the startup of
the `mongos`. To specify the log level for
`SHARDING` components, use the
`systemLog.component.sharding.verbosity` setting.

**`STORAGE`**

Messages related to storage activities, such as processes involved
in the `fsync` command. To specify the log level for
`STORAGE` components, use the
`systemLog.component.storage.verbosity` setting.

`STORAGE` is the parent component of `JOURNAL` and
`RECOVERY`.

**`TXN`**

Messages related to multi-document transactions. To specify the log level for `TXN`
components, use the
`systemLog.component.transaction.verbosity` setting.

**`WRITE`**

Messages related to write operations, such as `update`
commands. To specify the log level for `WRITE` components,
use the `systemLog.component.write.verbosity` setting.

**`WT`**

**New in version:** 5.3

Messages related to the WiredTiger storage
engine. To specify the log level for `WT` components, use the
`systemLog.component.storage.wt.verbosity` setting.

**`WTBACKUP`**

**New in version:** 5.3

Messages related to backup operations performed by the
WiredTiger storage engine.
To specify the log level for the `WTBACKUP` components, use the
`systemLog.component.storage.wt.wtBackup.verbosity` setting.

**`WTCHKPT`**

**New in version:** 5.3

Messages related to checkpoint operations performed by the
WiredTiger storage engine.
To specify the log level for `WTCHKPT` components, use the
`systemLog.component.storage.wt.wtCheckpoint.verbosity` setting.

**`WTCMPCT`**

**New in version:** 5.3

Messages related to compaction operations performed by the
WiredTiger storage engine. To specify the log
level for `WTCMPCT` components, use the
`systemLog.component.storage.wt.wtCompact.verbosity` setting.

**`WTEVICT`**

**New in version:** 5.3

Messages related to eviction operations performed by the
WiredTiger storage engine. To specify the log
level for `WTEVICT` components, use the
`systemLog.component.storage.wt.wtEviction.verbosity` setting.

**`WTHS`**

**New in version:** 5.3

Messages related to the history store of the
WiredTiger storage engine. To specify
the log level for `WTHS` components, use the
`systemLog.component.storage.wt.wtHS.verbosity` setting.

**`WTRECOV`**

**New in version:** 5.3

Messages related to recovery operations performed by the
WiredTiger storage engine. To specify
the log level for `WTRECOV` components, use the
`systemLog.component.storage.wt.wtRecovery.verbosity` setting.

**`WTRTS`**

**New in version:** 5.3

Messages related to rollback to stable (RTS) operations performed by the
WiredTiger storage engine. To specify
the log level for `WTRTS` components, use the
`systemLog.component.storage.wt.wtRTS.verbosity` setting.

**`WTSLVG`**

**New in version:** 5.3

Messages related to salvage operations performed by the
WiredTiger storage engine. To specify
the log level for `WTSLVG` components, use the
`systemLog.component.storage.wt.wtSalvage.verbosity` setting.

**`WTTS`**

**New in version:** 5.3

Messages related to timestamps used by the
WiredTiger storage engine. To specify
the log level for `WTTS` components, use the
`systemLog.component.storage.wt.wtTimestamp.verbosity` setting.

**`WTTXN`**

**New in version:** 5.3

Messages related to transactions performed by the
WiredTiger storage engine. To specify
the log level for `WTTXN` components, use the
`systemLog.component.storage.wt.wtTransaction.verbosity` setting.

**`WTVRFY`**

**New in version:** 5.3

Messages related to verification operations performed by the
WiredTiger storage engine. To specify
the log level for `WTVRFY` components, use the
`systemLog.component.storage.wt.wtVerify.verbosity` setting.

**`WTWRTLOG`**

**New in version:** 5.3

Messages related to log write operations performed by the
WiredTiger storage engine. To specify
the log level for `WTWRTLOG` components, use the
`systemLog.component.storage.wt.wtWriteLog.verbosity` setting.

**`-`**

Messages not associated with a named component. Unnamed components
have the default log level specified in the
`systemLog.verbosity` setting. The
`systemLog.verbosity` setting is the default setting for
both named and unnamed components.

See log-message-parsing-example-filter-component for log parsing
examples that filter on the component field.

### Client Data

`MongoDB Drivers` and client applications (including 
`mongosh`) have the ability to send identifying information at the 
time of connection to the server. After the connection is established, the 
client does not send the identifying information again unless the connection is 
dropped and reestablished.

This identifying information is contained in the **attributes**
field of the log entry. The exact information included varies by client. 

Below is a sample log message containing the client data document as
transmitted from a `mongosh` connection. The client
data is contained in the `doc` object in the **attributes** field:

```javascript
{"t":{"$date":"2020-05-20T16:21:31.561+00:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn202","msg":"client metadata","attr":{"remote":"127.0.0.1:37106","client":"conn202","doc":{"application":{"name":"MongoDB Shell"},"driver":{"name":"MongoDB Internal Client","version":"4.4.0"},"os":{"type":"Linux","name":"CentOS Linux release 8.0.1905 (Core) ","architecture":"x86_64","version":"Kernel 4.18.0-80.11.2.el8_0.x86_64"}}}}
```

When secondary members of a
replica set initiate
a connection to a primary, they send similar data. A sample log message
containing this initiation connection might appear as follows. The
client data is contained in the `doc` object in the **attributes**
field:

```javascript
{"t":{"$date":"2020-05-20T16:33:40.595+00:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn214","msg":"client metadata","attr":{"remote":"127.0.0.1:37176","client":"conn214","doc":{"driver":{"name":"NetworkInterfaceTL","version":"4.4.0"},"os":{"type":"Linux","name":"CentOS Linux release 8.0.1905 (Core) ","architecture":"x86_64","version":"Kernel 4.18.0-80.11.2.el8_0.x86_64"}}}}
```

See the examples section for a
pretty-printed example showing
client data.

For a complete description of client information and required fields,
see the [MongoDB Handshake specification](https://github.com/mongodb/specifications/blob/master/source/mongodb-handshake/handshake.rst).

## Verbosity Levels

You can specify the logging verbosity level to increase or decrease
the amount of log messages MongoDB outputs. Verbosity levels can be
adjusted for all components together, or for specific
named components individually.

Verbosity affects log entries in the severity categories **Informational** and **Debug** only.
Severity categories above these levels are always shown.

You might set verbosity levels to a high value to show detailed logging
for debugging or development, or to a low value to minimize writes to
the log on a vetted production deployment. [#slow-oplogs]_

### View Current Log Verbosity Level

To view the current verbosity levels, use the
`db.getLogComponents()` method:

```javascript
db.getLogComponents()
```

Your output might resemble the following:

```javascript
{
 "verbosity" : 0,
 "accessControl" : {
    "verbosity" : -1
 },
 "command" : {
    "verbosity" : -1
 },
 ...
 "storage" : {
    "verbosity" : -1,
    "recovery" : {
       "verbosity" : -1
    },
    "journal" : {
        "verbosity" : -1
    }
 },
 ...
```

The initial `verbosity` entry is the parent verbosity level for all
components, while the individual named components that follow, such as `accessControl`,
indicate the specific verbosity level for that component, overriding the
global verbosity level for that particular component if set.

A value of `-1`, indicates that the component inherits the verbosity
level of their parent, if they have one (as with `recovery` above,
inheriting from `storage`), or the global verbosity level if they do
not (as with `command`). Inheritance relationships for verbosity
levels are indicated in the components section.

### Configure Log Verbosity Levels

You can configure the verbosity level using: the
`systemLog.verbosity` and
`systemLog.component.<name>.verbosity` settings, the
`logComponentVerbosity` parameter, or the
`db.setLogLevel()` method. [#slow-oplogs]_

#### `systemLog` Verbosity Settings

To configure the default log level for all components, use the `systemLog.verbosity`
setting. To configure the level of specific components, use the
`systemLog.component.<name>.verbosity` settings.

For example, the following configuration sets the
`systemLog.verbosity` to `1`, the
`systemLog.component.query.verbosity` to `2`, the
`systemLog.component.storage.verbosity` to `2`, and the
`systemLog.component.storage.journal.verbosity` to `1`:

```javascript
systemLog:
   verbosity: 1
   component:
      query:
         verbosity: 2
      storage:
         verbosity: 2
         journal:
            verbosity: 1
```

You would set these values in the configuration file or on the command line for your
`mongod` or `mongos` instance.

All components not specified explicitly in the configuration have a
verbosity level of `-1`, indicating that they inherit the verbosity
level of their parent, if they have one, or the global verbosity level
(`systemLog.verbosity`) if they do not.

#### `logComponentVerbosity` Parameter

To set the `logComponentVerbosity` parameter, pass a
document with the verbosity settings to change.

For example, the following sets the `default verbosity level` to `1`, the `query` to `2`, the `storage` to `2`, and the
`storage.journal` to `1`.

```javascript
db.adminCommand( {
   setParameter: 1,
   logComponentVerbosity: {
      verbosity: 1,
      query: {
         verbosity: 2
      },
      storage: {
         verbosity: 2,
         journal: {
            verbosity: 1
         }
      }
   }
} )
```

You would set these values from `mongosh`.

#### `db.setLogLevel()`

Use the `db.setLogLevel()` method to update a single component
log level. For a component, you can specify verbosity level of `0` to
`5`, or you can specify `-1` to inherit the verbosity of the
parent. For example, the following sets the
`systemLog.component.query.verbosity` to its parent verbosity
(i.e. default verbosity):

```javascript
db.setLogLevel(-1, "query")
```

You would set this value from `mongosh`.

### Logging Slow Operations

Client operations (such as queries) appear in the log if their duration
exceeds the slow operation threshold or
when the log verbosity level is 1
or higher. [#slow-oplogs]_ These log entries include the full command
object associated with the operation.

The profiler entries and the 
diagnostic log messages (i.e. mongod/mongos logmessages) for read/write operations include:

- `queryHash` to help identify slow queries with the same
  query shape. 

- `planCacheKey` to provide more insight into the query plan
  cache for slow queries.

**Important:**

A single operation may log more than one entry. For example, if more 
than one write in a bulk write operation exceeds 
the slow operation threshold, each slow write is logged separately. 

#### Version-Specific Changes

The following table lists the changes to logging slow queries.

* - **MongoDB Version**
  - **Changes**

* - 6.0.13 (and 5.0.24)
  - .. include:: /includes/fact-totalOplogSlotDurationMicros.rst 

    For example, consider the following writes with commit timestamps:

    - writeA with Timestamp1
    - writeB with Timestamp2
    - writeC with Timestamp3

    Suppose writeB commits first at Timestamp2. Replication is paused
    until writeA commits because writeA's oplog entry with Timestamp1 is
    required for replication to copy the oplog to secondary replica set
    members. 

### Time Waiting for Shards Logged in `remoteOpWaitMillis` Field

**New in version:** 5.0

Starting in MongoDB 5.0, you can use the `remoteOpWaitMillis` log
field to obtain the wait time (in milliseconds) for results from
shards.

`remoteOpWaitMillis` is only logged:

- If you configure slow operations logging.

- On the shard or `mongos` that merges the results.

To determine if a merge operation or a shard issue is causing a slow
query, compare the `durationMillis` and `remoteOpWaitMillis` time
fields in the log. `durationMillis` is the total time the query took
to complete. Specifically:

- If `durationMillis` is slightly longer than `remoteOpWaitMillis`,
  then most of the time was spent waiting for a shard response. For
  example, `durationMillis` of 17 and `remoteOpWaitMillis` of 15.

- If `durationMillis` is significantly longer than
  `remoteOpWaitMillis`, then most of the time was spent performing the
  merge. For example, `durationMillis` of 100 and
  `remoteOpWaitMillis` of 15.

## Log Redaction

*Available in MongoDB Enterprise only*

A `mongod` or `mongos` running with 
`redactClientLogData` redacts any message accompanying a given log
event before logging, leaving only metadata, source files, or line numbers 
related to the event. `redactClientLogData` prevents 
potentially sensitive information from entering the system log at the cost of 
diagnostic detail.

For example, the following operation inserts a document into a
`mongod` running without log redaction. The `mongod`
has the log verbosity level set to 
`1`:

```javascript
db.clients.insertOne( { "name" : "Joe", "PII" : "Sensitive Information" } )
```

This operation produces the following log event:

```javascript
{
   "t": { "$date": "2024-07-19T15:36:55.024-07:00" },
   "s": "I",
   "c": "COMMAND",
   ...
   "attr": {
      "type": "command",
      ...
      "appName": "mongosh 2.2.10",
      "command": {
         "insert": "clients",
         "documents": [
            {
               "name": "Joe",
               "PII": "Sensitive Information",
               "_id": { "$oid": "669aea8792c7fd822d3e1d8c" }
            }
         ],
         "ordered": true,
         ...
      }
      ...
   }
}
```

When `mongod` runs with `redactClientLogData` and
performs the same insert operation, it produces the following log event:

```javascript
{
   "t": { "$date": "2024-07-19T15:36:55.024-07:00" },
   "s": "I",
   "c": "COMMAND",
   ...
   "attr": {
      "type": "command",
      ...
      "appName": "mongosh 2.2.10",
      "command": {
         "insert": "###",
         "documents": [
            {
               "name": "###",
               "PII": "###",
               "_id": "###"
            }
         ],
         "ordered": "###",
         ...
      }
      ...
   }
}
```

Use `redactClientLogData` in conjunction with 
security-encryption-at-rest and transport-encryption to assist 
compliance with regulatory requirements.

## Parsing Structured Log Messages

Log parsing is the act of programmatically searching through and
analyzing log files, often in an automated manner. With the introduction
of structured logging, log parsing is made simpler and
more powerful. For example:

- Log message fields are presented as key-value pairs. Log parsers can
  query by specific keys of interest to efficiently filter results.

- Log messages always contain the same message structure. Log parsers
  can reliably extract information from any log message, without needing
  to code for cases where information is missing or formatted
  differently.

The following examples demonstrate common log parsing workflows when
working with MongoDB JSON log output.

### Log Parsing Examples

When working with MongoDB structured logging, you can use the third-party
[jq command-line utility](https://stedolan.github.io/jq/) for easy 
pretty-printing of log entries, and powerful key-based matching and filtering.

`jq` is an open-source JSON parser, and is available for
Linux, Windows, and macOS.

These examples use `jq` to simplify log parsing.

#### Counting Unique Messages

The following example shows the top 10 unique message values in a given
log file, sorted by frequency:

```bash
jq -r ".msg" /var/log/mongodb/mongod.log | sort | uniq -c | sort -rn | head -10
```

#### Monitoring Connections

Remote client connections are shown in the log under the "remote" key
in the attribute object. The following counts all unique connections
over the course of the log file and presents them in descending order by
number of occurrences:

```bash
jq -r '.attr.remote' /var/log/mongodb/mongod.log | grep -v 'null' | sort | uniq -c | sort -r
```

Note that connections from the same IP address, but connecting over
different ports, are treated as different connections by this command.
You could limit output to consider IP addresses only, with the following
change:

```bash
jq -r '.attr.remote' /var/log/mongodb/mongod.log | grep -v 'null' | awk -F':' '{print $1}' | sort | uniq -c | sort -r
```

#### Analyzing Driver Connections

The following example counts all remote `MongoDB driver` connections, and
presents each driver type and version in descending order by number
of occurrences:

```bash
jq -cr '.attr.doc.driver' /var/log/mongodb/mongod.log | grep -v null | sort | uniq -c | sort -rn    
```

#### Analyzing Client Types

The following example analyzes the reported client data of remote `MongoDB driver`
connections and client applications, including `mongosh`,
and prints a total for each unique operating system type that
connected, sorted by frequency:

```bash
jq -r '.attr.doc.os.type' /var/log/mongodb/mongod.log | grep -v null | sort | uniq -c | sort -rn
```

The string "Darwin", as reported in this log field, represents a macOS
client.

#### Analyzing Slow Queries

With slow operation logging enabled, the
following returns only the slow operations that took above
2000 milliseconds:, for further analysis:

```bash
jq 'select(.attr.durationMillis>=2000)' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/)
for more information on the `jq` filters shown in this example.

#### Filtering by Component

Log components (the third field in the JSON log output format) indicate the general category a given log message falls under. Filtering by
component is often a great starting place when parsing log messages for
relevant events.

The following example prints only the log messages of
component type **REPL**:

```bash
jq 'select(.c=="REPL")' /var/log/mongodb/mongod.log
```

The following example prints all log messages *except* those of
component type **REPL**:

```bash
jq 'select(.c!="REPL")' /var/log/mongodb/mongod.log
```

The following example print log messages of
component type **REPL** *or*
**STORAGE**:

```bash
jq 'select( .c as $c | ["REPL", "STORAGE"] | index($c) )' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/)
for more information on the `jq` filters shown in this example.

#### Filtering by Known Log ID

Log IDs (the fifth field in the JSON log output format) map to specific log events, and can
be relied upon to remain stable over successive MongoDB releases.

As an example, you might be interested in the following two log events,
showing a client connection followed by a disconnection:

```javascript
{"t":{"$date":"2020-06-01T13:06:59.027-0500"},"s":"I", "c":"NETWORK", "id":22943,"ctx":"listener","msg":"connection accepted from {session_remote} #{session_id} ({connectionCount}{word} now open)","attr":{"session_remote":"127.0.0.1:61298","session_id":164,"connectionCount":11,"word":" connections"}}
{"t":{"$date":"2020-06-01T13:07:03.490-0500"},"s":"I", "c":"NETWORK", "id":22944,"ctx":"conn157","msg":"end connection {remote} ({connectionCount}{word} now open)","attr":{"remote":"127.0.0.1:61298","connectionCount":10,"word":" connections"}}
```

The log IDs for these two entries are `22943` and `22944`
respectively. You could then filter your log output to show only these
log IDs, effectively showing only client connection activity, using the
following `jq` syntax:

```bash
jq 'select( .id as $id | [22943, 22944] | index($id) )' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/)
for more information on the `jq` filters shown in this example.

#### Filtering by Date Range

Log output can be further refined by filtering on the timestamp field,
limiting log entries returned to a specific date range. For example, 
the following returns all log entries that occurred on April 15th, 2020:

```bash
jq 'select(.t["$date"] >= "2020-04-15T00:00:00.000" and .t["$date"] <= "2020-04-15T23:59:59.999")' /var/log/mongodb/mongod.log
```

Note that this syntax includes the full timestamp, including
milliseconds but excluding the timezone offset. 

Filtering by date range can be combined with any of the examples above,
creating weekly reports or yearly summaries for example. The following
syntax expands the "Monitoring Connections" example from earlier to
limit results to the month of May, 2020:

```bash
jq 'select(.t["$date"] >= "2020-05-01T00:00:00.000" and .t["$date"] <= "2020-05-31T23:59:59.999" and .attr.remote)' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/)
for more information on the `jq` filters shown in this example.

### Log Ingestion Services

Log ingestion services are third-party products that intake and
aggregate log files, usually from a distributed cluster of systems, and
provide ongoing analysis of that data in a central location.

The JSON log format allows for more 
flexibility when working with log ingestion and analysis services. Whereas 
plaintext logs generally require some manner of transformation before being 
eligible for use with these products, JSON files can often be consumed out of 
the box, depending on the service. Further, JSON-formatted logs offer more
control when performing filtering for these services, as the
key-value structure offers the ability to specifically import only the
fields of interest, while omitting the rest.

Consult the documentation for your chosen third-party log ingestion
service for more information.

## Log Message Examples

The following examples show log messages in JSON output
format. 

These log messages are presented in pretty-printed format for convenience.

### Startup Warning

This example shows a startup warning:

```javascript
{
  "t": {
    "$date": "2020-05-20T19:17:06.188+00:00"
  },
  "s": "W",
  "c": "CONTROL",
  "id": 22120,
  "ctx": "initandlisten",
  "msg": "Access control is not enabled for the database. Read and write access to data and configuration is unrestricted",
  "tags": [
    "startupWarnings"
  ]
}
```

### Client Connection

This example shows a client connection that includes
client data:

```javascript
{
  "t": {
    "$date": "2020-05-20T19:18:40.604+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 51800,
  "ctx": "conn281",
  "msg": "client metadata",
  "attr": {
    "remote": "192.168.14.15:37666",
    "client": "conn281",
    "doc": {
      "application": {
        "name": "MongoDB Shell"
      },
      "driver": {
        "name": "MongoDB Internal Client",
        "version": "4.4.0"
      },
      "os": {
        "type": "Linux",
        "name": "CentOS Linux release 8.0.1905 (Core) ",
        "architecture": "x86_64",
        "version": "Kernel 4.18.0-80.11.2.el8_0.x86_64"
      }
    }
  }
}
```

### Slow Operation

This example shows a slow operation message:

```javascript
{
  "t": {
    "$date": "2020-05-20T20:10:08.731+00:00"
  },
  "s": "I",
  "c": "COMMAND",
  "id": 51803,
  "ctx": "conn281",
  "msg": "Slow query",
  "attr": {
    "type": "command",
    "ns": "stocks.trades",
    "appName": "MongoDB Shell",
    "command": {
      "aggregate": "trades",
      "pipeline": [
        {
          "$project": {
            "ticker": 1,
            "price": 1,
            "priceGTE110": {
              "$gte": [
                "$price",
                110
              ]
            },
            "_id": 0
          }
        },
        {
          "$sort": {
            "price": -1
          }
        }
      ],
      "allowDiskUse": true,
      "cursor": {},
      "lsid": {
        "id": {
          "$uuid": "fa658f9e-9cd6-42d4-b1c8-c9160fabf2a2"
        }
      },
      "$clusterTime": {
        "clusterTime": {
          "$timestamp": {
            "t": 1590005405,
            "i": 1
          }
        },
        "signature": {
          "hash": {
            "$binary": {
              "base64": "AAAAAAAAAAAAAAAAAAAAAAAAAAA=",
              "subType": "0"
            }
          },
          "keyId": 0
        }
      },
      "$db": "test"
    },
    "planSummary": "COLLSCAN",
    "cursorid": 1912190691485054700,
    "keysExamined": 0,
    "docsExamined": 1000001,
    "hasSortStage": true,
    "usedDisk": true,
    "numYields": 1002,
    "nreturned": 101,
    "queryFramework": "classic"
    "reslen": 17738,
    "locks": {
      "ReplicationStateTransition": {
        "acquireCount": {
          "w": 1119
        }
      },
      "Global": {
        "acquireCount": {
          "r": 1119
        }
      },
      "Database": {
        "acquireCount": {
          "r": 1119
        }
      },
      "Collection": {
        "acquireCount": {
          "r": 1119
        }
      },
      "Mutex": {
        "acquireCount": {
          "r": 117
        }
      }
    },
    "storage": {
      "data": {
        "bytesRead": 232899899,
        "timeReadingMicros": 186017
      },
      "timeWaitingMicros": {
        "cache": 849
      }
    },
    "remote": "192.168.14.15:37666",
    "protocol": "op_msg",
    "durationMillis": 22427
  }
}
```

### Escaping

This example demonstrates character escaping, as shown in the `setName` field of the 
attribute object:

```javascript
{
  "t": {
    "$date": "2020-05-20T19:11:09.268+00:00"
  },
  "s": "I",
  "c": "REPL",
  "id": 21752,
  "ctx": "ReplCoord-0",
  "msg": "Scheduling remote command request",
  "attr": {
    "context": "vote request",
    "request": "RemoteCommand 229 -- target:localhost:27003 db:admin cmd:{ replSetRequestVotes: 1, setName: \"my-replica-name\", dryRun: true, term: 3, candidateIndex: 0, configVersion: 2, configTerm: 3, lastAppliedOpTime: { ts: Timestamp(1589915409, 1), t: 3 } }"
  }
}
```

### View

Starting in MongoDB 5.0, log messages for slow queries on views include a
`resolvedViews` field that contains the view details:

```javascript
"resolvedViews": [ {
   "viewNamespace": <String>,  // namespace and view name
   "dependencyChain": <Array of strings>,  // view name and collection
   "resolvedPipeline": <Array of documents>  // aggregation pipeline for view
} ]
```

The following example uses the `test` database and creates a view
named `myView` that sorts the documents in `myCollection` by the
`firstName` field:

```javascript
use test
db.createView( "myView", "myCollection", [ { $sort: { "firstName" : 1 } } ] )
```

Assume a slow query is run on `myView`.
The following example log message contains a `resolvedViews` field for
`myView`:

```javascript
{
   "t": {
      "$date": "2021-09-30T17:53:54.646+00:00"
   },
   "s": "I",
   "c": "COMMAND",
   "id": 51803,
   "ctx": "conn249",
   "msg": "Slow query",
   "attr": {
      "type": "command",
      "ns": "test.myView",
      "appName": "MongoDB Shell",
      "command": {
         "find": "myView",
         "filter": {},
         "lsid": {
            "id": { "$uuid": "ad176471-60e5-4e82-b977-156a9970d30f" }
         },
         "$db": "test"
      },
      "planSummary":"COLLSCAN",
         "resolvedViews": [ {
            "viewNamespace": "test.myView",
            "dependencyChain": [ "myView", "myCollection" ],
            "resolvedPipeline": [ { "$sort": { "firstName": 1 } } ]
         } ],
         "keysExamined": 0,
         "docsExamined": 1,
         "hasSortStage": true,
         "cursorExhausted": true,
         "numYields": 0,
         "nreturned": 1,
         "queryHash": "3344645B",
         "planCacheKey": "1D3DE690",
         "queryFramework": "classic"
         "reslen": 134,
         "locks": { "ParallelBatchWriterMode": { "acquireCount": { "r": 1 } },
         "ReplicationStateTransition": { "acquireCount": { "w": 1 } },
         "Global": { "acquireCount": { "r": 4 } },
         "Database": { "acquireCount": {"r": 1 } },
         "Collection": { "acquireCount": { "r": 1 } },
         "Mutex": { "acquireCount": { "r": 4 } } },
         "storage": {},
         "remote": "127.0.0.1:34868",
         "protocol": "op_msg",
         "durationMillis": 0
      }
   }
}
```

### Authorization

Starting in MongoDB 5.0, log messages for slow queries include a
`system.profile.authorization` section. These metrics help
determine if a request is delayed because of contention for the user
authorization cache. 

```javascript
"authorization": {
   "startedUserCacheAcquisitionAttempts": 1,
   "completedUserCacheAcquisitionAttempts": 1,
   "userCacheWaitTimeMicros": 508
 },
```

## Download Your Logs

You can use MongoDB Atlas to download a zipped file containing 
the logs for a selected hostname or process in your database 
deployment. To learn more, see 
View and Download MongoDB Logs.
