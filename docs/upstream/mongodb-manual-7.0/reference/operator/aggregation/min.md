<!-- Converted from reference/operator/aggregation/min.txt (reStructuredText). Includes are inlined. -->

# $min (Accumulator Operator)

## Definition

**`$min`**

Returns the minimum value across a group of documents.

The `$min` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$min` when used as an **accumulator**.
Accumulators return an aggregated value like sum,
maximum, or minimum across a group of input documents.

You can also use `$min` in these other contexts:

- `$min (expression)`, which returns the
  minimum value from an array.

- `$min (window function)`, which is used in
  the `$setWindowFields` stage to return the
  minimum value from documents in a particular window.

## Syntax

```none
{ $min: <expression> }
```

## Behavior

### Result Type

When `$min` compares values of different types, it uses the
BSON comparison order
to determine which value is smaller.

### Null or Missing Values

If some documents have a `null` value for the field or are
missing the field, `$min` ignores them. It considers
only the non-null and non-missing values.

If **all** documents have a `null` value for the field or are
missing the field, `$min` returns `null`.

### Array Operand

In the `$group` stage, if the expression resolves to
an array, `$min` does not traverse the array. It
compares the array as a whole.

### Equal Values

If multiple values compare as equal, `$min` may return any of those values.
There is no guarantee which equal value `$min` returns.

For example, under a case-insensitive collation, `"a"` and `"A"` can compare as equal.
There is no guarantee which will be returned.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Use $min in a $group Stage

The following example groups movies by MPAA rating and
returns the lowest IMDb rating for each group.

```shell
```

Output:

```shell
```

The preceding pipeline:

- Uses `$match` to filter for movies with a
  `rated` value of `G`, `PG`, `PG-13`, or `R`
  and a numeric IMDb rating.
- Uses `$group` to group movies by the `rated`
  field and computes `lowestRating` using `$min` on
  `imdb.rating`.
- Uses `$sort` to return the results in
  alphabetical order by content rating.
