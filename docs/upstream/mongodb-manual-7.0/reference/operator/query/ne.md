<!-- Converted from reference/operator/query/ne.txt (reStructuredText). Includes are inlined. -->

# $ne (query predicate operator)

## Definition

**`$ne`**

`$ne` selects documents where the value of the field is not equal
to the specified value. This includes documents that do not contain
the field.

## Compatibility

You can use `$ne` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$ne` operator has the following form:

```javascript
{ field: { $ne: value } }
```

**Note:**

If the value of `$ne` is null, see non-equality-filter.

## Behavior

### Type Bracketing

Unlike the inequality operators (`$gt`, `$gte`,
`$lt`, and `$lte`), `$ne` doesn't use type bracketing.
Instead, it matches documents where the field value is not equal to the
specified value, regardless of the value's type.

For example, `{ a: { $ne: 2 } }` also matches documents where `a` is
a string.

### Array Comparison

When comparing arrays, `$ne` behaves differently depending on
whether you pass a scalar or an array as the comparison value.

- **Scalar comparison**: `$ne` matches documents where the
  scalar value is not present as an element in the array,
  including documents that don't have the field.
- **Exact array comparison**: `$ne` matches documents where the
  field array is not identical to the specified array, including
  documents with a different element order, a different number of
  elements, or a missing field.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Match Document Fields That Are Not Equal

The following example returns movies where `runtime` is greater
than `1000` minutes and `rated` is not equal to `"G"`.
Because `$ne` also matches documents that don't contain the
`rated` field, the query returns movies even when the rating data
is unavailable:

```javascript
```

Output:

```javascript
```

### Update Based on Not Equal Embedded Document Fields

The following example sets the `highestRated` field based on a
`$ne` comparison on a field in an embedded document. The
`updateMany()` operation searches for an
embedded document, `imdb`, with a subfield named `rating`. It
uses `$set` to update the `highestRated` field to `false`
in each document where the value of `rating` is not equal to `9.3`
or where the `rating` subfield does not exist:

```javascript
```

Output:

```javascript
```

The SQL equivalent to this query is:

```sql
UPDATE movies SET highestRated = false WHERE imdb_rating != 9.3
```

The inequality operator `$ne` is *not* very selective since
it often matches a large portion of the index. As a result, in many
cases, a `$ne` query with an index may perform no better
than a `$ne` query that must scan all documents in a
collection. See also read-operations-query-selectivity.

### Arrays

The following examples show how `$ne` behaves differently
depending on whether you pass a scalar or an array as the
comparison value.

#### Use a Scalar Comparison

The following example returns movies where `runtime` is greater
than `1000` minutes and `"Drama"` is not an element of the
`genres` array:

```javascript
```

Output:

```javascript
```

#### Use an Exact Array Comparison

The following example returns movies where `runtime` is greater
than `1000` minutes and the `genres` array is not exactly equal
to `[ "Drama" ]`. Unlike the scalar comparison, `Centennial`
(with `genres: [ "Action", "Adventure", "Drama" ]`) matches
because that array is not identical to `[ "Drama" ]`:

```javascript
```

Output:

```javascript
```

## Learn More

- sql-to-mongodb-mapping
- read-operations-query-document
