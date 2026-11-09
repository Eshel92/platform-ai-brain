<!-- Converted from reference/alerts/query-targeting.txt (reStructuredText). Includes are inlined. -->

# Fix Query Issues

`Query Targeting` alerts indicate inefficient query or queries. 

## Alert Conditions

You can configure the following alert conditions in the project-level 
alert settings page to trigger alerts.

Query Targeting: Scanned / Returned occurs if the
number of index keys examined to fulfill a query relative to the actual
number of returned documents meets or is above a certain threshold.

Query Targeting: Scanned Objects / Returned 
occurs if the number of documents examined to fulfill a query relative 
to the actual number of returned documents meets or is above a certain 
threshold.

## Common Triggers

- No index that supports a given query or queries.

- Existing index can only partially support a query or queries.

## Fix the Immediate Problem

The Performance Advisor provides the
easiest and quickest way to create an index. The Performance Advisor
monitors queries that MongoDB considers slow and recommends indexes to
improve performance.

Click Create Index on a slow query for instructions on how
to create the recommended index.

**Note:**

It is possible to receive a Query Targeting alert for an
inefficient query without receiving index suggestions from the
Performance Advisor if the query exceeds the slow query threshold and
the ratio of scanned to returned documents is greater than the
threshold specified in the alert.

In addition, you can use the following resources to determine which 
query generated the alert:

- The Real-Time Performance Panel
  monitors and displays current network traffic and database operations
  on machines hosting MongoDB in your MongoDB Atlas clusters.

- The MongoDB logs maintain an account of 
  activity,
  including queries, for each `mongod` instance in your MongoDB Atlas
  clusters.

- The cursor.explain()
  command for `mongosh` provides performance details for
  all queries.

- The Data Profiler
  records operations that MongoDB Atlas considers slow when compared to
  average execution time for all operations on your cluster.

  **Note:**

  Enabling the Database Profiler incurs a performance overhead.

## Implement a Long-Term Solution

To learn more about query performance, see:

- MongoDB Indexing Strategies
- Analyze Query Plan

## Monitor Your Progress

Ops Manager provides two methods to visualize query targeting:

- Query Targeting
  metrics, which highlight high ratios
  of objects scanned to objects returned.

- The Profiler, which describes specific
  inefficient queries executed on the cluster.
