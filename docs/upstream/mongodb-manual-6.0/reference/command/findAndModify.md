<!-- Converted from reference/command/findAndModify.txt (reStructuredText). Includes are inlined. -->

# findAndModify

## Definition

**`findAndModify`**

The `findAndModify` command updates and returns a single
document. By default, the returned document does not include the
modifications made on the update. To return the document with the
modifications made on the update, use the `new` option.

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.findAndModify()` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

**Changed in version:** 5.0

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     findAndModify: <collection-name>,
     query: <document>,
     sort: <document>,
     remove: <boolean>,
     update: <document or aggregation pipeline>,
     new: <boolean>,
     fields: <document>,
     upsert: <boolean>,
     bypassDocumentValidation: <boolean>,
     writeConcern: <document>,
     maxTimeMS: <integer>, 
     collation: <document>,
     arrayFilters: <array>,
     hint: <document|string>,
     comment: <any>,
     let: <document> // Added in MongoDB 5.0
   } 
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `query`
  - document
  - Optional. The selection criteria for the modification. The `query` field
    employs the same query selectors as used in
    the `db.collection.find()` method. Although the query may
    match multiple documents, `findAndModify`
    **will only select one document to update**.

    If unspecified, defaults to an empty document.

    If the query argument is not a document, the operation errors.

* - .. _findandmodify-command-consistent-sorting:

    `sort`

  - document
  - Optional. Determines which document the operation updates if the query 
    selects multiple documents. `findAndModify` updates the first document in the 
    sort order specified by this argument.

    If the sort argument is not a document, the operation errors.

    MongoDB does not store documents in a collection in a particular order.
    When sorting on a field which contains duplicate values, documents
    containing those values may be returned in any order.

    If consistent sort order is desired, include at least one field in your
    sort that contains unique values. The easiest way to guarantee this is
    to include the `_id` field in your sort query.

    See sort-cursor-consistent-sorting for more information.

* - `remove`
  - boolean
  - Must specify either the `remove` or the `update` field. Removes
    the document specified in the `query` field. Set this to `true`
    to remove the selected document . The default is `false`.

* - `update`
  - document or array
  - Must specify either the `remove` or the `update` field. Performs
    an update of the selected document. 

    - If passed a document with update operator expressions, `findAndModify` performs the specified
      modification.

    - If passed a replacement document `{ <field1>: <value1>, ...}`,
      the `findAndModify` performs a replacement.

    - If passed an aggregation pipeline 
      `[ <stage1>, <stage2>, ... ]`, `findAndModify` updates the document per 
      the pipeline. The pipeline can consist of the following stages:

      - `$addFields` and its alias `$set`

      - `$project` and its alias `$unset`

      - `$replaceRoot` and its alias `$replaceWith`

* - `new`
  - boolean
  - Optional. When `true`, returns the updated document rather than the original.
    The default is `false`.

* - `fields`
  - document
  - Optional. A subset of fields to return. The `fields` document specifies an
    inclusion of a field with `1`, as in: ``fields: { <field1>: 1,
    <field2>: 1, ... }``. See find-projection.

    If the fields argument is not a document, the operation errors.

* - `upsert`
  - boolean
  - .. include:: /includes/extracts/findAndModify-behavior-command.rst

* - `bypassDocumentValidation`
  - boolean
  - Optional. Enables `findAndModify` to bypass schema validation
    during the operation. This lets you update documents that do not
    meet the validation requirements.

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern.
    Omit to use the default write concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - `maxTimeMS`
  - non-negative integer
  - Optional.

    Specifies a time limit in milliseconds. 
    If you do not specify a value for `maxTimeMS`, operations will not time out. 
    A value of `0` explicitly specifies the default unbounded behavior.

    MongoDB terminates operations that exceed their allotted time limit
    using the same mechanism as `db.killOp()`. MongoDB only
    terminates an operation at one of its designated interrupt 
    points.

* - `findAndModify`
  - string
  - The collection against which to run the command.

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

    For examples, see findAndModify-command-arrayFilters.

    `arrayFilters` is not available for updates that use an
    aggregation pipeline.

* - `hint`
  - document or string
  - Optional. A document or string that specifies the
    index to use to support the `query`.

    The option can take an index specification document or the
    index name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-findAndModify-hint.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

* - let
  - document
  - .. _findAndModify-let-syntax:

    Optional.

    Specifies a document with a list of variables. This allows you to
    improve command readability by separating the variables from the query
    text.

    The document syntax is:

    ```javascript
    { 
      <variable_name_1>: <expression_1>,
      ...,
      <variable_name_n>: <expression_n>
    }
    ```

    The variable is set to the value returned by the expression, and cannot
    be changed afterwards.

    To access the value of a variable in the command, use the double
    dollar sign prefix (`$$`) together with your variable name in the form
    `$$<variable_name>`. For example: `$$targetTotal`.

    To use a variable to filter results, you must access the variable
    within the `$expr` operator.

    For a complete example using `let` and variables, 
    see findAndModify-let-example.

    **New in version:** 5.0

## Output

The `findAndModify` command returns a document with the
following fields:

| Field | Type | Description |
|---|---|---|
| `value` | document | Contains the command's returned value. See findandmodify-value-field for details. |
| `lastErrorObject` | document | Contains information about updated documents. See findandmodify-lastErrorObject for details. |
| `ok` | number | Contains the command's execution status. `1` on success, or `0` if an error occurred. |

       

### `lastErrorObject`

The `lastErrorObject` embedded document contains the following fields:

* - Field

  - Type

  - Description

* - `updatedExisting`

  - boolean

  - Contains `true` if an `update` operation:

    - Updated an existing document.
    - Found the document, but it was already in the
      desired destination state so no update actually occurred.

* - `upserted`

  - document

  - Contains the objectid of the inserted document if an `update`
    operation with `upsert: true` resulted in a new document.
       
       

### `value`

For `remove` operations, `value` contains the removed document if
the query matches a document. If the query does not match a document to
remove, `value` contains `null`.

For `update` operations, the `value` embedded document contains the
following:

- If the `new` parameter is not set or is `false`:

  - the pre-modification document if the query matches a document;

  - otherwise, `null`.

- If `new` is `true`:

  - the updated document if the query returns a match;

  - the inserted document if `upsert: true` and no document matches the query;

  - otherwise, `null`.

## Behavior

### Upsert with Unique Index

Upserts can create duplicate documents, unless there is a
unique index to prevent duplicates.

Consider an example where no document with the name `Andy` exists
and multiple clients issue the following command at roughly the same
time:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { name: "Andy" },
     update: { $inc: { score: 1 } },
     upsert: true
   }
)
```

If all `findAndModify` operations finish the query phase before any
client successfully inserts data, **and** there is no unique index on
the `name` field, each `findAndModify` operation may result in an
insert, creating multiple documents with `name: Andy`.

A unique index on the `name` field ensures that only one document
is created. With a unique index in place, the multiple `findAndModify`
operations now exhibit the following behavior:

- Exactly one `findAndModify` operation will successfully insert a new
  document.

- Other `findAndModify` operations either update the newly-inserted
  document or fail due to a unique key collision.

  In order for other `findAndModify` operations to update the
  newly-inserted document, **all** of the following conditions must
  be met:

  - The target collection has a unique index that would cause a
    duplicate key error.

  - The update operation is not `updateMany` or `multi` is
    `false`.

  - The update match condition is either:

    - A single equality predicate. For example `{ "fieldA" : "valueA" }`

    - A logical AND of equality predicates. For example ``{ "fieldA" :
      "valueA", "fieldB" : "valueB" }``

  - The fields in the equality predicate match the fields in the
    unique index key pattern.

  - The update operation does not modify any fields in the
    unique index key pattern.

The following table shows examples of `upsert` operations that,
when a key collision occurs, either result in an update or fail.

| Unique Index Key Pattern | Update Operation | Result |
|---|---|---|
| .. code-block:: javascript :copyable: false { name : 1 } | .. code-block:: javascript :copyable: false db.people.updateOne( { name: "Andy" }, { $inc: { score: 1 } }, { upsert: true } ) | The `score` field of the matched document is incremented by 1. |
| .. code-block:: javascript :copyable: false { name : 1 } | .. code-block:: javascript :copyable: false db.people.updateOne( { name: { $ne: "Joe" } }, { $set: { name: "Andy" } }, { upsert: true } ) | The operation fails because it modifies the field in the unique index key pattern (`name`). |
| .. code-block:: javascript :copyable: false { name : 1 } | .. code-block:: javascript :copyable: false db.people.updateOne( { name: "Andy", email: "andy@xyz.com" }, { $set: { active: false } }, { upsert: true } ) | The operation fails because the equality predicate fields (`name`, `email`) do not match the index key field (`name`). |

### Sharded Collections

To use `findAndModify` on a sharded collection:

- If you only target one shard, you can use a partial shard key in the `query` field or,

- You can provide an equality condition on a full shard key in the `query` field. 

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

To update the **existing** shard key value with
`findAndModify`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write.
   
- You must include an equality filter on the full shard key.

#### Missing Shard Key

Documents in a sharded collection can be
missing the shard key fields. To use
`findAndModify` to set the document's **missing** shard
key:

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

   

### Schema Validation

The `findAndModify` command adds support for the
`bypassDocumentValidation` option, which lets you bypass
schema validation when
inserting or updating documents in a collection with validation    
rules.

### Comparisons with the `update` Method

When updating a document, `findAndModify` and the
`updateOne()` method operate differently:

- If multiple documents match the update criteria, for
  `findAndModify`, you can specify a `sort` to provide some
  measure of control on which document to update.

  `updateOne()` updates the first document that
  matches.

- By default, `findAndModify` returns an object that contains the pre-modified version of the. To
  obtain the updated document, use the `new` option.

  The `updateOne()` method returns a
  `WriteResult` object that contains the status of the operation.

  To return the updated document, use the `find()`
  method. However, other updates may have modified the document between
  your update and the document retrieval. Also, if the update modified
  only a single document but multiple documents matched, you will need to
  use additional logic to identify the updated document.

When modifying a *single* document, both `findAndModify` and the
`updateOne()` method *atomically* update the
document. See /core/write-operations-atomicity for more
details about interactions and order of operations of these methods.

### Transactions

`findAndModify` can be used inside distributed transactions.

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

`findAndModify` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

## Examples

### Update and Return

The following command updates an existing document in the `people`
collection where the document matches the `query` criteria:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { name: "Tom", state: "active", rating: { $gt: 10 } },
     sort: { rating: 1 },
     update: { $inc: { score: 1 } }
   }
)
```

This command performs the following actions:

#. The `query` finds a document in the `people` collection where the
   `name` field has the value `Tom`, the `state` field has
   the value `active` and the `rating` field has a value
   `greater than` 10.

#. The `sort` orders the results of the query in ascending order.
   If multiple documents meet the `query` condition, the command will
   select for modification the first document as ordered by this
   `sort`.

#. The `update` `increments` the value of the
   `score` field by 1.

#. The command returns a document with the following fields:

   - The `lastErrorObject` field that contains the details of the
     command, including the field `updatedExisting` which is
     `true`, and

   - The `value` field that contains the original (i.e.
     pre-modification) document selected for this update:

     ```javascript
     {
       "lastErrorObject" : {
          "connectionId" : 1,
          "updatedExisting" : true,
          "n" : 1,
          "syncMillis" : 0,
          "writtenTo" : null,
          "err" : null,
          "ok" : 1
       },
       value" : {
         "_id" : ObjectId("54f62d2885e4be1f982b9c9c"),
         "name" : "Tom",
         "state" : "active",
         "rating" : 100,
         "score" : 5
       },
       "ok" : 1
     }
     ```

To return the updated document in the `value` field, add the
`new:true` option to the command.

If no document match the `query` condition, the command
returns a document that contains `null` in the `value`
field:

```javascript
{ "value" : null, "ok" : 1 }
```

`mongosh` and many drivers
provide a `findAndModify()` helper method.
Using the shell helper, this previous operation can take the
following form:

```javascript
db.people.findAndModify( {
   query: { name: "Tom", state: "active", rating: { $gt: 10 } },
   sort: { rating: 1 },
   update: { $inc: { score: 1 } }
} );
```

However, the `findAndModify()` shell helper
method returns only the unmodified document, or if `new` is
`true`, the updated document.

```javascript
{
   "_id" : ObjectId("54f62d2885e4be1f982b9c9c"),
   "name" : "Tom",
   "state" : "active",
   "rating" : 100,
   "score" : 5
}
```

### `upsert: true`

The following `findAndModify` command includes the ``upsert:
true` option for the `update`` operation to either update a matching
document or, if no matching document exists, create a new document:

```javascript
db.runCommand(
               {
                 findAndModify: "people",
                 query: { name: "Gus", state: "active", rating: 100 },
                 sort: { rating: 1 },
                 update: { $inc: { score: 1 } },
                 upsert: true
               }
             )
```

If the command finds a matching document, the command performs an update.

If the command does **not** find a matching document, the `update`
with upsert: true operation results in an insertion
and returns a document with the following fields:

- The `lastErrorObject` field that contains the details of the
  command, including the field `upserted` that contains the
  `_id` value of the newly inserted document, and

- The `value` field containing `null`.

```bash
{
  "value" : null,
  "lastErrorObject" : {
     "updatedExisting" : false,
     "n" : 1,
     "upserted" : ObjectId("54f62c8bc85d4472eadea26f")
  },
  "ok" : 1
}
```

### Return New Document

The following `findAndModify` command includes both
`upsert: true` option and the `new:true` option. The command either
updates a matching document and returns the updated document or, if no
matching document exists, inserts a document and returns the newly
inserted document in the `value` field.

In the following example, no document in the `people` collection
matches the `query` condition:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { name: "Pascal", state: "active", rating: 25 },
     sort: { rating: 1 },
     update: { $inc: { score: 1 } },
     upsert: true,
     new: true
   }
)
```

The command returns the newly inserted document in the `value` field:

```bash
{
  "lastErrorObject" : {
     "connectionId" : 1,
     "updatedExisting" : false,
     "upserted" : ObjectId("54f62bbfc85d4472eadea26d"),
     "n" : 1,
     "syncMillis" : 0,
     "writtenTo" : null,
     "err" : null,
     "ok" : 1
  },
  "value" : {
     "_id" : ObjectId("54f62bbfc85d4472eadea26d"),
     "name" : "Pascal",
     "rating" : 25,
     "state" : "active",
     "score" : 1
  },
  "ok" : 1
}
```

### Sort and Remove

By including a `sort` specification on the `rating` field, the
following example removes from the `people` collection a single
document with the `state` value of `active` and the lowest
`rating` among the matching documents:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { state: "active" },
     sort: { rating: 1 },
     remove: true
   }
)
```

The command returns the deleted document:

```bash
{
  "lastErrorObject" : {
     "connectionId" : 1,
     "n" : 1,
     "syncMillis" : 0,
     "writtenTo" : null,
     "err" : null,
     "ok" : 1
  },
  "value" : {
     "_id" : ObjectId("54f62a6785e4be1f982b9c9b"),
     "name" : "XYZ123",
     "score" : 1,
     "state" : "active",
     "rating" : 3
  },
  "ok" : 1
}
```

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
db.runCommand(
   {
     findAndModify: "myColl",
     query: { category: "cafe", status: "a" },
     sort: { category: 1 },
     update: { $set: { status: "Updated" } },
     collation: { locale: "fr", strength: 1 }
   }
)
```

The operation returns the following document:

```javascript
{
   "lastErrorObject" : {
      "updatedExisting" : true,
      "n" : 1
   },
   "value" : {
      "_id" : 1,
      "category" : "café",
      "status" : "A"
   },
   "ok" : 1
}
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

To update all elements that are greater than or equal to `100` in the
`grades` array, use the positional `$[<identifier>]`
operator with the `arrayFilters` option:
   

```javascript
db.runCommand(
   {
     findAndModify: "students",
     query: { grades: { $gte: 100 } },
     update:  { $set: { "grades.$[element]" : 100 } },
     arrayFilters: [ { "element": { $gte: 100 } } ]
   }
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
the `arrayFilters` to update the `mean` for all elements in the
`grades` array where the grade is greater than or equal to `85`.

```javascript
db.runCommand(
   {
     findAndModify: "students2",
     query: { _id : 1 },
     update: { $set: { "grades.$[elem].mean" : 100 } },
     arrayFilters: [ { "elem.grade": { $gte: 85 } } ] 
   }
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

`findAndModify` can accept an aggregation pipeline for the update. 
The pipeline can consist of the following stages:

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
db.runCommand(
   {
     findAndModify: "students2",
     query: {  "_id" : 1 },
     update: [ { $set: { "total" : { $sum: "$grades.grade" } } } ],
     new: true
   }
)
```

**Note:**

The `$set` used in the pipeline refers to the aggregation stage
`$set` and not the update operator `$set`.

After the operation, the collection has the following documents:

```javascript
{ 
  "_id" : 1, 
  "grades" : [ { "grade" : 80, "mean" : 75, "std" : 6 }, { "grade" : 85, "mean" : 90, "std" : 4 }, { "grade" : 85, "mean" :85, "std" : 6 } ], 
  "total" : 250
}
{
   "_id" : 2,
   "grades" : [ { "grade" : 90, "mean" : 75, "std" : 6 }, { "grade" : 87, "mean" : 90, "std" : 3 }, { "grade" : 85, "mean" : 85,"std" : 4 } ]
}
```

### Specify `hint` for `findAndModify` Operations

In `mongosh`, create a `members` collection
with the following documents:

```javascript
db.members.insertMany( [
   { "_id" : 1, "member" : "abc123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 2, "member" : "xyz123", "status" : "A", "points" : 60,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" },
   { "_id" : 3, "member" : "lmn123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 4, "member" : "pqr123", "status" : "D", "points" : 20,  "misc1" : "Deactivated", "misc2" : null },
   { "_id" : 5, "member" : "ijk123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 6, "member" : "cde123", "status" : "A", "points" : 86,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" }
] )
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following operation explicitly hints to use the index
`{ status: 1 }`:

```javascript
db.runCommand({
   findAndModify: "members",
   query: { "points": { $lte: 20 }, "status": "P" },
   remove: true,
   hint: { status: 1 }
})
```

**Note:**

If you specify an index that does not exist, the operation errors.

To see the index used, run `explain` on the operation:

```javascript
db.runCommand(
   {
     explain: {
       findAndModify: "members",
       query: { "points": { $lte: 20 }, "status": "P" },
       remove: true,
       hint: { status: 1 }
     },
     verbosity: "queryPlanner"
   }
)
```

### Use Variables in `let`

**New in version:** 5.0

To define variables that you can access elsewhere in the command, use
the let option.

**Note:**

To filter results using a variable, you must access the variable
within the `$expr` operator.

Create a collection `cakeFlavors`:

```javascript
db.cakeFlavors.insertMany( [
   { _id: 1, flavor: "chocolate" },
   { _id: 2, flavor: "strawberry" },
   { _id: 3, flavor: "cherry" }
] )
```

The following example defines a `targetFlavor` variable in `let` and
uses the variable to change the cake flavor from cherry to orange:

```javascript
db.cakeFlavors.runCommand( {
   findAndModify: db.cakeFlavors.getName(),
   query: { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   update: { flavor: "orange" },
   let: { targetFlavor: "cherry" }
} )
```
