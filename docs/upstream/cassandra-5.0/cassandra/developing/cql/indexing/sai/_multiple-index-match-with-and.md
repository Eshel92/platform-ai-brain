<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_multiple-index-match-with-and.adoc (AsciiDoc). Includes are inlined. -->

# Multiple indexes matched with AND

This example uses the following table and indexes:

```sql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
CREATE INDEX commenter_idx 
    ON cycling.comments_vs (commenter) 
    USING 'sai';
CREATE INDEX created_at_idx 
    ON cycling.comments_vs (created_at) 
    USING 'sai';
CREATE INDEX ann_index 
    ON cycling.comments_vs (comment_vector) 
    USING 'sai';

```

Several indexes are created for the table to demonstrate how to query for matches on more than one column.

Query for matches on more than one column, and both columns must match:

Query::
+
--
```console
SELECT * FROM cycling.comments_vs 
    WHERE 
    created_at='2017-03-21 21:11:09.999000+0000' 
    AND commenter = 'Alex';

```
--

Result::
+
--
```results
 id                                   | created_at                      | comment                           | comment_vector               | commenter | record_id
--------------------------------------+---------------------------------+-----------------------------------+------------------------------+-----------+--------------------------------------
 e7ae5cf3-d358-4d99-b900-85902fda9bb0 | 2017-03-21 21:11:09.999000+0000 | Second rest stop was out of water | [0.99, 0.5, 0.99, 0.1, 0.34] |      Alex | 6d0b7b10-272b-11ee-859f-b9098002fcac
```
--
