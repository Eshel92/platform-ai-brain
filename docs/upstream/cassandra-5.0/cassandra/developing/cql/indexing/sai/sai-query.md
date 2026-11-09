<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/sai-query.adoc (AsciiDoc). Includes are inlined. -->

# Querying with SAI

The SAI quickstart focuses only on defining multiple indexes based on non-primary key columns (a very useful feature).
Let's explore other options using some examples of how you can run queries on tables that have differently defined SAI indexes.

**Important:**
SAI only supports `SELECT` queries, but not `UPDATE` or `DELETE` queries.

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

# Index match on a composite partition key column

This example uses the following table and indexes:

```sql
CREATE TABLE IF NOT EXISTS cycling.rank_by_year_and_name (
CREATE INDEX race_name_idx 
    ON cycling.rank_by_year_and_name (race_name) 
    USING 'sai';
CREATE INDEX race_year_idx 
    ON cycling.rank_by_year_and_name (race_year) 
    USING 'sai';
```

Composite partition keys have a partition defined by multiple columns in a table.
Normally, you would need to specify all the columns in the partition key to query the table with a `WHERE` clause.
However, an SAI index makes it possible to define an index using a single column in the table's composite partition key.
You can create an SAI index on each column in the composite partition key, if you need to query based on just one column.

SAI indexes also allow you to query tables without using the inefficient `ALLOW FILTERING` directive. 
The `ALLOW FILTERING` directive requires scanning all the partitions in a table, leading to poor performance.

The `race_year` and `race_name` columns comprise the composite partition key for the `cycling.rank_by_year_and_name` table.

Query for a match on the column `race_name`:

Query::
+
--
```console
    SELECT * FROM cycling.rank_by_year_and_name 
        WHERE race_name = 'Tour of Japan - Stage 4 - Minami > Shinshu';
```
--

Result::
+
--
```results
 race_year | race_name                                  | rank | cyclist_name
-----------+--------------------------------------------+------+----------------------
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |        Daniel MARTIN
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    2 | Johan Esteban CHAVES
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    3 |      Benjamin PRADES
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |      Benjamin PRADES
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    2 |          Adam PHELAN
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    3 |         Thomas LEBAS
```
--

Query for a match on the column `race_year`:

Query::
+
--
```console
    SELECT * FROM cycling.rank_by_year_and_name 
        WHERE race_year = 2014;
```
--

Result::
+
--
```results

 race_year | race_name                                  | rank | cyclist_name
-----------+--------------------------------------------+------+----------------------
      2014 |                        4th Tour of Beijing |    1 |    Phillippe GILBERT
      2014 |                        4th Tour of Beijing |    2 |        Daniel MARTIN
      2014 |                        4th Tour of Beijing |    3 | Johan Esteban CHAVES
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |        Daniel MARTIN
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    2 | Johan Esteban CHAVES
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    3 |      Benjamin PRADES
```
--

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

# Multiple indexes matched with IN

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

Query for match with column values in a list of values:

Query::
+
--
```console
SELECT * FROM cycling.comments_vs 
    WHERE created_at IN 
    ('2017-03-21 21:11:09.999000+0000' 
    ,'2017-03-22 01:16:59.001000+0000');

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

# User-defined type

SAI can index either a user-defined type (UDT) or a list of UDTs.
This example shows how to index a list of UDTs.

This example uses the following user-defined type (UDT), table and index:

```sql
CREATE TYPE IF NOT EXISTS cycling.race (
CREATE TABLE IF NOT EXISTS cycling.cyclist_races (
CREATE INDEX races_idx 
    ON cycling.cyclist_races (races) 
    USING 'sai';
```

An index is created on the list of UDTs column `races` in the `cycling.cyclist_races` table.

Query with `CONTAINS` from the list `races` column:

CQL::
+
--
```language-cql
SELECT * FROM cycling.cyclist_races 
    WHERE races CONTAINS {
       race_title:'Rabobank 7-Dorpenomloop Aalburg',
       race_date:'2015-05-09',
       race_time:'02:58:33'};
```
--

Result::
+
--
```console
 id                                   | firstname | lastname | races
--------------------------------------+-----------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |  Marianne |      VOS | [{race_title: 'Rabobank 7-Dorpenomloop Aalburg', race_date: '2015-05-09 00:00:00.000000+0000', race_time: '02:58:33'}, {race_title: 'Ronde van Gelderland', race_date: '2015-04-19 00:00:00.000000+0000', race_time: '03:22:23'}]

(1 rows)
```
--

# SAI indexing with collections

[[saiUsingCollections]]

SAI supports collections of type `map`, `list`, and `set`.
Collections allow you to group and store data together in a column.

In a relational database, a grouping such as a user's multiple email addresses is achieved via many-to-one joined relationship between (for example) a `user` table and an `email` table.
{product} avoids joins between two tables by storing the user's email addresses in a collection column in the `user` table.
Each collection specifies the data type of the data held.

A collection is appropriate if the data for collection storage is limited.
If the data has unbounded growth potential, like messages sent or sensor events registered every second, do not use collections.
Instead, use a table with a compound primary key where data is stored in the clustering columns.

**Tip:**
In CQL queries of database tables with SAI indexes, the `CONTAINS` clauses are supported with, and specific to:

* SAI *collection maps* with `keys`, `values`, and `entries`
* SAI *collections* with `list` and `set` types

[[saiUsingCollectionsSetExamples]]

# Using the set type

This example uses the following table and index:

```sql
CREATE TABLE IF NOT EXISTS cycling.cyclist_career_teams (
CREATE INDEX teams_idx 
    ON cycling.cyclist_career_teams (teams) 
    USING 'sai';
```

An index is created on the set column `teams` in the `cyclist_career_teams` table.

Query with `CONTAINS` from the set `teams` column:

CQL::
+
--
```language-cql
SELECT * FROM cycling.cyclist_career_teams 
   WHERE teams CONTAINS 'Rabobank-Liv Giant';
```
--

Result::
+
--
```console
 id                                   | lastname | teams
--------------------------------------+----------+------------------------------------------------------------------------------------------------------
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |      VOS | {'Nederland bloeit', 'Rabobank Women Team', 'Rabobank-Liv Giant', 'Rabobank-Liv Woman Cycling Team'}
```
--
[[saiUsingCollectionsListExamples]]

# Using the list type

This example uses the following table and index:

```sql
CREATE TABLE IF NOT EXISTS cycling.upcoming_calendar (
CREATE INDEX events_idx 
    ON cycling.upcoming_calendar (events) 
    USING 'sai';
```

An index is created on the list column `events` in the `upcoming_calendar` table.

Query with `CONTAINS` from the list `events` column:

CQL::
+
--
```language-cql
SELECT * FROM cycling.upcoming_calendar 
   WHERE events CONTAINS 'Criterium du Dauphine';
```
--

Result::
+
--
```console
 year | month | events
------+-------+-----------------------------------------------
 2015 |     6 | ['Criterium du Dauphine', 'Tour de Sui\nsse']
```
--

A slightly more complex query selects rows that either contain a particular event or have a particular month date:

CQL::
+
--
```language-cql
SELECT * FROM cycling.upcoming_calendar
    WHERE events CONTAINS 'Criterium du Dauphine' 
          OR month = 7;
```
--

Result::
+
--
```console
 year | month | events
------+-------+-----------------------------------------------
 2015 |     6 | ['Criterium du Dauphine', 'Tour de Sui\nsse']
 2015 |     7 |                            ['Tour de France']
```
--
[[saiUsingCollectionsMapExamples]]

# Using the map type

This example uses the following table and indexes:

```sql
CREATE TABLE IF NOT EXISTS cycling.cyclist_teams (
CREATE INDEX IF NOT EXISTS team_year_keys_idx
CREATE INDEX IF NOT EXISTS team_year_entries_idx
CREATE INDEX IF NOT EXISTS team_year_values_idx
```

Indexes created on the map column `teams` in the `cyclist_career_teams` table target the keys, values, and full entries of the column data.

Query with `KEYS` from the map `teams` column:

CQL::
+
--
```language-cql
SELECT * FROM cyclist_teams WHERE teams CONTAINS KEY 2014;
```
--

Result::
+
--
```console
 id                                   | firstname | lastname   | teams
--------------------------------------+-----------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 | Elizabeth | ARMITSTEAD | {2011: 'Team Garmin - Cervelo', 2012: 'AA Drink - Leontien.nl', 2013: 'Boels:Dolmans Cycling Team', 2014: 'Boels:Dolmans Cycling Team', 2015: 'Boels:Dolmans Cycling Team'}
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |  Marianne |        VOS |                                                                                          {2014: 'Rabobank-Liv Woman Cycling Team', 2015: 'Rabobank-Liv Woman Cycling Team'}
```
--

Query a value from the map `teams` column, noting that only the keyword `CONTAINS` is included: 

CQL::
+
--
```language-cql
SELECT * FROM cyclist_teams WHERE teams CONTAINS 'Team Garmin - Cervelo';
```
--

Result::
+
--
```console
 id                                   | firstname | lastname   | teams
--------------------------------------+-----------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 | Elizabeth | ARMITSTEAD | {2011: 'Team Garmin - Cervelo', 2012: 'AA Drink - Leontien.nl', 2013: 'Boels:Dolmans Cycling Team', 2014: 'Boels:Dolmans Cycling Team', 2015: 'Boels:Dolmans Cycling Team'}
```
--

Query entries from the map `teams` column, noting the difference in the `WHERE` clause: 

CQL::
+
--
```language-cql
SELECT * FROM cyclist_teams 
WHERE 
    teams[2014] = 'Boels:Dolmans Cycling Team' 
    AND teams[2015] = 'Boels:Dolmans Cycling Team';
```
--

Result::
+
--
```console
 id                                   | firstname | lastname   | teams
--------------------------------------+-----------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 | Elizabeth | ARMITSTEAD | {2011: 'Team Garmin - Cervelo', 2012: 'AA Drink - Leontien.nl', 2013: 'Boels:Dolmans Cycling Team', 2014: 'Boels:Dolmans Cycling Team', 2015: 'Boels:Dolmans Cycling Team'}
```
--

This example looks for a row where two entries are present in the map `teams` column.
For more information, see:

* CREATE CUSTOM INDEX
* Creating collections
* Using set type
* Using list type
* Using map type
