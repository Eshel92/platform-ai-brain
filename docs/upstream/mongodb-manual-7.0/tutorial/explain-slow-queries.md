<!-- Converted from tutorial/explain-slow-queries.txt (reStructuredText). Includes are inlined. -->

# Explain Slow Queries

The `explain` method provides information
on how MongoDB plans and executes the given query. You may find
this information useful when troubleshooting query performance
and planning optimizations.

## About This Task

### Explain Queries

The `explain` method is available to
queries that use the following methods:

- `aggregate()`
- `count()`
- `find()`
- `distinct()` 
- `findAndModify()`

### Profilers

This task runs the `explain` method on a
sample query in an attempt to identify performance issues. In
practice, it may be difficult to run `explain()` on every
query your application runs.

To narrow the list of queries to analyze to only those that are
slow, you can use a profiler:

| Profiler | Description |
|---|---|
| Atlas Query Profiler | Provides a scatterplot chart to Atlas customers, making it easy to identify slow queries and performance outliers. |
| database-profiler | Stores query performance information in a collection, allowing you to query MongoDB for queries with specific performance issues. |

Both the Atlas Query Profiler and the database profiler can
affect server performance, use up disk space, and expose query
metadata around encrypted fields. Consider the performance and
security implications before enabling them.

## Steps

**Step 1: Explain the query.**

Run the query you want to evaluate with the
`explain` method:

```js
db.movies.explain( "executionStats").find( {
   year: { $gt: 1990 },
   rated: { $in: [ "PG", "PG-13" ] }
} )
```

**Step 2: Evaluate the execution time.**

Check the `explain.executionStats.executionTimeMillis` 
field to see the execution time in milliseconds. This
shows the total time, including the time it takes to build
and select a query plan in addition to the time it takes
the plan to execute.

- If the execution time is within an acceptable period for
  your application and database needs, no optimization is
  required.

- If the execution time is above an acceptable period,
  further analysis is required to determine why the query
  takes so long to execute.

**Step 3: Evaluate the execution stages.**

Queries can execute in several stages. At each stage,
MongoDB collects documents from the previous stage to
perform the next set of operations.
`explain.executionStats.executionStages` provides
information on each execution stage, where each level of the
`inputStage`
field shows how MongoDB selected documents for the stage.

Check the `inputStage.stage`
field for each execution stage:

`COLLSCAN`
   Indicates MongoDB performed a collection scan.

`IXSCAN`
   Indicates MongoDB performed an index scan.

`FETCH`
   Indicates MongoDB fetched full documents from the
   database. 

   If the query returns a small number of fields and the
   application is not write intensive on this collection,
   consider adding indexes to cover the query. This allows
   MongoDB to fetch the field values from the index rather
   than reading the full document.

   For more information, see covered-queries.

`PROJECTION`
   Indicates MongoDB filtered return fields in memory.

`SORT`
   Indicates MongoDB sorted the documents in memory or
   used a covered index.

Queries that perform filter or sort operations that show a
`COLLSCAN` stage would benefit from an index.

For more information, see manual-create-an-index.

**Step 4: Evaluate key examination.**

Queries on collections with indexes may not make effective
use of the indexes.

Compare the number of keys examined to the number of
documents examined. If the number of keys is
significantly less than the number of documents, it
indicates the indexes were ineffective.

Check the total values for the query and ensure that
`executionStats.totalDocsExamined` does not show
a value greater than
`executionStats.totalKeysExamined`.

If the number of keys examined is much lower than the
number of documents examined, check each stage in
the `executionStages` field,
comparing the `keysExamined` and `docsExamined` to
determine which stage failed to use the index. Then,
create an index to
accommodate the query at that stage.

**Step 5: Evaluate the filter.**

Queries that use filters to specify the results may have
issues. To identify an inefficient filter, compare the
value on the `executionStats.totalDocsExamined` field to that
of the `executionStats.nReturned` field.

- If `totalDocsExamined` has a value much greater than
  that of `nReturned`, it indicates an ineffective
  index. That is, MongoDB had to scan the collection in
  order to filter the results.

  Create an index on the
  filter fields to improve performance.

- If `totalDocsExamined` and `nReturned` have the same
  values, it indicates that MongoDB only examined the
  documents that it returned. This indicates an effective
  index.

## Learn More

- query-performance

- Atlas Query Profiler

- database-profiler
