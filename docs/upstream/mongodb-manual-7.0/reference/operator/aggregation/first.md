<!-- Converted from reference/operator/aggregation/first.txt (reStructuredText). Includes are inlined. -->

# $first (accumulator operator)

## Definition

**`$first`**

Returns the result of an expression for
the first document in a group of documents. Only meaningful when
documents are in a defined order.

The `$first` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$first` when used as an **accumulator**.
Accumulators return a single aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$first` in these other contexts:

- `$first (expression)`, which returns the first
  element of an array.
- `$first (window function)`, which is used in the
  `$setWindowFields` stage to return a value for the first
  document in a window.

## Syntax

```javascript
{ $first: <expression> }
```

## Behavior

### Define Document Order

To define document order for `$first` in a grouping stage, add a
preceding `$sort` stage.

### Missing Values

Documents in a group may be missing fields. `$first` handles missing
values as follows:

- If there are no documents from the prior pipeline stage, the
  `$group` stage returns nothing.

- If the field that the `$first` accumulator is processing is
  missing, `$first` returns `null`.

For example, consider the following documents in the `badData`
collection, where some documents are missing fields:

```javascript
db.badData.insertMany( [
   { "_id": 1, "price": 6, "quantity": 6 },
   { "_id": 2, "item": "album", "price": 5, "quantity": 5 },
   { "_id": 7, "item": "tape", "price": 6, "quantity": 6 },
   { "_id": 8, "price": 5, "quantity": 5 },
   { "_id": 9, "item": "album", "price": 3, "quantity": '' },
   { "_id": 10, "item": "tape", "price": 3, "quantity": 4 },
   { "_id": 12, "item": "cd", "price": 7 }
] )
```

Query the `badData` collection, grouping the output on the `item`
field:

```javascript
```

Output:

```javascript
```

`$first` selects the first document from each output group. Documents
that are missing the `item` field are grouped together with a
`null` value for the `_id` field. When the accumulator field is
missing (`quantity` in this example), `$first` returns `null`.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example sorts movies by year and title, then groups them
by genre to find the earliest movie released in each genre:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$sort` orders movies by `year` in ascending order, then
  `title` in alphabetical order.
- `$unwind` creates a separate document for each genre in the
  `genres` array, maintaining the sort order established by the
  previous stage.
- `$group` with `$first` returns the `title` and `year`
  of the first movie (earliest by year, then alphabetically by title)
  for each genre.
- A second `$sort` sorts the results alphabetically
  by genre.
- `$limit` restricts the output to 5 genres.
