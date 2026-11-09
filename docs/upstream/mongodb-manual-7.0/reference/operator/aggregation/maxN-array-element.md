<!-- Converted from reference/operator/aggregation/maxN-array-element.txt (reStructuredText). Includes are inlined. -->

# $maxN (expression operator)

## Definition

**`$maxN`**

Returns the `n` largest values in an array.

**Note:** Other Uses of `$maxN`

This page describes `$maxN` when used as an **expression**,
which returns the largest `n` values from an array.

You can also use `$maxN` in these other contexts:

- `$maxN (accumulator)`, which returns the maximum
  `n` values within a group.

- `$maxN (window function)`, which is used in the
  `$setWindowFields` stage to return the largest `n`
  values from documents in a particular window.

## Syntax

```javascript
{ $maxN: { n: <expression>, input: <expression> } }
```

| Field | Type | Description |
|---|---|---|
| `n` | Expression | Specifies the number of elements to return. Must resolve to a positive integer. |
| `input` | Expression | Specifies the input array from which to return the maximum `n` elements. |

## Behavior

- `$maxN` filters out `null` values.

- If the `input` array contains fewer than `n` elements,
  `$maxN` returns all elements in the array.

- If `input` resolves to a non-array value, the operation returns
  an error.

- If `input` contains both numeric and string elements, string
  elements are sorted before numeric elements according to the
  BSON comparison order.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$maxN` to return the two alphabetically
last cast members for each movie, stored in a new `topTwoCast`
field created by `$addFields`.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for three specific movies.
- Uses `$addFields` with `$maxN` to create a new field
  `topTwoCast` containing the two alphabetically last values from
  the `cast` array with `n: 2`.
- Uses `$project` to include only the `title`, `cast`,
  and `topTwoCast` fields in the output.
- Uses `$sort` to sort the results by title.

## Learn More

- agg-pipeline-limits
