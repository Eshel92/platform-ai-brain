<!-- Converted from modules/cassandra/pages/vector-search/vector-search-working-with.adoc (AsciiDoc). Includes are inlined. -->

# Working with Vector Search

# Create vector keyspace

Create the keyspace you want to use for your Vector Search table. 
This example uses `cycling` as the `keyspace name`:

```cql
CREATE KEYSPACE IF NOT EXISTS cycling 
```

# Use vector keyspace

Select the keyspace you want to use for your Vector Search table. This example uses `cycling` as the `keyspace name`:

```cql
USE cycling;
```

# Create vector table

Create a new table in your keyspace, including the `comments_vector` column for vector. The code below creates a vector with five values: 

```cql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
```

Optionally, you can alter an existing table to add a vector column:

```cql
ALTER TABLE cycling.comments_vs
```

# Create vector index

Create the custom index with Storage Attached Indexing (SAI):

```cql
CREATE INDEX IF NOT EXISTS ann_index 
```

For more about SAI, see the Storage Attached Indexing documentation.

**Important:**
The index can be created with options that define the similarity function:

```
CREATE INDEX IF NOT EXISTS ann_index
```

Valid values for the `similarity_function` are `DOT_PRODUCT`, `COSINE`, or `EUCLIDEAN`.

# Load vector data into your database

Insert data into the table using the new type:

```cql
INSERT INTO cycling.comments_vs (record_id, id, created_at, comment, commenter, comment_vector)
```

# Query vector data with CQL

To query data using Vector Search, use a `SELECT` query:

```cql
SELECT * FROM cycling.comments_vs 
```

To obtain the similarity calculation of the best scoring node closest to the query data as part of the results, use a `SELECT` query:

```cql
SELECT comment, similarity_cosine(comment_vector, [0.2, 0.15, 0.3, 0.2, 0.05])
```

The supported functions for this type of query are:

* similarity_dot_product
* similarity_cosine
* similarity_euclidean

with the parameters of (<vector_column>, <embedding_value>).
Both parameters represent vectors.

**Note:**
* The limit must be 1,000 or fewer.
* Vector Search utilizes Approximate Nearest Neighbor (ANN) that in most cases yields results almost as good as the exact match. The scaling is superior to Exact Nearest Neighbor (KNN).

* Least-similar searches are not supported.
* Vector Search works optimally on tables with no overwrites or deletions of the `item_vector` column. For an `item_vector` column with changes, expect slower search results.
