<!-- Converted from reference/operator/aggregation/median.txt (reStructuredText). Includes are inlined. -->

# $median (accumulator operator)

## Definition

**`$median`**

**New in version:** 7.0

Returns an approximation of the median (50th percentile) value of documents in a group.

The `$median` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$median` when used as an **accumulator**.
Accumulators return an aggregated value across a group of input
documents.

You can also use `$median` in these other contexts:

- `$median (expression)`, which returns
  the median of an array of values within a single document.
- `$median (window function)`, which is used in
  the `$setWindowFields` stage to return the median
  value from documents in a window.

## Syntax

```javascript
{
   $median: {
      input: <number>,
      method: <string>
   }
}
```

### Command Fields

`$median` takes the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `input` | Expression | Required | `$median` calculates the 50th percentile over the values returned by this expression. `input` must be an expression that evaluates to a numeric type. If the expression does not evaluate to a numeric type, the `$median` calculation ignores that value. |
| `method` | String | Required | The method that `mongod` uses to calculate the 50th percentile value. The method must be `'approximate'`. |

## Behavior

When used as an accumulator, `$median`:

- Calculates a single result for all the documents in the group.
- Uses the [t-digest](https://arxiv.org/abs/1902.04023) algorithm for
  calculation of approximate percentiles. Approximation is necessary to
  calculate the median using a data structure of bounded size.

### Calculation Considerations

When used as an accumulator, `$median` always uses an approximation
algorithm. As a result, the computed percentiles `$median` returns on
the same data set might differ on each run, due to pseudorandomness in
the t-digest approximation algorithm. Additionally, `$median` may
return a value that differs slightly from the true statistical median.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$median` to calculate the median IMDb
rating of Action movies per year from 2000 to 2004:

```shell
```

Output:

```shell
```

In the preceding pipeline:

- `$match` filters for Action movies released between 2000
  and 2004 with a valid IMDb rating.
- `$group` groups documents by `year` and uses `$median`
  to calculate the median `imdb.rating` across all Action movies in
  each year.
- `$sort` sorts the results by year in ascending order.

## Learn More

- `$median (expression)`
- `$median (window function)`
- `$percentile`
