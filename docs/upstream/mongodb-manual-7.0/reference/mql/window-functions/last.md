<!-- Converted from reference/mql/window-functions/last.txt (reStructuredText). Includes are inlined. -->

# $last (window function)

## Definition

**`$last`**

Returns the value of an expression for the last document in a window.

**Note:** Disambiguation

This page describes `$last` when used as a **window function**.

You can also use `$last` in these other contexts:

- `$last (accumulator)`, used in grouping to return
  a value for the last document in each group.
- `$last (expression)`, which returns the
  last element of an array.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $last: <expression>
         }
      }
   }
}
```

## Behavior

The `$last` window function has the following behaviors for null and missing values:

- `$last` converts missing field values to `null`.
- `$last` returns `null` for empty windows.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to partition low-rated
movies by `year`, sort them by `imdb.rating` in descending order,
and identify the lowest-rated movie in each year. Each document includes
a field showing the title of the lowest-rated movie in that year's
partition:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters for movies released between 1999 and 2001
  with an IMDb rating of 3.5 or lower.
- `$setWindowFields` partitions movies by `year` and sorts
  them by `imdb.rating` in descending order, with `title` as a
  tiebreaker. The stage uses `$last` with a window defined as
  `documents: [ "unbounded", "unbounded" ]` to return the title of
  the lowest-rated movie in each year's partition.
- `$project` includes only `title`, `year`,
  `imdb.rating`, and `lowestRatedMovieInYear` in the output.
- `$sort` sorts the results by year, rating, and title.
