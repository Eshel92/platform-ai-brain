<!-- Converted from reference/mql/window-functions/stdDevPop.txt (reStructuredText). Includes are inlined. -->

# $stdDevPop (window function)

## Definition

**`$stdDevPop`**

Returns the population standard deviation of values from documents in
a particular window.

**Note:** Disambiguation

This page describes `$stdDevPop` when used as a **window
function**.

You can also use `$stdDevPop` in these other contexts:

- `$stdDevPop (accumulator)`, which returns the
  population standard deviation of values across a group of
  documents.

- `$stdDevPop (expression)`, which returns
  the population standard deviation of numeric values in an array.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $stdDevPop: <expression>
         }
      }
   }
}
```

## Behavior

### Result Type

`$stdDevPop` returns the population standard deviation of the
input values as a `double`.

### Non-Numeric Values

The `$stdDevPop` window function ignores non-numeric values. If the
window contains no numeric values, `$stdDevPop` returns `null`.

### Single Value

If the input consists of a single numeric value, `$stdDevPop`
returns `0`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to add to each
document a field that contains the running population standard
deviation of IMDb ratings for Musicals from 2009 and 2010.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for Musicals from 2009
  and 2010 with a numeric IMDb rating.

- Uses `$setWindowFields` to partition movies by `year`
  and sort them by `title`. The stage uses `$stdDevPop` with a
  documents window of
  `[ "unbounded", "current" ]` to create
  `stdDevPopRatingInYear`. The `stdDevPopRatingInYear` field
  holds the running population standard deviation of `imdb.rating`
  from the start of the partition to the current document.
  `$documentNumber` assigns a per-partition row number
  (`rankInYear`) to each document.

- Uses `$project` to include `title`, `year`,
  `imdb`, `stdDevPopRatingInYear`, and `rankInYear` in the
  output.

- Uses `$sort` to sort the results by year and title.
