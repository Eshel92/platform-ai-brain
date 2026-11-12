<!-- Part 7 of 8 of reference/parameters.md (split because the page is big). -->

### Health Manager Parameters

**`activeFaultDurationSecs`**

Available for `mongos` only.

*Type*: Document

The amount of time to wait from a Health Managers Overview failure until the 
mongos is removed from the cluster, in seconds.

When a failure is detected and a Health Manager is configured as 
`critical`, the server waits for the specified interval 
before removing the `mongos` from the cluster. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

Available for `mongos` only.

*Type*: Array of documents

Use this parameter to set intensity levels for Health Managers.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

Available for `mongos` only.

*Type*: Array of documents

How often this Health Manager will run, in milliseconds.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

Available for `mongos` only.

*Type*: Document

Progress Monitor runs tests 
to ensure that Health Manager checks do not become stuck or 
unresponsive. Progress Monitor runs these tests in intervals specified 
by `interval`. If a health check begins but does not complete within
the timeout given by `deadline`, Progress Monitor stops the 
mongos and removes it from the cluster.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

Available for both `mongod` and `mongos`.

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

mongos --setParameter honorSystemUmask=true
```

**Note:**

`honorSystemUmask` is not available on Windows systems.

**`journalCommitInterval`**

Available for `mongod` only.

Specify an integer between `1` and `500` signifying the number
of milliseconds (ms) between journal commits.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Consider the following example which sets the
`journalCommitInterval` to `200` ms:

```javascript
db.adminCommand( { setParameter: 1, journalCommitInterval: 200 } )
```

**See also:**

`storage.journal.commitIntervalMs`

**`minSnapshotHistoryWindowInSeconds`**

**New in version:** 5.0

Available for `mongod` only.

*Default*: `300`

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
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

**Changed in version:** 7.0

Available for `mongod` only.

*Type*: integer

Specifies the maximum number of concurrent read transactions (read tickets)
allowed into the storage engine.

**Note:**

Starting in version 7.0, MongoDB dynamically adjusts the number of 
tickets to optimize performance, with a highest possible value of 128.

Modifying this value can cause performance issues or errors. To 
determine if disabling the dynamic concurrent storage engine 
transactions algorithm is optimal for the cluster, contact 
[MongoDB Support](https://www.mongodb.com/docs/manual/support/).

Starting in MongoDB 7.0, this parameter is available for all storage 
engines. In earlier versions, this parameter is available for the 
WiredTiger storage engine only.

**See also:**

`wiredTiger.concurrentTransactions`

**`storageEngineConcurrentWriteTransactions`**

**Changed in version:** 7.0

Available for `mongod` only.

*Type*: integer 

Specifies the maximum number of concurrent write transactions allowed
into the WiredTiger storage engine.

**Note:**

Starting in version 7.0, MongoDB dynamically adjusts the number of 
tickets to optimize performance, with a highest possible value of 128.

Modifying this value can cause performance issues or errors. To 
determine if disabling the dynamic concurrent storage engine 
transactions algorithm is optimal for the cluster, contact 
[MongoDB Support](https://www.mongodb.com/docs/manual/support/).

Starting in MongoDB 7.0, this parameter is available for all storage 
engines. In earlier versions, this parameter is available for the 
WiredTiger storage engine only.

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
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

**`temporarilyUnavailableBackoffBaseMs`**

Available for `mongod` only.

*Default*: 1000

Specifies the initial delay before retying a write operation that was
rolled back due to cache pressure.

In rare circumstances, a write can fail due to cache pressure. When
this happens MongoDB issues a `TemporarilyUnavailable` error and
increments the `temporarilyUnavailableErrors` counter in two places:
the slow query log and the Full Time Diagnostic Data Capture
(FTDC).

Individual operations within multi-document transactions never return
`TemporarilyUnavailable` errors.

Adjust the write retry properties by modifying the
`temporarilyUnavailableBackoffBaseMs` and
`temporarilyUnavailableMaxRetries` parameters.

Contact support if you experience any cache pressure 
issues. 

The parameter accepts:

| Value | Description |
|---|---|
| `integer >= 0` | Defaults to 1 second. The initial delay between retries. The value increases with each retry to a maximum of 55 seconds. A larger value increases the chance that the cache pressure will be reduced before the next retry. To configure number of retries, use `temporarilyUnavailableMaxRetries`. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To set a new value, use `db.adminCommand()`:

```javascript
db.adminCommand( { setParameter: 1, temporarilyUnavailableBackoffBaseMs: 3 } )
```

**New in version:** 6.1.0

**`temporarilyUnavailableMaxRetries`**

Available for `mongod` only.

*Default*: 10

Specifies the maximum number of retries when a write operation is
rolled back due to cache pressure.

In rare circumstances, a write can fail due to cache pressure. When
this happens MongoDB issues a `TemporarilyUnavailable` error and
increments the `temporarilyUnavailableErrors` counter in two places:
the slow query log and the Full Time Diagnostic Data Capture
(FTDC).

Individual operations within multi-document transactions never return
`TemporarilyUnavailable` errors.

Adjust the write retry properties by modifying the
`temporarilyUnavailableBackoffBaseMs` and
`temporarilyUnavailableMaxRetries` parameters.

Contact support if you experience any cache pressure 
issues. 

The parameter accepts:

| Value | Description |
|---|---|
| `integer >= 0` | The maximum number of retries. There is an increasing delay between retries. To configure the backoff time, use `temporarilyUnavailableBackoffBaseMs`. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To set a new value, use `db.adminCommand()`:

```javascript
db.adminCommand( { setParameter: 1, temporarilyUnavailableMaxRetries: 5 } )
```

**New in version:** 6.1.0

**`upsertMaxRetryAttemptsOnDuplicateKeyError`**

Available for both `mongod` and `mongos`.

**New in version:** 7.0.22

Maximum number of retry attempts when an `upsert` operation
encounters a duplicate key error. 

*Type*: Integer

*Default*: 100

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the maximum number of times the server 
retries an `upsert` operation when encountering a duplicate key 
error to `50`.

```bash
mongod --setParameter "upsertMaxRetryAttemptsOnDuplicateKeyError=50"
```

During run time, you can also set the parameter with the 
`setParameter` command:

```javascript
db.adminCommand( { 
   setParameter: 1, 
   upsertMaxRetryAttemptsOnDuplicateKeyError: 50 
} )
```
