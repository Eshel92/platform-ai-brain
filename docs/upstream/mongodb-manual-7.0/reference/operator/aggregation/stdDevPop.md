<!-- Converted from reference/operator/aggregation/stdDevPop.txt (reStructuredText). Includes are inlined. -->

# $stdDevPop (accumulator operator)

## Definition

**`$stdDevPop`**

Calculates the population standard deviation of values across a group of
documents. Use `$stdDevPop` if the values encompass the entire
population of data you want to represent and you do not want to
generalize.

If the values represent only a sample from the population, use
`$stdDevSamp` instead.

The `$stdDevPop` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$stdDevPop` when used as an **accumulator**.
Accumulators return an aggregated value across a group of input
documents.

You can also use `$stdDevPop` in these other contexts:

- `$stdDevPop (expression)`, which
  returns the population standard deviation of numeric values in
  an array.

- `$stdDevPop (window function)`, which is
  used in the `$setWindowFields` stage to calculate the
  population standard deviation of values from documents in a
  particular window.

## Syntax

```javascript
{ $stdDevPop: <expression> }
```

For more information on expressions, see
aggregation-expressions.

## Behavior

### Result Type

`$stdDevPop` returns the population standard deviation of the
input values as a `double`.

### Non-numeric or Missing Values

`$stdDevPop` ignores non-numeric values, including missing values.
If all input values are non-numeric, `$stdDevPop` returns `null`.

### Single Value

If the input consists of a single numeric value, `$stdDevPop`
returns `0`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example groups movies by director and returns the five
directors with the most varied IMDb ratings, among directors with at
least 10 movies.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies that have a
  `directors` field and a numeric IMDb rating.
- Uses `$unwind` to create one document per director per
  movie, so each director-movie pair is grouped separately.
- Uses `$group` to group by director, count movies, and
  compute `stdDevRating` using `$stdDevPop` on `imdb.rating`.
- Uses `$match` to keep only directors with at least 10
  movies.
- Uses `$sort` to return results in descending order by
  `stdDevRating`.
- Uses `$limit` to return the top 5 results.

## Learn More

- accumulators-ref
- `$stdDevSamp`
- agg-pipeline-limits
