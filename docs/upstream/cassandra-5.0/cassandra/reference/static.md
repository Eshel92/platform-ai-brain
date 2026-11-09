<!-- Converted from modules/cassandra/pages/reference/static.adoc (AsciiDoc). Includes are inlined. -->

# Creating columns with a single value (static column)

Static column values are shared among the rows in the partition.
In a table that uses [clustering columns](https://cassandra.apache.org/\_/glossary.html#clustering-column), non-clustering columns can be declared static in the table definition.
[Static columns](https://cassandra.apache.org/_/glossary.html#static-column) are only static within a given partition.

In the following example, the `flag` column is static:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.country_flag (
```

```language-cql
INSERT INTO cycling.country_flag (
```

CQL::
+
--
```language-cql
SELECT *
```
--

Result::
+
--
```language-cql
 country | cyclist_name | flag
---------+--------------+------
 Belgium |        Andre |    1
 Belgium |      Jacques |    1
  France |        Andre |    3
  France |       George |    3

(4 rows)

```
--

**Important:**
The following restrictions apply:

* A table that does not define any clustering columns cannot have a static column.
The table that does not have clustering columns has a one-row partition in which every column is inherently static.
* A column designated to be the partition key cannot be static.

You can do batch conditional updates to a static column.

Use the `DISTINCT` keyword to select static columns.
In this case, the database retrieves only the beginning (static column) of the partition.
