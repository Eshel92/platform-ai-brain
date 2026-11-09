<!-- Converted from reference/command/update.txt (reStructuredText). Includes are inlined. -->

# update (database command)

## Definition

**`update`**

The `update` command modifies documents in a collection.
A single `update` command can contain multiple update
statements. 

   `updateMany`, 
   `replaceOne`,
   `findOneAndReplace`, and
   `findOneAndUpdate` 
   helper methods

**Tip:**

In `mongosh`, this command can also be run through the `updateOne`,.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

The command has the following syntax:

```javascript
db.runCommand(
   {
      update: <collection>,
      updates: [
         {
           q: <query>,
           u: <document or pipeline>,
           c: <document>, // Added in MongoDB 5.0
           upsert: <boolean>,
           multi: <boolean>,
           collation: <document>,
           arrayFilters: <array>,
           hint: <document|string>
         },
         ...
      ],
      ordered: <boolean>,
      maxTimeMS: <integer>,
      writeConcern: { <write concern> },
      bypassDocumentValidation: <boolean>,
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

* - `update`
  - string
  - The name of the target collection.

* - `updates`
  - array
  - An array of one or more update statements to perform on the named
    collection. For details of the update statements, see Update
    Statements.

* - `ordered`
  - boolean
  - Optional. If `true`, then when an update statement fails, return without
    performing the remaining update statements. If `false`, then when
    an update fails, continue with the remaining update statements, if
    any. Defaults to `true`.

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

* - `writeConcern`
  - document
  - Optional. A document expressing the write concern
    of the `update` command. Omit to use the default write
    concern.

    Do not explicitly set the write concern for the operation if run in
    a transaction. To use write concern with transactions, see
    transactions-write-concern.

* - `bypassDocumentValidation`
  - boolean
  - Optional. Enables `update` to bypass schema validation
    during the operation. This lets you update documents that do not
    meet the validation requirements.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

* - let
  - document
  - .. _update-let-syntax:

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

    For a complete example, see update-variables-example.

    **New in version:** 5.0

### Update Statements

Each element of the `updates` array is an update statement document.
Each document contains the following fields:

* - Field
  - Type
  - Description

* - q
  - document
  - .. _update-command-q:

    The query that matches documents to update. Use the same query
    selectors as used in the `find()` method.

* - u
  - document or pipeline
  - .. _update-command-u:

    The modifications to apply.
    The value can be either:

    - A document that contains update operator expressions,
    - A replacement document with only `<field1>: <value1>` pairs, or
    - An aggregation pipeline.

      - `$addFields` and its alias `$set`

      - `$project` and its alias `$unset`

      - `$replaceRoot` and its alias `$replaceWith`

    For details, see update-command-behaviors.

* - c
  - document
  - .. _update-command-c:

    Optional. You can specify `c` only if u is a pipeline. 

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
    update-variables-example.

    **New in version:** 5.0

* - upsert
  - boolean
  - .. _update-command-upsert:

    Optional. When `true`, `update` either: 

    - Creates a new document if no documents match the `query`.
      For more details see upsert behavior. 

    - Updates a single document that matches the `query`.

    If both `upsert` and `multi` are true and no documents match the query, the update operation inserts only a single document.

    To avoid multiple upserts, ensure that the
    `query` field(s) are uniquely indexed. See update-command-behaviors-unique-index for an example.

    Defaults to `false`, which does *not* insert a new document when no
    match is found.

* - `multi`
  - boolean
  - Optional. If `true`, updates all documents that meet the query criteria. If
    `false`, limit the update to one document that meet the query
    criteria. Defaults to `false`.

    When updating multiple documents, if a single document fails
    to update, further documents are not updated. See
    multi-update failures for more 
    details on this behavior.

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

  - Optional. An array of filter documents that determines which array elements to
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

    For examples, see update-command-arrayFilters.

* - hint 

  - Document or string

  - .. _update-command-hint:

    Optional. A document or string that specifies the index to use to support the query predicate.

    The option can take an index specification document or the index
    name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-update-command-hint.

### Returns

The command returns a document that contains the status of the
operation. For example:

```javascript
{
   "ok" : 1,
   "nModified" : 0,
   "n" : 1,
   "upserted" : [
      {
         "index" : 0,
         "_id" : ObjectId("52ccb2118908ccd753d65882")
      }
   ]
}
```

For details of the output fields, see update-command-output.

## Access Control

On deployments running with `authorization`, the
user must have access that includes the following privileges:

- `update` action on the specified collection(s).

- `find` action on the specified collection(s).

- `insert` action on the specified collection(s).

The built-in role `readWrite` provides the required
privileges.

## Behavior

### Limitations

If you set `multi: true`, use the `update` command only for 
idempotent operations.

### Update with an Update Operator Expressions Document

The update statement field u can accept a
document that only contains update operator
expressions. For example:

```javascript
updates: [
   {
     q: <query>,
     u: { $set: { status: "D" }, $inc: { quantity: 2 } },
      ...
   },
   ...
]
```

Then, the `update` command updates only the corresponding
fields in the document.

### Update with a Replacement Document

The update statement field u field can accept
a replacement document, i.e. the document contains *only*
`field:value` expressions. For example:

```javascript
updates: [
   {
      q: <query>,
      u: { status: "D", quantity: 4 },
      ...
   },
   ...
]
```

Then the `update` command *replaces* the matching document
with the update document. The `update` command can only
replace a *single* matching document; i.e. the `multi` field cannot
be `true`. The `update` command *does not* replace the
`_id` value.

### Multi-Update Failures

If a single document fails to update in an update command with the 
`multi` parameter set to `true`, no further documents
update as part of that command. 

For example, the `sample_mflix.movies` collection contains movies with 
`imdb.rating` fields. Create a document validator on the `movies` collection with a rule
that the `imdb.rating` value must be less than or equal to `10`: 

```javascript
db.runCommand( 
   { 
      update: "movies",
      updates: [
      {
         q: { 
            year: { $gte: 2000, $lte: 2005 },
            "imdb.rating": { $type: "number" }
         }, 
         u: { $inc: { "imdb.rating": 1 } },
         multi: true
      }
      ]
   }
)
```

If any movie already has a rating of `10`, incrementing it would violate 
the validator rule (rating > 10). When this happens, the update stops and 
no further documents are updated, even if thousands of documents matched 
the query.

**Note:**

If a subset of matched documents are updated, such as when an update
would cause some documents to fail schema validation, the value of
`nModified` returned by the `update` command might not be accurate.

### Update with an Aggregation Pipeline

The update statement field u field can accept an 
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
updates: [
   {
      q: <query>,
      u: [ 
        { $set: { status: "Modified", comments: [ "$misc1", "$misc2" ] } }, 
        { $unset: [ "misc1", "misc2" ] } 
      ],
      ...
   },
   ...
]
```

**Note:**

The `$set` and `$unset` used in the pipeline refers to the
aggregation stages `$set` and `$unset`
respectively, and not the update operators `$set` and `$unset`.

For examples, see update-command-example-agg.

### Upsert with Unique Index

Upserts can create duplicate documents, unless there is a
unique index to prevent duplicates.

Consider an example where no document with the name `Andy` exists
and multiple clients issue the following command at roughly the same
time:

```javascript
db.runCommand(
   {
     update: "people",
     updates: [
       { q: { name: "Andy" }, u: { $inc: { score: 1 } }, multi: true, upsert: true }
     ]
   }
)
```

If all `update` operations finish the query phase before any
client successfully inserts data, **and** there is no unique index on
the `name` field, each `update` operation may result in an
insert, creating multiple documents with `name: Andy`.

A unique index on the `name` field ensures that only one document
is created. With a unique index in place, the multiple `update`
operations now exhibit the following behavior:

- Exactly one `update` operation will successfully insert a new
  document.

- Other `update` operations either update the newly-inserted
  document or fail due to a unique key collision.

  In order for other `update` operations to update the
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

### Limits

For each update element in the `updates` array, the sum of the query
and the update sizes (i.e. `q` and `u` ) must be less than or equal
to the `maximum BSON document size`.

The total number of update statements in the `updates` array must be
less than or equal to the `maximum bulk size`.

### Schema Validation

The `update` command adds support for the
`bypassDocumentValidation` option, which lets you bypass
schema validation when
inserting or updating documents in a collection with validation    
rules.

### Sharded Collections

#### `upsert` on a Sharded Collection

To use `update` with `multi: false` on a sharded
collection,

- If you do not specify upsert: true,
  the filter q must either include an
  equality match on the `_id` field or target a single shard (such as
  by including the shard key).

- If you specify upsert: true, the
  filter q must include an equality match on the
  shard key.

  However, documents in a sharded collection can be
  missing the shard key fields. To target a
  document that is missing the shard key, you can use the `null`
  equality match in conjunction with another filter condition
  (such as on the `_id` field). For example:

  ```javascript
  { _id: <value>, <shardkeyfield>: null } // _id of the document missing shard key
  ```

#### Replace Document

When replacing a document, `update`  attempts to target a shard, 
first by using the query filter. If the operation cannot target a single shard 
by the query filter, it then attempts to target by the replacement document.

#### Shard Key Modification

You can update a document's shard key value unless the shard key field is the 
immutable `_id` field. 

To modify the **existing** shard key value with
`update`:

- You must run on a `mongos`. Do not
  issue the operation directly on the shard.

- You must run either in a transaction or as a retryable write.

- You must specify `multi: false`.

- You must include an equality query filter on the full shard key.

**Tip:**

Since a missing key value is returned as part of a null equality
match, to avoid updating a null-valued key, include additional
query conditions (such as on the `_id` field) as appropriate.

See also cmd-update-sharded-upsert.

#### Missing Shard Key

Documents in a sharded collection can be
missing the shard key fields. To use
`update` to set the document's
**missing** shard key, you must run on a
`mongos`. Do not issue the operation directly on
the shard.

In addition, the following requirements also apply:

* - Task

  - Requirements

* - To set to `null`

  - - Can specify `multi: true`.

    - Requires equality filter on the full shard key if ``upsert:
      true`` is specified.

* - To set to a non-`null` value:

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

`update` can be used inside distributed transactions.

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

`update` with `upsert: true` can be run on an existing
collection or a non-existing collection. If run on a non-existing
collection, the operation creates the collection.

**See also:**

transactions-create-collections-indexes

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Update Specific Fields of One Document

Use update operators to update only the
specified fields of a document.

For example, documents in the `movies` collection from the `sample_mflix` database 
contain fields such as `title`, `year`, and `num_mflix_comments`.

The following command uses the `$set` and `$inc`
update operators to update the `year` and the `num_mflix_comments` fields of a
document where the `title` equals `"The Godfather"`:

```javascript
db.runCommand(
   {
      update: "movies",
      updates: [
         {
            q: { title: "The Godfather" }, u: { $set: { year: 1972 }, $inc: { num_mflix_comments: 1 } }
         }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

Because the `<update>` document does not specify the optional
`multi` field, this operation modifies only one document, even if
more than one document matches the `q` query.

See update-command-output for details.

### Update Specific Fields of Multiple Documents

Use update operators to update only the
specified fields of a document, and include the `multi` field set to
`true` in the update statement.

For example, documents in the `movies` collection from the `sample_mflix` database 
contain fields such as `year` and `num_mflix_comments`.

The following command uses the `$inc` update operator to increment
the `num_mflix_comments` field for all movies released in 1924:

```javascript
db.runCommand(
   {
      update: "movies",
      updates: [
         { 
            q: { year: 1924 }, 
            u: { $inc: { num_mflix_comments: 1 }, $set: { classic: true, era: "silent" } }, 
            multi: true 
         }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

Because the `multi` field is set to `true`, the update modifies all 6
documents that match the query specified in the `q` field and returns the
following output:

```javascript
{ n: 6, nModified: 6, ok: 1, '...': '...' }
```

See update-command-output for details.

### Update with Aggregation Pipeline

The `update` command can use an aggregation pipeline for the update. 
The pipeline can consist of the following stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`

Using the aggregation pipeline allows for a more expressive update
statement, such as expressing conditional updates based on current
field values or updating one field using the value of another field(s).

#### Example 1

The following examples uses the aggregation pipeline to modify a field
using the values of the other fields in the document.

Documents in the `users` collection from the `sample_mflix` database 
contain fields such as `name` and `email`.

The following update operation uses an aggregation pipeline to add new fields
to a specific user's document:

```javascript
db.runCommand(
   {
      update: "users",
      updates: [
         { 
            q: { name: "Robert Baratheon" },  
            u: [ 
               { $set: { full_info: { $concat: [ "$name", " - ", "$email" ] } } },
               { $set: { status: "active" } }
            ], 
            multi: false
         }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

**Note:**

The `$set` operation used in the pipeline refers to the aggregation stage
`$set` and not the update operator `$set`.

#### Example 2

The aggregation pipeline allows the update to perform conditional
updates based on the current field values as well as use current field
values to calculate a separate field value.

Documents in the `movies` collection from the `sample_mflix` database 
have a `year` field.

The following example uses an aggregation pipeline to calculate the age of
"The Great Train Robbery" and assign an era classification based on when
it was released.

```javascript
db.runCommand(
   {
      update: "movies",
      updates: [
         { 
            q: { title: "The Great Train Robbery" },  
            u: [ 
                  { $set: { age: { $subtract: [ 2026, "$year" ] } } },
                  { $set: { era: { $switch: { 
                                       branches: [
                                             { case: { $lt: [ "$year", 1960 ] }, then: "Classic" },
                                             { case: { $lt: [ "$year", 1980 ] }, then: "Golden Age" },
                                             { case: { $lt: [ "$year", 2000 ] }, then: "Modern" },                                                   
                                             { case: { $gte: [ "$year", 2000 ] }, then: "Contemporary" }
                                       ],
                                       default: "Unknown" 
                  } } } } 
            ], 
            multi: false
         }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

**Note:**

The `$set` used in the pipeline refers to the aggregation stage
`$set`, and not the update operators `$set`.

First Stage
   The `$set` stage calculates a new field `age` based
   on the difference between 2026 and the movie's release year. See `$subtract`
   for more information.

Second Stage
   The `$set` stage calculates a new field `era` based on
   the `year` field using conditional logic. See
   `$switch` for more information on the `$switch`
   aggregation operator.

### Bulk Update

The following example performs multiple update operations in a single
command to both update existing documents and insert new documents. The operation: 

- marks highly-rated Horror movies from 2015 as `featured`
- categorizes short Drama and Romance movies from 2012 as `melodrama`
- upserts a new Science Fiction movie from 2024 if it doesn't exist

```javascript
db.runCommand(
   {
      update: "movies",
      updates: [
         // Update highly-rated Horror movies from 2015
         { 
            q: { year: 2015, genres: "Horror", "imdb.rating": { $gte: 7 } }, 
            u: { $set: { featured: true } },
            multi: true
         },
         // Update short Drama/Romance movies from 2012
         { 
            q: { year: 2012, genres: { $all: ["Drama", "Romance"] }, runtime: { $lt: 90 } }, 
            u: { $set: { category: "melodrama" } },
            multi: true
         },
         // Upsert a new movie from 2026
         { 
            q: { title: "A New Movie", year: 2026 }, 
            u: { 
               $set: { 
                  genres: ["Sci-Fi", "Adventure"],
                  runtime: 142,
                  "imdb.rating": 8.5,
                  featured: true
               }
            },
            upsert: true
         }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The returned document shows that the command modified existing documents
and inserted a new document via upsert. See update-command-output for details.

```javascript
{
  n: 16,
  upserted: [
    {
      index: 2,
      _id: ObjectId('69861e680e6ea1f51160fe1c')
    }
  ],
  nModified: 15,
  ok: 1,
  '...': '...'
}
```

### Specify Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

Documents in the `movies` collection from the `sample_mflix` database 
have fields such as `title` and `year`.

The following operation uses collation to perform a case-insensitive search.
The query searches for `"the godfather"` in lowercase, but with
`strength: 1` collation, the query matches `"The Godfather"` regardless of
capitalization:

```javascript
db.runCommand({
  update: "movies",
  updates: [
    {
      q: { title: "the godfather" },
      u: { $set: { featured: true } },
      collation: { locale: "en", strength: 1 }
    }
  ]
})
```

### Specify `arrayFilters` for Array Update Operations

When updating an array field, you can specify `arrayFilters` that 
determine which array elements to update.

#### Update Elements Match `arrayFilters` Criteria

Documents in the `movies` collection from the `sample_mflix` database 
have a `languages` array field.

The following example updates all movies that have `"English"` in their 
`languages` array. The operation replaces `"English"` with `"EN"`. 

```javascript
db.runCommand( {
   update: "movies",
   updates: [
      { q: { languages: "English" }, u: { $set: { "languages.$[element]" : "EN" } }, arrayFilters: [ { "element": "English" } ], multi: true}
   ]
} )
```

#### Update Specific Elements of an Array of Documents

Documents in the `movies` collection from the `sample_mflix` database 
have a `cast` array that lists actor names.

The following example finds a movie with the title `"The Godfather"` and 
replaces `"Al Pacino"` with `"REDACTED"` in its `cast` array. The 
`arrayFilters` option specifies which array elements to update:

```javascript
db.runCommand({
   update: "movies",
   updates: [
      { q: { title: "The Godfather" }, u: { $set: { "cast.$[elem]" : "REDACTED" } }, arrayFilters: [ { "elem": "Al Pacino" } ], multi: false }
   ]
})
```

### Specify `hint` for Update Operations

Documents in the `movies` collection from the `sample_mflix` database have 
fields such as `year` and `num_mflix_comments`.

Create the following indexes on the collection:

```javascript
[
   db.movies.createIndex( { year: 1 } ),
   db.movies.createIndex( { num_mflix_comments: 1 } )
]
```

The following update operation increments the `num_mflix_comments` field for
"The Great Train Robbery" and explicitly hints to use the index `{ year: 1 }`:

**Note:**

If you specify an index that does not exist, the operation errors.

```javascript
db.runCommand({
   update: "movies",
   updates: [
      { q: { title: "The Great Train Robbery" }, u: { $inc: { "num_mflix_comments": 1 } }, hint: { year: 1 }, multi: false }
   ]
})
```

To see the index used, you can run `explain` on an update operation.
For example, the following explains an update that increments `num_mflix_comments`
for movies with 5 or fewer comments released in 2000 or later:

```javascript
db.runCommand(
   {
      explain: {
         update: "movies",
         updates: [ 
         { q: { "num_mflix_comments": { $lte: 5 }, "year": { $gte: 2000 } }, u: { $inc: { "num_mflix_comments": 1 } }, hint: { year: 1 }, multi: true }
         ]
      },
      verbosity: "queryPlanner"
   }
)
```

The `explain` does not modify the documents.

### Use Variables in `let` Option or `c` Field

**New in version:** 5.0

Variables can be defined in the let option or
the c field and accessed in the `updates`
array.

**Note:**

To filter results using a variable, you must access the variable
within the `$expr` operator.

Documents in the `movies` collection from the `sample_mflix` database 
have fields such as `title` and `year`.

The following example uses the `let` option to define variables for finding
and adding a new field to a movie.

```javascript
db.runCommand( {
   update: "movies",
   updates: [
      { q: { $expr: { $eq: [ "$title", "$$movieTitle" ] } },
         u: [ { $set: { franchise: "$$franchiseName" } } ] }
   ],
   let : { movieTitle: "The Godfather", franchiseName: "The Godfather Trilogy" }
} )
```

The next example defines `movieTitle` and `franchiseName` variables in
`c` and uses the variables to add a `franchise` field. 

```javascript
db.runCommand( {
   update: "movies",
   updates: [
      { q: { $expr: { $eq: [ "$title", "$$movieTitle" ] } },
         u: [ { $set: { franchise: "$$franchiseName" } } ],
         c: { movieTitle: "The Godfather", franchiseName: "The Godfather Trilogy" } }
      ]
} )
```

## Output

The returned document contains a subset of the following fields:

**`update.ok`**

The status of the command.

**`update.n`**

An `update` command accepts an array of document updates, some of
which can be upserts. For an update, `n` is the
number of documents selected for the update. For an upsert, `n` is
`1` for the inserted document. The server adds the `n` values for
all the updates and upserts and returns the total as `update.n`.

If an update operation
results in no change to the document, e.g. `$set` expression
updates the value to the current value, `n` can be
greater than `nModified`.

**`update.nModified`**

The number of documents updated. If the update operation results in
no change to the document, such as setting the value of the field to
its current value, `nModified` can be less than
`n`.

**Note:**

If a subset of matched documents are updated, such as when an update
would cause some documents to fail schema validation, the value of
`nModified` returned by the `update` command might not be accurate.

**`update.upserted`**

An array of documents that contains information for each document
inserted through the update with `upsert: true`.

Each document contains the following information:

**`update.upserted.index`**

An integer that identifies the update with `upsert:true`
statement in the `updates` array, which uses a zero-based index.

**`update.upserted._id`**

The `_id` value of the added document.

**`update.writeErrors`**

An array of documents that contains information regarding any error
encountered during the update operation. The
`writeErrors` array contains an error document for
each update statement that errors.

Each error document contains the following fields:

**`update.writeErrors.index`**

An integer that identifies the update statement in the
`updates` array, which uses a zero-based index.

**`update.writeErrors.code`**

An integer value identifying the error.

**`update.writeErrors.errmsg`**

A description of the error.

**`update.writeConcernError`**

An array of documents that contains information regarding any
error encountered during the update operation.

**Changed in version:** 7.0.6

(*also available in 6.0.14 and 5.0.30*): When `update` executes
on `mongos`, write concern errors are always
reported, even when one or more write errors occur.
In previous releases, the occurrence of write errors could
cause the `update` to not report write concern errors.

Each error document contains the following fields:

**`update.writeConcernError.code`**

An integer value identifying the cause of the write concern error.

**`update.writeConcernError.errmsg`**

A description of the cause of the write concern error.

**`update.writeConcernError.errInfo.writeConcern`**

The write concern object used for the corresponding operation. For
information on write concern object fields, see wc-specs.

The write concern object may also contain the following field,
indicating the source of the write concern:

**`update.writeConcernError.errInfo.writeConcern.provenance`**

A string value indicating where the write concern originated (known as
write concern `provenance`). The following table shows the possible
values for this field and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

**Changed in version:** 8.1.2

When `update` executes on `mongos` in a sharded cluster, a `writeConcernError` is 
always reported in the response, even when one or more other errors occur. 
In previous releases, other errors sometimes caused `update` to not report write concern errors.

For example, if a document fails validation, triggering a `DocumentValidationFailed` error,
and a write concern error also occurs, both the `DocumentValidationFailed` error and the 
`writeConcernError` are returned in the top-level field of the response.

In addition to the aforementioned update specific return fields, the
`db.runCommand()` includes additional information:

- for replica sets: `optime`, `electionId`, `$clusterTime`, and
  `operationTime`. 
  
- for sharded clusters: `operationTime` and `$clusterTime`.

See db.runCommand Response for details on
these fields.

The following is an example document returned for a successful
`update` command that performed an upsert:

```javascript
{
   "ok" : 1,
   "nModified" : 0,
   "n" : 1,
   "upserted" : [
      {
         "index" : 0,
         "_id" : ObjectId("52ccb2118908ccd753d65882")
      }
   ]
}
```

The following is an example document returned for a bulk update
involving three update statements, where one update statement was
successful and two other update statements encountered errors:

```javascript
{
   "ok" : 1,
   "nModified" : 1,
   "n" : 1,
   "writeErrors" : [
      {
         "index" : 1,
         "code" : 16837,
         "errmsg" : "The _id field cannot be changed from {_id: 1.0} to {_id: 5.0}."
      },
      {
         "index" : 2,
         "code" : 16837,
         "errmsg" : "The _id field cannot be changed from {_id: 2.0} to {_id: 6.0}."
      },
   ]
}
```
