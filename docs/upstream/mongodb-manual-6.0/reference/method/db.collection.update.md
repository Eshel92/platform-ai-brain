<!-- Converted from reference/method/db.collection.update.txt (reStructuredText). Includes are inlined. -->

# db.collection.update()

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
     let: <document> // Added in MongoDB 5.0
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

    If you attempt to insert a document in this way, MongoDB will raise an
    error. For example, consider the following update operation. Since the
    update operation specifies `upsert:true` and the query specifies
    conditions on the `_id` field using dot notation, then the update will
    result in an error when constructing the document to insert.

    ```javascript
    db.collection.update(
       { "_id.name": "Robert Frost", "_id.uid": 0 },  // Query parameter
       { $set:
          {
             "categories": [ "poet", "playwright" ]  // Replacement document
          }
       },
       { upsert: true }  // Options
    )
    ```

* - update
  - document or pipeline
  - .. _update-parameter:

    The modifications to apply. Can be one of the following:

    * - Update document
      - .. _update-method-update-document:

        Contains only update operator expressions.

    * - Replacement document
      - .. _update-method-replacement-document:

        Contains only `<field1>: <value1>` pairs.

    * - Aggregation pipeline

      - .. _update-method-agg-pipeline:

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

    **Note:**

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

    **New in version:** 5.0

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
operator with the upsert flag set to `true` will generate an error.

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
/core/transactions-production-consideration.

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

## Examples

The following tabs showcase a variety of common
`update()` operations.

In `mongosh`, create a `books` collection which
contains the following documents. This command first removes all
previously existing documents from the `books` collection:

```javascript
db.books.remove({});

db.books.insertMany([
  {
    "_id" : 1,
    "item" : "TBD",
    "stock" : 0,
    "info" : { "publisher" : "1111", "pages" : 430 },
    "tags" : [ "technology", "computer" ],
    "ratings" : [ { "by" : "ijk", "rating" : 4 }, { "by" : "lmn", "rating" : 5 } ],
    "reorder" : false
   },
   {
    "_id" : 2,
    "item" : "XYZ123",
    "stock" : 15,
    "info" : { "publisher" : "5555", "pages" : 150 },
    "tags" : [ ],
    "ratings" : [ { "by" : "xyz", "rating" : 5 } ],
    "reorder" : false
   }
]);
```

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
db.books.update(
   { _id: 1 },
   {
     $inc: { stock: 5 },
     $set: {
       item: "ABC123",
       "info.publisher": "2222",
       tags: [ "software" ],
       "ratings.1": { by: "xyz", rating: 3 }
     }
   }
)
```

In this operation:

- The `<query>` parameter of `{ _id: 1 }` specifies which
  document to update,

- the `$inc` operator increments the `stock` field,
  and

- the `$set` operator replaces the value of the

  - `item` field,
  - `publisher` field in the `info` embedded document,
  - `tags` field, and
  - second element in the `ratings` array.

The updated document is the following:

```javascript
{
  "_id" : 1,
  "item" : "ABC123",
  "stock" : 5,
  "info" : { "publisher" : "2222", "pages" : 430 },
  "tags" : [ "software" ],
  "ratings" : [ { "by" : "ijk", "rating" : 4 }, { "by" : "xyz", "rating" : 3 } ],
  "reorder" : false
}
```

This operation corresponds to the following SQL statement:

```sql
UPDATE books
SET    stock = stock + 5
       item = "ABC123"
       publisher = 2222
       pages = 430
       tags = "software"
       rating_authors = "ijk,xyz"
       rating_values = "4,3"
WHERE  _id = 1
```

**Note:**

If the `query` parameter had matched multiple documents,
this operation would only update one matching document. To
update multiple documents, you must set the `multi` option
to `true`.

**See also:**

`$set`, `$inc`,
/reference/operator/update,
dot notation

**push-elements-existing-array:**

### Push Elements to Existing Array (`$push`)

The following operation uses the `$push` update
operator to append a new object to the `ratings` array.

```javascript
db.books.update(
   { _id: 2 },
   {
     $push: { ratings: { "by" : "jkl", "rating" : 2 } }
   }
)
```

The updated document is the following:

```javascript
{
  "_id" : 2,
  "item" : "XYZ123",
  "stock" : 15,
  "info" : {
   "publisher" : "5555",
   "pages" : 150
  },
  "tags" : [ ],
  "ratings" : [
   { "by" : "xyz", "rating" : 5 },
   { "by" : "jkl", "rating" : 2 }
  ],
  "reorder" : false
 }
```

**See also:**

`$push`

**remove-fields:**

### Remove Fields (`$unset`)

The following operation uses the `$unset` operator to remove
the `tags` field from the document with `{ _id: 1 }`.

```javascript
db.books.update( { _id: 1 }, { $unset: { tags: 1 } } )
```

The updated document is the following:

```javascript
{
  "_id" : 1,
  "item" : "TBD",
  "stock" : 0,
  "info" : {
   "publisher" : "1111",
   "pages" : 430
  },
  "ratings" : [ { "by" : "ijk", "rating" : 4 }, { "by" : "lmn", "rating" : 5 } ],
  "reorder" : false
 }
```

There is not a direct SQL equivalent to `$unset`,
however `$unset` is similar to the following SQL
command which removes the `tags` field from the `books`
table:

```sql
ALTER TABLE books
DROP COLUMN tags
```

**See also:**

`$unset`, `$rename`, /reference/operator/update

**update-multiple:**

### Update Multiple Documents (`$update` With `multi`)

If `multi` is set to `true`, the
`db.collection.update()` method updates *all* documents
that meet the `<query>` criteria. The `multi` update
operation may interleave with other read/write operations.

The following operation sets the `reorder` field to `true`
for all documents where `stock` is less than or equal to
`10`. If the `reorder` field does not exist in the matching
document(s), the `$set` operator adds the field
with the specified value.

```javascript
db.books.update(
   { stock: { $lte: 10 } },
   { $set: { reorder: true } },
   { multi: true }
)
```

The resulting documents in the collection are the following:

```javascript
[
  {
    "_id" : 1,
    "item" : "ABC123",
    "stock" : 5,
    "info" : {
     "publisher" : "2222",
     "pages" : 430
    },
    "ratings" : [ { "by" : "ijk", "rating" : 4 }, { "by" : "xyz", "rating" : 3 } ],
    "reorder" : true
   }
   {
     "_id" : 2,
     "item" : "XYZ123",
     "stock" : 10,
     "info" : { "publisher" : "2255", "pages" : 150 },
     "tags" : [ "baking", "cooking" ],
     "reorder" : true
   }
]
```

This operation corresponds to the following SQL statement:

```sql
UPDATE books
SET reorder=true
WHERE stock <= 10
```

**Note:**

You cannot specify `multi: true` when performing a
replacement, i.e., when the <update> document contains *only*
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
  parameter or replacement document, MongoDB generates adds the
  `_id` field with a randomly generated objectid
  value.

  **Note:**

  You cannot specify different `_id` field values in the
  query parameter and replacement document. If you do, the
  operation errors.

For example, the following update sets the upsert option to `true`:

```javascript
db.books.update(
   { item: "ZZZ135" },  // Query parameter
   { $set:
      {
         item: "ZZZ135", stock: 5, tags: [ "database" ]  // Replacement document
      }
   },
   { upsert: true }  // Options
)
```

If no document matches the `<query>` parameter, the update
operation inserts a document with *only* the replacement
document. Because no `_id` field was specified in the
replacement document or query document, the operation creates a
new unique `ObjectId` for the new document's `_id` field.
You can see the `upsert` reflected in the WriteResult of the operation:

```javascript
WriteResult({
  "nMatched" : 0,
  "nUpserted" : 1,
  "nModified" : 0,
  "_id" : ObjectId("5da78973835b2f1c75347a83")
 })
```

The operation inserts the following document into the `books`
collection (your objectid value will differ):

```javascript
{
  "_id" : ObjectId("5da78973835b2f1c75347a83"),
  "item" : "ZZZ135",
  "stock" : 5,
  "tags" : [ "database" ]
}
```

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
db.books.update(
   { item: "BLP921" },   // Query parameter
   {                     // Update document
      $set: { reorder: false },
      $setOnInsert: { stock: 10 }
   },
   { upsert: true }      // Options
)
```

If no documents match the query condition, the operation
inserts the following document (your objectid value
will differ):

```javascript
{
  "_id" : ObjectId("5da79019835b2f1c75348a0a"),
  "item" : "BLP921",
  "reorder" : false,
  "stock" : 10
}
```

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

For example, the following upsert: true operation specifies an aggregation pipeline that uses

- the `$replaceRoot` stage which can provide
  somewhat similar behavior to a `$setOnInsert`
  update operator expression,

- the `$set` stage which can provide similar
  behavior to the `$set` update operator expression,

- the aggregation variable `NOW`, which resolves to
  the current datetime and can provide similar behavior to the
  `$currentDate` update operator expression.

```javascript
db.books.update(
   { item: "MRQ014", ratings: [2, 5, 3] }, // Query parameter
   [                                       // Aggregation pipeline
      { $replaceRoot: { newRoot: { $mergeObjects: [ { stock: 0 }, "$$ROOT"  ] } } },
      { $set: { avgRating: { $avg: "$ratings" }, tags: [ "fiction", "murder" ], lastModified: "$$NOW" } }
   ],
   { upsert: true }   // Options
)
```

If no document matches the `<query>` parameter, the
operation inserts the following document into the `books`
collection (your objectid value will differ):

```javascript
{
   "_id" : ObjectId("5e2921e0b4c550aad59d1ba9"),
   "stock" : 0,
   "item" : "MRQ014",
   "ratings" : [ 2, 5, 3 ],
   "avgRating" : 3.3333333333333335,
   "tags" : [ "fiction", "murder" ],
   "lastModified" : ISODate("2020-01-23T04:32:32.951Z")
}
```

**See also:**

For additional examples of updates using
aggregation pipelines, see update-behavior-agg-pipeline.

**combine-upsert-multi:**

#### Using `upsert` with `multi` (Match)

From `mongosh`, insert the following
documents into a `books` collection:

```javascript
db.books.insertMany( [
  {
    _id: 5,
    item: "RQM909",
    stock: 18,
    info: { publisher: "0000", pages: 170 },
    reorder: true
  },
  {
    _id: 6,
    item: "EFG222",
    stock: 15,
    info: { publisher: "1111", pages: 72 },
    reorder: true
  }
] )
```

The following operation specifies both the `multi` option and
the `upsert` option. If matching documents exist, the
operation updates all matching documents. If no matching
documents exist, the operation inserts a new document.

```javascript
db.books.update(
   { stock: { $gte: 10 } },        // Query parameter
   {                               // Update document
     $set: { reorder: false, tags: [ "literature", "translated" ] }
   },
   { upsert: true, multi: true }   // Options
)
```

The operation updates all matching documents and results in the
following:

```javascript
{
   "_id" : 5,
   "item" : "RQM909",
   "stock" : 18,
   "info" : { "publisher" : "0000", "pages" : 170 },
   "reorder" : false,
   "tags" : [ "literature", "translated" ]
}
{
   "_id" : 6,
   "item" : "EFG222",
   "stock" : 15,
   "info" : { "publisher" : "1111", "pages" : 72 },
   "reorder" : false,
   "tags" : [ "literature", "translated" ]
}
```

#### Using `upsert` with `multi` (No Match)

If the collection had *no* matching document, the operation
would result in the insertion of a single document using the
fields from both the `<query>` and the `<update>`
specifications. For example, consider the following operation:

```javascript
db.books.update(
  { "info.publisher": "Self-Published" },   // Query parameter
  {                                         // Update document
    $set: { reorder: false, tags: [ "literature", "hardcover" ], stock: 25 }
  },
  { upsert: true, multi: true }             // Options
)
```

The operation inserts the following document into the `books`
collection (your objectid value will differ):

```javascript
{
  "_id" : ObjectId("5db337934f670d584b6ca8e0"),
  "info" : { "publisher" : "Self-Published" },
  "reorder" : false,
  "stock" : 25,
  "tags" : [ "literature", "hardcover" ]
}
```

**upsert-dotted-id:**

#### Upsert with Dotted `_id` Query

When you execute an `update()` with ``upsert:
true`` and the query matches no existing document, MongoDB will refuse
to insert a new document if the query specifies conditions on the
`_id` field using dot notation.

This restriction ensures that the order of fields embedded in the
`_id` document is well-defined and not bound to the order specified in
the query.

If you attempt to insert a document in this way, MongoDB will raise an
error. For example, consider the following update operation. Since the
update operation specifies `upsert:true` and the query specifies
conditions on the `_id` field using dot notation, then the update will
result in an error when constructing the document to insert.

```javascript
db.collection.update(
   { "_id.name": "Robert Frost", "_id.uid": 0 },  // Query parameter
   { $set:
      {
         "categories": [ "poet", "playwright" ]  // Replacement document
      }
   },
   { upsert: true }  // Options
)
```

The `WriteResult` of the operation returns the following
error:

```javascript
WriteResult({
  "nMatched" : 0,
  "nUpserted" : 0,
  "nModified" : 0,
  "writeError" : {
    "code" : 111,
    "errmsg" : "field at '_id' must be exactly specified, field at sub-path '_id.name'found"
  }
})
```

**See also:**

`WriteResult()`

#### Upsert with Duplicate Values

Upserts can create duplicate documents, unless there is a
unique index to prevent duplicates.

Consider an example where no document with the name `Andy` exists
and multiple clients issue the following command at roughly the same
time:

```javascript
db.people.update(
   { name: "Andy" },
   { $inc: { score: 1 } },
   {
     upsert: true,
     multi: true
   }
)
```

If all `update()` operations finish the query phase before any
client successfully inserts data, **and** there is no unique index on
the `name` field, each `update()` operation may result in an
insert, creating multiple documents with `name: Andy`.

A unique index on the `name` field ensures that only one document
is created. With a unique index in place, the multiple `update()`
operations now exhibit the following behavior:

- Exactly one `update()` operation will successfully insert a new
  document.

- Other `update()` operations either update the newly-inserted
  document or fail due to a unique key collision.

  In order for other `update()` operations to update the
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

**See also:**

`$setOnInsert`

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

Create a `students` collection with the following documents:

```javascript
db.students.insertMany( [
   { "_id" : 1, "student" : "Skye", "points" : 75, "commentsSemester1" : "great at math", "commentsSemester2" : "loses temper", "lastUpdate" : ISODate("2019-01-01T00:00:00Z") },
   { "_id" : 2, "students" : "Elizabeth", "points" : 60, "commentsSemester1" : "well behaved", "commentsSemester2" : "needs improvement", "lastUpdate" : ISODate("2019-01-01T00:00:00Z") }
] )
```

Assume that instead of separate `commentsSemester1` and `commentsSemester2` 
fields, you want to gather these into a new `comments` field. The following
update operation uses an aggregation pipeline to:

- add the new `comments` field and set the `lastUpdate` field.

- remove the `commentsSemester1` and `commentsSemester2` fields for all 
  documents in the collection.

```javascript
db.members.update(
   { },
   [
      { $set: { comments: [ "$commentsSemester1", "$commentsSemester2" ], lastUpdate: "$$NOW" } },
      { $unset: [ "commentsSemester1", "commentsSemester2" ] }
   ],
   { multi: true }
)
```

**Note:**

The `$set` and `$unset` used in the pipeline refers to the
aggregation stages `$set` and `$unset`
respectively, and not the update operators `$set` and
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
{ "_id" : 1, "student" : "Skye", "status" : "Modified", "points" : 75, "lastUpdate" : ISODate("2020-01-23T05:11:45.784Z"), "comments" : [ "great at math", "loses temper" ] }
{ "_id" : 2, "student" : "Elizabeth", "status" : "Modified", "points" : 60, "lastUpdate" : ISODate("2020-01-23T05:11:45.784Z"), "comments" : [ "well behaved", "needs improvement" ] }
```

**See also:**

/tutorial/update-documents-with-aggregation-pipeline

#### Perform Conditional Updates Based on Current Field Values

Create a `students3` collection with the following documents:

```javascript
db.students3.insertMany( [
   { "_id" : 1, "tests" : [ 95, 92, 90 ], "lastUpdate" : ISODate("2019-01-01T00:00:00Z") },
   { "_id" : 2, "tests" : [ 94, 88, 90 ], "lastUpdate" : ISODate("2019-01-01T00:00:00Z") },
   { "_id" : 3, "tests" : [ 70, 75, 82 ], "lastUpdate" : ISODate("2019-01-01T00:00:00Z") }
] )
```

Using an aggregation pipeline, you can update the documents with the
calculated grade average and letter grade.

```javascript
db.students3.update(
   { },
   [
     { $set: { average : { $trunc: [ { $avg: "$tests" }, 0 ] }, lastUpdate: "$$NOW" } },
     { $set: { grade: { $switch: {
                           branches: [
                               { case: { $gte: [ "$average", 90 ] }, then: "A" },
                               { case: { $gte: [ "$average", 80 ] }, then: "B" },
                               { case: { $gte: [ "$average", 70 ] }, then: "C" },
                               { case: { $gte: [ "$average", 60 ] }, then: "D" }
                           ],
                           default: "F"
     } } } }
   ],
   { multi: true }
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
     information on the  `$trunc` truncate aggregation operator.

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
{ "_id" : 1, "tests" : [ 95, 92, 90 ], "lastUpdate" : ISODate("2020-01-24T17:29:35.340Z"), "average" : 92, "grade" : "A" }
{ "_id" : 2, "tests" : [ 94, 88, 90 ], "lastUpdate" : ISODate("2020-01-24T17:29:35.340Z"), "average" : 90, "grade" : "A" }
{ "_id" : 3, "tests" : [ 70, 75, 82 ], "lastUpdate" : ISODate("2020-01-24T17:29:35.340Z"), "average" : 75, "grade" : "C" }
```

**See also:**

/tutorial/update-documents-with-aggregation-pipeline

### Specify `arrayFilters` for Array Update Operations

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

`arrayFilters` is not available for updates that use an
aggregation pipeline.

#### Update Elements Match `arrayFilters` Criteria

To update all array elements which match a specified criteria, use the
arrayFilters parameter.

In `mongosh`, create a `students`
collection with the following documents:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 95, 92, 90 ] },
   { "_id" : 2, "grades" : [ 98, 100, 102 ] },
   { "_id" : 3, "grades" : [ 95, 110, 100 ] }
] )
```

To update all elements that are greater than or equal to `100` in the
`grades` array, use the filtered positional operator
`$[<identifier>]` with the `arrayFilters` option:

```javascript
db.students.update(
   { grades: { $gte: 100 } },
   { $set: { "grades.$[element]" : 100 } },
   {
     multi: true,
     arrayFilters: [ { "element": { $gte: 100 } } ]
   }
)
```

After the operation, the collection contains the following documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 100 ] }
{ "_id" : 3, "grades" : [ 95, 100, 100 ] }
```

#### Update Specific Elements of an Array of Documents

You can also use the arrayFilters
parameter to update specific document fields within an array of
documents.

In `mongosh`, create a `students2`
collection with the following documents:

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

To modify the value of the `mean` field for all elements in the
`grades` array where the grade is greater than or equal to `85`,
use the filtered positional operator `$[<identifier>]` with
the `arrayFilters`:

```javascript
db.students2.update(
   { },
   { $set: { "grades.$[elem].mean" : 100 } },
   {
     multi: true,
     arrayFilters: [ { "elem.grade": { $gte: 85 } } ]
   }
)
```

After the operation, the collection has the following documents:

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
      { "grade" : 90, "mean" : 100, "std" : 6 },
      { "grade" : 87, "mean" : 100, "std" : 3 },
      { "grade" : 85, "mean" : 100, "std" : 4 }
   ]
}
```

### Specify `hint` for Update Operations

In `mongosh`, create a `newStudents`
collection with the following documents:

```javascript
db.newStudents.insertMany( [
   { "_id" : 1, "student" : "Richard", "grade" : "F", "points" :  0,  "comments1" : null, "comments2" : null },
   { "_id" : 2, "student" : "Jane", "grade" : "A", "points" : 60,  "comments1" : "well behaved", "comments2" : "fantastic student" },
   { "_id" : 3, "student" : "Ronan", "grade" : "F", "points" :  0,  "comments1" : null, "comments2" : null },
   { "_id" : 4, "student" : "Noah", "grade" : "D", "points" : 20,  "comments1" : "needs improvement", "comments2" : null },
   { "_id" : 5, "student" : "Adam", "grade" : "F", "points" :  0,  "comments1" : null, "comments2" : null },
   { "_id" : 6, "student" : "Henry", "grade" : "A", "points" : 86,  "comments1" : "fantastic student", "comments2" : "well behaved" }
] )
```

Create the following index on the collection:

```javascript
db.newStudents.createIndex( { grade: 1 } )
```

The following update operation explicitly hints to
use the index `{grade: 1 }`:

```javascript
db.newStudents.update(
   { points: { $lte: 20 }, grade: "F" },     // Query parameter
   { $set: { comments1: "failed class" } },  // Update document
   { multi: true, hint: { grade: 1 } }       // Options
)
```

**Note:**

If you specify an index that does not exist, the operation errors.   

The update command returns the following:

```javascript
WriteResult({ "nMatched" : 3, "nUpserted" : 0, "nModified" : 3 })
```

To see the index used, run `explain` on the operation:

```javascript
db.newStudents.explain().update(
   { "points": { $lte: 20 }, "grade": "F" },
   { $set: { "comments1": "failed class" } },
   { multi: true, hint: { grade: 1 } }
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

Create a collection `cakeFlavors`:

```javascript
db.cakeFlavors.insertMany( [
   { _id: 1, flavor: "chocolate" },
   { _id: 2, flavor: "strawberry" },
   { _id: 3, flavor: "cherry" }
] )
```

The following example defines `targetFlavor` and `newFlavor`
variables in `let` and uses the variables to change the cake flavor
from cherry to orange:

```javascript
db.cakeFlavors.update(
   { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   [ { $set: { flavor: "$$newFlavor" } } ],
   { let : { targetFlavor: "cherry", newFlavor: "orange" } }
)
```

### Override Default Write Concern

The following operation to a replica set specifies a write concern of `w: 2` with a `wtimeout` of 5000
milliseconds. This operation either returns after the write propagates
to both the primary and one secondary, or times out after 5 seconds.

```javascript
db.books.update(
   { stock: { $lte: 10 } },
   { $set: { reorder: true } },
   {
     multi: true,
     writeConcern: { w: 2, wtimeout: 5000 }
   }
)
```

### Specify Collation

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

In `mongosh`, create a collection named
`myColl` with the following documents:

```javascript
db.myColl.insertMany( [
    { _id: 1, category: "café", status: "A" },
    { _id: 2, category: "cafe", status: "a" },
    { _id: 3, category: "cafE", status: "a" }
] )
```

The following operation includes the collation
option and sets `multi` to `true` to update all matching documents:

```javascript
db.myColl.update(
   { category: "cafe" },
   { $set: { status: "Updated" } },
   {
     collation: { locale: "fr", strength: 1 },
     multi: true
   }
)
```

The write result of the operation returns the following document, indicating that all three documents in the
collection were updated:

```none
WriteResult({ "nMatched" : 3, "nUpserted" : 0, "nModified" : 3 })
```

After the operation, the collection contains the following documents:

```javascript
{ "_id" : 1, "category" : "café", "status" : "Updated" }
{ "_id" : 2, "category" : "cafe", "status" : "Updated" }
{ "_id" : 3, "category" : "cafE", "status" : "Updated" }
```

## WriteResult

### Successful Results

The `db.collection.update()` method returns a
`WriteResult` object that contains the status of the operation.
Upon success, the `WriteResult` object contains the number of
documents that matched the query condition, the number of documents
inserted by the update, and the number of documents modified:

```javascript
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

**See also:**

- `WriteResult.nMatched`
- `WriteResult.nUpserted`
- `WriteResult.nModified`

### Write Concern Errors

If the `db.collection.update()` method encounters write
concern errors, the results include the
`WriteResult.writeConcernError` field:

```javascript
WriteResult({
   "nMatched" : 1,
   "nUpserted" : 0,
   "nModified" : 1,
   "writeConcernError": {
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
field:

```javascript
WriteResult({
   "nMatched" : 0,
   "nUpserted" : 0,
   "nModified" : 0,
   "writeError" : {
      "code" : 7,
      "errmsg" : "could not contact primary for replica set shard-a"
   }
})
```
