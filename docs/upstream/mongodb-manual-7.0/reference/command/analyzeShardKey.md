<!-- Converted from reference/command/analyzeShardKey.txt (reStructuredText). Includes are inlined. -->

# analyzeShardKey (database command)

## Definition

**`analyzeShardKey`**

**New in version:** 7.0

Calculates metrics for evaluating a shard key for an unsharded or 
sharded collection. Metrics are based on sampled queries. You
can use `configureQueryAnalyzer` to configure query
sampling on a collection.

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

`analyzeShardKey` has this syntax:

```javascript
db.collection.analyzeShardKey(
   <shardKey>,
   {
     keyCharacteristics: <bool>,
     readWriteDistribution: <bool>,
     sampleRate: <double>,
     sampleSize: <int>
   }
 )
```

## Command Fields

| Field | Type | Necessity | Description |
|---|---|---|---|
| `shardKey` | document | Required | Shard key to analyze. This can be a candidate shard key for an unsharded collection or sharded collection or the current shard key for a sharded collection. There is no default value. |
| `keyCharacteristics` | boolean | Optional | Whether or not the metrics about the characteristics of the shard key are calculated. For details, see keyCharacteristics. Defaults to `true`. |
| `readWriteDistribution` | boolean | Optional | Whether or not the metrics about the read and write distribution are calculated. For details, see readWriteDistribution. Defaults to `true`. To return read and write distribution metrics for a collection using `analyzeShardKey`, you must configure the query analyzer to sample the queries run on the collection. Otherwise, `analyzeShardKey` returns the read and write distribution metrics as `0` values. To configure the query analyzer, see configureQueryAnalyzer. |
| `sampleRate` | double | Optional | The proportion of the documents in the collection to sample when calculating the metrics about the characteristics of the shard key. If you set `sampleRate`, you cannot set `sampleSize`. Must greater than `0`, up to and including `1`. There is no default value. |
| `sampleSize` | integer | Optional | The number of documents to sample when calculating the metrics about the characteristics of the shard key. If you set `sampleSize`, you cannot set `sampleRate`. If not specified and `sampleRate` is not specified, the sample size defaults to sample size set by `analyzeShardKeyCharacteristicsDefaultSampleSize`. |

 

## Behavior

`analyzeShardKey` command returns different metrics depending 
on the `keyCharacteristic` and `readWriteDistribution` values 
you specify when you run the method.

### Metrics About Shard Key Characteristics

`keyCharacteristic` consists of the metrics about the 
cardinality, frequency, and monotonicity 
of the shard key. These metrics are only returned when 
`keyCharacteristics` is true.

The metrics are calculated when `analyzeShardKey` command is run based on 
documents sampled from the collection. The calculation requires the 
shard key to have a supporting index. 
If there is no supporting index, no metrics are returned.

You can configure sampling with the `sampleRate` and
`sampleSize` fields. Both are optional, but only one can be
specified. When both `sampleRate` and `sampleSize` are
unspecified, MongoDB uses the value of the
`analyzeShardKeyCharacteristicsDefaultSampleSize`
parameter, which has a default value of 10 million.

To calculate metrics based on all documents in the collection, 
set the `sampleRate` to `1`.

### Metrics About the Read and Write Distribution

`readWriteDistribution` contains metrics about the query 
routing patterns and the hotness of shard key ranges. These 
metrics are based on sampled queries.

To configure query sampling for a collection, use the
`configureQueryAnalyzer` command. The read and write distribution
metrics are only returned if `readWriteDistribution` is `true`. The
metrics are calculated when `analyzeShardKey` command is run and the metrics use
the sampled read and write queries. If there are no sampled queries,
read and write distribution metrics aren't returned.

- If there are no sampled read queries, the command returns
  `writeDistribution` but omits `readDistribution`.

- If there are no sampled write queries, the command returns
  `readDistribution` but omits `writeDistribution`.

To return read and write distribution metrics for a collection using
`analyzeShardKey`, you must configure the query
analyzer to sample the queries run on the collection. Otherwise,
`analyzeShardKey` returns the read and write distribution metrics as
`0` values. To configure the query analyzer, see
configureQueryAnalyzer.

* - `keyCharacteristics` Value
  - `readWriteDistribution` Value 
  - Results Returned

* - `true`
  - `false`
  -
    - `analyzeShardKey` command returns 
      keyCharacteristics metrics and 
      omits readWriteDistribution
      metrics.

    - If the shard key doesn't have a |suppindx|, 
      `analyzeShardKey` command returns an 
      `IllegalOperation` error.

* - `false`
  - `true`
  - `analyzeShardKey` command returns `readWriteDistribution` metrics 
    and omits `keyCharacteristics` metrics.

* - `true`
  - `true`
  - 
    - `analyzeShardKey` command returns both `readWriteDistribution` 
      metrics and `keyCharacteristics` metrics.

    - If the shard key doesn't have a supporting index, 
      `analyzeShardKey` command returns `readWriteDistribution` metrics 
      and omits `keyCharacteristics` metrics.

### Non-Blocking Behavior

`analyzeShardKey` command does not block reads or writes to the 
collection.

### Query Sampling

The quality of the metrics about the read and write distribution is
determined by how representative the workload is when query sampling 
occurs. For some applications, returning representative metrics may 
require leaving query sampling on for several days.

### Supporting Indexes

The supporting index required by `analyzeShardKey` command
is different from the supporting index required by the 
`shardCollection` command. 

This table shows the supporting indexes for the same shard key for both 
`analyzeShardKey` command and `shardCollection`:

* - Command
  - Shard Key
  - Supporting Indexes

* - `analyzeShardKey` command
  -  `{ a.x: 1, b: "hashed" }`
  - 
    - `{ a.x: 1, b: 1, ... }`
    - `{ a.x: "hashed", b: 1, ... }` 
    - `{ a.x: 1, b: "hashed", ... }`
    - `{ a.x: "hashed", b: "hashed", ...}` 

* - `shardCollection`
  - `{ a.x: 1, b: "hashed" }`
  - `{ a.x: 1, b: “hashed”, ... }`

This allows you to analyze a shard key that may not yet have a 
supporting index required for sharding it. 

Both `analyzeShardKey` command and `shardCollection` have the following
index requirements:

- Index has a simple collation 
- Index is not multi-key
- Index is not sparse
- Index is not partial

To create supporting indexes, use the
`db.collection.createIndex()` method.

### Read Preference

To minimize the performance, run `analyzeShardKey` command with the 
`secondary` or `secondaryPreferred` read preference. 
On a sharded cluster, `mongos` automatically sets the read preference 
to `secondaryPreferred` if not specified.

### Limitations

- You cannot run `analyzeShardKey` command on Atlas
  flex clusters.
- You cannot run `analyzeShardKey` command on standalone deployments.
- You cannot run `analyzeShardKey` command directly against a
  `--shardsvr` replica set.
  When running on a sharded cluster, `analyzeShardKey` command
  must run against a `mongos`.
- You cannot run `analyzeShardKey` command against
  time series collections.
- You cannot run `analyzeShardKey` command against collections
  with Queryable Encryption.

## Access Control

`analyzeShardKey` command requires one of these roles:

- `enableSharding` privilege action against the collection 
  being analyzed.
- `clusterManager` role against the cluster.

## Output

`analyzeShardKey` command returns information regarding 
keyCharacteristics and readWriteDistribution.

- `keyCharacteristics` provides metrics about the cardinality, 
  frequency, and monotonicity of the shard key.
- `readWriteDistribution` provides metrics about query routing 
  patterns and the hotness of shard key ranges.

### keyCharacteristics

This is the structure of the `keyCharacteristics` document that is
returned when `keyCharacteristics` is set to `true`:

```javascript
{
   keyCharacteristics: {
      numDocsTotal: <integer>,
      numOrphanDocs: <integer>, 
      avgDocSizeBytes: <integer>,
      numDocsSampled: <integer>,
      isUnique: <bool>,
      numDistinctValues: <integer>,
      mostCommonValues: [
        { value: <shardkeyValue>, frequency: <integer> },
        ...
      ],
      monotonicity: {
        recordIdCorrelationCoefficient: <double>,
        type: "monotonic"|"not monotonic"|"unknown",
    }
  }
}
```

* - Field
  - Type
  - Description
  - Usage    

* - `numDocsTotal`
  - integer
  - The number of documents in the collection.
  - 

* - `numOrphanDocs`
  - integer
  - The number of orphan documents.
  - Orphan documents are not excluded from metrics calculation for 
    performance reasons. If `numOrphanDocs` is large relative 
    to `numDocsTotal`, consider waiting until the number of orphan 
    documents is very small compared to the total number of documents 
    in the collection to run the command.

* - `avgDocSizeBytes`
  - integer
  - The average size of documents in the collection, in bytes.
  - If `numDocsTotal` is comparable to `numDocsSampled`, you can
    estimate the size of the largest chunks by multiplying the 
    `frequency` of each `mostCommonValues` by 
    `avgDocSizeBytes`.

* - `numDocsSampled`
  - integer
  - The number of sampled documents.
  - 

* - `numDistinctValues`
  - integer
  - The number of distinct shard key values.
  - Choose a shard key with a large `numDistinctValues` since the 
    number of distinct shard key values is the maximum number of 
    chunks that the balancer can create.

* - `isUnique`
  - boolean
  - Indicates whether the shard key is unique. This is only set to 
    `true` if there is a unique index for the shard key.
  - If the shard key is unique, then the number of distinct values 
    is equal to the number of documents. 

* - `mostCommonValues`
  - array of documents
  - An array of value and `frequency` (number of documents) of 
    the top most common shard key values.
  - The frequency of a shard key value is the minimum number of 
    documents in the chunk containing that value. If the frequency 
    is large, then the chunk can become a bottleneck for storage, 
    reads and writes. Choose a shard key where the frequency for 
    each most common value is low relative to `numDocsSampled`.  

    The number of most common shard key values can be configured
    by setting `analyzeShardKeyNumMostCommonValues` which defaults 
    to `5`. To avoid exceeding the 16MB BSON size limit for the 
    response, each value is set to "truncated" if its size exceeds 
    15MB / 
    analyzeShardKey
    NumMostCommonValues.

* - `mostCommonValues[n].value`
  - document
  - The shard key.
  - 

* - `mostCommonValues[n].frequency`
  - integer
  - The number of documents for a given shard key.
  - Choose a shard key where the frequency for each most common 
    value is low relative to `numDocsSampled`.

* - `monotonicity.`
    `recordIdCorrelationCoefficient`
  - double
  - Only set if the monotonicity is known.
  - This is set to `"unknown"` when the one of the following is
    true:

    - The shard key does not have a supporting index per 
      `shardCollection` definition.
    - The collection is clustered.
    - The shard key is a hashed compound shard key where the hashed 
      field is not the first field. 

    The monotonicity check can return an incorrect result if the 
    collection has gone through chunk migrations. Chunk migration 
    deletes documents from the donor shard and re-inserts them on 
    the recipient shard. There is no guarantee that the insertion 
    order from the client is preserved.

    You can configure the threshold for the correlation coefficient 
    with 
    analyzeShardKeyMonotonicity
    CorrelationCoefficientThreshold.

* - `monotoncity.type`
  - string
  - Can be one of: 

    `"monotonic"`,
    `"not monotonic"`,
    `"unknown"`
  - Avoid a shard key with type `"monotonic"` unless you do not 
    expect to insert new documents often.

    If a collection is sharded on a shard key that is monotonically 
    increasing or decreasing, new documents will be inserted onto 
    the shard that owns the `MaxKey` or `MinKey` chunk. That 
    shard can become the bottleneck for inserts and the data will 
    likely be unbalanced most of the time since the balancer will 
    need to compete with the inserts that come in. 

### readWriteDistribution

This is the structure of the document that is
returned when `readWriteDistribution` is set to `true`:

```javascript
{
   readDistribution: {
     sampleSize: {
       total: <integer>,
       find: <integer>,
       aggregate: <integer>,
       count: <integer>,
       distinct: <integer>
     },
     percentageOfSingleShardReads: <double>,
     percentageOfMultiShardReads: <double>,
     percentageOfScatterGatherReads: <double>,
     numReadsByRange: [
       <integer>,
       ...
     ]
   },
   writeDistribution: {
     sampleSize: {
       total: <integer>,
       update: <integer>,
       delete: <integer>,
       findAndModify: <integer>
     },
     percentageOfSingleShardWrites: <double>,
     percentageOfMultiShardWrites: <double>,
     percentageOfScatterGatherWrites: <double>,
     numWritesByRange: [
       <integer>,
       ...     
     ],
     percentageOfShardKeyUpdates: <double>,
     percentageOfSingleWritesWithoutShardKey: <double>,
     percentageOfMultiWritesWithoutShardKey: <double>
   }
}
```

To return read and write distribution metrics for a collection using
`analyzeShardKey`, you must configure the query
analyzer to sample the queries run on the collection. Otherwise,
`analyzeShardKey` returns the read and write distribution metrics as
`0` values. To configure the query analyzer, see
configureQueryAnalyzer.

#### readDistribution Fields

| Field | Type | Description | Usage |
|---|---|---|---|
| `sampleSize.total` | integer | Total number of sampled read queries. |  |
| `sampleSize.find` | integer | Total number of sampled `find` queries. |  |
| `sampleSize.aggregate` | integer | Total number of sampled `aggregate` queries. |  |
| `sampleSize.count` | integer | Total number of sampled `count` queries. |  |
| `sampleSize.distinct` | integer | Total number of sampled `distinct` queries. |  |
| `percentageOfSingleShardReads` | double | Percentage of reads that target a single shard, regardless of how the data is distributed. |  |
| `percentageOfMultiShardReads` | double | Percentage of reads that target multiple shards. | This category includes the reads that may target only a single shard if the data is distributed such that the values targeted by the read fall under a single shard. If the queries operate on a large amount of data, then targeting multiple shards instead of one may result in a decrease in latency due to the parallel query execution. |
| `percentageOfScatterGatherReads` | double | Percentage of reads that are scatter-gather, regardless of how the data is distributed. | Avoid a shard key with high value for this metric. While scatter-gather queries are low-impact on the shards that do not have the target data, they still have some performance impact. On a cluster with a large number of shards, scatter-gather queries perform significantly worse than queries that target a single shard. |
| `numReadsByRange` | array of integers | Array of numbers representing the number of times that each range sorted from `MinKey` to `MaxKey` is targeted. | Avoid a shard key where the distribution of `numReadsByRange` is very skewed since that implies that there is likely to be one or more hot shards for reads. Choose a shard key where the sum of `numReadsByRange` is similar to `sampleSize.total`. The number of ranges can be configured using the `analyzeShardKeyNumRanges` parameter which defaults to `100`. The value is `100` because the goal is to find a shard key that scales up to 100 shards. |

#### writeDistribution Fields

| Field | Type | Description | Usage |
|---|---|---|---|
| `sampleSize.total` | integer | Total number of sampled write queries. |  |
| `sampleSize.update` | integer | Total number of sampled `update` queries. |  |
| `sampleSize.delete` | integer | Total number of sampled `delete` queries. |  |
| `sampleSize.findAndModify` | integer | Total number of sampled `findAndModify` queries. |  |
| `percentageOfSingleShardWrites` | double | Percentage of writes that target a single shard, regardless of how the data is distributed. |  |
| `percentageOfMultiShardWrites` | double | Percentage of writes that target multiple shards. | This category includes the writes that may target only a single shard if the data is distributed such that the values targeted by the write fall under a single shard. |
| `percentageOfScatterGatherWrites` | double | Percentage of writes that are scatter-gather, regardless of how the data is distributed. | Avoid a shard key with a high value for this metric because it is generally more performant for a write to target a single shard. |
| `numWritesByRange` | array of integers | Array of numbers representing the number of times that each range sorted from `MinKey` to `MaxKey` is targeted. | Avoid a shard key where the distribution of `numWritesByRange` is a very skewed since that implies that there is likely to be one or more hot shards for writes. Choose a shard key where the sum of `numWritesByRange` is similar to `sampleSize.total`. The number of ranges can be configured using the `analyzeShardKeyNumRanges` parameter which defaults to `100`. The value is `100` because the goal is to find a shard key that scales up to 100 shards. |
| `percentageOfShardKeyUpdates` | double | Percentage of write queries that update a document’s shard key value. | Avoid a shard key with a high `percentageOfShardKeyUpdates`. Updates to a document’s shard key value may cause the document to move to a different shard, which requires executing an internal transaction on the shard that the query targets. For details on changing a document's shard key value, see change-a-shard-key. Updates are currently only supported as retryable writes or in a transaction, and have a batch size limit of `1`. |
| `percentageOfSingleWritesWithoutShardKey` | double | The percentage of write queries that are `multi=false` and not targetable to a single shard. | Avoid a shard key with a high value for this metric. Performing this type of write is expensive because they can involve running internal transactions. |
| `percentageOfMultiWritesWithoutShardKey` | double | The percentage of write queries that are `multi=true` and not targetable to a single shard. | Avoid a shard key with a high value for this metric. |

## Examples

Consider a simplified version of a social media app. The collection 
we are trying to shard is the `post` collection. 

Documents in the `post` collection have the following schema:

```javascript
{
   userId: <uuid>,
   firstName: <string>,
   lastName: <string>,
   body: <string>,  // the field that can be modified.
   date: <date>,    // the field that can be modified.
}
```

### Background Information

- The app has 1500 users.
- There are 30 last names and 45 first names, some more common than 
  others. 
- There are three celebrity users. 
- Each user follows exactly five other users and has a very high 
  probability of following at least one celebrity user.

### Sample Workload

- Each user posts about two posts a day at random times. They edit each 
  post once, right after it is posted.
- Each user logs in every six hours to read their own profile and posts 
  by the users they follow from the past 24 hours. They also reply under 
  a random post from the past three hours.
- For every user, the app removes posts that are more than three days 
  old at midnight.

### Workload Query Patterns

This workload has the following query patterns:

- `find` command with filter 
  `{ userId: , firstName: , lastName: }`
- `find` command with filter 
  ``{ $or: [ { userId: , firstName: , lastName: , date: { $gte:  } }, ... , { 
  userId: , date: } ] }``
- `findAndModify` command with filter 
  `{ userId: , firstName: , lastName: , date:  }` to 
  update the body and date field.
- `update` command with `multi: false` and filter 
  `{ userId: , firstName: , lastName: , date: { $gte: , $lt:  } }` 
  to update the body and date field.
- `delete` command with `multi: true` and filter 
  `{ userId: , firstName: , lastName: , date: { $lt:  } }`

Below are example metrics returned by `analyzeShardKey` command for some 
candidate shard keys, with sampled queries collected from seven days of 
workload.

**Note:**

Before you run `analyzeShardKey` commands, read the
supporting-indexes-ref section earlier on this page. If you
require supporting indexes for the shard key you are analyzing, use
the `db.collection.createIndex()` method to create the
indexes.

### { _id: 1 } keyCharacteristics

This example uses the `analyzeShardKey` command to provide metrics on the 
`{ _id: 1 }` shard key on the `social.post` collection.

The following code block uses
`db.collection.configureQueryAnalyzer()` to turn on query
sampling:

```javascript
use social
db.post.configureQueryAnalyzer( 
   {
      mode: "full",
      samplesPerSecond: 5
   } 
)
```

After `db.collection.configureQueryAnalyzer()` collects query
samples, the following code block uses the `analyzeShardKey` command to sample
10,000 documents and calculate results:

```javascript
use social
db.post.analyzeShardKey(
   { _id: 1 },
   {
      keyCharacteristics: true,
      readWriteDistribution: false,
      sampleSize: 10000
   }
)
```

### { lastName: 1 } keyCharacteristics

This `analyzeShardKey` command provides metrics on the 
`{ lastName: 1 }` shard key on the `social.post` collection:

```javascript
use social
db.post.analyzeShardKey(
   { lastName: 1 },
   {
      keyCharacteristics: true,
      readWriteDistribution: false
   }
)
```

The output for this example resembles the following:

```none
{
   "keyCharacteristics": {
     "numDocsTotal" : 9039,
     "avgDocSizeBytes" : 153,
     "numDocsSampled" : 9039,
     "isUnique" : false,
     "numDistinctValues" : 30,
     "mostCommonValues" : [
         {
           "value" : {
               "lastName" : "Smith"
           },
           "frequency" : 1013
         },
         {
           "value" : {
               "lastName" : "Johnson"
           },
           "frequency" : 984
         },
         {
           "value" : {
               "lastName" : "Jones"
           },
           "frequency" : 962
         },
         {
           "value" : {
               "lastName" : "Brown"
           },
           "frequency" : 925
         },
         {
           "value" : {
               "lastName" : "Davies"
           },
           "frequency" : 852
         }
     ],
     "monotonicity" : {
       "recordIdCorrelationCoefficient" : 0.0771959161,
       "type" : "not monotonic"
   },
 }
}
```

### { userId: 1 } keyCharacteristics

This `analyzeShardKey` command provides metrics on the 
`{ userId: 1 }` shard key on the `social.post` collection:

```javascript
use social
db.post.analyzeShardKey(
   { userId: 1 },
   {
      keyCharacteristics: true,
      readWriteDistribution: false
   }
)
```

The output for this example resembles the following:

```none
{
  "keyCharacteristics": {
    "numDocsTotal" : 9039,
    "avgDocSizeBytes" : 162,
    "numDocsSampled" : 9039,
    "isUnique" : false,
    "numDistinctValues" : 1495,
    "mostCommonValues" : [
      {
        "value" : {
          "userId" : UUID("aadc3943-9402-4072-aae6-ad551359c596")
        },
        "frequency" : 15
      },
     {
       "value" : {
         "userId" : UUID("681abd2b-7a27-490c-b712-e544346f8d07")
       },
       "frequency" : 14
     },
     {
       "value" : {
         "userId" : UUID("714cb722-aa27-420a-8d63-0d5db962390d")
       },
       "frequency" : 14
     },
     {
       "value" : {
         "userId" : UUID("019a4118-b0d3-41d5-9c0a-764338b7e9d1")
       },
       "frequency" : 14
     },
     {
       "value" : {
         "userId" : UUID("b9c9fbea-3c12-41aa-bc69-eb316047a790")
       },
       "frequency" : 14
     }
   ],
   "monotonicity" : {
     "recordIdCorrelationCoefficient" : -0.0032039729,
     "type" : "not monotonic"
   },
 }
}
```

### { userId: 1 } readWriteDistribution

This `analyzeShardKey` command provides metrics on the 
`{ userId: 1 }` shard key on the `social.post` collection:

```javascript
use social
db.post.analyzeShardKey(
   { userId: 1 },
   {
      keyCharacteristics: false,
      readWriteDistribution: true
   }
)
```

The output for this example resembles the following:

```none
{
   "readDistribution" : {
     "sampleSize" : {
       "total" : 61363,
       "find" : 61363,
       "aggregate" : 0,
       "count" : 0,
       "distinct" : 0
     },
     "percentageOfSingleShardReads" : 50.0008148233,
     "percentageOfMultiShardReads" : 49.9991851768,
     "percentageOfScatterGatherReads" : 0,
     "numReadsByRange" : [
       688,
       775,
       737,
       776,
       652,
       671,
       1332,
       1407,
       535,
       428,
       985,
       573,
       1496,
       ...
       ],
     },
   "writeDistribution" : {
     "sampleSize" : {
       "total" : 49638,
       "update" : 30680,
       "delete" : 7500,
       "findAndModify" : 11458
     },
     "percentageOfSingleShardWrites" : 100,
     "percentageOfMultiShardWrites" : 0,
     "percentageOfScatterGatherWrites" : 0,
     "numWritesByRange" : [
       389,
       601,
       430,
       454,
       462,
       421,
       668,
       833,
       493,
       300,
       683,
       460,
       ...
      ],
      "percentageOfShardKeyUpdates" : 0,
      "percentageOfSingleWritesWithoutShardKey" : 0,
      "percentageOfMultiWritesWithoutShardKey" : 0
    }
}
```

## Learn More

- sharding-reference
- `sh.shardCollection()`
- `refineCollectionShardKey`
