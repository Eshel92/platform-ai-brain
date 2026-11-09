<!-- Converted from reference/mql/window-functions/addToSet.txt (reStructuredText). Includes are inlined. -->

# $addToSet (window function)

## Definition

**`$addToSet`**

Returns an array of all unique values from a particular window.

The order of the elements in the returned array is unspecified.

**Note:** Disambiguation

This page describes `$addToSet` when used as a **window function**.

You can also use `$addToSet` in these other contexts:

- `$addToSet (accumulator)`, which returns a single
  aggregated value based on a variable number of input documents.
- `$addToSet (update operator)`, which adds elements
  to an array field in a document.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $addToSet: <expression>
         }
      }
   }
}
```

## Behavior

If the value of the expression is an array, `$addToSet` appends the
whole array as a single element.

If the value of the expression is a document, MongoDB determines that
the document is a duplicate if another document in the array matches the
to-be-added document exactly. Specifically, the existing document has
the exact same fields and values in the exact same order.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses the `$addToSet` window function to show how unique
genres accumulate across movies over time. Movies are sorted
alphabetically by title, and the window function tracks all unique
genres that have appeared in movies from the beginning of the result set
up to and including the current movie.

```shell
```

Output:

```shell
```

In the example:

- The `$match` stage filters to movies from 2002 with genre
  information.

- The `$group` stage groups by year, title, and the first
  genre in the `genres` array.

- The `$setWindowFields` stage uses `$addToSet` with an
  `unbounded` to `current` window to
  accumulate unique genres from the beginning of the result set up to the
  current document.

- The `$project` stage reshapes the output and calculates
  `uniqueGenreCount` to show how the set size grows.

- The `$limit` stage restricts output to 8 documents.

The output demonstrates how `$addToSet` accumulates unique genres
across documents. Notice that `genresSeenSoFar` grows from 1 genre to
7 genres as each movie adds its genre to the set. The seventh document
(`'3 Extremes II'`) has the same `uniqueGenreCount` as the sixth
because its genre (Horror) was already in the set. This demonstrates
that `$addToSet` only adds unique values and ignores duplicates.
