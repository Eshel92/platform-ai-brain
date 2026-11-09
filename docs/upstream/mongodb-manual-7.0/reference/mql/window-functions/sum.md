<!-- Converted from reference/mql/window-functions/sum.txt (reStructuredText). Includes are inlined. -->

# $sum (Window Function)

## Definition

**`$sum`**

Returns the sum of numeric values from documents in a particular window.

**Note:** Other Uses of `$sum`

This page describes `$sum` when used as a **window function**.

You can also use `$sum` in these other contexts:

- `$sum (accumulator)`, which returns the
  collective sum of numeric values across a group of documents.

- `$sum (expression)`, which returns the
  sum of numeric values in an array.

## Syntax

```javascript
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $sum: <expression>
         }
      }
   }
}
```

## Behavior

### Result Type

When input types are mixed, `$sum` promotes the smaller input type
to the larger of the two. A type is considered larger when it
represents a wider range of values. The order of numeric types from
smallest to largest is: integer → long → double → decimal.

The larger of the input types also determines the result type unless
the operation overflows and is beyond the range represented by that
larger data type. In cases of overflow, `$sum` promotes the result
according to the following order:

- If the larger input type is `integer`, the result
  type is promoted to `long`.

- If the larger input type is `long`, the result
  type is promoted to `double`.

- If the larger type is `double` or
  `decimal`, the overflow result is represented
  as positive or negative infinity. There is no type promotion of the
  result.

### Null or Missing Values

If some documents in the window have a `null` value for the
field or are missing the field, `$sum` ignores those values
and sums the remaining values.

If **all** documents in the window have a `null` value for the
field or are missing the field, `$sum` returns `0`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

This example uses `$setWindowFields` to calculate a
running cumulative vote total for each Musical movie from 2009
and 2010. Each document receives the `$sum` value computed from
the beginning of its yearly partition through the current document.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for Musical movies from 2009
  and 2010 with a numeric IMDb rating and at least one vote.

- Uses `$setWindowFields` to partition movies by
  `year` and sort them by `title`. The stage uses `$sum`
  with a documents window of
  `[ "unbounded", "current" ]` to create the following fields
  for each document:

  - `cumulativeVotesInYear`: the running cumulative sum of
    `imdb.votes`.

  - `rankInYear`: a per-partition row number assigned by
    `$documentNumber`.

- Uses `$project` to include `title`, `year`,
  `imdb.votes`, `cumulativeVotesInYear`, and `rankInYear`
  in the output.

- Uses `$sort` to sort results by year and title.

## Learn More

- window-functions-ref
- read-operations-projection
- agg-pipeline-limits
