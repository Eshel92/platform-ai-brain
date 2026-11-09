<!-- Converted from tutorial/evaluate-operation-performance.txt (reStructuredText). Includes are inlined. -->

# Evaluate Performance of Current Operations

The following sections describe techniques for evaluating operational
performance.

## Use the Database Profiler to Evaluate Operations Against the Database

MongoDB provides a database profiler that shows performance
characteristics of each operation against the database. Use the profiler
to locate any queries or write operations that are running slow. You can
use this information, for example, to determine what indexes to create.

The profiler entries and the 
diagnostic log messages (i.e. mongod/mongos logmessages) for read/write operations include:

- `queryHash` to help identify slow queries with the same
  query shape. 

- `planCacheKey` to provide more insight into the query plan
  cache for slow queries.

Secondary members of a replica set now log oplog entries that take longer than the slow operation
threshold to apply. These slow oplog messages:

- Are logged for the secondaries in the
  `diagnostic log`.

- Are logged under the `REPL` component with the text
  `applied op: <oplog entry> took <num>ms`.

- Do not depend on the log levels (either at the system or component
  level)

- Do not depend on the profiling level.

- Are affected by `slowOpSampleRate`.

The profiler does not capture slow oplog entries.

For more information, see /tutorial/manage-the-database-profiler.

## Use `db.currentOp()` to Evaluate `mongod` Operations

The `db.currentOp()` method reports on current operations
running on a `mongod` instance.

## Use `explain` to Evaluate Query Performance

The `cursor.explain()` and `db.collection.explain()`
methods return information on a query execution, such as the index
MongoDB selected to fulfill the query and execution statistics. You can
run the methods in queryPlanner
mode, executionStats mode, or
allPlansExecution mode to
control the amount of information returned.

**Example:** To use `cursor.explain()` on a query

for documents matching the expression `{ a: 1 }`, in the
collection named `records`, use an operation that resembles the
following in `mongosh`:

```javascript
db.records.find( { a: 1 } ).explain("executionStats")
```

Starting in MongoDB 4.2, the explain output includes:

- `queryHash` to help identify slow queries
  with the same query shape.

- `planCacheKey` to provide more insight
  into the query plan cache for slow queries.

For more information, see /reference/explain-results,
`cursor.explain()`, `db.collection.explain()`, and
/tutorial/analyze-query-plan.
