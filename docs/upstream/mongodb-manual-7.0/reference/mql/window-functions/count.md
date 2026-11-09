<!-- Converted from reference/mql/window-functions/count.txt (reStructuredText). Includes are inlined. -->

# $count (window function)

## Definition

**`$count`**

Returns the number of documents in a particular window.

**Note:** Disambiguation

This page describes `$count` when used as a **window function**.

You can also use `$count` in these other contexts:

- `$count (accumulator)`, which returns the number of
  documents in a group.

- `$count (aggregation stage)`, which returns the
  number of input documents.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $count: {},
            window: {
               documents: [ <lower boundary>, <upper boundary> ]
            }
         }
      }
   }
}
```

`$count` does not accept any parameters.

**Tip:**

`$count` is functionally equivalent to using `{ $sum: 1 }` in the
`$setWindowFields` stage.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Count Movies with a Similar Rating

This example uses the `$count` window function with a range-based
window to count how many Action movies from 2000 have an IMDb rating
within 0.5 points of each movie's rating.

```shell
```

Output:

```shell
```

In the preceding example:

- `$match` filters for Action movies released in 2000 that have an
  `imdb.rating` value.

- `sortBy: { "imdb.rating": 1 }` sorts documents by IMDb rating in
  ascending order. A `sortBy` is required when using a range-based
  window.

- `output` uses `$count` to set the `moviesWithSimilarRating`
  field to the number of movies whose IMDb rating falls within the
  current window.

  The window uses
  `range: [ -0.5, 0.5 ]`, which includes all documents whose
  `imdb.rating` is within 0.5 points of the current document's
  rating.

- `$project` includes the `title`, `imdb.rating`, and
  `moviesWithSimilarRating` fields in the output.

- `$sort` and `$limit` return the 10 highest-rated movies for
  readability.

The output shows that Gladiator (8.5), with a relatively unique
rating, has a lower `moviesWithSimilarRating` count than movies
with more common ratings such as 7.4.
