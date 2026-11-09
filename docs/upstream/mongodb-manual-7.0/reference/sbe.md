<!-- Converted from reference/sbe.txt (reStructuredText). Includes are inlined. -->

# Slot-Based Query Execution Engine

**New in version:** 5.1

To find and return query results, MongoDB uses one of the following
query engines:

- The classic query engine

- The slot-based query execution engine, which is available for some queries starting in MongoDB
  5.1.

MongoDB automatically selects the engine to execute the query. You
cannot manually specify an engine for a particular query.

MongoDB can use the slot-based query execution engine for a subset of queries provided certain
conditions are met. In most cases, the slot-based execution engine provides improved
performance and lower CPU and memory costs compared to the classic query
engine.

MongoDB uses the classic engine for queries that are ineligible for the
slot-based query execution engine.

**Note:**

Starting in version 7.0.17, the slot-based query execution engine is no longer
enabled by default for patch versions of 7.0. If you want 
your queries to use the slot-based query execution engine, please upgrade to 
version 8.0, where it is enabled by default.

## Eligible Queries for the Slot-Based Execution Engine

MongoDB determines eligibility for using the slot-based execution engine on a per-query basis, 
and considers support for each operator and expressions present in the query. 
For example, two common pipelines that use slot-based execution engine are aggregations with 
`$group` or `$lookup` stages. However, support for the 
slot-based execution engine is version specific and actively changing.

To see whether your query used the slot-based execution engine, refer to the 
sbe-determine-query-engine section.

## Determine which Query Engine was Used

There are a few ways to determine whether the classic engine or the
slot-based execution engine was used to execute a query.

### Check Query Explain Results

The explain results for a query differ based on
which query engine was used. For example, explain results for queries
executed using the slot-based execution engine include the 
`explain.queryPlanner.winningPlan.slotBasedPlan` field.

For more information about the differences in explain results between
query engines, see explain-output-structure.

### Check Slow Query Logs

Slow operation log messages include a `queryFramework` field that indicates 
which query engine executed the query:

- `queryFramework: "classic"` indicates that the classic engine
  executed the query.

- `queryFramework: "sbe"` indicates that the slot-based query execution engine executed the
  query.

To see an example log message for a query that used the slot-based execution engine,
see log-message-json-examples-slow-op.
