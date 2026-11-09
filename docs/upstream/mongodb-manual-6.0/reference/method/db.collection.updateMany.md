<!-- Converted from reference/method/db.collection.updateMany.txt (reStructuredText). Includes are inlined. -->

# db.collection.updateMany()

(Include not available offline: includes/wayfinding/mongosh-method-updateMany.rst)

## Definition

**`db.collection.updateMany(filter, update, options)`**

Updates all documents that match the specified filter for a
collection.

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

The `updateMany()` method has the following form:

```javascript
db.collection.updateMany(
   <filter>,
   <update>,
   {
     upsert: <boolean>,
     writeConcern: <document>,
     collation: <document>,
     arrayFilters: [ <filterdocument1>, ... ],
     hint:  <document|string>,
     let: <document>
   }
)
```

### Parameters

The `updateMany()` method takes the following
parameters:

* - Parameter

  - Type

  - Description

* - filter

  - document

  - .. _update-many-filter:

    The selection criteria for the update. The same query
    selectors as in the `find()` method are available.

    Specify an empty document `{ }` to update all documents in 
    the collection.

* - update

  - document or pipeline

  - .. _update-many-update:

    The modifications to apply. Can be one of the following:

    * - Update document

      - .. _update-many-method-update-document:

        Contains only update operator expressions.

        For more information, see
        updateMany-behavior-update-expressions

    * - Aggregation pipeline

      - .. _update-many-method-agg-pipeline:

        Contains only the following aggregation stages:

        - `$addFields` and its alias `$set`

        - `$project` and its alias `$unset`

        - `$replaceRoot` and its alias `$replaceWith`

        For more information, see
        updateMany-behavior-aggregation-pipeline.

    To update with a replacement document, see
    `db.collection.replaceOne()`.

* - `upsert`

  - boolean

  - .. include:: /includes/extracts/updateMany-behavior-method.rst

* - `writeConcern`

  - document

  - Optional. A document expressing the write concern. Omit to use the default write concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

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

    For examples, see updateMany-arrayFilters.

* - hint 

  - Document or string

  - .. _update-many-hint:

    Optional. A document or string that specifies the index to use to support the query predicate.

    The option can take an index specification document or the index
    name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-update-many-hint.

* - `let`

  - Document

  - .. _updateMany-let-syntax:

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

### Returns

The method returns a document that contains:
      
- A boolean `acknowledged` as `true` if the operation ran with 
  write concern or `false` if write concern was disabled
 
- `matchedCount` containing the number of matched documents

- `modifiedCount` containing the number of modified documents

- `upsertedId` containing the `_id` for the upserted document

- `upsertedCount` containing the number of upserted documents

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

`updateMany()` finds all documents in the collection that match the 
`filter` and applies modifications specified by the `update` 
parameter.

`updateMany()` modifies each document individually. Each 
document write is an atomic operation, but `updateMany()` 
as a whole is *not* atomic. If your use case requires atomicity of 
writes to multiple documents, use transactions.

If a single document update fails, all document updates written before 
the failure are retained, but any remaining matching documents are *not* 
updated. For details on this behavior, see multi-update-failures.

**See also:**

updateMany-sharded-collection for more information about 
`updateMany()` behavior in sharded collections.

### Limitations

- `updateMany()` should only be used for idempotent 
  operations.

### Upsert

If `upsert: true` and no documents match the `filter`, 
`db.collection.updateMany()` creates a new 
document based on the `filter` and `update` parameters.

If you specify `upsert: true` on a sharded collection, you must
include the full shard key in the `filter`. For additional
`db.collection.updateMany()` behavior, see
updateMany-sharded-collection.

See 
updateMany-example-update-multiple-documents-with-upsert.

### Update with an Update Operator Expressions Document

For the modification specification, the
`db.collection.updateMany()` method can accept a document that
only contains update operator expressions to
perform.

For example:

```javascript
db.collection.updateMany( 
   <query>,
   { $set: { status: "D" }, $inc: { quantity: 2 } },
   ...
)
```

### Update with an Aggregation Pipeline

The `db.collection.updateMany()` method can accept an 
aggregation pipeline 
`[ <stage1>, <stage2>, ... ]` that specifies the modifications to 
perform. The pipeline can consist of the following stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`

Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

For example:

```javascript
db.collection.updateMany( 
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

For examples, see updateMany-example-agg.

### Capped Collections

If an update operation changes the document size, the operation will fail.

### Time Series Collections

The `updateMany()` method is available for
time series collections starting in
MongoDB 5.1. 

Update commands must meet the following requirements:

- You can only match on the `metaField` field value.
- You can only modify the `metaField` field value.
- Your update document can only contain update operator expressions.
- Your update command must not limit the number of documents to be
  updated. Set `multi: true` or use the
  `updateMany()` method. 
- Your update command must not set upsert: true.

### Sharded Collections

`updateMany()` exhibits the following behaviors when used with 
sharded collections:

- `updateMany()` operations that include `upsert: true` must 
  include the full shard key in the `filter`.

- If you attempt to run `updateMany()` during a 
  sharding-chunk-migration or a 
  shard key value update, the operation can 
  miss documents in some scenarios. To ensure all documents are updated, 
  use idempotent updates and rerun the command until no further updates 
  are applied. For more information on idempotent updates with 
  `updateMany()`, see updateMany-example-idempotent.

- If `updateMany()` is run outside a transaction, operations that target more 
  than one shard broadcast the operation to all shards in the cluster. 

- If `updateMany()` is run inside a transaction, operations that target more
  than one shard only target the relevant shards.

### Explainability

`updateMany()` is not compatible with
`db.collection.explain()`.

### Transactions

`db.collection.updateMany()` can be used inside distributed transactions.

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

`db.collection.updateMany()` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Oplog Entries

`updateMany()` adds an entry to the oplog (operations log) 
for each successfully updated document. If no documents are updated,
`updateMany()` does not add entries to the oplog.

## Examples

### Idempotent Updates

The following example demonstrates an idempotent update with
`updateMany()`:

A company is giving a $1,000 raise to all employees earning less than 
$100,000.

Consider an `employees` collection with the following documents:

```javascript
db.employees.insertMany( [
   { _id: 1, name: "Rob", salary: 37000 },
   { _id: 2, name: "Trish", salary: 65000 },
   { _id: 3, name: "Zeke", salary: 99999 },
   { _id: 4, name: "Mary", salary: 200000 }
] )
```

The following command matches all employees who earn less than 
$100,000 and have not received a raise, increments those salaries 
by $1,000, and sets `raiseApplied` to true:

```javascript
db.employees.updateMany(
   { salary: { $lt: 100000 }, raiseApplied: { $ne: true } },
   { $inc: { salary: 1000 }, $set: { raiseApplied: true } }
)
```

`updateMany()` modifies the matching `employee` documents 
individually. The individual document updates are atomic operations, 
but the `updateMany()` operation as a whole is not atomic.

If the operation fails to update all matched documents, you can 
safely rerun an idempotent command until no additional documents 
match the specified filter. In this case, each document's `salary` 
field is only updated one time regardless of how many times it is 
retried because the command is idempotent.

After all eligible employees have received their raises, you can 
remove the `raiseApplied` field with the following command:

```javascript
db.employees.updateMany(
   { },
   { $unset: { raiseApplied: 1 } }
)
```

### Update Multiple Documents

The `restaurant` collection contains the  following documents:

```javascript
db.restaurant.insertMany( [
   { _id: 1, name: "Central Perk Cafe", violations: 3 },
   { _id: 2, name: "Rock A Feller Bar and Grill", violations: 2 },
   { _id: 3, name: "Empire State Sub", violations: 5 },
   { _id: 4, name: "Pizza Rat's Pizzaria", violations: 8 },
] )
```

The following operation updates all documents where `violations` are 
greater than `4` and `$set` a flag for review:

```javascript
try {
   db.restaurant.updateMany( 
      { violations: { $gt: 4 } }, 
      { $set: { "Review" : true } } 
   );
} catch (e) {
   print(e);
}
```

  
The operation returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
```

   
The collection now contains the following documents:

```javascript
{ _id: 1, name: "Central Perk Cafe", violations: 3 }
{ _id: 2, name: "Rock A Feller Bar and Grill", violations: 2 }
{ _id: 3, name: "Empire State Sub", violations: 5, Review: true }
{ _id: 4, name: "Pizza Rat's Pizzaria", violations: 8, Review: true }
```

If no matches were found, the operation instead returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
```

Setting `upsert: true` would insert a document if no match was found.

### Update with Aggregation Pipeline

The `db.collection.updateMany()` can use an aggregation pipeline for the 
update. The pipeline can consist of the following stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`

Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

#### Example 1: Update with Aggregation Pipeline Using Existing Fields

The following examples uses the aggregation pipeline to modify a field
using the values of the other fields in the document.

Create a `students` collection with the following documents:

```javascript
db.students.insertMany( [
   { _id: 1, student: "Skye", points: 75, commentsSemester1: "great at math", commentsSemester2: "loses temper", lastUpdate: ISODate("2019-01-01T00:00:00Z") },
   { _id: 2, students: "Elizabeth", points: 60, commentsSemester1: "well behaved", commentsSemester2: "needs improvement", lastUpdate: ISODate("2019-01-01T00:00:00Z") }
] )
```

Assume that instead of separate `commentsSemester1` and `commentsSemester2`
fields, you want to gather these into a new `comments` field. The following
update operation uses an aggregation pipeline to:
   
- add the new `comments` field and set the `lastUpdate` field.

- remove the `commentsSemester1` and `commentsSemester2` fields for all 
  documents in the collection.

```javascript
db.students.updateMany(
   { },
   [
      { $set: { comments: [ "$commentsSemester1", "$commentsSemester2" ], lastUpdate: "$$NOW" } },
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
     content of the `commentsSemester1` and `commentsSemester2` fields and 

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
{ _id: 1, student: "Skye", status: "Modified", points: 75, lastUpdate: ISODate("2020-01-23T05:11:45.784Z"), comments: [ "great at math", "loses temper" ] }
{ _id: 2, student: "Elizabeth", status: "Modified", points: 60, lastUpdate: ISODate("2020-01-23T05:11:45.784Z"), comments: [ "well behaved", "needs improvement" ] }
```

   

#### Example 2: Update with Aggregation Pipeline Using Existing Fields Conditionally

The aggregation pipeline allows the update to perform conditional
updates based on the current field values as well as use current field
values to calculate a separate field value.

For example, create a `students3` collection with the following documents:

```javascript
db.students3.insertMany( [
   { _id: 1, tests: [ 95, 92, 90 ], lastUpdate: ISODate("2019-01-01T00:00:00Z") },
   { _id: 2, tests: [ 94, 88, 90 ], lastUpdate: ISODate("2019-01-01T00:00:00Z") },
   { _id: 3, tests: [ 70, 75, 82 ], lastUpdate: ISODate("2019-01-01T00:00:00Z") }
] )
```

Using an aggregation pipeline, you can update the documents with the
calculated grade average and letter grade.

```javascript
db.students3.updateMany(
   { },
   [
     { $set: { average : { $trunc: [ { $avg: "$tests" }, 0 ] } , lastUpdate: "$$NOW" } },
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

In this pipeline, `$set` and `$unset` are aggregation stages, as
opposed to update operators. The aggregation stages `$set` and
`$unset` add new fields to documents and do not modify
existing field values.

For more information on the update operators, see `$set` and
`$unset`.

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
{ _id: 1, tests: [ 95, 92, 90 ], lastUpdate: ISODate("2020-01-24T17:31:01.670Z"), average: 92, grade: "A" }
{ _id: 2, tests: [ 94, 88, 90 ], lastUpdate: ISODate("2020-01-24T17:31:01.670Z"), average: 90, grade: "A" }
{ _id: 3, tests: [ 70, 75, 82 ], lastUpdate: ISODate("2020-01-24T17:31:01.670Z"), average: 75, grade: "C" }
```

      

**See also:**

/tutorial/update-documents-with-aggregation-pipeline

### Update Multiple Documents with Upsert

The `inspectors` collection contains the following documents:

```javascript
db.inspectors.insertMany( [
   { _id: 92412, inspector: "F. Drebin", Sector: 1, Patrolling: true },
   { _id: 92413, inspector: "J. Clouseau", Sector: 2, Patrolling: false },
   { _id: 92414, inspector: "J. Clouseau", Sector: 3, Patrolling: true },
   { _id: 92415, inspector: "R. Coltrane", Sector: 3, Patrolling: false }
] )
```

The following operation updates all documents with `Sector` greater
than 4 and `inspector` equal to `"R. Coltrane"`:

```javascript
try {
   db.inspectors.updateMany(
      { "Sector" : { $gt : 4 }, "inspector" : "R. Coltrane" },
      { $set: { "Patrolling" : false } },
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
   "upsertedId" : ObjectId("56fc5dcb39ee682bdc609b02"),
   "upsertedCount": 1
}
```

The collection now contains the following documents:

```javascript
{ _id: 92412, inspector: "F. Drebin", Sector: 1, Patrolling: true },
{ _id: 92413, inspector: "J. Clouseau", Sector: 2, Patrolling: false },
{ _id: 92414, inspector: "J. Clouseau", Sector: 3, Patrolling: true },
{ _id: 92415, inspector: "R. Coltrane", Sector: 3, Patrolling: false },
{ _id: ObjectId("56fc5dcb39ee682bdc609b02"), inspector: "R. Coltrane", Patrolling: false }
```

Since no documents matched the filter, and `upsert` was `true`,
`updateMany` inserted the document with a
generated `_id`, the equality conditions from the `filter`, and the
`update` modifiers.

### Update with Write Concern

Given a three member replica set, the following operation specifies a 
`w` of `majority` and `wtimeout` of `100`:

```javascript
try {
   db.restaurant.updateMany(
       { "name" : "Pizza Rat's Pizzaria" },
       { $inc: { "violations" : 3}, $set: { "Closed" : true } },
       { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print(e);
}
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
db.myColl.updateMany(
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

To update all elements that are greater than or equal to `100` in the
`grades` array, use the filtered positional operator
`$[<identifier>]` with the `arrayFilters` option:

```javascript
db.students.updateMany(
   { grades: { $gte: 100 } },
   { $set: { "grades.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

After the operation, the collection contains the following documents:

```javascript
{ _id: 1, grades: [ 95, 92, 90 ] }
{ _id: 2, grades: [ 98, 100, 100 ] }
{ _id: 3, grades: [ 95, 100, 100 ] }
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
the `arrayFilters`:

```javascript
db.students2.updateMany(
   { },
   { $set: { "grades.$[elem].mean" : 100 } },
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)
```

After the operation, the collection has the following documents:

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
      { grade: 90, mean: 100, std: 6 },
      { grade: 87, mean: 100, std: 3 },
      { grade: 85, mean: 100, std: 4 }
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
```

The following update operation explicitly hints to use the index ``{
grade: 1 }``:

**Note:**

If you specify an index that does not exist, the operation errors.

```javascript
db.students.updateMany(
   { "points": { $lte: 20 }, "grade": "F" }, 
   { $set: { "comments1": "failed class" } },
   { hint: { grade: 1 } }
)
```

The update command returns the following:

```javascript
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }
```

To see if the hinted index is used, run the `$indexStats` pipeline:

```javascript
db.students.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } }, { $match: {key: { grade: 1 } } } ] )
```
