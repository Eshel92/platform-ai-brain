<!-- Converted from reference/mql/window-functions/lastN.txt (reStructuredText). Includes are inlined. -->

# $lastN (window function)

## Definition

**`$lastN`**

Returns an array containing the last `n` elements within a window.

**Note:** Disambiguation

This page describes `$lastN` when used as a **window function**.

You can also use `$lastN` in these other contexts:

- `$lastN (accumulator)`, used in grouping to
  return the last `n` elements from each group.

- `$lastN (expression)`, which returns the
  specified number of elements from the end of an array.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $lastN: {
               input: <expression>,
               n: <expression>
            }
         }
      }
   }
}
```

### Options

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The `input` expression is evaluated over each document in the window, and the last `n` results are preserved. |
| `n` | Expression | The number of elements that `$lastN` returns from the window. Must evaluate to a positive integer. If the window contains fewer than `n` elements, `$lastN` returns all elements in the window. |

## Behavior

`$lastN` has the following behaviors for null and missing values:

- `$lastN` does not filter out null values.
- `$lastN` converts missing values to null.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to partition movies by
`year`, sort them by `imdb.rating` in descending order, and return
the three lowest-rated movies from each year.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses the `$match` stage to filter the results to movies
  released in 1979, 1985, and 1992 with an IMDb rating of 4.5 or
  lower.
- Uses `$setWindowFields` to partition movies by `year` and
  sort them by `imdb.rating` in descending order with `title` as a
  tiebreaker. The stage uses `$lastN` with `n: 3` to create
  `lowestRatedThreeMoviesInYear` from a
  window defined as ``documents: [
  "unbounded", "unbounded" ]``.
- Uses `$project` to include only the `title`, `year`,
  `imdb.rating`, and `lowestRatedThreeMoviesInYear` fields in the output.
- Uses `$sort` to sort the results by year, rating, and title.
