<!-- Converted from reference/operator/query/exists.txt (reStructuredText). Includes are inlined. -->

# $exists

## Definition

**`$exists`**

The `$exists` operator matches documents that
contain or do not contain a specified field, including documents 
where the field value is `null`.

**Note:**

MongoDB `$exists` does **not** correspond to SQL operator
`exists`. For SQL `exists`, refer to the `$in`
operator. 

For Atlas Search `exists`, refer to the exists-ref 
operator in the Atlas documentation.

**See also:**

- `$nin`
- `$in`
- faq-developers-query-for-nulls

## Compatibility

You can use `$exists` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

To specify an `$exists` expression, use the following prototype:

```javascript
{ field: { $exists: <boolean> } }
```

When `<boolean>` is true, `$exists` matches the documents that
contain the field, including documents where the field value is
`null`. If `<boolean>` is false, the query returns only the
documents that do not contain the field. [#type0]_

## Query Data on Atlas by Using Atlas Search

For data stored in MongoDB Atlas, you can use the 
Atlas Search exists-ref 
operator when running `$search` queries. Running 
`$exists` after `$search` is less performant 
than running `$search` with the exists-ref
operator.

To learn more about the Atlas Search version of this operator, 
see the exists-ref operator in the Atlas documentation.

## Examples

### Exists and Not Equal To

Consider the following example:

```javascript
db.inventory.find( { qty: { $exists: true, $nin: [ 5, 15 ] } } )
```

This query will select all documents in the `inventory` collection
where the `qty` field exists *and* its value does not equal `5` or
`15`.

### Null Values

The following examples uses a collection named `spices` with the
following documents:

```javascript
db.spices.insertMany( [
   { saffron: 5, cinnamon: 5, mustard: null },
   { saffron: 3, cinnamon: null, mustard: 8 },
   { saffron: null, cinnamon: 3, mustard: 9 },
   { saffron: 1, cinnamon: 2, mustard: 3 },
   { saffron: 2, mustard: 5 },
   { saffron: 3, cinnamon: 2 },
   { saffron: 4 },
   { cinnamon: 2, mustard: 4 },
   { cinnamon: 2 },
   { mustard: 6 }
] )
```

#### `$exists: true`

The following query specifies the query predicate `saffron: { $exists: true }`:

```javascript
db.spices.find( { saffron: { $exists: true } } )
```

The results consist of those documents that contain the field `saffron`,
including the document whose field `saffron` contains a null value:

```javascript
{ saffron: 5, cinnamon: 5, mustard: null }
{ saffron: 3, cinnamon: null, mustard: 8 }
{ saffron: null, cinnamon: 3, mustard: 9 }
{ saffron: 1, cinnamon: 2, mustard: 3 }
{ saffron: 2, mustard: 5 }
{ saffron: 3, cinnamon: 2 }
{ saffron: 4 }
```

   

#### `$exists: false`

The following query specifies the query predicate `cinnamon: { $exists: false }`:

```javascript
db.spices.find( { cinnamon: { $exists: false } } )
```

The results consist of those documents that do not contain the field
`cinnamon`:

```javascript
{ saffron: 2, mustard: 5 }
{ saffron: 4 }
{ mustard: 6 }
```

Users can no longer use the query filter `$type: 0` as a synonym for
`$exists:false`. To query for null or missing fields, see
/tutorial/query-for-null-fields.

### Use a Sparse Index to Improve `$exists` Performance

The following table compares `$exists` query performance using sparse 
and non-sparse indexes:

| `$exists` Query | Using a Sparse Index | Using a Non-Sparse Index |
|---|---|---|
| `{ $exists: true }` | Most efficient. MongoDB can make an exact match and does not require a `FETCH`. | More efficient than queries without an index, but still requires a `FETCH`. |
| `{ $exists: false }` | Cannot use the index and requires a `COLLSCAN`. | Requires a `FETCH`. |

Queries that use `{ $exists: true }` on fields that use a non-sparse 
index or that use `{ $exists: true }` on fields that are not indexed
examine all documents in a collection. To improve performance, create 
a sparse index on the `field` as shown in 
the following scenario:

#. Create a `stockSales` collection:

   ```javascript
   db.stockSales.insertMany( [
      { _id: 0, symbol: "MDB", auditDate: new Date( "2021-05-18T16:12:23Z" ) },
      { _id: 1, symbol: "MDB", auditDate: new Date( "2021-04-21T11:34:45Z" ) },
      { _id: 2, symbol: "MSFT", auditDate: new Date( "2021-02-24T15:11:32Z" ) },
      { _id: 3, symbol: "MSFT", auditDate: null },
      { _id: 4, symbol: "MSFT", auditDate: new Date( "2021-07-13T18:32:54Z" ) },
      { _id: 5, symbol: "AAPL" }
   ] )
   ```

   The document with an `_id` of:

   - `3` has a null `auditDate` value.
   - `5` is missing the `auditDate` value.

#. Create a sparse index on the
   `auditDate` field:

   ```javascript
   db.getCollection( "stockSales" ).createIndex( 
      { auditDate: 1 },
      { name: "auditDateSparseIndex", sparse: true }
   )
   ```

#. The following example counts the documents where the `auditDate`
   field has a value (including null) and uses the sparse index:

   ```javascript
   db.stockSales.countDocuments( { auditDate: { $exists: true } } )
   ```

   The example returns 5. The document that is missing the `auditDate`
   value is not counted.

**Tip:**

If you only need documents where the `field` has a non-null value,
you:

- Can use `$ne: null` instead of `$exists: true`.
- Do not need a sparse index on the
  `field`.

For example, using the `stockSales` collection:

```javascript
db.stockSales.countDocuments( { auditDate: { $ne: null } } )
```

The example returns 4. Documents that are missing the `auditDate`
value or have a null `auditDate` value are not counted.

**See also:**

/tutorial/query-for-null-fields
