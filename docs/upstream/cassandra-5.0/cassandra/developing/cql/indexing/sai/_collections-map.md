<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_collections-map.adoc (AsciiDoc). Includes are inlined. -->

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
