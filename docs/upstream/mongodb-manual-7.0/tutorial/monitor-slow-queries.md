<!-- Converted from tutorial/monitor-slow-queries.txt (reStructuredText). Includes are inlined. -->

# Monitor Slow Queries

The `$currentOp` aggregation stage provides
information on all operations currently running on MongoDB. If
your application is experiencing performance issues, you can
build an aggregation pipeline around this stage to monitor for
slow queries and similar issues.

## About This Task

### Database Profilers

This task uses `$currentOp` to identify slow queries
currently running on your application. To find all slow queries
within a specified period, consider using a profiler.

| Profiler | Description |
|---|---|
| Atlas Query Profiler | Provides a scatterplot chart to Atlas customers, making it easy to identify slow queries and performance outliers. |
| database-profiler | Stores query performance information in a collection, allowing you to query MongoDB for queries with specific performance issues. |

Both the Atlas Query Profiler and the database profiler can
affect server performance, use up disk space, and expose query
metadata around encrypted fields. Consider the performance and
security implications before enabling them.

### Explain Queries

This task identifies queries with performance issues. If you
already know which queries have performance issues, see
manual-explain-slow-queries to troubleshoot them.

## Steps

**Step 1: Retrieve current operations.**

Use the `$currentOp` aggregation stage to
retrieve current operations from MongoDB:

```javascript
db.getSiblingDB("admin").aggregate( [
   { $currentOp: { allUsers: true } },
   { $match: { secs_running: { $gt: 2 } } },
   { $sort: { secs_running: 1 } }
] )
```

Output:

```javascript
[
   {
      "opid": "12345",
      "secs_running": 5,
      "active": true,
      "ns": "sample_mflix.movies",
      "command": {
         "find": "movies",
         "filter": { "title": { "$regex": "The" } }
      },
      "planSummary": "COLLSCAN",
      "locks": { ... },
      "client": "203.0.113.25:43210"
   }
]
```

This aggregation pipeline retrieves all current operations
in the cluster. The `$match` aggregation stage
then filters the operations to those that have been
running for more than two seconds. This allows you to
filter queries that run within a specified period. Adjust
the value to match your application and database needs.

The `$sort` stage sorts the results in
ascending operation time order.

**Step 2: Check for activity.**

View the `currentOp.active` field. If `currentOp.active` is
`true`, MongoDB indicates that the operation is currently
running.

To stop a long running operation, use the
`db.killOp` method to stop the given
`opid`.

**Step 3: Check for locks.**

View the `currentOp.waitingForLock` field. If `currentOp.waitingForLock` is
`true`, another operation running on the server or cluster is blocking the query.

To stop a blocked operation, use the `db.killOp`
method to stop the given `opid`.

**Step 4: Check the plan summary.**

Check the value in the `currentOp.planSummary`
field.

`IXSCAN`
   Indicates the query performed an index scan.

`COLLSCAN`
   Indicates the query performed a full collection scan.
   To correct this, manual-create-an-index.

**Step 5: Explain the query.**

If the `$currentOp` aggregation stage returns a
query that requires further investigation, use the
`explain` method to analyze the
query plan and execution statistics.

For details, see manual-explain-slow-queries.

## Learn More

- query-performance
- profiler
- manual-find-slow-queries-with-database-profiler 
- manual-explain-slow-queries
