<!-- Converted from reference/operator/query/nin.txt (reStructuredText). Includes are inlined. -->

# $nin

**`$nin`**

`$nin` selects the documents where:

- the specified field value is not in the specified array **or**
- the specified field does not exist.

## Compatibility

You can use `$nin` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

If the `field` holds an array, then the `$nin` operator selects
the documents whose `field` holds an array with **no** element equal to
a value in the specified array (for example, `<value1>`,
`<value2>`, and so on).

For comparison of different BSON type values, see the specified
BSON comparison order.

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

### Select on Unmatching Documents

The following query selects all documents from the `inventory`
collection where the `quantity` does **not** equal either 5 or 15. 

The query also matches documents that do *not* have a `quantity`
field.

```javascript
db.inventory.find( { quantity: { $nin: [ 5, 15 ] } }, { _id: 0 } )
```

Example output:

```javascript
{ item: 'Pens', quantity: 350, tags: [ 'school', 'office' ] },
{ item: 'Maps', tags: [ 'office', 'storage' ] }
```

### Select on Elements Not in an Array

Set the `exclude` field to `true` for documents that don't have the
`"school"` tag.

```javascript
db.inventory.updateMany(
    { tags: { $nin: [ "school" ] } },
    { $set: { exclude: true } }
)
```

`updateMany()` also selects a document when the
document does not contain the field `$nin` is matching on.

The inequality operator `$nin` is *not* very selective since
it often matches a large portion of the index. As a result, in many
cases, a `$nin` query with an index may perform no better
than a `$nin` query that must scan all documents in a
collection. See also read-operations-query-selectivity.

   

**See also:**

- `find()`
- `updateMany()`
- `$set`
