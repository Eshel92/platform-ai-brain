<!-- Part 4 of 8 of reference/parameters.md (split because the page is big). -->

### Logging Parameters

**`logLevel`**

Available for both `mongod` and `mongos`.

*Default*: 0 (informational)

Specify an integer between `0` and `5` signifying the verbosity
of the logging, where `5` is the
most verbose. [#log-message]_

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the `logLevel` to `2`:

```javascript
db.adminCommand( { setParameter: 1, logLevel: 2 } )
```

**See also:**

- `logComponentVerbosity`
- `systemLog.verbosity`

**`logComponentVerbosity`**

Available for both `mongod` and `mongos`.

*Default*: 0

Sets the verbosity levels of various components for log messages. The verbosity level determines the
amount of Informational and Debug
messages MongoDB outputs. [#log-message2]_

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

For a component, you can also specify `-1` to inherit the parent's
verbosity level.

To specify the verbosity level, use a document similar to the
following:

```none
{
  verbosity: <int>,
  <component1>: { verbosity: <int> },
  <component2>: {
     verbosity: <int>,
     <component3>: { verbosity: <int> }
  },
  ...
}
```

For the components, you can specify just the `<component>: <int>`
in the document, unless you are setting both the parent verbosity
level and that of the child component(s) as well:

```none
{
  verbosity: <int>,
  <component1>: <int> ,
  <component2>: {
     verbosity: <int>,
     <component3>: <int>
  }
  ...
}
```

The top-level `verbosity` field corresponds to
`systemLog.verbosity` which sets the default level for all
components. The default value of `systemLog.verbosity` is
`0`.

The components correspond to the following settings:

- `accessControl`

- `assert`

- `command`

- `control`

- `ftdc`

- `geo`

- `index`

- `network`

- `query`

- `queryStats`

- `replication`

- `replication.election`

- `replication.heartbeats`

- `replication.initialSync`

- `replication.rollback`

- `recovery`

- `sharding`

- `storage`

- `storage.journal`

- `transaction`

- `write`

Unless explicitly set, the component has the verbosity level of its
parent. For example, `storage` is the parent of
`storage.journal`. That is, if you specify a `storage` verbosity level, this level
also applies to:

- `storage.journal` components
  *unless* you specify the verbosity level for
  `storage.journal`.

- `storage.recovery` components
  *unless* you specify the verbosity level for
  `storage.recovery`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the `default verbosity
level` to `1`, the `query` to `2`, the
`storage` to `2`,
and the `storage.journal` to `1`.

```javascript
db.adminCommand( {
   setParameter: 1,
   logComponentVerbosity: {
      verbosity: 1,
      query: { verbosity: 2 },
      storage: {
         verbosity: 2,
         journal: {
            verbosity: 1
         }
      }
   }
} )
```

You can also set parameter `logComponentVerbosity` at
startup time, passing the verbosity level document as a string.

```bash
mongod --setParameter "logComponentVerbosity={command: 3}"
```

`mongosh` also provides the `db.setLogLevel()`
to set the log level for a single component. For various ways to set
the log verbosity level, see log-messages-configure-verbosity.

**`maxLogSizeKB`**

Available for both `mongod` and `mongos`.

*Type*: non-negative integer

*Default*: 10

Specifies the maximum size, in kilobytes, for an individual
attribute field in a log entry; attributes exceeding this limit are
truncated.

Truncated attribute fields print field content up to the
`maxLogSizeKB` limit and excise field content past that
limit, retaining valid JSON formatting. Log entries that contain
truncated attributes append a `truncated` object to the end of the
log entry.

See log message truncation for more
information.

A value of `0` disables truncation entirely. Negative values for
this parameter are not valid.

**Warning:**

Using a large value, or disabling truncation with a value of
`0`, may adversely affect system performance and negatively
impact database operations.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the maximum log line size to `20`
kilobytes:

```bash
mongod --setParameter maxLogSizeKB=20
```

**`profileOperationResourceConsumptionMetrics`**

Available for `mongod` only.

*Type*: boolean

*Default*: false

Flag that determines whether operations collect resource 
consumption metrics and report them in the slow query logs. 
If you enable profiling, 
these metrics are also included.

If set to `true`, running the `explain` command
returns operationMetrics when the verbosity 
is `executionStats` or higher.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`quiet`**

Available for both `mongod` and `mongos`.

Sets quiet logging mode. If
`1`, `mongod` will go into a quiet logging
mode which will not log the following events/activities:

- connection events;

- the `drop` command, the
  `dropIndexes` command, the
  `validate` command; and

- replication synchronization activities.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Consider the following example which sets the
`quiet` parameter to `1`:

```javascript
db.adminCommand( { setParameter: 1, quiet: 1 } )
```

**See also:**

`systemLog.quiet`

**`redactClientLogData`**

Available for both `mongod` and `mongos`.

*Type*: boolean

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

Configure the `mongod` or `mongos` to
redact any message accompanying a given log event before logging.
This prevents the program from writing potentially sensitive data
stored on the database to the diagnostic log. Metadata such as error
or operation codes, line numbers, and source file names are still
visible in the logs.

Use `redactClientLogData` in conjunction with
/core/security-encryption-at-rest and
/core/security-transport-encryption to assist compliance with
regulatory requirements.

To enable log redaction at startup, you can either:

- Start `mongod` with the
  `--redactClientLogData` option: 

  ```javascript
  mongod --redactClientLogData
  ```

- Set the `security.redactClientLogData` option in the 
  configuration file:

  ```yaml
  security: 
     redactClientLogData: true
     ...
  ```

You can't use the `--setParameter` 
option to set `redactClientLogData` at startup.

To enable log redaction on a running `mongod` or
`mongos`, use the following command:

```javascript
db.adminCommand( { setParameter: 1, redactClientLogData : true } )
```

**See also:**

`security.redactClientLogData`

**`redactEncryptedFields`**

**New in version:** 6.1.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: `true`

Configures `mongod` and `mongos` to redact field values
of encrypted `Binary` data from all 
log messages.

- If the `redactClientLogData` parameter or the
  `security.redactClientLogData` setting is set to `false` and
  `redactEncryptedFields` is set to `true` (the default), encrypted 
  fields are redacted from all log messages.

- If the `redactClientLogData` parameter or
  `security.redactClientLogData` setting is set to `true`,
  all fields are redacted, regardless of the `redactEncryptedFields`
  setting.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`traceExceptions`**

Available for both `mongod` and `mongos`.

Configures `mongod` to log full source code stack traces
for every database and socket C++ exception, for use with debugging.
If `true`, `mongod` will log full stack traces.

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

Consider the following example which sets the
`traceExceptions` to `true`:

```javascript
db.adminCommand( { setParameter: 1, traceExceptions: true } )
```

**See also:**

`systemLog.traceAllExceptions`

**`suppressNoTLSPeerCertificateWarning`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

By default, a `mongod` or `mongos` with
TLS/SSL enabled and
`net.ssl.allowConnectionsWithoutCertificates` : `true`
lets clients connect without providing a certificate for
validation while logging an warning. Set
`suppressNoTLSPeerCertificateWarning` to `1` or `true` to
suppress those warnings.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following operation sets `suppressNoTLSPeerCertificateWarning`
to `true`:

```bash
db.adminCommand( { setParameter: 1, suppressNoTLSPeerCertificateWarning: true} )
```

**`enableDetailedConnectionHealthMetricLogLines`**

**New in version:** 7.0

Available for both `mongod` and `mongos`. 

*Type*: boolean

*Default*: true 

Determines whether to enable specific log messages related to cluster 
connection health metrics. If 
`enableDetailedConnectionHealthMetricLogLines` is set to 
`false`, the following log messages are turned off, but MongoDB still 
collects data on the cluster connection health metrics:

| Log Message | Description |
|---|---|
| Accepted TLS connection from peer | Indicates that the server successfully parsed the peer certificate during the TLS handshake with an accepted ingress connection. |
| Ingress TLS handshake complete | Indicates that the TLS handshake with an ingress connection is complete. |
| Hello completed | Indicates that the initial connection handshake completed on an incoming client connection. MongoDB displays the log message only with the first `hello` command. |
| Auth metrics report | Specifies the completion of a step in the authentication conversation. |
| Received first command on ingress connection since session start or auth handshake | Indicates that an ingress connection received the first command that is not part of the handshake. |
| Slow network response send time | Indicates that the time spent, in milliseconds, to send the response back to the client over an ingress connection takes more time than the duration defined by the `slowMS` server parameter. |
| Completed client-side verification of OCSP request | If the peer doesn't include an OCSP (Online Certificate Status Protocol) response to the TLS handshake when an egress TLS connection is established, the server must send an OCSP request to the certificate authority. MongoDB writes this log message when the certificate authority receives the OCSP response. |
| Slow connection establishment | Indicates that the time taken to send a response back to the client over an ingress connection takes longer than the threshold specified with the `slowConnectionThresholdMillis` parameter. MongoDB also emits this log message when the connection establishment times out. |
| Operation timed out while waiting to acquire connection | Indicates that an operation timed out while waiting to acquire an egress connection. |
| Acquired connection for remote operation and completed writing to wire | Indicates that the server took one millisecond or longer to write an outgoing request on an egress connection, counting from the instant when the connection establishes. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.


### Diagnostic Parameters

To facilitate analysis of the MongoDB server behavior by MongoDB
engineers, MongoDB logs server statistics to diagnostic files at
periodic intervals.

For `mongod`, the diagnostic data files are stored in the
`diagnostic.data` directory under the `mongod` instance's
`--dbpath` or `storage.dbPath`.

For `mongos`, the diagnostic data files, by default, are
stored in a directory under the `mongos` instance's
`--logpath` or `systemLog.path` directory. The diagnostic
data directory is computed by truncating the logpath's file
extension(s) and concatenating `diagnostic.data` to the remaining
name.

For example, if `mongos` has ``--logpath
/var/log/mongodb/mongos.log.201708015``, then the diagnostic data
directory is `/var/log/mongodb/mongos.diagnostic.data/` directory. To
specify a different diagnostic data directory for `mongos`,
set the `diagnosticDataCollectionDirectoryPath` parameter.

The following parameters support diagnostic data capture (FTDC):

**Note:**

The default values for the diagnostic data capture interval and the
maximum sizes are configured to provide data to MongoDB engineers
with minimal impact on performance and storage size. Typically, these
values need modification only when requested by MongoDB engineers
for specific diagnostic purposes.

**`diagnosticDataCollectionEnabled`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: true

Determines whether to enable the collecting and logging of data for
diagnostic purposes. Diagnostic logging is enabled by default.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following disables the diagnostic collection:

```bash
mongod --setParameter diagnosticDataCollectionEnabled=false
```

**`diagnosticDataCollectionDirectoryPath`**

Available for `mongos` only.

*Type*: String

**Warning:**

If Full Time Diagnostic Data Capture (FTDC) is 
disabled with `diagnosticDataCollectionEnabled` or if 
`systemLog.destination` is set to `syslog`, you must restart 
`mongos` after setting 
`diagnosticDataCollectionDirectoryPath`.

Specify the directory for the diagnostic directory for
`mongos`. If the directory does not exist,
`mongos` creates the directory.

If unspecified, the diagnostic data directory is computed by
truncating the `mongos` instance's `--logpath` or
`systemLog.path` file extension(s) and concatenating
`diagnostic.data`.

For example, if `mongos` has ``--logpath
/var/log/mongodb/mongos.log.201708015``, then the diagnostic data
directory is `/var/log/mongodb/mongos.diagnostic.data/`.

If the `mongos` cannot create the specified directory, the 
diagnostic data capture is disabled for that instance. `mongos`
may not be able to create the specified directory if a file with the same 
name already exists in the path or if the process does not have permissions 
to create the directory.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`diagnosticDataCollectionDirectorySizeMB`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 200

Specifies the maximum size, in megabytes, of the `diagnostic.data`
directory. If directory size exceeds this number, the oldest
diagnostic files in the directory are automatically deleted based on
the timestamp in the file name.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the maximum size of the directory to
`250` megabytes:

```bash
mongod --setParameter diagnosticDataCollectionDirectorySizeMB=250
```

The minimum value for
`diagnosticDataCollectionDirectorySizeMB` is `10`
megabytes. `diagnosticDataCollectionDirectorySizeMB` must
be greater than maximum diagnostic file size
`diagnosticDataCollectionFileSizeMB`.

**`diagnosticDataCollectionFileSizeMB`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10

Specifies the maximum size, in megabytes, of each diagnostic
file. If the file exceeds the maximum file size, MongoDB creates a new file.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the maximum size of each diagnostic
file to `20` megabytes:

```bash
mongod --setParameter diagnosticDataCollectionFileSizeMB=20
```

The minimum value for
`diagnosticDataCollectionFileSizeMB` is `1` megabyte.

**`diagnosticDataCollectionPeriodMillis`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 1000

Specifies the interval, in milliseconds, at which to collect
diagnostic data.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the interval to
`5000` milliseconds or 5 seconds:

```bash
mongod --setParameter diagnosticDataCollectionPeriodMillis=5000
```

The minimum value for
`diagnosticDataCollectionPeriodMillis` is `100`
milliseconds.
