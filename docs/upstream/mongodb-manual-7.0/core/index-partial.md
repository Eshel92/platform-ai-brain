<!-- Converted from core/index-partial.txt (reStructuredText). Includes are inlined. -->

# Partial Indexes

Partial indexes only index the documents in a collection that meet a
specified filter expression. Partial indexes have lower storage
requirements and reduced performance costs for index creation and
maintenance.

## Create a Partial Index

To create a `partial` index, use the
`db.collection.createIndex()` method with the
`partialFilterExpression` option. The `partialFilterExpression`
option accepts a document that specifies the filter condition using:

- equality expressions (i.e. `field: value` or using the `$eq`
  operator)

- `$exists: true` expression

- `$gt`, `$gte`, `$lt`, `$lte` expressions

- `$type` expressions

- `$and` operator

- `$or` operator

- `$in` operator

- `$geoWithin` operator

- `$geoIntersects` operator

For example, the following operation creates a compound index that
indexes only the documents where the `genre` field is `Drama`:

```javascript
db.movies.createIndex(
   { title: 1 },
   { partialFilterExpression: { genres: "Drama" } }
)
```

You can specify a `partialFilterExpression` option for all MongoDB
index types. When specifying a
`partialFilterExpression` for a TTL index on a time series collection,
you can only filter on the collection `metaField`.

**See also:**

To learn how to manage indexes in MongoDB Compass, see
manage-indexes.

   

## Behavior

### Query Coverage

MongoDB does not use the partial index for a query or sort operation if
using the index results in an incomplete result set.

To use the partial index, a query must contain the filter expression
(or a modified filter expression that specifies a subset of the filter
expression) as part of its query condition.

For example, given the following index:

```javascript
db.users.createIndex(
   { name: 1 },
   { partialFilterExpression: { password: { $exists: true } } }
)
```

The following query can use the index since the query predicate
includes the condition `password: { $exists: true }` that matches
documents matched by the index filter expression ``password: { $exists: true
}``:

```javascript
db.users.find( { name: "Ned Stark", password: { $exists: true } } )
```

However, the following query cannot use the partial index on the
`name` field because using the index results in an incomplete
result set. Specifically, the query predicate includes the condition
`password: { $exists: false }` while the index has the filter ``password: { $exists:
true }`. That is, the query `{ name: "Ned Stark", password: { $exists: false }
}`` matches documents that the partial index doesn't include (users
without passwords).

```javascript
db.users.find( { name: "Ned Stark", password: { $exists: false } } )
```

Similarly, the following query cannot use the partial index because the
query predicate does not include the filter expression and using the
index would return an incomplete result set.

```javascript
db.users.find( { name: "Ned Stark" } )
```

### Comparison Operators

For an index that uses a comparison operator such as `$gt`, a query
condition satisfies the filter expression if it specifies an equal or
narrower range of values.

For example, given an index with the filter expression
`{ year: { $gt: 2000 } }`:

```javascript
db.movies.createIndex(
   { year: 1 },
   { name: "year_gt_2000_partial", partialFilterExpression: { year: { $gt: 2000 } } }
)
```

The following query can use the index because the condition
`year: 2005` satisfies a subset of the documents matched by the
filter expression:

```javascript
db.movies.find( { year: 2005 } ).explain("executionStats")
```

Similarly, the following query can use the index because the
condition `year: { $gt: 2010 }` matches a narrower range of
documents than the filter expression:

```javascript
db.movies.find( { year: { $gt: 2010 } } ).explain("executionStats")
```

However, the following query cannot use the index because the
condition `year: { $gt: 1990 }` matches documents that the
partial index doesn't include:

```javascript
db.movies.find( { year: { $gt: 1990 } } ).explain("executionStats")
```

**Note:**

Subset matching does not behave identically for every operator
supported in a `partialFilterExpression`. Before relying on a
partial index for a query pattern not shown here, use
explain() to confirm MongoDB
selects the index you expect.

### Comparison with Sparse Indexes

Use partial indexes instead of sparse indexes
for more precise control over which documents to index:

- Sparse indexes include or exclude documents *solely* based on the presence of
  the indexed field (or multiple fields, for sparse compound indexes).

- Partial indexes include or exclude documents based on the filter expression. 
  The expression can include fields other than index keys, and
  can specify conditions other than a field existing. 

For example, a partial index can implement the same behavior as a sparse index.
This partial index supports the same queries as a sparse index on the
`name` field:

```javascript
db.users.createIndex(
   { name: 1 },
   { partialFilterExpression: { name: { $exists: true } } }
)
```

However, a partial index can also filter on fields other than the index key.
For example, a partial index on the `name` field can check for the existence
of the `email` field:

```javascript
db.users.createIndex(
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
db.users.find( { name: "Ned Stark", email: { $regex: /gameofthron\.es$/ } } )
```

However, the following query cannot use the index because it
includes a null match on the `email` field, which is not permitted
by the filter expression
`{ email: { $exists: true } }`:

```javascript
db.users.find( { name: "Ned Stark", email: { $exists: false } } )
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

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Create a Partial Index On A Collection

The following example adds a partial index on the `title` and `genres` fields.
The operation only indexes documents where the `rating`
field is `PG`:

```javascript
db.movies.createIndex(
   { title: 1, genres: 1 },
   { partialFilterExpression: { rated: "PG" } }
)
```

The following query on the `movies` collection uses the partial index to return
the writers of the all movies titled "The Three Musketeers":

```javascript
db.movies.find( { title: "The Three Musketeers", genres: ["Action", "Adventure", "Comedy"], rated: "PG" }, { writers: 1 } )
```

However, the following query cannot use the partial index because the
query predicate does not include the `rating` filter:

```javascript
db.movies.find( { genres: "Drama" }, { title: 1 } ).limit(5)
```

### Partial Index with Unique Constraint

Partial indexes only index the documents in a collection that meet a
specified filter expression. If you specify both the
`partialFilterExpression` and a unique constraint, the unique constraint only applies to the
documents that meet the filter expression. A partial index with a
unique constraint does not prevent the insertion of documents that do
not meet the unique constraint if the documents do not meet the filter
criteria.

The following operation on the `users` collection creates an index that
specifies a unique constraint on the `email` field
and a partial filter expression `password: { $exists: true }`.

```javascript
db.users.createIndex(
   { email: 1 },
   { unique: true, partialFilterExpression: { password: { $exists: true } } }
)
```

The index prevents the insertion of documents that have both an email
address that already exists in the collection and an existing
`password` field.

However, you can still insert documents with duplicate `email`
addresses if the documents do not include a `password` field. The
unique constraint only applies to documents that the index includes. The
following example inserts two documents with the same email address:

```javascript
db.users.insertMany( [
   // This document has a password field, so the index includes it and
   // the unique constraint applies to its email address
   { name: "Jon Snow", email: "jon@example.com", password: "example123" },

   // This document does not have a password field, so the index does not
   // include it. You can insert it even though it has the same email
   // address as the first document
   { name: "Jon Snow", email: "jon@example.com" }
] )
```
