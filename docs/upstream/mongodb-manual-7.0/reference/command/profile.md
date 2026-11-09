<!-- Converted from reference/command/profile.txt (reStructuredText). Includes are inlined. -->

# profile (database command)

## Definition

**`profile`**

**Changed in version:** 5.0

For a `mongod` instance, the command enables, disables,
or configures the database profiler. The
profiler captures and records data on the performance of write
operations, cursors, and database commands on a running
`mongod` instance. If the profiler is disabled, the
command configures how slow operations are logged to the diagnostic
log.

On `mongod`, if the database profiler level is `2`, full logging is enabled on
the profiler and the `diagnostic log`.

At database profiler level `1`,
the following settings modify both the profiler and the
`diagnostic log`:

- slowms
- sampleRate
- filter

If the database profiler level is
`0`, the database profiler is disabled.
At level `0` the following settings only modify the diagnostic log:

- slowms
- sampleRate
- filter

For a `mongos` instance, the command only configures how 
operations get written to the diagnostic log. You cannot enable the 
database profiler on a `mongos` 
instance because `mongos` does not have any collections that the profiler 
can write to.

Starting in MongoDB 5.0, changes made to the database profiler `level`, `slowms`, `sampleRate`, or
`filter` using the `profile` command or
`db.setProfilingLevel()` wrapper method are recorded in the
`log file`.

On `mongos`, you can set `profile` level to:

- `0` to set the `slowms`, `sampleRate`, and `filter` for
  the diagnostic log;

- `-1` to read the current settings.

The profiler is off by default.

**Warning:**

Profiling can degrade performance and expose unencrypted query data in the
system log. Carefully consider any performance and security implications
before configuring and enabling the profiler on a production deployment.

See database-profiling-overhead for more information on
potential performance degradation.

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
    profile: <level>,
    slowms: <threshold>,
    sampleRate: <rate>,
    filter: <filter expression>
  }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `profile`
  - int
  - Configures the profiler level.
    The following profiler levels are available:

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

    Since profiling is not available on `mongos`, the
    `profile` command cannot be used to set the profiling
    level to a value other than `0` on a `mongos` instance.

* - `slowms`
  - int
  - .. _slowms-threshold-option:

    Optional. Default: 100

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

    This argument affects the same setting as the configuration option
    `operationProfiling.slowOpThresholdMs`.

* - `sampleRate`
  - double
  - Optional. Default: 1.0

    The fraction of *slow* operations that should be profiled or logged.
    `sampleRate` accepts values between 0 and 1, inclusive.

    This argument affects the same setting as the configuration option
    `operationProfiling.slowOpSampleRate` and does not
    affect the slow oplog entry log messages on secondaries.

* - `filter`
  - object
  - .. _profile-filter-def:

    Optional.
    A query that determines which operations are profiled or
    logged.

    The filter query takes the following form:

    ```javascript
    { <field1>: <expression1>, ... }
    ```

    The query can be any legal `find()`
    operation where the query `<field>` matches a field in the
    profiler output.

    This argument affects the same setting as the
    configuration option `operationProfiling.filter`.
    When `filter` is set, the `slowms` and `sampleRate`
    options are not used for profiling and slow-query log
    lines.

The `db.getProfilingStatus()` and
`db.setProfilingLevel()` shell methods provide wrappers around the
`profile` command.

## Behavior

The `profile` command obtains a write lock on the affected
database while enabling or disabling the profiler. This is typically a
short operation. The lock blocks other operations until the
`profile` command has completed.

When connected to a sharded cluster through `mongos`, you can run 
the `profile` command against any database. 

**See also:**

Database Profiling

## Example

### Enable Filtering

To enable profiling and filter the logged data:

```javascript
db.runCommand( 
   {
     profile: 1,
     filter:
        {
           $or:
           [
              { millis: { $gte: 100 } },
              { user: "testuser@admin" }
           ]
        }
   }
)
```

The filter only selects operations that
are:

- at least `100` milliseconds long, or
- submitted by the `testuser`.

### Unset a Filter

To clear a profile filter, run `profile` with the `filter: "unset"`
option.

```javascript
db.runCommand(
   { 
      profile: 1,
      filter: "unset" 
   }
)
```

The operation returns a document with the **previous** values for the
settings.

To view the current profiling level, see
`db.getProfilingStatus()`.
