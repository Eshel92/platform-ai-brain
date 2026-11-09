<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_collections-set.adoc (AsciiDoc). Includes are inlined. -->

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
