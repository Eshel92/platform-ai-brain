<!-- Converted from reference/operator/aggregation/max.txt (reStructuredText). Includes are inlined. -->

# $max (accumulator operator)

## Definition

**`$max`**

Returns the maximum value. `$max` compares both value and
type, using the specified BSON comparison order for values of different types.

The `$max` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$max` when used as an **accumulator**.
Accumulators return a single aggregated value like sum, maximum,
or minimum across a group of input documents.

You can also use `$max` in these other contexts:

- `$max (expression)`, which returns the
  maximum value from an array or a list of values.

- `$max (window function)`, which is used in
  the `$setWindowFields` stage to return the maximum
  value from documents in a particular window.

## Syntax

```javascript
{ $max: <expression> }
```

## Behavior

### Result Type

`$max` compares input data following the
BSON Comparison order to
determine the appropriate output type. When the input data contains
multiple data types, the `$max` output type is the highest in the
comparison order.

### Null and Missing Values

If some, **but not all**, input values for `$max` are `null` or
missing, `$max` only considers the non-null and non-missing values.

If **all** input values for `$max` are `null` or missing, `$max`
returns `null`.

### Array Operand

In the `$group` stage, if the expression resolves to an
array, `$max` does not traverse the array and compares the
array as a whole.

### Equal Values

If multiple values compare as equal, `$max` may return any of those values.
There is no guarantee which equal value `$max` returns.

For example, under a case-insensitive collation, `"a"` and `"A"` can compare as equal.
There is no guarantee which will be returned.

### Use in `$group` Stage

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$max` in a `$group` stage
to find the highest IMDb rating and longest runtime for movies in
each rating category:

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies with a common US
  rating, a valid IMDb rating, and a known runtime.
- Sorts documents by `rated` to ensure consistent grouping
  order.
- Uses `$group` with `$max` to find the highest IMDb
  rating and longest runtime for each `rated` group.
- Sorts the output alphabetically by rating category.
