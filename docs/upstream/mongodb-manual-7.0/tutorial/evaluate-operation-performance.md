<!-- Converted from tutorial/evaluate-operation-performance.txt (reStructuredText). Includes are inlined. -->

# Analyze Query Performance

MongoDB provides several ways to examine the performance of your
workload, allowing you to understand query performance and identify
long-running queries. Understanding query performance helps you build
effective indexes and ensure your application runs critical queries
efficiently.

## Identify Slow Queries

Use the following methods to identify slow queries that occur on your
deployment.

### Performance Overview

The following methods provide overviews of your deployment's
performance. Use these methods to determine if there are performance
issues that need to be addressed:

| Method | Availability | Description |
|---|---|---|
| Use the Atlas Performance Advisor | M10+ Atlas clusters | The Atlas Performance Advisor monitors slow queries and suggests new indexes to improve performance. For more information, see performance-advisor. |
| Check ongoing operations in Atlas | M10+ Atlas clusters | You can use the Atlas Real-Time Performance Panel (RTPP) to see current network traffic, database operations, and hardware statistics. |
| Check ongoing operations locally | Atlas clusters and self-hosted deployments | The `$currentOp` aggregation stage returns information on active operations and cursors. Use `$currentOp` to identify long-running or stuck operations that may be negatively impacting performance. You can also use the `top` command to get additional operation count and latency statistics.. |
| Check server metrics | Atlas clusters and self-hosted deployments | For Atlas clusters, you can view cluster metrics to identify performance issues. For self-hosted deployments, the `serverStatus` command provides metrics that can indicate poor performance and anomalies for query execution. |
| View index statistics | Atlas clusters and self-hosted deployments | The `$indexStats` aggregation stage returns information about your collection's indexes and how often individual indexes are used. Use `$indexStats` to identify unused indexes that can be removed to improve write performance. |

### Analyze a Slow Query

Use these methods to analyze a slow query and determine the cause of
poor performance:

* - Method
  - Availability
  - Description

* - Use the Atlas Query Profiler
  - M10+ Atlas clusters
  - The Atlas Query Profiler shows long-running operations and
    performance statistics. For more information, see
    profile-database.

* - Enable the Database Profiler
  - Atlas clusters and self-hosted deployments
  - When enabled, the database profiler stores information about slow
    queries in the `system.profile <`
    collection.

    For more information, see database-profiler.

* - View slow queries in the diagnostic log
  - Atlas clusters and self-hosted deployments
  - MongoDB logs queries that exceed the slow operation threshold
    (default 100 milliseconds) in the diagnostic logs.

    Check the diagnostic logs to identify problematic queries and see
    which queries would benefit from indexes.

* - View explain results
  - Atlas clusters and self-hosted deployments
  - Query explain results show information on the query plan and
    execution statistics. You can use explain results to determine
    the following information about a query:

    - The amount of time a query took to execute
    - Whether the query used an index
    - The number of documents and index keys scanned to fulfill a
      query

    To view explain results, use the following methods:

    - `db.collection.explain()`
    - `explain()` cursor method

    To learn about explain results output, see explain-results
    and interpret-explain-plan.

## Perform Advanced Query Analysis

The following methods are suited for deeper investigation of problematic
queries, and can provide fine-grained performance insights:

| Method | Availability | Description |
|---|---|---|
| View plan cache statistics | Atlas clusters and self-hosted deployments | The `$planCacheStats` aggregation stage returns information about a collection's plan cache. The plan cache contains query plans that the query planner uses to efficiently complete queries. Generally, the plan cache should contain entries for your most commonly-run queries. |
