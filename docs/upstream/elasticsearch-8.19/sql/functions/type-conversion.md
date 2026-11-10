<!-- Converted from sql/functions/type-conversion.asciidoc (AsciiDoc). Includes are inlined. -->

### Type Conversion Functions

Functions for converting an expression of one data type to another.

#### `CAST`

**Synopsis:**
```sql
CAST(
    expression <1>
 AS data_type) <2>
```

<1> Expression to cast. If `null`, the function returns `null`.
<2> Target data type to cast to

*Description*: Casts the result of the given expression to the target data type.
If the cast is not possible (for example because of target type is too narrow or because
the value itself cannot be converted), the query fails.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[conversionStringToIntCast]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[conversionIntToStringCast]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[conversionStringToDateTimeCast]
```

**Important:** Both ANSI SQL and {es-sql} types are supported with the former taking
precedence. This only affects `FLOAT` which due naming conflict, is interpreted as ANSI SQL 
and thus maps to `double` in Elasticsearch as oppose to `float`.
To obtain an Elasticsearch `float`, perform casting to its SQL equivalent, `real` type.

#### `CONVERT`

**Synopsis:**
```sql
CONVERT(
    expression, <1>
    data_type)  <2>
```

<1> Expression to convert. If `null`, the function returns `null`.
<2> Target data type to convert to

*Description*: Works exactly like sql-functions-type-conversion-cast with slightly different syntax.
Moreover, apart from the standard data types it supports the corresponding
[ODBC data types](https://docs.microsoft.com/en-us/sql/odbc/reference/appendixes/explicit-data-type-conversion-function?view=sql-server-2017).

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[conversionStringToIntConvertODBCDataType]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[conversionStringToIntConvertESDataType]
```
