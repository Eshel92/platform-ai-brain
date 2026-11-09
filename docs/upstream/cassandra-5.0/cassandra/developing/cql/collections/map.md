<!-- Converted from modules/cassandra/pages/developing/cql/collections/map.adoc (AsciiDoc). Includes are inlined. -->

# Using map type

A map relates one item to another with a key-value pair.
For each key, only one value may exist, and duplicates cannot be stored.
Both the key and the value are designated with a data type.

Using the map type, you can store timestamp-related information in user profiles.
Each element of the map is internally stored as a single column that you can modify, replace, delete, and query.
Each element can have an individual time-to-live and expire when the TTL ends.

## Prerequisite

* Keyspace must exist

In the following example, each team listed in the `map` called `teams` will have a `year` of integer type and a `team name` of text type.
The table is named `cyclist_teams`.
The map collection is specified with a map column name and the pair of data types enclosed in angle brackets.

CQL::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_teams (
```
--

Result::
+
--
```results
 id                                   | firstname | lastname | teams
--------------------------------------+-----------+----------+---------------------------------------------------------------------------
---------
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |  Marianne |      VOS | {2014: 'Rabobank-Liv Woman Cycling Team', 2015: 'Rabobank-Liv Woman Cyclin
g Team'}

(1 rows)

```
--
