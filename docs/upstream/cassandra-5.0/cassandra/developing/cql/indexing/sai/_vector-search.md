<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_vector-search.adoc (AsciiDoc). Includes are inlined. -->

# Vector search

This example uses the following table and index:

```sql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
CREATE INDEX IF NOT EXISTS ann_index 
  ON cycling.comments_vs(comment_vector) USING 'sai';
```

# Query vector data with CQL

To query data using Vector Search, use a `SELECT` query: 

CQL::
+
--
```cql
SELECT * FROM cycling.comments_vs 
    ORDER BY comment_vector ANN OF [0.15, 0.1, 0.1, 0.35, 0.55] 
    LIMIT 3;

```
--
Result::
+
--
```cql
 id                                   | created_at                      | comment                                | comment_vector               | commenter | record_id
--------------------------------------+---------------------------------+----------------------------------------+------------------------------+-----------+--------------------------------------
 e7ae5cf3-d358-4d99-b900-85902fda9bb0 | 2017-04-01 14:33:02.160000+0000 | LATE RIDERS SHOULD NOT DELAY THE START | [0.9, 0.54, 0.12, 0.1, 0.95] |      Alex | 616e77e0-22a2-11ee-b99d-1f350647414a
 c7fceba0-c141-4207-9494-a29f9809de6f | 2017-02-17 08:43:20.234000+0000 |      Glad you ran the race in the rain | [0.3, 0.34, 0.2, 0.78, 0.25] |       Amy | 6170c1d0-22a2-11ee-b99d-1f350647414a
 c7fceba0-c141-4207-9494-a29f9809de6f | 2017-04-01 13:43:08.030000+0000 |                Last climb was a killer |   [0.3, 0.75, 0.2, 0.2, 0.5] |       Amy | 62105d30-22a2-11ee-b99d-1f350647414a
```
--

**Note:**
The limit has to be 1,000 or fewer.

Scrolling to the right on the results shows the comments from the table that most closely matched the embeddings used for the query.
