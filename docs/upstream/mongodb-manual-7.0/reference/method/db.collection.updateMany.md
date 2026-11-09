<!-- Converted from reference/method/db.collection.updateMany.txt (reStructuredText). Includes are inlined. -->

# db.collection.updateMany() (mongosh method)

(Include not available offline: includes/wayfinding/mongosh-method-updateMany.rst)

## Definition

**`db.collection.updateMany(filter, update, options)`**

Updates all documents that match the specified filter for a
collection.

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
     let: <document>,
     maxTimeMS: <int>,
     bypassDocumentValidation: <boolean>
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

    - .. _update-many-method-update-document:

      Update document:

      Contains only update operator expressions.

      For more information, see
      updateMany-behavior-update-expressions

    - .. _update-many-method-agg-pipeline:

      Aggregation pipeline:

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

  - .. _update-many-arrayFilters:

    Optional. An array of filter documents that determine which array elements to
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

* - let
  - Document
  - .. _updateMany-let:

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
  - .. _updateMany-maxTimeMS:

    Optional. Specifies the time limit in milliseconds for the
    update operation to run before timing out.

* - bypassDocumentValidation
  - boolean
  - .. _updateMany-bypassDocumentValidation:

    Optional. Enables `insert` to bypass schema validation
    during the operation. This lets you insert documents that do not
    meet the validation requirements.

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
include the full shard key in the `filter`. For information about
`db.collection.updateMany()` behavior in sharded collections, see
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
production-considerations.

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

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Idempotent Updates

The `sample_mflix.movies` collection contains movies with IMDB ratings. 
This idempotent update does the following operations:

- matches all movies with IMDB ratings less than 3.0
- increments those ratings by 0.5
- sets a `ratingBoosted` field to `true`

```javascript
db.movies.updateMany(
   { "imdb.rating": { $lt: 3, $type: "number" }, ratingBoosted: { $ne: true } },
   { $inc: { "imdb.rating": 0.5 }, $set: { ratingBoosted: true } }
)
```

`updateMany()` modifies the matching movie documents individually. The 
individual document updates are atomic operations, but the `updateMany()` 
operation as a whole is not atomic.

If the operation fails to update all matched documents, you can safely rerun 
an idempotent command until no additional documents match the specified filter. 
In this case, each document's `imdb.rating` field is only updated one time 
regardless of how many times it is retried because the command is idempotent.

### Update Multiple Documents

The `sample_mflix.movies` collection contains movies with a
`num_mflix_comments` field.

The following operation finds all movies with more than 100 comments and adds a
`popular` flag to those movies:

```javascript
db.movies.updateMany( 
   { num_mflix_comments: { $gt: 100 } }, 
   { $set: { "popular" : true } } 
)
```

### Update with Aggregation Pipeline

`db.collection.updateMany()` can use an aggregation pipeline to express
a more complex update, such as a conditional update based on current
field values. For the supported pipeline stages, see
updateMany-behavior-aggregation-pipeline.

#### Example 1: Update with Aggregation Pipeline Using Existing Fields

The following example uses the aggregation pipeline to modify a field
using the values of the other fields in the document.

This pipeline: 
   
- combines the IMDB and Tomatoes viewer ratings into a new `combinedRatings` array field
- sets the `ratingsUpdated` field
- removes the original `imdb.rating` and `tomatoes.viewer.rating` fields for all 
  matching documents

```javascript
db.movies.updateMany(
   { year: { $gte: 2010, $lte: 2019 } },
   [
      { $set: { 
         combinedRatings: [ "$imdb.rating", "$tomatoes.viewer.rating" ], 
         ratingsUpdated: "$$NOW" 
      } },
      { $unset: [ "imdb.rating", "tomatoes.viewer.rating" ] }
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

   - creates a new array field `combinedRatings` whose elements are the current
     content of the `imdb.rating` and `tomatoes.viewer.rating` fields 

   - sets the field `ratingsUpdated` to the value of the aggregation
     variable `NOW`.

Second Stage
   The `$unset` stage removes the `imdb.rating` and 
   `tomatoes.viewer.rating` fields.

After the command, matching movies from the 2010s have a `combinedRatings`
array with both rating values and a timestamp.
   

#### Example 2: Update with Aggregation Pipeline Using Existing Fields Conditionally

Using an aggregation pipeline, you can update movies from the 2010s with a
calculated combined rating score (averaging IMDB and Tomatoes viewer ratings)
and assign a letter grade based on that score.

```javascript
db.movies.updateMany(
   { 
      year: { $gte: 2010, $lte: 2019 },
      "imdb.rating": { $exists: true },
      "tomatoes.viewer.rating": { $exists: true }
   },
   [
     { $set: { 
        combinedScore: { $trunc: [ 
           { $avg: [ "$imdb.rating", "$tomatoes.viewer.rating" ] }, 
           1 
        ] },
        scoreUpdated: "$$NOW" 
     } },
     { $set: { 
        ratingGrade: { $switch: {
           branches: [
              { case: { $gte: [ "$combinedScore", 8 ] }, then: "A" },
              { case: { $gte: [ "$combinedScore", 6 ] }, then: "B" },
              { case: { $gte: [ "$combinedScore", 4 ] }, then: "C" },
              { case: { $gte: [ "$combinedScore", 2 ] }, then: "D" }
           ],
           default: "F"
        } } 
     } }
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

   - calculates a new field `combinedScore` based on the average of the
     `imdb.rating` and `tomatoes.viewer.rating` fields. See `$avg` 
     for more information on the `$avg` aggregation operator and 
     `$trunc` for more information on the `$trunc` truncate 
     aggregation operator.
     
   - sets the field `scoreUpdated` to the value of the aggregation
     variable `NOW`.
   

Second Stage
   The `$set` stage calculates a new field `ratingGrade` based on
   the `combinedScore` field calculated in the previous stage. See
   `$switch` for more information on the `$switch`
   aggregation operator.

After the command, matching movies have a combined score and letter grade.
      

**See also:**

/tutorial/update-documents-with-aggregation-pipeline

### Update Multiple Documents with Upsert

The following operation updates all movies released after 2020 and
directed by Christopher Nolan:

```javascript
db.movies.updateMany(
   { 
      year: { $gt: 2020 }, 
      directors: "Christopher Nolan" 
   },
   { $set: { "upcomingRelease": true } },
   { upsert: true }
)
```

In this example, since no documents match the filter, and `upsert` is
`true`, `updateMany` inserts a new document with a
generated `_id` and the equality conditions from the `filter`, and
the `update` modifiers.

### Update with Write Concern

Given a three member replica set, the following operation specifies a 
`w` of `majority` and `wtimeout` of `100`:

```javascript
db.movies.updateMany(
    { title: "The Godfather" },
    { $inc: { num_mflix_comments: 10 }, $set: { trending: true } },
    { w: "majority", wtimeout: 100 }
)
```

If the acknowledgment takes longer than the `wtimeout` limit, MongoDB throws
an exception. 

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

The following operation uses a case-insensitive collation to match
movies with the genre "drama" with any combination of lowercase and uppercase. 

```javascript
db.movies.updateMany(
   { genres: "drama" },
   { $set: { genreNormalized: true } },
   { collation: { locale: "en", strength: 1 } }
)
```

### Specify `arrayFilters` for an Array Update Operations

When updating an array field, you can specify `arrayFilters` that 
determine which array elements to update.

#### Update Elements Match `arrayFilters` Criteria

Add a `ratings` array to some movies by combining their various
rating scores:

```javascript
db.movies.updateMany(
   { 
      "imdb.rating": { $exists: true },
      "tomatoes.viewer.rating": { $exists: true },
      "tomatoes.critic.rating": { $exists: true },
      year: { $gte: 2010, $lte: 2015 }
   },
   [
      { $set: { 
         ratings: [
            { $multiply: ["$imdb.rating", 10] },
            { $multiply: ["$tomatoes.viewer.rating", 10] },
            { $multiply: ["$tomatoes.critic.rating", 10] }
         ]
      } }
   ]
)
```

To update all ratings that are greater than or equal to `100` in the
`ratings` array, use the filtered positional operator
`$[<identifier>]` with the `arrayFilters` option:

```javascript
db.movies.updateMany(
   { ratings: { $gte: 100 } },
   { $set: { "ratings.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

After the operation, all rating values greater than or equal to 100
in the `ratings` arrays are set to 100.

#### Update Specific Elements of an Array of Documents

Add a `ratingDetails` array to movies with individual rating sources:

```javascript
db.movies.updateMany(
   { 
      "imdb.rating": { $exists: true },
      "tomatoes.viewer.rating": { $exists: true },
      year: { $gte: 2010, $lte: 2012 }
   },
   [
      { $set: { 
         ratingDetails: [
            { source: "imdb", score: "$imdb.rating", weight: 10 },
            { source: "tomatoes_viewer", score: "$tomatoes.viewer.rating", weight: 8 },
            { source: "tomatoes_critic", score: "$tomatoes.critic.rating", weight: 7 }
         ]
      } }
   ]
)
```

To modify the value of the `weight` field to 10 for all elements in the
`ratingDetails` array where the score is greater than or equal to `8`,
use the filtered positional operator `$[<identifier>]` with
`arrayFilters`:

```javascript
db.movies.updateMany(
   { ratingDetails: { $exists: true } },
   { $set: { "ratingDetails.$[elem].weight" : 10 } },
   { arrayFilters: [ { "elem.score": { $gte: 8 } } ] }
)
```

After the operation, all rating sources with scores less than or equal to 8 have their weight set to 10.

### Specify `hint` for Update Operations

Create the following index on the collection:

```javascript
db.movies.createIndex( { rated: 1 } )
```

The following update operation explicitly hints to use the index ``{
rated: 1 }``:

**Note:**

If you specify an index that does not exist, the operation errors.

```javascript
db.movies.updateMany(
   { "num_mflix_comments": { $lte: 5 }, "rated": "G" }, 
   { $set: { "familyFriendly": true } },
   { hint: { rated: 1 } }
)
```

To see if the hinted index is used, run the `$indexStats` pipeline:

```javascript
db.movies.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } }, { $match: {key: { rated: 1 } } } ] )
```

### Write Concern Errors in Sharded Clusters

**Changed in version:** 8.1.2

When `db.collection.updateMany()` executes on `mongos` in a sharded cluster, a `writeConcernError` is 
always reported in the response, even when one or more other errors occur. 
In previous releases, other errors sometimes caused `db.collection.updateMany()` to not report write concern errors.

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
// Attempt to update many documents
db.medical.updateMany(
   // User must have the Provider role to perform the update
   { $expr: { $ne: [ {
      $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 02"} }
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
// Attempt to update many documents
db.medical.updateMany(
   // User must have the Provider role to perform the update
   { $expr: { $ne: [ {
      $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 02"} }
)
```

The previous example does not update any documents.
