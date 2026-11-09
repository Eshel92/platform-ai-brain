<!-- Converted from reference/expression/first.txt (reStructuredText). Includes are inlined. -->

# $first (expression)

## Definition

**`$first`**

Returns the first element of an array.

**Note:** Disambiguation

This page describes `$first` when used as an **expression**, which
returns the first element of an array.

You can also use `$first` in these other contexts:

- `$first (accumulator)`, used in grouping to return
  the first value from each group.
- `$first (window function)`, used in the
  `$setWindowFields` stage to return a value for the first
  document in a window.

## Syntax

```javascript
{ $first: <expression> }
```

The `<expression>` must evaluate to an array.

## Behavior

- If the operand expression evaluates to an array, `$first` returns the first
  element of that array.

- If the array is empty, `$first` returns `null`.

- If the expression evaluates to `null` or refers to a missing field,
  `$first` returns `null`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$first` to return the top-billed actor
for each movie. In the `sample_mflix` dataset, the `cast` array
lists actors in billing order, so the first element is the top-billed
actor:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters for three specific movies.
- `$addFields` with `$first` creates a new field
  `topBilledActor` containing the first element of the `cast`
  array.
- `$project` includes only the `title`, `cast`,
  and `topBilledActor` fields in the output.
- `$sort` sorts the results by title.

## Learn More

- `$arrayElemAt`
- `$max`
- read-operations-arrays
