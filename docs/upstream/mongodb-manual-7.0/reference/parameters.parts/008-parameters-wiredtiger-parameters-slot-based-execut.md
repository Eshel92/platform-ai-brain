<!-- Part 8 of 8 of reference/parameters.md (split because the page is big). -->

### WiredTiger Parameters

**`wiredTigerConcurrentReadTransactions`**

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

**Changed in version:** 6.0

The `wiredTigerConcurrentReadTransactions` parameter was renamed to 
`storageEngineConcurrentReadTransactions`.

**`wiredTigerConcurrentWriteTransactions`**

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

**Changed in version:** 6.0

The `wiredTigerConcurrentWriteTransactions` parameter was renamed to 
`storageEngineConcurrentWriteTransactions`.

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

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

Enables the auditing of authorization
successes for the authCheck
action.

When `auditAuthorizationSuccess` is `false`, the
audit system only logs the authorization
failures for `authCheck`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

Available for both `mongod` and `mongos`.

*Type*: string

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

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

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

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


### Transaction Parameters

**`AbortExpiredTransactionsSessionCheckoutTimeout`**

**New in version:** 7.0.26

Available for `mongod` only.

*Type*: integer

*Default*: 100 milliseconds

A session is checked out from a session pool to run database operations.

`AbortExpiredTransactionsSessionCheckoutTimeout` sets the
maximum number of milliseconds for a session to be checked out when
attempting to end an expired transaction.

If the expired transaction is successfully ended, MongoDB increments
`metrics.abortExpiredTransactions.successfulKills`. If the
transaction isn't successfully ended because it timed out when
attempting to check out a session, MongoDB increments
`metrics.abortExpiredTransactions.timedOutKills`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`AbortExpiredTransactionsSessionCheckoutTimeout` to `120`
milliseconds:

```javascript
db.adminCommand( { setParameter: 1, AbortExpiredTransactionsSessionCheckoutTimeout: 120 } )
```

You can also set this parameter during startup. For example:

```bash
mongod --setParameter AbortExpiredTransactionsSessionCheckoutTimeout=120
```

**`coordinateCommitReturnImmediatelyAfterPersistingDecision`**

**New in version:** 5.0

*Updated in version 6.1*

Available for `mongod` only.

*Type*: boolean

*Default*: false

- When set to `false`, the shard
  transaction coordinator waits for all participating shards
  to acknowledge the decision to either commit or cancel a
  multi-document transaction
  before returning the result to the client.

- When set to `true`, the shard transaction coordinator
  returns a multi-document transaction commit decision to the client as
  soon as the decision is made durable with the
  requested transaction write concern.

  If the client requested a write concern that is less than
  `"majority"`, the commit may roll back after the
  decision is returned to the client.

  Transactions may not have "read your writes" consistency.
  That is, a read operation may not show the results of write
  operations that preceded it. This can happen if: 

  - A transaction has to write to multiple shards.
  - The read and the earlier write take place in different sessions.

  Causal consistency only guarantees the
  causal relationship of reads and writes that occur within the same
  session.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`coordinateCommitReturnImmediatelyAfterPersistingDecision` to
`true`:

```javascript
mongod --setParameter coordinateCommitReturnImmediatelyAfterPersistingDecision=true
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, coordinateCommitReturnImmediatelyAfterPersistingDecision: true } )
```

**`internalSessionsReapThreshold`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

*Default*: 1000

Session limit for internal session metadata deletion. The metadata:

- Contains session transaction information for user operations.
- Is stored in the `config.transactions` collection.

When the number of internal sessions is greater than
`internalSessionsReapThreshold`, the metadata is deleted.

If you set `internalSessionsReapThreshold` to `0`, the
internal session metadata is only deleted when the user session ends.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `internalSessionsReapThreshold`
to `500` sessions:

```javascript
db.adminCommand( { setParameter: 1, internalSessionsReapThreshold: 500 } )
```

You can also set `internalSessionsReapThreshold` at
startup. For example:

```bash
mongod --setParameter internalSessionsReapThreshold=500
```

**`maxConcurrentMultiDocumentTransactions`**

**New in version:** 7.0.46

Available for `mongod` only.

*Type*: integer

*Default*: 10000

The maximum number of concurrently open multi-document
transactions that the server allows for
external clients at one time. When this limit is reached, the
server rejects new multi-document transactions from external
clients and returns a `TooManyOpenTransactions` error.

The count of open transactions is server-wide. Process-internal
transactions are exempt from rejection, but still contribute to the
total count when the server enforces the limit for external
clients.

Limiting the number of concurrent multi-document transactions can
help prevent high numbers of idle transactions from degrading
system performance.

Set this parameter to `0` to disable the limit. The minimum value
is `0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`maxConcurrentMultiDocumentTransactions` to `5000` at runtime:

```javascript
db.adminCommand( { setParameter: 1, maxConcurrentMultiDocumentTransactions: 5000 } )
```

You can also set this parameter at startup. For example:

```bash
mongod --setParameter maxConcurrentMultiDocumentTransactions=5000
```

**`transactionLifetimeLimitSeconds`**

Available for `mongod` only.

*Default*: 60

Specifies the lifetime of multi-document transactions. Transactions that exceed this limit are
considered expired and will be aborted by a periodic cleanup
process. The cleanup process runs every
`transactionLifetimeLimitSeconds`/2 seconds or at least
once every 60 seconds.

The cleanup process helps relieve storage cache pressure.

The minimum value for transactionLifetimeLimitSeconds is `1`
second.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the
`transactionLifetimeLimitSeconds` to `30`
seconds:

```javascript
db.adminCommand( { setParameter: 1, transactionLifetimeLimitSeconds: 30 } )
```

You can also set parameter `transactionLifetimeLimitSeconds` at
startup time.

```bash
mongod --setParameter "transactionLifetimeLimitSeconds=30"
```

To set the parameter for a sharded cluster, the parameter must be
modified for all shard replica set members.

Starting in MongoDB 5.0, if you change the
`transactionLifetimeLimitSeconds` parameter, you must also
change `transactionLifetimeLimitSeconds` to the same value on
all config server replica set members. Keeping this value consistent:

- Ensures the routing table history is retained for at least as long as
  the transaction lifetime limit on the shard replica set members.

- Reduces the transaction retry frequency and therefore improves
  performance.

**`transactionTooLargeForCacheThreshold`**

**New in version:** 6.2

Available for `mongod` only.

*Type*: decimal

*Default*: 0.75

The threshold value for retrying transactions that fail due to cache
pressure. The value is a percentage of the dirty cache size. The
default value, `0.75`, means 75% of the dirty cache.

The dirty cache is limited to 20% of the total cache size. When
`transactionTooLargeForCacheThreshold` is set to `0.75`, the
server only retries transactions that use less than 15%
(`0.75 * 20%`) of the total storage engine cache.

The limit only applies to retries. Large transactions can use more
than `transactionTooLargeForCacheThreshold` percent of the dirty
cache. However, if a large transaction is rolled back due to cache
pressure, the server issues a
transactionTooLargeForCache-error error and does not retry the
transaction. 

To disable this behavior, set
`transactionTooLargeForCacheThreshold` to `1.0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Contact support if you experience any cache pressure 
issues. 

For more information on WiredTiger storage, see:
wiredTiger-storage-options.

**`maxTransactionLockRequestTimeoutMillis`**

Available for `mongod` only.

*Type*: integer

*Default*: 5

The maximum amount of time in milliseconds that multi-document
transactions should wait to acquire locks
required by the operations in the transaction.

If the transaction cannot acquire the locks after waiting
`maxTransactionLockRequestTimeoutMillis`, the transaction
aborts.

By default, multi-document transactions
wait `5` milliseconds. That is, if the transaction cannot acquire
the locks within `5` milliseconds, the transaction aborts. If an
operation provides a greater timeout in a lock request,
`maxTransactionLockRequestTimeoutMillis` overrides the
operation-specific timeout.

You can set `maxTransactionLockRequestTimeoutMillis` to:

- `0` such that if the transaction cannot acquire the required
  locks immediately, the transaction aborts.

- A number greater than `0` to wait the specified time to acquire
  the required locks. This can help obviate transaction aborts on
  momentary concurrent lock acquisitions, like fast-running metadata
  operations. However, this could possibly delay the abort of
  deadlocked transaction operations.

- `-1` to use the operation specific timeout.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the
`maxTransactionLockRequestTimeoutMillis` to `20`
milliseconds:

```javascript
db.adminCommand( { setParameter: 1, maxTransactionLockRequestTimeoutMillis: 20 } )
```

You can also set this parameter during start-up:

```bash
mongod --setParameter maxTransactionLockRequestTimeoutMillis=20
```


### Slot-Based Execution Parameters

**`planCacheSize`**

**New in version:** 6.3

Available for `mongod` only.

*Type*: string

*Default*: 5%

**Note:**

Although the `planCacheSize` parameter existed in prior versions of 
MongoDB, it had no effect on the plan cache until version 6.3.

Sets the size of the plan cache 
only for the slot-based query execution engine.

You can set the `planCacheSize` value to either:

- A percentage of the system's total physical memory to allocate for
  the plan cache. For example, `"8.5%"`.

- The exact amount of data to allocate for the plan cache in either
  `MB` or `GB`. For example, `"100MB"` or `"1GB"`.

Increasing the plan cache size adds more cached query shapes for the
query planner. This can
improve query performance, but increases memory usage.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following startup command sets `planCacheSize` to 80
megabytes:

```bash
mongod --setParameter planCacheSize="80MB"
```

You can also use the `setParameter` command within the
`MongoDB Shell`:

```javascript
db.adminCommand( { setParameter: 1, planCacheSize: "80MB" } )
```
