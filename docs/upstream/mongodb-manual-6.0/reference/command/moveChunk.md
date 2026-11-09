<!-- Converted from reference/command/moveChunk.txt (reStructuredText). Includes are inlined. -->

# moveChunk

## Definition

**`moveChunk`**

Internal administrative command. Moves chunks between
shards. Issue the `moveChunk` command via
a `mongos` instance while using the admin database.
Use the following forms:

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.moveChunk`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

```javascript
db.adminCommand( { moveChunk : <namespace> ,
                 find : <query> ,
                 to : <string>,
                 forceJumbo: <boolean>,
                 _secondaryThrottle : <boolean>,
                 writeConcern: <document>,
                 _waitForDelete : <boolean> } )
```

Alternatively:

```javascript
db.adminCommand( { moveChunk : <namespace> ,
                 bounds : <array> ,
                 to : <string>,
                 forceJumbo: <boolean>, 
                 _secondaryThrottle : <boolean>,
                 writeConcern: <document>,
                 _waitForDelete : <boolean> } )
```

The `moveChunk` command has the following fields:

* - Field

  - Type

  - Description

* - `moveChunk`

  - string

  - The namespace of the collection where the
    chunk exists. Specify the collection's full namespace,
    including the database name.

* - `find`

  - document

  - An equality match on the shard key that specifies the shard-key value
    of the chunk to move. Specify either the `bounds` field or the
    `find` field but not both. Do **not** use the `find` field to
    select chunks in collections that use a hashed shard key.

* - `bounds`

  - array

  - The bounds of a specific chunk to move. The array must consist of two
    documents that specify the lower and upper shard key values of a chunk
    to move. Specify either the `bounds` field or the `find` field but
    not both. Use `bounds` to select chunks in collections that use a
    hashed shard key.

* - `to`

  - string

  - The name of the destination shard for the chunk.

* - forceJumbo

  - boolean

  - .. _movechunk-forceJumbo:

    Optional. A flag that determines if the command can move a
    chunk that is too large to migrate. The chunk may or may not be
    labeled as jumbo.

    - If `true`, the command can move the chunk.

    - If `false`, the command cannot move the chunk.

    The default is `false`.

    WARNING:

    The `moveChunk` command with `forceJumbo=true` blocks write
    operations on the collection.

    This option causes the shard to migrate chunks even when they
    are larger than the configured chunk size. The collection
    remains unavailable for writes for the duration of the
    migration.

    To migrate these large chunks without this long blocking period,
    see balance-chunks-that-exceed-size-limit instead.

* - `_secondaryThrottle`

  - boolean

  - Optional. For WiredTiger, defaults to 
    `false`.

    - If `true`, then by default, each document move during chunk
      migration propagates to at least one secondary before the balancer
      proceeds with the next document. This is equivalent to a write
      concern of `{ w: 2 } <`. 

      Use the `writeConcern` option to specify a different write concern.

    - If `false`, the balancer does not wait for replication to a
      secondary and instead continues with the next document.

    For more information, see
    sharded-cluster-config-secondary-throttle.

* - `writeConcern`

  - document

  - Optional. A document that expresses the write concern that the `_secondaryThrottle` will use to
    wait for secondaries during the chunk migration. 

    `writeConcern` requires `_secondaryThrottle: true`.

* - `_waitForDelete`

  - boolean

  - Optional. If set to `true`, the delete phase of a `moveChunk` 
    operation is blocking. `_waitForDelete` defaults to `false`.

    When the `_waitForDelete` field is set, MongoDB does not wait on the 
    `orphanCleanupDelaySecs` delay before performing the range 
    deletion. If you use the `_waitForDelete` parameter and have any
    read operations occurring on secondaries, the read may miss documents 
    due to the migration's delete phase. 

The value of `bounds` takes the form:

```javascript
[ { hashedField : <minValue> } ,
  { hashedField : <maxValue> } ]
```

The chunk migration section
describes how chunks move between shards on MongoDB.

**See also:**

- `split`
- `sh.moveChunk()`
- `sh.splitAt()`
- `sh.splitFind()`

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

     

## Considerations

Only use the `moveChunk` in special circumstances
such as preparing your sharded cluster for an initial
ingestion of data, or a large bulk import operation.  In most cases
allow the balancer to create and balance chunks in sharded clusters.
See /tutorial/create-chunks-in-sharded-cluster for more information.

## Behavior

### Indexes

`moveChunk` requires that all indexes exist on the
target (i.e. `to` ) shard before migration and returns an error if a
required index does not exist.

### Meta Data Error

`moveChunk` returns the following error message if another
metadata operation is in progress on the `chunks` collection:

```none
errmsg: "The collection's metadata lock is already taken."
```

If another process, such as a balancer process, changes meta data
while `moveChunk` is running, you may see this
error. You may retry the `moveChunk` operation without
side effects.

### `maxCatchUpPercentageBeforeBlockingWrites` Server Parameter

Starting in MongoDB 5.0, you can set the
`maxCatchUpPercentageBeforeBlockingWrites` to specify the
maximum allowed percentage of data not yet migrated
during a `moveChunk` operation when compared to the
total size (in MBs) of the chunk being transferred.
