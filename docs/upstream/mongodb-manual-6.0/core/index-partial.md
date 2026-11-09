<!-- Converted from core/index-partial.txt (reStructuredText). Includes are inlined. -->

# Partial Indexes

Partial indexes only index the documents in a collection that meet a
specified filter expression. By indexing a subset of the documents in a
collection, partial indexes have lower storage requirements and reduced
performance costs for index creation and maintenance.

## Create a Partial Index

To create a `partial` index, use the
`db.collection.createIndex()` method with the
`partialFilterExpression` option. The `partialFilterExpression`
option accepts a document that specifies the filter condition using:

- equality expressions (i.e. `field: value` or using the `$eq`
  operator),

- `$exists: true` expression,

- `$gt`, `$gte`, `$lt`, `$lte` expressions,

- `$type` expressions,

- `$and` operator,

- `$or` operator, 

- `$in` operator 

For example, the following operation creates a compound index that
indexes only the documents with a `rating` field greater than 5.

```javascript
db.restaurants.createIndex(
   { cuisine: 1, name: 1 },
   { partialFilterExpression: { rating: { $gt: 5 } } }
)
```

You can specify a `partialFilterExpression` option for all MongoDB
index types.

**See also:**

To learn how to manage indexes in MongoDB Compass, see manage-indexes.

   

## Behavior

### Query Coverage

MongoDB will not use the partial index for a query or sort operation if
using the index results in an incomplete result set.

To use the partial index, a query must contain the filter expression
(or a modified filter expression that specifies a subset of the filter
expression) as part of its query condition.

For example, given the following index:

```javascript
db.restaurants.createIndex(
   { cuisine: 1 },
   { partialFilterExpression: { rating: { $gt: 5 } } }
)
```

The following query can use the index since the query predicate
includes the condition `rating: { $gte: 8 }` that matches a subset of
documents matched by the index filter expression ``rating: { $gt: 5
}``:

```javascript
db.restaurants.find( { cuisine: "Italian", rating: { $gte: 8 } } )
```

However, the following query cannot use the partial index on the
`cuisine` field because using the index results in an incomplete
result set. Specifically, the query predicate includes the condition
`rating: { $lt: 8 }` while the index has the filter ``rating: { $gt:
5 }`. That is, the query `{ cuisine: "Italian", rating: { $lt: 8 }
}`` matches more documents (e.g. an Italian restaurant with a rating
equal to 1) than are indexed.

```javascript
db.restaurants.find( { cuisine: "Italian", rating: { $lt: 8 } } )
```

Similarly, the following query cannot use the partial index because the
query predicate does not include the filter expression and using the
index would return an incomplete result set.

```javascript
db.restaurants.find( { cuisine: "Italian" } )
```

### Comparison with Sparse Indexes

Use partial indexes over sparse indexes if you want
more precise control over which documents to index:

- Sparse indexes include or exclude documents *solely* based on the presence of
  the indexed field (or multiple fields, for sparse compound indexes).

- Partial indexes include or exclude documents based on the filter expression. 
  The expression can include fields other than index keys, and
  can specify conditions other than a field existing. 

For example, a partial index can implement the same behavior as a sparse index.
This partial index supports the same queries as a sparse index on the
`name` field:

```javascript
db.contacts.createIndex(
   { name: 1 },
   { partialFilterExpression: { name: { $exists: true } } }
)
```

However, a partial index can also filter on fields other than the index key.
For example, a partial index on the `name` field can check for the existence
of the `email` field:

```javascript
db.contacts.createIndex(
   { name: 1 },
   { partialFilterExpression: { email: { $exists: true } } }
)
```

For the query optimizer to choose this partial index, the query
predicate must include a condition on the `name` field as well
as a *non-null* match on the `email` field.

For example, the following query can use the index because it includes
both a condition on the `name` field and a non-null match on the
`email` field:

```javascript
db.contacts.find( { name: "xyz", email: { $regex: /\.org$/ } } )
```

However, the following query cannot use the index because it
includes a null match on the `email` field, which is not permitted
by the filter expression
`{ email: { $exists: true } }`:

```javascript
db.contacts.find( { name: "xyz", email: { $exists: false } } )
```

### Partial TTL Indexes

Partial indexes can also be TTL indexes. Partial TTL indexes match the 
specified filter expression and expire only those documents. For details, see
partial-ttl-index-example. 

## Restrictions

- You cannot specify both the `partialFilterExpression` option and
  the `sparse` option.

- `_id` indexes cannot be partial indexes.

- Shard key indexes cannot be partial indexes.

- .. include:: /includes/queryable-encryption/qe-csfle-partial-filter-disclaimer.rst

## Examples

### Create a Partial Index On A Collection

Consider a collection `restaurants` containing documents that resemble
the following

```javascript
{
   "_id" : ObjectId("5641f6a7522545bc535b5dc9"),
   "address" : {
      "building" : "1007",
      "coord" : [
         -73.856077,
         40.848447
      ],
      "street" : "Morris Park Ave",
      "zipcode" : "10462"
   },
   "borough" : "Bronx",
   "cuisine" : "Bakery",
   "rating" : { "date" : ISODate("2014-03-03T00:00:00Z"),
                "grade" : "A",
                "score" : 2
              },
   "name" : "Morris Park Bake Shop",
   "restaurant_id" : "30075445"
}
```

You could add a partial index on the `borough` and `cuisine` fields
choosing only to index documents where the `rating.grade`
field is `A`:

```javascript
db.restaurants.createIndex(
   { borough: 1, cuisine: 1 },
   { partialFilterExpression: { 'rating.grade': { $eq: "A" } } }
)
```

Then, the following query on the `restaurants` collection uses the partial index
to return the restaurants in the Bronx with `rating.grade` equal to `A`:

```javascript
db.restaurants.find( { borough: "Bronx", 'rating.grade': "A" } )
```

However, the following query cannot use the partial index because the
query expression does not include the `rating.grade` field:

```javascript
db.restaurants.find( { borough: "Bronx", cuisine: "Bakery" } )
```

### Partial Index with Unique Constraint

Partial indexes only index the documents in a collection that meet a
specified filter expression. If you specify both the
`partialFilterExpression` and a unique constraint, the unique constraint only applies to the
documents that meet the filter expression. A partial index with a
unique constraint does not prevent the insertion of documents that do
not meet the unique constraint if the documents do not meet the filter
criteria.

For example, a collection `users` contains the following documents:

```javascript
{ "_id" : ObjectId("56424f1efa0358a27fa1f99a"), "username" : "david", "age" : 29 }
{ "_id" : ObjectId("56424f37fa0358a27fa1f99b"), "username" : "amanda", "age" : 35 }
{ "_id" : ObjectId("56424fe2fa0358a27fa1f99c"), "username" : "rajiv", "age" : 57 }
```

The following operation creates an index that specifies a unique
constraint on the `username` field and a partial
filter expression `age: { $gte: 21 }`.

```javascript
db.users.createIndex(
   { username: 1 },
   { unique: true, partialFilterExpression: { age: { $gte: 21 } } }
)
```

The index prevents the insertion of the following documents since
documents already exist with the specified usernames and the `age`
fields are greater than `21`:

```javascript
db.users.insertMany( [
   { username: "david", age: 27 },
   { username: "amanda", age: 25 },
   { username: "rajiv", age: 32 }
] )
```

However, the following documents with duplicate usernames are allowed
since the unique constraint only applies to documents with `age`
greater than or equal to 21.

```javascript
db.users.insertMany( [
   { username: "david", age: 20 },
   { username: "amanda" },
   { username: "rajiv", age: null }
] )
```
