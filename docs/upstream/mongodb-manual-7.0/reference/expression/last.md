<!-- Converted from reference/expression/last.txt (reStructuredText). Includes are inlined. -->

# $last (expression)

## Definition

**`$last`**

Returns the last element of an array.

**Note:** Disambiguation

This page describes `$last` when used as an **expression**, which
returns the last element of an array.

You can also use `$last` in these other contexts:

- `$last (accumulator)`, used in grouping to return
  a value for the last document in each group.
- `$last (window function)`, used in the
  `$setWindowFields` stage to return a value for the last
  document in a window.

## Syntax

```javascript
{ $last: <expression> }
```

The `<expression>` must evaluate to an array.

## Behavior

- If the array is empty, `$last` returns `null`.

- If the expression evaluates to `null` or refers to a missing field,
  `$last` returns `null`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$last` to return the last cast member listed
for each movie:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters for three specific movies.
- `$addFields` with `$last` creates a new field `lastCast`
  containing the last element of the `cast` array.
- `$project` includes only the `title`, `cast`,
  and `lastCast` fields in the output.
- `$sort` sorts the results by title.

## Learn More

- `$arrayElemAt`
- read-operations-arrays
