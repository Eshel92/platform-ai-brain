<!-- Converted from modules/cassandra/pages/vector-search/_create-vector-table-cycling.adoc (AsciiDoc). Includes are inlined. -->

# Create vector table

Create a new table in your keyspace, including the `comments_vector` column for vector. The code below creates a vector with five values: 

```cql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
```

Optionally, you can alter an existing table to add a vector column:

```cql
ALTER TABLE cycling.comments_vs
```
