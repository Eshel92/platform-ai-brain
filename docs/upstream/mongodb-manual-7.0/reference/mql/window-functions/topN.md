<!-- Converted from reference/mql/window-functions/topN.txt (reStructuredText). Includes are inlined. -->

# $topN (window function)

## Definition

**`$topN`**

Returns the top `n` elements within a particular window,
according to the specified sort order.

**Note:** Other Uses of `$topN`

This page describes `$topN` when used as a **window function**.

You can also use the `$topN (accumulator)`, which
returns the top `n` elements within a group according to the
specified sort order.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $topN: {
               n: <expression>,
               output: <expression>,
               sortBy: {
                  <field1>: <sort order>,
                  <field2>: <sort order>, ...
               }
            }
         }
      }
   }
}
```

### Options

| Field | Necessity | Description |
|---|---|---|
| `n` | Required | Number of results to return. Must evaluate to a positive integral value. If the window contains fewer than `n` elements, `$topN` returns all elements in the window. |
| `output` | Required | Determines the output for each document in the window. Can be any expression. |
| `sortBy` | Required | Defines the ranking order of elements within the window, with syntax similar to `$sort`. Does not affect the order of documents in pipeline output. |

## Behavior

### Null and Missing Values

- `$topN` does not filter out null values.
- `$topN` converts missing values to null.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Three Highest Rated Movies in a Window

This example uses `$topN` in `$setWindowFields` to
return each movie with the three highest-rated movies
released in the same year.

```javascript
```

Output:

```javascript
```

In the preceding example:

- `$match` filters for movies released in `1999` or
  `2001` with an IMDb rating of at least `8.5`.
- `$setWindowFields` partitions the documents by `year`.
- `window: { documents: [ "unbounded", "unbounded" ] }` spans the
  entire year partition, so `$topN` considers all documents in the
  year when determining the three highest-rated movies.
- `$topN` uses `sortBy: { "imdb.rating": -1, title: 1 }` to rank
  movies by IMDb score and uses `title` as a tie-breaker. Every
  document in the same year receives the same `topThreeRatedInYear`
  value.
- `$project` removes unneeded fields to highlight the
  window function result.
- `$sort` sorts the output by year ascending and rating
  descending.
