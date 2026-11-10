<!-- Converted from sql/language/syntax/commands/show-columns.asciidoc (AsciiDoc). Includes are inlined. -->

### SHOW COLUMNS

**Synopsis:**
```sql
SHOW COLUMNS
    [CATALOG identifier]? <1>
    [INCLUDE FROZEN]?     <2>
    [FROM | IN]
    [table_identifier |   <3>
     LIKE pattern]        <4>
```

<1> Catalog (cluster) identifier. Supports wildcards (`*`).
<2> Whether or not to include frozen indices.
<3> Single table (index or data stream) identifier or double-quoted multi-target pattern.
<4> SQL LIKE pattern matching table names.

See index patterns for more information about
patterns.

*Description*: List the columns in table and their data type (and other attributes).

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showColumns]
```
