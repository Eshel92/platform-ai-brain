<!-- Converted from reference/mql/window-functions/max.txt (reStructuredText). Includes are inlined. -->

# $max (window function)

## Definition

**`$max`**

Returns the maximum value from documents in a particular window.

**Note:** Disambiguation

This page describes `$max` when used as a **window
function**.

You can also use `$max` in these other contexts:

- `$max (accumulator)`, which returns the
  maximum value across a group of input documents.

- `$max (expression)`, which returns the
  maximum value from an array or a list of values.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $max: <expression>
         }
      }
   }
}
```

## Behavior

### Result Type

`$max` compares input data following the
BSON Comparison order to
determine the appropriate output type. When the input data contains
multiple data types, the `$max` output type is the highest in the
comparison order.

### Null and Missing Values

If some, **but not all**, documents in the window have a `null` value for the
field or are missing the field, `$min` ignores them. It
considers only the non-null and non-missing values.

If **all** documents in the window have a `null` value for the
field or are missing the field, `$min` returns `null`.

### Array Operand

In the `$setWindowFields` stage, if the expression
evaluates to an array, `$max` does not traverse the array and
compares the array as a whole.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$max` in the `$setWindowFields`
stage to output the highest IMDb rating for highly-rated movies
in 1999 and 2000. For each movie, the pipeline adds a field
containing the highest IMDb rating across all movies in that
year:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters for movies from 1999 and 2000 with
  an IMDb rating of 8.5 or higher.

- `$setWindowFields` partitions movies by `year` and
  sorts them by `imdb.rating` in ascending order within each
  partition. The `$max` window function uses a
  documents window with
  `unbounded` lower and upper limits, spanning the entire
  partition. `$max` returns the highest `imdb.rating`
  across all documents in each year's partition.

- `$project` limits the output to `title`, `year`,
  `imdb.rating`, and the computed `highestRatingInYear` field.

- `$sort` orders results by year and then by IMDb
  rating in ascending order.
