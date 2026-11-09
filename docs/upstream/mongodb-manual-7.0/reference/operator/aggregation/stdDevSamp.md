<!-- Converted from reference/operator/aggregation/stdDevSamp.txt (reStructuredText). Includes are inlined. -->

# $stdDevSamp (accumulator operator)

## Definition

**`$stdDevSamp`**

Calculates the sample standard deviation of values across a group of
documents.

Use `$stdDevSamp` if the input values represent a sample of a
population of data from which you want to generalize about the
population. If the values represent the entire population of data, use
`$stdDevPop` instead.

The `$stdDevSamp` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$stdDevSamp` when used as an **accumulator**.
Accumulators return an aggregated value across a group of input
documents.

You can also use `$stdDevSamp` in these other contexts:

- `$stdDevSamp (expression)`, which
  returns the sample standard deviation of numeric values in an
  array.

- `$stdDevSamp (window function)`, which
  is used in the `$setWindowFields` stage to calculate
  the sample standard deviation of values in a window.

## Syntax

```javascript
{ $stdDevSamp: <expression> }
```

## Behavior

### Result Type

`$stdDevSamp` returns the sample standard deviation of the input
values as a `double`.

### Non-Numeric Values

`$stdDevSamp` ignores non-numeric values, null values, and missing
fields. If all input values are non-numeric or missing, `$stdDevSamp`
returns `null`.

### Single Value

If the input consists of a single numeric value, `$stdDevSamp` returns
`null`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example returns the five directors with the most varied IMDb
ratings among directors with at least 10 movies.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies that have a
  `directors` field and a numeric `imdb.rating`.
- Uses `$unwind` to create a separate document for each
  director credit.
- Uses `$group` to group by director, counts the movies
  with `$sum`, and computes `stdDevSampRating` using
  `$stdDevSamp` on `imdb.rating`.
- Uses a second `$match` to keep only directors with at
  least 10 movies.
- Uses `$sort` to sort by `stdDevSampRating` descending.
- Uses `$limit` to return the top 5 results.

## Learn More

- accumulators-ref
- `$stdDevPop`
- aggregation-expressions
