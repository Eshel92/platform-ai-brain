<!-- Converted from sql/language/syntax/commands/show-tables.asciidoc (AsciiDoc). Includes are inlined. -->

### SHOW TABLES

**Synopsis:**
```sql
SHOW TABLES
    [CATALOG [catalog_identifier | <1>
              LIKE pattern]]?      <2>
    [INCLUDE FROZEN]?              <3>
    [table_identifier |            <4>
     LIKE pattern]?                <5>
```

<1> Catalog (cluster) identifier. Supports wildcards (`*`).
<2> SQL LIKE pattern matching catalog names.
<3> Whether or not to include frozen indices.
<4> Single table (index or data stream) identifier or double-quoted multi-target pattern.
<5> SQL LIKE pattern matching table names.

See index patterns for more information about
patterns.

*Description*: List the tables available to the current user and their type.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showTables]
```

Match multiple indices by using Elasticsearch multi-target syntax
notation:

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showTablesEsMultiIndex]
```

One can also use the `LIKE` clause to restrict the list of names to the given pattern.

The pattern can be an exact match:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showTablesLikeExact]
```

Multiple chars:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showTablesLikeWildcard]
```

A single char:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showTablesLikeOneChar]
```

Or a mixture of single and multiple chars:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showTablesLikeMixed]
```

List tables within remote clusters whose names are matched by a wildcard:
```sql
include-tagged::{sql-specs}/multi-cluster-with-security/multi-cluster-command.csv-spec[showTablesCatalogPatternMultiLike]
```
