<!-- Part 3 of 3 of release-notes/7.0.md (split because the page is big). -->

## Changes Introduced in MongoDB 6.1

### $addFields and $set Allow Empty Objects as Expressions

Starting in MongoDB 6.1, the aggregation stages `$addFields` and 
`$set` allow you to set paths to empty objects without using the 
`$literal` expression.

### Auditing

MongoDB 6.1 adds the following cluster audit events:

- getClusterParameter
- setClusterParameter
- updateCachedClusterServerParameter

Starting in MongoDB 6.1, the startup 
audit event has this structure:

```none
{ 
    originalClusterServerParameter: <original parameter value>,
    updatedClusterServerParameter": <new parameter value> 
}
```

For additional details, see audit-action-details-results. 

### Balancing Policy Changes

Starting in MongoDB 6.1, data in sharded clusters is distributed based on data 
size rather than number of chunks. As a result, note the following
significant changes in sharded cluster data distribution behavior:

- The balancer distributes ranges of data rather than chunks. The balancing 
  policy looks for evenness of data distribution rather than chunk distribution.

- Chunks are not subject to auto-splitting. Instead, chunks are split only when
  moved across shards. 

- A chunk is now referred to as a range. 

- `moveRange` has replaced `moveChunk`. 

### Changes to Journaling

Starting in MongoDB 6.1, journaling is always enabled. As a result, MongoDB 
removes the `storage.journal.enabled` option and the corresponding 
`--journal` and `--nojournal` command-line options.

### `currentOp` Metrics

Starting in MongoDB 6.1, the `currentOp` command and the
`db.currentOp()` method have expanded output for resharding.

Resharding operations can involve multiple MongoDB instances, and
MongoDB instances can play different roles in the resharding operation.
The particular operation and the role the host instance plays in the 
resharding process determine when each
metric updates. 

* - Metric
  - Role Tracked
  - Description

* - `opStatus`
  -  
  -  Removed.

* - `desc` 
  - All
  - Describes the action taken. The value is one of:

    - ReshardingDonorService<operationUUID>
    - ReshardingRecipientService<operationUUID>
    - ReshardingCoordinatorService<operationUUID>

    For `$currentOp`, the command UUID is added to each role's
    state document.

* - `op`
  - All
  - This metric has a constant value: "command".

* - `ns`
  - All
  - The namespace for the resharded index. The value is a string in
    the form: `<database>.<collection>`.

* - `originatingCommand`
  - All
  - A document that lists the command options for the operation.

* - `donorState`
  - Donor
  - The current state of the role's state machine.

* - `coordinatorState`
  - Coordinator
  - The current state of the role's state machine.

* - `recipientState`
  - Recipient
  - The current state of the role's state machine.

* - approxDocumentsToCopy
  - Recipient
  - The number of documents in the source collection.

* - documentsCopied
  - Recipient
  - The number of documents already copied.

* - approxBytesToCopy
  - Recipient
  - The total size, in bytes, of the documents in the source
    collection.

* - bytesCopied
  - Recipient
  - The number of bytes copied. When resharding completes, this value
    is similar to the value of `approxBytesToCopy`. 

* - oplogEntriesFetched
  - Recipient
  - The number of oplog entries written to the oplog buffer
    collection.

* - oplogEntriesApplied
  - Recipient
  - The number of oplog entries applied from the oplog buffer
    collection.

* - insertsApplied
  - Recipient
  - The number of inserts applied to the temporary resharding
    collection. Each oplog entry that involves an insert increments
    the counter by 1.

* - updatesApplied
  - Recipient
  - The number of updates applied to the temporary resharding
    collection. Each oplog entry that involves an update increments
    the counter by 1.

* - deletesApplied
  - Recipient
  - The number of deletes applied to the temporary resharding
    collection. Each oplog entry that involves a delete increments the
    counter by 1.

* - totalOperationTimeElapsedSecs
  - All
  - The number of seconds since the operation began.

* - totalCopyTimeElapsedSecs
  - Recipient
  - The number of seconds spent cloning.

* - totalCopyTimeElapsedSecs
  - Coordinator
  - The maximum number of seconds a Recipient could have spent
    cloning.

* - totalApplyTimeElapsedSecs
  - Recipient
  - The number of seconds spent applying changes.

* - totalApplyTimeElapsedSecs
  - Coordinator
  - The approximate maximum number of seconds a Recipient could have
    spent applying changes.

* - totalCriticalSectionTimeElapsedSecs
  - Recipient
  - The number of seconds spent in the critical section.

* - totalCriticalSectionTimeElapsedSecs
  - Coordinator
  - The number of seconds the critical section could have been held.

* - remainingOperationTimeEstimatedSecs
  - Recipient
  - The estimated number of seconds until the operation completes.

* - allShardsLowestRemainingOperationTimeEstimatedSecs
  - Coordinator
  - Calculated across all shards, the lowest estimate of the number of
    seconds remaining. 

* - allShardsHighestRemainingOperationTimeEstimatedSecs
  - Coordinator
  - Calculated across all shards, the highest estimate of the number
    of seconds remaining.

* - countWritesToStashCollections
  - Recipient
  - The number of writes to the recipient stash collections.

* - countWritesDuringCriticalSection
  - Donor
  - The number of writes attempted during the donor's critical
    section. 

* - countReadsDuringCriticalSection
  - Donor
  - The number of reads attempted during the donor's critical section.

### Improved Efficiency for Multiple Document Deletions

Starting in MongoDB 6.1:

- To improve efficiency, MongoDB may batch multiple document deletions
  together.
- The `explain` command results
  contain a new `BATCHED_DELETE` stage for batched document deletions.

### PCRE Library Upgrade

Perl Compatible Regular Expressions (PCRE (Perl Compatible Regular Expressions)) is the library used by MongoDB to implement
regular expression pattern matching. Starting in version 6.1, MongoDB
upgrades the PCRE (Perl Compatible Regular Expressions) library to PCRE2. PCRE2 is the current
PCRE (Perl Compatible Regular Expressions) library and is actively maintained and updated.

To learn how to perform regex matches in MongoDB, see the following
pages:

- `$regex` (query operator)
- `$regexFind` (aggregation operator)
- `$regexFindAll` (aggregation operator)
- `$regexMatch` (aggregation operator)

### Retryable Writes Error Handling

Starting in MongoDB 6.1, if both the first and second attempt of a
retryable write fail without a single write being performed, MongoDB
returns an error with the `NoWritesPerformed` label.

The `NoWritesPerformed` label differentiates the results of batch
operations like `insertMany()`. In an
`insertMany` operation, one of the following outcomes can occur:

| Outcome | MongoDB Output |
|---|---|
| No documents are inserted. | Error returned with `NoWritesPerformed` label. |
| Partial work done. (At least one document is inserted, but not all.) | Error returned without `NoWritesPerformed` label. |
| All documents are inserted. | Success returned. |

Applications can use the `NoWritesPerformed` label to definitively
determine that no documents were inserted. This error reporting lets the
application maintain an accurate state of the database when handling
retryable writes.

In previous versions of MongoDB, an error is returned when both the
first and second attempts of a retryable write fail. However, there is
no distinction made to indicate that no writes were performed.

### Resharding

Starting in MongoDB 6.1, there are new metrics available 
resharding. The output of the following
commands has changed:

- `currentOp`
- `db.currentOp()`
- `serverStatus`
- `db.serverStatus()`

### Server Parameters

Starting in MongoDB 6.1, MongoDB adds the following new parameters:

- `temporarilyUnavailableBackoffBaseMs` adjusts the time
  between retries after a write failure. 
- `temporarilyUnavailableMaxRetries` limits the number of
  retries after a write failure.
- `ldapRetryCount` sets the number of operation retries by
  the server LDAP manager after a network error.

### `serverStatus` Metrics

Starting in MongoDB 6.1, the `serverStatus` command and the
`db.serverStatus()` method have these output changes:

#### New Metrics

- `countWritesToStashCollections`
  The number of writes to the recipient stash collection.
- `latencies` Timing
  metrics for resharding operations. 

  - `collectionCloningTotalRemoteBatchRetrievalTimeMillis`
    Total time recipients spent retrieving batches of documents from
    donors, in milliseconds.
  - `collectionCloningTotalRemoteBatchesRetrieved`
    Total number of batches of documents recipients retrieved from
    donors.
  - `collectionCloningTotalLocalInsertTimeMillis`
    Total time recipients spent inserting batches of document from
    donors, in milliseconds.
  - `collectionCloningTotalLocalInserts`
    Total number of batches of documents from donors that recipients
    inserted.
  - `oplogFetchingTotalRemoteBatchRetrievalTimeMillis`
    Total time recipients spent retrieving batches of oplog entries
    from donors, in milliseconds.
  - `oplogFetchingTotalRemoteBatchesRetrieved`
    Total number of batches of oplog entries recipients retrieved from
    donors.
  - `oplogFetchingTotalLocalInsertTimeMillis`
    Total time recipients spent inserting batches of oplog entries
    from donors, in milliseconds.
  - `oplogFetchingTotalLocalInserts`
    Total number of batches of oplog entries from donors that
    recipients inserted.
  - `oplogApplyingTotalLocalBatchRetrievalTimeMillis`
    Total time recipients spent retrieving batches of oplog entries
    that were inserted during fetching, in milliseconds.
  - `oplogApplyingTotalLocalBatchesRetrieved`
    Total number of batches of oplog entries that were inserted during
    fetching that recipients retrieved.
  - `oplogApplyingTotalLocalBatchApplyTimeMillis`
    Total time recipients spent applying batches of oplog entries, in
    milliseconds.
  - `oplogApplyingTotalLocalBatchesApplied`
    Total number of batches of oplog entries that recipients applied.

#### Replaced Metrics

`resharding.remainingOperationTimeEstimatedMillis` is replaced by:

- `coordinatorAllShardsHighestRemainingOperationTimeEstimatedMillis`
- `coordinatorAllShardsLowestRemainingOperationTimeEstimatedMillis`
- `recipientRemainingOperationTimeEstimatedMillis`

#### Renamed Metrics

- `countReshardingSuccessful` is now `countSucceeded`
- `countReshardingFailures` is now `countFailed`
- `countReshardingOperations` is now `countStarted`
- `countReshardingCanceled` is now `countCanceled`
- `minShardRemainingOperationTimeEstimatedMillis` is now `coordinatorAllShardsLowestRemainingOperationTimeEstimatedMillis`
- `maxShardRemainingOperationTimeEstimatedMillis` is now `coordinatorAllShardsHighestRemainingOperationTimeEstimatedMillis`
- `resharding.opcounters.insert` is now `insertsApplied`
- `resharding.opcounters.update` is now `updatesApplied`
- `resharding.opcounters.delete` is now `deletesApplied`

#### Removed Metrics

- `oplogApplierApplyBatchLatencyMillis`
- `collClonerFillBatchForInsertLatencyMillis`

### Storage Engine

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

### `*UCP` Regex Option to Match Non-ASCII Characters

Starting in MongoDB 6.1, you can use the `*UCP` option for regex
queries. The `*UCP` option matches non-ASCII characters (specifically,
the option can match UTF-8 characters). However, the `*UCP` option
results in a slower query than one without the option specified.

For an example that uses the `*UCP` option, see
regex-example-pcre2-ucp.


## Upgrade Procedures

**Important:** Feature Compatibility Version

To upgrade to MongoDB 7.0 from a 6.0 deployment, the 6.0 deployment
must have `featureCompatibilityVersion` set to `6.0`. To check
the version:

```javascript
db.adminCommand( { getParameter: 1, featureCompatibilityVersion: 1 } )
```

To upgrade to MongoDB 7.0, refer to the upgrade instructions specific to
your MongoDB deployment:

- 7.0-upgrade-standalone

- 7.0-upgrade-replica-set

- 7.0-upgrade-sharded-cluster

If you need guidance on upgrading to 7.0, MongoDB professional services
offer major version upgrade support to help ensure a smooth transition
without interruption to your MongoDB application. To learn more, see
MongoDB Consulting.


## Downgrade Considerations

### Only Single-Version Downgrades are Supported

(Include not available offline: includes/downgrade/single-version-support.rst)

### Downgrade Policy Changes

Starting in MongoDB 7.0: 

- Binary downgrades are no longer supported for MongoDB Community Edition. 

- You cannot downgrade your deployment's FCV (feature compatibility version) to or from a
  rapid release version of MongoDB.

- The `setFeatureCompatibilityVersion` command requires an
  additional parameter, `confirm`, which must be set to `true` to
  upgrade or downgrade FCV (feature compatibility version).

- If you upgrade or downgrade your deployment's FCV (feature compatibility version), you cannot
  downgrade your Enterprise deployment's binary version without assistance from
  support.

### Backward-Incompatible Features

MongoDB 7.0 includes features that are not compatible with earlier releases.
Downgrading from 7.0 to an earlier release requires that you remove data 
that uses these features.

For more information, see 7.0-downgrade-incompatible.


## Download

To download MongoDB 7.0, go to the [MongoDB Download Center](https://www.mongodb.com/try/download).


## Report an Issue

To report an issue, see the [MongoDB GitHub repository](https://github.com/mongodb/mongo/wiki/Submit-Bug-Reports) for
instructions on how to file a JIRA ticket for the MongoDB server or one
of the related projects.
