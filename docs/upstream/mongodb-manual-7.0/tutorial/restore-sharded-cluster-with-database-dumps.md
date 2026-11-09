<!-- Converted from tutorial/restore-sharded-cluster-with-database-dumps.txt (reStructuredText). Includes are inlined. -->

# Restore a Self-Managed Sharded Cluster from Database Dumps

`mongorestore` is a tool that reads `mongodump`
binary exports and restores the data to a MongoDB deployment. Use
`mongorestore` to restore a sharded cluster from a
`mongodump` backup.

## Before you Begin

Ensure you have a `mongodump` backup of your source
cluster. To create one, see backup-sharded-dumps. If you
have file system snapshots, see restore-sharded-cluster.

## Steps

**Step 1: Stop the balancer.**

To prevent chunk migrations from disrupting the restore,
connect to `mongos` and stop the balancer:

```javascript
sh.stopBalancer()
```

To verify that you stopped the balancer, run:

```javascript
use config
while( sh.isBalancerRunning().mode != "off" ) {
   print( "Waiting for Balancer to stop..." );
   sleep( 1000 );
}
```

**Step 2: Pre-shard collections on the destination cluster.**

For each sharded collection in the source cluster, create
the collection on the destination cluster and shard it
using the same shard key before restoring data.

To find the shard key for each collection, query
the live source cluster:

```javascript
use config
db.collections.find()
```

Alternatively, you can use `bsondump` to inspect the
`config/collections.bson` file from your dump directory:

```bash
bsondump /path/to/dump/config/collections.bson
```

Output:

```json
{
  "_id": "<database>.<collection>",
  ...
  "key": { "<shardKeyField>": "<key>" },
  ...
}
```

**Note:**

Valid shard key values are `1` or `"hashed"`.

For each sharded collection, shard the collection on the
destination cluster using the same shard key:

```javascript
sh.shardCollection(
   "<database-name>.<collection-name>",
   { <shardKeyField>: <key> }
)
```

**Step 3: Restore the cluster.**

Use `mongorestore` to connect to
`mongos` and restore the cluster. Exclude the
`config` database to preserve the destination cluster's
existing configuration:

```bash
mongorestore \
   --host <host> \
   --port 27017 \
   --username <username> \
   --password "<password>" \
   --authenticationDatabase admin \
   --nsExclude='config.*' \
   /path/to/backup
```

**Important:**

The `--drop` option drops the collection before
restoring. If you use `--drop` after pre-sharding
collections, `mongorestore` removes the
sharding configuration.

**Step 4: Restart the balancer.**

After the restore completes, restart the balancer:

```javascript
sh.startBalancer()
```

To confirm that the balancer is running:

```javascript
sh.isBalancerRunning().mode
```

Output:

```javascript
full
```

**Step 5: Validate cluster accessibility.**

Connect to `mongos` and run
`sh.status()` to check the overall cluster
status:

```javascript
sh.status()
```

To confirm that all shards are accessible and
communicating, insert a test document into a temporary
collection:

```javascript
db.testRestore.insertOne({ test: 1 })
```

Then connect to each shard primary and run
`db.collection.find()` to confirm that the
document is present:

```javascript
db.testRestore.find()
```

## Learn More

- backup-restore-sharded-clusters
- backup-sharded-dumps
- restore-sharded-cluster
