<!-- Converted from reference/method/db.collection.findOneAndUpdate.txt (reStructuredText). Includes are inlined. -->

# db.collection.findOneAndUpdate()

(Include not available offline: includes/wayfinding/mongosh-method-findOneAndUpdate.rst)

## Definition

**`db.collection.findOneAndUpdate( filter, update, options )`**

Updates a single document based on the `filter` and
`sort` criteria.

:returns:
   Returns the original document by default. Returns the updated document
   if returnNewDocument is set to
   `true` or returnDocument is
   set to `after`.

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

## Syntax

The `findOneAndUpdate()` method has the following
form:

```javascript
db.collection.findOneAndUpdate(
    <filter>,
    <update document or aggregation pipeline>,
    {
      writeConcern: <document>,
      projection: <document>,
      sort: <document>,
      maxTimeMS: <number>,
      upsert: <boolean>,
      returnDocument: <string>,
      returnNewDocument: <boolean>,
      collation: <document>,
      arrayFilters: [ <filterdocument1>, ... ]
    }
)
```

The `findOneAndUpdate()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - `filter`
  - document
  - The selection criteria for the update. The same query
    selectors as in the `find()` method are available.

    To update the first document returned in the collection,
    specify an empty document `{ }`.

    If unspecified, defaults to an empty document.

    If the query field is not a document, the operation returns an error.

    If no document matches the `filter`, no document is updated.

* - `update`
  - document or array
  - The update document or an aggregation pipeline.

    - If passed a document with update operator expressions, `db.collection.findOneAndUpdate()` performs the specified
      modification.

      **Note:**

      The document must contain only update operators. You cannot specify a
      replacement document `{ <field1>: <value1>, ...}`. To
      use a replacement document, see
      `db.collection.findOneAndReplace()` instead.

    - If passed an aggregation pipeline
      `[ <stage1>, <stage2>, ... ]`, `db.collection.findOneAndUpdate()` modifies the
      document per the pipeline. The pipeline can consist of the
      following stages:

      - `$addFields` and its alias `$set`

      - `$project` and its alias `$unset`

      - `$replaceRoot` and its alias `$replaceWith`

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern.
    Omit to use the default write concern.

    ```javascript
    { w: <value>, j: <boolean>, wtimeout: <number> }
    ```

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

* - `upsert`
  - boolean
  - .. include:: /includes/extracts/findOneAndUpdate-behavior-method.rst

* - `returnDocument`
  - string
  - .. _findOneUpdate-returnDocument:

    Optional. Starting in `mongosh` 0.13.2,
    `returnDocument` is an alternative for
    `returnNewDocument`. If both options are set,
    `returnDocument` takes precedence.

    `returnDocument: "before"` returns the original document.
    `returnDocument: "after"` returns the updated document.

* - `returnNewDocument`
  - boolean
  - .. _findOneUpdate-returnNewDocument:

    Optional. When `true`, returns the updated document instead
    of the original document.

    Defaults to `false`.

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

* - `arrayFilters`
  - array
  - Optional. An array of filter documents that determine which array elements to
    modify for an update operation on an array field.

    In the update document, use the `$[<identifier>]` filtered
    positional operator to define an identifier, which you then reference
    in the array filter documents. You cannot have an array filter
    document for an identifier if the identifier is not included in the
    update document.

    The `<identifier>` must begin with a lowercase letter and
    contain only alphanumeric characters.

    You can include the same identifier multiple times in the update
    document; however, for each distinct identifier (`$[identifier]`)
    in the update document, you must specify **exactly one**
    corresponding array filter document. That is, you cannot specify
    multiple array filter documents for the same identifier. For
    example, if the update statement includes the identifier `x`
    (possibly multiple times), you cannot specify the following for
    `arrayFilters` that includes 2 separate filter documents for `x`:

    ```javascript
    // INVALID

    [
      { "x.a": { $gt: 85 } },
      { "x.b": { $gt: 80 } }
    ]
    ```

    However, you can specify compound conditions on the same identifier
    in a single filter document, such as in the following examples:

    ```javascript
    // Example 1
    [
      { $or: [{"x.a": {$gt: 85}}, {"x.b": {$gt: 80}}] }
    ]
    // Example 2
    [
      { $and: [{"x.a": {$gt: 85}}, {"x.b": {$gt: 80}}] }
    ]
    // Example 3
    [
      { "x.a": { $gt: 85 }, "x.b": { $gt: 80 } }
    ]
    ```

    For examples, see findOneAndUpdate-arrayFilters.

    **Note:**

    `arrayFilters` is not available for updates that use an
    aggregation pipeline.

## Behavior

### Document Match

`db.collection.findOneAndUpdate()` updates the first matching
document in the collection that matches the `filter`. If no document
matches the `filter`, no document is updated.

The `sort` parameter can be used to influence which document is updated.

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
{ field1 : <value>, field2 : <value> ... }
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

#### Shard Key Modification

You can update a document's shard key value unless the shard key field is the 
immutable `_id` field. 

**Warning:**

Documents in sharded collections can be missing the shard key fields. 
Take precaution to avoid accidentally removing the shard key when changing 
a document's shard key value.

To modify the **existing** shard key value with
`db.collection.findOneAndUpdate()`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write.
  
- You must include an equality filter on the full shard key.

#### Missing Shard Key

Documents in a sharded collection can be
missing the shard key fields. To use
`db.collection.findOneAndUpdate()` to set the document's
**missing** shard key, 

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write if the new shard key value is not
  `null`.

- You must include an equality filter on the full shard key.

**Tip:**

Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.

See also:

- shard-key-missing
   

### Transactions

`db.collection.findOneAndUpdate()` can be used inside distributed transactions.

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

#### Upsert within Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

`db.collection.findOneAndUpdate()` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Oplog Entries

If a `db.collection.findOneAndUpdate()` operation successfully updates
a document, the operation adds an entry on the oplog (operations
log). If the operation fails or does not find a document to update, the
operation does not add an entry on the oplog. 

## Examples

### Update A Document

The `grades` collection contains documents similar to the following:

```javascript
{ _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
{ _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
{ _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
{ _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
{ _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
{ _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
```

The following operation finds the first document where `name : R. Stiles`
and increments the score by `5`:

```javascript
db.grades.findOneAndUpdate(
   { "name" : "R. Stiles" },
   { $inc: { "points" : 5 } }
)
```

The operation returns the *original* document before the update:

```javascript
{ _id: 6319, name: "R. Stiles", "assignment" : 2, "points" : 12 }
```

If `returnNewDocument` was true, the operation would return the
updated document instead.

### Sort And Update A Document

The `grades` collection contains documents similar to the following:

```javascript
{ _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
{ _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
{ _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
{ _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
{ _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
{ _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
```

The following operation updates a document where `name : "A. MacDyver"`.  The
operation sorts the matching documents by `points` ascending to update the
matching document with the least points.

```javascript
db.grades.findOneAndUpdate(
   { "name" : "A. MacDyver" },
   { $inc : { "points" : 5 } },
   { sort : { "points" : 1 } }
)
```

The operation returns the *original* document before the update:

```javascript
{ _id: 6322, name: "A. MacDyver", "assignment" : 2, "points" : 14 }
```

### Project the Returned Document

The following operation uses projection to only display the `_id`,
`points`, and `assignment` fields in the returned document:

```javascript
db.grades.findOneAndUpdate(
   { "name" : "A. MacDyver" },
   { $inc : { "points" : 5 } },
   { sort : { "points" : 1 }, projection: { "assignment" : 1, "points" : 1 } }
)
```

The operation returns the *original* document with only the
fields specified in the `projection` document and the `_id` field as it was not
explicitly suppressed (`_id: 0`) in the projection document.

```javascript
{ "_id" : 6322, "assignment" : 2, "points" : 14 }
```

### Update Document with Time Limit

The following operation sets a 5ms time limit to complete the update:

```javascript
try {
   db.grades.findOneAndUpdate(
      { "name" : "A. MacDyver" },
      { $inc : { "points" : 5 } },
      { sort: { "points" : 1 }, maxTimeMS : 5 };
   );
}
catch(e){
   print(e);
}
```

If the operation exceeds the time limit, it returns:

```javascript
Error: findAndModifyFailed failed: { "ok" : 0, "errmsg" : "operation exceeded time limit", "code" : 50 }
```

### Update Document with Upsert

The following operation uses the `upsert` field to insert the update
document if nothing matches the `filter`:

```javascript
try {
db.grades.findOneAndUpdate(
   { "name" : "A.B. Abracus" },
   { $set: { "name" : "A.B. Abracus", "assignment" : 5}, $inc : { "points" : 5 } },
   { sort: { "points" : 1 }, upsert:true, returnNewDocument : true }
);
}
catch (e){
   print(e);
}
```

The operation returns the following:

```javascript
{
   "_id" : ObjectId("5789249f1c49e39a8adc479a"),
   "name" : "A.B. Abracus",
   "assignment" : 5,
   "points" : 5
}
```

If `returnNewDocument` was false, the operation would return `null` as
there is no original document to return.

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following operation includes the collation
option:

```javascript
db.myColl.findOneAndUpdate(
   { category: "cafe" },
   { $set: { status: "Updated" } },
   { collation: { locale: "fr", strength: 1 } }
);
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```

### Array Update Operations with `arrayFilters`

**Note:**

`arrayFilters` is not available for updates that use an
aggregation pipeline.

When updating an array field, you can specify `arrayFilters` that 
determine which array elements to update.

#### Update Elements Match `arrayFilters` Criteria

**Note:**

`arrayFilters` is not available for updates that use an
aggregation pipeline.

Create a collection `students` with the following documents:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 95, 92, 90 ] },
   { "_id" : 2, "grades" : [ 98, 100, 102 ] },
   { "_id" : 3, "grades" : [ 95, 110, 100 ] }
] )
```

To modify all elements that are greater than or equal to `100` in the
`grades` array, use the filtered positional operator
`$[<identifier>]` with the `arrayFilters` option in the
`db.collection.findOneAndUpdate` method:

```javascript
db.students.findOneAndUpdate(
   { grades: { $gte: 100 } },
   { $set: { "grades.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

The operation updates the `grades` field for a single document, and
after the operation, the collection has the following documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 100 ] }
{ "_id" : 3, "grades" : [ 95, 110, 100 ] }
```

#### Update Specific Elements of an Array of Documents

**Note:**

`arrayFilters` is not available for updates that use an
aggregation pipeline.

Create a collection `students2` with the following documents:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
] )
```

The following operation finds a document where the `_id` field equals
`1` and uses the filtered positional operator `$[<identifier>]` with
the `arrayFilters` to modify the `mean` for all elements in the
`grades` array where the grade is greater than or equal to `85`.

```javascript
db.students2.findOneAndUpdate(
   { _id : 1 },
   { $set: { "grades.$[elem].mean" : 100 } },
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)
```

The operation updates the `grades` field for a single document, and after the
operation, the collection has the following documents:

```javascript
{
   "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 6 },
      { "grade" : 85, "mean" : 100, "std" : 4 },
      { "grade" : 85, "mean" : 100, "std" : 6 }
    ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 75, "std" : 6 },
      { "grade" : 87, "mean" : 90, "std" : 3 },
      { "grade" : 85, "mean" : 85, "std" : 4 }
   ]
}
```

### Use an Aggregation Pipeline for Updates

`db.collection.findOneAndUpdate()` can accept an aggregation pipeline 
for the update. The pipeline can consist of the following stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`

Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

For example, create a collection `students2` with the following
documents:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
] )
```

The following operation finds a document where the `_id` field equals
`1` and uses an aggregation pipeline to calculate a new field
`total` from the `grades` field:

```javascript
db.students2.findOneAndUpdate(
   { _id : 1 },
   [ { $set: { "total" : { $sum: "$grades.grade" } } } ],  // The $set stage is an alias for ``$addFields`` stage
   { returnNewDocument: true }
)
```

**Note:**

The `$set` used in the pipeline refers to the aggregation stage
`$set` and not the update operator `$set`.

The operation returns the *updated* document :

```javascript
{ 
  "_id" : 1, 
  "grades" : [ { "grade" : 80, "mean" : 75, "std" : 6 }, { "grade" : 85, "mean" : 90, "std" : 4 }, { "grade" : 85, "mean" :85, "std" : 6 } ], 
  "total" : 250
}
```
