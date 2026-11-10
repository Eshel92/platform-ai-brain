<!-- Converted from sql/functions/aggs.asciidoc (AsciiDoc). Includes are inlined. -->

### Aggregate Functions

Functions for computing a _single_ result from a set of input values.
{es-sql} supports aggregate functions only alongside grouping (implicit or explicit).

### General Purpose

#### `AVG`

**Synopsis:**
```sql
AVG(numeric_field) <1>
```

*Input*:

<1> numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*: Returns the [Average](https://en.wikipedia.org/wiki/Arithmetic_mean) (arithmetic mean) of input values.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggAvg]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggAvgScalars]
```

#### `COUNT`

**Synopsis:**
```sql
COUNT(expression) <1>
```

*Input*:

<1> a field name, wildcard (`*`) or any numeric value. For `COUNT(*)` or
`COUNT(<literal>)`, all values are considered, including `null` or missing
ones. For `COUNT(<field_name>)`, `null` values are not considered.

*Output*: numeric value

*Description*: Returns the total number (count) of input values.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggCountStar]
```

#### `COUNT(ALL)`

**Synopsis:**
```sql
COUNT(ALL field_name) <1>
```

*Input*:

<1> a field name. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: numeric value

*Description*: Returns the total number (count) of all _non-null_ input values. `COUNT(<field_name>)` and `COUNT(ALL <field_name>)` are equivalent.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggCountAll]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggCountAllScalars]
```

#### `COUNT(DISTINCT)`

**Synopsis:**
```sql
COUNT(DISTINCT field_name) <1>
```

*Input*:

<1> a field name

*Output*: numeric value. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Description*: Returns the total number of _distinct non-null_ values in input values.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggCountDistinct]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggCountDistinctScalars]
```

#### `FIRST/FIRST_VALUE`

**Synopsis:**
```sql
FIRST(
    field_name               <1>
    [, ordering_field_name]) <2>
```

*Input*:

<1> target field for the aggregation
<2> optional field used for ordering

*Output*: same type as the input

*Description*: Returns the first non-`null` value (if such exists) of the `field_name` input column sorted by
the `ordering_field_name` column. If `ordering_field_name` is not provided, only the `field_name`
column is used for the sorting. E.g.:

|===
s| a    | b

 | 100  | 1
 | 200  | 1
 | 1    | 2
 | 2    | 2
 | 10   | null
 | 20   | null
 | null | null
|===

```sql
SELECT FIRST(a) FROM t
```

will result in:
|===
s| FIRST(a)
 | 1
|===

and

```sql
SELECT FIRST(a, b) FROM t
```

will result in:
|===
s| FIRST(a, b)
 | 100
|===

```
include-tagged::{sql-specs}/docs/docs.csv-spec[firstWithOneArg]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[firstWithOneArgAndGroupBy]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[firstWithTwoArgs]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[firstWithTwoArgsAndGroupBy]
```

`FIRST_VALUE` is a name alias and can be used instead of `FIRST`, e.g.:

```
include-tagged::{sql-specs}/docs/docs.csv-spec[firstValueWithTwoArgsAndGroupBy]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[firstValueWithTwoArgsAndGroupByScalars]
```

`FIRST` cannot be used in a HAVING clause.
`FIRST` cannot be used with columns of type `text` unless
the field is also saved as a keyword.

#### `LAST/LAST_VALUE`

**Synopsis:**
```sql
LAST(
    field_name               <1>
    [, ordering_field_name]) <2>
```

*Input*:

<1> target field for the aggregation
<2> optional field used for ordering

*Output*: same type as the input

*Description*: It's the inverse of sql-functions-aggs-first. Returns the last non-`null` value (if such exists) of the
`field_name` input column sorted descending by the `ordering_field_name` column. If `ordering_field_name` is not
provided, only the `field_name` column is used for the sorting. E.g.:

|===
s| a    | b

 | 10   | 1
 | 20   | 1
 | 1    | 2
 | 2    | 2
 | 100  | null
 | 200  | null
 | null | null
|===

```sql
SELECT LAST(a) FROM t
```

will result in:
|===
s| LAST(a)
 | 200
|===

and

```sql
SELECT LAST(a, b) FROM t
```

will result in:
|===
s| LAST(a, b)
 | 2
|===

```
include-tagged::{sql-specs}/docs/docs.csv-spec[lastWithOneArg]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[lastWithOneArgAndGroupBy]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[lastWithTwoArgs]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[lastWithTwoArgsAndGroupBy]
```

`LAST_VALUE` is a name alias and can be used instead of `LAST`, e.g.:

```
include-tagged::{sql-specs}/docs/docs.csv-spec[lastValueWithTwoArgsAndGroupBy]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[lastValueWithTwoArgsAndGroupByScalars]
```

`LAST` cannot be used in `HAVING` clause.
`LAST` cannot be used with columns of type `text` unless
the field is also `saved as a keyword`.

#### `MAX`

**Synopsis:**
```sql
MAX(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: same type as the input

*Description*: Returns the maximum value across input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggMax]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggMaxScalars]
```

`MAX` on a field of type `text` or `keyword` is translated into
sql-functions-aggs-last and therefore, it cannot be used in `HAVING` clause.

#### `MIN`

**Synopsis:**
```sql
MIN(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: same type as the input

*Description*: Returns the minimum value across input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggMin]
```

`MIN` on a field of type `text` or `keyword` is translated into
sql-functions-aggs-first and therefore, it cannot be used in `HAVING` clause.

#### `SUM`

**Synopsis:**
```sql
SUM(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `bigint` for integer input, `double` for floating points

*Description*: Returns the sum of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggSum]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggSumScalars]
```

### Statistics

#### `KURTOSIS`

**Synopsis:**
```sql
KURTOSIS(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

[Quantify](https://en.wikipedia.org/wiki/Kurtosis) the shape of the distribution of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggKurtosis]
```

**Note:**
`KURTOSIS` cannot be used on top of scalar functions or operators but only directly on a field. So, for example,
the following is not allowed and an error is returned:
```sql
 SELECT KURTOSIS(salary / 12.0), gender FROM emp GROUP BY gender
```

#### `MAD`

**Synopsis:**
```sql
MAD(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

[Measure](https://en.wikipedia.org/wiki/Median_absolute_deviation) the variability of the input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggMad]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggMadScalars]
```

#### `PERCENTILE`

**Synopsis:**
```sql
PERCENTILE(
    field_name,         <1>
    percentile[,        <2>
    method[,            <3>
    method_parameter]]) <4>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.
<2> a numeric expression (must be a constant and not based on a field). If
`null`, the function returns `null`.
<3> optional string literal for the percentile algorithm. Possible values: `tdigest` or `hdr`. Defaults to `tdigest`.
<4> optional numeric literal that configures the percentile algorithm. Configures `compression` for `tdigest` or `number_of_significant_value_digits` for `hdr`. The default is the same as that of the backing algorithm.

*Output*: `double` numeric value

*Description*:

Returns the nth [percentile](https://en.wikipedia.org/wiki/Percentile) (represented by `numeric_exp` parameter)
of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggPercentile]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggPercentileScalars]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggPercentileWithPercentileConfig]
```

#### `PERCENTILE_RANK`

**Synopsis:**
```sql
PERCENTILE_RANK(
    field_name,         <1>
    value[,             <2>
    method[,            <3>
    method_parameter]]) <4>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.
<2> a numeric expression (must be a constant and not based on a field). If
`null`, the function returns `null`.
<3> optional string literal for the percentile algorithm. Possible values: `tdigest` or `hdr`. Defaults to `tdigest`.
<4> optional numeric literal that configures the percentile algorithm. Configures `compression` for `tdigest` or `number_of_significant_value_digits` for `hdr`. The default is the same as that of the backing algorithm.

*Output*: `double` numeric value

*Description*:

Returns the nth [percentile rank](https://en.wikipedia.org/wiki/Percentile_rank) (represented by `numeric_exp` parameter)
of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggPercentileRank]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggPercentileRankScalars]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggPercentileRankWithPercentileConfig]
```

#### `SKEWNESS`

**Synopsis:**
```sql
SKEWNESS(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

[Quantify](https://en.wikipedia.org/wiki/Skewness) the asymmetric distribution of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggSkewness]
```

**Note:**
`SKEWNESS` cannot be used on top of scalar functions but only directly on a field. So, for example, the following is
not allowed and an error is returned:
```sql
 SELECT SKEWNESS(ROUND(salary / 12.0, 2), gender FROM emp GROUP BY gender
```

#### `STDDEV_POP`

**Synopsis:**
```sql
STDDEV_POP(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

Returns the [population standard deviation](https://en.wikipedia.org/wiki/Standard_deviations) of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggStddevPop]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggStddevPopScalars]
```

#### `STDDEV_SAMP`

**Synopsis:**
```sql
STDDEV_SAMP(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

Returns the [sample standard deviation](https://en.wikipedia.org/wiki/Standard_deviations) of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggStddevSamp]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggStddevSampScalars]
```

#### `SUM_OF_SQUARES`

**Synopsis:**
```sql
SUM_OF_SQUARES(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

Returns the sum of squares of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggSumOfSquares]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggSumOfSquaresScalars]
```

#### `VAR_POP`

**Synopsis:**
```sql
VAR_POP(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

Returns the [population variance](https://en.wikipedia.org/wiki/Variance) of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggVarPop]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggVarPopScalars]
```

#### `VAR_SAMP`

**Synopsis:**
```sql
VAR_SAMP(field_name) <1>
```

*Input*:

<1> a numeric field. If this field contains only `null` values, the function
returns `null`. Otherwise, the function ignores `null` values in this field.

*Output*: `double` numeric value

*Description*:

Returns the [sample variance](https://en.wikipedia.org/wiki/Variance) of input values in the field `field_name`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggVarSamp]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[aggVarSampScalars]
```
