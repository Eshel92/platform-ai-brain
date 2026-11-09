<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_single-index-with-case-sensitive.adoc (AsciiDoc). Includes are inlined. -->

# Single index match on a column with options

This example uses the following table and indexes:

```sql
CREATE TABLE IF NOT EXISTS cycling.comments_vs (
CREATE INDEX commenter_cs_idx ON cycling.comments_vs (commenter)
USING 'sai' 
WITH OPTIONS = {'case_sensitive': 'true', 'normalize': 'true', 'ascii': 'true'};
```

## Case-sensitivty

The column `commenter` is not the partition key in this table, so an index is required to query on it.
If we want to check `commenter` as a case-sensitive value, we can use the `case_sensitive` option set to `true`.

Note that no results are returned if you use an inappropriately case-sensitive value in the query:

Query::
+
--
```console
SELECT * FROM comments_vs WHERE commenter ='alex';
```
--

Result::
+
--
```results
 id | created_at | comment | comment_vector | commenter | record_id
----+------------+---------+----------------+-----------+-----------

(0 rows)
```
--

When we switch the case of the cyclist's name to match the case in the index, the query succeeds:

Query::
+
--
```console
SELECT comment,commenter FROM comments_vs WHERE commenter ='Alex';
```
--

Result::
+
--
```results
 comment                                | commenter
----------------------------------------+-----------
 LATE RIDERS SHOULD NOT DELAY THE START |      Alex
      Second rest stop was out of water |      Alex
(2 rows)
```
--
