<!-- Converted from reference/operator/aggregation/last.txt (reStructuredText). Includes are inlined. -->

# $last (accumulator operator)

## Definition

**`$last`**

Returns the result of an expression for
the last document in a group of documents. Only meaningful when
documents are in a defined order.

The `$last` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$last` when used as an **accumulator**.
Accumulators return a single aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$last` in these other contexts:

- `$last (expression)`, which returns the last
  element of an array.
- `$last (window function)`, used in the
  `$setWindowFields` stage to return a value for the last
  document in a window.

## Syntax

```javascript
{ $last: <expression> }
```

## Behavior

### Define Document Order

To define document order for `$last` in a grouping stage, add a
preceding `$sort` stage.

### Missing Values

Documents in a group may be missing fields. `$last` handles missing
values as follows:

- If there are no documents from the prior pipeline stage, the
  `$group` stage returns nothing.

- When the `expression` for the last document in the group evaluates
  to a missing value, `$last` returns `null`.

For example, consider the following documents in the `badData`
collection, where some documents are missing fields:

```javascript
db.badData.insertMany( [
   { "_id": 1, "price": 6, "quantity": 6 },
   { "_id": 2, "item": "album", "price": 5, "quantity": 5  },
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
db.badData.aggregate( [
   { $sort: { item: 1, price: 1 } },
   { $group:
      {
         _id: "$item",
         inStock: { $last: "$quantity" }
      }
   }
] )
```

Output:

```javascript
[
  { _id: null, inStock: 6 },
  { _id: 'album', inStock: 5 },
  { _id: 'cd', inStock: null },
  { _id: 'tape', inStock: 6 }
]
```

`$last` selects the last document from each output group. Documents
that are missing the `item` field are grouped together with a
`null` value for the `_id` field. When the accumulator field is
missing (`quantity` in this example), `$last` returns `null`.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following example sorts movies by year and title, then groups them
by genre to find the most recent movie released in each genre:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters to movies with an integer `year` field.
  This eliminates bad data where `year` is missing or not a number.
- `$sort` orders movies by `year` in ascending order, then
  `title` in alphabetical order.
- `$unwind` creates a separate document for each genre in the
  `genres` array, maintaining the previously established sort order.
- `$group` with `$last` returns the `title` and `year`
  of the last movie (most recent by year and alphabetically last by
  title) for each genre.
- A second `$sort` sorts the results alphabetically
  by genre.
- `$limit` restricts the output to 5 genres.

## Learn More

- `$last (expression)`
- `$last (window function)`
- `$first`
