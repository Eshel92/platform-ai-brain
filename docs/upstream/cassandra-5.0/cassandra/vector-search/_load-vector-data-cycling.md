<!-- Converted from modules/cassandra/pages/vector-search/_load-vector-data-cycling.adoc (AsciiDoc). Includes are inlined. -->

# Load vector data into your database

Insert data into the table using the new type:

```cql
INSERT INTO cycling.comments_vs (record_id, id, created_at, comment, commenter, comment_vector)
```
