<!-- Converted from reference/operator/aggregation/percentile.txt (reStructuredText). Includes are inlined. -->

# $percentile (accumulator operator)

## Definition

**`$percentile`**

**New in version:** 7.0

Returns an array of scalar values that correspond to specified
percentile values.

Available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$percentile` when used as an
**accumulator**. Accumulators return an aggregated value across a
group of input documents.

You can also use `$percentile` in these other contexts:

- `$percentile (expression)`, which
  calculates percentile values over an array of input values.

- `$percentile (window function)`, which
  is used in the `$setWindowFields` stage to return
  an array of percentile values for documents in a particular
  window.

## Syntax

```javascript
{
   $percentile: {
      input: <expression>,
      p: [ <expression1>, <expression2>, ... ],
      method: <string>
   }
}
```

### Options

`$percentile` takes the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `input` | Expression | Required | `$percentile` calculates the percentile values of this data. `input` must be an expression that evaluates to a numeric type. If the expression does not evaluate to a numeric type, the `$percentile` calculation ignores that value. |
| `p` | Expression | Required | .. include:: /includes/aggregation/percentile/opt-p.rst |
| `method` | String | Required | .. include:: /includes/aggregation/percentile/opt-method.rst |

## Behavior

When used as an accumulator, `$percentile`:

- Calculates one set of percentiles per group, aggregated across all
  documents in the group.
- Uses the [t-digest](https://arxiv.org/abs/1902.04023) algorithm
  for calculation of approximate percentiles. Approximation is
  necessary to calculate percentiles using a data structure of
  bounded size.

### Calculation Considerations

When used as an accumulator, `$percentile` always uses an approximation
algorithm. Due to pseudorandomness in the t-digest approximation
algorithm, the computed percentile values on the same data set might
differ on each run. Additionally, `$percentile` may return values that
differ slightly from the true statistical percentiles.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Calculate Rating Percentiles by Genre

The following example uses the `$percentile` accumulator to
calculate the 50th and 90th percentile IMDB ratings for movies in
the `Action` and `Drama` genres:

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$unwind` to create a separate document for each
  genre in the `genres` array.
- Uses `$match` to filter for movies that are classified
  as `Action` or `Drama` and have an IMDB rating field.
- Groups movies by genre.
- Uses `$percentile` to calculate the 50th and 90th percentile
  IMDB ratings for each genre with `p: [0.5, 0.9]`.
- Uses `$sort` to order the output by genre name.

The output `ratingPercentiles` array contains two values: the
50th percentile and the 90th percentile IMDB rating for each genre.
