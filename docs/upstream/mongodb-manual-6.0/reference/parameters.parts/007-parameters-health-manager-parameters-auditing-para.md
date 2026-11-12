<!-- Part 7 of 8 of reference/parameters.md (split because the page is big). -->

### Health Manager Parameters

**`activeFaultDurationSecs`**

*Type*: Document

Available for `mongos` only.

The amount of time to wait from a Health Managers Overview failure until the 
mongos is removed from the cluster, in seconds.

When a failure is detected and a Health Manager is configured as 
`critical`, the server waits for the specified interval 
before removing the `mongos` from the cluster. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set the duration from failure to crash to five
minutes, issue the following at startup:

```bash
mongos --setParameter activeFaultDurationSecs=300
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      activeFaultDurationSecs: 300 
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `activeFaultDurationSecs`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   activeFaultDurationSecs: 300
```

**`healthMonitoringIntensities`**

*Type*: Array of documents

Available for `mongos` only.

Use this parameter to set intensity levels for Health Managers.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

`healthMonitoringIntensities` accepts an array of documents,
`values`. Each document in `values` takes two fields: 

- `type`, the Health Manager facet 
- `intensity`, the intensity level

#### Health Managers

| Facet | What the Health Observer Checks |
|---|---|
| `configServer` | Cluster health issues related to connectivity to the config server. |
| `dns` | Cluster health issues related to DNS availability and functionality. |
| `ldap` | Cluster health issues related to LDAP availability and functionality. |

#### Intensity Levels

| Intensity Level | Description |
|---|---|
| `critical` | The Health Manager on this facet is enabled and has the ability to move the failing mongos out of the cluster if an error occurs. The Health Manager waits the amount of time specified by `activeFaultDurationSecs` before stopping and moving the mongos out of the cluster automatically. |
| `non-critical` | The Health Manager on this facet is enabled and logs errors, but the mongos remains in the cluster if errors are encountered. |
| `off` | The Health Manager on this facet is disabled. The mongos does not perform any health checks on this facet. This is the default intensity level. |

For example, to set the `dns` Health Manager facet to the 
`critical` intensity level, issue the following at startup:

```bash
mongos --setParameter 'healthMonitoringIntensities={ values:[ { type:"dns", intensity: "critical"} ] }'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      healthMonitoringIntensities: { values: [ { type: "dns", intensity: "critical" } ] } } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `healthMonitoringIntensities`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   healthMonitoringIntensities: "{ values:[ { type:\"dns\", intensity: \"critical\"} ] }"
```

**`healthMonitoringIntervals`**

*Type*: Array of documents

Available for `mongos` only.

How often this Health Manager will run, in milliseconds.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

`healthMonitoringIntervals` accepts an array of documents,
`values`. Each document in `values` takes two fields:

- `type`, the Health Manager facet 
- `interval`, the time interval it runs at, in milliseconds

#### Health Managers

| Facet | What the Health Observer Checks |
|---|---|
| `configServer` | Cluster health issues related to connectivity to the config server. |
| `dns` | Cluster health issues related to DNS availability and functionality. |
| `ldap` | Cluster health issues related to LDAP availability and functionality. |

For example, to set the `ldap` Health Manager facet to the 
run health checks every 30 seconds, issue the following at startup:

```bash
mongos --setParameter 'healthMonitoringIntervals={ values:[ { type:"ldap", interval: "30000"} ] }'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      healthMonitoringIntervals: { values: [ { type: "ldap", interval: "30000" } ] } } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `healthMonitoringIntervals`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   healthMonitoringIntervals: "{ values: [{type: \"ldap\", interval: 200}] }"
```

**`progressMonitor`**

*Type*: Document

Available for `mongos` only.

Progress Monitor runs tests 
to ensure that Health Manager checks do not become stuck or 
unresponsive. Progress Monitor runs these tests in intervals specified 
by `interval`. If a health check begins but does not complete within
the timeout given by `deadline`, Progress Monitor stops the 
mongos and removes it from the cluster.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

#### `progressMonitor` Fields

| Field | Description | Units |
|---|---|---|
| `interval` | How often to ensure Health Managers are not stuck or unresponsive. | Milliseconds |
| `deadline` | Timeout before automatically failing the mongos if a Health Manager check is not making progress. | Seconds |

To set the `interval` to 1000 milliseconds and the `deadline` 
to 300 seconds, issue the following at startup:

```bash
mongos --setParameter 'progressMonitor={"interval": 1000, "deadline": 300}'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      progressMonitor: { interval: 1000, deadline: 300 } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `progressMonitor`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   progressMonitor: "{ interval: 1000, deadline: 300 }"
```


### Storage Parameters

**`honorSystemUmask`**

Available for `mongod` only.

*Default*: `false`

If `honorSystemUmask` is set to `true`, new files
created by MongoDB have permissions in accordance with the
user's `umask` settings. You cannot set `processUmask`
if `honorSystemUmask` is set to `true`.

If `honorSystemUmask` is set to `false`, new files
created by MongoDB have permissions set to `600`, which gives
read and write permissions only to the owner. New directories have
permissions set to `700`. You can use `processUmask`
to override the default permissions for groups and other users on
all new files created by MongoDB.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter honorSystemUmask=true
```

**Note:**

`honorSystemUmask` is not available on Windows systems.

**`journalCommitInterval`**

Available for `mongod` only.

Specify an integer between `1` and `500` signifying the number
of milliseconds (ms) between journal commits.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

Consider the following example which sets the
`journalCommitInterval` to `200` ms:

```javascript
db.adminCommand( { setParameter: 1, journalCommitInterval: 200 } )
```

**See also:**

`storage.journal.commitIntervalMs`

**`minSnapshotHistoryWindowInSeconds`**

**New in version:** 5.0

*Default*: `300`

Available for `mongod` only.

The minimum time window in seconds for which the storage engine keeps
the snapshot history. If you query data using read concern
`"snapshot"` and specify an
atClusterTime value older than the specified
`minSnapshotHistoryWindowInSeconds`, `mongod` returns
a `SnapshotTooOld` error.

**Warning:**

In sharded clusters, changing the default `minSnapshotHistoryWindowInSeconds` 
value on config server nodes may cause 
internal operations to fail.

Do not set `minSnapshotHistoryWindowInSeconds` to `0` on config server 
nodes. Setting this parameter to `0` causes internal operations conducting 
`snapshot` reads targeting the config server with a specified 
`atClusterTime` to fail.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

Specify an integer greater than or equal to (`>=`) 0.

Consider the following example which sets the
`minSnapshotHistoryWindowInSeconds` to `600` seconds:

```javascript
db.adminCommand( { setParameter: 1, minSnapshotHistoryWindowInSeconds: 600 } )
```

**Note:**

Increasing the value of
`minSnapshotHistoryWindowInSeconds` increases disk
usage. For more information, see storage-snapshot-history.

To modify this value for a MongoDB Atlas cluster, you
must contact Atlas Support.

**`processUmask`**

Available for `mongod` only.

Overrides the default permissions used for groups and other users
when `honorSystemUmask` is set to `false`. By default,
when `honorSystemUmask` is set to `false`, new files
created by MongoDB have permissions set to `600`. Use the
`processUmask` parameter to override this default with a custom
`umask` value. The file owner inherits permissions from the system
`umask`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

You cannot set this parameter if `honorSystemUmask` is set
to `true`. 

Consider the following example, which sets the permissions for groups
and other users to read/write only and retains the system `umask`
settings for the owner:

```bash
mongod --setParameter processUmask=011
```

**Note:**

`processUmask` is not available on Windows systems.

**`storageEngineConcurrentReadTransactions`**

Available for `mongod` only.

*Default*: 128

**Changed in version:** 6.0

The `wiredTigerConcurrentReadTransactions` parameter was renamed to 
`storageEngineConcurrentReadTransactions`.

Available for the WiredTiger storage engine only.

Specify the maximum number of concurrent read transactions allowed
into the WiredTiger storage engine.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

```javascript
db.adminCommand( { setParameter: 1, storageEngineConcurrentReadTransactions: <num> } )
```

**See also:**

`wiredTiger.concurrentTransactions`

**`storageEngineConcurrentWriteTransactions`**

Available for `mongod` only.

*Default*: 128

**Changed in version:** 6.0

The `wiredTigerConcurrentReadTransactions` parameter was renamed to 
`storageEngineConcurrentReadTransactions`.

Available for the WiredTiger storage engine only.

Specify the maximum number of concurrent write transactions allowed
into the WiredTiger storage engine.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

```javascript
db.adminCommand( { setParameter: 1, storageEngineConcurrentWriteTransactions: <num> } )
```

**See also:**

`wiredTiger.concurrentTransactions`

**`syncdelay`**

Available for `mongod` only.

*Default*: 60

Specify the interval in seconds when
`mongod` flushes its working memory to disk. By
default, `mongod` flushes memory to disk every 60
seconds. In almost every situation you should not set this value
and use the default setting.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

Consider the following example which sets the `syncdelay` to
`60` seconds:

```javascript
db.adminCommand( { setParameter: 1, syncdelay: 60 } )
```

To provide durable data, WiredTiger
uses checkpoints. For more
details, see journaling-wiredTiger.

**See also:**

- `journalCommitInterval`
- `storage.syncPeriodSecs`


### WiredTiger Parameters

**`wiredTigerEngineRuntimeConfig`**

Available for `mongod` only.

Specify `wiredTiger` storage engine configuration options for a
running `mongod` instance. 

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

**Warning:**

Avoid modifying the `wiredTigerEngineRuntimeConfig`
unless under the direction from MongoDB engineers as this setting has
major implication across both WiredTiger and MongoDB.

Consider the following operation prototype:

```javascript
db.adminCommand({
   "setParameter": 1,
   "wiredTigerEngineRuntimeConfig": "<option>=<setting>,<option>=<setting>"
})
```

**`wiredTigerFileHandleCloseIdleTime`**

Available for `mongod` only.

*Type*: integer 

*Default*: 600

Specifies the amount of time in seconds that a file handle in `wiredTiger` 
can remain idle before being closed.

If you set `wiredTigerFileHandleCloseIdleTime` to `0`, idle handles 
are not closed. 

**Tip:**

This parameter is case sensitive. If you capitalize the `w` in 
`wiredTigerFileHandleCloseIdleTime` and run the parameter, the operation
returns the following error message:

```bash
{ "code":2,"codeName":"BadValue","errmsg":"Unknown --setParameter 'WiredTigerFileHandleCloseIdleTime'" }
```

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example:

```bash
mongod --setParameter wiredTigerFileHandleCloseIdleTime=100000
```

See the WiredTiger documentation for all available
:wtdocs-v5.0:`WiredTiger configuration options </struct_w_t___c_o_n_n_e_c_t_i_o_n.html#>`.


### Auditing Parameters

**`auditAuthorizationSuccess`**

*Type*: boolean

*Default*: false

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

Available for both `mongod` and `mongos`.

Enables the auditing of authorization
successes for the authCheck
action.

When `auditAuthorizationSuccess` is `false`, the
audit system only logs the authorization
failures for `authCheck`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

To enable the audit of authorization successes, issue the following
command:

```javascript
db.adminCommand( { setParameter: 1, auditAuthorizationSuccess: true } )
```

Enabling `auditAuthorizationSuccess` degrades performance
more than logging only the authorization failures.

If runtime audit configuration
is enabled, the `auditAuthorizationSuccess` parameter
should not appear in the `mongod` or `mongos` configuration
file. The server will fail to start if the parameter is present.

**See also:**

`getParameter`

**`auditConfigPollingFrequencySecs`**

**New in version:** 5.0

*Type*: integer

*Default*: 300

A sharded cluster may have servers which maintain audit
configuration settings for the cluster. Set the interval, in
seconds, for non-configured servers to poll a config server for the
current audit generation. If this value returned differs from the
previously known value, the initiating node will request the current
configuration and update its internal state.

**Note:**

Using the default value of 300 seconds, non-config nodes may lag up
to 5 minutes behind a setAuditConfig command.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`auditEncryptionHeaderMetadataFile`**

**New in version:** 6.0

*Type*: string

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

Available for both `mongod` and `mongos`.

Path and file name for logging metadata audit headers for audit
log encryption. A header is
placed at the top of each audit log file and contains metadata for
decrypting the audit log. The headers are also stored in the
audit log.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following sets the path and file for
`auditEncryptionHeaderMetadataFile`:

```bash
mongod --setParameter auditEncryptionHeaderMetadataFile=/auditFiles/auditHeadersMetadataFile.log
```

**`auditEncryptKeyWithKMIPGet`**

**New in version:** 6.0

*Type*: boolean

*Default*: false

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

Available for both `mongod` and `mongos`.

Enables audit log encryption for Key Management
Interoperability Protocol (KMIP) servers that only support KMIP
protocol version 1.0 or 1.1.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following example sets
`auditEncryptKeyWithKMIPGet` to `true`:

```bash
mongod --setParameter auditEncryptKeyWithKMIPGet=true
```
