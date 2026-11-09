<!-- Converted from reference/expression/lastN.txt (reStructuredText). Includes are inlined. -->

# $lastN (expression)

## Definition

**`$lastN`**

Returns the specified number of elements from the end of an array.

**Note:** Disambiguation

This page describes `$lastN` when used as an **expression**, which
returns the specified number of elements from the end of an array.

You can also use `$lastN` in these other contexts:

- `$lastN (accumulator)`, used in grouping to
  return the last `n` elements from each group.

- `$lastN (window function)`, which is used in the
  `$setWindowFields` stage to return the last `n` values
  from documents in a particular window.

## Syntax

```javascript
{ $lastN: { input: <expression>, n: <expression> } }
```

### Options

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The array from which to return the last `n` elements. |
| `n` | Expression | The number of elements that `$lastN` returns. Must resolve to a positive integer. |

## Behavior

- `$lastN` returns elements in the same order they appear in
  the input array.

- `$lastN` does not filter out `null` values in the input
  array.

- You cannot specify a value of `n` less than `1`.

- If the specified `n` is greater than or equal to the number of
  elements in the `input` array, `$lastN` returns the entire
  `input` array.

- If `input` resolves to a non-array value, the expression
  errors.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses the `$lastN` operator to return the last
three cast members for each movie. The cast members are returned in the new field
`lastThreeCast` created by `$addFields`.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for three specific movies.
- Uses `$addFields` with `$lastN` to create a new field
  `lastThreeCast` containing the last three elements from the
  `cast` array.
- Uses `$project` to include only the `title`, `cast`,
  and `lastThreeCast` fields in the output.
- Uses `$sort` to sort the results by title.

## Learn More

- `$firstN`
- `$sortArray`
