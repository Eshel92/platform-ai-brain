<!-- Part 5 of 8 of reference/parameters.md (split because the page is big). -->

### Replication and Consistency

**`connectTimeoutMs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10000

Sets the connection timeout,
in milliseconds, for the replica set 
monitor.

This parameter is only available at startup. If you set this parameter,
it must be greater than or equal to 500.

The following example sets `connectTimeoutMs` for a `mongod` 
instance to 700 milliseconds:

```bash
mongod --setParameter connectTimeoutMs=700
```

**`disableSplitHorizonIPCheck`**

**New in version:** 5.0.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

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

To allow configuration changes using IP addresses, set
`disableSplitHorizonIPCheck=true` using the command line:

```javascript
/usr/local/bin/mongod  --setParameter disableSplitHorizonIPCheck=true -f /etc/mongod.conf
```

To allow configuration changes using IP addresses, set
`disableSplitHorizonIPCheck=true` using the node's configuration
file:

```javascript
setParameter:
   disableSplitHorizonIPCheck: true
```

If you attempt to update `disableSplitHorizonIPCheck` at runtime,
`db.adminCommand` returns an error:

```javascript
db.adminCommand( { setParameter: 1, "disableSplitHorizonIPCheck": true } )
MongoServerError: not allowed to change [disableSplitHorizonIPCheck] at runtime
```

**`enableOverrideClusterChainingSetting`**

**New in version:** 5.0.2

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

If `enableOverrideClusterChainingSetting` is `true`,
replica set secondary members can replicate data from
other secondary members even if `settings.chainingAllowed` is
`false`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the
`enableOverrideClusterChainingSetting` for a
`mongod` instance to `true`:

```bash
mongod --setParameter enableOverrideClusterChainingSetting=true
```

**`heartBeatFrequencyMs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10000

When `replicaSetMonitorProtocol` is set to `'sdam'`, 
`heartBeatFrequencyMs` determines how long, 
in milliseconds, to wait between `hello` requests.

When `replicaSetMonitorProtocol` is set to `'streamable'`, 
`heartBeatFrequencyMs` determines how long, 
in milliseconds, to wait between `hello` round trip time
(RTT) measurements. RTT measurements are used in 
server selection.

This parameter is only available at startup. If you set this
parameter, it must be greater than or equal to 500.

The following example sets `heartBeatFrequencyMs` 
in a `mongod` instance to 700 milliseconds:

```bash
mongod --setParameter heartBeatFrequencyMs=700
```

**`logicalSessionRefreshMillis`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 300000 (5 minutes)

The interval (in milliseconds) at which the cache refreshes its logical
session records against the main session store.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `logicalSessionRefreshMillis`
for a `mongod` instance to 10 minutes:

```bash
mongod --setParameter logicalSessionRefreshMillis=600000
```

**`localLogicalSessionTimeoutMinutes`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 30

**Warning:** For testing purposes only

This parameter is intended for testing purposes only and not for
production use.

The time in minutes that a session remains active
after its most recent use. Sessions that have not received a new
read/write operation from the client or been refreshed with
`refreshSessions` within this threshold are cleared from the
cache. State associated with an expired session may be cleaned up by the
server at any time.

This parameter applies only to the instance on which it is set. To
set this parameter on replica sets and sharded clusters, you must
specify the same value on every member; otherwise, sessions will
not function properly.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `localLogicalSessionTimeoutMinutes`
for a test `mongod` instance to 20 minutes:

```bash
mongod --setParameter localLogicalSessionTimeoutMinutes=20
```

**`localThresholdMs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 15

Defines the length of the latency window used in
server selection in
milliseconds.

This parameter is only available at startup. If you set this parameter,
it must be greater than or equal to 0.

The following example sets `localThresholdMs`
for a `mongod` instance to 20 milliseconds:

```bash
mongod --setParameter localThresholdMs=20
```

**`maxAcceptableLogicalClockDriftSecs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 31536000 (1 year)

The maximum amount by which the current cluster time can be advanced;
specifically, `maxAcceptableLogicalClockDriftSecs` is the
maximum difference between the new value of the cluster time and the
current cluster time. Cluster time is a logical time used for
ordering of operations.

You cannot advance the cluster time to a new value if the new
cluster time differs from the current cluster time by more than
`maxAcceptableLogicalClockDriftSecs`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `maxAcceptableLogicalClockDriftSecs`
for a `mongod` instance to 15 minutes:

```bash
mongod --setParameter maxAcceptableLogicalClockDriftSecs=900
```

**`maxSessions`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 1000000

The maximum number of sessions that can be cached.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `maxSessions`
for a `mongod` instance to 1000:

```bash
mongod --setParameter maxSessions=1000
```

**`oplogBatchDelayMillis`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 0

The number of milliseconds to delay applying batches of oplog
operations on secondary nodes. By default, `oplogBatchDelayMillis`
is `0`, meaning oplog batches are applied with no delay. When there
is no delay, MongoDB may apply frequent, small oplog batches to
secondaries.

Increasing `oplogBatchDelayMillis` causes MongoDB to apply oplog
batches less frequently on secondaries, with each batch containing
larger amounts of data. This reduces IOPS (Input/Output
Operations Per Second) on secondaries, but adds latency for writes
with write concern `"majority"`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, run the following command to set the
`oplogBatchDelayMillis` for a `mongod` instance to 20
milliseconds:

```bash
mongod --setParameter oplogBatchDelayMillis=20
```

**`periodicNoopIntervalSecs`**

Available for `mongod` only.

*Type*: integer

*Default*: 10

The duration in seconds between noop writes on each individual node.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**Note:**

To modify this value for a MongoDB Atlas cluster, you
must contact Atlas Support.

The following example sets the `periodicNoopIntervalSecs` to 1 second at 
startup:

```javascript
mongod --setParameter periodicNoopIntervalSecs=1
```

**`replicaSetMonitorProtocol`**

Available for both `mongod` and `mongos`.

*Type*: string

*Default*: "streamable"

Determines which replica set monitor protocol to use. You can set this
parameter to `"streamable"`, which is compliant with [Server Discovery and Monitoring (SDAM)](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md) 
specification and allows for constant `hello`
requests. You can also set this parameter to `"sdam"`, which is compliant
with SDAM specification.

This parameter is only available at startup. 

The following example sets
`replicaSetMonitorProtocol` to `"sdam"` on a `mongod`
instance:

```bash
mongod --setParameter replicaSetMonitorProtocol='sdam'
```

**`storeFindAndModifyImagesInSideCollection`**

**New in version:** 5.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: true

Determines whether the temporary documents required for
retryable `findAndModify`
commands are stored in the *side* collection
(`config.image_collection`).

If `storeFindAndModifyImagesInSideCollection` is:

- `true`, the temporary documents are stored in the side
  collection.

- `false`, the temporary documents are stored in the replica
  set oplog.

Keep `storeFindAndModifyImagesInSideCollection` set to
`true` if you:

- Have a large retryable
  `findAndModify` workload.

- Require more temporary document space for retryable `findAndModify` commands than is
  available in the replica set oplog.

**Note:**

Secondaries may experience increased CPU
usage when `storeFindAndModifyImagesInSideCollection`
is `true`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, to set
`storeFindAndModifyImagesInSideCollection` to `false`
during startup:

```bash
mongod --setParameter storeFindAndModifyImagesInSideCollection=false
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, storeFindAndModifyImagesInSideCollection: false } )
```

**`TransactionRecordMinimumLifetimeMinutes`**

Available for `mongod` only.

*Type*: integer

*Default*: 30

The minimum lifetime a transaction record exists in the
`transactions` collection before the record becomes
eligible for cleanup.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `TransactionRecordMinimumLifetimeMinutes`
for a `mongod` instance to 20 minutes:

```bash
mongod --setParameter TransactionRecordMinimumLifetimeMinutes=20
```

**See also:**

`localLogicalSessionTimeoutMinutes`

**`enableFlowControl`**

*Type*: boolean

*Default*: true

Enables or disables the mechanism that controls the rate at which the
primary applies its writes with the goal of keeping the secondary members'
`majority committed` lag under a
configurable maximum value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`flowControlTargetLagSeconds`**

*Type*: integer

*Default*: 10

The target maximum `majority committed` lag when running
with flow control. When flow control is enabled, the mechanism
attempts to keep the `majority committed` lag under
the specified seconds. The parameter has no effect if flow control
is disabled.

The specified value must be greater than 0.

In general, the default settings should suffice; however, if
modifying from the default value, decreasing, rather than
increasing, the value may prove to be more useful.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`flowControlWarnThresholdSeconds`**

*Type*: integer

*Default*: 10

The amount of time to wait to log a warning once the flow control
mechanism detects the majority commit point has not moved.

The specified value must be greater than or equal to 0, with 0 to
disable warnings.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`initialSyncTransientErrorRetryPeriodSeconds`**

*Type*: integer

*Default*: 86400

The amount of time in seconds a secondary performing initial sync
attempts to resume the process if interrupted by a transient
network error. The default value is equivalent to 24 hours.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`initialSyncSourceReadPreference`**

Available for `mongod` only.

*Type*: String

The preferred source for performing initial sync. Specify one of the following read
preference modes:

- `primary`
- `primaryPreferred` (Default for voting replica set members)
- `secondary`
- `secondaryPreferred`
- `nearest` (Default for newly added *or* non-voting replica set members)

If the replica set has disabled `chaining`, the default
`initialSyncSourceReadPreference` read preference mode
is `primary`.

You cannot specify a tag set or `maxStalenessSeconds` to
`initialSyncSourceReadPreference`.

If the `mongod` cannot find a sync source based on the
specified read preference, it logs an error and restarts the initial
sync process. The `mongod` exits with an error if it
cannot complete the initial sync process after `10` attempts. For
more information on sync source selection, see
replica-set-initial-sync-source-selection.

`initialSyncSourceReadPreference` takes precedence over
the replica set's `settings.chainingAllowed` setting when
selecting an initial sync source. After a replica set member
successfully completes initial sync, it defers to the value of
`chainingAllowed` when selecting a replication sync
source.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`initialSyncMethod`**

**New in version:** 5.2

Available for `mongod` only.                                                            

*Type*: String                                                           

*Default*: `logical`   

Available only in MongoDB Enterprise.

Method used for initial sync.

Set to `logical` to use logical initial sync. Set to `fileCopyBased` to         
use file copy based initial sync.

This parameter only affects the sync method for the member on which
it is specified. Setting this parameter on a single replica set
member does not affect the sync method of any other replica set
members.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`maxNumSyncSourceChangesPerHour`**

**New in version:** 5.0

*Type*: integer

*Default*: 3

Sync sources
are evaluated each time a sync source is updated and each time a
node fetches a batch of oplog entries. If there are more than
`maxNumSyncSourceChangesPerHour` source changes in an hour, the
node temporarily stops re-evaluating that sync source. If this
parameter is set with a high value, the node may make unnecessary
source changes.

This parameter will not prevent a node from starting to sync from
another node if it doesn't have a sync source. The node will
re-evaluate if a sync source becomes invalid. Similarly, if the
primary changes and chaining is disabled, the node will update to
sync from the new primary.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`oplogFetcherUsesExhaust`**

Available for `mongod` only.

*Type*: boolean

*Default*: true

Enables or disables streaming replication. Set the value to `true` to enable
streaming replication.

Set the value to `false` to disable streaming replication. If
disabled, secondaries fetch batches of oplog
entries by issuing a request to their *sync from* source and waiting for a
response. This requires a network roundtrip for each batch of oplog entries.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`oplogInitialFindMaxSeconds`**

*Type*: integer

*Default*: 60

Available for `mongod` only.

Maximum time in seconds for a member of a replica set to wait
for the `find` command to finish during
data synchronization.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`replWriterThreadCount`**

*Type*: integer

*Default*: 16

Available for `mongod` only.

Maximum number of threads to use to apply replicated operations in
parallel. Values can range from 1 to 256 inclusive. However, the
maximum number of threads used is capped at twice the number of
available cores.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

`replWriterMinThreadCount`

**`replWriterMinThreadCount`**

**New in version:** 5.0

*Type*: integer

*Default*: 0

Available for `mongod` only.

Minimum number of threads to use to apply replicated operations in
parallel. Values can range from 0 to 256 inclusive. You can only set
`replWriterMinThreadCount` at startup and cannot change
this setting with the `setParameter` command.

Parallel application of replication operations uses up to
`replWriterThreadCount` threads. If
`replWriterMinThreadCount` is configured with a value
less than `replWriterThreadCount`, the thread pool will
timeout idle threads until the total count of threads in the thread
pool is equal to `replWriterMinThreadCount`.

`replWriterMinThreadCount` must be configured with a value
that is less than or equal to `replWriterThreadCount`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`rollbackTimeLimitSecs`**

*Type*: 64-bit integer

*Default*: 86400  (1 day)

Maximum age of data that can be rolled back. Negative values for
this parameter are not valid.

If the time between the end
of the to-be-rolledback instance's oplog and the first operation
after the common point (the last point where the source node and the
to-be-rolledback node had the same data) exceeds this value, the
rollback will fail.

To effectively have an unlimited rollback period, set the value to
`2147483647` which is the maximum value allowed and equivalent to
roughly 68 years.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`waitForSecondaryBeforeNoopWriteMS`**

Available for `mongod` only.

*Type*: integer

*Default*: 10

The length of time (in milliseconds) that a secondary must wait if
the `afterClusterTime` is greater than the last applied time from
the oplog. After the `waitForSecondaryBeforeNoopWriteMS` passes,
if the `afterClusterTime` is still greater than the last applied
time, the secondary makes a no-op write to advance the last applied
time.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets the
`waitForSecondaryBeforeNoopWriteMS` to 20 milliseconds:

```bash
mongod --setParameter waitForSecondaryBeforeNoopWriteMS=20
```

During runtime, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, waitForSecondaryBeforeNoopWriteMS: 20 } )
```

**`createRollbackDataFiles`**

Available for `mongod` only.

*Type*: boolean

*Default*: true

Flag that determines whether MongoDB creates rollback files that contains documents affected during a
rollback.

By default, `createRollbackDataFiles` is `true` and
MongoDB creates the rollback files.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets `createRollbackDataFiles`
to false so that the rollback files are not created:

```javascript
mongod --setParameter createRollbackDataFiles=false
```

During runtime, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, createRollbackDataFiles: false } )
```

For more information, see rollback-data-files.

**`replBatchLimitBytes`**

*Default*: 104857600 (100MB)

Sets the maximum oplog application batch size in bytes.

Values can range from 16777216 (16MB) to 104857600 (100MB) inclusive.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

The following example sets `replBatchLimitBytes`
to 64 MB to limit the oplog application batch size:

```javascript
mongod --setParameter replBatchLimitBytes=67108864
```

During runtime, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, replBatchLimitBytes: 64 * 1024 * 1024 } )
```

**`mirrorReads`**

Available for `mongod` only.

**New in version:** 4.4

*Type*: Document

*Default*: `{ samplingRate: 0.01, maxTimeMS: 1000 }`

Specifies the settings for mirrored reads
for the `mongod` instance. The settings only take
effect when the member is a primary.

The parameter `mirrorReads` takes a JSON document with
the following fields:

* - Field
  - Description

* - `samplingRate`

  - The sampling rate used to mirror a subset of operations
    that support mirroring
    to a subset of electable (specifically,  `priority
    greater than 0`) secondaries. That is,
    the primary mirrors reads to each electable secondary at the
    specified sampling rate.

    Valid values are:

    |  |  |
    |---|---|
    | `0.0` | Turns off mirroring. |
    | `1.0` | The primary mirrors all operations that supports mirroring to each electable secondary. |
    | Number between `0.0` and `1.0` (exclusive) | The primary randomly samples each electable secondary at the specified rate to be sent mirrored reads. |

    For example, given a replica set with a primary and two
    electable secondaries and a sampling rate of `0.10`, the
    primary mirrors reads to each electable secondary at the
    sampling rate of 10 percent such that one read may be
    mirrored to one secondary and not to the other or to both or
    to neither. That is, if the primary receives `100`
    operations that can be mirrored, the sampling rate of
    `0.10` may result in `8` reads being mirrored to one
    secondary and `13` reads to the other or `10` to each,
    etc.

    The default value is `0.01`.

* - `maxTimeMS`

  - The maximum time in milliseconds for the mirrored reads. The
    default value is `1000`.

    The `maxTimeMS` for the mirrored reads is separate from the
    `maxTimeMS` of the original read being mirrored.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

If you specify from the configuration file or on the command
line, **enclose the** `mirrorReads` **document in quotes**.

For example, the following sets the mirror reads sampling rate to
`0.10` from the command line:

```bash
mongod --setParameter mirrorReads='{ samplingRate: 0.10 }'
```

Or, to specify in a configuration file:

```yaml
setParameter:
   mirrorReads: '{samplingRate: 0.10}'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongod`, do **not** enclose the document in quotes:

```javascript
db.adminCommand( { setParameter: 1, mirrorReads: { samplingRate: 0.10 } } )
```

**`allowMultipleArbiters`**

Available for `mongod` only.

**New in version:** 5.3

*Type*: boolean

*Default*: false

Specifies whether the replica set allows the use of multiple arbiters.

The use of multiple arbiters is not recommended:

- Multiple arbiters prevent the reliable use of the majority write concern.
  MongoDB counts arbiters in calculating a membership majority, but arbiters
  do not store data. With the inclusion of multiple arbiters, it's possible
  for a majority write operation to return success before the write replicates
  to a majority of data bearing nodes.

- Multiple arbiters allow replica sets to accept writes even when the
  replica set doesn't have sufficient secondaries for data replication.

For more information, see
Concerns with Multiple Arbiters.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter allowMultipleArbiters=true
```
