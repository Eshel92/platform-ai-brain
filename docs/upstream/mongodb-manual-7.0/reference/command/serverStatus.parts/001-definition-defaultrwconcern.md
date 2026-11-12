<!-- Part 1 of 11 of reference/command/serverStatus.md (split because the page is big). -->

## Definition

**`serverStatus`**

The `serverStatus` command returns a document that
provides an overview of the database's state. Monitoring
applications can run this command at a regular interval to
collect statistics about the instance.


## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB


## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     serverStatus: 1 
   } 
)
```

The value (that is, `1` above) does not affect the operation of
the command. The `db.serverStatus()` command returns a large amount of
data. To return a specific object or field from the output append the
object or field name to the command.

For example:

```javascript
db.runCommand({ serverStatus: 1}).metrics
db.runCommand({ serverStatus: 1}).metrics.commands
db.runCommand({ serverStatus: 1}).metrics.commands.update
```

`mongosh` provides the `db.serverStatus()`
wrapper for the `serverStatus` command.

**See also:**

Much of the output of `serverStatus` is also displayed
dynamically by `mongostat`. See the
`mongostat` command for more information.


## Behavior

By default, `serverStatus` excludes in its output:

- some content in the server-status-repl document.

- server-status-mirroredReads document.

To include fields that are excluded by default, specify the top-level
field and set it to `1` in the command. To exclude fields that are included 
by default, specify the field and set to 0. You can specify either top-level 
or embedded fields. 

For example, the following operation excludes the `repl`,
`metrics` and `locks` information in the output.

```javascript
db.runCommand( { serverStatus: 1, repl: 0, metrics: 0, locks: 0 } )
```

For example, the following operation excludes the embedded `histogram` 
field in the output.

```javascript
db.runCommand( { serverStatus: 1, metrics: { query: { multiPlanner: { histograms: false } } } } )
```

The following example includes
all server-status-repl information in the output:

```javascript
db.runCommand( { serverStatus: 1,  repl: 1 } )
```

### Exclude All Optional Fields

Starting in MongoDB 7.0.38, you can exclude all optional fields 
from the `serverStatus` output by specifying `none: 1`. 
After you exclude all optional fields, you can then specify
the fields you want to include.

This example uses `none` to initially exclude all optional 
field from the output, then includes the  `locks` document.

```javascript
db.runCommand({ serverStatus: 1, none: 1, locks: 1 })
```

### Initialization

The statistics reported by `serverStatus` are reset when the
`mongod` server is restarted.

This command always returns a value, even on a fresh database. The
related command `db.serverStatus()` does not always return a
value unless a counter has started to increment for a particular
metric.

After you run an update query, `db.serverStatus()` and
`db.runCommand({ serverStatus: 1})` both return the same values.

```javascript
{
   arrayFilters : Long("0"),
   failed : Long("0"),
   pipeline : Long("0"),
   total : Long("1")
}
```

### Include `latchAnalysis`

By default, the `latchAnalysis` information is not included in 
the output. To return `latchAnalysis` information, you must 
explicitly specify the inclusion:

```javascript
db.runCommand( { serverStatus: 1, latchAnalysis: 1 } )
```

### Change `tcmalloc` Verbosity

By default, `tcmalloc` information is included in the output. This
section provides memory allocation statistics for your database. To
change the verbosity of the `tcmalloc` section, specify an integer 
between `0` and `2` (inclusive):

```javascript
db.runCommand( { serverStatus: 1, tcmalloc: <int> } )
```

The command has the following behavior:

- By default, `tcmalloc` is set to `1`.
- Passing a larger integer value increases the verbosity.
- Passing `0` or `false` omits the `tcmalloc` section from the
  output. 
- Passing any other input results in the default setting.

For more information about how MongoDB allocates memory, see TCMalloc.


## Output

**Note:**

The output fields vary depending on the version of MongoDB,
underlying operating system platform, the storage engine, and the
kind of node, including `mongos`, `mongod` or
replica set member.

For the `serverStatus` output specific to the version of
your MongoDB, refer to the appropriate version of the MongoDB Manual.


### asserts

```javascript
asserts : {
   regular : <num>,
   warning : <num>,
   msg : <num>,
   user : <num>,
   rollovers : <num>
},
```

**`asserts`**

A document that reports on the number of assertions raised since the
MongoDB process started. Assertions are internal checks for errors that 
occur while the database is operating and can help diagnose issues with the 
MongoDB server. Non-zero asserts values indicate assertion errors, which are 
uncommon and not an immediate cause for concern. Errors that generate asserts 
can be recorded in the log file or returned directly to a client application 
for more information.

**`asserts.regular`**

The number of regular assertions raised since the MongoDB process
started. Examine the MongoDB log for more information.

**`asserts.warning`**

This field always returns zero `0`.

**`asserts.msg`**

The number of message assertions raised since the MongoDB process
started. Examine the log file for more information about these
messages.

**`asserts.user`**

The number of "user asserts" that have occurred since the last time
the MongoDB process started. These are errors that user may
generate, such as out of disk space or duplicate key. You can
prevent these assertions by fixing a problem with your application
or deployment. Server logs may have limited information about "user asserts."
To learn more information about the source of "user asserts," check the 
application logs for application errors.

**`asserts.rollovers`**

The number of times that the assert counters have rolled over
since the last time the MongoDB process started. The counters will
roll over to zero after 2`30` assertions. Use this
value to provide context to the other values in the
`asserts` data structure.


### batchedDeletes

```javascript
batchedDeletes: {
   batches: <num>,
   docs: <num>,
   stagedSizeBytes: <num>,
   timeInBatchMillis: <num>,
   refetchesDueToYield: <num>
},
```

A document that reports metrics related to all batched deletes.

The `batchedDeletes` returns the following metrics:

| Metric | Description |
|---|---|
| `batches` |  |
| `docs` |  |
| `stagedSizeBytes` |  |
| `timeInBatchMillis` |  |
| `refetchesDueToYield` |  |


### bucketCatalog

```javascript
bucketCatalog : {
    numBuckets : <num>,
    numOpenBuckets : <num>,
    numIdleBuckets : <num>,
    memoryUsage : <num>
 }
```

A document that reports metrics related to the internal storage of
time series collections.

The `bucketCatalog` returns the following metrics:

| Metric | Description |
|---|---|
| `numBuckets` | The number of buckets that store time series data internally. |
| `numOpenBuckets` | The number of active, uncommitted writes to buckets. |
| `numIdleBuckets` | The number of buckets that are not full and can store incoming time series data. |
| `memoryUsage` | The total number of buckets that are being tracked for conflict management. This includes open buckets in the bucket catalog and any buckets that are being directly written to, including by update and delete commands. |
| `stateManagement.currentEra` | The current era of the bucket catalog. The bucket catalog starts at era 0 and increments when a bucket is cleared. Attempting to insert into a bucket either causes it to be removed if it was cleared, or update it to the current era. |
| `stateManagement.erasWithRemainingBuckets` | The number of eras with tracked buckets. |
| `stateManagement.trackedClearOperations` | The number of times the a set of buckets has been cleared, but the removal of those buckets was deferred. This can happen due to events such as dropping a collection, moving a chunk in a sharded collection, or an election. |

You can also use the `$collStats` aggregation pipeline stage to find time series
metrics. To learn more, see storage-stats-time-series. 


### catalogStats

**New in version:** 5.1

```javascript
catalogStats: {
   collections: <num>,
   capped: <num>, 
   views: <num>, 
   timeseries: <num>,
   internalCollections: <num>, 
   internalViews: <num>,
   csfle: <num>,
   queryableEncryption: <num>,
   systemProfile: <num>
}
```

**`catalogStats`**

A document that reports statistics on collection usage via collection counts.

**`catalogStats.collections`**

The total number of user collections (not including system
collections).

**`catalogStats.capped`**

The total number of capped user collections. 

**`catalogStats.views`**

The total number of user views.

**`catalogStats.timeseries`**

The total number of time series collections. 

**`catalogStats.internalCollections`**

The total number of system collections (collections on the
`config`, `admin`, or `local` databases).

**`catalogStats.internalViews`**

The total number of views of system collections (collections on the
`config`, `admin`, or `local` databases).

**`catalogStats.csfle`**

**New in version:** 7.0.1

The total number of collections configured for Client-Side Field Level Encryption
(collections with an encrypted validator).

**`catalogStats.queryableEncryption`**

**New in version:** 7.0.1

The total number of collections configured for Queryable Encryption (collections
with `encryptedFields`).

**`catalogStats.systemProfile`**

The total number of `profile` collections on all databases.


### connections

```javascript
connections : {
   current : <num>,
   available : <num>,
   totalCreated : <num>,
   rejected : <num>,  // Added in MongoDB 6.3
   active : <num>,
   threaded : <num>,
   exhaustIsMaster : <num>,
   exhaustHello : <num>,
   awaitingTopologyChanges : <num>,
   loadBalanced : <num> 
},
```

**`connections`**

A document that reports on the status of the connections. Use these
values to assess the current load and capacity requirements of the
server.

**`connections.current`**

The number of incoming connections from clients to the database
server. This includes connections from the current shell session
and from other servers, such as replica set members and
`mongos` instances. Consider the value of
`connections.available` for additional context.

**`connections.available`**

The number of unused incoming connections available. Consider this
value in combination with the value of
`connections.current` to understand the connection
load on the database, and the ulimit document for
more information about system thresholds on available connections.

**`connections.totalCreated`**

Count of **all** incoming connections created to the server. This
number includes connections that have since closed.

**`connections.rejected`**

**New in version:** 6.3

The number of incoming connections the server rejected because the
server doesn't have the capacity to accept additional connections or
the `net.maxIncomingConnections` setting is reached.

**`connections.active`**

The number of active client connections to the server. Active client
connections refers to client connections that currently have
operations in progress.

**`connections.threaded`**

The number of incoming connections from clients that are assigned
to threads that service client requests.

**New in version:** 5.0

**`connections.exhaustIsMaster`**

The number of connections whose last request was an
`isMaster` request with exhaustAllowed.

**Note:**

If you are running MongoDB 5.0 or later, do not use the
`isMaster` command. Instead, use `hello`.

**`connections.exhaustHello`**

The number of connections whose last request was a `hello`
request with exhaustAllowed.

**New in version:** 5.0

**`connections.awaitingTopologyChanges`**

The number of clients currently waiting in a `hello` or
`isMaster` request for a topology change.

**Note:**

If you are running MongoDB 5.0 or later, do not use the
`isMaster` command. Instead, use `hello`.

**`connections.loadBalanced`**

**New in version:** 5.3

The current number of incoming connections received through the 
load balancer.


### defaultRWConcern

The `defaultRWConcern` section provides information on the local copy
of the global default read or write concern settings. The data may be
stale or out of date. See `getDefaultRWConcern` for more
information.

```javascript
defaultRWConcern : {
  defaultReadConcern : {
    level : <string>
  },
  defaultWriteConcern : {
    w : <string> | <int>,
    wtimeout : <int>,
    j : <bool>
  },
  defaultWriteConcernSource: <string>,
  defaultReadConcernSource: <string>,
  updateOpTime : Timestamp,
  updateWallClockTime : Date,
  localUpdateWallClockTime : Date
}
```

**`defaultRWConcern`**

The last known global default read or write concern settings.

**`defaultRWConcern.defaultReadConcern`**

The last known global default read concern
setting.

If `serverStatus` does not return this field, the global
default read concern has either not been set *or* has not yet
propagated to the instance.

**`defaultRWConcern.defaultReadConcern.level`**

The last known global default read concern level setting.

If `serverStatus` does not return this field, the global
default for this setting has either not been set *or* has not yet
propagated to the instance.

**`defaultRWConcern.defaultWriteConcern`**

The last known global default write concern
setting.

If `serverStatus` does not return this field, the global
default write concern has either not been set *or* has not yet
propagated to the instance. 

**`defaultRWConcern.defaultWriteConcern.w`**

The last known global default w setting. 

If `serverStatus` does not return this field, the global
default for this setting has either not been set *or* has not yet
propagated to the instance.

**`defaultRWConcern.defaultWriteConcern.wtimeout`**

The last known global default wtimeout setting. 

If `serverStatus` does not return this field, the global
default for this setting has either not been set *or* has not yet
propagated to the instance.

**`defaultRWConcern.defaultWriteConcernSource`**

The source of the default write concern. By 
default, the value is `"implicit"`. Once you set the default write
concern with `setDefaultRWConcern`, the value becomes 
`"global"`.

**New in version:** 5.0

**`defaultRWConcern.defaultReadConcernSource`**

The source of the default read concern. By 
default, the value is `"implicit"`. Once you set the default read
concern with `setDefaultRWConcern`, the value becomes
`"global"`.

**New in version:** 5.0

**`defaultRWConcern.updateOpTime`**

The timestamp when the instance last updated its copy of any global
read or write concern settings. If the
`defaultRWConcern.defaultReadConcern` and
`defaultRWConcern.defaultWriteConcern` fields are
absent, this field indicates the timestamp when the defaults were
last unset.

**`defaultRWConcern.updateWallClockTime`**

The wall clock time when the instance last updated its copy of any
global read or write concern settings. If the
`defaultRWConcern.defaultReadConcern` and
`defaultRWConcern.defaultWriteConcern` fields are
absent, this field indicates the time when the defaults were last
unset.

**`defaultRWConcern.localUpdateWallClockTime`**

The local system wall clock time when the instance last updated its
copy of any global read or write concern setting. If this field is
the *only* field under `defaultRWConcern`, the instance
has never had knowledge of a global default read or write concern
setting.
