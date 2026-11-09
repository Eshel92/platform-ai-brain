<!-- Converted from reference/operator/query/or.txt (reStructuredText). Includes are inlined. -->

# $or (query predicate operator)

   

**`$or`**

The `$or` operator performs a logical `OR` operation on an
array of *one or more* `<expressions>` and selects the documents
that satisfy *at least* one of the `<expressions>`. 
   

## Compatibility

You can use `$or` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$or` operator has the following syntax:

```javascript
{ $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
```

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

Consider the following example:

```javascript
```

Output:

```javascript
```

This query selects all documents in the `movies` collection
that meet either of the following conditions:

- The `runtime` field value is greater than `1000`.
- The `year` field value is earlier than `1910`.

## Behaviors

### `$or` Clauses and Indexes

When evaluating the clauses in the `$or` expression, MongoDB
either performs a collection scan or, if all the clauses are supported
by indexes, MongoDB performs index scans. That is, for MongoDB to use
indexes to evaluate an `$or` expression, all the clauses in the
`$or` expression must be supported by indexes. Otherwise,
MongoDB will perform a collection scan.

When using indexes with `$or` queries, each clause of an
`$or` can use its own index.  Consider the following query:

```javascript
db.movies.find(
   { $or: [ { runtime: { $gt: 1000 } }, { year: { $lt: 1910 } } ] }
)
```

To support this query, create one index on `runtime` and
another index on `year`, rather than a compound index:

```javascript
db.movies.createIndex( { runtime: 1 } ),
db.movies.createIndex( { year: 1 } ),
```

### `$or` and `text` Queries

If `$or` includes a `$text` query, all clauses in the
`$or` array must be supported by an index. This is because a
`$text` query *must* use an index, and `$or` can only use
indexes if all its clauses are supported by indexes. If the
`$text` query cannot use an index, the query will return an
error.

**Note:**

`$text` provides text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search.

### `$or` and Geospatial Queries

`$or` supports geospatial clauses.
However, if you use a near clause (`$near` or
`$nearSphere`), `$or` cannot contain any other clauses. Using
`$or` with a single clause has the same effect as omitting the `$or`
operator.

The following query is valid because `$or` uses a non-near
geospatial clause (`$geoIntersects`):

```javascript
```

Output:

```javascript
```

### `$or` and Sort Operations

When executing `$or` queries with a `sort()`,
MongoDB can use indexes that support the `$or` clauses.

### `$or` and Partial Indexes

You can create partial indexes with `$or`. 
Use the `partialFilterExpression` of the db.collection.createIndex()
method to create a partial index. 

### `$or` versus `$in`

When using `$or` with `<expressions>` that are equality checks
for the value of the same field, use the `$in` operator instead
of the `$or` operator.

This query selects documents in the `movies` collection where
`year` is `1903` or `1909`:

```javascript
```

Output:

```javascript
```

### Nested `$or` Clauses

You may nest `$or` operations.

**See also:**

- `$and`
- `find()`
- `sort()`
- `$in`

### Error Handling

To allow the query engine to optimize queries, `$or` handles
errors as follows:

- If any expression supplied to `$or` would cause an error when
  evaluated alone, the `$or` containing the expression may cause an
  error but an error is not guaranteed.

- An expression supplied after the first expression supplied to `$or`
  may cause an error even if the first expression evaluates to
  `true`.
