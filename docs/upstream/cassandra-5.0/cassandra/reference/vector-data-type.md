<!-- Converted from modules/cassandra/pages/reference/vector-data-type.adoc (AsciiDoc). Includes are inlined. -->

# Vector CQL data type

A new CQL data type, a `VECTOR` is required for Vector Search.
https://issues.apache.org/jira/browse/CASSANDRA-18504 added this data type to {cass-50}.
The new type `VECTOR` has the following properties:

* fixed length array
* elements may not be null
* flatten array (aka multi-cell = false)

Although the data type specified for a vector used in vector search is a floating point number, the vector data type can be used to create a vector of any data type. For example, a vector of `int` or `bigint` can be created, but cannot be used with vector search.

**Note:**
Vectors are limited to a maximum dimension of 8K (2^13) items.

Create a keyspace:

```cql
CREATE KEYSPACE IF NOT EXISTS cycling 
```

Use the keyspace:

```cql
USE cycling;
```

This data type can be used in a `CREATE TABLE` statement:

```cql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
```
<1> Create a 5-dimensional embedding

Index the vector column:

```cql
CREATE INDEX IF NOT EXISTS ann_index 
```

Insert data:

```cql
INSERT INTO cycling.comments_vs (record_id, id, created_at, comment, commenter, comment_vector)
```

Select data:

```cql
SELECT * FROM cycling.comments_vs 
```
