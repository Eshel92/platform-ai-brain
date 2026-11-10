<!-- Converted from sql/language/syntax/commands/show-functions.asciidoc (AsciiDoc). Includes are inlined. -->

### SHOW FUNCTIONS

**Synopsis:**
```sql
SHOW FUNCTIONS [LIKE pattern]? <1>
```

<1> SQL match pattern

*Description*: List all the SQL functions and their type. The `LIKE` clause can be used to restrict the list of names to the given pattern.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showFunctions]
```

The list of functions returned can be customized based on the pattern.

It can be an exact match:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showFunctionsLikeExact]
```

A wildcard for exactly one character:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showFunctionsLikeChar]
```

A wildcard matching zero or more characters:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showFunctionsLikeWildcard]
```

Or of course, a variation of the above:
```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[showFunctionsWithPattern]
```
