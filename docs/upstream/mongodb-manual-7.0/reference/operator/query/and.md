<!-- Converted from reference/operator/query/and.txt (reStructuredText). Includes are inlined. -->

# $and (query predicate operator)

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

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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

When evaluating the clauses in the `$and` expression, MongoDB's
query optimizer considers which indexes are available that could
help satisfy clauses of the `$and` expression when
selecting the best plan to execute.
 
To allow the query engine to optimize queries, `$and` handles
errors as follows:

- If any expression supplied to `$and` would cause an error when
  evaluated alone, the `$and` containing the expression may cause an
  error but an error is not guaranteed.

- An expression supplied after the first expression supplied to `$and`
  may cause an error even if the first expression evaluates to
  `false`.

Most programming languages and drivers, including the
MongoDB Shell (`mongosh`),
do not allow the construction of objects with duplicate keys at the
same object level. For example:

```javascript
db.inventory.find( { price: { $in: [ 7.99, 3.99 ], $in: [ 4.99, 1.99 ] } } )
```

The previous query is invalid because the field name `price` has
duplicate operators at the same object level. The query sent to the
server differs from the intent. To make the query work, use an explicit
`AND`:

```javascript
db.inventory.find( {
   $and: [
      { price: { $in: [ 7.99, 3.99 ] } },
      { price: { $in: [ 4.99, 1.99 ] } }
   ]
} )
```

The previous query explicitly checks that both conditions are satisfied:
the `price` array must include at least one value from each
`$in` set. For more information, see query-and-examples.

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
