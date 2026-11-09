<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_single-index-match.adoc (AsciiDoc). Includes are inlined. -->

# Single index match on a column

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

The column `commenter` is not the partition key in this table, so an index is required to query on it.

Query for a match on that column:

Query::
+
--
```console
    SELECT * FROM cycling.comments_vs 
        WHERE commenter = 'Alex';
```
--

Result::
+
--
```results
 id                                   | created_at                      | comment                                | comment_vector               | commenter | record_id
--------------------------------------+---------------------------------+----------------------------------------+------------------------------+-----------+--------------------------------------
 e7ae5cf3-d358-4d99-b900-85902fda9bb0 | 2017-04-01 14:33:02.160000+0000 | LATE RIDERS SHOULD NOT DELAY THE START | [0.9, 0.54, 0.12, 0.1, 0.95] |      Alex | 6d0cdaa0-272b-11ee-859f-b9098002fcac
 e7ae5cf3-d358-4d99-b900-85902fda9bb0 | 2017-03-21 21:11:09.999000+0000 |      Second rest stop was out of water | [0.99, 0.5, 0.99, 0.1, 0.34] |      Alex | 6d0b7b10-272b-11ee-859f-b9098002fcac
```
--

.Failure with index
****
Note that a failure will occur if you try this query before creating the index:

Query::
+
--
```console
    SELECT * FROM cycling.comments_vs 
        WHERE commenter = 'Alex';
```
--

Result::
+
--
```results
InvalidRequest: Error from server: code=2200
[Invalid query] message="Cannot execute this query as it might involve data filtering and thus may have unpredictable performance.
If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING"
```
--
****
