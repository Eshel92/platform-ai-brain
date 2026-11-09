<!-- Converted from reference/mql/window-functions/stdDevSamp.txt (reStructuredText). Includes are inlined. -->

# $stdDevSamp (window function)

## Definition

**`$stdDevSamp`**

Returns the sample standard deviation of values in a window.

**Note:** Disambiguation

This page describes `$stdDevSamp` when used as a **window
function**.

You can also use `$stdDevSamp` in these other contexts:

- `$stdDevSamp (accumulator)`, which
  calculates the sample standard deviation of values across a
  group of documents.

- `$stdDevSamp (expression)`, which
  calculates the sample standard deviation of numeric values in an
  array.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $stdDevSamp: <expression>
         }
      }
   }
}
```

## Behavior

### Result Type

`$stdDevSamp` returns the sample standard deviation of the input
values as a `double`.

### Non-Numeric and Missing Values

The `$stdDevSamp` window function ignores non-numeric values,
including missing values. If the window contains no numeric values,
`$stdDevSamp` returns `null`.

### Single Value

If the window contains only one document, `$stdDevSamp` returns
`null`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to calculate a running
sample standard deviation field for each Musical movie from 2009 and
2010. Each document receives the `$stdDevSamp` value computed from the
beginning of its yearly partition through the current document.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for Musical movies from 2009
  and 2010 with a numeric IMDb rating.

- Uses `$setWindowFields` to partition movies by `year` and
  sort them by `title`. The stage uses `$stdDevSamp` with a
  documents window of ``[
  "unbounded", "current" ]`` to create the following fields for each
  document:

  - `stdDevSampRatingInYear`: the running sample standard deviation
    of `imdb.rating`.

  - `rankInYear`: a per-partition row number assigned by
    `$documentNumber`.

  The first document in each partition has only one value in
  its window, so `stdDevSampRatingInYear` is `null`. Each
  subsequent document adds one more value to the window.

- Uses `$project` to include `title`, `year`,
  `imdb`, `stdDevSampRatingInYear`, and `rankInYear`
  in the output.

- Uses `$sort` to sort results by year and title.

## Learn More

- aggregation
- aggregation-expressions
- window-functions-ref
