<!-- Converted from reference/operator/query/or.txt (reStructuredText). Includes are inlined. -->

# $or

   

**`$or`**

The `$or` operator performs a logical `OR` operation on an
array of *one or more* `<expressions>` and selects the documents
that satisfy *at least* one of the `<expressions>`. 
   

## Compatibility

You can use `$or` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

Consider the following example:

```javascript
db.inventory.find( { $or: [ { quantity: { $lt: 20 } }, { price: 10 } ] } )
```

This query will select all documents in the `inventory` collection
where either the `quantity` field value is less than `20` **or** the
`price` field value equals `10`.

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
db.inventory.find( { $or: [ { quantity: { $lt: 20 } }, { price: 10 } ] } )
```

To support this query, rather than a compound index, you would create
one index on `quantity` and another index on `price`:

```javascript
db.inventory.createIndex( { quantity: 1 } )
db.inventory.createIndex( { price: 1 } )
```

MongoDB can use all but the geoHaystack
index to support `$or` clauses.

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

### `$or` and GeoSpatial Queries

`$or` supports geospatial clauses with the following exception
for the near clause (near clause includes `$nearSphere` and
`$near`). `$or` cannot contain a near clause with any
other clause.

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

For example, to select all documents in the `inventory` collection
where the `quantity` field value equals either `20` *or* `50`, use the
`$in` operator:

```javascript
db.inventory.find ( { quantity: { $in: [20, 50] } } )
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

For example, the following query *always* produces an error if `$x` is
`0`:

```javascript
db.example.find( {
   $expr: { $eq: [ { $divide: [ 1, "$x" ] }, 3 ] }
} )
```

The following query, which contains multiple expressions supplied to
`$or`, *may* produce an error if there is any document where `$x`
is `0`:

```javascript
db.example.find( {
   $or: [
      { x: { $eq: 0 } },
      { $expr: { $eq: [ { $divide: [ 1, "$x" ] }, 3 ] } }
   ]
} )
```
