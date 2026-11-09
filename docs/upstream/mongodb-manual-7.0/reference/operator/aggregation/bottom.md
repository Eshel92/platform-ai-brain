<!-- Converted from reference/operator/aggregation/bottom.txt (reStructuredText). Includes are inlined. -->

# $bottom (accumulator operator)

## Definition

**`$bottom`**

Returns the bottom element within a group according to the specified
sort order.

Available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$bottom` when used as an **accumulator**.
Accumulators return a single aggregated value across a group of input
documents.

You can also use the `$bottom (window function)`
in the `$setWindowFields` stage to return the bottom
element from documents in a particular window.

## Syntax

```none
{
   $bottom:
      {
         sortBy: { <field1>: <sort order>, <field2>: <sort order> ... },
         output: <expression>
      }
}
```

| Field | Necessity | Description |
|---|---|---|
| sortBy | Required | Defines the ranking order of elements within each group, with syntax similar to `$sort`. Does not affect the order of documents in pipeline output. |
| output | Required | Represents the output for each element in the group and can be any expression. |

## Behavior

### Null and Missing Values

`$bottom` does not filter out null values, and `$bottom` converts
missing values to null.

Consider the following aggregation that returns the bottom 
document from a group of scores:

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
               $bottom:
                  {
                     output: [ "$playerId", "$score" ],
                     sortBy: { "score": -1 }
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
      _id: 'G1',
      playerId: [ 'PlayerD', null ]
   }
]
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
- Specify the ranking order with `sortBy: { "score": -1 }`.
- `PlayerD` and `PlayerE` tied for the bottom element. `PlayerD`
  is returned as the bottom `score`.

## Restrictions

### Memory Limit Considerations

Aggregation pipelines which call `$bottom` are subject to the
100 MB limit. If this
limit is exceeded for an individual group, the aggregation fails
with an error.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Bottom Rating in a Genre

You can use the `$bottom` accumulator to find the lowest-rated movie
in a single genre.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Uses `$match` to filter the results on a single genre. 
  In this case, `Comedy`.
- Uses `$group` to group all Comedy movies under a
  single `"Comedy"` group key.
- Specifies the fields that are output for `$bottom` with
  `output : ["$title", "$imdb.rating"]`.
- Uses `sortBy: { "imdb.rating": -1 }` to define the bottom element in
  each group as the one with the lowest rating.
- Uses `$bottom` to return the lowest-rated movie for the genre.

### Find the Bottom Rating Across Multiple Years

You can use the `$bottom` accumulator to find the lowest-rated movie
for each year.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Uses `$match` to filter for movies from 2010-2012 that have an IMDb rating.
- Uses `$group` to group the results by `year`.
- Uses `$bottom` to return the lowest-rated movie for each year.
- Specifies the fields that are output for `$bottom` with
  `output : ["$title", "$imdb.rating"]`.
- Uses `sortBy: { "imdb.rating": -1 }` to define the bottom element in
  each group as the one with the lowest rating.
- Uses `$sort` to sort the results by year in ascending order.
