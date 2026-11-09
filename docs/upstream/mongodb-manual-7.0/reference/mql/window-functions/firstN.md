<!-- Converted from reference/mql/window-functions/firstN.txt (reStructuredText). Includes are inlined. -->

# $firstN (window function)

## Definition

**`$firstN`**

Returns an array containing the first `n` elements within a window.

**Note:** Disambiguation

This page describes `$firstN` when used as a **window function**.

You can also use `$firstN` in these other contexts:

- `$firstN (accumulator)`, used in grouping to
  return the first `n` elements from each group.

- `$firstN (expression)`, which returns the 
  specified number of elements from the beginning of an array.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $firstN: {
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
| `input` | Expression | The `input` expression is evaluated over each document in the window, and the first `n` results are preserved. |
| `n` | Expression | The number of elements that `$firstN` returns from the window. Must evaluate to a positive integer. If the window contains fewer than `n` elements, `$firstN` returns all elements in the window. |

## Behavior

### Null and Missing Values

- `$firstN` does not filter out null values.
- `$firstN` converts missing values to null.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to partition movies by
`year`, sort them by `imdb.rating` in descending order, and return
the first three movies from each year. Each movie also includes a field
that shows the three highest-rated movie titles released in that year:

```shell
```

Output:

```shell
```

The preceding pipeline:

- Uses the `$match` stage to filter the results to movies
  released between the years 
  1999 and 2001 with an IMDb rating of 8.5 or higher.
- Uses `$setWindowFields` to partition movies by `year` and
  sort them by `imdb.rating` in descending order. The stage uses
  `$firstN` with `n: 3` to create `topThreeMoviesInYear` from a
  window defined as ``documents: [
  "unbounded", "unbounded" ]``.
- Uses `$project` to include only the `title`, `year`, 
  `imdb.rating`, and `topThreeMoviesInYear` fields in the output.
- Uses `$sort` to sort the results by year and rating.
