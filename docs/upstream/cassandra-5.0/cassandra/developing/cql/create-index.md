<!-- Converted from modules/cassandra/pages/developing/cql/create-index.adoc (AsciiDoc). Includes are inlined. -->

# CREATE INDEX

Define a new index on a single column of a table.
If the column already contains data, it is indexed during the execution of this statement.
After an index has been created, it is automatically updated when data in the column changes.
{product} supports creating an index on most columns, including the partition and cluster columns of a PRIMARY KEY, collections, and static columns.
Indexing via this `CREATE INDEX` command can impact performance.
Before creating an index, be aware of when and when not to create an index.

Use CREATE CUSTOM INDEX for Storage-Attached Indexes (SAI).

*Restriction:* Indexing counter columns is not supported.
For maps, index the key, value, or entries.

## Synopsis

```
CREATE INDEX [ IF NOT EXISTS ] <index_name>
  ON [<keyspace_name>.]<table_name>
  ([ ( KEYS | FULL ) ] <column_name>)
  (ENTRIES <column_name>) ;
```

.Syntax legend
include:cassandra:partial$cql-syntax-legend.adoc[]

*index_name*::
Optional identifier for index.
If no name is specified, DataStax Enterprise
names the index: `<table_name>_<column_name>_idx`.
Enclose in quotes to use special characters or preserve capitalization.

## Examples

### Creating an index on a clustering column

Define a table having a composite partition key, and then create an index on a clustering column.

```language-cql
CREATE TABLE IF NOT EXISTS cycling.rank_by_year_and_name (
```

```language-cql
CREATE INDEX IF NOT EXISTS rank_idx
```

### Creating an index on a set or list collection

Create an index on a set or list collection column as you would any other column.
Enclose the name of the collection column in parentheses at the end of the `CREATE INDEX` statement.
For example, add a collection of teams to the `cyclist_career_teams` table to index the data in the teams set.

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_career_teams (
```

```language-cql
CREATE INDEX IF NOT EXISTS teams_idx
```

[[CreatIdxCollKey]]

### Creating an index on map keys

You can create an index on map collection keys.
If an index of the map values of the collection exists, drop that index before creating an index on the map collection keys.
Assume a cyclist table contains this map data:

```no-highlight
{'nation':'CANADA' }
```

The map key is located to the left of the colon, and the map value is located to the right of the colon.

To index map keys, use the `KEYS` keyword and map name in nested parentheses:

```language-cql
CREATE INDEX IF NOT EXISTS team_year_keys_idx
```

To query the table, you can use CONTAINS KEY in `WHERE` clauses.

```language-cql
SELECT *
```

The example returns cyclist teams that have an entry for the year 2015.

```results
 id                                   | firstname | lastname   | teams
--------------------------------------+-----------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 | Elizabeth | ARMITSTEAD | {2011: 'Team Garmin - Cervelo', 2012: 'AA Drink - Leontien.nl', 2013: 'Boels:Dolmans Cycling Team', 2014: 'Boels:Dolmans Cycling Team', 2015: 'Boels:Dolmans Cycling Team'}
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |  Marianne |        VOS |                                                                                                                                   {2015: 'Rabobank-Liv Woman Cycling Team'}

(2 rows)

```

### Creating an index on map entries

You can create an index on map entries.
An `ENTRIES` index can be created only on a map column of a table that doesn't have an existing index.

To index collection entries, use the `ENTRIES` keyword and map name in nested parentheses:

CREATE INDEX IF NOT EXISTS blist_idx
```language-cql

To query the map entries in the table, use a `WHERE` clause with the map name and a value.

[source,language-cql]
```
SELECT *
```

The example finds cyclists who are the same age.

[source,results]
```
 cyclist_name     | blist
------------------+----------------------------------------------------------
   Claudio HEINEN | {'age': '23', 'bday': '27/07/1992', 'nation': 'GERMANY'}
 Laurence BOURQUE |  {'age': '23', 'bday': '27/07/1992', 'nation': 'CANADA'}

(2 rows)

```

Use the same index to find cyclists from the same country.

```
SELECT *
```

[source,results]
```
 cyclist_name  | blist
---------------+--------------------------------------------------------------
 Luc HAGENAARS | {'age': '28', 'bday': '27/07/1987', 'nation': 'NETHERLANDS'}
   Toine POELS | {'age': '52', 'bday': '27/07/1963', 'nation': 'NETHERLANDS'}

(2 rows)

```

=== Creating an index on map values

To create an index on map values, use the `VALUES` keyword and map name in nested parentheses:

```
CREATE INDEX IF NOT EXISTS blist_values_idx
```

To query the table, use a `WHERE` clause with the map name and the value it contains.

```
SELECT *
```

[source,results]
```
 cyclist_name  | blist
---------------+--------------------------------------------------------------
 Luc HAGENAARS | {'age': '28', 'bday': '27/07/1987', 'nation': 'NETHERLANDS'}
   Toine POELS | {'age': '52', 'bday': '27/07/1963', 'nation': 'NETHERLANDS'}

(2 rows)

```

=== Creating an index on the full content of a frozen collection

You can create an index on a full `FROZEN` collection.
A `FULL` index can be created on a set, list, or map column of a table that doesn't have an existing index.

Create an index on the full content of a `FROZEN` `list`.
The table in this example stores the number of Pro wins, Grand Tour races, and Classic races that a cyclist has competed in.

[source,language-cql]
```
CREATE TABLE IF NOT EXISTS cycling.race_starts (
```

To index collection entries, use the `FULL` keyword and collection name in nested parentheses.
For example, index the frozen list `rnumbers`.

[source,language-cql]
```
CREATE INDEX IF NOT EXISTS rnumbers_idx
```

To query the table, use a `WHERE` clause with the collection name and values:

[source,language-cql]
```
SELECT *
```

[source,results]
```
 cyclist_name   | rnumbers
----------------+-------------
 John DEGENKOLB | [39, 7, 14]

(1 rows)
```
