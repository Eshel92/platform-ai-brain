<!-- Converted from modules/cassandra/pages/developing/cql/drop-index.adoc (AsciiDoc). Includes are inlined. -->

# DROP INDEX

Removes an existing index.
The default index name is `table_name_column_name_idx`.

## Synopsis

```
DROP INDEX [ IF EXISTS ] [<keyspace_name>.]<index_name> ;
```

.Syntax legend
include:cassandra:partial$cql-syntax-legend.adoc[]

## Example

Drop the index `rank_idx` from the `cycling.rank_by_year_and_name` table.

```language-cql
DROP INDEX IF EXISTS cycling.rank_idx;
```
