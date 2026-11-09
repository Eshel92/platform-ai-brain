<!-- Converted from tutorial/drop-a-hashed-shard-key-index.txt (reStructuredText). Includes are inlined. -->

# Drop a Hashed Shard Key Index

Starting in MongoDB 7.0.3 (and 6.0.12 and 5.0.22), you can drop the 
index for a hashed shard key.

This can speed up data insertion for collections sharded with a hashed 
shard key.

## About this Task

Dropping an unnecessary index
can speed up CRUD operations. Each CRUD operation has to update all the 
indexes related to a document. Removing one index can increase the 
speed of all CRUD operations.

**Important:**

You should only drop a hashed shard key index from a collection 
if a supporting non-hashed index on the shard key exists. If a 
supporting non-hashed index does not exist on the shard key, queries 
filtering by the shard key perform a collection scan.
To see what indexes exist on a collection, use 
`db.collection.getIndexes()`.

## Considerations

When dropping a hashed shard key index, consider the following:

- The server disables balancing for your collection and excludes
  the collection from future balancing rounds. As a result, if you
  later add or remove a shard, the server cannot rebalance the
  collection's data. To include the collection in future balancing rounds,
  recreate the hashed shard key index.
- When you drop the shard key index, the range deleter does not clean up 
  any remaining orphans in your collection. You must confirm that no orphaned
  documents exist in your collection before dropping the hashed shard key index.
  See the below procedure for how to confirm that there are no orphaned documents
  in your collection.

## Steps

**Step 1: Stop the balancer**

Run the following command to stop the balancer:

```javascript
sh.stopBalancer()
```

You can only run `sh.stopBalancer()` on `mongos`. 
`sh.stopBalancer()` produces an error if run on `mongod`.

**Step 2: Confirm there are no orphaned documents in your collection**

Starting in MongoDB 6.0.3, you can run an aggregation using the 
`$shardedDataDistribution` stage to confirm no orphaned 
documents remain:

```javascript
db.aggregate([ 
   { $shardedDataDistribution: {} },
   { $match: { "ns": "<database>.<collection>" } }
])
```

`$shardedDataDistribution` has output similar to the following:

```json
[
  {
    "ns": "test.names",
    "shards": [
      {
        "shardName": "shard-1",
        "numOrphanedDocs": 0,
        "numOwnedDocuments": 6,
        "ownedSizeBytes": 366,
        "orphanedSizeBytes": 0
      },
      {
        "shardName": "shard-2",
        "numOrphanedDocs": 0,
        "numOwnedDocuments": 6,
        "ownedSizeBytes": 366,
        "orphanedSizeBytes": 0
      }
    ]
  }
]
```

Ensure that `"numOrphanedDocs"` is `0` for each shard in the
cluster.

**Step 3: Drop the hashed shard key index**

Run the following command to drop the index:

```javascript
db.collection.dropIndex("<index name>")
```

**Step 4: Restart the balancer**

Run the following command to restart the balancer on the cluster:

```javascript
sh.startBalancer()
```

## Learn More

- sharding-hashed
- sharding-balancing
- `db.collection.dropIndex()`
- `sh.stopBalancer()`
- `sh.startBalancer()`
- `sh.getBalancerState()`
