<!-- Converted from reference/operator/aggregation/sum.txt (reStructuredText). Includes are inlined. -->

# $sum (Accumulator Operator)

## Definition

**`$sum`**

Returns the collective sum of numeric values across a group of
documents.

The `$sum` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Other Uses of `$sum`

This page describes `$sum` when used as an **accumulator**.
Accumulators return an aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$sum` in these other contexts:

- `$sum (expression)`, which returns the sum
  of numeric values in an array.

- `$sum (window function)`, which is used in the
  `$setWindowFields` stage to calculate the cumulative
  sum of values in a window.

## Syntax

```javascript
{ $sum: <expression> }
```

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

When you use `$sum` on a field that contains both numeric and
non-numeric values, `$sum` ignores the non-numeric values and returns
the sum of the numeric values.

When you use `$sum` on a field that does not exist in any document in
the collection, `$sum` returns `0` for that field.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example groups movies by content rating and returns
the total number of IMDb votes for each group.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies with a `rated`
  value of `G`, `PG`, `PG-13`, or `R` and an integer
  IMDb vote count.
- Uses `$group` to group movies by the `rated` field
  and computes `totalVotes` using `$sum` on `imdb.votes`.
- Uses `$sort` to return results in alphabetical order
  by content rating.

## Learn More

- accumulators-ref
- `$count (aggregation accumulator)`
- agg-pipeline-limits
