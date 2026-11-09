<!-- Converted from analyze-slow-queries.txt (reStructuredText). Includes are inlined. -->

# Analyze Slow Queries

Ops Manager provides several tools to help analyze slow queries
executed on your clusters. See the following sections for descriptions 
of each tool. To optimize your query performance, 
review the best practices for query performance.

## Performance Advisor

The Performance Advisor monitors slow 
queries and suggests new indexes to improve query performance.

You can use the Performance Advisor to review the following information:

- Index Ranking
- Drop Index Recommendations

## Profiler

The Profiler displays slow-running 
operations and their key performance statistics. You can explore a 
sample of historical queries for up to the last 24 hours without 
additional performance overhead. Before you enable the 
Profiler, see Considerations.

## Best Practices for Query Performance

To optimize query performance, review the following best practices:

- Create queries that your current indexes support to reduce the time 
  needed to search for your results.
  
- Avoid creating documents with large array fields that require a lot 
  of processing to search and index.

- Optimize your indexes and remove unused or inefficient indexes. Too 
  many indexes can negatively affect write performance.

- Consider the suggested indexes from the Performance Advisor with the highest Impact scores and 
  lowest Average Query Targeting scores.

- Create the indexes that the Performance Advisor suggests when they 
  align with your Indexing Strategies.

- .. include:: /includes/fact-performance-advisor-timestamp.rst

- Perform rolling index builds
  to reduce the performance impact of building indexes on 
  replica sets and sharded clusters.

- Drop unused, redundant, and hidden indexes to 
  improve write performance and free storage space.
