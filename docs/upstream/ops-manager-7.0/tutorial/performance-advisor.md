<!-- Converted from tutorial/performance-advisor.txt (reStructuredText). Includes are inlined. -->

# Monitor and Improve Slow Queries

The Performance Advisor monitors any operation with a query predicate
that MongoDB considers slow and suggests new
indexes to improve query performance. For the
selected host and time period, the Performance Advisor evaluates up to
the 20,000 most recent slow queries found in the logs.

Recommended indexes are accompanied by sample queries, grouped by
query shape, that were run against a collection that would
benefit from the suggested index. The Performance Advisor does not
negatively affect the performance of your Ops Manager clusters.

**Note:**

To view the Performance Advisor, you must:

- Run MongoDB version 3.2 or later on your cluster.

- Manage your cluster with MongoDB Agent Automation.

  To learn more about the MongoDB Agent, see
  /tutorial/nav/mongodb-agent.

To view the field values in the example queries, you must be an Ops Manager
user with one or more of the following roles:

- `Project Owner`

- `Project Data Access Admin`

- `Project Data Access Read/Write`

- `Project Data Access Read Only`

Users without the aforementioned roles cannot see the field values.

## Common Reasons for Slow Queries

If a query is slow, common reasons include:

- The query is unsupported by your current indexes. 
- Some documents in your collection have large array fields that are 
  costly to search and index.
- One query retrieves information from multiple collections with 
  $lookup.

## Index Considerations

Indexes improve read performance, but a large number of indexes can
negatively impact write performance since indexes must be updated during
writes. If your collection already has several indexes, consider this
tradeoff of read and write performance when deciding whether to create
new indexes. Examine whether a query for such a collection can be
modified to take advantage of existing indexes, as well as whether a
query occurs often enough to justify the cost of a new index.

The Performance Advisor can help identify and remove unnecessary 
indexes. To learn more, see pa-drop-index.

## Access Performance Advisor

To access the Performance Advisor:

**Step 1: Click Deployment.**

**Step 2: Click the replica set where the collection resides.**

If the replica set resides in a sharded cluster, first click the
sharded cluster containing the replica set.

**Step 3: Click Performance Advisor.**

**Step 4: Select a collection from the Collections dropdown.**

**Step 5: Select a time period from the Time Range dropdown.**

The Performance Advisor displays up to 20 query shapes
across all collections in the cluster and suggested indexes for those
shapes. The Performance Advisor ranks the indexes according 
to their Impact, which indicates High or 
Medium based on the total wasted bytes read. To learn more 
about index ranking, see pa-index-ranking.

**Note:**

If the slow query log contains consecutive `$match` stages 
in the aggregation pipeline, the two stages can coalesce 
into the first `$match` stage and result in a single 
`$match` stage. As a result, the query shape in the 
Performance Advisor might differ from the actual query you ran.

## Index Suggestions

The Performance Advisor ranks the indexes that it suggests 
according to their Impact, which indicates High 
or Medium based on the total wasted bytes read. To learn 
more about how the Performance Advisor ranks indexes, see pa-index-ranking.

To learn how to create indexes that the Performance Advisor suggests, see 
pa-create-suggested-indexes.

### Index Metrics

Each index that the Performance Advisor suggests contains the following
metrics. These metrics apply specifically to queries which would be
improved by the index:

| Metric | Description |
|---|---|
| Execution Count | Number of queries executed per hour which would be improved. |
| Average Execution Time | Current average execution time in milliseconds for affected queries. |
| Average Query Targeting | Average number of documents read per document returned by affected queries. A higher query targeting score indicates a greater degree of inefficiency. For more information on query targeting, see query-targeting. |
| In Memory Sort | Current number of affected queries per hour that needed to be sorted in memory. |
| Average Docs Scanned | Average number of documents scanned. |
| Average Docs Returned | Average number of documents returned. |
| Avgerage Object Size | Average object size. |

### Sample Queries

For each suggested index, the Performance Advisor shows the most commonly executed 
query shapes that the index would improve. For each query shape, the 
Performance Advisor displays the following metrics:

| Metric | Description |
|---|---|
| Execution Count | Number of queries executed per hour which match the query shape. |
| Average Execution Time | Average execution time in milliseconds for queries which match the query shape. |
| Average Query Targeting | Average number of documents read for every document returned by matching queries. A higher query targeting score indicates a greater degree of inefficiency. For more information on query targeting, see query-targeting. |
| Average Docs Scanned | Average number of documents scanned. |
| Average Docs Returned | Average number of documents returned. |

The Performance Advisor also shows each executed sample query that matches the 
query shape, with specific metrics for that query.

### Query Targeting

Each index suggestion includes an Average Query Targeting
score indicating how many documents were read for every document
returned for the index's corresponding query shapes. A score of 1
represents very efficient query shapes because every document read
matched the query and was returned with the query results. All suggested
indexes represent an opportunity to improve query performance.

### Filter Index Suggestions

By default, the Performance Advisor suggests indexes for all clusters
in the deployment. To only show suggested indexes from a specific
collection, use the Collection dropdown at the top of
the Performance Advisor.

You can also adjust the time range the Performance Advisor takes into
account when suggesting indexes by using the Time Range
dropdown at the top of the Performance Advisor.

### Limitations of Index Suggestions

#### Timestamp Format for Indexes

The Performance Advisor can't suggest indexes for MongoDB databases
configured to use the ctime timestamp format. As a
workaround, set the timestamp format for such databases to either
iso8601-utc or
iso8601-local.

#### Log Size

The Performance Advisor analyzes up to 200,000 of your cluster's most recent log lines.

## Create Suggested Indexes

You can create indexes suggested by the
Performance Advisor directly within the Performance Advisor itself. When
you create indexes, keep the ratio of reads to writes on the target
collection in mind. Indexes come with a performance cost, but are more
than worth the cost for frequent queries on large data sets. To
learn more about indexing strategies, see
Indexing Strategies.

### Behavior

- You can only create one index at a time through the Performance
  Advisor. If you want to create more simultaneously, you can do so
  using Data Explorer or the
  shell

- Ops Manager always creates indexes at the top level of the deployment. If 
  you create an index while viewing the Performance Advisor for a single shard in a 
  sharded cluster, Ops Manager creates that index for the entire 
  sharded cluster.

### Procedure

To create a suggested index:

**Step 1: For the index you want to create, click Create Index.**

The Performance Advisor opens the Create Index dialog
and prepopulates the Fields based on the
index you selected.

**Step 2: *(Optional)* Specify the index options.**

```javascript
{ <option1>: <value1>, ... }
```

**Example:**

The following options document specifies the `unique` option and
the `name` for the index:

```javascript
{ unique: true, name: "myUniqueIndex" }
```

**Step 3: *(Optional)* Set the Collation options.**

Use collation to specify language-specific rules for string comparison,
such as rules for lettercase and accent marks. The
collation document
contains a `locale` field which indicates the [ICU Locale code](http://userguide.icu-project.org/locale), and may contain other
fields to define collation behavior.

**Example:**

The following collation option document specifies a locale value
of `fr` for a French language collation:

```json
{ "locale": "fr" }
```

To review the list of locales that MongoDB collation supports, see
the list of languages and locales. To learn more about collation
options, including which are enabled by default for each locale, see
Collation in the MongoDB manual.

**Step 4: *(Optional)* Enable building indexes in a rolling fashion.**

**Warning:**

Due to critical issue SERVER-68925, Ops Manager deployments
using certain versions of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v6.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

- MongoDB 4.2.19-4.2.22
- MongoDB 4.4.13-4.4.16
- MongoDB 5.0.6-5.0.11
- MongoDB 6.0.0-6.0.1

You can continue to perform manual rolling index builds safely on your clusters.
To perform automated rolling index builds safely, upgrade the MongoDB Agent to 12.0.11.7606 or later or 
upgrade your clusters to:

- MongoDB 4.2.23 or later
- MongoDB 4.4.17 or later
- MongoDB 5.0.12 or later
- MongoDB 6.0.2 or later

**Important:**

Rolling index builds succeed only when they meet certain conditions. 
To ensure your index build succeeds, avoid the following design 
patterns that commonly trigger a restart loop:

- Index key exceeds the index key limit
- Index name already exists
- Index on more than one array field
- Index on collection that has the 
  maximum number of text indexes
- Text index on collection that has the
  maximum number of text indexes

**Note:**

Data Explorer doesn't support building indexes in a rolling fashion
for standalone deployments.

Building indexes in a rolling fashion reduces the performance impact of
building indexes on replica sets and
sharded clusters. To maintain cluster
availability, Ops Manager removes one node from the cluster at a time
starting with a secondary.

After you build an index in a rolling fashion, if your MongoDB database
runs with an FCV
less than `4.2`, resync the head database to ensure that the head database takes the 
new index into account.

Ops Manager automatically cancels rolling index builds 
that don't succeed on all nodes. When a rolling index build completes 
on some nodes, but fails on others, Ops Manager cancels the build
and removes the index from any nodes that it was successfully built on. 

In the event of a rolling index build cancellation, Ops Manager generates an 
activity feed event and sends a notification email to the project owner 
with the following information:

- Name of the cluster on which the rolling index build failed
- Namespace on which the rolling index build failed
- Project that contains the cluster and namespace
- Organization that contains the project
- Link to the activity feed event

To learn more about rebuilding indexes, see Build Indexes on
Replica Sets.

**Note:**

The following index options are 
incompatible with building indexes in a rolling fashion:

- unique

- storageEngine

- textIndexVersion

- 2dsphereIndexVersion

Ops Manager ignores these options if you specify them in the
Options pane.

**Step 5: Click Review.**

**Step 6: In the Confirm Operation dialog, confirm your index.**

**Important:**

When an index build completes, Ops Manager generates 
an activity feed event
and sends a notification email to the project owner 
with the following information:

- Completion date of the index build
- Name of the cluster on which the index build completed
- Namespace on which the index build completed
- Project containing the cluster and namespace
- Organization containing the project
- Link to the activity feed event
