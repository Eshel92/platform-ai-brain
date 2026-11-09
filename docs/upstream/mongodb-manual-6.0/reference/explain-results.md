<!-- Converted from reference/explain-results.txt (reStructuredText). Includes are inlined. -->

# Explain Results

To return information on query plans and execution statistics of the
query plans, MongoDB provides:

- the `db.collection.explain()` method,

- the `cursor.explain()` method, and

- the `explain` command.

**Important:**

`explain` ignores the plan cache. Instead, a set 
of candidate plans are generated, and a winner is chosen without consulting 
the plan cache. Furthermore, `explain` prevents the MongoDB query planner 
from caching the winning plan.

**Note:**

Only the most important output fields are shown on this page, and fields for 
internal use are not documented. The fields listed in the output are subject 
to change.

## Explain Output Structure

The `explain` results present the query plans as a tree of stages. 
The output structure can differ based on which query engine the 
operation uses. Operations can use the classic query engine or the 
slot based execution query engine. 

**Note:**

Starting in version 6.0.18, the slot-based execution 
query engine is no longer enabled by default for 
patch versions of 6.0. If you want your queries to 
use the slot-based execution query engine, please upgrade to 
version 8.0, where it is enabled by default.

To see how the output structure can differ between the two execution 
engines, see the following examples:

tabs:

   - id: classic-sample-output
     name: "Classic Execution Engine"
     content: |

         ```javascript
         winningPlan: {
            stage: <STAGE1>,
            ...
            inputStage: {
               stage: <STAGE2>,
               ...
               inputStage: {
                  stage: <STAGE3>,
                  ...
               }
            }
         },
         ```

   - id: sbe-sample-output
     name: "Slot-based Execution Engine"
     content: |

         ```javascript
         winningPlan: {
            queryPlan: {
               stage: <STAGE1>,
               ...
               inputStage: {
                  stage: <STAGE2>,
                  ...
                  inputStage: {
                     stage: <STAGE3>,
                     ...
                  }
               }
            }
            slotBasedPlan: {
               ...  
            }
         },
         ```

Each stage passes its resulting documents or index keys to the
parent node. The leaf nodes access the collection or the indices. The
internal nodes use the documents or the index keys that result from the 
child nodes. The root node indicates the stage that MongoDB ultimately 
derives the result set from.

Stages are descriptive of the operation. For example:

- `COLLSCAN` for a collection scan

- `IXSCAN` for scanning index keys

- `FETCH` for retrieving documents

- `GROUP` for grouping documents

- `SHARD_MERGE` for merging results from shards

- `SHARDING_FILTER` for filtering out orphan documents from shards

## Explain Output for MongoDB 5.1 and Later

This section shows the `explain` output for MongoDB 5.1 and later. To 
see the explain output for older versions of MongoDB, refer to the 
documentation for that version.

**`explain.explainVersion`**

Integer field.

`explainVersion` is the output format version for the plan, such as
`"1"` or `"2"`.

**New in version:** 5.1

### `queryPlanner`

`explain.queryPlanner` information details the plan selected by
the query optimizer.

These examples may combine the output structures of MongoDB's classic
and slot-based execution engines. They are not meant to be 
representative. Your output may differ significantly.

tabs:

   - id: unsharded
     name: "Unsharded Collections"
     content: |

         For unsharded collections, `explain` returns the following
         `queryPlanner` information:

         ```javascript
         queryPlanner: {
            namespace: <string>,                                                                                                                                                                                                   
            indexFilterSet: <boolean>,                                                                                                                                                                                                      
            parsedQuery: {                                                                                                                                                                                                              
               ...                                                                                                                                                  
            },                                                                                                                                                                                                                          
            queryHash: <hexadecimal string>,                                                                                                                                                                                                      
            planCacheKey: <hexadecimal string>,                                                                                                                                                                                                   
            maxIndexedOrSolutionsReached: <boolean>,                                                                                                                                                                                        
            maxIndexedAndSolutionsReached: <boolean>,                                                                                                                                                                                       
            maxScansToExplodeReached: <boolean>,                                                                                                                                                                                            
            winningPlan: {  
              stage: <STAGE1>,
              inputStage: {
                stage: <string>,
                ...
              }
            },
            rejectedPlans: [
              <candidate plan1>,
            ]
           }                                                                                                               
         }
         ```

   - id: sharded
     name: "Sharded Collections"
     content: |
         For sharded collections, `explain` includes the core
         query planner and server information for each accessed
         shard in the `shards` field:

         ```javascript
         {
            queryPlanner: {
               mongosPlannerVersion: <int>
               winningPlan: {
                  stage: <STAGE1>,
                  shards: [
                  { 
                     shardName: <string>,
                     connectionString: <string>,
                     serverInfo: {
                        ...
                     },
                     namespace: <string>,
                     indexFilterSet: <boolean>,
                     parsedQuery: {
                        ...
                     },
                     queryHash: <hexadecimal string>,
                     planCacheKey: <hexadecimal string>,
                     maxIndexedOrSolutionsReached: <boolean>,
                     maxIndexedAndSolutionsReached: <boolean>,
                     maxScansToExplodeReached: <boolean>,
                     winningPlan: {
                        stage: <STAGE1>,
                        inputStage: {
                           stage: <string>,
                           ...
                        }
                     },
                     rejectedPlans: [
                       <candidate plan1>,
                     ] 
                  }
                  ]
               }
            }
         }
         ```

**`explain.queryPlanner`**

Contains information on the selection of the query plan by the
query optimizer.

**`explain.queryPlanner.namespace`**

A string that specifies the namespace with the names of
the database and the collection accessed by the query. The
namespace has the format `<database>.<collection>`.

**`explain.queryPlanner.indexFilterSet`**

A boolean that specifies whether MongoDB applied an index
filter for the query shape.

**`explain.queryPlanner.queryHash`**

A hexadecimal string that represents the hash of the
query shape and is dependent only on the query shapes.
`queryHash` can help identify slow queries (including the
query filter of write operations) with the same query shape.

**Note:**

As with any hash function, two different query shapes may result
in the same hash value. However, the occurrence of hash
collisions between different query shapes is unlikely.

For more information on `queryHash` and `planCacheKey`,
see query-hash-plan-cache-key.

**`explain.queryPlanner.planCacheKey`**

A hash of the key for the plan cache entry associated with the
query.

Unlike the `explain.queryPlanner.queryHash`, the
`explain.queryPlanner.planCacheKey` is a function of
both the query shape and the currently available indexes for
that shape. That is, if indexes that can support the query
shape are added/dropped, the `planCacheKey` value may change
whereas the `queryHash` value would not change.

For more information on `queryHash` and `planCacheKey`,
see query-hash-plan-cache-key.

**`explain.queryPlanner.optimizedPipeline`**

A boolean that indicates that the entire aggregation pipeline
operation was optimized away, and instead, fulfilled by a tree
of query plan execution stages.

For example, the following aggregation operation can be fulfilled by the 
tree of query plan execution rather than using the aggregation pipeline.

```javascript
db.example.aggregate([ { $match: { someFlag: true } } ] )
```

The field is only present if the value is `true` and only
applies to explain on aggregation pipeline operations. When
`true`, because the pipeline was optimized away, no
aggregation stage information appears in the output.

**`explain.queryPlanner.winningPlan`**

A document that details the plan selected by the query
optimizer. 

**`explain.queryPlanner.winningPlan.stage`**

A string that denotes the name of the stage.

Each stage consists of information specific to the stage. For
example, an `IXSCAN` stage includes the index bounds along with
other data specific to the index scan. If a stage has a child
stage or multiple child stages, the stage will have an
`inputStage` or `inputStages`.

This field appears if the operation used the classic query
execution engine. 

**`explain.queryPlanner.winningPlan.inputStage`**

A document that describes the child stage, which provides the 
documents or index keys to its parent. The field is present *if* 
the parent stage has only one child.

**`explain.queryPlanner.winningPlan.inputStages`**

An array of documents describing the child stages. Child stages 
provide the documents or index keys to the parent stage. The field 
is present *if* the parent stage has multiple child nodes. 
For example, stages for $or expressions or index intersection consume input from multiple 
sources.

This field appears if the operation used the classic query
execution engine. 

**`explain.queryPlanner.winningPlan.queryPlan`**

A document that details the plan selected by the query
optimizer. MongoDB presents the plan as a tree
of stages.

This document appears if the query used the slot-based 
execution query engine.

**New in version:** 5.1

**`explain.queryPlanner.winningPlan.queryPlan.stage`**

A string that denotes the name of the stage.

Each stage consists of information specific to the stage. For
example, an `IXSCAN` stage includes the index bounds along
with other data specific to the index scan.

**`explain.queryPlanner.winningPlan.queryPlan.planNodeId`**

Unique integer field that identifies each stage in the execution
plan. Field is included in all stages throughout the `explain`
results.

**New in version:** 5.1

**`explain.queryPlanner.winningPlan.queryPlan.inputStage`**

See `explain.queryPlanner.winningPlan.inputStage`.

**`explain.queryPlanner.winningPlan.slotBasedPlan`**

Document with information about the slot based query execution plan
tree and stages. **For internal use by MongoDB.**

**New in version:** 5.1

**`explain.queryPlanner.rejectedPlans`**

Array of candidate plans considered and rejected by the
query optimizer. The array can be empty if there were no other
candidate plans.

### `executionStats`

The returned `explain.executionStats` information details the
execution of the winning plan. In order to include
`executionStats` in the results, you must run the explain in either:

- executionStats or

- allPlansExecution
  verbosity mode. Use `allPlansExecution` mode to include partial
  execution data captured during plan selection.

These examples may combine the output structures of MongoDB's classic
and slot-based execution engines. They are not meant to be 
representative. Your output may differ significantly.

tabs:

   - id: unsharded
     name: "Unsharded Collections"
     content: |

         For unsharded collections, `explain` returns the following
         `executionStats` information:

         ```javascript
         executionStats: {
            executionSuccess: <boolean>,
            nReturned: <int>,
            executionTimeMillis: <int>,
            totalKeysExamined: <int>,
            totalDocsExamined: <int>,
            executionStages: {
               stage: <STAGE1>
               nReturned: <int>,
               executionTimeMillisEstimate: <int>,
               opens: <int>, // Starting in MongoDB 5.1
               closes: <int>, // Starting in MongoDB 5.1
               works: <int>,
               advanced: <int>,
               needTime: <int>,
               needYield: <int>,
               saveState: <int>,
               restoreState: <int>,
               isEOF: <boolean>,
               ...
               inputStage: {
                  stage: <STAGE2>,
                  nReturned: <int>,
                  ...
                  numReads: <int>, // Starting in MongoDB 5.1
                  ...
                  executionTimeMillisEstimate: <int>,
                  ...
                  inputStage: {
                     ...
                  }
               }
            },
            allPlansExecution: [
               {
                  nReturned: <int>,
                  executionTimeMillisEstimate: <int>,
                  totalKeysExamined: <int>,
                  totalDocsExamined:<int>,
                  executionStages: {
                     stage: <STAGEA>,
                     nReturned: <int>,
                     executionTimeMillisEstimate: <int>,
                     ...
                     inputStage: {
                        stage: <STAGEB>,
                        ...
                        inputStage: {
                          ...
                        }
                     }
                  }
               },
               ...
            ]
         }
         ```

   - id: sharded
     name: "Sharded Collections"
     content: |

         For sharded collections, `explain` includes the execution
         statistics for each accessed shard.

         ```javascript
         executionStats: {
            nReturned: <int>,
            executionTimeMillis: <int>,
            totalKeysExamined: <int>,
            totalDocsExamined: <int>,
            executionStages: {
               stage: <STAGE1>
               nReturned: <int>,
               executionTimeMillis: <int>,
               opens: <int>, // Starting in MongoDB 5.1
               closes: <int>, // Starting in MongoDB 5.1
               totalKeysExamined: <int>,
               totalDocsExamined: <int>,
               totalChildMillis: <NumberLong>,
               shards: [
                  {
                     shardName: <string>,
                     executionSuccess: <boolean>,
                     executionStages: {
                        stage: <STAGE2>,
                        nReturned: <int>,
                        executionTimeMillisEstimate: <int>,
                        ...
                        chunkSkips: <int>,
                        inputStage: {
                           stage: <STAGE3>,
                           ...
                           numReads: <int>, // Starting in MongoDB 5.1
                           ...
                           inputStage: {
                              ...
                           }
                        }
                     }
                  },
                  ...
               ]
            }
            allPlansExecution: [
               {
                  shardName: <string>,
                  allPlans: [
                     {
                        nReturned: <int>,
                        executionTimeMillisEstimate: <int>,
                        totalKeysExamined: <int>,
                        totalDocsExamined:<int>,
                        executionStages: {
                           stage: <STAGEA>,
                           nReturned: <int>,
                           executionTimeMillisEstimate: <int>,
                           ...
                           inputStage: {
                              stage: <STAGEB>,
                              ...
                              inputStage: {
                                ...
                              }
                           }
                        }
                     },
                     ...
                  ]
               },
               {
                  shardName: <string>,
                  allPlans: [
                   ...
                  ]
               },
               ...
            ]
         }
         ```

**`explain.executionStats`**

Contains statistics that describe the completed query execution for
the winning plan. For write operations, completed query execution
refers to the modifications that *would* be performed, but does
*not* apply the modifications to the database.

**`explain.executionStats.nReturned`**

Number of documents returned by the winning query plan.
`nReturned` corresponds to the `n` field
returned by `cursor.explain()` in earlier versions of MongoDB.

**`explain.executionStats.executionTimeMillis`**

Total time in milliseconds required for query plan selection and
query execution. It includes the time it takes to run the trial phase 
part of the plan selection process, but does not include the network time 
to transmit the data back to the client.

The time reported by `explain.executionStats.executionTimeMillis` is 
not necessarily representative of actual query time. During steady 
state operations (when the query plan is cached), or when using 
`cursor.hint()` with `cursor.explain()`, MongoDB bypasses the 
plan selection process, resulting in a faster actual time, leading to 
a lower `explain.executionStats.executionTimeMillis` value.

**`explain.executionStats.totalKeysExamined`**

Number of index entries scanned.
`explain.executionStats.totalKeysExamined` corresponds to the
`nscanned` field returned by `cursor.explain()` in
earlier versions of MongoDB.

**`explain.executionStats.totalDocsExamined`**

Number of documents examined during query execution. Common
query execution stages that examine documents are `COLLSCAN`
and `FETCH`.

**Note:**

`explain.executionStats.totalDocsExamined` refers to
the total number of documents examined and *not* to the
number of documents returned. For example, a stage can
examine a document in order to apply a filter. If the
document is filtered out, then it has been examined but
will not be returned as part of the query result set.

If a document is examined multiple times during query
execution,
`explain.executionStats.totalDocsExamined` counts
each examination. That is,
`explain.executionStats.totalDocsExamined` is *not* a
count of the total number of *unique* documents examined.

**`explain.executionStats.executionStages`**

Details the completed execution of the winning plan as a tree of
stages; i.e. a stage can have an `inputStage` or multiple
`inputStages`.

Starting in MongoDB 5.1, a stage can have these input stages:

- `thenStage`
- `elseStage`
- `innerStage`
- `outerStage`

Each stage consists of execution information specific to the
stage.

**`explain.executionStats.executionStages.executionTimeMillisEstimate`**

The estimated amount of time in milliseconds for query execution.

**`explain.executionStats.executionStages.opens`**

Starting in MongoDB 5.1, the number of times a stage was
opened during query execution.

**`explain.executionStats.executionStages.closes`**

Starting in MongoDB 5.1, the number of times a stage was
closed during query execution.

**`explain.executionStats.executionStages.works`**

Specifies the number of "work units" performed by the query 
execution stage. Query execution divides its work into small 
units. A "work unit" might consist of examining a single index 
key, fetching a single document from the collection, applying 
a projection to a single document, or doing a piece of internal 
bookkeeping.

This field appears if the operation used the classic query
execution engine. 

**`explain.executionStats.executionStages.saveState`**

The number of times that the query stage suspended processing
and saved its current execution state, for example in
preparation for yielding its locks.

**`explain.executionStats.executionStages.restoreState`**

The number of times that the query stage restored a saved
execution state, for example after recovering locks that it had
previously yielded.

**`explain.executionStats.executionStages.isEOF`**

Specifies whether the execution stage has reached end of stream:

- If `true` or `1`, the execution stage has reached
  end-of-stream.

- If `false` or `0`, the stage may still have results to
  return. For example, consider a query with a limit whose
  execution stages consists of a `LIMIT` stage with an
  input stage of `IXSCAN` for the query. If the query
  returns more than the specified limit, the `LIMIT` stage
  will report `isEOF: 1`, but its underlying `IXSCAN` stage
  will report `isEOF: 0`.

**`explain.executionStats.executionStages.inputStage`**

Each `inputStage` can have different fields depending on the
value of `inputStage.stage`. The following table describes 
possible fields and what stages they can appear in.

Each `inputStage` can have another `inputStage` as a field.
See explain-output-structure.

* - Field
  - Description
  - Applicable Stages

* - `docsExamined`
  - Specifies the number of documents scanned during the
    query execution stage.
  - `COLLSCAN`, `FETCH`

* - `keysExamined`
  - For query execution stages that scan an index `keysExamined` 
    is the total number of in-bounds and out-of-bounds
    keys that are examined in the process of the index scan. If the
    index scan consists of a single contiguous range of keys, only
    in-bounds keys need to be examined. If the index bounds consists of
    several key ranges, the index scan execution process may examine
    out-of-bounds keys in order to skip from the end of one range to the
    beginning of the next.
  - `IXSCAN`

* - `numReads`
  - The number of documents scanned or index keys examined during
    the query execution stage. 

    **New in version:** 5.1

  - `COLLSCAN`, `IXSCAN`

* - `seeks`
  - The number of times that we had to seek the index cursor to
    a new position in order to complete the index scan.
  - `IXSCAN`

* - `spilledBytesApprox`
  - The approximate number of in-memory bytes spilled to disk in 
    the stage.

    **New in version:** 5.3

  - `GROUP`

* - `spilledRecords`
  - The number of produced records spilled to disk in the stage.

    **New in version:** 5.3

  - `GROUP`

* - `usedDisk`
  - Whether the stage wrote to disk.

    **New in version:** 5.3

  - `GROUP`

**`explain.executionStats.allPlansExecution`**

Contains *partial* execution information captured during the
plan selection phase for
both the winning and rejected plans. The field is present only if
`explain` runs in `allPlansExecution` verbosity mode.

### `serverInfo`

tabs:

   - id: unsharded
     name: "Unsharded Collections"
     content: |

         For unsharded collections, `explain` returns the following
         `serverInfo` information for the MongoDB instance:

         ```javascript
         serverInfo: {
            host: <string>,
            port: <int>,
            version: <string>,
            gitVersion: <string>
         }
         ```

   - id: sharded
     name: "Sharded Collections"
     content: |

        For sharded collections, `explain` returns the
        `serverInfo` for each accessed shard, and a top-level
        `serverInfo` object for the `bin.mongos`.

        ```javascript
        queryPlanner: {
           ...
           winningPlan: {
              stage: <STAGE1>,
              shards: [
                 {
                    shardName: <string>,
                    connectionString: <string>,
                    serverInfo: {
                       host: <string>,
                       port: <int>,
                       version: <string>,
                       gitVersion: <string>
                    },
                    ...
                 }
                 ...
              ]
           }
         },
         serverInfo: {      // serverInfo for mongos
           host: <string>,
           port: <int>,
           version: <string>,
           gitVersion: <string>
         }
         ...
        ```

## Execution Plan Statistics for Query with `$lookup` Pipeline Stage

**New in version:** 5.0

The explain results can include execution
statistics for queries that use a `$lookup` pipeline stage. To
include those execution statistics, you must run the explain operation
in one of these execution verbosity modes:

- executionStats
- allPlansExecution

The following fields are included in the explain results for a
`$lookup` query:

```none
'$lookup': {
   from: <string>,
   as: <string>,
   localField: <string>,
   foreignField: <string>
},
totalDocsExamined: <long>,
totalKeysExamined: <long>,
collectionScans: <long>,
indexesUsed: [ <string_1>, <string_2>, ..., <string_n> ],
executionTimeMillisEstimate: <long>
```

To see the descriptions for the fields in the `$lookup` section, see
the `$lookup` page.

The other fields are:

**`explain.totalDocsExamined`**

Number of documents examined during the query execution.

**`explain.totalKeysExamined`**

Number of index keys examined.

**`explain.collectionScans`**

Number of times a collection scan occurred during query execution.
During a collection scan, each document in a collection is compared
to the query predicate. Collection scans occur if no appropriate
index exists that covers the query.

**`explain.indexesUsed`**

Array of strings with the names of the indexes used by the query.

**`explain.executionTimeMillisEstimate`**

Estimated time in milliseconds for the query execution.

## Collection Scan

If the query planner selects a collection scan, the explain result
includes a `COLLSCAN` stage.

If the query planner selects an index, the explain result includes a
`IXSCAN` stage. The stage includes information such as the index
key pattern, direction of traversal, and index bounds.

Starting in MongoDB 5.3, if the query planner selects a clustered
index for a clustered
collection and the query contains bounds that
define the portion of the index to search, the explain result includes a
`CLUSTERED_IXSCAN` stage. The stage includes information about the
clustered index key and index bounds.

If the query planner selects a clustered index for a clustered collection and the query *does not* contain bounds, the
query performs an unbounded collection scan and the explain result
includes a `COLLSCAN` stage.

**Note:**

The `notablescan` parameter does not allow unbounded
queries that use a clustered index because the queries require a
full collection scan. 

For more information on execution statistics of collection scans, see
/tutorial/analyze-query-plan.

## Covered Queries

When an index covers a query, 
MongoDB can both match the query conditions **and** return the 
results using only the index keys. MongoDB does not need to 
examine documents from the collection to perform any part of the 
query.

When an index covers a query, the explain result has an `IXSCAN`
stage that is **not** a descendant of a `FETCH` stage, and in the
executionStats, the `explain.executionStats.totalDocsExamined` 
is `0`.

## Index Intersection

For an index intersection plan, the
result will include either an `AND_SORTED` stage or an `AND_HASH`
stage with an `explain.queryPlanner.winningPlan.inputStages` array that
details the indexes; e.g.:

```javascript
{
   stage : 'AND_SORTED',
   inputStages : [
      {
         stage : 'IXSCAN',
         ...
      },
      {
         stage : 'IXSCAN',
         ...
      }
   ]
}
```

## `$or` Expression

If MongoDB uses indexes for an `$or` expression, the result will
include the `OR` stage with an
`explain.queryPlanner.winningPlan.inputStages` array that
details the indexes; e.g.:

```javascript
{
   stage: 'OR',
   inputStages: [
      {
         stage: 'IXSCAN',
         ...
      },
      {
         stage : 'IXSCAN',
         ...
      },
      ...
   ]
}
```

In previous versions of MongoDB, `cursor.explain()` returned the
`clauses` array that detailed the indexes.

## `$sort` and `$group` Stages

When `explain` is run in either  
executionStats or 
allPlansExecution verbosity 
mode, the `$sort` and `$group` stages have 
additional output.

| Stage | Field | Type | Description |
|---|---|---|---|
| `$sort` | `totalDataSizeSortedBytesEstimate` | long | An estimated number of bytes processed in the `$sort` stage. |
| `$sort` | `usedDisk` | boolean | Whether the `$sort` stage wrote to disk. |
| `$group` | `totalOutputDataSizeBytes` | long | An estimate of the total size of all documents output by the `$group` stage in bytes. |
| `$group` | `usedDisk` | boolean | Whether the `$group` stage wrote to disk. |

## Sort Stage

If MongoDB cannot use an index or indexes to obtain the sort order, the
results include a `SORT` stage indicating an in-memory sort operation.
If the explain plan does not contain an explicit `SORT` stage, then MongoDB used
an index to obtain the sort order.
