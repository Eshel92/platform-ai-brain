<!-- Converted from tutorial/suggest-indexes.txt (reStructuredText). Includes are inlined. -->

# Calculate Suggested Indexes

Ops Manager can analyze the data on query patterns collected by the database
profiler and suggest a set of indexes that could improve query
performance. Ops Manager scores each suggested index on its expected benefit.

## Prerequisites

For Ops Manager to suggest indexes, the following must be true:

- You must enable database profiling for the MongoDB process.
  See /tutorial/profile-database.

- The profiler must have data. If profiling is enabled, but no
  profiling data has yet been collected, Ops Manager cannot suggest indexes.

## Procedure

To edit the deployment's configuration:

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click a deployment.**

**Step 3: (Optional) For sharded clusters, filter which process type is listed.**

The four buttons are listed in the following order, left to right:
Shards, Configs, Mongos, and
BIs. 

| Process | Displays |
|---|---|
| Shards | mongod processes that host your data. |
| Configs | mongod processes that run as config servers to store a sharded cluster's metadata. |
| Mongos | mongos processes that route data in a sharded cluster. |
| BIs | BI (Business Intelligence) processes that access data in a sharded cluster. |

**Step 4: Click the process for which you want to calculate suggested indexes.**

For shared clusters, you must first click the shard that contains the
process.

**Step 5: Click the Profiler tab above the charts.**

**Step 6: Click the Calculate Suggested Indexes link above the chart.**

The calculate suggested indexes link will not appear
if the profiling-prerequisites have not been met.

**Step 7: Copy the indexes you want to create and add them to the MongoDB process.**

For instructions on adding an index to a MongoDB process, see either:

- Index Creation in the MongoDB manual, or

- Create Indexes with Data Explorer.
