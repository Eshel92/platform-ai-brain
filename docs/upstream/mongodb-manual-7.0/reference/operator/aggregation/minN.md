<!-- Converted from reference/operator/aggregation/minN.txt (reStructuredText). Includes are inlined. -->

# $minN (aggregation accumulator)

## Definition

**`$minN`**

Returns the minimum `n` values within a group. If the group
contains fewer than `n` elements, `$minN` returns all elements
in the group.

**Note:** Disambiguation

This page describes `$minN` when used as an **accumulator**.
Accumulators return an aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$minN` in these other contexts:

- `$minN (expression)`, which returns the `n`
  minimum values in an array.

- `$minN (window function)`, which is used in the
  `$setWindowFields` stage to return the minimum `n`
  values from documents in a particular window.

## Syntax

```javascript
{
   $minN:
      {
         input: <expression>,
         n: <expression>
      }
}
```

| Field | Type | Description |
|---|---|---|
| `input` | Expression | An expression evaluated for each input document to determine the input values. The smallest `n` such values are retained for each group. |
| `n` | Expression | Determines the maximum number of results returned per group. `n` must evaluate to a positive integer. |

## Behavior

### Result Type

When `$minN` compares values of different types, the ordering
of types follows the
BSON comparison order.

### Null and Missing Values

`$minN` filters out null and missing values.

Consider the following aggregation that returns the minimum `n` 
values from a group:

```javascript
db.aggregate( [
   {
      $documents: [
         { playerId: "PlayerA", gameId: "G1", score: 1 },
         { playerId: "PlayerB", gameId: "G1", score: 2 },
         { playerId: "PlayerC", gameId: "G1", score: 3 },
         { playerId: "PlayerD", gameId: "G1" },
         { playerId: "PlayerE", gameId: "G1", score: null }
      ]
   },
   {
      $group:
      {  
         _id: "$gameId",
         minimumThreeScores:
            { 
               $minN:
                  {    
                     input: "$score",
                     n: 4
                  }
            }
      }
   }
] )
```

In this example:

- `$documents` creates the literal documents that contain
  player scores.
- `$group` groups the documents by `gameId`. This
  example has only one `gameId`, `G1`.
- `PlayerD` has a missing score and `PlayerE` has a
  null `score`. These values are both ignored.
- The `minimumThreeScores` field is specified as `$minN`
  with `input : "$score"` and returned as an array.
- Since there are only 3 documents with `scores`, `$minN` returns
  the minimum 3 `score` fields even though `n = 4`.

```javascript
[ 
   { 
   _id: 'G1',
   minimumThreeScores: [ 1, 2, 3 ] 
   } 
]
```

### Comparison of $minN and $bottomN Accumulators

Both `$minN` and `$bottomN` accumulators return `n`
values from a group, but they differ in how they determine which
values to return.

- Use `$minN` when the values you want to compare are the
  same values you want to return. `$minN` selects the `n`
  smallest values by comparing inputs directly.

- Use `$bottomN` when you want to define the sort order
  separately from the output. `$bottomN` lets you specify a
  `sortBy` key to determine which documents are "bottom" and
  an `output` expression to control what values to return.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Minimum Three Ratings for a Single Genre

You can use the `$minN` accumulator to find the three lowest IMDb
ratings in a single genre.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Uses `$match` to filter the results to movies where
  `Horror` is included in the `genres` array.
- Uses `$group` to group all matching documents into a
  single group.
- Specifies the input for `$minN` with
  `input: "$imdb.rating"`.
- Uses `$minN` to return the three lowest IMDb rating entries
  for the `Horror` genre with `n: 3`.

### Find the Minimum Three Ratings Across Multiple Genres

You can use the `$minN` accumulator to find the minimum `n`
IMDb ratings in each genre.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Uses `$unwind` to create a separate document for each genre
  in the `genres` array.
- Uses `$group` to group the results by `genres`.
- Uses `$minN` to return the three lowest IMDb rating entries
  for each genre with `n: 3`.
- Specifies the input for `$minN` with
  `input: "$imdb.rating"`.
- Uses `$sort` to sort the results alphabetically by
  genre.
- Limits the output to five documents to improve readability.

### Set n Dynamically Based on the Group Key

You can assign the value of `n` dynamically. In this example,
the `$cond` expression is used on the `rated` field.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Filters for movies with ratings of `G`, `PG`, `PG-13`, or `R`.
- Groups movies by `rated` (the content rating).
- Specifies the input for `$minN` with
  `input: "$imdb.rating"`.
- Uses the `$cond` expression to return `3` minimum entries for
  `R`-rated movies and `1` minimum entry for all other ratings.

In the output, the `R` rating returns 3 entries, while `G`,
`PG`, and `PG-13` ratings each return 1 entry.
