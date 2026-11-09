<!-- Converted from modules/cassandra/pages/developing/cql/indexing/sai/_user-defined-type-match.adoc (AsciiDoc). Includes are inlined. -->

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
