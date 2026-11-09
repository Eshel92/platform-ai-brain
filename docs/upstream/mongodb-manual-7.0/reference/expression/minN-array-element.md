<!-- Converted from reference/expression/minN-array-element.txt (reStructuredText). Includes are inlined. -->

# $minN (expression operator)

## Definition

**`$minN`**

Returns the `n` smallest values in an array.

**Note:** Disambiguation

This page describes `$minN` when used as an **expression**, which
returns the `n` minimum values in an array.

You can also use `$minN` in these other contexts:

- `$minN (accumulator)`, which returns an
  aggregated value based on a variable number of input documents.

- `$minN (window function)`, which is used in the
  `$setWindowFields` stage to return the minimum `n`
  values from documents in a particular window.

## Syntax

```javascript
{ $minN: { n: <expression>, input: <expression> } }
```

| Field | Description |
|---|---|
| `n` | An expression that evaluates to a positive integer. The integer specifies the number of array elements that `$minN` returns. |
| `input` | An expression that evaluates to the array from which to return the minimum `n` elements. |

## Behavior

- You cannot specify a value of `n` less than `1`.

- `$minN` filters out `null` values found in the `input` 
  array.

- If the specified `n` is greater than or equal to the number of elements 
  in the `input` array, `$minN` returns all elements in the 
  `input` array.

- If `input` resolves to a non-array value, the expression 
  produces an error.

- If `input` contains elements of different types, comparisons across types follow the
  BSON comparison order.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses the `$minN` operator to return
the two alphabetically-first genres for each movie. The results are
returned in the new field `firstAlphabeticalGenres` created by
`$addFields`.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter for movies that have at least three
  genres.
- Uses `$addFields` to create a `firstAlphabeticalGenres` field.
  `$minN` with `n: 2` returns the two alphabetically-first values
  from the `genres` array.
- Uses `$project` to return only the `title`, `genres`,
  and `firstAlphabeticalGenres` fields.
- Uses `$limit` to return five documents to improve readability.
