<!-- Converted from modules/cassandra/pages/reference/cql-commands/create-index.adoc (AsciiDoc). Includes are inlined. -->

# CREATE INDEX

Defines a new secondary index (2i) or storage-attached index (SAI) for a single column of a table.

{product} supports creating a secondary index or storage-attached index on most columns, including the partition and cluster columns of a `PRIMARY KEY`, collections, and static columns. 
For maps, you can index using the key, value, or entries (a key:value pair).

All column date types except the following are supported for SAI indexes:

* `counter`
* non-frozen user-defined type (UDT)

.One exception 
****
You cannot define an SAI index based on the partition key when it's comprised of only one column.
If you attempt to create an SAI index in this case, SAI issues an error message.
****

*See also:* CREATE CUSTOM INDEX for Storage-Attached Indexes (SAI), DROP INDEX

## Syntax

BNF definition:

```bnf
index_name::= re('[a-zA-Z_0-9]+')

```

```
CREATE INDEX [ IF NOT EXISTS ] <index_name>
  ON [<keyspace_name>.]<table_name> 
  ( [ ( KEYS | FULL | ENTRIES ) ] <column_name>)
    //   | [ (KEYS(<map_name>)) ]
    // | [ (VALUES(<map_name>)) ]
    // | [ (ENTRIES(<map_name>)) ]
   [USING 'sai']
  [ WITH OPTIONS = { <option_map> } ];
```

.Syntax legend
.Legend
|===
| Syntax conventions | Description

| UPPERCASE
| Literal keyword.

| Lowercase
| Not literal.

| `< >`
| Variable value.
Replace with a user-defined value.

| `[]`
| Optional.
Square brackets (`[]`) surround optional command arguments.
Do not type the square brackets.

| `( )`
| Group.
Parentheses ( `( )` ) identify a group to choose from.
Do not type the parentheses.

| `\|`
| Or.
A vertical bar (`\|`) separates alternative elements.
Type any one of the elements.
Do not type the vertical bar.

| `...`
| Repeatable.
An ellipsis ( `...` ) indicates that you can repeat the syntax element as often as required.

| `'<Literal string>'`
| Single quotation (`'`) marks must surround literal strings in CQL statements.
Use single quotation marks to preserve upper case.

| `{ <key> : <value> }`
| Map collection.
Braces (`{ }`) enclose map collections or key value pairs.
A colon separates the key and the value.

| `< <datatype1>,<datatype2> >`
| Set, list, map, or tuple.
Angle brackets ( `< >` ) enclose data types in a set, list, map, or tuple.
Separate the data types with a comma.

| `<cql_statement>;`
| End CQL statement.
A semicolon (`;`) terminates all CQL statements.

| `[--]`
| Separate the command line options from the command arguments with two hyphens ( `--` ).
This syntax is useful when arguments might be mistaken for command line options.

| `+' <<schema\> ...
</schema\>> '+`
| Search CQL only: Single quotation marks (`'`) surround an entire XML schema declaration.

| `@<xml_entity>='<xml_entity_type>'`
| Search CQL only: Identify the entity and literal value to overwrite the XML element in the schema and solrConfig files.
|===

## Required parameters

|===

| Parameter | Description

| table_name
| Name of the table to index.

| column_name
| Name of the column to index.
SAI allows only alphanumeric characters and underscores in names.
SAI returns `InvalidRequestException` if you try to define an index on a column name that contains other characters, and does not create the index.
|===

## Optional parameters

|===

| Parameter | Description

| index_name
| Name of the index.
Enclose in quotes to use special characters or preserve capitalization.
If no name is specified, {product} names the index as `<table_name>\_<column_name>\_idx`.

| keyspace_name
| Name of the keyspace that contains the table to index.
If no name is specified, the current keyspace is used.

| map_name
| Used with collections, identifier of the `map_name` specified in `CREATE TABLE` ...
`map(<map_name>)`.
The regular column syntax applies for collection types `list` and `set`.
|===

|============================
|option_map 2+<|Define options in JSON simple format.
.4+||`case_sensitive` |Ignore case in matching string values. Default: `true`
|`normalize`|When set to `true`, perform [Unicode normalization](https://unicode.org/faq/normalization.html) on indexed strings.
SAI supports Normalization Form C (NFC) Unicode.
When set to `true`, SAI normalizes the different versions of a given Unicode character to a single version, retaining all the marks and symbols in the index.
For example, SAI would change the character Å (U212B) to Å (U00C5).

When implementations keep strings in a normalized form, equivalent strings have a unique binary representation.
See [Unicode Standard Annex #15, Unicode Normalization Forms](https://unicode.org/reports/tr15/).

Default: `false`.
|`ascii` |When set to `true`, SAI converts alphabetic, numeric, and symbolic characters that are not in the Basic Latin Unicode block (the first 127 ASCII characters) to the ASCII equivalent, if one exists.
For example, this option changes à to a.
Default: `false`.
|`similarity_function` |Vector search relies on computing the similarity or distance between vectors to identify relevant matches.
The similarity function is used to compute the similarity between two vectors.
Valid options are: `EUCLIDEAN`, `DOT_PRODUCT`, `COSINE`
Default: `COSINE`
|============================

## Usage notes

If the column already contains data, it is indexed during the execution of this statement.
After an index has been created, it is automatically updated when data in the column changes.

Indexing with the `CREATE INDEX` command can impact performance.
Before creating an index, be aware of when and when not to create an index.

*Restriction:* Indexing counter columns is not supported.

### SAI indexes

You can define an SAI index on one of the columns in a table's composite partition key, i.e., a partition key comprised of multiple columns.
If you need to query based on one of those columns, an SAI index is a helpful option. 
In fact, you can define an SAI index on each column in a composite partition key, if needed.

Defining one or more SAI indexes based on any column in a database table allows queries to use the indexed column to filter results. 

### SAI query operators

SAI supports the following query operators for tables with SAI indexes:

ifeval::["{evalproduct}" == "dse"]
* Numerics: `=`, `<`, `>`, `<=`, `>=`, `AND`
* Strings: `=`, `CONTAINS`, `CONTAINS KEY`, `AND`
ifeval::["{evalproduct}" != "dse"]
* Numerics: `=`, `<`, `>`, `<=`, `>=`, `AND`, `OR`, `IN`
* Strings: `=`, `CONTAINS`, `CONTAINS KEY`, `AND`, `OR`, `IN`

SAI does not support the following query operators for tables with SAI indexes:

ifeval::["{evalproduct}" == "dse"]
* Strings or Numerics: `LIKE`, `OR`, `IN`
ifeval::["{evalproduct}" != "dse"]
* Strings or Numerics: `LIKE`

See the SAI section.

## Examples

### Creating a SAI index on a clustering column

Define a table having a composite partition key, and then create an index on a clustering column.

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.rank_by_year_and_name (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS rank_idx
```
--

SELECT query::
+
--
```language-cql
SELECT * FROM rank_by_year_and_name WHERE rank = 1;
```
--

SELECT result::
+
--
```language-cql
 race_year | race_name                                  | rank | cyclist_name
-----------+--------------------------------------------+------+-------------------
      2014 |                        4th Tour of Beijing |    1 | Phillippe GILBERT
      2014 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |     Daniel MARTIN
      2015 |   Giro d'Italia - Stage 11 - Forli > Imola |    1 |     Ilnur ZAKARIN
      2015 | Tour of Japan - Stage 4 - Minami > Shinshu |    1 |   Benjamin PRADES

(4 rows)
```
--

### Creating an index on a set or list collection

Create an index on a set or list collection column as you would any other column.
Enclose the name of the collection column in parentheses at the end of the `CREATE INDEX` statement.
For example, add a collection of teams to the `cyclist_career_teams` table to index the data in the teams set.

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_career_teams (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS teams_idx
```
--

SELECT query::
+
--
```language-cql
SELECT * FROM cyclist_career_teams WHERE teams CONTAINS 'Rabobank-Liv Woman Cycling Team';
```
--

SELECT result::
+
--
```language-cql
 id                                   | lastname        | teams
--------------------------------------+-----------------+------------------------------------------------------------------------------------------------------
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |             VOS | {'Nederland bloeit', 'Rabobank Women Team', 'Rabobank-Liv Giant', 'Rabobank-Liv Woman Cycling Team'}
 1c9ebc13-1eab-4ad5-be87-dce433216d40 |           BRAND |   {'AA Drink - Leontien.nl', 'Leontien.nl', 'Rabobank-Liv Giant', 'Rabobank-Liv Woman Cycling Team'}
 e7cd5752-bc0d-4157-a80f-7523add8dbcd | VAN DER BREGGEN |                 {'Rabobank-Liv Woman Cycling Team', 'Sengers Ladies Cycling Team', 'Team Flexpoint'}

(3 rows)
```
--

[[CreatIdxCollKey]]

### Creating an index on map keys

You can create an index on map collection keys.
If an index of the map values of the collection exists, drop that index before creating an index on the map collection keys.
Assume a cyclist table contains this map data where `nation` is the map key and `Canada` is the map value:

```no-highlight
{'nation':'CANADA' }
```

To index map keys, use the `KEYS` keyword and map name in nested parentheses in the CREATE INDEX statement.
To run a `SELECT` query on the table, use CONTAINS KEY in `WHERE` clauses.
This query returns cyclist teams that have an entry for the year 2015.

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_teams (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS team_year_keys_idx
```
--

SELECT query::
+
--
```language-cql
SELECT *
```
--

SELECT result::
+
--
```language-cql
 id                                   | firstname | lastname   | teams
--------------------------------------+-----------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 cb07baad-eac8-4f65-b28a-bddc06a0de23 | Elizabeth | ARMITSTEAD | {2011: 'Team Garmin - Cervelo', 2012: 'AA Drink - Leontien.nl', 2013: 'Boels:Dolmans Cycling Team', 2014: 'Boels:Dolmans Cycling Team', 2015: 'Boels:Dolmans Cycling Team'}
 5b6962dd-3f90-4c93-8f61-eabfa4a803e2 |  Marianne |        VOS |                                                                                                                                   {2015: 'Rabobank-Liv Woman Cycling Team'}

(2 rows)

```
--

### Creating an index on map entries

You can create an index on map entries.
An `ENTRIES` index can be created only on a map column of a table that doesn't have an existing index.

To index collection entries, use the `ENTRIES` keyword and map name in nested parentheses.
To query the map entries in the table, use a `WHERE` clause with the map name and a value.
This query finds cyclists who are the same age.

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.birthday_list (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS blist_idx
```
--

SELECT query::
+
--
```language-cql
SELECT *
```
--

SELECT result::
+
--
```language-cql
 cyclist_name     | blist
------------------+----------------------------------------------------------
   Claudio HEINEN | {'age': '23', 'bday': '27/07/1992', 'nation': 'GERMANY'}
 Laurence BOURQUE |  {'age': '23', 'bday': '27/07/1992', 'nation': 'CANADA'}

(2 rows)

```
--

Use the same index to find cyclists from the same country:

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.birthday_list (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS blist_idx
```
--

SELECT query::
+
--
```language-cql
SELECT *
```
--

SELECT result::
+
--
```language-cql
 cyclist_name  | blist
---------------+--------------------------------------------------------------
 Luc HAGENAARS | {'age': '28', 'bday': '27/07/1987', 'nation': 'NETHERLANDS'}
   Toine POELS | {'age': '52', 'bday': '27/07/1963', 'nation': 'NETHERLANDS'}

(2 rows)

```
--

### Creating an index on map values

To create an index on map values, use the `VALUES` keyword and map name in nested parentheses.
To query the table, use a `WHERE` clause with the map name and the value it contains.

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.birthday_list (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS blist_values_idx
```
--

SELECT query::
+
--
```language-cql
SELECT *
```
--

SELECT result::
+
--
```language-cql
 cyclist_name  | blist
---------------+--------------------------------------------------------------
 Luc HAGENAARS | {'age': '28', 'bday': '27/07/1987', 'nation': 'NETHERLANDS'}
   Toine POELS | {'age': '52', 'bday': '27/07/1963', 'nation': 'NETHERLANDS'}

(2 rows)

```
--

### Creating an index on the full content of a frozen collection

You can create an index on a full `FROZEN` collection.
A `FULL` index can be created on a set, list, or map column of a table that doesn't have an existing index.

Create an index on the full content of a `FROZEN` `list`.
The table in this example stores the number of Pro wins, Grand Tour races, and Classic races that a cyclist has competed in.
To index collection entries, use the `FULL` keyword and collection name in nested parentheses.
For example, index the frozen list `rnumbers`.
To query the table, use a `WHERE` clause with the collection name and values.

CREATE TABLE::
+
--
```language-cql
CREATE TABLE IF NOT EXISTS cycling.race_starts (
```
--

CREATE INDEX::
+
--
```language-cql
CREATE INDEX IF NOT EXISTS rnumbers_idx
```
--

SELECT query::
+
--
```language-cql
SELECT *
```
--

SELECT result::
+
--
```language-cql
 cyclist_name   | rnumbers
----------------+-------------
 John DEGENKOLB | [39, 7, 14]

(1 rows)
```
--
