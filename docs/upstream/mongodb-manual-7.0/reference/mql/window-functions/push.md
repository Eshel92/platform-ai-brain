<!-- Converted from reference/mql/window-functions/push.txt (reStructuredText). Includes are inlined. -->

# $push (window function)

## Definition

**`$push`**

Returns an array of all values, including duplicates, that result
from applying an expression to each document in a window.

**Note:** Disambiguation

This page describes `$push` when used as a **window function**.

You can also use `$push` in these other contexts:

- `$push (accumulator)`, which returns the resulting
  array after applying an expression to each document in a group.
- `$push (update operator)`, which appends a value
  to an array field in a document.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $push: <expression>
         }
      }
   }
}
```

## Behavior

`$push` includes all values in the window, including duplicates. The
order of elements in the output array corresponds to the sort order
specified in the `$setWindowFields` `sortBy` field.

The `internalQueryMaxPushBytes` server parameter limits the amount
of memory that the accumulated array can use. To learn more, see
agg-memory-push-accumulator.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses the `$push` window function to build a running list
of genres across movies from 2002. For each movie, `$push` adds the
movie's primary genre to `genresSeenSoFar`, retaining all values
including duplicates.

```javascript
```

Output:

```javascript
```

In the example:

- The `$match` stage filters to movies from 2002 with genre
  information.

- The `$addFields` stage adds a `primaryGenre` field that
  contains the first element in the `genres` array.

- The `$setWindowFields` stage uses `$push` with an
  `unbounded` to `current` window
  to accumulate all genres from the beginning of the result set up to
  the current document.

- The `$project` stage reshapes the output and calculates
  `totalGenreCount` to show how the array grows with each document.

- The `$limit` stage restricts output to 8 documents
  to improve readability.

`totalGenreCount` increases by one with every document. The seventh
document (`'3 Extremes II'`) has genre `Horror`, which was already
in the array, so `Horror` appears twice in `genresSeenSoFar`. This
demonstrates that `$push` includes duplicate values, unlike
`$addToSet`, which adds only unique values.

## Learn More

- window-functions-ref
- `$addToSet`
- agg-pipeline-limits
