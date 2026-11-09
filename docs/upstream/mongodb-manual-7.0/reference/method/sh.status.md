<!-- Converted from reference/method/sh.status.txt (reStructuredText). Includes are inlined. -->

# sh.status() (mongosh method)

## Definition

**`sh.status()`**

When run on a `mongos` instance, prints a formatted report
of the sharding configuration and the information regarding existing
chunks in a sharded cluster. The default behavior suppresses
the detailed chunk information if the total number of chunks is
greater than or equal to 20.

The `sh.status()` method has the following parameter:

* - Parameter

  - Type

  - Description

* - `verbose`

  - boolean

  - Optional. Determines the level of verbosity.

    If `true`, the method displays:

    - Full details of the chunk distribution across shards even if
      you have 20 or more chunks, as well as the number of chunks
      on each shard.

    - Details of active mongos instances.

    If `false`, the method displays:

    - Full details of the chunk distribution across shards only if
      you have less than 20 chunks. If you have 20 or more chunks,
      the method instead returns a `too many chunks to print ...`
      message, showing only the number of chunks on each shard.

    - Only the version and number of active mongos
      instances.

    The default verbose value is `false`.

The output also includes a `shardedDataDistribution` section,
which provides data distribution metrics for each sharded
collection. This data is the same as the output of the
`$shardedDataDistribution` aggregation stage.

**See also:**

`db.printShardingStatus()`

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

## Output Examples

The sharding-status-version-fields section displays information on the
config database:

```javascript
--- Sharding Status ---
  sharding version: {
   "_id" : <num>,
   "minCompatibleVersion" : <num>,
   "currentVersion" : <num>,
   "clusterId" : <ObjectId>
}
```

The sharding-status-shards-fields section lists information on
the shard(s). For each shard, the section displays the name, host, and
the associated tags, if any.

```javascript
shards:
 { "_id" : <shard name1>, "host" : <string>, "tags" : [ <string> ... ], "state" : <num> }
 { "_id" : <shard name2>, "host" : <string>, "tags" : [ <string> ... ], "state" : <num> }
 ...
```

The sharding-status-mongoses section displays, by default,
information on the version and count of `mongos` instances
that have been active within the last 60 seconds:

```javascript
active mongoses:
  <version> : <num>
```

If the method is run with the `verbose` parameter to true, the
sharding-status-mongoses section displays additional information:

```javascript
active mongoses:
{  "_id" : "<hostname:port>",  "advisoryHostFQDNs" : [ "<name>" ],  "mongoVersion" : <string>,  "ping" : <ISODate>,  "up" : <long>,  "waiting" : <boolean> }
```

The autosplit-status displays information on whether autosplit
is enabled:

```javascript
autosplit:
  Currently enabled: <yes|no>
```

The sharding-status-balancer-fields section lists information
about the state of the balancer. This provides insight into
current balancer operation and can be useful when troubleshooting an
unbalanced sharded cluster.

```none
balancer:
      Currently enabled:  yes
      Currently running:  yes
      Collections with active migrations: 
              config.system.sessions started at Fri May 15 2020 17:38:12 GMT-0400 (EDT)
      Failed balancer rounds in last 5 attempts:  0
      Migration Results for the last 24 hours: 
             416 : Success
             1 : Failed with error 'aborted', from shardA to shardB
```

The sharding-status-databases-fields section lists information
on the database(s). It displays the database name and the primary
shard for each database.

```javascript
databases:
 { "_id" : <dbname1>, "primary" : <string>, "partitioned" : <boolean>, "version": <document> }
 { "_id" : <dbname2>, "primary" : <string>, "partitioned" : <boolean>, "version": <document> }
 ...
```

The sharding-status-collection-fields section provides
information on the sharding details for sharded collection(s). For each
sharded collection, the section displays the shard key, the number of
chunks per shard(s), the distribution of chunks across shards
[#chunk-details]_, and the tag information, if any, for shard key
range(s).

```javascript
<dbname>.<collection>
   shard key: { <shard key> : <1 or hashed> }
   unique: <boolean>
   balancing: <boolean>
   allowMigrations: <boolean>
   chunks:
      <shard name1> <number of chunks>
      <shard name2> <number of chunks>
      ...
   { <shard key>: <min range1> } -->> { <shard key> : <max range1> } on : <shard name> <last modified timestamp>
   { <shard key>: <min range2> } -->> { <shard key> : <max range2> } on : <shard name> <last modified timestamp>
   ...
   tag: <tag1>  { <shard key> : <min range1> } -->> { <shard key> : <max range1> }
   ...
```

The sharding-status-sharded-data-distribution section displays
data distribution information for each sharded collection:

```javascript
shardedDataDistribution:
[
  {
    "ns" : "<database>.<collection>",
    "shards" : [
      {
        "shardName" : "<shard name>",
        "numOrphanedDocs" : <num>,
        "numOwnedDocuments" : <num>,
        "ownedSizeBytes" : <num>,
        "orphanedSizeBytes" : <num>
      }
    ]
  }
]
```

## Output Fields

### Sharding Version

**`sh.status.sharding-version._id`**

The `_id` is an identifier
for the version details.

**`sh.status.sharding-version.minCompatibleVersion`**

The `minCompatibleVersion` is
the minimum compatible version of the config server.

In MongoDB versions earlier than 6.2, this field is included in the
`config.version` collection, but in `mongosh` 2.0.0 and later, the
field is not returned in the `sh.status()` output. Starting in MongoDB
6.2, this field is removed and not returned in any `mongosh` version
or other client application. Instead, to obtain version information, see
the feature compatibility version (fcv).

**`sh.status.sharding-version.currentVersion`**

The `currentVersion` is
the current version of the config server.

In MongoDB versions earlier than 6.2, this field is included in the
`config.version` collection, but in `mongosh` 2.0.0 and later, the
field is not returned in the `sh.status()` output. Starting in MongoDB
6.2, this field is removed and not returned in any `mongosh` version
or other client application. Instead, to obtain version information, see
the feature compatibility version (fcv).

**`sh.status.sharding-version.clusterId`**

The `clusterId` is the
identification for the sharded cluster.

### Active `mongos` Instances

**`sh.status.active-mongoses`**

If `verbose` is `false`, `sh.status.active-mongoses` lists
the version and count of the active `mongos` instances.
Active `mongos` instances are `mongos`
instances that have been pinged within the last 60 seconds.

If `verbose` is `true`, `sh.status.active-mongoses` returns
a document for each active `mongos` instance containing
the following fields:

* - Field
  - Data Type
  - Description

* - `_id`
  - String
  - The hostname and port where the
    `mongos` is running. The `_id` is formatted as
    `<hostname>:<port>`.

* - `advisoryHostFQDNs`
  - Array of strings
  - Array of the `mongos`'s fully qualified domain
    names (FQDNs).

* - `created`
  - Date
  - When the `mongos` was started.

    **New in version:** 5.2

* - `mongoVersion`
  - String
  - Version of MongoDB that the `mongos` is running.

* - `ping`
  - Date
  - `mongos` instances send pings to the
    config server every 30
    seconds. This field indicates the last ping time.

* - `up`
  - NumberLong
  - Number of seconds the `mongos` has been up as of
    the last ping.

* - `waiting`
  - Boolean
  - This field is always `true` and is only included for backward 
    compatibility.

```javascript
active mongoses:

{ 
   "_id" : "<hostname:port>", 
   "advisoryHostFQDNs" : [ "<name>" ],
   "created" : <ISODate>,
   "mongoVersion" : <string>,
   "ping" : <ISODate>,
   "up" : <long>,
   "waiting" : <boolean>
}
...
```

### Autosplit

**`sh.status.autosplit`**

`sh.status.autosplit` indicates whether autosplit is
currently enabled.

**Note:**

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. 

In MongoDB versions earlier than 6.1:

- The `balancerStart` command and the
  `mongo` shell helper methods
  `sh.startBalancer()` and
  `sh.setBalancerState(true)` also
  enable auto-splitting for the sharded cluster.

  | To disable auto-splitting when the balancer is enabled, you can
    use `sh.disableAutoSplit()`.

- The `balancerStop` command and the `mongo`
  shell helper methods `sh.stopBalancer()` and
  `sh.setBalancerState(false)` also
  disable auto-splitting for the sharded cluster. 

  | To enable auto-splitting when the balancer is disabled, you can
    use `sh.enableAutoSplit()`.

The `mongo` methods
`sh.enableBalancing(namespace)` and
`sh.disableBalancing(namespace)` have no affect on the
auto-splitting.

### Automerge

**`sh.status.automerge`**

Indicates whether the AutoMerger is enabled.

**Note:**

The `automerge` section only appears if you explicitly enable or
disable the AutoMerger. By default, the
AutoMerger is enabled.

### Shards

**`sh.status.shards._id`**

The `_id` displays the name of the shard.

**`sh.status.shards.host`**

The `host` displays the host location
of the shard.

**`sh.status.shards.tags`**

The `tags` displays all the tags for
the shard. The field only displays if the shard has tags.

**`sh.status.shards.state`**

The `state` displays:

- `0` if the shard is not shard aware.

- `1` if the shard is shard aware.

### Balancer

**Note:**

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. 

In MongoDB versions earlier than 6.1:

- The `balancerStart` command and the
  `mongo` shell helper methods
  `sh.startBalancer()` and
  `sh.setBalancerState(true)` also
  enable auto-splitting for the sharded cluster.

  | To disable auto-splitting when the balancer is enabled, you can
    use `sh.disableAutoSplit()`.

- The `balancerStop` command and the `mongo`
  shell helper methods `sh.stopBalancer()` and
  `sh.setBalancerState(false)` also
  disable auto-splitting for the sharded cluster. 

  | To enable auto-splitting when the balancer is disabled, you can
    use `sh.enableAutoSplit()`.

The `mongo` methods
`sh.enableBalancing(namespace)` and
`sh.disableBalancing(namespace)` have no affect on the
auto-splitting.

**`sh.status.balancer.currently-enabled`**

`currently-enabled` indicates if the
balancer is currently enabled on the sharded cluster.

**`sh.status.balancer.currently-running`**

`currently-running` indicates whether
the balancer is currently running, and therefore currently
balancing the cluster.

**`sh.status.balancer.collections-with-active-migrations`**

`collections-with-active-migrations`
lists the names of any collections with active migrations, and
specifies when the migration began. If there are no active
migrations, this field will not appear in the `sh.status()`
output.

**`sh.status.balancer.failed-balancer-rounds-in-last-5-attempts`**

`failed-balancer-rounds-in-last-5-attempts`
displays the number of balancer rounds that failed, from among
the last five attempted rounds. A balancer round will fail when a chunk
migration fails.

**`sh.status.balancer.last-reported-error`**

`last-reported-error` lists the most
recent balancer error message. If there have been no errors, this
field will not appear in the `sh.status()` output.

**`sh.status.balancer.time-of-reported-error`**

`time-of-reported-error` provides
the date and time of the most recently-reported error.

**`sh.status.balancer.migration-results-for-the-last-24-hours`**

`migration-results-for-the-last-24-hours`
displays the number of migrations in the last 24 hours, and the
error messages from failed
migrations . If there have been no recent migrations,
`migration-results-for-the-last-24-hours`
displays `No recent migrations`.

`migration-results-for-the-last-24-hours`
includes *all* migrations, including those not initiated by the balancer.

### Databases

**`sh.status.databases._id`**

The `_id` displays the name of the database.

**`sh.status.databases.partitioned`**

Starting in MongoDB 6.0 and feature compatibility version (fCV) 6.0, the `partitioned` flag only maintains backward
compatibility with previous versions. By default, all databases are
enabled for sharding regardless of the `partitioned` value.

**`sh.status.databases.primary`**

The `primary` displays the
primary shard for the database.

**`sh.status.databases.version`**

The `version` displays the
version information for the database:

```bash
{  "uuid" : UUID("cc250b66-8638-49f7-a2e8-c6f1220b9d7a"),  "lastMod" : 1 } 
```

where:

- `uuid` is the database identifier.

- `lastMod` is the database version.

### Sharded Collection

**`sh.status.databases.<collection>.shard-key`**

The `shard-key` displays the shard
key specification document.

**`sh.status.databases.<collection>.unique`**

The `unique` displays
whether MongoDB enforces uniqueness on the shard key values (i.e.
whether the underlying shard key index is unique).

**`sh.status.databases.<collection>.balancing`**

Displays whether the balancer can balance the collection. If the balancer is
enabled and this status returns `true`, the balancer includes this collection
in balancing operations. If the status returns `false`, it indicates that
the balancer does **not** balance data in this collection.

**`sh.status.databases.<collection>.allowMigrations`**

Displays whether migrations are allowed for the collection. When `true`,
the collection allows migrations. When `false`, the 
collection does not allow migrations, preventing chunk migrations for this
collection. Use `sh.enableMigrations()` and 
`sh.disableMigrations()` to control this setting.

**`sh.status.databases.<collection>.chunks`**

The `chunks` lists all the shards
and the number of chunks that reside on each shard.

**`sh.status.databases.<collection>.chunk-details`**

The `chunk-details` lists the details
of the chunks [#chunk-details]_:

- The range of shard key values that define the chunk,

- The shard where the chunk resides, and

- The last modified timestamp for the chunk.

**`sh.status.databases.<collection>.tag`**

The `tag` lists the details of
the tags associated with a range of shard key values.

### Sharded Data Distribution

**`sh.status.shardedDataDistribution`**

An array of documents that provides data distribution metrics for
each sharded collection in the cluster. The data is the same as
the output of the `$shardedDataDistribution` aggregation
stage.

**`sh.status.shardedDataDistribution.ns`**

The namespace of the sharded collection in
`<database>.<collection>` format.

**`sh.status.shardedDataDistribution.shards`**

An array of documents that reports data distribution metrics for
each shard.

**`sh.status.shardedDataDistribution.shards.shardName`**

The name of the shard.

**`sh.status.shardedDataDistribution.shards.numOrphanedDocs`**

The number of orphaned documents in the shard.

**`sh.status.shardedDataDistribution.shards.numOwnedDocuments`**

The number of documents owned by the shard.

**`sh.status.shardedDataDistribution.shards.ownedSizeBytes`**

The estimated size in bytes of documents owned by the shard when
the documents are uncompressed.

**`sh.status.shardedDataDistribution.shards.orphanedSizeBytes`**

The estimated size in bytes of orphaned documents in the shard
when the documents are uncompressed.

**See also:**

`sh.balancerCollectionStatus()`
