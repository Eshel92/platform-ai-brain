<!-- Converted from modules/cassandra/pages/developing/cql/indexing/2i/_2i-create-on-collection.adoc (AsciiDoc). Includes are inlined. -->

# Create a 2i on a collection column

Collections can be indexed and queried to find a collection containing a particular value.
Sets and lists are indexed a bit differently from maps, given the key-value nature of maps.

Sets and lists can index all values found by indexing the collection column.
Maps can index a map key, map value, or map entry using the methods shown below.
Multiple indexes can be created on the same map column in a table so that map keys, values, or entries can be queried.
In addition, frozen collections can be indexed using `FULL` to index the full content of a frozen collection.

**Note:**
All the cautions about using secondary indexes apply to indexing collections.

* For set and list collections, create an index on the column name.
Create an index on a set to find all the cyclists that have been on a particular team.

```language-cql
CREATE INDEX IF NOT EXISTS teams_idx
```

```language-cql
SELECT *
```

```results
 id                                   | lastname | teams
--------------------------------------+----------+-----------------------------------------------------------------------------
-----------------------
 1c9ebc13-1eab-4ad5-be87-dce433216d40 |    BRAND | {'AA Drink - Leontien.nl', 'Leontien.nl', 'Rabobank-Liv Giant', 'Rabobank-Li
v Woman Cycling Team'}

(1 rows)
```

* For map collections, create an index on the map key, map value, or map entry.
Create an index on a map key to find all cyclist/team combinations for a particular year.

```language-cql
CREATE INDEX IF NOT EXISTS team_year_keys_idx
```

```language-cql
SELECT *
```

```results
 id                                   | firstname | lastname   | teams
--------------------------------------+-----------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 | Elizabeth | ARMITSTEAD | {2011: 'Team Garmin - Cervelo', 2012: 'AA Drink - Leontien.nl', 2013: 'Boels:Dolmans Cycling Team', 2014: 'Boels:Dolmans Cycling Team', 2015: 'Boels:Dolmans Cycling Team'}
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |  Marianne |        VOS |                                                                                                                                   {2015: 'Rabobank-Liv Woman Cycling Team'}

(2 rows)

```

* Create an index on the map entries and find cyclists who are the same age.
An index using `ENTRIES` is only valid for maps.

```language-cql
CREATE TABLE IF NOT EXISTS cycling.birthday_list (
```

```language-cql
CREATE INDEX IF NOT EXISTS blist_idx
```

```language-cql
SELECT *
```

```results
 cyclist_name     | blist
------------------+----------------------------------------------------------
   Claudio HEINEN | {'age': '23', 'bday': '27/07/1992', 'nation': 'GERMANY'}
 Laurence BOURQUE |  {'age': '23', 'bday': '27/07/1992', 'nation': 'CANADA'}

(2 rows)

```

* Using the same index, find cyclists from the same country.

```language-cql
SELECT *
```

```results
 cyclist_name  | blist
---------------+--------------------------------------------------------------
 Luc HAGENAARS | {'age': '28', 'bday': '27/07/1987', 'nation': 'NETHERLANDS'}
   Toine POELS | {'age': '52', 'bday': '27/07/1963', 'nation': 'NETHERLANDS'}

(2 rows)

```

* Create an index on the map values and find cyclists who have a particular value found in the specified map.

```language-cql
CREATE TABLE IF NOT EXISTS cycling.birthday_list (
```

```language-cql
CREATE INDEX IF NOT EXISTS blist_values_idx
```

```language-cql
SELECT *
```
+
```results
 cyclist_name  | blist
---------------+--------------------------------------------------------------
 Luc HAGENAARS | {'age': '28', 'bday': '27/07/1987', 'nation': 'NETHERLANDS'}
   Toine POELS | {'age': '52', 'bday': '27/07/1963', 'nation': 'NETHERLANDS'}

(2 rows)

```

* Create an index on the full content of a `FROZEN` map.
The table in this example stores the number of Pro wins, Grand Tour races, and Classic races that a cyclist has competed in.
The SELECT statement finds any cyclist who has 39 Pro race wins, 7 Grand Tour starts, and 14 Classic starts.

```language-cql
CREATE TABLE IF NOT EXISTS cycling.race_starts (
```

```language-cql
CREATE INDEX IF NOT EXISTS rnumbers_idx
```

```language-cql
SELECT *
```

```results
 cyclist_name   | rnumbers
----------------+-------------
 John DEGENKOLB | [39, 7, 14]

(1 rows)
```
