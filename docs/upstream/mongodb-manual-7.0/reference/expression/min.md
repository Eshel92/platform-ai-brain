<!-- Converted from reference/expression/min.txt (reStructuredText). Includes are inlined. -->

# $min (Expression)

## Definition

**`$min`**

Returns the minimum value from an array.

**Note:** Disambiguation

This page describes `$min` when used as an **expression**.

You can also use `$min` in these other contexts:

- `$min (accumulator)`, used in grouping to return the
  minimum value from a group of documents.

- `$min (window function)`, used in
  the `$setWindowFields` stage to return the
  minimum value from documents in a particular window.

## Syntax

```none
{ $min: <expression> }
```

The `expression` must evaluate to an array.

## Behavior

### Result Type

When `$min` compares values of different types, it uses the
BSON comparison order
to determine which value is smaller.

### Null or Missing Values

If some, **but not all**, input values are `null` or missing,
`$min` considers only the non-null and non-missing values.

If **all** input values are `null` or missing, `$min`
returns `null`.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example uses `$min` in the `$project`
stage to calculate the minimum values from the
`sample_mflix.movies` collection.

```shell
```

Output:

```shell
```

The preceding pipeline:

- Uses `$match` to filter for three specific movies.
- Uses `$project` with `$min` to create two fields:

  - `firstAlphabeticalGenre`: First genre in alphabetical order from
    the genres array, using `{ $min: "$genres" }`
  - `lowestRating`: Lowest rating between IMDb and
    Metacritic, both normalized to a 0–100 scale, using
    `{ $min: [ { $multiply: [ "$imdb.rating", 10 ] }, "$metacritic" ] }`

- Uses `$sort` to sort results by title.
