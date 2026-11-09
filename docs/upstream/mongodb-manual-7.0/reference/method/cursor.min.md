<!-- Converted from reference/method/cursor.min.txt (reStructuredText). Includes are inlined. -->

# cursor.min() (mongosh method)

## Definition

**`cursor.min()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Specifies the *inclusive* lower bound for a specific index in order
to constrain the results of
`find()`. `min()` provides a
way to specify lower bounds on compound key indexes.

The `min()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `indexBounds` | document | The inclusive lower bound for the index keys. |

The `indexBounds` parameter has the following prototype form:

```javascript
{ field1: <min value>, field2: <min value2>, fieldN:<min valueN> }
```

**Note:** Index Use

To use an index with the `max()` method, you must use the
`hint()` method to specify the index you want to use,
except when the `find()` query is an equality
condition on the `_id` field.

**See also:**

`max()`

`min()` exists primarily to support the
`mongos` process.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behaviors

### Interaction with Index Selection

Because `min()` requires an index on a
field, and forces the query to use this index, you may prefer
the `$gte` operator for the query if
possible. Consider the following example:

```javascript
db.products.find( { _id: { $in: [ 6, 7 ] } } ).min( { price: Decimal128("1.39") } ).hint( { price: 1 } )
```

The query will use the index on the `price` field, even if
the index on `_id` may be better.

### Index Bounds

If you use `min()` with `max()` to
specify a range:

- the index bounds specified in `min()` and
  `max()` must both refer to the keys of the same index.

- the bound specified by `max()` must be greater than
  the bound specified by `min()`.

### `min()` without `max()`

The `min()` and `max()` methods
indicate that the system should avoid normal query planning. They
construct an index scan where the index bounds are explicitly specified
by the values given in `min()` and
`max()`.

**Warning:**

If one of the two boundaries is not specified, the query plan will be
an index scan that is unbounded on one side. This may degrade performance
compared to a query containing neither operator, or one that uses both
operators to more tightly constrain the index scan.

## Example

Unless the `find()` query is an equality condition on 
the `_id` field `{ _id: <value> }`, you must explicitly specify the 
index with the `hint()` method to run `min()`.
   
For the examples below, create a sample collection named `products` that holds the
following documents:

```javascript
db.products.insertMany([
   { "_id" : 1, "item" : "apple", "type" : "honey crisp", "price" : Decimal128("1.99") },
   { "_id" : 2, "item" : "apple", "type" : "fuji", "price" : Decimal128("1.99") },
   { "_id" : 3, "item" : "apple", "type" : "jonagold", "price" : Decimal128("1.29") },
   { "_id" : 4, "item" : "apple", "type" : "jonathan", "price" : Decimal128("1.29") },
   { "_id" : 5, "item" : "apple", "type" : "mcintosh", "price" : Decimal128("1.29") },
   { "_id" : 6, "item" : "apple", "type" : "cortland", "price" : Decimal128("1.29") },
   { "_id" : 7, "item" : "orange", "type" : "cara cara", "price" : Decimal128("2.99") },
   { "_id" : 9, "item" : "orange", "type" : "satsuma", "price" : Decimal128("1.99") },
   { "_id" : 8, "item" : "orange", "type" : "valencia", "price" : Decimal128("0.99") },
   { "_id" : 10, "item" : "orange", "type" : "navel", "price" : Decimal128("1.39") }
])
```

Create the following indexes for the collection:

```javascript
db.products.createIndexes( [
   { "item" : 1, "type" : 1 },
   { "item" : 1, "type" : -1 },
   { "price" : 1 } 
] )
```

- Using the ordering of the `{ item: 1, type: 1 }` index,
  `min()` limits the query to the documents
  that are at or above the index key bound of `item` equal to
  `apple` and `type` equal to `jonagold`, as in the following:

  ```javascript
  db.products.find().min( { item: 'apple', type: 'jonagold' } ).hint( { item: 1, type: 1 } )
  ```

  The query returns the following documents:

  ```javascript
  { "_id" : 3, "item" : "apple", "type" : "jonagold", "price" : Decimal128("1.29") }
  { "_id" : 4, "item" : "apple", "type" : "jonathan", "price" : Decimal128("1.29") }
  { "_id" : 5, "item" : "apple", "type" : "mcintosh", "price" : Decimal128("1.29") }
  { "_id" : 7, "item" : "orange", "type" : "cara cara", "price" : Decimal128("2.99") }
  { "_id" : 10, "item" : "orange", "type" : "navel", "price" : Decimal128("1.39") }
  { "_id" : 9, "item" : "orange", "type" : "satsuma", "price" : Decimal128("1.99") }
  { "_id" : 8, "item" : "orange", "type" : "valencia", "price" : Decimal128("0.99") }
  ```

- Using the ordering of the index `{ price: 1 }`, `min()` limits the query to the documents that are at or
  above the index key bound of `price` equal to `1.39` and
  `max()` limits the query to the documents
  that are below the index key bound of `price` equal to `1.99`:

  **Note:**

  The bound specified by `max()` must be greater than the 
  bound specified by `min()`.

  ```javascript
  db.products.find().min( { price: Decimal128("1.39") } ).max( { price:  Decimal128("1.99") } ).hint( { price: 1 } )
  ```

  The query returns the following documents:

  ```javascript
  { "_id" : 10, "item" : "orange", "type" : "navel", "price" : Decimal128("1.39") }
  ```
