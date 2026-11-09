<!-- Converted from reference/operator/aggregation/count-accumulator.txt (reStructuredText). Includes are inlined. -->

# $count (accumulator operator)

## Definition

**`$count`**

Returns the number of documents in a group.

The `$count` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes the `$count` aggregation accumulator. You
can also use `$count` in these other contexts:

- `$count (aggregation stage)`, which returns the
  number of input documents.

- `$count (window function)`, which is used in the
  `$setWindowFields` stage to return the number of
  documents in a particular window.

## Syntax

```none
{ $count: { } }
```

The `$count` accumulator does not accept any parameters.

**Tip:**

The `$count` accumulator is functionally equivalent to using ``{
$sum: 1 }`` within the `$group` stage.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$count` in the `$group` stage to
count the number of movies in the `sample_mflix.movies` collection
for each selected `genre`:

```shell
```

Output:

```shell
```

In the example:

- `$unwind: "$genres"` creates a document for each value in the
  `genres` array.

- `$match` limits the documents to the `Drama` and `Short`
  genres.

- `_id: "$genres"` groups the documents by genre.

- `$count: {}` sets the `countNumberOfMoviesForGenre` field to the
  number of movies that share the same genre.

The output shows the number of movies for `Drama` and `Short` in the
`countNumberOfMoviesForGenre` field.
