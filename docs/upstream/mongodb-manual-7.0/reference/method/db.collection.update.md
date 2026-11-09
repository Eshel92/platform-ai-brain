<!-- Converted from reference/method/db.collection.update.txt (reStructuredText). Includes are inlined. -->

# db.collection.update() (mongosh method)

**Important:** Deprecated `mongosh` Method

This method is deprecated in `mongosh`. For alternative
methods, see compatibility.

## Definition

**`db.collection.update(query, update, options)`**

Modifies an existing document or documents in a collection. The
method can modify specific fields of an existing document or documents
or replace an existing document entirely, depending on the
update parameter.

By default, the `db.collection.update()` method updates a
**single** document. Include the option multi: true
to update all documents that match the query criteria.

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

**Changed in version:** 5.0

The `db.collection.update()` method has the following form:

```javascript
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
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

The `db.collection.update()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - query
  - document
  - .. _update-query:

    The selection criteria for the update. The same query
    selectors as in the `find()` method are available.

    When you execute an `update()` with ``upsert:
    true`` and the query matches no existing document, MongoDB will refuse
    to insert a new document if the query specifies conditions on the
    `_id` field using dot notation.

    This restriction ensures that the order of fields embedded in the
    `_id` document is well-defined and not bound to the order specified in
    the query.

    If you attempt to insert a document in this way, MongoDB raises an
    error.

* - update
  - document or pipeline
  - .. _update-parameter:

    The modifications to apply. Can be one of the following:

    - .. _update-method-update-document:

      Update document:

      Contains only update operator expressions.

    - .. _update-method-replacement-document:

      Replacement document:

      Contains only `<field1>: <value1>` pairs.

    - .. _update-method-agg-pipeline:

      Aggregation pipeline:

      Contains only the following aggregation stages:

      - `$addFields` and its alias `$set`

      - `$project` and its alias `$unset`

      - `$replaceRoot` and its alias `$replaceWith`

    For details and examples, see update-method-examples.

* - upsert
  - boolean
  - .. _update-upsert:

    Optional. When `true`, `update()` either: 

    - Creates a new document if no documents match the `query`.
      For more details see upsert behavior. 

    - Updates a single document that matches the `query`.

    If both `upsert` and `multi` are true and no documents match the query, the update operation inserts only a single document.

    To avoid multiple upserts, ensure that the
    `query` field(s) are uniquely indexed. See update-with-unique-indexes for an example.

    Defaults to `false`, which does *not* insert a new document when no
    match is found.

* - multi
  - boolean
  - .. _update-multi:

    Optional. If set to `true`, updates multiple documents that
    meet the `query` criteria. If set to `false`, updates one
    document. The default value is `false`. For additional
    information, see Update Multiple Documents Examples.

* - writeConcern
  - document
  - .. _update-wc:

    Optional. A document expressing the write concern. Omit to use the default write concern 
    `w: "majority"`.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

    For an example using `writeConcern`, see
    example-update-write-concern.

* - collation
  - document
  - .. _update-collation:

    Optional.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    For an example using `collation`, see
    example-update-collation.

* - arrayFilters
  - array
  - .. _update-array-filters:

    Optional. An array of filter documents that determine which array
    elements to modify for an update operation on an array field.

    In the update document, use the
    `$[<identifier>]` to define an identifier to update
    only those array elements that match the corresponding filter
    document in the `arrayFilters`.

    You cannot have an array filter document for an identifier if
    the identifier is not included in the update document.

    For examples, see update-arrayFilters.

* - hint
  - Document or string
  - .. _update-hint:

    Optional. A document or string that specifies the index to use to support the query predicate.

    The option can take an index specification document or the index
    name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-update-hint.

* - let
  - document
  - .. _db.collection.update-let-syntax:

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

    For a complete example using `let` and variables, see
    db.collection.update-let-example.

* - maxTimeMS
  - integer
  - .. _update-maxTimeMS:

    Optional. Specifies the time limit in milliseconds for the
    update operation to run before timing out.

* - bypassDocumentValidation
  - boolean
  - .. _update-bypassDocumentValidation:

    Optional. Enables `insert` to bypass schema validation
    during the operation. This lets you insert documents that do not
    meet the validation requirements.

### Returns

The method returns a writeresults-update document that contains
the status of the operation.

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

### Limitations

If you set `multi: true`, use the `update()` method only for 
idempotent operations.

### Using `$expr` in an Update with `Upsert`

Attempting to use the $expr 
operator with the upsert flag set to `true` generates an error.

### Sharded Collections

To use `db.collection.update()` with `multi: false` on a
sharded collection, you must include an exact match on the `_id`
field or target a single shard (such as by including the shard key).

When the `db.collection.update()` performs update operations
(and not document replacement operations),
`db.collection.update()` can target multiple shards.

**See also:**

`findAndModify()`

#### Replace Document Operations on a Sharded Collection

Replace document operations attempt to target a single shard, first by using 
the query filter. If the operation cannot target a single shard by the query 
filter, it then attempts to target by the replacement document.

In earlier versions, the operation attempts to target using the
replacement document.

#### `upsert` on a Sharded Collection

For a `db.collection.update()` operation that includes
upsert: true and is on a sharded collection, you
must include the full shard key in the `filter`:

- For an update operation.

- For a replace document operation.

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

To modify the **existing** shard key value with
`db.collection.update()`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write.

- You must specify `multi: false`.

- You must include an equality query filter on the full shard key.

**Tip:**

Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.

See also method-update-sharded-upsert.

#### Missing Shard Key

Documents in a sharded collection can be
missing the shard key fields. To use
`db.collection.update()` to set the document's
**missing** shard key, you must run on a
`mongos`. Do not issue the operation directly on
the shard.

In addition, the following requirements also apply:

* - Task

  - Requirements

* - To set to `null`

  - - Can specify `multi: true`.

    - Requires equality filter on the full shard key if ``upsert:
      true``.

* - To set to a non-`null` value

  - - Must be performed either inside a transaction or as a retryable write.

    - Must specify `multi: false`.

    - Requires equality filter on the full shard key if either:

      - `upsert: true`, or

      - if using a replacement document and the new shard key
        value belongs to a different shard.

**Tip:**

Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.

See also:

- method-update-sharded-upsert

- shard-key-missing

### Transactions

`db.collection.update()` can be used inside distributed transactions.

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

`db.collection.update()` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Oplog Entries

If a `db.collection.update()` operation successfully updates one or
more documents, the operation adds an entry on the oplog
(operations log). If the operation fails or does not find any documents
to update, the operation does not add an entry on the oplog. 

### Upsert with Dotted `_id` Query

When you execute an `update()` with ``upsert:
true`` and the query matches no existing document, MongoDB will refuse
to insert a new document if the query specifies conditions on the
`_id` field using dot notation.

This restriction ensures that the order of fields embedded in the
`_id` document is well-defined and not bound to the order specified in
the query.

If you attempt to insert a document in this way, MongoDB raises an
error.

### Upsert with Duplicate Values

Upserts can create duplicate documents, unless there is a
unique index to prevent duplicates.

If all `db.collection.update()` operations finish the query phase before any
client successfully inserts data, **and** there is no unique index on
the `name` field, each `db.collection.update()` operation may result in an
insert, creating multiple documents with `name: Andy`.

A unique index on the `name` field ensures that only one document
is created. With a unique index in place, the multiple `db.collection.update()`
operations now exhibit the following behavior:

- Exactly one `db.collection.update()` operation successfully inserts a new
   document.

- Other `db.collection.update()` operations either update the newly-inserted
   document or fail due to a unique key collision.
   
   For other `db.collection.update()` operations to update the
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

**See also:**

`$setOnInsert`

### Array Update Operations

In the update document, use the `$[<identifier>]` filtered positional
operator to define an identifier, which you then reference in the array filter
documents. You cannot have an array filter document for an identifier if the
identifier is not included in the update document.

The `<identifier>` must begin with a lowercase letter and contain only
alphanumeric characters.

You can include the same identifier multiple times in the update document;
however, for each distinct identifier (`$[identifier]`) in the update
document, you must specify **exactly one** corresponding array filter document.
That is, you cannot specify multiple array filter documents for the same
identifier. However, you can specify compound conditions on the same identifier
in a single filter document

**Note:**

`arrayFilters` is not available for updates that use an
aggregation pipeline.

## WriteResult

### Successful Results

The `db.collection.update()` method returns a
`WriteResult` object that contains the status of the operation.
Upon success, the `WriteResult` object contains the number of
documents that matched the query condition, the number of documents
inserted by the update, and the number of documents modified.

**See also:**

- `WriteResult.nMatched`
- `WriteResult.nUpserted`
- `WriteResult.nModified`

### Write Concern Errors

If the `db.collection.update()` method encounters write
concern errors, the results include the
`WriteResult.writeConcernError` field.

The following table explains the possible values of
`WriteResult.writeConcernError.provenance`:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

### Errors Unrelated to Write Concern

If the `db.collection.update()` method encounters a non-write
concern error, the results include the `WriteResult.writeError`
field.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

**op-expr:**

### Use Update Operator Expressions (`$inc` and `$set`)

If the `<update>` document contains update operator modifiers, such as those using the
`$set` modifier, then:

- The `<update>` document must contain *only*
  update operator expressions.

- The `db.collection.update()` method updates only the
  corresponding fields in the document.

  - To update an embedded document or an array as a whole,
    specify the replacement value for the field.

  - To update particular fields in an embedded document or in
    an array, use dot notation
    to specify the field.

```javascript
db.movies.update(
   { title: "The Godfather" },
   {
      $inc: { "tomatoes.viewer.numReviews": 1 },
      $set: {
         "tomatoes.viewer.meter": 99
      }
   }
)

/* Corresponds to the following SQL statement:
*  UPDATE movies
*  SET    tomatoes_viewer_numReviews = tomatoes_viewer_numReviews + 1,
*         tomatoes_viewer_meter = 99
*  WHERE  title = "The Godfather"
*/
```

In this operation:

- The `<query>` parameter of `{ title: "The Godfather" }` specifies which
  document to update

- the `$inc` operator increments the `numReviews` field in the
  `tomatoes.viewer` embedded document

- the `$set` operator updates the `meter` field in the 
  `tomatoes.viewer` embedded document.

If the `query` parameter matches multiple documents,
the operation only updates one matching document. To
update multiple documents, set the `multi` option
to `true`.

**See also:**

`$set`, `$inc`,
update operators
dot notation

**push-elements-existing-array:**

### Push Elements to Existing Array (`$push`)

The following operation uses the `$push` update
operator to append a value to the `genres` array.

```javascript
db.movies.update(
   { title: "The Matrix" },
   {
      $push: { genres: "Thriller" }
   }
)
```

After the update, the `genres` array includes the new value.

**See also:**

`$push`

**remove-fields:**

### Remove Fields (`$unset`)

The following operation uses the `$unset` operator to remove
the `metacritic` field from "The Godfather" document.

```javascript
db.movies.update( 
   { title: "The Godfather" }, 
   { $unset: { metacritic: "" } } 
)

/* $unset is similar (but not identical) to the following SQL
   command which removes the ``metacritic`` field from the ``movies``
   table

*  UPDATE movies
*  SET    metacritic = NULL
*  WHERE  title = "The Godfather"
*/
```

After the update, the `metacritic` field is removed.

**See also:**

`$unset`, `$rename`, update operators

**update-multiple:**

### Update Multiple Documents (`$update` With `multi`)

If `multi` is set to `true`, the
`db.collection.update()` method updates *all* documents
that meet the `<query>` criteria. The `multi` update
operation may interleave with other read/write operations.

The following operation sets the `test_field` field to `true`
for documents where the title is either "The Godfather" or "The Matrix".

```javascript
db.movies.update(
   { title: { $in: ["The Godfather", "The Matrix"] } },
   { $set: { test_field: true } },
   { multi: true }
)

/* Corresponds to the following SQL statement:
*  UPDATE movies
*  SET test_field = true
*  WHERE title IN ('The Godfather', 'The Matrix')
*/
```

The operation updates both matching documents.

You cannot specify `multi: true` when performing a replacement
and the update document contains *only*
`field:value` expressions.

**See also:**

`$set`

### Insert a New Document if No Match Exists (`Upsert`)

When you specify the option upsert: true:

- If document(s) match the query criteria,
  `db.collection.update()` performs an update.

- If no document matches the query criteria,
  `db.collection.update()` inserts a *single* document.

  **Note:**

  If multiple, identical upserts are issued at
  roughly the same time, it is possible for
  `update()` used with upsert: true to create duplicate documents. See
  update-with-unique-indexes for more information.

If you specify `upsert: true` on a sharded collection, you must
include the full shard key in the `filter`. For additional
`db.collection.update()` behavior on a sharded collection, see
update-sharded-collection.

The following tabs showcase a variety of uses of the `upsert` modifier
with `update()`.

**upsert-example:**

#### Upsert with Replacement Document

If no document matches the query criteria and the `<update>`
parameter is a replacement document (i.e., contains only field
and value pairs), the update inserts a new document with the
fields and values of the replacement document.

- If you specify an `_id` field in either the query parameter
  or replacement document, MongoDB uses that `_id` field in the
  inserted document.

- If you do not specify an `_id` field in either the query
  parameter or replacement document, MongoDB adds the
  `_id` field with a randomly generated objectid
  value.

  You cannot specify different `_id` field values in the
  query parameter and replacement document. If you do, the
  operation errors.

For example, the following update sets the upsert option to `true`:

```javascript
db.movies.update(
   { title: "Test Movie 12345" },
   { 
      $set: {
         title: "Test Movie 12345", 
         year: 2024, 
         genres: [ "Documentary" ],
         rated: "NR"
      }
   },
   { upsert: true }
)
```

If no document matches the `<query>` parameter, the update
operation inserts a document with *only* the replacement
document. Because no `_id` field was specified in the
replacement document or query document, the operation creates a
new unique `ObjectId` for the new document's `_id` field.
You can see the `upsert` reflected in the WriteResult of the operation.

**upsert-op-expr:**

#### Upsert with Operator Expressions (`$set`)

If no document matches the query criteria and the `<update>`
parameter is a document with update operator expressions, then the operation creates a base document
from the equality clauses in the `<query>` parameter and
applies the expressions from the `<update>` parameter.

Comparison operations from
the `<query>` will not be included in the new document. If
the new document does not include the `_id` field, MongoDB
adds the `_id` field with an objectid value.

For example, the following update sets the upsert option to `true`:

```javascript
db.movies.update(
   { title: "Test Movie 67890" },   // Query parameter
   {                                // Update document
      $set: { rated: "PG" },
      $setOnInsert: { year: 2024, type: "movie" }
   },
   { upsert: true }                 // Options
)
```

If no documents match the query condition, the operation
inserts the corresponding document.

**See also:**

`$setOnInsert`

**agg-pipeline-upsert:**

#### Upsert using an Aggregation Pipeline

If the `<update>` parameter is an aggregation pipeline, the update creates a base
document from the equality clauses in the `<query>`
parameter, and then applies the pipeline to the document to
create the document to insert. If the new document does not
include the `_id` field, MongoDB adds the `_id` field with
an objectid value.

For example, the following aggregation pipeline inserts a new document in
the `movies` collection because there is not an existing document that
matches the query filter:

```javascript
db.movies.update(
   { title: "Test Movie ABC123" },  // Query parameter
   [                                // Aggregation pipeline
      { $set: { 
         year: 2024, 
         type: "movie",
         rated: "NR",
         lastModified: "$$NOW" 
      } }
   ],
   { upsert: true }   // Options
)
```

**See also:**

For additional examples of updates using
aggregation pipelines, see update-behavior-agg-pipeline.

**combine-upsert-multi:**

#### Using `upsert` with `multi` (Match)

The following operation specifies both the `multi` option and
the `upsert` option. If matching documents exist, the
operation updates all matching documents. If no matching
documents exist, the operation inserts a new document.

```javascript
db.movies.update(
   { title: { $in: ["The Godfather", "The Matrix"] } },
   { $set: { test_upsert_field: true } },
   { upsert: true, multi: true }
)
```

Since both movies exist in the collection, the operation updates 
both matching documents.

#### Using `upsert` with `multi` (No Match)

If the collection had *no* matching document, the operation
would result in the insertion of a single document using the
fields from both the `<query>` and the `<update>`
specifications. For example, consider the following operation:

```javascript
db.movies.update(
   { "title": "Test Movie Unique789" },
   { $set: { year: 2024, type: "movie" } },
   { upsert: true, multi: true }
)
```

The operation inserts the corresponding document into the `movies`
collection.

### Update with Aggregation Pipeline

The `db.collection.update()` method can accept an 
aggregation pipeline 
`[ <stage1>, <stage2>, ... ]` that specifies the modifications to 
perform. The pipeline can consist of the following stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`

Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

#### Modify a Field Using the Values of the Other Fields in the Document

The following example creates a `displayTitle` field that combines the movie's
title and year with an aggregation pipeline that performs these operations:

- creates a `displayTitle` field by concatenating the `title` and `year` 
  fields

- sets a `lastModified` timestamp

```javascript
db.movies.update(
   { title: "The Godfather" },
   [
      { $set: { 
            displayTitle: { $concat: [ "$title", " (", { $toString: "$year" }, ")" ] },
            lastModified: "$$NOW" 
         } 
      }
   ]
)
```

**See also:**

updates-agg-pipeline

#### Perform Conditional Updates Based on Current Field Values

The following example updates movies released in 2015 to calculate a combined
rating score from IMDB and Tomatoes ratings, and assign a grade based on the
score.

```javascript
db.movies.update(
   { 
      year: 2015,
      "imdb.rating": { $type: "number" },
      "tomatoes.viewer.rating": { $type: "number" }
   },
   [
      { $set: { 
         combinedScore: { 
            $round: [ 
               { $avg: [ 
               { $multiply: [ "$imdb.rating", 10 ] }, 
               { $multiply: [ "$tomatoes.viewer.rating", 10 ] } 
               ] }, 
               1 
            ] 
         }, 
         lastUpdate: "$$NOW" 
         } 
      },
      { $set: { 
         grade: { 
            $switch: {
               branches: [
               { case: { $gte: [ "$combinedScore", 80 ] }, then: "A" },
               { case: { $gte: [ "$combinedScore", 70 ] }, then: "B" },
               { case: { $gte: [ "$combinedScore", 60 ] }, then: "C" },
               { case: { $gte: [ "$combinedScore", 50 ] }, then: "D" }
               ],
               default: "F"
            } 
         } 
         } 
      }
   ],
   { multi: true }
)
```

**Note:**

The `$set` used in the pipeline refers to the aggregation stage
`$set`, and not the update operators `$set`.

The `$set` stage:

- calculates a new field `combinedScore` by averaging the IMDB rating 
  (scaled by 10) and Tomatoes viewer rating (scaled by 10), then 
  rounding to one decimal place. See `$avg`, 
  `$multiply`, and `$round` for more information.

- sets the field `lastUpdate` to the value of the aggregation
  variable `NOW`. 

- assigns a letter grade based on the `combinedScore` using the
  `$switch` operator.

**See also:**

updates-agg-pipeline

### Specify `arrayFilters` for Array Update Operations

#### Update Elements Match `arrayFilters` Criteria

To update all array elements which match a specified criteria, use the
arrayFilters parameter.

The following example updates all movies that have `"English"` in their 
`languages` array. The operation replaces `"English"` with `"EN"`. 

```javascript
db.movies.update(
   { languages: "English" },
   { $set: { "languages.$[element]" : "EN" } },
   {
      arrayFilters: [ { "element": "English" } ],
      multi: true
   }
)
```

#### Update Specific Elements of an Array Using Pattern Matching

You can also use the arrayFilters
parameter with the filtered positional operator to update specific 
array elements that match a pattern.

The following example uses "The Godfather" movie from the existing collection,
which has a `writers` array. The operation updates only the writers whose
names contain "screenplay" by appending a suffix.

```javascript
db.movies.update(
   { title: "The Godfather" },
   { $set: { "writers.$[elem]" : { $concat: [ "$elem", " - UPDATED" ] } } },
   {
      arrayFilters: [ { "elem": { $regex: /screenplay/ } } ]
   }
)
```

The operation targets "The Godfather" document and updates only array 
elements matching the filter criteria. After the operation, the writers
who worked on the screenplay have " - UPDATED" appended.

### Specify `hint` for Update Operations

The `hint` option specifies which index MongoDB uses for the update
operation. Specify an index to ensure a consistent query plan when you
update multiple documents. This example uses the existing `movies`
collection from the sample_mflix database.

First, create an index on the `year` field:

```javascript
db.movies.createIndex( { year: 1 } )
```

The following update operation explicitly hints to
use the `{ year: 1 }` index to update all movies from 2010-2015:

```javascript
db.movies.update(
   { year: { $gte: 2010, $lte: 2015 } },  // Query parameter
   { $set: { decade: "2010s" } },             // Update document
   { multi: true, hint: { year: 1 } }          // Options
)
```

**Note:**

If you specify an index that does not exist, the operation errors.   

To see the index used, run `explain` on the operation:

```javascript
db.movies.explain().update(
   { title: "The Godfather", year: { $gte: 1970 } },
   { $set: { test_hint_field: true } },
   { hint: { year: 1 } }
)
```

The `db.collection.explain().update()`
does not modify the documents.

### Use Variables in `let`

**New in version:** 5.0

To define variables that you can access elsewhere in the command, use
the let option.

**Note:**

To filter results using a variable, you must access the variable
within the `$expr` operator.

The example:

- Defines two variables in the `let` option: `targetTitle` (set to "The Matrix") 
  and `newTitle` (set to "The Matrix Reloaded")

- Uses `$expr` in the query filter to compare the document's `title` field 
  against the `$$targetTitle` variable

- Uses an aggregation pipeline with `$set` to update the `title` field to 
  the value of `$$newTitle`

```javascript
db.movies.update(
   { $expr: { $eq: [ "$title", "$$targetTitle" ] } },
   [ { $set: { sequel: "$$sequelTitle" } } ],
   { let : { targetTitle: "The Matrix", sequelTitle: "The Matrix Reloaded" } }
)
```

### Override Default Write Concern

The following operation to a replica set specifies a write concern of `w: 2` with a `wtimeout` of 5000
milliseconds. This operation either returns after the write propagates
to both the primary and one secondary, or times out after 5 seconds.

```javascript
db.movies.update(
   { num_mflix_comments: { $lte: 10 } },
   { $set: { featured: true } },
   {
      multi: true,
      writeConcern: { w: 2, j: true, wtimeout: 5000 }
   }
)
```

The operation successfully completes after the write is acknowledged by the
primary and at least one secondary, as specified by `w: 2`.

### Write Concern Errors in Sharded Clusters

**Changed in version:** 8.1.2

When `db.collection.update()` executes on `mongos` in a sharded cluster, a `writeConcernError` is 
always reported in the response, even when one or more other errors occur. 
In previous releases, other errors sometimes caused `db.collection.update()` to not report write concern errors.

For example, if a document fails validation, triggering a `DocumentValidationFailed` error,
and a write concern error also occurs, both the `DocumentValidationFailed` error and the 
`writeConcernError` are returned in the top-level field of the response.

### Specify Collation

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

This operation updates all movies with titles that start with
`night` and uses `strength: 1` for case-insensitive comparison:

```javascript
db.movies.update(
   { title: /^night/i },
   { $set: { updated: true } },
   {
      collation: { locale: "en", strength: 1 },
      multi: true
   }
)
```
