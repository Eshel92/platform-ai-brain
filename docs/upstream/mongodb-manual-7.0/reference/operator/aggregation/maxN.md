<!-- Converted from reference/operator/aggregation/maxN.txt (reStructuredText). Includes are inlined. -->

# $maxN (accumulator operator)

## Definition

**`$maxN`**

Returns an aggregation of the maximum value `n` elements within a
group. If the group contains fewer than `n` elements, `$maxN`
returns all elements in the group.

The `$maxN` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Other Uses of `$maxN`

This page describes `$maxN` when used as an **accumulator**.
Accumulators return an aggregated value like sum, maximum,
or minimum across a group of input documents.

You can also use `$maxN` in these other contexts:

- `$maxN (expression)`, which returns the
  largest `n` values from an array.

- `$maxN (window function)`, which is used in the
  `$setWindowFields` stage to return the largest `n`
  values from documents in a particular window.

## Syntax

```javascript
{
   $maxN:
      {
         input: <expression>,
         n: <expression>
      }
}
```

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The expression evaluated for each element in the group. `$maxN` preserves the maximum `n` values. |
| `n` | Expression | The number of elements that `$maxN` returns from the group. For an example of setting `n` dynamically, see max-n-with-group-key. |

## Behavior

### Result Type

When `$maxN` compares values of different types, the ordering
of types follows the
BSON comparison order.

### Null and Missing Values

`$maxN` filters out null and missing values.

The following aggregation demonstrates how `$maxN` handles null and
missing values:

```javascript
db.aggregate( [
   {
      $documents: [
         { title: "Fight Club", genre: "Drama", rating: 8.9 },
         { title: "The Matrix", genre: "Drama", rating: 8.7 },
         { title: "The Green Mile", genre: "Drama", rating: 8.5 },
         { title: "Magnolia", genre: "Drama" },
         { title: "Dogma", genre: "Drama", rating: null }
      ]
   },
   {
      $group: {
         _id: "$genre",
         topFourRatings: {
            $maxN: {
               input: "$rating",
               n: 4
            }
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: 'Drama',
      topFourRatings: [ 8.9, 8.7, 8.5 ]
   }
]
```

In this example:

- `$documents` creates the literal documents that contain
  movie ratings.
- `$group` groups the documents by `genre`. This example
  has only one `genre`, `Drama`.
- `Magnolia` has a missing `rating` and `Dogma` has a null
  `rating`. Both values are filtered out.
- Since only 3 documents have valid ratings, `$maxN` returns 3
  values even though `n = 4`.

### Comparison of $maxN and $topN Accumulators

You can use `$maxN` or `$topN` to return the highest-ranked
`n` elements from a group. The choice between them depends on
whether your input documents are already sorted.

- If the input documents are already sorted, use `$maxN` to return the
  maximum `n` values.

- If you need to sort and select the top `n` elements at the same time,
  use `$topN` to accomplish both with a single accumulator.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Three Highest Rated Movies for a Single Year

You can use the `$maxN` accumulator to find the three highest IMDb
ratings for movies released in a single year.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies released in `1999`
  that have an `imdb.rating` field.
- Groups all matching documents into a single group with
  `_id: 1999`.
- Specifies `"$imdb.rating"` as the `input` for `$maxN`.
- Uses `$maxN` to return the three highest ratings with
  `n: 3`.

### Find the Three Highest Rated Movies Across Multiple Years

You can use the `$maxN` accumulator to find the three highest rated
movies for each year in a set of years.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies released in `1999`,
  `2000`, or `2001` that have an `imdb.rating` field.
- Uses `$group` to group movies by `year`.
- Specifies `"$imdb.rating"` as the `input` for `$maxN`.
- Uses `$maxN` to return the three highest ratings per year
  with `n: 3`.
- Sorts the results by year in ascending order.

### Set n Based on the Group Key

You can assign the value of `n` dynamically based on the group key.
In this example, the `$cond` expression uses the `year`
field to change the value of `n`:

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Filters for movies released in `1999`, `2000`, or `2001`
  that have an `imdb.rating` field.
- Groups movies by `year`.
- Uses the `$cond` expression to return `3` ratings for
  the year `2001` and `1` rating for all other years.

In the output, `2001` returns three ratings while `1999` and
`2000` each return one rating.

## Learn More

- agg-pipeline-limits
