<!-- Converted from reference/method/db.collection.findOneAndReplace.txt (reStructuredText). Includes are inlined. -->

# db.collection.findOneAndReplace()

(Include not available offline: includes/wayfinding/mongosh-method-findOneAndReplace.rst)

## Definition

**`db.collection.findOneAndReplace( filter, replacement, options )`**

Replaces a single document based on the specified filter.

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

The `findOneAndReplace()` method has the following 
form:

```javascript
db.collection.findOneAndReplace(
   <filter>,
   <replacement>,
   {
     writeConcern: <document>,
     projection: <document>,
     sort: <document>,
     maxTimeMS: <number>,
     upsert: <boolean>,
     returnDocument: <string>,
     returnNewDocument: <boolean>,
     collation: <document>
   }
)
```

### Fields and Options

The `findOneAndReplace()` method takes the following
fields and options:

* - Field
  - Type
  - Description

* - filter
  - document
  - .. _findOneAndReplace-filter:

    The selection criteria for the update. The same query
    selectors as in the `find()` method are available.

    To replace the first document returned in the collection,
    specify an empty document `{ }`.

    If unspecified, defaults to an empty document.

    If the query argument is not a document, the operation returns an error.

* - replacement
  - document
  - .. _findOneAndReplace-replacement:

    The replacement document.

    Cannot contain 
    update operators.

    The `<replacement>` document cannot specify an `_id` value
    that differs from the replaced document.

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

* - projection
  - document
  - .. _findOneAndReplace-projection:

    Optional. A subset of fields to return.

    To return all fields in the matching document, omit this
    field.

    If the projection argument is not a document, the operation errors.

* - sort
  - document
  - .. _findOneAndReplace-sort:

    Optional. Specifies a sorting order for the documents matched by
    the filter.

    If the sort argument is not a document, the operation errors.

    See `cursor.sort()`.

* - `maxTimeMS`
  - number
  - Optional. Specifies a time limit in milliseconds within which
    the operation must complete. Returns an error if the limit is
    exceeded.

* - upsert
  - boolean
  - .. _findOneAndReplace-upsert:

    Optional. When `true`, `findOneAndReplace()` either:

    - Inserts the document from the `replacement` parameter if no document matches the
      `filter`. Returns `null` after inserting the new document, unless `returnNewDocument` is `true`.

    - Replaces the document that matches the `filter` with the `replacement` document.

    MongoDB will add the `_id` field to the replacement document if it is not specified
    in either the `filter` or `replacement` documents. If `_id` is present in both,
    the values must be equal.

    To avoid multiple upserts, ensure that the `query` fields
    are uniquely indexed.

    Defaults to `false`.

* - returnDocument
  - string
  - .. _findOneAndReplace-returnDocument:

    Optional. Starting in `mongosh` 0.13.2,
    `returnDocument` is an alternative for
    returnNewDocument.
    If both options are set, `returnDocument` takes precedence.

    `returnDocument: "before"` returns the original document.
    `returnDocument: "after"` returns the updated document.

* - returnNewDocument
  - boolean
  - .. _findOneAndReplace-returnNewDocument:

    Optional. When `true`, returns the replacement document
    instead of the original document.

    Defaults to `false`.

* - collation
  - document
  - .. _findOneAndReplace-collation:

    Optional. 

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

### Returns

Returns the original document by default. Returns the updated document
if returnDocument is set to
`after` or returnNewDocument is set to `true`.

## Behavior

### Document Match

`db.collection.findOneAndReplace()` replaces the first matching 
document in the collection that matches the `filter`. 
The `sort` field can be used to influence which document is modified.

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

The `projection` field takes a document in the following form:

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

#### Shard Key Modification

You can update a document's shard key value unless the shard key field is the 
immutable `_id` field. 

**Warning:**

Documents in sharded collections can be missing the shard key fields. 
Take precaution to avoid accidentally removing the shard key when changing 
a document's shard key value.

To modify the **existing** shard key value with
`db.collection.findOneAndReplace()`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write.
  
- You must include an equality filter on the full shard key.

#### Missing Shard Key

Documents in a sharded collection can be
missing the shard key fields. To use
`db.collection.findOneAndReplace()` to set the document's
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

`db.collection.findOneAndReplace()` can be used inside distributed transactions.

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

`db.collection.findOneAndReplace()` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Oplog Entries

If a `db.collection.findOneAndReplace()` operation successfully
replaces a document, the operation adds an entry on the oplog
(operations log). If the operation fails or does not find a document to
replace, the operation does not add an entry on the oplog. 

## Examples

### Replace A Document

Create a sample `scores` collection with the following documents:

```javascript
db.scores.insertMany([
   { "_id" : 1, "team" : "Fearful Mallards", "score" : 25000 },
   { "_id" : 2, "team" : "Tactful Mooses", "score" : 23500 },
   { "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 },
   { "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 },
   { "_id" : 5, "team" : "Garrulous Bears", "score" : 18000 }
]);
```

The following operation finds a document with `score` less than
`20000` and replaces it:

```javascript
db.scores.findOneAndReplace( 
   { "score" : { $lt : 20000 } },  
   { "team" : "Observant Badgers", "score" : 20000 }
)
```

The operation returns the *original* document that has been replaced:

```javascript
{ "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 }
```

If returnNewDocument was
true, the operation would return the replacement document instead.

Although multiple documents meet the filter criteria,
`db.collection.findOneAndReplace` replaces only one document.

### Sort and Replace A Document

Create a sample `scores` collection with the following documents:

```javascript
db.scores.insertMany([
   { "_id" : 1, "team" : "Fearful Mallards", "score" : 25000 },
   { "_id" : 2, "team" : "Tactful Mooses", "score" : 23500 },
   { "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 },
   { "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 },
   { "_id" : 5, "team" : "Garrulous Bears", "score" : 18000 }
]);
```

By including an ascending sort on
the `score` field, the following example replaces the document with the
lowest score among those documents that match the filter:

```javascript
db.scores.findOneAndReplace(
   { "score" : { $lt : 20000 } },
   { "team" : "Observant Badgers", "score" : 20000 },
   { sort: { "score" : 1 } }
)
```

The operation returns the *original* document that has been replaced:

```javascript
{ "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 }
```

See findOneAndReplace-example-replace-document for the non-sorted 
result of this command.

### Project Specific Fields in Return Document

Create a sample `scores` collection with the following documents:

```javascript
db.scores.insertMany([
   { "_id" : 1, "team" : "Fearful Mallards", "score" : 25000 },
   { "_id" : 2, "team" : "Tactful Mooses", "score" : 23500 },
   { "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 },
   { "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 },
   { "_id" : 5, "team" : "Garrulous Bears", "score" : 18000 }
])
```

The following operation uses projection to only display the `team` field in
the returned document:

```javascript
db.scores.findOneAndReplace(
   { "score" : { $lt : 22250 } },
   { "team" : "Therapeutic Hamsters", "score" : 22250 },
   { sort : { "score" : 1 }, projection: { "_id" : 0, "team" : 1 } }
)
```

   
The operation returns the *original* document with only the `team` field: 

```javascript
{ "team" : "Cuddly Zebras" }
```

### Replace Document with Time Limit

The following operation sets a 5ms time limit to complete:

```javascript
try {
   db.scores.findOneAndReplace(
      { "score" : { $gt : 25000 } },
      { "team" : "Emphatic Rhinos", "score" : 25010 },
      { maxTimeMS: 5 } 
   );
} catch(e){
   print(e);
}
```

If the operation exceeds the time limit, it returns:

```javascript
Error: findAndModifyFailed failed: { "ok" : 0, "errmsg" : "operation exceeded time limit", "code" : 50 }
```

### Replace Document with Upsert

The following operation uses the upsert field to insert the replacement document if
no document matches the filter:

```javascript
try {
   db.scores.findOneAndReplace( 
      { "team" : "Fortified Lobsters" },
      { "_id" : 6019, "team" : "Fortified Lobsters" , "score" : 32000},
      { upsert : true, returnDocument: "after" }
   );
} catch (e){
   print(e);
}
```

The operation returns the following:

```javascript
{
   "_id" : 6019,
   "team" : "Fortified Lobsters",
   "score" : 32000
}
```

   
If `returnDocument: "before"` was set, the operation would return
`null` because there is no original document to return.

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

Create a sample `myColl` collection with the following documents:

```javascript
db.myColl.insertMany([
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
]);
```

The following operation includes the collation
option:

```javascript
db.myColl.findOneAndReplace(
   { category: "cafe", status: "a" },
   { category: "cafÉ", status: "Replaced" },
   { collation: { locale: "fr", strength: 1 } }
);
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```
