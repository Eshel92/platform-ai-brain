<!-- Converted from reference/operator/aggregation/planCacheStats.txt (reStructuredText). Includes are inlined. -->

# $planCacheStats

## Definition

**`$planCacheStats`**

Returns plan cache information for a
collection. The stage returns a document for each plan cache entry.

The `$planCacheStats` stage must be the first stage in the
pipeline. The stage takes an empty document as a parameter and has
the following syntax:

```javascript
{ $planCacheStats: { } }
```

**See also:**

query-plans-query-optimization 

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

### Redaction

When using Queryable Encryption, the
`$planCacheStats` stage omits operations against encrypted collections, even though the operations are cached as normal.

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

**Changed in version:** 7.0

The output of `$planCacheStats` depends on the query engine used to
complete the query. The value of the `version` field of the
`$planCacheStats` indicates which query engine was used:

- `1` indicates that the classic engine was used.

- `2` indicates that the slot-based query execution engine was used.

**Note:**

Starting in version 7.0.17, the slot-based query execution engine is no longer
enabled by default for patch versions of 7.0. If you want 
your queries to use the slot-based query execution engine, please upgrade to 
version 8.0, where it is enabled by default.

**classic-sample-output:**

For queries that use the classic execution engine,
`$planCacheStats` returns a document similar to the following:

```none
{
   "version" : 1,
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
         "executionTimeMillisEstimate" : <num>,
         "totalKeysExamined" : <num>,
         "totalDocsExamined" :<num>,
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
   "estimatedSizeBytes" : <num>,
   "host" : <string>,
   "shard" : <string>
}
```

Each document includes various query plan and execution stats,
including:

* - Field
  - Description

* - `version`

  - .. _planCacheStats-classic-version:

    A number that indicates the query engine used to complete the query.

    - `1` indicates that the classic engine was used.

    - `2` indicates that the slot-based query execution engine was used.

* - `createdFromQuery`

  - .. _plancachestats-createdFromQuery:

    A document that contains the specific query that resulted in
    this cache entry. For example:

    ```javascript
    {
      "query" : <document>,
      "sort" : <document>,
      "projection" : <document>
    }
    ```

* - `isActive`

  - .. include:: /includes/planCacheStats/isActive.rst

* - `queryHash`

  - .. _plancachestats-queryHash:

    A hexadecimal string that represents the hash of the query
    shape. See `explain.queryPlanner.queryHash`.

* - `planCacheKey`

  - .. _plancachestats-planCacheKey:

    A hexadecimal string that represents the hash of the key used to find
    the plan cache entry associated with this query. The plan cache key is a
    function of both the query shape and the currently available indexes for
    that shape. See `explain.queryPlanner.planCacheKey`.

* - `cachedPlan`

  - .. _plancachestats-cachedPlan:

    The details of the cached plan. The fields included in the
    `cachedPlan` vary based on whether the query was completed using the
    classic engine or the slot-based query execution engine. For more information on query plans, see
    `explain.queryPlanner`.

* - `works`

  - .. include:: /includes/planCacheStats/works.rst

* - `timeOfCreation`
  - Time of creation for the entry.

* - `creationExecStats`

  - .. _plancachestats-creationExecStats:

    An array of execution stats documents. The array contains a
    document for each candidate plan.

    For details on the execution stats, see
    `explain.executionStats`.

* - `candidatePlanScores`

  - .. _plancachestats-candidatePlanScores:

    An array of scores for the candidate plans listed in the
    `creationExecStats` array.

* - `indexFilterSet`

  - .. include:: /includes/planCacheStats/indexFilterSet.rst

* - `estimatedSizeBytes`

  - .. include:: /includes/planCacheStats/estimatedSizeBytes.rst

* - `host`

  - .. _plancachestats-host:

    The hostname and port of the `mongod` instance from which
    the plan cache information was returned.

    When run on a sharded cluster, the operation returns plan cache entry
    information from a single member in each shard replica set. This member
    is identified with the shard and
    host fields. See also
    plancachestats-read-pref.

* - `shard`

  - .. _plancachestats-shard:

    The name of the shard from which `$planCacheStats`
    retrieved the cache entry.

    Only available if run on a sharded cluster.

**sbe-sample-output:**

For queries that use the slot-based query execution engine, `$planCacheStats` returns a
document similar to the following:

```none
{
   "version" : 2,
   "queryHash" : <hexadecimal string>,
   "planCacheKey" : <hexadecimal string>,
   "isActive" :  <boolean>,
   "works" : <NumberLong>,
   "cachedPlan" : {
      "slots" : <string>,
      "stages": <string>
   },
   "indexFilterSet" : <boolean>,
   "estimatedSizeBytes" : <num>,
   "host" : <string>
}
```

Each document includes various query plan and execution stats,
including:

* - Field
  - Description

* - `version`

  - .. _planCacheStats-sbe-version:

    A number that indicates the query engine used to complete the query.

    - `1` indicates that the classic engine was used.

    - `2` indicates that the slot-based query execution engine was used.

* - `queryHash`

  - .. _plancachestats-sbe-queryHash:

    A hexadecimal string that represents the hash of the query
    shape. See `explain.queryPlanner.queryHash`.

* - `planCacheKey`

  - .. _plancachestats-sbe-planCacheKey:

    A hexadecimal string that represents the hash of the key used to find
    the plan cache entry associated with this query. The plan cache key is a
    function of both the query shape and the currently available indexes for
    that shape. See `explain.queryPlanner.planCacheKey`.

* - `isActive`

  - .. _plancachestats-sbe-isActive:

    A boolean that indicates whether the entry is active or inactive.

    - If active, the query planner is currently using the entry to generate
      query plans.

    - If inactive, the query planner is not currently using the entry to
      generate query plans.

    See cache-entry-state.

* - `works`

  - .. _plancachestats-sbe-works:

    The number of "work units" performed by the query execution plan during
    the trial period when the query planner evaluates candidate plans. For
    more information, see
    `explain.executionStats.executionStages.works`.

* - `cachedPlan`

  - .. _plancachestats-sbe-cachedPlan:

    The details of the cached plan. The fields included in the
    `cachedPlan` vary based on whether the query was completed using the
    classic engine or the slot-based query execution engine. For more information on query plans, see
    `explain.queryPlanner`.

* - `indexFilterSet`

  - .. _plancachestats-sbe-indexFilterSet:

    A boolean that indicates whether an index filter exists for the query shape.

* - `estimatedSizeBytes`

  - .. _plancachestats-sbe-estimatedSizeBytes:

    The estimated size in bytes of a plan cache entry.

* - `host`

  - .. _plancachestats-sbe-host:

    The hostname and port of the `mongod` instance from which
    the plan cache information was returned.

    When run on a sharded cluster, the operation returns plan cache entry
    information from a single member in each shard replica set. This member
    is identified with the shard and
    host fields. See also
    plancachestats-read-pref.

## Examples

**shell:**

The examples in this section use the following `orders` collection:

```javascript
db.orders.insertMany( [
    { "_id" : 1, "item" : "abc", "price" : Decimal128("12"), "quantity" : 2, "type": "apparel" },
    { "_id" : 2, "item" : "jkl", "price" : Decimal128("20"), "quantity" : 1, "type": "electronics" },
    { "_id" : 3, "item" : "abc", "price" : Decimal128("10"), "quantity" : 5, "type": "apparel" },
    { "_id" : 4, "item" : "abc", "price" : Decimal128("8"), "quantity" : 10, "type": "apparel" },
    { "_id" : 5, "item" : "jkl", "price" : Decimal128("15"), "quantity" : 15, "type": "electronics" }
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
    { partialFilterExpression: { price: { $gte: Decimal128("10")} } }
);
```

**Note:**

Index `{ item: 1, price: 1 }` is a partial index and only indexes documents with `price`
field greater than or equal to `Decimal128("10")`.

Run some queries against the collection:

```javascript
db.orders.find( { item: "abc", price: { $gte: Decimal128("10") } } )
db.orders.find( { item: "abc", price: { $gte: Decimal128("5") } } )
db.orders.find( { quantity: { $gte: 20 } } )
db.orders.find( { quantity: { $gte: 5 }, type: "apparel" } )
```

The preceding queries are completed using the slot-based query execution engine.

### Return Information for All Entries in the Query Cache

The following aggregation pipeline uses `$planCacheStats` to return
information about the plan cache entries for the collection:

```javascript
db.orders.aggregate( [ 
    { $planCacheStats: { } }
] )
```

Output:

```javascript
[
  {                                             // Plan Cache Entry 1
    version: '2',
    planCacheShapeHash: '478AD696',
    planCacheKey: '21AE23AD',
    isActive: true,
    works: Long("7"),
    timeOfCreation: ISODate("2023-05-22T20:33:49.031Z"),
    cachedPlan: {
      ...
    },
    indexFilterSet: false,
    isPinned: false,
    estimatedSizeBytes: Long("8194"),
    host: 'mongodb1.example.net:27018'
  },
  {                                             // Plan Cache Entry 2
        version: '2',
        planCacheShapeHash: '3D8AFDC6',
        planCacheKey: '1C2C4360',
        isActive: true,
        works: Long("6"),
        timeOfCreation: ISODate("2023-05-22T20:33:50.584Z"),
        cachedPlan: {
          ...
        },
        indexFilterSet: false,
        isPinned: false,
        estimatedSizeBytes: Long("11547"),
        host: 'mongodb1.example.net:27018'
      },
      {                                          // Plan Cache Entry 3
        version: '2',
        planCacheShapeHash: '27285F9B',
        planCacheKey: '20BB9404',
        isActive: true,
        works: Long("1"),
        timeOfCreation: ISODate("2023-05-22T20:33:49.051Z"),
        cachedPlan: {
          ...
        },
        indexFilterSet: false,
        isPinned: false,
        estimatedSizeBytes: Long("7406"),
        host: 'mongodb1.example.net:27018'
      },
      {                                          // Plan Cache Entry 4
        version: '2',
        planCacheShapeHash: '478AD696',
        planCacheKey: 'B1435201',
        isActive: true,
        works: Long("5"),
        timeOfCreation: ISODate("2023-05-22T20:33:49.009Z"),
        cachedPlan: {
          ...
        },
        indexFilterSet: false,
        isPinned: false,
        estimatedSizeBytes: Long("7415"),
        host: 'mongodb1.example.net:27018'
      }
```

See also plan-cache-key. 

### Find Cache Entry Details for a Query Hash

To return plan cache information for a particular query hash, the
`$planCacheStats` stage can be followed by a
`$match` on the `planCacheKey` field.

The following aggregation pipeline uses `$planCacheStats`
followed by a `$match` stage to return specific information
for a particular query hash:

```javascript
db.orders.aggregate( [
    { $planCacheStats: { } },
    { $match: { planCacheKey: "B1435201"} }
] )
```

Output:

```javascript
[
  {
    version: '2',
    planCacheShapeHash: '478AD696',
    planCacheKey: 'B1435201',
    isActive: true,
    works: Long("5"),
    timeOfCreation: ISODate("2023-05-22T20:33:49.009Z"),
    cachedPlan: {
      slots: '$$RESULT=s11 env: { s3 = 1684787629009 (NOW), s6 = Nothing, s5 = Nothing, s1 = TimeZoneDatabase(Asia/Kuwait...Etc/UCT) (timeZoneDB), s10 = {"item" : 1, "price" : 1}, s2 = Nothing (SEARCH_META) }',
      stages: '[2] nlj inner [] [s4, s7, s8, s9, s10] \n' +
        '    left \n' +
        '        [1] cfilter {(exists(s5) && exists(s6))} \n' +
        '        [1] ixseek s5 s6 s9 s4 s7 s8 [] @"358822b7-c129-47b7-ad7f-40017a51b03c" @"item_1_price_1" true \n' +
        '    right \n' +
        '        [2] limit 1 \n' +
        '        [2] seek s4 s11 s12 s7 s8 s9 s10 none none [] @"358822b7-c129-47b7-ad7f-40017a51b03c" true false \n'
    },
    indexFilterSet: false,
    isPinned: false,
    estimatedSizeBytes: Long("7415"),
    host: 'mongodb1.example.net:27018'
  }
]
```

See also plan-cache-key and query-hash.

**nodejs:**

To use the MongoDB Node.js driver to add a `$planCacheStats` stage to an aggregation
pipeline, use the `$planCacheStats` operator in a pipeline object.

### Return Information for All Entries in the Query Cache

The following example creates a pipeline stage that returns information about the plan cache entries for the collection. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $planCacheStats: {} }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

### Find Cache Entry Details for a Query Hash

To return plan cache information for a particular query hash, include a
`$match` stage that checks for a specific query hash in the
`planCacheKey` field.

The following example creates a pipeline that returns information for a
query hash value of `"B1435201"`. The example then runs the aggregation
pipeline:

```javascript
 const pipeline = [
{ $planCacheStats: {} },
   { $match: { planCacheKey: "B1435201"} }
 ];

 const cursor = collection.aggregate(pipeline);
 return cursor;
```
