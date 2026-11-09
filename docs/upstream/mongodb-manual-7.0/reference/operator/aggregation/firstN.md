<!-- Converted from reference/operator/aggregation/firstN.txt (reStructuredText). Includes are inlined. -->

# $firstN (accumulator operator)

## Definition

**`$firstN`**

Returns an aggregation of the first `n` elements in a group. The
results are meaningful only if the input data to the grouping stage has
a defined sort order. If the group contains fewer than `n` elements,
`$firstN` returns all elements in the group.

The `$firstN` accumulator is available in these stages:

- `$bucket`

- `$bucketAuto`

- `$group`

**Note:** Disambiguation

This page describes `$firstN` when used as an **accumulator**.
Accumulators return a single aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$firstN` in these other contexts:

- `$firstN (expression)`, which returns the 
  specified number of elements from the beginning of an array.

- `$firstN (window function)`, which is used in the
  `$setWindowFields` stage to return the first `n` values
  from documents in a particular window.

## Syntax

```none
{
   $firstN:
      {
         input: <expression>,
         n: <expression>
      }
}
```

### Options

| Field | Type | Description |
|---|---|---|
| `input` | Expression | The `input` expression is evaluated over each document in the input group, and the first `n` results are preserved. |
| `n` | Expression | The number of elements that `$firstN` returns from the group. For an example of setting `n` dynamically based on the group key, see first-n-with-group-key. |

## Behavior

### Null and Missing Values

- `$firstN` does not filter out null values.
- `$firstN` converts missing values to null.

### Comparison of $firstN and $topN

Both `$firstN` and `$topN` accumulators can accomplish similar
results.

In general:

- If the documents coming into `$group` are already ordered,
  you should use `$firstN`.
- If you're sorting and selecting the top `n` elements then you can use 
  `$topN` to accomplish both tasks with one accumulator.

## Examples

The examples on this page use the `movies` collection in the
sample_mflix sample dataset. To
learn how to load the sample dataset into your MongoDB deployment, see
load-sample-data.

### Find the First Three Movies for a Single Genre

You can use the `$firstN` accumulator to find the first three movies
in a single genre.

```shell
```

Output:

```shell
```

The preceding pipeline:

- Uses `$match` to filter the results to movies where
  `Horror` is included in the `genres` array.
- Sorts the results by `year` in ascending order.
- Groups all resulting documents into a single group.
- Specifies the fields that are input for `$firstN` with
  `input : ["$title", "$year"]`.
- Uses `$firstN` to return the first three documents
  for the `Horror` genre with `n: 3`.

### Find the First Three Movies Across Multiple Genres

You can use the `$firstN` accumulator to find the first `n`
input fields in each genre.

```shell
```

Output:

```shell
```

   
The preceding pipeline:

- Uses `$unwind` to create a separate document for each genre
  in the `genres` array.
- Sorts the results by `year` in ascending order.
- Uses `$group` to group the results by `genres`.
- Uses `$firstN` to return the first three documents
  for each genre with `n: 3`.
- Specifies the fields that are input for `$firstN` with
  `input : ["$title", "$year"]`.
- Limits the output to five documents to improve readability.

### Set n Based on the Group Key

You can assign the value of `n` dynamically based on the group key. In
this example, the `$cond` expression uses the `rated`
field to change the value of `n`:

```shell
```

Output:

```shell
```

The preceding pipeline:

- Filters for movies with ratings of `G`, `PG`, `PG-13`, or `R`.
- Sorts the results alphabetically by `title`.
- Groups movies by `rated` (the movie rating).
- Uses the `$cond` expression to return `3` movies for `PG`-rated
  movies and `1` movie for all other ratings.

In the output, the `PG` rating returns 3 movies, while `G`,
`PG-13`, and `R` ratings each return 1 movie.

## Learn More

- `$firstN (expression)`
- `$firstN (window function)`
- `$lastN`
