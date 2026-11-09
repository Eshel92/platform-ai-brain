<!-- Converted from reference/command/configureQueryAnalyzer.txt (reStructuredText). Includes are inlined. -->

# configureQueryAnalyzer (database command)

## Definition

**`configureQueryAnalyzer`**

**New in version:** 7.0

Configures query sampling for a collection on a replica set or
sharded cluster. Sampled queries provide information to
`analyzeShardKey` to calculate metrics about read and 
write distribution of a shard key.

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
     configureQueryAnalyzer: <string>,
     mode: <string>,
     samplesPerSecond: <double>
   } 
)
```

### Command Fields

`configureQueryAnalyzer` has the following fields:

* - Field
  - Type
  - Necessity
  - Description

* - `configureQueryAnalyzer`
  - string
  - Required
  - namespace of the collection to configure for query
    sampling.

* - `mode`
  - string
  - Required
  - Mode the query analyzer runs in. Must be set to either
    `"full"` or `"off"`.

* - `samplesPerSecond`
  - double
  - Optional
  - Number of samples per second.

    - When `mode` is set to `"full"`, `samplesPerSecond` must
      be set between `0` and `50`.
    - When `mode` is set to `"off"`, the server ignores
      `samplesPerSecond`.

    For details, see samplesPerSecond Upper Limit.

## Access Control

`configureQueryAnalyzer` requires one of the following roles:

- `dbAdmin` role against the database that contains the 
  collection being analyzed 
- `clusterManager` role against the cluster

## Behavior

Consider the following behavior when running `configureQueryAnalyzer`:

### Dropped Collections and Renamed Collections

Query sampling is disabled automatically when the collection is dropped 
or renamed. If you want to sample queries after a collection is 
recreated or renamed, you must reconfigure query sampling.

### Conversion to Sharded Cluster

If you have query analysis running on a replica set and you
convert it to a sharded cluster with a dedicated config server,
it stops query analysis.

### samplesPerSeconds Upper Limit

The upper limit for `samplesPerSecond` is `50`. A higher rate 
causes the sampled queries to fill up 10GB of disk space in less than 
four days.

This table shows the estimated disk usage for each sample rate and 
duration combination: 

| Average Sampled Query Size (kB) | `samplesPerSecond` | Sampling Duration (Days) | Number of Sampled Queries | Total Size of Sampled Queries (GB) |
|---|---|---|---|---|
| 0.5 | 0.1 | 7 | 60,480 | 0.03024 |
| 0.5 | 10 | 7 | 6,048,000 | 3.024 |
| 0.5 | 50 | 7 | 30,240,000 | 15.12 |
| 1000 | 50 | 1 | 4,320,000 | 4320 |
| 16,000 | 50 | 1 | 4,320,000 | 69,120 |

### queryAnalysisSampleExpirationSecs

Sampled queries are stored in an internal collection that has a TTL
index with `expireAfterSeconds`. To configure `expireAfterSeconds`,
use the `queryAnalysisSampleExpirationSecs` server parameter.
Sampled queries are automatically deleted after
`queryAnalysisSampleExpirationSecs`.

### Query Sampling Progress

To monitor the query sampling process, use the `$currentOp`
stage. For an example, see sampled-queries-currentOp-stage.

### View Sampled Queries

To see sampled queries for all collections or a specific collection, use
the `$listSampledQueries` aggregation stage.

To see the count of every command type captured by the query analyzer, use:

```javascript
db.getSiblingDB("admin").aggregate( [
  { "$listSampledQueries": { ns: "<db.collectionName>" } },
  {
    "$group": {
      "_id": {
        ns: "$ns",
        cmdName: "$cmdName"
      },
      count: { "$sum": 1 }
    }
  },
  {
   "$project": {
     "_id.ns": 1,
      "_id.cmdName": 1,
      "count": 1 // Explicitly include fields to output
    }
  },
  { "$sort": { "_id.ns": 1 } }
] );
```

Output:

```javascript
[{ count: 10, cmdName: 'aggregate' },
  { count: 51, cmdName: 'delete' },
  { count: 25, cmdName: 'distinct' },
  { count: 100, cmdName: 'find' },
  { count: 24, cmdName: 'findAndModify' },
  { count: 7, cmdName: 'update' }]
```

When you have enough samples, you can disable the query analyzer.

### Limitations

- You cannot run `configureQueryAnalyzer` on Atlas 
  flex clusters.
- You cannot run `configureQueryAnalyzer` on 
  standalone deployments.
- You cannot run `configureQueryAnalyzer` directly 
  against a `--shardsvr` replica set. 
  When running on a sharded cluster, 
  `configureQueryAnalyzer` must run against a 
  `mongos`.
- You cannot run `configureQueryAnalyzer` against 
  time series collections.
- You cannot run `configureQueryAnalyzer` against 
  collections with Queryable Encryption.

## Output

`configureQueryAnalyzer` returns a document containing fields that describe the old
configuration, if one exists, and fields describing the new 
configuration. 

- `oldConfiguration`, if it exists, contains fields 
  describing the old configuration.
- `newConfiguration` contains fields describing the new
  configuration.

`configureQueryAnalyzer` returns a document similar to the following:

```none
{
   ok: 1,
   oldConfiguration: {
     mode: ...,
     samplesPerSecond: ...
   }
   newConfiguration: {
     ...
   }
}
```

## Examples

### Enable Query Sampling

To enable query sampling on the `test.students` collection at a 
rate of five samples per second, use the following command:

```javascript
db.adminCommand(
   {
     configureQueryAnalyzer: "test.students",
     mode: "full",
     samplesPerSecond: 5
   } 
)
```

### Disable Query Sampling

To disable query sampling on the `test.students` collection,
use the following command:

```javascript
db.adminCommand(
   {
     configureQueryAnalyzer: "test.students",
     mode: "off"
   } 
)
```

## Learn More

- `db.collection.configureQueryAnalyzer()`
- currentOp Query Sampling Metrics
- `$listSampledQueries`
