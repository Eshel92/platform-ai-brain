<!-- Converted from reference/operator/aggregation/planCacheStats.txt (reStructuredText). Includes are inlined. -->

# $planCacheStats

## Definition

**`$planCacheStats`**

**New in version:** 4.2

Returns plan cache information for a
collection. The stage returns a document for each plan cache entry.

The `$planCacheStats` stage must be the first stage in the
pipeline. The stage takes an empty document as a parameter and has
the following syntax:

```javascript
{ $planCacheStats: { } }
```

**Note:** 4.4 Changes

Starting in version 4.4, 

- `$planCacheStats` stage can be run on
  `mongos` instances as well as on
  `mongod` instances. In 4.2,
  `$planCacheStats` stage can only run on
  `mongod` instances.

- `$planCacheStats` includes new fields: the host field and, when run against a
  `mongos`, the shard
  field.

- `mongo` shell provides the method
  `PlanCache.list()` as a wrapper for
  `$planCacheStats` aggregation stage.

- MongoDB removes the following:

  - `planCacheListPlans` and `planCacheListQueryShapes`
    commands, and

  - `PlanCache.getPlansByQuery()` and
    `PlanCache.listQueryShapes()` methods.

  Use `$planCacheStats` or `PlanCache.list()` instead.

**See also:**

/core/query-plans 

## Considerations

### Pipeline

`$planCacheStats` must be the first stage in an aggregation
pipeline.

### Restrictions

- `$planCacheStats` is not allowed in:

  - transactions

  - `$facet` aggregation stage

- `$planCacheStats` requires read concern level
  `"local"`.

### Access Control

On systems running with `authorization`, the user
must have the `planCacheRead` privilege for the collection.

### Read Preference

`$planCacheStats` observes the read preference in selecting the host(s) from which to return
the plan cache information.

Applications may target different members of a replica set. As such,
each replica set member might receive different read commands and have
plan cache information that differs from other members. Nevertheless,
running `$planCacheStats` on a replica set or a sharded
cluster obeys the normal read preference rules. That is, on a replica
set, the operation gathers plan cache information from just one member
of replica set, and on a sharded cluster, the operation gathers plan
cache information from just one member of each shard replica set.

## Output

For each plan cache entry, the `$planCacheStats` stage returns a
document similar to the following:

```javascript
{
   "createdFromQuery" : <document>,
   "queryHash" : <hexadecimal string>,
   "planCacheKey" : <hexadecimal string>,
   "isActive" :  <boolean>,
   "works" : <NumberLong>,
   "cachedPlan" : {
      "stage" : <STAGE1>,
      "filter" : <document>,
      "inputStage" : {
         "stage" : <STAGE2>,
         ...
      }
   },
   "timeOfCreation" : <date>,
   "creationExecStats" : [   // Exec Stats Document for each candidate plan
      {
         "nReturned" : <num>,
         "executionTimeMillisEstimate" : <num>
         "totalKeysExamined" : <num>
         "totalDocsExamined" :<num>
         "executionStages" : {
            "stage" : <STAGE A>,
            ...
            "inputStage" : {
               "stage" : <STAGE B>,
               ...
            }
         }
      },
      ...
   ],
   "candidatePlanScores" : [
      <number>,
      ...
   ],
   "indexFilterSet" : <boolean>,
   "estimatedSizeBytes" : <num>, // Available starting in MongoDB 5.0, 4.4.3, 4.2.12
   "host" : <string>,   // Available starting in MongoDB 4.4
   "shard" : <string>   // Available starting in MongoDB 4.4 if run on sharded cluster
}
```

Each document includes various query plan and execution stats,
including:

* - Field
  - Description

* - createdFromQuery

  - .. _plancachestats-createdFromQuery:

    A document that contains the specific query that resulted in
    this cache entry; i.e.

    ```javascript
    {
      "query" : <document>,
      "sort" : <document>,
      "projection" : <document>
    }
    ```

* - `isActive`

  - A boolean that indicates whether the entry is active or inactive.

    - If active, the query planner is currently using the entry to
      generate query plans.

    - If inactive, the query planner is not currently using the
      entry to generate query plans.

    **See also:**

    cache-entry-state

* - queryHash

  - .. _plancachestats-queryHash:

    A hexadecimal string that represents the hash of the query 
    shape. For more information, see
    `explain.queryPlanner.queryHash`

* - planCacheKey

  - .. _plancachestats-planCacheKey:

    A hexadecimal string that represents the hash of the key used to
    find the plan cache entry associated with this query. The plan
    cache key is a function of both the query shape and the
    currently available indexes for that shape. For more information, see
    `explain.queryPlanner.planCacheKey`

* - cachedPlan

  - .. _plancachestats-cachedPlan:

    The details of the cached plan. See `explain.queryPlanner`.

* - `works`

  - The number of "work units" performed by the query execution plan
    during the trial period when the query planner evaluates
    candidate plans. For more information, see
    `explain.executionStats.executionStages.works`

* - `timeOfCreation`
  - Time of creation for the entry.

* - creationExecStats

  - .. _plancachestats-creationExecStats:

    An array of execution stats documents. The array contains a
    document for each candidate plan.

    For details on the execution stats, see
    `explain.executionStats`.

* - candidatePlanScores

  - .. _plancachestats-candidatePlanScores:

    An array of scores for the candidate plans listed in the
    `creationExecStats` array.

* - `indexFilterSet`

  - A boolean that indicates whether the an index filter exists for the query shape.

* - `estimatedSizeBytes`

  - A number that describes the estimated size in bytes of a plan
    cache entry.

    **New in version:** 5.0

    Starting in MongoDB 5.0, 4.4.3, and 4.2.12, this field is available.

* - host

  - .. _plancachestats-host:

    The hostname and port of the `mongod` instance from
    which the plan cache information was returned.

    When run on a sharded cluster, the operation returns plan cache
    entry information from a single member in each shard replica
    set. This member is identified with the shard and host
    fields. See also plancachestats-read-pref.

    **New in version:** 4.4

* - shard

  - .. _plancachestats-shard:

    The name of the shard from which `$planCacheStats`
    retrieved the cache entry.

    Only available if run on a sharded cluster.

    **New in version:** 4.4

## Examples

The examples in this section use the following `orders` collection:

```javascript
db.orders.insertMany( [
   { "_id" : 1, "item" : "abc", "price" : NumberDecimal("12"), "quantity" : 2, "type": "apparel" },
   { "_id" : 2, "item" : "jkl", "price" : NumberDecimal("20"), "quantity" : 1, "type": "electronics" },
   { "_id" : 3, "item" : "abc", "price" : NumberDecimal("10"), "quantity" : 5, "type": "apparel" },
   { "_id" : 4, "item" : "abc", "price" : NumberDecimal("8"), "quantity" : 10, "type": "apparel" },
   { "_id" : 5, "item" : "jkl", "price" : NumberDecimal("15"), "quantity" : 15, "type": "electronics" }
] )
```

Create the following indexes on the collection:

```javascript
db.orders.createIndex( { item: 1 } );
db.orders.createIndex( { item: 1, quantity: 1 } );
db.orders.createIndex( { quantity: 1 } );
db.orders.createIndex( { quantity: 1, type: 1 } );
db.orders.createIndex(
   { item: 1, price: 1 },
   { partialFilterExpression: { price: { $gte: NumberDecimal("10")} } }
);
```

**Note:**

Index `{ item: 1, price: 1 }` is a partial index and only indexes documents with `price`
field greater than or equal to `NumberDecimal("10")`.

Run some queries against the collection:

```javascript
db.orders.find( { item: "abc", price: { $gte: NumberDecimal("10") } } )
db.orders.find( { item: "abc", price: { $gte: NumberDecimal("5") } } )
db.orders.find( { quantity: { $gte: 20 } } )
db.orders.find( { quantity: { $gte: 5 }, type: "apparel" } )
```

### Return Information for All Entries in the Query Cache

The following aggregation pipeline uses `$planCacheStats` to
return information on the plan cache entries for the collection:

```javascript
db.orders.aggregate( [ 
   { $planCacheStats: { } }
] )
```

The operation returns all entries in the cache:

```javascript
{                                               // Plan Cache Entry 1
   "createdFromQuery" : {
      "query" : { "quantity" : { "$gte" : 5 }, "type" : "apparel" },
      "sort" : { },
      "projection" : { }
   },
   "queryHash" : "4D151C4C",
   "planCacheKey" : "DD67E353",
   "isActive" : false,
   "works" : NumberLong(4),
   "cachedPlan" : {
      ...
   },
   "timeOfCreation" : ISODate("2020-02-06T18:15:44.849Z"),
   "creationExecStats" : [
      {
         ... // Exec Stats for Candidate 1
      },
      {
         ... // Exec Stats for Candidate 2
      }
   ],
   "candidatePlanScores" : [
      1.5002,
      1.5002
   ],
   "indexFilterSet" : false,
   "estimatedSizeBytes" : NumberLong(3160),     // Available starting in MongoDB 5.0, 4.4.3, 4.2.12
   "host" : "mongodb1.example.net:27018",       // Available starting in MongoDB 4.4
   "shard" : "shardA"                           // Available starting in MongoDB 4.4 if run on sharded cluster
}
{                                               // Plan Cache Entry 2
   "createdFromQuery" : {
      "query" : { "quantity" : { "$gte" : 20 } },
      "sort" : { },
      "projection" : { }
   },
   "queryHash" : "23B19B75",
   "planCacheKey" : "6F23F858",
   "isActive" : false,
   "works" : NumberLong(1),
   "cachedPlan" : {
      ...
   },
   "timeOfCreation" : ISODate("2020-02-06T18:15:44.454Z"),
   "creationExecStats" : [
      {
         ... // Exec Stats for Candidate 1
      },
      {
         ... // Exec Stats for Candidate 2
      }
   ],
   "candidatePlanScores" : [
      1.0002,
      1.0002
   ],
   "indexFilterSet" : false,
   "estimatedSizeBytes" : NumberLong(2539),     // Available starting in MongoDB 5.0, 4.4.3, 4.2.12
   "host" : "mongodb1.example.net:27018",       // Available starting in MongoDB 4.4
   "shard" : "shardA"                           // Available starting in MongoDB 4.4 if run on sharded cluster
}
{                                               // Plan Cache Entry 3
   "createdFromQuery" : {
      "query" : { "item" : "abc", "price" : { "$gte" : NumberDecimal("5") } },
      "sort" : { },
      "projection" : { }
   },
   "queryHash" : "117A6B10",
   "planCacheKey" : "A1824628",
   "isActive" : true,
   "works" : NumberLong(4),
   "cachedPlan" : {
      ...
   },
   "timeOfCreation" : ISODate("2020-02-06T18:15:44.452Z"),
   "creationExecStats" : [
      {
         ... // Exec Stats for Candidate 1
      },
      {
         ... // Exec Stats for Candidate 2
      }
   ],
   "candidatePlanScores" : [
      1.7502,
      1.7502
   ],
   "indexFilterSet" : false,
   "estimatedSizeBytes" : NumberLong(3183),     // Available starting in MongoDB 5.0, 4.4.3, 4.2.12
   "host" : "mongodb1.example.net:27018",       // Available starting in MongoDB 4.4
   "shard" : "shardA"                           // Available starting in MongoDB 4.4 if run on sharded cluster
}
{                                               // Plan Cache Entry 4
   "createdFromQuery" : {
      "query" : { "item" : "abc", "price" : { "$gte" : NumberDecimal("10") } },
      "sort" : { },
      "projection" : { }
   },
   "queryHash" : "117A6B10",
   "planCacheKey" : "2E6E536B",
   "isActive" : true,
   "works" : NumberLong(3),
   "cachedPlan" : {
      ...
   },
   "timeOfCreation" : ISODate("2020-02-06T18:15:44.449Z"),
   "creationExecStats" : [
      {
         ... // Exec Stats for Candidate 1
      },
      {
         ... // Exec Stats for Candidate 2
      },
      {
         ... // Exec Stats for Candidate 3
      }
   ],
   "candidatePlanScores" : [
      1.6668666666666665,
      1.6668666666666665,
      1.6668666666666665
   ],
   "indexFilterSet" : false,
   "estimatedSizeBytes" : NumberLong(4653),     // Available starting in MongoDB 5.0, 4.4.3, 4.2.12
   "host" : "mongodb1.example.net:27018",       // Available starting in MongoDB 4.4
   "shard" : "shardA"                           // Available starting in MongoDB 4.4 if run on sharded cluster
}
```

See also plan-cache-key. 

### List Query Shapes

MongoDB 4.4 removes the deprecated `planCacheListQueryShapes` command
and its helper method `PlanCache.listQueryShapes()`.

As an alternative, you can use the `$planCacheStats` stage to
obtain a list of all of the query shapes for which there is a cached
plan.

For example, the following uses the `$project` stage to only
output the `createdFromQuery` field and the `queryHash` field.

```javascript
db.orders.aggregate( [ { $planCacheStats: { } } , { $project: {createdFromQuery: 1, queryHash: 1 } } ] )
```

 
The operation returns the following query shapes:

```javascript
{ "createdFromQuery" : { "query" : { "item" : "abc", "price" : { "$gte" : NumberDecimal("5") } }, "sort" : {  }, "projection" : {  } }, "queryHash" : "117A6B10" }
{ "createdFromQuery" : { "query" : { "quantity" : { "$gte" : 5 }, "type" : "apparel" }, "sort" : {  }, "projection" : {  } }, "queryHash" : "4D151C4C" }
{ "createdFromQuery" : { "query" : { "quantity" : { "$gte" : 20 } }, "sort" : {  }, "projection" : {  } }, "queryHash" : "23B19B75" }
{ "createdFromQuery" : { "query" : { "item" : "abc", "price" : { "$gte" : NumberDecimal("10") } }, "sort" : {  }, "projection" : {  } }, "queryHash" : "117A6B10" }
```

### Find Cache Entry Details for a Query Shape

To return plan cache information for a particular query shape, the
`$planCacheStats` stage can be followed by a
`$match` on the `planCacheKey` field.

The following aggregation pipeline uses `$planCacheStats`
followed by a `$match` and `$project` to return
specific information for a particular query shape:

```javascript
db.orders.aggregate( [
   { $planCacheStats: { } },
   { $match: { planCacheKey: "DD67E353"} }
] )
```

The operation returns the following:

```javascript
{
   "createdFromQuery" : {
      "query" : { "quantity" : { "$gte" : 5 }, "type" : "apparel" },
      "sort" : { },
      "projection" : { }
   },
   "queryHash" : "4D151C4C",
   "planCacheKey" : "DD67E353",
   "isActive" : false,
   "works" : NumberLong(4),
   "cachedPlan" : {
      "stage" : "FETCH",
      "filter" : {
         "type" : {
            "$eq" : "apparel"
         }
      },
      "inputStage" : {
         "stage" : "IXSCAN",
         "keyPattern" : {
            "quantity" : 1
         },
         "indexName" : "quantity_1",
         "isMultiKey" : false,
         "multiKeyPaths" : {
            "quantity" : [ ]
         },
         "isUnique" : false,
         "isSparse" : false,
         "isPartial" : false,
         "indexVersion" : 2,
         "direction" : "forward",
         "indexBounds" : {
            "quantity" : [
               "[5.0, inf.0]"
            ]
         }
      }
   },
   "timeOfCreation" : ISODate("2020-02-06T18:15:44.849Z"),
   "creationExecStats" : [
      {
         "nReturned" : 2,
         "executionTimeMillisEstimate" : 0,
         "totalKeysExamined" : 3,
         "totalDocsExamined" : 3,
         "executionStages" : {
            "stage" : "FETCH",
            "filter" : {
               "type" : {
                  "$eq" : "apparel"
               }
            },
            "nReturned" : 2,
            "executionTimeMillisEstimate" : 0,
            "works" : 4,
            "advanced" : 2,
            "needTime" : 1,
            "needYield" : 0,
            "saveState" : 0,
            "restoreState" : 0,
            "isEOF" : 1,
            "docsExamined" : 3,
            "alreadyHasObj" : 0,
            "inputStage" : {
               "stage" : "IXSCAN",
               "nReturned" : 3,
               "executionTimeMillisEstimate" : 0,
               "works" : 4,
               "advanced" : 3,
               "needTime" : 0,
               "needYield" : 0,
               "saveState" : 0,
               "restoreState" : 0,
               "isEOF" : 1,
               "keyPattern" : {
                  "quantity" : 1
               },
               "indexName" : "quantity_1",
               "isMultiKey" : false,
               "multiKeyPaths" : {
                  "quantity" : [ ]
               },
               "isUnique" : false,
               "isSparse" : false,
               "isPartial" : false,
               "indexVersion" : 2,
               "direction" : "forward",
               "indexBounds" : {
                  "quantity" : [
                     "[5.0, inf.0]"
                  ]
               },
               "keysExamined" : 3,
               "seeks" : 1,
               "dupsTested" : 0,
               "dupsDropped" : 0
            }
         }
      },
      {
         "nReturned" : 2,
         "executionTimeMillisEstimate" : 0,
         "totalKeysExamined" : 3,
         "totalDocsExamined" : 2,
         "executionStages" : {
            "stage" : "FETCH",
            "nReturned" : 2,
            "executionTimeMillisEstimate" : 0,
            "works" : 4,
            "advanced" : 2,
            "needTime" : 1,
            "needYield" : 0,
            "saveState" : 0,
            "restoreState" : 0,
            "isEOF" : 1,
            "docsExamined" : 2,
            "alreadyHasObj" : 0,
            "inputStage" : {
               "stage" : "IXSCAN",
               "nReturned" : 2,
               "executionTimeMillisEstimate" : 0,
               "works" : 4,
               "advanced" : 2,
               "needTime" : 1,
               "needYield" : 0,
               "saveState" : 0,
               "restoreState" : 0,
               "isEOF" : 1,
               "keyPattern" : {
                  "quantity" : 1,
                  "type" : 1
               },
               "indexName" : "quantity_1_type_1",
               "isMultiKey" : false,
               "multiKeyPaths" : {
                  "quantity" : [ ],
                  "type" : [ ]
               },
               "isUnique" : false,
               "isSparse" : false,
               "isPartial" : false,
               "indexVersion" : 2,
               "direction" : "forward",
               "indexBounds" : {
                  "quantity" : [
                     "[5.0, inf.0]"
                  ],
                  "type" : [
                     "[\"apparel\", \"apparel\"]"
                  ]
               },
               "keysExamined" : 3,
               "seeks" : 2,
               "dupsTested" : 0,
               "dupsDropped" : 0
            }
         }
      }
   ],
   "candidatePlanScores" : [
      1.5002,
      1.5002
   ],
   "indexFilterSet" : false,
   "estimatedSizeBytes" : NumberLong(3160),     // Available starting in MongoDB 5.0, 4.4.3, 4.2.12
   "host" : "mongodb1.example.net:27018",       // Available starting in MongoDB 4.4
   "shard" : "shardA"                           // Available starting in MongoDB 4.4 if run on sharded cluster
}
```

See also plan-cache-key and query-hash.
