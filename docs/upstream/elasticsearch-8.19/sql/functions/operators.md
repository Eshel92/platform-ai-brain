<!-- Converted from sql/functions/operators.asciidoc (AsciiDoc). Includes are inlined. -->

### Comparison Operators

Boolean operator for comparing against one or multiple expressions.

#### `Equality (=)`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereFieldEquality]
```

#### `Null safe Equality (<=>)`

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[nullEqualsCompareWithNull]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[nullEqualsCompareTwoNulls]
```

#### `Inequality (<> or !=)`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereFieldNonEquality]
```

#### `Comparison (<, <=, >, >=)`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereFieldLessThan]
```

#### `BETWEEN`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereBetween]
```

#### `IS NULL/IS NOT NULL`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereIsNotNullAndIsNull]
```

#### `IN (<value1>, <value2>, ...)`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereWithInAndMultipleValues]
```

### Logical Operators

Boolean operator for evaluating one or two expressions.

#### `AND`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereFieldAndComparison]
```

#### `OR`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereFieldOrComparison]
```

#### `NOT`

```sql
include-tagged::{sql-specs}/filter.sql-spec[whereFieldEqualityNot]
```

### Math Operators

Perform mathematical operations affecting one or two values.
The result is a value of numeric type.

#### `Add (+)`

```sql
include-tagged::{sql-specs}/arithmetic.sql-spec[plus]
```

#### `Subtract (infix -)`

```sql
include-tagged::{sql-specs}/arithmetic.sql-spec[minus]
```

#### `Negate (unary -)`

```sql
include-tagged::{sql-specs}/arithmetic.sql-spec[unaryMinus]
```

#### `Multiply (*)`

```sql
include-tagged::{sql-specs}/arithmetic.sql-spec[multiply]
```

#### `Divide (/)`

```sql
include-tagged::{sql-specs}/arithmetic.sql-spec[divide]
```

#### `Modulo or Remainder(%)`

```sql
include-tagged::{sql-specs}/arithmetic.sql-spec[mod]
```

### Cast Operators

#### `Cast (::)`

`::` provides an alternative syntax to the sql-functions-type-conversion-cast function.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[conversionStringToLongCastOperator]
```
