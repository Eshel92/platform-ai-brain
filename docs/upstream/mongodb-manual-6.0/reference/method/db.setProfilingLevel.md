<!-- Converted from reference/method/db.setProfilingLevel.txt (reStructuredText). Includes are inlined. -->

# db.setProfilingLevel()

## Definition

**`db.setProfilingLevel(level, options)`**

**Changed in version:** 5.0

For a `mongod` instance, the method enables, disables,
or configures the /tutorial/manage-the-database-profiler. The
profiler captures and records data on the performance of write
operations, cursors, and database commands on a running
`mongod` instance. If the profiler is disabled, the
method configures how slow operations are logged to the diagnostic
log.

**Note:**

Changes made to the profiling level with `db.setProfilingLevel()`
do *not* persist.  When the server restarts, it reverts to `0`
(the default), or the value set by either the 
`operationProfiling.mode` setting or the 
`--profile` command-line option.

If the database profiler level is
`1` or `2` (specifically, the database profiler is enabled), the
slowms,
sampleRate affect
the behavior of both the profiler and the `diagnostic log`.

If the database profiler level is
`0` (specifically, database profiler is disabled), the
slowms and
sampleRate, affect
only the diagnostic log.

With `mongos` instances, the
method sets the `slowms`, `sampleRate` and `filter`
configuration settings, which configure how operations get written to
the diagnostic log. You cannot enable the
/tutorial/manage-the-database-profiler on a
`mongos` instance because `mongos` does not have any
collections that the profiler can write to. The `profile` level
must be `0` for a `mongos` instance.

You can specify a filter on both 
`mongod` and `mongos` instances to control which 
operations are logged by the profiler. When you specify a `filter` for the
profiler, the slowms, and
sampleRate options
are not used for profiling and slow-query log lines.

`db.setProfilingLevel()` provides a wrapper around the
`profile` command.

Starting in MongoDB 5.0, changes made to the database profiler `level`, `slowms`, `sampleRate`, or
`filter` using the `profile` command or
`db.setProfilingLevel()` wrapper method are recorded in the
`log file`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `db.setProfilingLevel()` method has the following form:

```javascript
db.setProfilingLevel(<level>, <options>)
```

## Parameters

* - Parameter

  - Type

  - Description

* - level

  - integer

  - .. _set-profiling-level-level:

    Configures the database profiler level. The following
    profiler levels are available:

    `0`
       The profiler is off and does not collect any data.
       This is the default profiler level.

    `1`
       The profiler collects data for operations that exceed the
       `slowms` threshold or match a specified filter.

       When a filter is set:

       - The `slowms` and `sampleRate` options are not used for
         profiling.
       - The profiler only captures operations that match the
         filter.

    `2`
       The profiler collects data for all operations.

    Because profiling is not available on `mongos`,
    `db.setProfilingLevel()` cannot be used to set the profiling
    level to a value other than `0` on a `mongos` instance.

* - options

  - document or integer

  - .. _set-profiling-level-options:

    Optional. Accepts an integer or an options document. If an integer value is
    passed as the `options` argument instead of a document, the value is
    assigned to slowms.
    The following options are available:

    * - slowms

      - .. _set-profiling-level-options-slowms:

        | Default: 100
        | Type: integer

        The *slow* operation time threshold, in milliseconds. Operations
        that run for longer than this threshold are considered *slow*.

        When `logLevel` is set to `0`, MongoDB records *slow*
        operations to the diagnostic log at a rate determined by
        `slowOpSampleRate`.

        At higher `logLevel` settings, all operations appear in
        the diagnostic log regardless of their latency with the following
        exception: the logging of slow oplog entry messages by the
        secondaries. The secondaries log only the slow oplog
        entries; increasing the `logLevel` does not log all
        oplog entries.

        For `mongod` instances, the setting affects both the
        diagnostic log and, if enabled, the profiler.

        For `mongos` instances, the setting affects
        the diagnostic log only and not the profiler because
        profiling is not available on `mongos`.

        This argument affects the same setting as the configuration
        file option `slowOpThresholdMs`.

    * - sampleRate

      - .. _set-profiling-level-options-sampleRate:

        | Default: 1.0
        | Type: double

        The fraction of *slow* operations that should be profiled or logged.
        `sampleRate` accepts values between 0 and 1, inclusive.

        For `mongod` instances, the setting affects both the
        diagnostic log and, if enabled, the profiler.

        For `mongos` instances, the setting affects
        the diagnostic log only and not the profiler because
        profiling is not available on `mongos`.

        This argument affects the same setting as the
        configuration option
        `slowOpSampleRate`.

    * - filter

      - .. _set-profiling-level-options-filter:

        Type: object

        A filter expression that controls which operations are
        profiled and logged.  The field in the filter expression
        can be any field in the profiler output.

        For `mongod` instances, the setting affects both the
        diagnostic log and, if enabled, the profiler.

        For `mongos` instances, the setting affects
        the diagnostic log only and not the profiler because
        profiling is not available on `mongos`.

        For an example of a filter used to control logged
        operations, see profiler-filter-example.

        When a profiling filter is set, the
        slowms and
        sampleRate options do
        not affect the diagnostic log or the profiler.

## Returns

The method returns a document that contains the **previous** values of
the settings.

**standalone:**

```javascript
{
   "was" : 2,
   "slowms" : 100,
   "sampleRate" : 1,
   "filter" : {
      "$and" : [
         {
            "op" : {
               "$eq" : "query"
            }
         },
         {
            "millis" : {
               "$gt" : 20000
            }
         }
      ]
   },
   "note" : "When a filter expression is set, slowms and sampleRate are not used for profiling and slow-query log lines.",
   "ok" : 1
}
```

**repl-set:**

```javascript
{
   "was" : 0,
   "slowms" : 100,
   "sampleRate" : 1,
   "filter" : {
      "$and" : [
         {
            "op" : {
               "$eq" : "query"
            }
         },
         {
            "millis" : {
               "$gte" : 2000
            }
         }
      ]
   },
   "note" : "When a filter expression is set, slowms and sampleRate are not used for profiling and slow-query log lines.",
   "ok" : 1,
   "$clusterTime" : {
      "clusterTime" : Timestamp(1572991238, 1),
      "signature" : {
         "hash" : BinData(0,"hg6GnlrVhV9MAhwWdeHmHQ4T4qU="),
         "keyId" : NumberLong("6755945537557495811")
      }
   },
   "operationTime" : Timestamp(1572991238, 1)
}
```

**mongos:**

```javascript
{
   "was" : 0,
   "slowms" : 100,
   "sampleRate" : 1,
   "filter" : {
      "$and" : [
         {
            "op" : {
               "$eq" : "query"
            }
         },
         {
            "millis" : {
               "$gte" : 2000
            }
         }
      ]
   },
   "note" : "When a filter expression is set, slowms and sampleRate are not used for profiling and slow-query log lines.",
   "ok" : 1,
   "operationTime" : Timestamp(1572991499, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1572991499, 2),
      "signature" : {
         "hash" : BinData(0,"nhCquIxUw7thlrBudXe3PnsnvP0="),
         "keyId" : NumberLong("6755946491040235540")
      }
   }
}
```

Where:

- `was` is the **previous** level
  setting.

- `slowms` is the **previous** slowms setting.

- `sampleRate` is the **previous** sampleRate setting.

- `filter` is the **previous** filter setting.

- `note` is a string explaining the behavior of `filter`. This field
  only appears in the output when `filter` is also present.

**Note:**

The `filter` and `note` fields only appear in the output if
they were present in the previous level setting.

To view the current profiling level, see `db.getProfilingStatus()`.

## Behavior

**Warning:**

Profiling can degrade performance and expose unencrypted query data in the
system log. Carefully consider any performance and security implications
before configuring and enabling the profiler on a production deployment.

See database-profiling-overhead for more information on
potential performance degradation.

## Examples

### Enable Profiler and Set Slow Operation Threshold and Sample Rate

The following example sets for a `mongod` instance:

- the profiling level to `1`,

- the slow operation threshold slowms to `20` milliseconds, and
  
- the sampleRate to
  `0.42`.

```javascript
db.setProfilingLevel(1, { slowms: 20, sampleRate: 0.42 })
```

The operation returns a document with the **previous** values for the
settings.

To view the current profiling level, see
`db.getProfilingStatus()`.

### Disable Profiler and Set Slow Operation Threshold and Sample Rate

The following example sets for a `mongod` or
`mongos` instance:

- the profiling level to `0`,

- the slow operation threshold slowms to `20` milliseconds, and

- the sampleRate to
  `0.42`.

```javascript
db.setProfilingLevel(0, { slowms: 20, sampleRate: 0.42 })
```

The operation returns a document with the **previous** values for the
settings.

To view the current profiling level, see
`db.getProfilingStatus()`.

### Set a Filter to Determine Profiled Operations

The following example sets for a `mongod` instance:

- the profiling level to `1`,

- a filter of
  `{ op: "query", millis: { $gt: 2000 } }`, which causes the profiler
  to only record `query` operations that took longer than 2 seconds.

```javascript
db.setProfilingLevel( 1, { filter: { op: "query", millis: { $gt: 2000 } } } )
```

The operation returns a document with the **previous** values for the
settings.

To view the current profiling level, see
`db.getProfilingStatus()`.

### Unset a Filter

To clear a profile filter, run `db.setProfilingLevel()` with the
`filter: "unset"` option.

```javascript
db.setProfilingLevel( 1, { filter: "unset" } )
```

The operation returns a document with the **previous** values for the
settings.

To view the current profiling level, see
`db.getProfilingStatus()`.
