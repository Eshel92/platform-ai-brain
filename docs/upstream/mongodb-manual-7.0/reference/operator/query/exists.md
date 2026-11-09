<!-- Converted from reference/operator/query/exists.txt (reStructuredText). Includes are inlined. -->

# $exists (query predicate operator)

## Definition

**`$exists`**

The `$exists` operator matches documents that
contain or do not contain a specified field, including documents 
where the field value is `null`.

**Note:**

MongoDB `$exists` does **not** correspond to SQL operator
`exists`. For SQL `exists`, see `$in`. 

For Atlas Search `exists`, see exists-ref 
in the Atlas documentation.

## Compatibility

You can use `$exists` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

Expressions do not support 
the `$exists` operator. To check for the existence of a field in an 
expression, you can use the `$type` aggregation
operator to check if a field has a type of `missing`.

For more information, see $type Existence Check.

## Syntax

To specify an `$exists` expression, use the following prototype:

```javascript
{ field: { $exists: <boolean> } }
```

When `<boolean>` is true, `$exists` matches the documents that
contain the field, including documents where the field value is
`null`. If `<boolean>` is false, the query returns only the
documents that do not contain the field.

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

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Exists and Not Equal To

Consider the following example:

```javascript
db.movies.find( { rated: { $exists: true, $nin: [ "R", "PG-13" ] } } ).limit(5)
```

This query selects 5 documents in the `movies` collection
where the `rated` field exists *and* its value does not equal `"R"` or
`"PG-13"`.

### Null Values

The `movies` collection in the `sample_mflix` database contains
documents where some fields are present and others are missing. For
example, the `rated` field exists in 11,455 documents and is absent
from the remaining 9,894 documents.

#### `$exists: true`

The following query specifies the query predicate `rated: { $exists: true }`:

```javascript
db.movies.find( { rated: { $exists: true } }, { _id: 0, title: 1, rated: 1 } ).limit( 3 )
```

The results consist of three documents that contain the field `rated`:

```javascript
[
  { title: 'The Great Train Robbery', rated: 'TV-G' },
  { title: 'A Corner in Wheat', rated: 'G' },
  { title: 'Traffic in Souls', rated: 'TV-PG' }
]
```

#### `$exists: false`

The following query specifies the query predicate `rated: { $exists: false }`:

```javascript
db.movies.find( { rated: { $exists: false } }, { _id: 0, title: 1, year: 1 } ).limit( 3 )
```

The results consist of three documents that do not contain the field
`rated`:

```javascript
[
  {
    title: 'Winsor McCay, the Famous Cartoonist of the N.Y. Herald and His Moving Comics',
    year: 1911
  },
  { title: 'Gertie the Dinosaur', year: 1914 },
  { title: 'In the Land of the Head Hunters', year: 1914 }
]
```

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

#. The `movies` collection contains documents where the
   `metacritic` field is present in some documents and absent from
   others. Of the 21,349 documents, 6,964 have the `metacritic`
   field and 14,385 do not.

#. Create a sparse index on the
   `metacritic` field:

   ```javascript
   db.movies.createIndex(
      { metacritic: 1 },
      { name: "metacriticSparseIndex", sparse: true }
   )
   ```

#. The following example counts the documents where the `metacritic`
   field has a value (including null) and uses the sparse index:

   ```javascript
   db.movies.countDocuments( { metacritic: { $exists: true } } )
   ```

   The example returns 6964. The operation does not count the documents that are
   missing the `metacritic` field.

**Tip:**

If you only need documents where the `field` has a non-null value,
you:

- Can use `$ne: null` instead of `$exists: true`.
- Do not need a sparse index on the
  `field`.

For example, using the `movies` collection:

```javascript
db.movies.countDocuments( { metacritic: { $ne: null } } )
```

The example returns 6964. Documents that are missing the
`metacritic` value or have a null `metacritic` value are not
counted.

## Learn More

- faq-developers-query-for-nulls
- `$nin`
- `$in`
