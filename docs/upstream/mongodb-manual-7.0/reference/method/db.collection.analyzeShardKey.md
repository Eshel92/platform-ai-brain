<!-- Converted from reference/method/db.collection.analyzeShardKey.txt (reStructuredText). Includes are inlined. -->

# db.collection.analyzeShardKey() (mongosh method)

## Definition

**`db.collection.analyzeShardKey(key, opts)`**

Calculates metrics for evaluating a shard key for an unsharded or 
sharded collection. Metrics are based on sampled queries. You
can use `configureQueryAnalyzer` to configure query
sampling on a collection.

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

## Syntax

`db.collection.analyzeShardKey()` has this syntax:

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

## Fields

| Field | Type | Necessity | Description |
|---|---|---|---|
| `key` | document | Required | Shard key to analyze. This can be a candidate shard key for an unsharded collection or sharded collection or the current shard key for a sharded collection. There is no default value. |
| `opts.keyCharacteristics` | boolean | Optional | Whether or not the metrics about the characteristics of the shard key are calculated. For details, see keyCharacteristics. Defaults to `true`. |
| `opts.readWriteDistribution` | boolean | Optional | Whether or not the metrics about the read and write distribution are calculated. For details, see readWriteDistribution. Defaults to `true`. |
| `opts.sampleRate` | double | Optional | The proportion of the documents in the collection to sample when calculating the metrics about the characteristics of the shard key. If you set `sampleRate`, you cannot set `sampleSize`. Must greater than `0`, up to and including `1`. There is no default value. |
| `opts.sampleSize` | integer | Optional | The number of documents to sample when calculating the metrics about the characteristics of the shard key. If you set `sampleSize`, you cannot set `sampleRate`. If not specified and `sampleRate` is not specified, the sample size defaults to sample size set by `analyzeShardKeyCharacteristicsDefaultSampleSize`. |

## Behavior

For behavior, see analyzeShardKey Behavior.

## Access Control

For details, see analyzeShardKey Access Control.

## Output

For sample output, see analyzeShardKey Output.

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

Below are example metrics returned by `db.collection.analyzeShardKey` method for some 
candidate shard keys, with sampled queries collected from seven days of 
workload.

**Note:**

Before you run the `db.collection.analyzeShardKey` method method, read the
supporting-indexes-ref section. If you require supporting 
indexes for the shard key you are analyzing, use the 
`db.collection.createIndex()` method to create the indexes.

### { _id: 1 } keyCharacteristics

This example uses the `db.collection.analyzeShardKey` method to provide metrics on the 
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
samples, the following code block uses the `db.collection.analyzeShardKey` method to sample
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

This `db.collection.analyzeShardKey` method provides metrics on the 
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

This `db.collection.analyzeShardKey` method provides metrics on the 
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

This `db.collection.analyzeShardKey` method provides metrics on the 
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

- `configureQueryAnalyzer`
- `refineCollectionShardKey`
- sharding-reference
- `sh.shardCollection()`
