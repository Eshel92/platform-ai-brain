<!-- Converted from reference/operator/query/size.txt (reStructuredText). Includes are inlined. -->

# $size (query predicate operator)

**`$size`**

The `$size` operator matches any array with the number of
elements specified by the argument.

## Compatibility

You can use `$size` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

Consider the following examples:

```javascript
db.collection.find( { field: { $size: 2 } } );
```

This query returns all documents in `collection` where `field` is an
array with 2 elements. For example, the query returns
`{ field: [ red, green ] }` and ``{ field: [ apple,
lime ] }` but *not* `{ field: fruit }` or `{ field: [
orange, lemon, grapefruit ] }``. To match fields with only one
element within an array use `$size` with a value of 1, as
follows:

```javascript
db.collection.find( { field: { $size: 1 } } );
```

`$size` does not accept ranges of values. To select
documents based on fields with different numbers of elements,
create a counter field that you increment when you add elements to
a field.

Queries cannot use indexes for the `$size` portion of a
query, although the other portions of a query can use indexes if
applicable.

## Additional Examples

For additional examples on querying arrays, see:

- read-operations-arrays
- array-match-embedded-documents

For additional examples on querying, see 
read-operations-query-document.

**See also:**

`db.collection.find()`
