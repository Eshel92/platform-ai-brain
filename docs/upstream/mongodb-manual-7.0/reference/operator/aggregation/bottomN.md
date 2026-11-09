<!-- Converted from reference/operator/aggregation/bottomN.txt (reStructuredText). Includes are inlined. -->

# $bottomN (accumulator operator)

## Definition

**`$bottomN`**

**New in version:** 5.2

Returns an aggregation of the bottom `n` elements within a group,
according to the specified sort order. If the group contains fewer 
than `n` elements, `$bottomN` returns all elements in the group.

**Note:** Disambiguation

This page describes `$bottomN` when used as an **accumulator**.
Accumulators return an aggregated value across a group of input
documents.

You can also use the `$bottomN (window function)`,
which returns the bottom `n` elements from documents in a particular
window according to the specified sort order.

## Syntax

```none
{
   $bottomN:
      {
         n: <expression>,
         output: <expression>,
         sortBy: { <field1>: <sort order>, <field2>: <sort order> ... }
      }
}
```

### Options

| Field | Necessity | Description |
|---|---|---|
| `n` | Required | The number of elements that `$bottomN` returns from the group. For an example of setting n dynamically, see bottomN-dynamic-n. |
| `output` | Required | Determines the output for each element in the group. Can be any expression. |
| `sortBy` | Required | Defines the ranking order of elements within each group, with syntax similar to `$sort`. Does not affect the order of documents in pipeline output. |

## Behavior

### Null and Missing Values

- `$bottomN` does not filter out null values.
- `$bottomN` converts missing values to null which are preserved in
  the output.

```javascript
db.aggregate( [
   {
      $documents: [
         { playerId: "PlayerA", gameId: "G1", score: 1 },
         { playerId: "PlayerB", gameId: "G1", score: 2 },
         { playerId: "PlayerC", gameId: "G1", score: 3 },
         { playerId: "PlayerD", gameId: "G1"},
         { playerId: "PlayerE", gameId: "G1", score: null }
      ]
   },
   {
      $group:
      {  
            _id: "$gameId",
            playerId:
               { 
                  $bottomN:
                     {    
                        output: [ "$playerId", "$score" ],
                        sortBy: { "score": -1 },
                        n: 3
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
  null `score`. These values are both considered as null.
- The `playerId` and `score` fields are specified as 
  `output : ["$playerId"," $score"]` and returned as array values. 
- Because of the `sortBy: { "score" : -1 }`, the null values are sorted
  to the end of the returned `playerId` array.

```javascript
[
   {
      _id: "G1",
      playerId: [ [ "PlayerA", 1 ], [ "PlayerD", null ], [ "PlayerE", null ] ]
   }
]
```

### BSON Data Type Sort Ordering

When sorting different types, the order of BSON data types is used to determine ordering. As an example, 
consider a collection whose values consist of strings and numbers.

- In an ascending sort, string values are sorted after numeric values.
- In a descending sort, string values are sorted before numeric values.

```javascript
db.aggregate( [
   {
      $documents: [
         { playerId: "PlayerA", gameId: "G1", score: 1 },
         { playerId: "PlayerB", gameId: "G1", score: "2" },
         { playerId: "PlayerC", gameId: "G1", score: "" }
      ]
   },
   {
      $group:
         {
            _id: "$gameId",
            playerId: {
               $bottomN:
               {
                  output: ["$playerId","$score"],
                  sortBy: {"score": -1},
                  n: 3
               }
            }
         }
   }
] )
```

In this example:

- `PlayerA` has an integer score.
- `PlayerB` has a string `"2"` score. 
- `PlayerC` has an empty string score.

Because the sort is in descending `{ "score" : -1 }`, the string
literal values are sorted before `PlayerA`'s numeric score:

```javascript
[
   {
      _id: "G1",
      playerId: [ [ "PlayerB", "2" ], [ "PlayerC", "" ], [ "PlayerA", 1 ] ]
   }
]
```

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Three Lowest Rated Movies in a Single Genre

You can use the `$bottomN` accumulator to find the three lowest-rated
movies in the `Short` genre.

```shell
```

Output:

```shell
```

The example pipeline:

- Uses `$match` to restrict the input to `Short` movies that
  include an `imdb.rating` value.
- Uses `$group` to place the matched movies into a single
  `Short` group.
- Uses `sortBy: { "imdb.rating": -1, title: 1 }` to rank movies by
  rating and use `title` as a tie-breaker.
- Specifies the fields returned by `$bottomN` with
  `output: [ "$title", "$imdb.rating" ]`.
- Uses `$bottomN` to return the bottom three matching movies with
  `n: 3`.

### Find the Lowest Rated Movies for Each Genre

You can use the `$bottomN` accumulator to find the lowest-rated movies
for each genre.

```shell
```

Output:

```shell
```

The example pipeline:

- Uses `$unwind` to expand each movie's `genres` array.
- Uses `$match` to keep only documents that include an
  `imdb.rating` value.
- Uses `$group` to group the results by genre.
- Specifies the fields returned by `$bottomN` with
  `output: [ "$title", "$imdb.rating" ]`.
- Uses `sortBy: { "imdb.rating": -1, title: 1 }` to rank movies by
  rating and use `title` as a deterministic tie-breaker.
- Uses `$bottomN` to return the bottom three movies for each genre with
  `n: 3`.
- Uses `$sort` and `$limit` to show the first five
  genres alphabetically.

### Set n Dynamically Based on the Group Key

You can assign the value of `n` dynamically. The following example
uses the `$cond` expression to return different numbers of
movies based on content rating.

```shell
```

Output:

```shell
```

The example pipeline:

- Uses `$match` to keep only movies with `G`, `PG`,
  `PG-13`, or `R` content ratings that include an `imdb.rating`
  value.
- Uses `$group` to group the results by content rating with
  `_id: { rated: "$rated" }`.
- Specifies the fields returned by `$bottomN` with
  `output: { title: "$title", rating: "$imdb.rating" }`.
- If the content rating is `PG` then `n` is 3. Otherwise, `n`
  is 1.
- Uses `sortBy: { "imdb.rating": -1 }` to find the bottom `n` movies
  based on IMDb score.
- Sorts the results alphabetically by content rating.

## Learn More

- agg-pipeline-limits
- bson-types-comparison-order
