<!-- Converted from reference/mql/window-functions/maxN.txt (reStructuredText). Includes are inlined. -->

# $maxN (window function)

## Definition

**`$maxN`**

Returns an array containing the maximum `n` elements within a window.

**Note:** Other Uses of `$maxN`

This page describes `$maxN` when used as a **window function**.

You can also use `$maxN` in these other contexts:

- `$maxN (accumulator)`, which returns the maximum
  `n` values within a group.

- `$maxN (expression)`, which returns the
  largest `n` values from an array.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $maxN: {
               input: <expression>,
               n: <expression>
            },
            window: {
               documents: [ <lower boundary>, <upper boundary> ]
            }
         }
      }
   }
}
```

### Options

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The expression evaluated over each document in the window. `$maxN` returns the maximum `n` values. |
| `n` | Expression | The number of elements that `$maxN` returns from the window. Must evaluate to a positive integer. If the window contains fewer than `n` elements, `$maxN` returns all elements in the window. |

## Behavior

### Null and Missing Values

`$maxN` filters out null and missing values.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$maxN` in `$setWindowFields` to return
the three highest-rated movies for each year. The window spans the
entire partition, so every document in the same year receives the same
`topThreeRatedInYear` value.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies released in `1999`
  or `2001` with an IMDb rating of `8.5` or higher.
- Uses `$setWindowFields` to partition movies by `year`
  and sort them by `imdb.rating` in descending order. The stage
  uses `$maxN` with `n: 3` to create `topThreeRatedInYear`
  from a window spanning the entire partition
  (`documents: ["unbounded", "unbounded"]`).
- Uses `$project` to include only the `title`, `year`,
  `imdb.rating`, and `topThreeRatedInYear` fields in the output.
- Uses `$sort` to sort the results by year ascending and rating descending.

## Learn More

- agg-pipeline-limits
