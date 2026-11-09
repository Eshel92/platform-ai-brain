<!-- Converted from reference/expression/max.txt (reStructuredText). Includes are inlined. -->

# $max (expression)

## Definition

**`$max`**

Returns the maximum value from an array.

**Note:** Disambiguation

This page describes `$max` when used as an **expression**,
which returns the maximum value from an array or a list of
values.

You can also use `$max` in these other contexts:

- `$max (accumulator)`, which returns a single
  aggregated value based on a variable number of input
  documents.

- `$max (window function)`, which is used in
  the `$setWindowFields` stage to return the maximum
  value from documents in a particular window.

## Syntax

```javascript
{ $max: <expression> }
```

The `expression` must evaluate to an array.

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

With a single expression as its operand, if the expression
resolves to an array, `$max` traverses the array to find the
maximum value.

With a list of expressions as its operand, if any expression
resolves to an array, `$max` does **not** traverse that array
and instead compares the array as a whole.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$max` in the `$project`
stage to find the highest rating for each movie across three
rating sources: IMDb, Rotten Tomatoes viewer, and Rotten Tomatoes
critic:

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for three specific movies that
  have valid ratings from all three sources.
- Uses `$project` with `$max` and a list of
  expressions to compute the highest rating across
  `imdb.rating`, `tomatoes.viewer.rating`, and
  `tomatoes.critic.rating` for each movie.
- Sorts the output alphabetically by title.
