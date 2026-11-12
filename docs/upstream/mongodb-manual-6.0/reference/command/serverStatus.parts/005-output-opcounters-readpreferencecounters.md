<!-- Part 5 of 10 of reference/command/serverStatus.md (split because the page is big). -->

### opcounters

The returned opcounters.* values are type NumberLong.

```javascript
opcounters : {
   insert : Long("<num>"), 
   query : Long("<num>"),  
   update : Long("<num>"),  
   delete : Long("<num>"),  
   getmore : Long("<num>"), 
   command : Long("<num>"), 
},
```

**`opcounters`**

A document that reports on database operations by type since the
`mongod` instance last started.

These numbers will grow over time until next restart. Analyze these
values over time to track database utilization.

**Note:**

The data in `opcounters` treats operations
that affect multiple documents, such as bulk insert or
multi-update operations, as a single operation. See
`metrics.document` for more granular
document-level operation tracking.

Additionally, these values reflect received operations, and
increment even when operations are not successful.

**`opcounters.insert`**

The total number of insert operations received since the
`mongod` instance last started.

The returned opcounters.* values are type NumberLong.

**`opcounters.query`**

The total number of queries received since the `mongod`
instance last started.

The returned opcounters.* values are type NumberLong.

**`opcounters.update`**

The total number of update operations received since the
`mongod` instance last started.

The returned opcounters.* values are type NumberLong.

**`opcounters.delete`**

The total number of delete operations since the `mongod`
instance last started.

The returned opcounters.* values are type NumberLong.

**`opcounters.getmore`**

The total number of `getMore` operations since the
`mongod` instance last started. This counter can be high
even if the query count is low. Secondary nodes send
`getMore` operations as part of the replication process.

The returned opcounters.* values are type NumberLong.

**`opcounters.command`**

The total number of commands issued to the database since the
`mongod` instance last started.

`opcounters.command` counts all commands **except** the write commands:
`insert`, `update`, and `delete`.

The returned opcounters.* values are type NumberLong.

**`opcounters.deprecated`**

This section only appears in the `db.serverStatus()` output
when one of the following, deprecated opcodes has been used:

```javascript
deprecated: {
   opQuery: Long("<num>")
}
```

These opcodes were deprecated in MongoDB 5.0 and support for these
opcodes is removed in MongoDB 5.1. Starting in MongoDB 5.1,
`mongod` refuses requests that use a deprecated
opcode and increments the corresponding counter.

`OP_QUERY` is an exception to the general rule.
`mongod` continues to support `hello` and
`isMaster` requests that use `OP_QUERY`. `mongod`
refuses any other `OP_QUERY` requests.

The counters are reset when `mongod` starts.


### opcountersRepl

The returned opcountersRepl.* values are 
type NumberLong. 

```javascript
opcountersRepl : {
   insert : Long("<num>"),  
   query : Long("<num>"),   
   update : Long("<num>"), 
   delete : Long("<num>"), 
   getmore : Long("<num>"), 
   command : Long("<num>"), 
},
```

**`opcountersRepl`**

A document that reports on database replication operations by type
since the `mongod` instance last started.

These values only appear when the current host is a member of a
replica set.

These values will differ from the `opcounters` values
because of how MongoDB serializes operations during replication.
See /replication for more information on replication.

These numbers will grow over time in response to database use until
next restart. Analyze these values over time to track database
utilization.

The returned opcountersRepl.* values are 
type NumberLong. 

**`opcountersRepl.insert`**

The total number of replicated insert operations since the
`mongod` instance last started.

The returned opcountersRepl.* values are 
type NumberLong. 

**`opcountersRepl.query`**

The total number of replicated queries since the `mongod`
instance last started.

The returned opcountersRepl.* values are 
type NumberLong. 

**`opcountersRepl.update`**

The total number of replicated update operations since the
`mongod` instance last started.

The returned opcountersRepl.* values are 
type NumberLong. 

**`opcountersRepl.delete`**

The total number of replicated delete operations since the
`mongod` instance last started.

The returned opcountersRepl.* values are 
type NumberLong. 

**`opcountersRepl.getmore`**

The total number of `getMore` operations since the
`mongod` instance last started. This counter can be high
even if the query count is low. Secondary nodes send
`getMore` operations as part of the replication process.

The returned opcountersRepl.* values are 
type NumberLong. 

**`opcountersRepl.command`**

The total number of replicated commands issued to the database since
the `mongod` instance last started.

The returned opcountersRepl.* values are 
type NumberLong. 


### oplogTruncation

```javascript
oplogTruncation : {
   totalTimeProcessingMicros : Long("<num>"),
   processingMethod : <string>,
   oplogMinRetentionHours : <double>
   totalTimeTruncatingMicros : Long("<num>"),
   truncateCount : Long("<num>")
},
```

**`oplogTruncation`**

A document that reports on oplog
truncations.

The field only appears when the current instance is a member of a
replica set and uses either the /core/wiredtiger or
/core/inmemory.

Available in the /core/wiredtiger.

**`oplogTruncation.totalTimeProcessingMicros`**

The total time taken, in microseconds, to scan or sample the oplog
to determine the oplog truncation points.

`totalTimeProcessingMicros` is only
meaningful if the `mongod` instance started on existing
data files (i.e. not meaningful for /core/inmemory).

See `oplogTruncation.processingMethod`

Available in the /core/wiredtiger.

**`oplogTruncation.processingMethod`**

The method used at start up to determine the oplog truncation points.
The value can be either `"sampling"` or `"scanning"`.

`processingMethod` is only meaningful
if the `mongod` instance started on existing data files
(i.e. not meaningful for /core/inmemory).

Available in the /core/wiredtiger.

**`oplogTruncation.oplogMinRetentionHours`**

The minimum retention period for the oplog in hours. If the oplog
has exceeded the oplog size, the `mongod` only
truncates oplog entries older than the configured retention
value.

Only visible if the `mongod` is a member of a replica
set *and*:

- The `mongod` was started with the
  `--oplogMinRetentionHours` command line option *or* the 
  `storage.oplogMinRetentionHours` configuration file 
  option,

  *or*

- The minimum retention period was configured after startup using
  `replSetResizeOplog`.

**`oplogTruncation.totalTimeTruncatingMicros`**

The cumulative time spent, in microseconds, performing oplog truncations.

Available in the /core/wiredtiger.

**`oplogTruncation.truncateCount`**

The cumulative number of oplog truncations.

Available in the /core/wiredtiger.


### queryStats

**New in version:** 6.0.7

```javascript
queryStats: {
   numEvicted: Long("<num>"),
   numRateLimitedRequests: Long("<num>"),
   queryStatsStoreSizeEstimateBytes: Long("<num>"),
   numQueryStatsStoreWriteErrors: Long("<num>"),
   numHmacApplicationErrors: Long("<num>")
},
```

**`queryStats`**

A document that contains metrics for the `$queryStats`
aggregation stage.

**`queryStats.numEvicted`**

Number of queries that the `$queryStats` virtual collection has
evicted due to space contraints.

**`queryStats.numRateLimitedRequests`**

Number of times that query stats were not recorded for a query due to
rate limiting.

**`queryStats.queryStatsStoreSizeEstimateBytes`**

Current estimated size of objects in the `$queryStats` virtual
collection.

**`queryStats.numQueryStatsStoreWriteErrors`**

Number of times this MongoDB process failed to store a new query
stats key. Generally, these failures happen when the
`$queryStats` virtual collection runs out of space.

**`queryStats.numHmacApplicationErrors`**

Number of times this MongoDB process failed to compute a one-way
tokenized query stats key when `$queryStats` was called with the
`transformIdentifiers` option.


### readConcernCounters

**New in version:** 5.0

```javascript
readConcernCounters : {
   nonTransactionOps : {
      none : Long("<num>"),
      noneInfo : {
         CWRC : {
            local : Long("<num>"),
            available : Long("<num>"),
            majority : Long("<num>")
         },
         implicitDefault : {
            local : Long("<num>"),
            available : Long("<num>")
         }
      },
      local : Long("<num>"),
      available : Long("<num>"),
      majority : Long("<num>"),
      snapshot : {
         withClusterTime : Long("<num>"),
         withoutClusterTime : Long("<num>")
      },
      linearizable : Long("<num>")
   },
   transactionOps : {
      none : Long("<num>"),
      noneInfo : {
         CWRC : {
            local : Long("<num>"),
            available : Long("<num>"),
            majority : Long("<num>")
         },
         implicitDefault : {
            local : Long("<num>"),
            available : Long("<num>")
         }
      },
      local : Long("<num>"),
      majority : Long("<num>"),
      snapshot : {
         withClusterTime : Long("<num>"),
         withoutClusterTime : Long("<num>")
      }
   }
},
```

**`readConcernCounters`**

A document that reports on the read concern level specified by query operations. This document
contains the `readConcernCounters.nonTransactionOps`
and `readConcernCounters.transactionOps` documents.

**`readConcernCounters.nonTransactionOps`**

A document that reports on the read concern level specified by non-transaction query operations
performed after the database server last started.

**`readConcernCounters.nonTransactionOps.none`**

Number of non-transaction query operations that did not specify a
read concern level and instead used either:

- the default read  concern level, or
- the global default read concern configuration if it was set by the
  `setDefaultRWConcern` command.

**`readConcernCounters.nonTransactionOps.noneInfo`**

The number of non-transaction query operations that use the global
default read concern and an implicit-default read concern.

The sum of the values in
`readConcernCounters.nonTransactionOps.noneInfo` should equal the
value of `readConcernCounters.nonTransactionOps.none`.

**`readConcernCounters.nonTransactionOps.local`**

Number of non-transaction query operations that specified the
`"local"` read concern level.

**`readConcernCounters.nonTransactionOps.available`**

Number of non-transaction query operations that specified the
`"available"` read concern level.

**`readConcernCounters.nonTransactionOps.majority`**

Number of non-transaction query operations that specified the
`"majority"` read concern level.

**`readConcernCounters.nonTransactionOps.snapshot`**

Document containing non-transaction query operations that specified
the `"snapshot"` read concern level.

**`readConcernCounters.nonTransactionOps.snapshot.withClusterTime`**

Number of non-transaction query operations that specified the
`"snapshot"` read concern level and the cluster time,
which specified a point in time.

**`readConcernCounters.nonTransactionOps.snapshot.withoutClusterTime`**

Number of non-transaction query operations that specified the
`"snapshot"` read concern level without the cluster
time, which means a point in time was omitted and the server will
read the most recently committed snapshot available to the node.

**`readConcernCounters.nonTransactionOps.linearizable`**

Number of non-transaction query operations that specified the
`"linearizable"` read concern level.

**`readConcernCounters.transactionOps`**

A document that reports on the read concern level specified by transaction query operations
performed after the database server last started.

**`readConcernCounters.transactionOps.none`**

Number of transaction query operations that did not specify a
read concern level and instead used the default read concern
level or the global default read or write
concern configuration added with the `setDefaultRWConcern`
command.

**`readConcernCounters.transactionOps.noneInfo`**

Information about the global default read concern and
implicit-default read concern used by transaction query operations.

**`readConcernCounters.transactionOps.local`**

Number of transaction query operations that specified the
`"local"` read concern level.

**`readConcernCounters.transactionOps.available`**

Number of transaction query operations that specified the
`"available"` read concern level.

**`readConcernCounters.transactionOps.majority`**

Number of transaction query operations that specified the
`"majority"` read concern level.

**`readConcernCounters.transactionOps.snapshot`**

Document containing transaction query operations that specified the
`"snapshot"` read concern level.

**`readConcernCounters.transactionOps.snapshot.withClusterTime`**

Number of transaction query operations that specified the
`"snapshot"` read concern level and the cluster time,
which specified a point in time.

**`readConcernCounters.transactionOps.snapshot.withoutClusterTime`**

Number of transaction query operations that specified the
`"snapshot"` read concern level without the cluster
time, which means a point in time was omitted and the server will
read the most recently committed snapshot available to the node.


### readPreferenceCounters

*Available starting in MongoDB 6.0.11.*

*Available on mongod only.*

```javascript
readPreferenceCounters : {
   executedOnPrimary : { 
      primary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      primaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      secondary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      secondaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      nearest : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      tagged : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }
   },
   executedOnSecondary : { 
      primary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      primaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      secondary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      secondaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      nearest : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      tagged : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }
   }
}
```

**`readPreferenceCounters`**

*Available on mongod only.*

A document that reports the number of operations received by this 
`mongod` node with the specified 
read preference.

The `tagged` sub-field refers to any read preference passed in 
with a tag.

**`readPreferenceCounters.executedOnPrimary`**

*Available on mongod only.*

A document that counts how many internal and external read preference 
operations the node received while serving as the primary.

**`readPreferenceCounters.executedOnSecondary`**

*Available on mongod only.*

A document that counts how many internal and external read preference 
operations the node received while serving as a secondary.
