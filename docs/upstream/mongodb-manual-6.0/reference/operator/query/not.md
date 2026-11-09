<!-- Converted from reference/operator/query/not.txt (reStructuredText). Includes are inlined. -->

# $not

## Definition

**`$not`**

`$not` performs a logical `NOT` operation on the
specified `<operator-expression>` and selects the documents that
do *not* match the `<operator-expression>`. This includes
documents that do not contain the `field`.

## Compatibility

You can use `$not` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$not` operator has the following form:

```javascript
{ field: { $not: { <operator-expression> } } }
```

Consider the following example:

```javascript
db.inventory.find( { price: { $not: { $gt: 1.99 } } } )
```

This query will select all documents in the `inventory` collection where:

- the `price` field value is less than or equal to `1.99` **or**
- the `price` field does not exist

`{ $not: { $gt: 1.99 } }` is different from the `$lte`
operator. `{ $lte: 1.99 }` returns *only* the documents where
`price` field exists and its value is less than or equal to
`1.99`.

You must use the `$not` operator with another operator expression. For
example, to use `$not` to perform an inequality check, use this
syntax:

```javascript
{ price: { $not: { $eq: 1.99 } } }
```

   
The preceding query is equivalent to:

```javascript
{ price: { $ne: 1.99 } }
```

   
The following `$not` query is **invalid** because it attempts to
compare a field without an operator:

```javascript
{ price: { $not: 1.99 } }
```

## Behavior

### Arrays

When passed an array argument, the `$not` operator may yield
unexpected results. To match documents based on multiple false
conditions, use `$nor`.

### Regular Expressions

`$not` operator can perform logical `NOT` operation on:

- Regular expression objects (i.e. `/pattern/`)

  For example, the following query selects all documents in the
  `inventory` collection where the `item` field value does *not*
  start with the letter `p`.

  ```javascript
  db.inventory.find( { item: { $not: /^p.*/ } } )
  ```

- `$regex` operator expression 

  For example, the following query selects all documents in the
  `inventory` collection where the `item` field value does *not*
  start with the letter `p`.

  ```javascript
  db.inventory.find( { item: { $not: { $regex: "^p.*" } } } )
  db.inventory.find( { item: { $not: { $regex: /^p.*/ } } } )
  ```

- driver language's regular expression objects

  For example, the following [PyMongo](https://pymongo.readthedocs.io/en/stable/index.html) query uses
  Python's `re.compile()` method to compile a regular expression:

  ```python
  import re
  for noMatch in db.inventory.find( { "item": { "$not": re.compile("^p.*") } } ):
      print noMatch
  ```

**See also:**

- `find()`
- `$set`
- `$gt`
- `$regex`
