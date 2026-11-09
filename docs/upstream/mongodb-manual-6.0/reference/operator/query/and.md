<!-- Converted from reference/operator/query/and.txt (reStructuredText). Includes are inlined. -->

# $and

**`$and`**

`$and` performs a logical `AND` operation on an array of
*one or more* expressions (`<expression1>`, `<expression2>`, and
so on) and selects the documents that satisfy *all* the expressions.

**Note:**

MongoDB provides an implicit `AND` operation when specifying a
comma separated list of expressions.

## Compatibility

You can use `$and` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$and` has the following syntax:

```javascript
{ $and: [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] }
```

## Behavior

To allow the query engine to optimize queries, `$and` handles
errors as follows:

- If any expression supplied to `$and` would cause an error when
  evaluated alone, the `$and` containing the expression may cause an
  error but an error is not guaranteed.

- An expression supplied after the first expression supplied to `$and`
  may cause an error even if the first expression evaluates to
  `false`.

For example, the following query *always* produces an error if `$x` is
`0`:

```javascript
db.example.find( {
   $expr: { $eq: [ { $divide: [ 1, "$x" ] }, 3 ] }
} )
```

The following query, which contains multiple expressions supplied to
`$and`, *may* produce an error if there is any document where `$x`
is `0`:

```javascript
db.example.find( {
   $and: [
      { x: { $ne: 0 } },
      { $expr: { $eq: [ { $divide: [ 1, "$x" ] }, 3 ] } }
   ]
} )
```

## Examples

### `AND` Queries With Multiple Expressions Specifying the Same Field

Consider this query:

```javascript
db.inventory.find( { $and: [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } )
```

The query selects all documents in the `inventory` collection where:

- the `price` field value is not equal to `1.99` **and**
- the `price` field exists.

The query can be rewritten with an implicit `AND` operation that
combines the operator expressions for the `price` field:

```javascript
db.inventory.find( { price: { $ne: 1.99, $exists: true } } )
```

### `AND` Queries With Multiple Expressions Specifying the Same Operator

Consider this query:

```javascript
db.inventory.find( {
    $and: [
        { $or: [ { qty: { $lt : 10 } }, { qty : { $gt: 50 } } ] },
        { $or: [ { sale: true }, { price : { $lt : 5 } } ] }
    ]
} )
```

The query selects all documents where:

- the `qty` field value is less than `10` or greater than `50`, **and**
- the `sale` field value is equal to `true` **or** the `price`
  field value is less than `5`.

The query cannot use an implicit `AND` operation because it uses the
`$or` operator more than once.

**See also:**

- `find()`
- `updateMany()`
- `$ne`
- `$exists`
- `$set`
