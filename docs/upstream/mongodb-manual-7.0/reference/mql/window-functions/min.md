<!-- Converted from reference/mql/window-functions/min.txt (reStructuredText). Includes are inlined. -->

# $min (Window Function)

## Definition

**`$min`**

Returns the minimum value from documents in a particular window.

**Note:** Disambiguation

This page describes `$min` when used as a **window
function**.

You can also use `$min` in these other contexts:

- `$min (accumulator)`, used in grouping to return the
  minimum value from a group of documents.

- `$min (expression)`, which returns the
  minimum value from an array.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $min: <expression>
         }
      }
   }
}
```

## Behavior

### Result Type

When `$min` compares values of different types, it uses the
BSON comparison order
to determine which value is smaller.

### Null or Missing Values

If some documents in the window have a `null` value for the
field or are missing the field, `$min` ignores them. It
considers only the non-null and non-missing values.

If **all** documents in the window have a `null` value for the
field or are missing the field, `$min` returns `null`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to add a field
to each document containing the IMDb rating of the
worst-rated movie released in the same year:

```shell
```

Output:

```shell
```

The preceding pipeline:

- Uses `$match` to filter to movies from 1999,
  2000, and 2001 with an IMDb rating of 3.0 or lower.

- Uses `$setWindowFields` to partition movies by
  `year` and sort them by `title`. The stage uses
  `$min` with a
  documents window of
  `[ "unbounded", "unbounded" ]` to create
  `minimumRatingInYear`, which holds the minimum
  `imdb.rating` across the entire partition, and
  `$documentNumber` to assign a per-partition row number
  (`rankInYear`) to each document.

- Uses `$project` to include `title`, `year`,
  `imdb`, `minimumRatingInYear`, and `rankInYear`
  in the output.

- Uses `$sort` to sort the results by year and
  title.
