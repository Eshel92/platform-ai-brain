<!-- Converted from reference/method/cursor.max.txt (reStructuredText). Includes are inlined. -->

# cursor.max()

## Definition

**`cursor.max()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Specifies the *exclusive* upper bound for a specific index in order
to constrain the results of
`find()`. `max()` provides a
way to specify an upper bound on compound key indexes.

### Parameters

The `max()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `indexBounds` | document | The exclusive upper bound for the index keys. |

          
          
   

The `indexBounds` parameter has the following prototype form:

```javascript
{ field1: <max value>, field2: <max value2> ... fieldN:<max valueN> }
```

The fields correspond to *all* the keys of a particular index *in
order*. 

**Note:** Index Use

To use an index with the `max()` method, you must use the
`hint()` method to specify the index you want to use,
exept when the `find()` query is an equality
condition on the `_id` field.

**See also:**

`min()`

`max()` exists primarily to support the
`mongos` (sharding) process.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Interaction with Index Selection

Because `max()` requires an index on a field,
and forces the query to use this index, you may prefer the
`$lt` operator for the query if possible. Consider the
following example:

```javascript
db.products.find( { _id: { $in: [ 6, 7 ] } } ).max( { price: NumberDecimal("1.39") } ).hint( { price: 1 } )
```

The query will use the index on the `price` field, even if
the index on `_id` may be better.

### Index Bounds

If you use `max()` with `min()` to
specify a range:

- the index bounds specified in `min()` and
  `max()` must both refer to the keys of the same index.

- the bound specified by `max()` must be greater than
  the bound specified by `min()`.

### `max()` without `min()`

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

**Note:**

You must explicitly specify the particular index with the 
`hint()` method to run `max()` with the 
following exception: you do not need to hint if the 
`find()` query is an equality condition on the 
`_id` field `{ _id: <value> }`.

For the examples below, create a sample collection named `products` that holds the
following documents:

```javascript
db.products.insertMany([
   { "_id" : 1, "item" : "apple", "type" : "honey crisp", "price" : NumberDecimal("1.99") },
   { "_id" : 2, "item" : "apple", "type" : "fuji", "price" : NumberDecimal("1.99") },
   { "_id" : 3, "item" : "apple", "type" : "jonagold", "price" : NumberDecimal("1.29") },
   { "_id" : 4, "item" : "apple", "type" : "jonathan", "price" : NumberDecimal("1.29") },
   { "_id" : 5, "item" : "apple", "type" : "mcintosh", "price" : NumberDecimal("1.29") },
   { "_id" : 6, "item" : "apple", "type" : "cortland", "price" : NumberDecimal("1.29") },
   { "_id" : 7, "item" : "orange", "type" : "cara cara", "price" : NumberDecimal("2.99") },
   { "_id" : 9, "item" : "orange", "type" : "satsuma", "price" : NumberDecimal("1.99") },
   { "_id" : 8, "item" : "orange", "type" : "valencia", "price" : NumberDecimal("0.99") },
   { "_id" : 10, "item" : "orange", "type" : "navel", "price" : NumberDecimal("1.39") }
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

- Using the ordering of `{ item: 1, type: 1 }` index,
  `max()` limits the query to the documents
  that are below the bound of `item` equal to `apple` and
  `type` equal to `jonagold`:

  ```javascript
  db.products.find().max( { item: 'apple', type: 'jonagold' } ).hint( { item: 1, type: 1 } )
  ```

  The query returns the following documents:

  ```javascript
  { "_id" : 6, "item" : "apple", "type" : "cortland", "price" : NumberDecimal("1.29") }
  { "_id" : 2, "item" : "apple", "type" : "fuji", "price" : NumberDecimal("1.99") }
  { "_id" : 1, "item" : "apple", "type" : "honey crisp", "price" : NumberDecimal("1.99") }
  ```

- Using the ordering of the index `{ price: 1 }`, `max()` 
  limits the query to the documents that are below
  the index key bound of `price` equal to `NumberDecimal("1.99")` and
  `min()` limits the query to the documents
  that are at or above the index key bound of `price` equal to
  `NumberDecimal("1.39")`:

  **Note:**

  The bound specified by `max()` must be greater than 
  the bound specified by `min()`.

  ```javascript
  db.products.find().min( { price: NumberDecimal("1.39") } ).max( { price:  NumberDecimal("1.99") } ).hint( { price: 1 } )
  ```

  The query returns the following documents:

  ```javascript
  { "_id" : 10, "item" : "orange", "type" : "navel", "price" : NumberDecimal("1.39") }
  ```
