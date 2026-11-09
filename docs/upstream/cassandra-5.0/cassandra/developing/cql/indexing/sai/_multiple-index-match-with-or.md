<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_multiple-index-match-with-or.adoc (AsciiDoc). Includes are inlined. -->

# Multiple indexes matched with OR

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

Query for a match on either one column or the other:

Query::
+
--
```console
SELECT * FROM cycling.comments_vs 
    WHERE 
    created_at='2017-03-21 21:11:09.999000+0000' 
    OR created_at='2017-03-22 01:16:59.001000+0000';

```
--

Result::
+
--
```results
 id                                   | created_at                      | comment                           | comment_vector               | commenter | record_id
--------------------------------------+---------------------------------+-----------------------------------+------------------------------+-----------+--------------------------------------
 e7ae5cf3-d358-4d99-b900-85902fda9bb0 | 2017-03-21 21:11:09.999000+0000 | Second rest stop was out of water | [0.99, 0.5, 0.99, 0.1, 0.34] |      Alex | 6d0b7b10-272b-11ee-859f-b9098002fcac
 c7fceba0-c141-4207-9494-a29f9809de6f | 2017-03-22 01:16:59.001000+0000 |     Great snacks at all reststops |  [0.1, 0.4, 0.1, 0.52, 0.09] |       Amy | 6d0fc0d0-272b-11ee-859f-b9098002fcac
```
--
