<!-- Converted from reference/operator/aggregation/top.txt (reStructuredText). Includes are inlined. -->

# $top (accumulator operator)

## Definition

**`$top`**

Returns the top element within a group according to the specified 
sort order. 

**Note:** Disambiguation

This page describes `$top` when used as an **accumulator**.
Accumulators return a single aggregated value across a group of
input documents.

You can also use the `$top (window function)` in the
`$setWindowFields` stage to return the top element from
documents in a particular window.

## Syntax

```none
{
   $top:
      {
         sortBy: { <field1>: <sort order>, <field2>: <sort order> ... },
         output: <expression>
      }
}
```

| Field | Necessity | Description |
|---|---|---|
| sortBy | Required | Specifies the order of results, with syntax similar to `$sort`. |
| output | Required | Represents the output for each element in the group and can be any expression. |

## Behavior

### Null and Missing Values

Consider the following aggregation that returns the top document 
from a group of scores:

- `$top` does not filter out null values.
- `$top` converts missing values to null.

```javascript
```

Output:

```javascript
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
- Specify the sort order with `sortBy: { "score": 1 }`.
- `PlayerD` and `PlayerE` tied for the top element. `PlayerD`
  is returned as the top `score`.
- To have more deterministic tie breaking behavior for multiple null
  values, add more fields to `sortBy`.

### BSON Data Type Sort Ordering

When sorting different types, the order of BSON data types is used to determine ordering. As an example,
consider a collection whose values consist of strings and numbers.

- In an ascending sort, string values are sorted after numeric values.
- In a descending sort, string values are sorted before numeric
  values.

In this example:

- `PlayerA` has an integer score.
- `PlayerB` has a string `"2"` score.
- `PlayerC` has an empty string score.

Because the sort is in descending `{ "score": -1 }`, string values
are sorted before `PlayerA`'s numeric score. `$top` returns
the first element after sorting, which is `PlayerB`:

```javascript
```

Output:

```javascript
```

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Top Rating in a Genre

You can use the `$top` accumulator to find the highest-rated
movie in a genre.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Uses `$match` to filter for Comedy movies with a
  positive IMDb rating.
- Uses `$group` to group all Comedy movies under a
  single `"Comedy"` group key.
- Specifies the fields that are output for `$top` with
  `output : ["$title", "$imdb.rating"]`.
- Uses `sortBy: { "imdb.rating": -1 }` to rank movies within
  the group by IMDb rating in descending order, which determines
  the movie that `$top` returns.

### Find the Top Rating Across Multiple Ratings

You can use the `$top` accumulator to find the highest-rated
movie for each movie rating category.

```javascript
```

Output:

```javascript
```

The example pipeline:

- Uses `$match` to filter for movies in the `G`,
  `PG`, `PG-13`, and `R` categories with a positive
  IMDb rating.
- Uses `$group` to group the results by `rated`.
- Uses `$top` to return the highest-rated movie for each
  category.
- Specifies the fields that are output for `$top` with
  `output : ["$title", "$imdb.rating"]`.
- Uses `sortBy: { "imdb.rating": -1 }` to rank movies within
  each group by IMDb rating in descending order, which determines
  the movie that `$top` returns.
- Uses `$sort` to sort the results alphabetically by
  rating category.

## Learn More

- agg-pipeline-limits
- bson-types-comparison-order
