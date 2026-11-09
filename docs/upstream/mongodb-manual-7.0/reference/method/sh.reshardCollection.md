<!-- Converted from reference/method/sh.reshardCollection.txt (reStructuredText). Includes are inlined. -->

# sh.reshardCollection() (mongosh method)

## Definition

**`sh.reshardCollection(namespace, key, unique, options)`**

**New in version:** 5.0

The `sh.reshardCollection()` method changes the shard key for
a collection and changes the distribution of your data.

Before you reshard a collection, read the the reshard
requirements and reshard limitations.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `reshardCollection` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

`sh.reshardCollection()` takes the following fields:

* - Field
  - Type
  - Description

* - `namespace`
  - string
  - The namespace of the collection to shard in the form
    `"<database>.<collection>"`.

* - `key`
  - document
  - The document that specifies the new field or fields to use as the
    shard key.

    `{ <field1>: <1|"hashed">, ... }`

    Set the field values to either:

    - `1` for ranged based sharding
    - `"hashed"` to specify a
      hashed shard key.

    See also sharding-shard-key-indexes

* - `unique`
  - boolean
  - Optional. Specify whether there is a uniqueness constraint on the shard key. Only
    `false` is supported. Defaults to `false`.

* - `options`
  - document
  - Optional. A document containing optional fields, including
    `numInitialChunks`, `collation` and `zones`.

The `options` field supports the following fields:

* - Field
  - Type
  - Description

* - `numInitialChunks`
  - integer
  - Optional. Specifies the initial number of chunks to create
    across all shards in the cluster when resharding a collection.
    The default is the number of chunks that exist for the
    collection under the current shard key pattern. MongoDB will
    then create and balance chunks across the cluster. The
    `numInitialChunks` must result in less than `8192` per shard.

    If you see the error "The shard key provided does not have enough
    cardinality to make the required number of chunks", reshard the
    collection with a lower `numInitialChunks` value.

* - `collation`
  - document
  - Optional. If the collection specified to `reshardCollection`
    has a default collation, you *must* include a 
    collation document with `{ locale : "simple" }`, or the 
    `reshardCollection` command fails.

* - `zones`
  - array
  - Optional. To maintain or add zones,
    specify the zones for your collection in an array:

    ```javascript
    [
       {
           min: <document with same shape as shardkey>,
           max: <document with same shape as shardkey>,
           zone: <string> | null
       },
       ...
    ]
    ```

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Considerations

Index builds that occur during resharding might silently
fail.

- Do not create indexes during the resharding process.

- Do not start the resharding process if there are ongoing index builds.

## Resharding Process

In a collection resharding operation, a shard can be a:

- **donor**, which currently stores chunks for the
  sharded collection.
- **recipient**, which stores new chunks for the sharded collection
  based on the shard keys and zones.

A shard can be donor and a recipient at the same time. The set of donor
shards is identical to the recipient shards, unless you use zones.

The config server primary is always the resharding coordinator and
starts each phase of the resharding operation.

### Initialization Phase

During the initialization phase, the resharding coordinator determines
the new data distribution for the sharded collection.

### Index Phase

During the index phase:

- Each shard recipient creates a new, empty sharded collection with the
  same collection options as the existing sharded collection. This new
  sharded collection is the target for where recipient shards write the
  new data.
- Each shard recipient builds the necessary new indexes. These include
  all existing indexes on the sharded collection and an index compatible
  with the new shard key pattern if such an index doesn’t already exist on
  the sharded collection.

### Clone, Apply, and Catch-up Phase

During the clone, apply, and catch-up phase:

- Each shard recipient clones an initial copy of the documents it would
  own under the new shard key.
- Each shard recipient begins applying oplog entries from operations
  that happened after the recipient cloned the data.
- When the estimate for the time remaining to complete the resharding
  operation is under **two seconds**, the resharding coordinator blocks
  writes for the collection.

  **Note:**

  If required, you can manually force the resharding operation to
  complete by issuing the `sh.commitReshardCollection()`
  method. This is useful if the current time estimate to complete the
  resharding operation is an acceptable duration for your collection
  to block writes. The `sh.commitReshardCollection()` method
  blocks writes early and forces the resharding operation to
  complete. During the time period where writes are blocked your
  application experiences an increase in latency.

### Commit Phase

- After the resharding process reaches the commit phase, the process
  cannot be ended with `sh.abortReshardCollection()`.
- When all shards have reached strict consistency, the resharding
  coordinator commits the resharding operation and installs the new
  routing table.
- The resharding coordinator instructs each donor and recipient shard
  primary, independently, to rename the temporary sharded collection.
  The temporary collection becomes the new resharded collection.
- Each donor shard drops the old sharded collection.

  **See also:**

  sharding-resharding

## Example

### Reshard a Collection

The following example reshards the `sales.orders` collection with the
new shard key `{ order_id: 1 }`:

```javascript
sh.reshardCollection( "sales.orders", { order_id: 1 } )
```

Example output:

```javascript
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp(1, 1624887954),
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: 0
    }
  },
  operationTime: Timestamp(1, 1624887947)
}
```

### Reshard a Collection with Zones

Reshard a collection with zones when you need to adjust the distribution 
of data across the shards in your cluster to meet changing requirements or 
to improve performance. 

In the following example, the `test.scores` collection resides on `shard0` 
and `shard1`. The current shard key is `{ _id: 1}`. 

**Step 1: Add shards to a new zone**

In this example, this zone is called `NewZone`.

```javascript
sh.addShardToZone( “shard2”, ‘NewZone’ )
sh.addShardToZone( “shard3”, ‘NewZone’ )
```

**Step 2: Run `sh.reshardCollection` with the new zone information**

```javascript
sh.reshardCollection(
  "test.scores", 
  { "studentId": 1, "testId": 1}, 
  { zones: [ {
    min: { "studentId": MinKey(), "testId": MinKey() },
    max: { "studentId": MaxKey(), "testId": MaxKey() },
    zone: "NewZone" }
    ]
} )
```

The resharding operation adds the shards in zone `NewZone` as recipients. 
The database primary shard is added as a recipient as a backstop for any
missing ranges in the zone definition. If there are no missing ranges, the 
collection is cloned on shards in the "NewZone", such as `shard2` and 
`shard3` in this example. `sh.reshardCollection` returns the following:

```javascript
{
   ok: 1,
   '$clusterTime': {
   clusterTime: Timestamp( { t: 1699484530, i: 54 } ),
   signature: {
   hash: Binary.createFromBase64( "90ApBDrSSi4XnCpV3OWIH4OGO0Y=", 0 ),
   keyId: Long( "7296989036055363606" )
   } },
   operationTime: Timestamp( { t: 1699484530, i: 54 } )
}
```

**See also:**

sharding-resharding
