<!-- Converted from tutorial/manage-the-database-profiler.txt (reStructuredText). Includes are inlined. -->

# Database Profiler

**Warning:**

The database profiler can degrade MongoDB performance. Before enabling 
the database profiler, consider using one of the following alternatives:

- Atlas Query Profiler
- Atlas Performance Advisor
- `$queryStats` (aggregation stage)

To learn more about the performance impact of the database profiler, see 
database-profiling-overhead.

The database profiler collects detailed information about
database-commands executed against a running `mongod`
instance. This includes CRUD operations as well as configuration and
administration commands.

The profiler writes all the data it collects to a
`system.profile <` collection, a
capped collection in each profiled
database. See /reference/database-profiler for an overview of the
`system.profile <` documents created by
the profiler.

The profiler is `off` by default. You can enable the profiler on a
per-database or per-instance basis at one of several profiling
levels.

When enabled, profiling has an effect on database performance and
disk use. See Database Profiler Overhead for more information.

This page shows important administration options for the
database profiler. For additional information, see:

- profiler
- Profile Command
- `db.currentOp()`

## Profiling Levels

The following profiling levels are available:

`0`
   The profiler is off and does not collect any data.
   This is the default profiler level.

`1`
   The profiler collects data for operations that take longer
   than the value of `slowms` or that match a filter. 

   When a filter is set:

   - The `slowms` and `sampleRate` options are not used for
     profiling.
   - The profiler only captures operations that match the
     filter.

`2`
   The profiler collects data for all operations.
   When set to level `2`, the profiler ignores user 
   provided values for `slowms` and `filter`.

## Enable and Configure Database Profiling

You can enable database profiling for `mongod` instances.

To enable profiling, use one of the following methods:

- To enable profiling at startup, set `operationProfiling.mode` 
  in your configuration file.
- To enable profiling during runtime, use the `mongosh` 
  helper method `db.setProfilingLevel()`.
- To enable profiling with a driver, use a `driver method`.

The profiler records data in the `system.profile
<` collection. MongoDB creates the
`system.profile <` collection in a
database after you enable profiling for that database.

To enable profiling for a `mongod` instance at
startup, set `operationProfiling.mode` in your
configuration file to your 
preferred logging level.

To enable profiling and set the profiling level, pass the profiling
level to the `db.setProfilingLevel()` helper. For example, to
enable profiling for all database operations for the currently connected
database, run this operation in `mongosh`:

```javascript
db.setProfilingLevel(2)
```

The shell returns the *previous* profiling level in the `was` field
and sets the new level. In the following output, the ``"ok" :
1`` key-value pair indicates the operation succeeded:

```javascript
{ "was" : 0, "slowms" : 100, "sampleRate" : 1.0, "ok" : 1 }
```

To verify the new setting, see the
database-profiling-view-status section.

Starting in MongoDB 5.0, changes made to the database profiler `level`, `slowms`, `sampleRate`, or
`filter` using the `profile` command or
`db.setProfilingLevel()` wrapper method are recorded in the
`log file`.

### Global and Per-Database Profiling Settings

The slowms and
sampleRate profiling
settings are *global*. When set, these settings affect all databases in
your process.

When set through the `profile` command or
`db.setProfilingLevel()` shell helper method, profiling
level and filter settings are set at the *database*
level. When set as either command line or configuration
file options, profiling level and `filter`
settings affect the entire process.

### Specify the Threshold for Slow Operations

By default, the slow operation threshold is 100 milliseconds. To change
the slow operation threshold, specify the required threshold value in
one of the following ways:

- Set the value of `slowms` using the `profile` command or
  `db.setProfilingLevel()` shell helper method.

- Set the value of `--slowms` from the command line at startup.

- Set the value of `slowOpThresholdMs` in a
  configuration file.

The following example sets the profiling level for the
currently connected database to `1` and sets the slow
operation threshold for the `mongod` instance to `20`
milliseconds:

```javascript
db.setProfilingLevel( 1, { slowms: 20 } )
```

A profiling level of `1` causes the profiler to record operations
slower than the `slowms` threshold.

**Important:**

The slow operation threshold applies to all databases in a
`mongod` instance. It is used by both the database profiler
and the diagnostic log and should be set to the highest useful value to
avoid performance degradation.

You can use `db.setProfilingLevel()`
to configure `slowms` and `sampleRate` for `mongos`.
For the `mongos`, the `slowms` and `sampleRate`
configuration settings only affect the diagnostic log and not the
profiler since profiling is not available on `mongos`.
[#mongos-systemlog]_

The following example sets a `mongos` instance's slow
operation threshold for logging slow operations to `20`:

```javascript
db.setProfilingLevel( 0, { slowms: 20 } )
```

The profiler entries and the 
diagnostic log messages (i.e. mongod/mongos logmessages) for read/write operations include:

- `queryHash` to help identify slow queries with the same
  query shape. 

- `planCacheKey` to provide more insight into the query plan
  cache for slow queries.

Secondary members of a replica set now log oplog entries that take longer than the slow operation
threshold to apply. These slow oplog messages:

- Are logged for the secondaries in the
  `diagnostic log`.

- Are logged under the `REPL` component with the text
  `applied op: <oplog entry> took <num>ms`.

- Do not depend on the log levels (either at the system or component
  level)

- Do not depend on the profiling level.

- Are affected by `slowOpSampleRate`.

The profiler does not capture slow oplog entries.

   

### Profile a Random Sample of Slow Operations

To profile only a randomly sampled subset of all *slow* operations,
specify the desired sample rate in one of the following ways:
[#slow-oplogs]_

- Set the value of `sampleRate` using the `profile` command
  or `db.setProfilingLevel()` shell helper method.

- Set the value of `--slowOpSampleRate` 
  for `mongod` or `--slowOpSampleRate`
  for `mongos` from the command line at startup.

- Set the value of `slowOpSampleRate` in a
  configuration file.

By default, `sampleRate` is set to `1.0`, meaning all *slow*
operations are profiled. When `sampleRate` is set between `0` and `1`,
databases with a profiling level `1` only profile a randomly sampled
percentage of *slow* operations based on `sampleRate`.

The following example sets the profiling level for the currently
connected database to `1` and sets the profiler to sample 42% of all
*slow* operations:

```javascript
db.setProfilingLevel( 1, { sampleRate: 0.42 } )
```

The modified sample rate value also applies to the system log.

You can use `db.setProfilingLevel()`
to configure `slowms` and `sampleRate` for `mongos`.
For the `mongos`,  the `slowms` and
`sampleRate` configuration settings only affect the diagnostic log
and not the profiler because profiling isn't available on
`mongos`. [#mongos-systemlog]_

For example, the following sets a `mongos` instance's
sampling rate for logging slow operations:

```javascript
db.setProfilingLevel( 0, { sampleRate: 0.42 } )
```

**Important:**

When `logLevel` is set to `0`, MongoDB records *slow*
operations to the diagnostic log at a rate determined by
`slowOpSampleRate`.

At higher `logLevel` settings, all operations appear in
the diagnostic log regardless of their latency with the following
exception: the logging of slow oplog entry messages by the
secondaries. The secondaries log only the slow oplog
entries; increasing the `logLevel` does not log all
oplog entries.

### Set a Filter to Determine Profiled Operations

You can set a filter to control which operations are profiled and
logged. You can set the profiling filter in one of the following ways:

- Set the value of `filter` using the `profile` command
  or the `db.setProfilingLevel()` shell helper method.

- Set the value of `filter` in a
  configuration file.

For `mongod` instances, the `filter` affects both the
diagnostic log and, if enabled, the profiler.

For `mongos` instances, the `filter` affects the
diagnostic log only and not the profiler since profiling is not
available on `mongos`.

**Note:**

When a profiling `filter` is set, the slowms and sampleRate options do not affect the
diagnostic log or the profiler.

The following `db.setProfilingLevel()` example sets
the profile level for the currently connected database:

- the profiling level to `1`,

- the filter of
  `{ op: "query", millis: { $gt: 2000 } }`, which causes the profiler
  to only log `query` operations that took longer than 2 seconds.

```javascript
db.setProfilingLevel( 1, { filter: { op: "query", millis: { $gt: 2000 } } } )
```

### Check Profiling Level

To view the profiling level, run
the following example in `mongosh`:

```javascript
db.getProfilingStatus()
```

The shell returns a document similar to the following:

```javascript
{ "was" : 0, "slowms" : 100, "sampleRate" : 1.0, "ok" : 1 }
```

The `was` field indicates the current profiling level.

The `slowms` field indicates operation time threshold, in
milliseconds, beyond which operations are considered *slow*.

The `sampleRate` field indicates the percentage of *slow* operations
that should be profiled.

### Disable Profiling

To disable profiling, run the following example in
`mongosh`:

```javascript
db.setProfilingLevel(0)
```

**Note:**

Disabling profiling can improve database performance and lower disk
use. For more information, see Database Profiler
Overhead  .

### Enable Profiling for an Entire `mongod` Instance

For development and test environments, you can enable
database profiling for an entire `mongod` instance. The
profiling level applies to all databases provided by the
`mongod` instance.

To enable profiling for a `mongod` instance, pass the following
options to `mongod` at startup.

```bash
mongod --profile 1 --slowms 15 --slowOpSampleRate 0.5
```

Alternatively, you can specify operationProfiling in the configuration
file.

This sets the profiling level to `1`, defines slow operations as those
that last longer than `15` milliseconds, and specifies that only 50%
of *slow* operations should be profiled. [#slow-oplogs]_

The `slowms` and `slowOpSampleRate` also affect the operations that
are recorded in the diagnostic log when `logLevel` is set to
`0`. The `slowms` and `slowOpSampleRate` are also available to
configure diagnostic logging for `mongos`. [#slow-oplogs]_

**See also:**

- `mode`
- `slowOpThresholdMs`
- `slowOpSampleRate`

### Database Profiling and Sharding

You *cannot* enable profiling on a `mongos` instance. To enable
profiling in a sharded cluster, you must enable profiling for each
`mongod` instance in the cluster.

However, you can set the `--slowms` and 
`slowOpSampleRate` on `mongos` 
to configure the diagnostic log for slow operations.

## View Profiler Data

The database profiler logs information about database operations in the
`system.profile <` collection.

To view profiling information, query the `system.profile
<` collection. To view example queries, see
database-profiling-example-queries. For an explanation of the
output data, see /reference/database-profiler.

It is no longer possible to perform any operation, including reads, on the 
`system.profile <` collection from within a
transaction.

### Example Profiler Data Queries

This section shows example queries on the `system.profile
<` collection. For query output details, see
/reference/database-profiler.

To return the most recent 10 log entries in the `system.profile <`
collection, run a query similar to the following:

```javascript
db.system.profile.find().limit(10).sort( { ts : -1 } ).pretty()
```

To return all operations except command operations ($cmd), run a query
similar to the following:

```javascript
db.system.profile.find( { op: { $ne : 'command' } } ).pretty()
```

To return operations for a particular collection, run a query similar to
the following. This example returns operations in the `mydb` database's
`test` collection:

```javascript
db.system.profile.find( { ns : 'mydb.test' } ).pretty()
```

To return operations that take longer than 5 milliseconds to complete,
run:

```javascript
db.system.profile.find( { millis : { $gt : 5 } } ).pretty()
```

To return operations for a specific time range, run:

```javascript
db.system.profile.find( {
   ts : {
      $gt: new ISODate("2012-12-09T03:00:00Z"),
      $lt: new ISODate("2012-12-09T03:40:00Z")
   }
} ).pretty()
```

The following example looks at the time range, suppresses the `user`
field from the output to make it easier to read, and sorts the results
by how long each operation took to run:

```javascript
db.system.profile.find( {
   ts : {
      $gt: new ISODate("2011-07-12T03:00:00Z"),
      $lt: new ISODate("2011-07-12T03:40:00Z")
   }
}, { user: 0 } ).sort( { millis: -1 } )
```

### Show the Five Most Recent Events

On a database that has profiling enabled, the `show profile` helper
in `mongosh` displays the 5 most recent operations
that took at least 1 millisecond to execute. Run `show profile`
from `mongosh`:

```javascript
show profile
```

## Profiler Overhead

When enabled, profiling has an effect on database performance,
especially when configured with a
profiling level of 2, or when using a
low threshold value
with a profiling level of 1.

Profiling also uses disk space, because profiling
writes logs to the `system.profile <`
collection and the MongoDB `logfile`.

**Warning:**

Consider performance and storage implications before
you enable the profiler in a production deployment.

### The `system.profile` Collection

The `system.profile <` collection is a
capped collection with a default size of 1 megabyte. A
collection of this size can typically store several thousand profile
documents, but some applications may use more or less profiling data per
operation. If you need to change the size of the
`system.profile <` collection, follow
the steps below.

### Change Size of `system.profile` Collection on the Primary

To change the size of the `system.profile
<` collection on the primary, you
must:

1. Disable profiling.

#. Drop the `system.profile <`
   collection.

#. Create a new `system.profile <`
   collection.

#. Re-enable profiling.

For example, to create a new `system.profile
<` collection that is `4000000` bytes
(4 MB), use the following sequence of operations in
`mongosh`:

```javascript
db.setProfilingLevel(0)

db.system.profile.drop()

db.createCollection( "system.profile", { capped: true, size:4000000 } )

db.setProfilingLevel(1)
```

### Change Size of `system.profile` Collection on a Secondary

To change the size of the `system.profile
<` collection on a secondary, you must
stop the secondary, run it as a standalone, and then perform the steps
above. When done, restart the standalone as a member of the replica set.
For more information, see perform-maint-on-replica-set.
