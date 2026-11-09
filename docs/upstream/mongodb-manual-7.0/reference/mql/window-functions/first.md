<!-- Converted from reference/mql/window-functions/first.txt (reStructuredText). Includes are inlined. -->

# $first (window function)

## Definition

**`$first`**

Returns the value of an expression for the first document in a window.

**Note:** Disambiguation

This page describes `$first` when used as a **window function**.

You can also use `$first` in these other contexts:

- `$first (accumulator)`, used in grouping to return
  the first value from each group.

- `$first (expression)`, which returns the
  first element of an array.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $first: <expression>
         }
      }
   }
}
```

## Behavior

The `$first` window function has the following behaviors for null and
missing values:

- `$first` converts missing field values to `null`.
- `$first` returns `null` for empty windows.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to partition movies by
`year`, sort them by `imdb.rating` in descending order, and identify
the highest-rated movie in each year. Each document includes a field
showing the title of the highest-rated movie released in that year:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters for movies from 1999-2001 with an
  IMDb rating of 8.5 or higher.
- `$setWindowFields` partitions movies by `year` and
  sorts them by `imdb.rating` in descending order. The stage uses
  `$first` with a window defined as ``documents: [ "unbounded",
  "unbounded" ]`` to return the title of the highest-rated movie in
  each year's partition.
- `$project` includes only `title`, `year`,
  `imdb.rating`, and `topRatedMovieInYear` in the output.
- `$sort` sorts the results by year and rating.
