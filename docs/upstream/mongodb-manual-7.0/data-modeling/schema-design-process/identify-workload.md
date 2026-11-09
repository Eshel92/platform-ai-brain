<!-- Converted from data-modeling/schema-design-process/identify-workload.txt (reStructuredText). Includes are inlined. -->

# Identify Application Workload

The first step in the schema design process is to identify the operations that your
application runs most frequently. This helps you create effective 
indexes and minimize the number of calls the application makes to the database.

Consider the scenarios your application currently supports and scenarios 
it may support in the future.

## Steps

**Step 1: Identify the data your application needs**

To identify the data that your application needs, consider the
following factors:

- Your application's users and the information they need.
- Your business domain.
- Application logs and frequently-run queries. To see database
  commands run on a MongoDB deployment, see
  database-profiler.

**Step 2: Create a workload table with your application's queries**

Fill out the following table with the queries that your
application needs to run:

| Action | Query Type | Information | Frequency | Priority |
|---|---|---|---|---|
| The action that a user takes to trigger the query. | The type of query (read or write). | The document fields that are either written or returned by the query. | How frequently your application runs the query. Queries that are run frequently benefit from indexes and should be optimized to avoid lookup operations. | How critical the query is to your application. |

## Example

The following example shows a workload table for a blog application:

| Action | Type | Information | Frequency | Priority |
|---|---|---|---|---|
| Submit a new article | Write | author, text | 10 per day | High |
| Submit a comment on an article | Write | user, text | 1,000 per day (100 per article) | Medium |
| View an article | Read | article id, text, comments | 1,000,000 per day | High |
| View article analytics | Read | article id, comments, clicks | 10 per hour | Low |

## Next Steps

After you identify your application's workload, the next step in the
schema design process is to map related data in your schema. See
data-modeling-map-relationships.
