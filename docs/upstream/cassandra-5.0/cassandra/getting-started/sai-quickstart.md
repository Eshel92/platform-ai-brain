<!-- Converted from modules/cassandra/pages/getting-started/sai-quickstart.adoc (AsciiDoc). Includes are inlined. -->

# Storage-attached Indexing (SAI) Quickstart

To get started with Storage-Attached Indexing (SAI), we'll do the following steps:

* Create a keyspace.
* Create a table.
* Create an index using SAI.
* Add data.
* Create and run a query using SAI.

The examples in this quickstart topic show SAI indexes with non-partition key columns.

## Create a keyspace

In `cqlsh`, define the `cycling` keyspace to try the commands in a test environment:

```language-cql
CREATE KEYSPACE IF NOT EXISTS cycling 
   WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };
```

## Create a database table

Using `cqlsh` or the CQL Console, create a `cyclist_semi_pro` database table in the `cycling` keyspace or the keyspace name of your choice:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_semi_pro (
```

## Create SAI indexes on the database table

To test a non-trivial query, you'll need some SAI indexes.
Use CREATE CUSTOM INDEX commands to create SAI indexes on a few non-primary-key columns in the `cyclist_semi_pro` table:

```language-cql
CREATE INDEX lastname_sai_idx ON cycling.cyclist_semi_pro (lastname) 
```

Let's take a look at the description of the table and its indexes:
Query::
+
--
```language-cql
DESCRIBE TABLE cycling.cyclist_semi_pro;
```
--

Result::
+
--
```language-cql
CREATE TABLE cycling.cyclist_semi_pro (
```
--

## Add data to your table

Use CQLSH `INSERT` commands to add some data to the `cyclist_semi_pro` database table:

```language-cql
INSERT INTO cycling.cyclist_semi_pro (id, firstname, lastname, age, affiliation, country, registration) VALUES (1, 'Carlos', 'Perotti', 22, 'Recco Club', 'ITA', '2020-01-12'); 
```

Adding data in this quickstart topic shows simple `INSERT` commands.
To load databases with many rows, consider using [DataStax Bulk Loader for Apache Cassandra](https://docs.datastax.com/en/dsbulk/doc/index.html).

## Try out CQL queries

Use the CQLSH `SELECT` command to submit queries.

**Tip:**
The supported query operators for tables with SAI indexes:
ifeval::["{evalproduct}" == "dse"]
* Numerics: `=`, `<`, `>`, `<=`, `>=`, `AND`
* Strings: `=`, `CONTAINS`, `CONTAINS KEY`, `AND`
ifeval::["{evalproduct}" != "dse"]
* Numerics: `=`, `<`, `>`, `<=`, `>=`, `AND`, `OR`, `IN`
* Strings: `=`, `CONTAINS`, `CONTAINS KEY`, `AND`, `OR`, `IN`

ifeval::["{evalproduct}" == "dse"]
* Strings or Numerics: `LIKE`, `OR`, `IN`
ifeval::["{evalproduct}" != "dse"]
* Strings or Numerics: `LIKE`

Find a specific semi-pro cyclist:

Query::
+
--
```language-cql
SELECT * FROM cycling.cyclist_semi_pro WHERE lastname = 'Eppinger';
```
--

Result::
+
--
```console
 id | affiliation       | age | country | firstname | lastname | registration
```
--

Find semi-pro cyclists whose age is less than or equal to 23:

Query::
+
--
```language-cql
SELECT * FROM cycling.cyclist_semi_pro WHERE age <= 23;
```
--

Result::
+
--
```console
 id | affiliation        | age | country | firstname | lastname | registration
```
--

Find semi-pro cyclists from Great Britain:

Query::
+
--
```language-cql
SELECT * FROM cycling.cyclist_semi_pro WHERE country = 'GBR';
```
--

Result::
+
--
```console
 id | affiliation          | age | country | firstname | lastname  | registration
```
--

Find semi-pro cyclists who registered between a given date range:

Query::
+
--
```language-cql
SELECT * FROM cycling.cyclist_semi_pro WHERE registration > '2010-01-01' AND registration < '2015-12-31' LIMIT 10;
```
--

Result::
+
--
```results
 id | affiliation         | age | country | firstname | lastname | registration
```
--

**Tip:**
For query examples with `CONTAINS` clauses that take advantage of SAI collection maps, lists, and sets, be sure to see SAI collection map examples with keys, values, and entries.

## Removing an SAI index

To remove an SAI index, use `DROP INDEX`.

Example:

```language-cql
DROP INDEX IF EXISTS cycling.age_sai_idx;
```

## Resources

SAI overview
