<!-- Converted from reference/command/moveRange.txt (reStructuredText). Includes are inlined. -->

# moveRange (database command)

## Definition

**`moveRange`**

**New in version:** 6.0

Moves ranges between shards. Run
the `moveRange` command with a `mongos` 
instance while using the admin database.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.moveRange`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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
db.adminCommand( 
  { 
    moveRange: <namespace>,
    toShard: <ID of the recipient shard>,
    min: <min key of the range to move>, // conditional
    max: <max key of the range to move>, // conditional
    forceJumbo: <bool>, // optional
    writeConcern: <write concern>, // optional
    secondaryThrottle: <bool> // optional
  } 
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `toShard`
  - string
  - ID of the recipient shard.

* - `min`
  - key
  - Minimum key of the range to move. Required if you don't specify
    `max`.

    If you do not specify `min`, given a chunk `C` where `max`
    is either the exclusive upper bound of `C` or `C` includes
    the shard key `max`, `min` is determined in the following
    way:

    - If the data size of the range between `min(C)` and `max` 
      is less than the per-collection chunk size or the default 
      chunk size, the chunk's `min` value is selected as 
      `min` = `min(C)`.

    - Otherwise, key `min` > `min(C)` where `min` depends 
      on the configured chunk size.

* - `max`
  - key
  - Maximum key of the range to move. Required if you don't specify
    `min`.

    If you do not specify 
    `max`, given a chunk `C` including the shard key `min`, 
    `max` is determined in the following way:

    - If the data size of the range between `min` and `max(C)` 
      is less than the per-collection chunk size or the default 
      chunk size, the chunk's max is selected as 
      `max` = `max(C)`.

    - Otherwise, key `max` < `max(C)` where `max` depends 
      on the configured chunk size.

* - forceJumbo
  - boolean
  - .. _moverange-forceJumbo:

    Optional. 

    Flag that determines if the command can move a range that is 
    too large to migrate. The 
    range may or may not be labeled as jumbo.

    - If `true`, the command can move the range.
    - If `false`, the command cannot move the range.

    The default is `false`.

    WARNING:

    The `moveRange` command with `forceJumbo=true` blocks write
    operations on the collection.

    This option causes the shard to migrate chunks even when they
    are larger than the configured chunk size. The collection
    remains unavailable for writes for the duration of the
    migration.

    To migrate these large chunks without this long blocking period,
    see balance-chunks-that-exceed-size-limit instead.

* - `writeConcern`
  - document
  - Optional. 

    Document with the write concern.

    The default is `w: majority`.

* - `secondaryThrottle`
  - boolean
  - Optional. 

    - If `true`, each document move during chunk migration 
      propagates to at least one secondary before the balancer 
      proceeds with the next document. This is equivalent to a write 
      concern of `{ w: 2 } <`. 

      Use the `writeConcern` option to specify a different write 
      concern.

    - If `false`, the balancer does not wait for replication to a
      secondary and instead continues with the next document.

    For more information, see
    sharded-cluster-config-secondary-throttle.
       
The range migration section
describes how ranges move between shards on MongoDB.

## Considerations

Only use the `moveRange` in scenarios like:

- an initial ingestion of data
- a large bulk import operation  

Allow the balancer to create and balance ranges in sharded clusters in
most cases.

**See also:**

create-chunks-in-a-sharded-cluster

## Examples

The following examples use a collection with:

- Shard key `x`
- Configured chunk size of 128MB
- A chunk with boundaries: `[x: 0, x: 100)`

### Specify both `min` and `max`

The following table lists the results of setting `min` and `max`
to various values:

* - `min`
  - `max`
  - Result

* - `0`
  - `100`
  - Moves all the documents in the range to the recipient shard.

* - `10`
  - `30`
  - Creates three sub-ranges: 

    - `[x: 0, x: 10)`
    - `[x: 10, x: 30)` 
    - `[x: 30, x: 100)`

    Moves all the documents in `[x: 10, x: 30)` to the recipient
    shard.

* - `0`
  - `20` 
  - Creates two sub-ranges:

    - `[x: 0, x: 20)`
    - `[x: 20, x: 100)`

    Moves all the documents in `[x: 0, x: 20)` to the recipient
    shard.

* - `40`
  - `100`
  - Creates two sub-ranges:

    - `[x: 0, x: 40)`
    - `[x: 40, x: 100)`

    Moves all the documents in `[x: 40, x: 100)` to the recipient
    shard.

### Specify `min` but not `max`

The following table lists the results of setting `min` to various 
values:

* - `min`
  - Amount of Data in Key Range
  - Result

* - `0`
  - Less than 128 MB contained between keys `x: 0` and `x: 100`.
  - Moves all the documents in the range to the recipient shard.

* - `10`
  - Less than 128 MB contained between keys `x: 0` and `x: 100`.
  - Creates two sub-ranges:

    - `[x: 0, x: 10)`
    - `[x : 10, x: 100)`

    Moves all documents in `[x: 10, x: 100)` to the recipient 
    shard.

* - `10`
  - 128 MB contained between keys `x: 10` and `x: 30`.
  - Creates three sub-ranges:

    - `[x: 0, x: 10)`
    - `[x: 10, x: 30)` 
    - `[x: 30, x: 100)`

    Moves all documents in `[x: 10, x: 30)` to the recipient
    shard.

### Specify `max` but not `min`

The following table lists the results of setting `max` to various 
values:

* - `max`
  - Amount of Data in Key Range
  - Result

* - `100`
  - Less than 128 MB contained between keys `x: 0` and `x: 100`.
  - Moves all the documents in the range to the recipient shard.

* - `10`
  - Less than 128 MB contained between keys `x: 0` and `x: 100`.
  - Creates two sub-ranges:

    - `[x: 0, x: 10)`
    - `[x : 10, x: 100)`

    Moves all documents in `[x: 0, x: 10)` to the recipient 
    shard.

* - `30`
  - 128 MB contained between keys `x: 10` and `x: 30`.
  - Creates three sub-ranges:

    - `[x: 0, x: 10)`
    - `[x: 10, x: 30)` 
    - `[x: 30, x: 100)`

    Moves all documents in `[x: 10, x: 30)` to the recipient
    shard.
