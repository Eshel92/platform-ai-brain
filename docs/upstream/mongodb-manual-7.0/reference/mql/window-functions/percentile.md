<!-- Converted from reference/mql/window-functions/percentile.txt (reStructuredText). Includes are inlined. -->

# $percentile (window function)

## Definition

**`$percentile`**

Returns an array of percentile values for the specified percentiles
within a window.

**Note:** Disambiguation

This page describes `$percentile` when used as a **window
function**.

You can also use `$percentile` in these other contexts:

- `$percentile (accumulator)`, which returns
  an aggregated array of percentile values across a group of input
  documents.

- `$percentile (expression)`, which
  calculates percentile values over an array of input values.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $percentile: {
               input: <expression>,
               p: [ <expression1>, <expression2>, ... ],
               method: <string>
            },
         }
      }
   }
}
```

### Options

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The field over which `$percentile` calculates percentile values. `input` must be an expression that evaluates to a numeric type. If the expression does not evaluate to a numeric type, the `$percentile` calculation ignores that value. |
| `p` | Expression | .. include:: /includes/aggregation/percentile/opt-p.rst |
| `method` | String | .. include:: /includes/aggregation/percentile/opt-method.rst |

## Behavior

In `$setWindowFields`, `$percentile` returns a result for each
document, but the results are computed over a window of documents.

### Calculation Considerations

When used as a window function, `$percentile` always uses an
accurate percentile calculation algorithm rather than an approximate
one, even when `method: 'approximate'` is specified.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$percentile` in a
`$setWindowFields` stage to find Action movies in the top
10% of IMDB ratings for each year from 2002 to 2004.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for Action movies released in
  2002, 2003, or 2004 with at least 5,000 IMDB votes.
- Uses `$setWindowFields` to partition movies by `year`.
  Within each partition, the `$percentile` operator computes the
  90th percentile IMDB rating using `p: [0.9]` and an unbounded
  window, stored in `top10PctRatingForYear`.
- Uses `$match` with `$expr` to filter for
  movies whose IMDB rating is greater than or equal to the 90th
  percentile rating for their year.
- Uses `$project` to include the `title`, `year`,
  `imdb_rating`, and `top10PctRatingForYear` fields in the
  output.
- Uses `$sort` to order the results by year ascending, then
  by IMDB rating descending.
