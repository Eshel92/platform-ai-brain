<!-- Part 8 of 8 of reference/parameters.md (split because the page is big). -->

### Transaction Parameters

**`coordinateCommitReturnImmediatelyAfterPersistingDecision`**

**New in version:** 5.0

*Updated in version 6.0 and in 5.0.10*

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

The shard transaction coordinator returns a multi-document
transaction commit decision to the client
as soon as the decision is made durable with the requested
transaction write concern.

If the client requested a write concern that is less than
`"majority"`, the commit may roll back after the
decision is returned to the client.

Transactions may not have "read your writes" consistency. That is, a
read operation may not reflect the results of a write operation that
preceded it. This can happen in the following cases:

- A transaction has to write to multiple shards.
- The read and the earlier write take place in different sessions.

Causal consistency only guarantees the
causal relationship of reads and writes that occurr within the same
session.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

#### Example

The following example sets
`coordinateCommitReturnImmediatelyAfterPersistingDecision` to
`true`:

```javascript
mongod --setParameter coordinateCommitReturnImmediatelyAfterPersistingDecision=true
```

During runtime, you can also set the parameter with the
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
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

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
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

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

**New in version:** 6.0.5

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
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

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
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

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
