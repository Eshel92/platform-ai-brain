<!-- Converted from reference/mql/window-functions/median.txt (reStructuredText). Includes are inlined. -->

# $median (window function)

## Definition

**`$median`**

**New in version:** 7.0

Returns the median (50th percentile) value from documents in a
specified window. You can use `$median` in both document-based
and range-based windows.

**Note:** Disambiguation

This page describes `$median` when used as a **window function**.

You can also use `$median` in these other contexts:

- `$median (accumulator)`, used in grouping to
  return the median value across a group of input documents.
- `$median (expression)`, which returns the
  median of an array of values.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $median: {
               input: <expression>,
               method: <string>
            }
         }
      }
   }
}
```

### Command Fields

| Field | Type | Necessity | Description |
|---|---|---|---|
| `input` | Expression | Required | Returns the values over which the median is calculated. `input` must be an expression that evaluates to a number. If the expression does not evaluate to a number, the `$median` calculation ignores that value. |
| `method` | String | Required | The method that `mongod` uses to calculate the median value. The method must be `'approximate'`. |

## Behavior

### Calculation Considerations

When `$median` is used as a window function, it always uses an accurate
percentile calculation algorithm rather than an approximate one, even
when `method: "approximate"` is specified.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to compute the median
IMDb rating for each movie that belongs to all three of the Adventure,
Comedy, and Drama genres. The window spans the previous year, the same
year, and the following year (range `[ -1, 1 ]`):

```shell
```

Output:

```shell
```

In the preceding pipeline:

- `$match` filters for movies that belong to all three of
  the Adventure, Comedy, and Drama genres, released between 2000 and
  2005.
- `$setWindowFields` sorts by `year` in ascending order
  and applies `$median` with a range-based window of `[ -1, 1 ]`.
  Each movie's `medianRatingByYear` is the median `imdb.rating`
  of movies in all three genres released within one year of it.
- `$project` includes only the `title`, `year`,
  `genres`, `imdb.rating`, and `medianRatingByYear` fields.
- `$sort` sorts the results by `year` in ascending order,
  then by `imdb.rating` in descending order.
- `$limit` restricts the output to 10 results to improve
  readability.

## Learn More

- `$percentile`
- projection-operators-ref
- agg-pipeline-limits
