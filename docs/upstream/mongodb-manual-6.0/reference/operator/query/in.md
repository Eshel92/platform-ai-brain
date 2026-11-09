<!-- Converted from reference/operator/query/in.txt (reStructuredText). Includes are inlined. -->

# $in

**`$in`**

The `$in` operator selects the documents where the value
of a field equals any value in the specified array.

## Compatibility

You can use `$in` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

To specify an `$in` expression, use the following prototype:

```javascript
{ field: { $in: [<value1>, <value2>, ... <valueN> ] } }
```

For comparison of different BSON type values, see the specified
BSON comparison order.

If the `field` holds an array, then the `$in` operator
selects the documents whose `field` holds an array that contains
at least one element that matches a value in the specified array
(for example, `<value1>`, `<value2>`, and so on).

The `$in` operator compares each parameter to each document
in the collection, which can lead to performance issues.
To improve performance:

* It is recommended that you limit the number of parameters passed to the
   `$in` operator to tens of values.  Using hundreds of parameters
   or more can negatively impact query performance.

* Create an index on the `field` you want to query.

**Note:**

This document describes the `$in` query operator.
For the `$in` aggregation operator, see
/reference/operator/aggregation/in.

## Query Data on Atlas by Using Atlas Search

For data stored in MongoDB Atlas, you can use the 
Atlas Search in-ref 
operator when running `$search` queries. Running 
`$in` after `$search` is less performant 
than running `$search` with the in-ref
operator.

To learn more about the Atlas Search version of this operator, 
see the in-ref operator in the Atlas documentation.

## Examples

Create the `inventory` collection:

```javascript
db.inventory.insertMany( [
   { item: "Pens", quantity: 350, tags: [ "school", "office" ] },
   { item: "Erasers", quantity: 15, tags: [ "school", "home" ] },
   { item: "Maps", tags: [ "office", "storage" ] },
   { item: "Books", quantity: 5, tags: [ "school", "storage", "home" ] }
] )
```

### Use the `$in` Operator to Match Values

Consider the following example:

```javascript
db.inventory.find( { quantity: { $in: [ 5, 15 ] } }, { _id: 0 } )
```

This query selects all documents in the `inventory` collection where
the value of the `quantity` field is either 5 or 15. 

```javascript
{ item: 'Erasers', quantity: 15, tags: [ 'school', 'home' ] },
{ item: 'Books', quantity: 5, tags: [ 'school', 'storage', 'home' ] }
```

Although you can write this query using the `$or` operator,
use the `$in` operator rather than the `$or` operator
when performing equality checks on the same field.

### Use the `$in` Operator to Match Values in an Array

The following `updateMany()` operation sets the
`exclude` field to `false` when the `tags` array has at least one
element that matches either `"home"` or `"school"`.

```javascript
db.inventory.updateMany(
   { tags: { $in: [ "home", "school" ] } },
   { $set: { exclude: false } }
)
```

Example output:

```javascript
{
   item: 'Pens',
   quantity: 350,
   tags: [ 'school', 'office' ],
   exclude: false
 },
 {
   item: 'Erasers',
   quantity: 15,
   tags: [ 'school', 'home' ],
   exclude: false
 },
 {
   item: 'Books',
   quantity: 5,
   tags: [ 'school', 'storage', 'home' ],
   exclude: false
 }
```

For additional examples on querying arrays, see:

- read-operations-arrays
- array-match-embedded-documents

For additional examples on querying, see 
read-operations-query-document.

### Use the `$in` Operator with a Regular Expression

The `$in` operator can specify matching values using regular
expressions of the form `/pattern/`. You *cannot* use `$regex`
operator expressions inside an `$in`.

Consider the following example:

```javascript
db.inventory.find( { tags: { $in: [ /^be/, /^st/ ] } } )
```

This query selects all documents in the `inventory` collection where
the `tags` field holds either a string that starts with `be` or
`st` or an array with at least one element that starts with `be` or
`st`.

**See also:**

- `find()`
- `updateMany()`
- `$or`
- `$set`
- `$elemMatch`
