<!-- Converted from reference/mql/window-functions/minN.txt (reStructuredText). Includes are inlined. -->

# $minN (window function)

## Definition

**`$minN`**

Returns the `n` minimum values from documents in a specified window.

**Note:** Disambiguation

This page describes `$minN` when used as a **window function**.

You can also use `$minN` in these other contexts:

- `$minN (accumulator)`, which returns
  the minimum `n` values for each group.
- `$minN (expression)`, which returns the `n`
  minimum values in an array.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $minN: { input: <expression>, n: <expression> }
         }
      }
   }
}
```

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The `input` expression is evaluated over each document in the window, and the minimum `n` results are preserved. |
| `n` | Expression | The number of elements that `$minN` returns from the window. Must evaluate to a positive integer. If the window contains fewer than `n` elements, `$minN` returns all elements in the window. |

## Behavior

### Type Comparison Order

When `$minN` compares values of different types, the ordering
of types follows the
BSON comparison order.

### Null and Missing Values

`$minN` filters out null and missing values.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses the `$minN` window function to return the two
lowest IMDb ratings for each year.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter to movies from 1999 or 2001
  with an IMDb rating of 3.8 or lower and greater than 0.

- Uses `$setWindowFields` to partition movies by
  `year`. The stage uses `$minN` with `n: 2` to create
  `lowestTwoRatingsInYear` from a
  window defined as
  `documents: [ "unbounded", "unbounded" ]`. The window covers
  all documents in the partition, so `lowestTwoRatingsInYear`
  shows the two lowest ratings for the entire year.

- Uses `$project` to include only the `title`,
  `year`, `imdb.rating`, and `lowestTwoRatingsInYear`
  fields in the output.

- Uses `$sort` to order results by year and
  `imdb.rating` in ascending order.
