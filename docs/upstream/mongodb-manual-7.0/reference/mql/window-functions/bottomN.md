<!-- Converted from reference/mql/window-functions/bottomN.txt (reStructuredText). Includes are inlined. -->

# $bottomN (window function)

## Definition

**`$bottomN`**

Returns the bottom `n` elements within a particular window, according
to the specified sort order.

**Note:** Disambiguation

This page describes `$bottomN` when used as a **window function**.

You can also use `$bottomN (accumulator)`, which
returns the bottom `n` elements within a group according to the
specified sort order.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $bottomN: {
               n: <expression>,
               output: <expression>,
               sortBy: { <field1>: <sort order>, <field2>: <sort order> ... }
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

| Field | Necessity | Description |
|---|---|---|
| `n` | Required | Number of results to return. Must evaluate to a positive integral value. If the window contains fewer than `n` elements, `$bottomN` returns all elements in the window. |
| `output` | Required | Determines the output for each document in the window. Can be any expression. |
| `sortBy` | Required | Defines the ranking order of elements within the window, with syntax similar to `$sort`. Does not affect the order of documents in pipeline output. |

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Three Lowest Rated Movies in a Window

This example uses the `$bottomN` window function to return each movie
along with the three lowest-rated movies released in the same year.

```shell
```

Output:

```shell
```

In the preceding example:

- `$unwind` deconstructs the `genres` array so each movie
  document only contains a single genre.
- `$match` restricts the input to `Action` movies that are
  rated `PG-13`, have an `imdb.rating` value of 5 or less, and were
  released in 2000, 2001, or 2002.
- `$setWindowFields` partitions the documents by `year`.
- `window: { documents: [ "unbounded", "unbounded" ] }` spans the
  entire year partition, so `$bottomN` considers all documents in the
  year when determining the three lowest-rated movies.
- `$bottomN` uses `sortBy: { "imdb.rating": -1, title: 1 }` to rank
  movies by IMDb score and uses `title` as a tie-breaker. Every
  document in the same year receives the same `lowestThreeMovies`
  value.
- `$project` removes unneeded fields to highlight the window
  function result.
