<!-- Converted from reference/expression/sum.txt (reStructuredText). Includes are inlined. -->

# $sum (Expression)

## Definition

**`$sum`**

Returns the sum of numeric values in an array.

**Note:** Other Uses of `$sum`

This page describes `$sum` when used as an **expression**,
which returns the sum of numeric values in an array.

You can also use `$sum` in these other contexts:

- `$sum (accumulator)`, which returns the
  collective sum of numeric values across a group of documents.

- `$sum (window function)`, which is used in the
  `$setWindowFields` stage to calculate the cumulative
  sum of values in a window.

## Syntax

When used as an expression, `$sum` has one of two syntaxes:

```javascript
{ $sum: <expression> }
```

In the preceding syntax, the operand is a single expression that
evaluates to an array. `$sum` traverses the array and returns
the sum of the array's numeric values.

```javascript
{ $sum: [ <expression1>, <expression2>, ... ] }
```

In the preceding syntax, each expression is a single numeric
value. `$sum` returns the sum of those values.

## Behavior

### Result Type

When input types are mixed, `$sum` promotes the smaller input type
to the larger of the two. A type is considered larger when it
represents a wider range of values. The order of numeric types from
smallest to largest is: integer → long → double → decimal.

The larger of the input types also determines the result type unless
the operation overflows and is beyond the range represented by that
larger data type. In cases of overflow, `$sum` promotes the result
according to the following order:

- If the larger input type is `integer`, the result
  type is promoted to `long`.

- If the larger input type is `long`, the result
  type is promoted to `double`.

- If the larger type is `double` or
  `decimal`, the overflow result is represented
  as positive or negative infinity. There is no type promotion of the
  result.

### Non-Numeric or Non-Existent Fields

If used on a field that contains both numeric and non-numeric
values, `$sum` ignores the non-numeric values and returns the
sum of the numeric values.

If all operands are non-numeric, `$sum` returns `0`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$sum` in the `$project` stage to
calculate the total awards won and nominated for three movies, and store
the result in a new field called `totalAwards`.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for three specific movies.
- Uses `$project` with `$sum` to create the
  `totalAwards` field, which holds the sum of `awards.wins`
  and `awards.nominations` for each movie.
- Uses `$sort` to sort results by total awards in
  descending order.
