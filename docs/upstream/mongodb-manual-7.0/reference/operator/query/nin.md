<!-- Converted from reference/operator/query/nin.txt (reStructuredText). Includes are inlined. -->

# $nin (query predicate operator)

**`$nin`**

`$nin` selects documents where:

- the specified field value is not in the specified array **or**
- the specified field does not exist.

## Compatibility

You can use `$nin` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$nin` operator has the following form:

```javascript
{ field: { $nin: [ <value1>, <value2> ... <valueN> ] } }
```

## Behavior

### Type Bracketing

Unlike the inequality operators (`$gt`, `$gte`,
`$lt`, and `$lte`), `$nin` doesn't use type bracketing.
Instead, it matches documents where the field value is not one of the
specified values, regardless of the value's type.

For example, `{ a: { $nin: [ 2, 4 ] } }` also matches documents where
`a` is a string.

### Match an Array Value

If `field` has an array, the `$nin` operator selects
the documents whose `field` has an array with **no** element equal to
a value in the specified array. For example, `<value1>`,
`<value2>`, and so on.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Select on Unmatching Documents

The following example returns movies where `runtime` is greater
than `1000` minutes and `rated` is not in `[ "G", "PG" ]`.
Because `$nin` also matches documents that don't contain the
`rated` field, the query returns movies even when the rating data
is unavailable:

```javascript
```

Output:

```javascript
```

### Select on Elements Not in an Array

The following example sets the `exclude` field to `true` for
movies that don't have `"Drama"` in their `genres` array:

```javascript
```

Output:

```javascript
```

`updateMany()` also selects a document when the
document does not contain the field `$nin` is matching on.

The inequality operator `$nin` is *not* very selective since
it often matches a large portion of the index. As a result, in many
cases, a `$nin` query with an index may perform no better
than a `$nin` query that must scan all documents in a
collection. See also read-operations-query-selectivity.

## Learn More

- `find()`
- `updateMany()`
- `$set`
