<!-- Converted from reference/method/db.collection.updateOne.txt (reStructuredText). Includes are inlined. -->

# db.collection.updateOne() (mongosh method)

(Include not available offline: includes/wayfinding/mongosh-method-updateOne.rst)

## Definition

**`db.collection.updateOne(filter, update, options)`**

Updates a single document within the collection based on the filter.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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

The `updateOne()` method has the following syntax:

```javascript
db.collection.updateOne(
   <filter>,
   <update>,
   {
     upsert: <boolean>,
     writeConcern: <document>,
     collation: <document>,
     arrayFilters: [ <filterdocument1>, ... ],
     hint:  <document|string>,
     let: <document>,
     maxTimeMS: <int>,
     bypassDocumentValidation: <boolean>
   }
)
```

### Parameters

The `db.collection.updateOne()` method takes the following
parameters:

* - Parameter

  - Type

  - Description

* - filter

  - document

  - .. _update-one-filter:

    The selection criteria for the update. The same query
    selectors as in the `find()` method are available.

    Specify an empty document `{ }` to update the first document returned in 
    the collection.

* - update

  - document or pipeline

  - .. _update-one-update:

    The modifications to apply. Can be one of the following:

    - .. _update-one-method-update-document:

      Update document:

      Contains only update operator expressions.

      For more information, see
      updateOne-behavior-update-expressions

    - .. _update-one-method-agg-pipeline:

      Aggregation pipeline:

      Contains only the following aggregation stages:

      - `$addFields` and its alias `$set`

      - `$project` and its alias `$unset`

      - `$replaceRoot` and its alias `$replaceWith`

      For more information, see
      updateOne-behavior-aggregation-pipeline.

    To update with a replacement document, see
    `db.collection.replaceOne()`.

* - `upsert`

  - boolean

  - .. include:: /includes/extracts/updateOne-behavior-method.rst

* - `writeConcern`

  - document

  - Optional. A document expressing the write concern. Omit to use the default write concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - `collation`

  - document

  - Optional. 

    Optional. Specifies the collation  to use for the operation.

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

    For examples, see updateOne-arrayFilters.

* - hint 

  - Document or string

  - .. _update-one-hint:

    Optional. A document or string that specifies the index to use to support the query predicate.

    The option can take an index specification document or the index
    name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-update-one-hint.

* - `let`

  - Document

  - .. _updateOne-let-syntax:

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
    see updateMany-let-example.

* - maxTimeMS
  - integer
  - .. _updateOne-maxTimeMS:

    Optional. Specifies the time limit in milliseconds for the
    update operation to run before timing out.

* - bypassDocumentValidation
  - boolean
  - .. _updateOne-bypassDocumentValidation:

    Optional. Enables `insert` to bypass schema validation
    during the operation. This lets you insert documents that do not
    meet the validation requirements.

### Returns

The method returns a document that contains:

- `matchedCount` containing the number of matched documents

- `modifiedCount` containing the number of modified documents

- `upsertedId` containing the `_id` for the upserted document

- `upsertedCount` containing the number of upserted documents

- A boolean `acknowledged` as `true` if the operation ran with
  write concern or `false` if write concern was disabled

## Access Control

On deployments running with `authorization`, the
user must have access that includes the following privileges:

- `update` action on the specified collection(s).

- `find` action on the specified collection(s).

- `insert` action on the specified collection(s) if the
  operation results in an upsert.

The built-in role `readWrite` provides the required
privileges.

## Behavior

### Updates a Single Document

`db.collection.updateOne()` finds the first document that
matches the filter and applies the specified
update modifications.

### Update with an Update Operator Expressions Document

For the update specifications, the
`db.collection.updateOne()` method can accept a document that
only contains update operator expressions.

For example:

```javascript
db.collection.updateOne( 
   <query>,
   { $set: { status: "D" }, $inc: { quantity: 2 } },
   ...
)
```

### Update with an Aggregation Pipeline

The `db.collection.updateOne()` method can accept an 
aggregation pipeline 
`[ <stage1>, <stage2>, ... ]` that specifies the modifications to perform. 
The pipeline can consist of the following stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`

Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

For example:

```javascript
db.collection.updateOne( 
   <query>,
   [ 
      { $set: { status: "Modified", comments: [ "$misc1", "$misc2" ] } }, 
      { $unset: [ "misc1", "misc2" ] } 
   ]
   ...
)
```

**Note:**

In this pipeline, `$set` and `$unset` are aggregation stages, as
opposed to update operators. The aggregation stages `$set` and
`$unset` add new fields to documents and do not modify
existing field values.

For more information on the update operators, see `$set` and
`$unset`.

For examples, see updateOne-example-agg.

### Upsert

- If `upsert: true` and no documents match the `filter`,
  `db.collection.updateOne()` creates a new 
  document based on the `filter` criteria and `update` 
  modifications. See updateOne-example-update-with-upsert.
  
- For additional `db.collection.updateOne()` behavior on a 
  sharded collection, see updateOne-sharded-collection.

### Capped Collection

If an update operation changes the document size, the operation will fail.

### Sharded Collections

#### `upsert` on a Sharded Collection

To use `db.collection.updateOne()` on a sharded collection:

- If you don't specify `upsert: true`, you must include an exact
  match on the `_id` field or target a single shard (such as by
  including the shard key in the filter).

- If you specify `upsert: true`, the filter
  must include the shard key.

However, documents in a sharded collection can be
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
`db.collection.updateOne()`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write. 

- You must include an equality filter on the full shard key.

See also updateOne-sharded-upsert.

#### Missing Shard Key

- Starting in version 7.1, you do not need to provide the shard key 
  or `_id` field in the query specification. 

- Documents in a sharded collection can be
  missing the shard key fields. To use
  `db.collection.updateOne()` to set a **missing** shard key, 
  you must run on a `mongos`. Do not issue 
  the operation directly on the shard.

In addition, the following requirements also apply:

* - Task

  - Requirements

* - To set to `null`

  - - Requires equality filter on the full shard key if
      `upsert: true`.

* - To set to a non-`null` value

  - - Must be performed either inside a
      transaction or as a
      retryable write.

    - Requires equality filter on the full shard key if ``upsert:
      true``.

**Tip:**

Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.

See also:

- updateOne-sharded-upsert

- shard-key-missing

### Explainability

`updateOne()` is not compatible with
`db.collection.explain()`.

### Transactions

`db.collection.updateOne()` can be used inside distributed transactions.

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
production-considerations.

#### Upsert within Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

`db.collection.updateOne()` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Oplog Entries

If a `db.collection.updateOne()` operation successfully updates a
document, the operation adds an entry on the oplog (operations
log). If the operation fails or does not find a document to update, the
operation does not add an entry on the oplog. 

## Examples

### Update using Update Operator Expressions

The `restaurant` collection contains the following documents:

```javascript
db.restaurant.insertMany( [
   { _id: 1, name: "Central Perk Cafe", Borough: "Manhattan" },
   { _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
   { _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 0 }
] )
```

The following operation sets the `violations` field on the document
where `name` is `Central Perk Cafe`:

```javascript
try {
   db.restaurant.updateOne( 
      { "name" : "Central Perk Cafe" }, 
      { $set: { "violations" : 3 } } 
   );
} catch (e) {
   print(e);
}
```

  
The operation returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

If no matches were found, the operation instead returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
```

Setting `upsert: true` would insert the document if no match was found. See 
updateOne-example-update-with-upsert

### Update with Aggregation Pipeline

`db.collection.updateOne()` can use an aggregation pipeline to express
a more complex update, such as a conditional update based on current
field values. For the supported pipeline stages, see
updateOne-behavior-aggregation-pipeline.

#### Example 1

The following examples uses the aggregation pipeline to modify a field
using the values of the other fields in the document.

Create a `students` collection with the following documents:

```javascript
db.students.insertMany( [
   { _id: 1, student: "Skye", points: 75, commentsSemester1: "great at math", commentsSemester2: "loses temper", lastUpdate: ISODate("2019-01-01T00:00:00Z") },
   { _id: 2, student: "Elizabeth", points: 60, commentsSemester1: "well behaved", commentsSemester2: "needs improvement", lastUpdate: ISODate("2019-01-01T00:00:00Z") }
] )
```

Assume that instead of separate `commentsSemester1` and `commentsSemester2` 
fields in the first document, you want to gather these into a `comments` field,
like the second document. The following update operation uses an
aggregation pipeline to:

- add the new `comments` field and set the `lastUpdate` field.

- remove the `commentsSemester1` and `commentsSemester2` fields for all 
  documents in the collection.

Make sure that the filter in the update command targets a unique document. The
field `id` in the code below is an example of such a filter: 

```javascript
db.students.updateOne(
   { _id: 1 },
   [
      { $set: { status: "Modified", comments: [ "$commentsSemester1", "$commentsSemester2" ], lastUpdate: "$$NOW" } },
      { $unset: [ "commentsSemester1", "commentsSemester2" ] }
   ]
)
```

**Note:**

In this pipeline, `$set` and `$unset` are aggregation stages, as
opposed to update operators. The aggregation stages `$set` and
`$unset` add new fields to documents and do not modify
existing field values.

For more information on the update operators, see `$set` and
`$unset`.

First Stage
   The `$set` stage:
   
   - creates a new array field `comments` whose elements are the current
     content of the `commentsSemester1` and `commentsSemester2`
     fields and

   - sets the field `lastUpdate` to the value of the aggregation
     variable `NOW`. The aggregation variable
     `NOW` resolves to the current datetime value and remains
     the same throughout the pipeline. To access aggregation
     variables, prefix the variable with double dollar signs `$$`
     and enclose in quotes.
   

Second Stage
   The `$unset` stage removes the `commentsSemester1` and 
   `commentsSemester2` fields.

After the command, the collection contains the following documents:

```javascript
{ _id: 2, student: "Elizabeth", status: "Modified", points: 60, lastUpdate: ISODate("2020-01-23T05:11:45.784Z"), comments: [ "well behaved", "needs improvement" ] }
{ _id: 1, student: 'Skye', points: 75, commentsSemester1: 'great at math', commentsSemester2: 'loses temper', lastUpdate: ISODate("2019-01-01T00:00:00.000Z") }
```

#### Example 2

The aggregation pipeline allows the update to perform conditional
updates based on the current field values and use current field
values to calculate a separate field value.

For example, create a `students3` collection with the following documents:

```javascript
db.students3.insertMany( [
   { _id: 1, tests: [ 95, 92, 90 ], average: 92, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") },
   { _id: 2, tests: [ 94, 88, 90 ], average: 91, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") },
   { _id: 3, tests: [ 70, 75, 82 ], lastUpdate: ISODate("2019-01-01T00:00:00Z") }
] )
```

The third document `_id: 3` is missing the `average` and `grade`
fields. Using an aggregation pipeline, you can update the document with
the calculated grade average and letter grade.

```javascript
db.students3.updateOne(
   { _id: 3 },
   [
     { $set: { average: { $trunc: [  { $avg: "$tests" }, 0 ] }, lastUpdate: "$$NOW" } },
     { $set: { grade: { $switch: {
                           branches: [
                               { case: { $gte: [ "$average", 90 ] }, then: "A" },
                               { case: { $gte: [ "$average", 80 ] }, then: "B" },
                               { case: { $gte: [ "$average", 70 ] }, then: "C" },
                               { case: { $gte: [ "$average", 60 ] }, then: "D" }
                           ],
                           default: "F"
     } } } }
   ]
)
```

**Note:**

The `$set` used in the pipeline refers to the aggregation stage
`$set`, and not the update operators `$set`.

First Stage
   The `$set` stage:
   
   - calculates a new field `average` based on the average of the
     `tests` field. See `$avg` for more information on the
     `$avg` aggregation operator and `$trunc` for more
     information on the `$trunc` truncate aggregation operator.
     
   - sets the field `lastUpdate` to the value of the aggregation
     variable `NOW`. The aggregation variable
     `NOW` resolves to the current datetime value and remains
     the same throughout the pipeline. To access aggregation
     variables, prefix the variable with double dollar signs `$$`
     and enclose in quotes.

Second Stage
   The `$set` stage calculates a new field `grade` based on
   the `average` field calculated in the previous stage. See
   `$switch` for more information on the `$switch`
   aggregation operator.

After the command, the collection contains the following documents:

```javascript
{ _id: 1, tests: [ 95, 92, 90 ], average: 92, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") }
{ _id: 2, tests: [ 94, 88, 90 ], average: 91, grade: "A", lastUpdate: ISODate("2020-01-23T05:18:40.013Z") }
{ _id: 3, tests: [ 70, 75, 82 ], lastUpdate: ISODate("2020-01-24T17:33:30.674Z"), average: 75, grade: "C" }
```

**See also:**

/tutorial/update-documents-with-aggregation-pipeline

### Update with Upsert

The `restaurant` collection contains the following documents:

```javascript
db.restaurant.insertMany( [
   { _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },
   { _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
   { _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: "0" }
] )
```

The following operation attempts to update the document with 
`name : "Pizza Rat's Pizzaria"`, while `upsert: true` :

```javascript
try {
   db.restaurant.updateOne( 
      { "name" : "Pizza Rat's Pizzaria" },
      { $set: {"_id" : 4, "violations" : 7, "borough" : "Manhattan" } }, 
      { upsert: true }
   );
} catch (e) {
   print(e);
}
```

Since `upsert:true` the document is `inserted` based on the `filter` and 
`update` criteria. The operation returns:

```javascript
{
   "acknowledged" : true,
   "matchedCount" : 0,
   "modifiedCount" : 0,
   "upsertedId" : 4,
   "upsertedCount": 1
}
```

The collection now contains the following documents:

```javascript
{ _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },
{ _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
{ _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 4 },
{ _id: 4, name: "Pizza Rat's Pizzaria", Borough: "Manhattan", violations: 7 }
```

The `name` field was filled in using the `filter` criteria, while the 
`update` operators were used to create the rest of the document.

The following operation updates the first document with `violations` that 
are greater than `10`:

```javascript
try {
   db.restaurant.updateOne( 
      { "violations" : { $gt: 10} }, 
      { $set: { "Closed" : true } }, 
      { upsert: true }
   );
} catch (e) {
   print(e);
}
```

The operation returns:

```javascript
{
   "acknowledged" : true,
   "matchedCount" : 0,
   "modifiedCount" : 0,
   "upsertedId" : ObjectId("56310c3c0c5cbb6031cafaea")
}
```

The collection now contains the following documents:

```javascript
{ _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },
{ _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
{ _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 4 },
{ _id: 4, name: "Pizza Rat's Pizzaria", Borough: "Manhattan", violations: 7 }
{ _id: ObjectId("56310c3c0c5cbb6031cafaea"), Closed: true }
```

Since no documents matched the filter, and `upsert` was `true`, 
`updateOne` inserted the document with a generated 
`_id` and the `update` criteria only.

### Update with Write Concern

Given a three member replica set, the following operation specifies a 
`w` of `majority`, `wtimeout` of `100`:

```javascript
try {
   db.restaurant.updateOne(
       { "name" : "Pizza Rat's Pizzaria" },
       { $inc: { "violations" : 3}, $set: { "Closed" : true } },
       { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print(e);
}
```

If the primary and at least one secondary acknowledge each write operation 
within 100 milliseconds, it returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

If the acknowledgment takes longer than the `wtimeout` limit, the following 
exception is thrown:

```javascript
WriteConcernError({
   "code" : 64,
   "errmsg" : "waiting for replication timed out",
   "errInfo" : {
     "wtimeout" : true,
     "writeConcern" : {
       "w" : "majority",
       "wtimeout" : 100,
       "provenance" : "getLastErrorDefaults"
     }
   }
})
```

The following table explains the possible values of
`errInfo.writeConcern.provenance`:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

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
db.myColl.updateOne(
   { category: "cafe" },
   { $set: { status: "Updated" } },
   { collation: { locale: "fr", strength: 1 } }
);
```

### Specify `arrayFilters` for an Array Update Operations

When updating an array field, you can specify `arrayFilters` that 
determine which array elements to update.

#### Update Elements Match `arrayFilters` Criteria

Create a collection `students` with the following documents:

```javascript
db.students.insertMany( [
   { _id: 1, grades: [ 95, 92, 90 ] },
   { _id: 2, grades: [ 98, 100, 102 ] },
   { _id: 3, grades: [ 95, 110, 100 ] }
] )
```

To modify all elements that are greater than or equal to `100` in the
`grades` array, use the filtered positional operator
`$[<identifier>]` with the `arrayFilters` option in the
`db.collection.updateOne` method:

```javascript
db.students.updateOne(
   { grades: { $gte: 100 } },
   { $set: { "grades.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

The operation updates the `grades` field of a single document, and
after the operation, the collection has the following documents:

```javascript
{ _id: 1, grades: [ 95, 92, 90 ] }
{ _id: 2, grades: [ 98, 100, 100 ] }
{ _id: 3, grades: [ 95, 110, 100 ] }
```

#### Update Specific Elements of an Array of Documents

Create a collection `students2` with the following documents:

```javascript
db.students2.insertMany( [
   {
      _id: 1,
      grades: [
         { grade: 80, mean: 75, std: 6 },
         { grade: 85, mean: 90, std: 4 },
         { grade: 85, mean: 85, std: 6 }
      ]
   },
   {
      _id: 2,
      grades: [
         { grade: 90, mean: 75, std: 6 },
         { grade: 87, mean: 90, std: 3 },
         { grade: 85, mean: 85, std: 4 }
      ]
   }
] )
```

To modify the value of the `mean` field for all elements in the
`grades` array where the grade is greater than or equal to `85`,
use the filtered positional operator `$[<identifier>]` with
the `arrayFilters` in the `db.collection.updateOne` method:

```javascript
db.students2.updateOne(
   { },
   { $set: { "grades.$[elem].mean" : 100 } },
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)
```

The operation updates the array of a single document, and after the
operation, the collection has the following documents:

```javascript
{
   _id: 1,
   grades: [
      { grade: 80, mean: 75, std: 6 },
      { grade: 85, mean: 100, std: 4 },
      { grade: 85, mean: 100, std: 6 } 
    ]
}
{
   _id: 2,
   grades: [
      { grade: 90, mean: 75, std: 6 },
      { grade: 87, mean: 90, std: 3 },
      { grade: 85, mean: 85, std: 4 }
   ]
}
```

### Specify `hint` for Update Operations

Create a sample `students` collection with the following documents:

```javascript
db.students.insertMany( [
   { _id: 1, student: "Richard", grade: "F", points:  0,  comments1: null, comments2: null },
   { _id: 2, student: "Jane", grade: "A", points: 60,  comments1: "well behaved", comments2: "fantastic student" },
   { _id: 3, student: "Ronan", grade: "F", points:  0,  comments1: null, comments2: null },
   { _id: 4, student: "Noah", grade: "D", points: 20,  comments1: "needs improvement", comments2: null },
   { _id: 5, student: "Adam", grade: "F", points:  0,  comments1: null, comments2: null },
   { _id: 6, student: "Henry", grade: "A", points: 86,  comments1: "fantastic student", comments2: "well behaved" }
] )
```

Create the following indexes on the collection:

```javascript
db.students.createIndex( { grade: 1 } )
db.students.createIndex( { points: 1 } )
```

The following update operation explicitly hints to use the index ``{
grade: 1 }``:

**Note:**

If you specify an index that does not exist, the operation errors.

```javascript
db.students.updateOne(
   { "points": { $lte: 20 }, "grade": "F" }, 
   { $set: { "comments1": "failed class" } },
   { hint: { grade: 1 } }
)
```

The update command returns the following:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

**Note:**

Even though 3 documents match the criteria of the update, `updateOne` only
modifies the first document it finds. Therefore, even though the students 
Richard, Ronan, and Adam all meet the criteria, only Richard is updated.

To see the index used, run `explain` on the operation:

```javascript
db.students.explain().update(
   { "points": { $lte: 20 }, "grade": "F" },
   { $set: { "comments1": "failed class" } },
   { multi: true, hint: { grade: 1 } }
)
```

### Write Concern Errors in Sharded Clusters

**Changed in version:** 8.1.2

When `db.collection.updateOne()` executes on `mongos` in a sharded cluster, a `writeConcernError` is 
always reported in the response, even when one or more other errors occur. 
In previous releases, other errors sometimes caused `db.collection.updateOne()` to not report write concern errors.

For example, if a document fails validation, triggering a `DocumentValidationFailed` error,
and a write concern error also occurs, both the `DocumentValidationFailed` error and the 
`writeConcernError` are returned in the top-level field of the response.

### User Roles and Document Updates

Starting in MongoDB 7.0, you can use the new `USER_ROLES`
system variable to return user roles.

The example in this section shows updates to fields in a collection
containing medical information. The example reads the current user roles
from the `USER_ROLES` system variable and only performs the updates if
the user has a specific role.

To use a system variable, add `$$` to the start of the variable name.
Specify the `USER_ROLES` system variable as `$$USER_ROLES`.

The example creates these users:

- `James` with a `Billing` role.
- `Michelle` with a `Provider` role.

Perform the following steps to create the roles, users, and collection:

**Step 1: Create the roles**

Create roles named `Billing` and `Provider` with the required
privileges and resources.

Run:

```javascript
db.createRole( { role: "Billing", privileges: [ { resource: { db: "test",
   collection: "medicalView" }, actions: [ "find" ] } ], roles: [ ] } )
db.createRole( { role: "Provider", privileges: [ { resource: { db: "test",
   collection: "medicalView" }, actions: [ "find" ] } ], roles: [ ] } )
```

**Step 2: Create the users**

Create users named `James` and `Michelle` with the required
roles.

```javascript
db.createUser( {
   user: "James",
   pwd: "js008",
   roles: [
      { role: "Billing", db: "test" }
   ]
} )

db.createUser( {
   user: "Michelle",
   pwd: "me009",
   roles: [
      { role: "Provider", db: "test" }
   ]
} )
```

**Step 3: Create the collection**

Run:

```javascript
db.medical.insertMany( [
   {
      _id: 0,
      patientName: "Jack Jones",
      diagnosisCode: "CAS 17",
      creditCard: "1234-5678-9012-3456"
   },
   {
      _id: 1,
      patientName: "Mary Smith",
      diagnosisCode: "ACH 01",
      creditCard: "6541-7534-9637-3456"
   }
] )
```

Log in as as `Michelle`, who has the `Provider` role, and perform an
update:

**Step 1: Log in as `Michelle`**

Run:

```javascript
db.auth( "Michelle", "me009" )
```

**Step 2: Perform update**

Run:

```javascript
// Attempt to update one document
db.medical.updateOne( {
   // User must have the Provider role to perform the update
   $expr: { $ne: [
      { $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 01"} }
)
```

The previous example uses `$setIntersection` to return
documents where the intersection between the `"Provider"` string and
the user roles from `$$USER_ROLES.role` is not empty. `Michelle` has
the `Provider` role, so the update is performed.

Next, log in as as `James`, who does not have the `Provider` role,
and attempt to perform the same update:

**Step 1: Log in as `James`**

Run:

```javascript
db.auth( "James", "js008" )
```

**Step 2: Attempt to perform update**

Run:

```javascript
// Attempt to update one document
db.medical.updateOne( {
   // User must have the Provider role to perform the update
   $expr: { $ne: [
      { $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 01"} }
)
```

The previous example does not update any documents.

**See also:**

To update multiple documents, see
`db.collection.updateMany()`.
