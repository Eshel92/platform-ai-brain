<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/collections.adoc (AsciiDoc). Includes are inlined. -->

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
