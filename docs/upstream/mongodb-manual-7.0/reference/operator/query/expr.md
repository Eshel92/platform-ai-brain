<!-- Converted from reference/operator/query/expr.txt (reStructuredText). Includes are inlined. -->

# $expr (query predicate operator)

## Definition

**Changed in version:** 5.0

**`$expr`**

Allows the use of expressions within
a query predicate.

## Compatibility

You can use `$expr` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```javascript
{ $expr: { <expression> } }
```

The argument can be any valid expression.

## Behavior

### $expr in $lookup Operations

When `$expr` appears in a `$match` stage that is part of a
`$lookup` subpipeline, `$expr` can refer to `let`
variables defined by the `$lookup` stage. For an example, see
lookup-multiple-joins.

The `$eq`, `$lt`, `$lte`,
`$gt`, and `$gte` comparison operators placed in
an `$expr` operator can use an index on the `from` collection
referenced in a `$lookup` stage. Limitations:

- Indexes can only be used for comparisons between fields and constants, so the
  `let` operand must resolve to a constant.

  For example, a comparison between `$a` and a constant 
  value can use an index, but a comparison between `$a` and `$b` 
  cannot.

- Indexes are not used for comparisons where the `let` operand resolves to an
  empty or missing value.

- Multikey, partial, or 
  sparse indexes are not used.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Compare Two Fields from a Single Document

`$expr` can contain expressions that compare fields from the same
document.

The following operation uses `$expr` to find documents in the
`movies` collection where the Rotten Tomatoes viewer rating exceeds
the critic rating:

```javascript
```

Output:

```javascript
```

### Use $expr With Conditional Statements

Some queries need to execute conditional logic when 
defining a query filter. The aggregation pipeline provides the
`$cond` operator to express conditional statements. By using
`$expr` with the `$cond` operator, you can
specify a conditional filter for your query statement.

Assume you want to calculate a weighted score for movies so that
highly-rated movies with few votes do not dominate the results:

- If `imdb.votes` is greater than or equal to 1000, the weighted
  score is the full `imdb.rating`.

- If `imdb.votes` is less than 1000, the weighted score is 0.5 of
  the `imdb.rating`.

You would like to know which movies in the `movies` collection have a
weighted score greater than `9`.

The following example uses `$expr` with `$cond` to
calculate the weighted score based on `imdb.votes` and 
`$gt` to return documents whose calculated weighted score
is greater than `9`:

```javascript
db.movies.find(
   {
      "imdb.rating": { $type: "number" },
      "imdb.votes": { $type: "number" },
      $expr: {
         $gt: [
            {
               $cond: {
                  if: { $gte: ["$imdb.votes", 1000] },
                  then: { $multiply: ["$imdb.rating", 1.0] },
                  else: { $multiply: ["$imdb.rating", 0.5] }
               }
            },
            9
         ]
      }
   },
   { _id: 0, title: 1, "imdb.rating": 1, "imdb.votes": 1 }
).sort( { title: 1 } ).limit(5)
```

The following table shows the weighted score for selected documents and
whether the weighted score is greater than `9` (i.e. whether the
document meets the query condition).

| Document | Weighted Score | > 9 |
|---|---|---|
| `{ title: "The Shawshank Redemption", imdb: { rating: 9.3, votes: 1521105 } }` | 9.3 | `true` |
| `{ title: "The Godfather", imdb: { rating: 9.2, votes: 1038358 } }` | 9.2 | `true` |
| `{ title: "Fight Club", imdb: { rating: 8.9, votes: 1191784 } }` | 8.9 | `false` |
| `{ title: "Planet Earth", imdb: { rating: 9.5, votes: 82896 } }` | 9.5 | `true` |
| `{ title: "Hollywood", imdb: { rating: 9.1, votes: 511 } }` | 4.55 | `false` |

The `db.collection.find()` operation returns 5 documents whose
calculated weighted score is greater than `9`:

```javascript
[
  { title: 'Band of Brothers', imdb: { rating: 9.6, votes: 183802 } },
  { title: 'Baseball', imdb: { rating: 9.1, votes: 2460 } },
  { title: 'Cosmos', imdb: { rating: 9.3, votes: 17174 } },
  { title: 'Frozen Planet', imdb: { rating: 9.2, votes: 5903 } },
  { title: 'Human Planet', imdb: { rating: 9.2, votes: 9057 } }
]
```

Even though `$cond` calculates a weighted score, that score
is not reflected in the returned documents. Instead, the returned
documents represent the matching documents in their original state.
