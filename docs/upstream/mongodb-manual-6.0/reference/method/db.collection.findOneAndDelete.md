<!-- Converted from reference/method/db.collection.findOneAndDelete.txt (reStructuredText). Includes are inlined. -->

# db.collection.findOneAndDelete()

(Include not available offline: includes/wayfinding/mongosh-method-findOneAndDelete.rst)

## Definition

**`db.collection.findOneAndDelete( filter, options )`**

Deletes a single document based on the `filter` and 
`sort` criteria, returning the deleted document.

The `findOneAndDelete()` method has the following 
form:

```none
db.collection.findOneAndDelete(
   <filter>,
   {
     writeConcern: <document>,
     projection: <document>,
     sort: <document>,
     maxTimeMS: <number>,
     collation: <document>
   }
)
```

The `findOneAndDelete()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - `filter`
  - document
  - The selection criteria for the deletion. The same query
    selectors as in the `find()` method are available.

    Specify an empty document `{ }` to delete the first document returned in 
    the collection.

    If unspecified, defaults to an empty document.

    If the query argument is not a document, the operation errors.

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern.
    Omit to use the default write concern.

    ```javascript
    { w: <value>, j: <boolean>, wtimeout: <number> }
    ```

    See Delete A Document Using WriteConcern for usage.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - `projection`
  - document
  - Optional. A subset of fields to return.

    To return all fields in the returned document, omit this parameter.

    If the projection argument is not a document, the operation errors.

* - `sort`
  - document
  - Optional. Specifies a sorting order for the documents matched by the `filter`.

    If the sort argument is not a document, the operation errors.

    See `cursor.sort()`.

* - `maxTimeMS`
  - number
  - Optional. Specifies a time limit in milliseconds within which the operation must 
    complete within. Throws an error if the limit is exceeded.

* - `collation`
  - document
  - Optional. 

    Specifies the collation  to use for the operation.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    The collation option has the following syntax:

    ```none
    collation: {
       locale: <string>,
       caseLevel: <boolean>,
       caseFirst: <string>,
       strength: <int>,
       numericOrdering: <boolean>,
       alternate: <string>,
       maxVariable: <string>,
       backwards: <boolean>
    }
    ```

    When specifying collation, the `locale` field is mandatory; all
    other collation fields are optional. For descriptions of the fields,
    see collation-document-fields.

    If the collation is unspecified but the collection has a
    default collation (see `db.createCollection()`), the
    operation uses the collation specified for the collection.

    If no collation is specified for the collection or for the
    operations, MongoDB uses the simple binary comparison used in prior
    versions for string comparisons.

    You cannot specify multiple collations for an operation. For
    example, you cannot specify different collations per field, or if
    performing a find with a sort, you cannot use one collation for the
    find and another for the sort.

:returns:

   Returns the deleted document.

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

### Document Match

`findOneAndDelete()` deletes the first matching 
document in the collection that matches the `filter`. 
The `sort` parameter can be used to influence which document is deleted.

### Projection

**Important:** Language Consistency

As part of making `find` and
`findAndModify` projection consistent with
aggregation's `$project` stage,

- The `find` and
  `findAndModify` projection can accept
  aggregation expressions and syntax.

- MongoDB enforces additional restrictions with regards to
  projections. See `Projection Restrictions` for details.

The `projection` parameter takes a document in the following form:

```javascript
{ field1: <value>, field2: <value> ... }
```

* - Projection
  - Description

* - `<field>: <1 or true>`

  - Specifies the inclusion of a field. If you specify a non-zero 
    integer for the projection value, the operation treats the 
    value as `true`.

* - `<field>: <0 or false>`

  - Specifies the exclusion of a field.

* - `"<field>.$": <1 or true>`

  - Uses the `$` array projection operator to return 
    the first element that matches the query condition on the
    array field. If you specify a non-zero integer for the 
    projection value, the operation treats the value as `true`.

    Not available for views.

* - `<field>: <array projection>`

  - Uses the array projection operators (`$elemMatch`,
    `$slice`) to specify the array elements to
    include. 

    Not available for views.

* - `<field>: <aggregation expression>`

  - Specifies the value of the projected field.

    With the use of aggregation
    expressions and syntax, including the
    use of literals and aggregation variables, you can project new
    fields or project existing fields with new values.

    - If you specify a non-numeric, non-boolean literal (such as a
      literal string or an array or an operator expression) for
      the projection value, the field is projected with the new
      value, for example:

      - `{ field: [ 1, 2, 3, "$someExistingField" ] }`
      - `{ field: "New String Value" }`
      - `{ field: { status: "Active", total: { $sum: "$existingArray" } } }`

    - To project a literal value for a field, use the
      `$literal` aggregation expression, for example:

      - `{ field: { $literal: 5 } }`
      - `{ field: { $literal: true } }`
      - `{ field: { $literal: { fieldWithValue0: 0, fieldWithValue1: 1 } } }` 

#### Embedded Field Specification

For fields in an embedded documents, you can specify the field using
either:

- dot notation, for example `"field.nestedfield": <value>`

- nested form, for example `{ field: { nestedfield: <value> } }`

#### `_id` Field Projection

The `_id` field is included in the returned documents by default unless
you explicitly specify `_id: 0` in the projection to suppress the field.

#### Inclusion or Exclusion

A `projection` *cannot* contain *both* include and exclude
specifications, with the exception of the `_id` field:

- In projections that *explicitly include* fields, the `_id` field is
  the only field that you can *explicitly exclude*.

- In projections that *explicitly excludes* fields, the `_id` field
  is the only field that you can *explicitly include*; however, the
  `_id` field is included by default.

For more information on projection, see also:

- read-operations-projection

### Sharded Collections

Documents in a sharded collection can be
missing the shard key fields. To target a
document that is missing the shard key, you can use the `null`
equality match in conjunction with another filter condition
(such as on the `_id` field). For example:

```javascript
{ _id: <value>, <shardkeyfield>: null } // _id of the document missing shard key
```

### Transactions

`db.collection.findOneAndDelete()` can be used inside distributed transactions.

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

**Important:**

In most cases, a distributed transaction incurs a greater
performance cost over single document writes, and the
availability of distributed transactions should not be a
replacement for effective schema design. For many scenarios, the
denormalized data model (embedded documents and arrays) will continue to be optimal for your
data and use cases. That is, for many scenarios, modeling your data
appropriately will minimize the need for distributed
transactions. 

For additional transactions usage considerations
(such as runtime limit and oplog size limit), see also
/core/transactions-production-consideration.

### Oplog Entries

If a `db.collection.findOneAndDelete()` operation successfully deletes
a document, the operation adds an entry on the oplog (operations
log). If the operation fails or does not find a document to delete, the
operation does not add an entry on the oplog. 

## Examples

### Delete A Document

The `scores` collection contains documents similar to the following:

```javascript
 db.scores.insertMany( [
   { _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
   { _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
   { _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
   { _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
   { _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
   { _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
] )
```

The following operation finds the first document where `name : M. Tagnum` 
and deletes it:

```javascript
db.scores.findOneAndDelete( 
   { "name" : "M. Tagnum" }
)
```

The operation returns the *original* document that has been deleted:

```javascript
{ _id: 6312, name: "M. Tagnum", "assignment" : 5, "points" : 30 }
```

### Delete A Document Using WriteConcern

The `scores` collection contains documents similar to the following:

```javascript
db.scores.insertMany( [
   { _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
   { _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
   { _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
   { _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
   { _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
   { _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
] )
```

The following operation uses a write concern document inside of the 
`db.collection.findOneAndDelete()` method with options:

- `w:1` to requests acknowledgment that the write operation has 
  propagated to the standalone mongod or the primary in a replica set. 
- `j:true` to tell the number of MongoDB instances specified in `w:1`
  to have the delete written to on-disk journel.
- `wtimeout : 1000` to specify a time limit, in milliseconds, 
  for the write concern. `wtimeout` is only applicable for `w` 
  values greater than 1.

```javascript
db.scores.findOneAndDelete(
   { name: "A. MacDyver" },
   { 
      writeConcern: {  
         w : 1,
         j : true,
         wtimeout : 1000
      } 
   }
)
```

The operation returns the following document:

```javascript
{ _id: 6305, name: 'A. MacDyver', assignment: 5, points: 24 }
```

The document is deleted with the writeConcern options specified.

### Sort And Delete A Document

The `scores` collection contains documents similar to the following:

```javascript
db.scores.insertMany( [
   { _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
   { _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
   { _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
   { _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
   { _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
   { _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
] )
```

The following operation first finds all documents where 
`name : "A. MacDyver"`. It then sorts by `points` ascending before 
deleting the document with the lowest points value:

```javascript
db.scores.findOneAndDelete(
   { "name" : "A. MacDyver" },
   { sort : { "points" : 1 } }
)
```

The operation returns the *original* document that has been deleted:

```javascript
{ _id: 6322, name: "A. MacDyver", "assignment" : 2, "points" : 14 }
```

### Projecting the Deleted Document

The following operation uses projection to only return the `_id` and 
`assignment` fields in the returned document:

```javascript
db.scores.findOneAndDelete(
   { "name" : "A. MacDyver" },
   { sort : { "points" : 1 }, projection: { "assignment" : 1 } }
)
```

   
The operation returns the *original* document with the 
`assignment` and `_id` fields: 

```javascript
{ _id: 6322, "assignment" : 2 }
```

### Update Document with Time Limit

The following operation sets a 5ms time limit to complete the deletion:

```javascript
try {
   db.scores.findOneAndDelete(
      { "name" : "A. MacDyver" },
      { sort : { "points" : 1 }, maxTimeMS : 5 }
   )
}
catch(e){
   print(e)
}
```

If the operation exceeds the time limit, it returns:

```javascript
MongoServerError: operation exceeded time limit: { "ok": 0, "code" : 50, "codeName" : "MaxTimeMSExpired" }
```

**Note:**

This error message has been shortened for brevity.

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```javascript
db.myColl.insertMany( [
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
] )
```

The following operation includes the collation
option:

```javascript
db.myColl.findOneAndDelete(
   { category: "cafe", status: "a" },
   { collation: { locale: "fr", strength: 1 } }
);
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```
