<!-- Converted from reference/expression/firstN.txt (reStructuredText). Includes are inlined. -->

# $firstN (expression)

## Definition

**`$firstN`**

Returns the specified number of elements from the beginning of an array.

**Note:** Disambiguation

This page describes `$firstN` when used as an **expression**, which
returns the specified number of elements from the beginning of an array.

You can also use `$firstN` in these other contexts:

- `$firstN (accumulator)`, used in grouping to
  return the first `n` elements from each group.

- `$firstN (window function)`, which is used in the
  `$setWindowFields` stage to return the first `n` values
  from documents in a particular window.

## Syntax

```javascript
{ $firstN: { input: <expression>, n: <expression> } }
```

### Options

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The array from which to return the first `n` elements. |
| `n` | Expression | The number of elements that `$firstN` returns. Must resolve to a positive integer. |

## Behavior

- `$firstN` returns elements in the same order they appear in 
  the input array.

- `$firstN` does not filter out `null` values in the input 
  array.

- You cannot specify a value of `n` less than `1`.

- If the specified `n` is greater than or equal to the number of
  elements in the `input` array, `$firstN` returns the entire
  `input` array. 

- If `input` resolves to a non-array value, the aggregation operation 
  errors.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses the `$firstN` operator to return the first
three cast members for each movie. The cast members are returned in the new field
`firstThreeCast` created by `$addFields`. 

```shell
```

Output:

```shell
```

The preceding pipeline:

- Uses `$match` to filter for three specific movies.
- Uses `$addFields` with `$firstN` to create a new field
  `firstThreeCast` containing the first three elements from the
  `cast` array with `n: 3`.
- Uses `$project` to include only the `title`, `cast`,
  and `firstThreeCast` fields in the output.
- Uses `$sort` to sort the results by title.

## Learn More

- `$lastN`
- `$sortArray`
