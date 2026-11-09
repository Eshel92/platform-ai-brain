<!-- Converted from reference/command/delete.txt (reStructuredText). Includes are inlined. -->

# delete (database command)

## Definition

**`delete`**

Removes documents from a collection. A single command can contain
multiple delete specifications. MongoDB driver delete methods use
this command internally.

**Changed in version:** 5.0

`deleteMany`, and
`findOneAndDelete`
helper methods

**Tip:**

In `mongosh`, this command can also be run through the `deleteOne`,.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

:returns:

   A document that contains the status of the operation.
   See delete-command-output for details.

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

The command has the following syntax:

```javascript
 db.runCommand(
    {
      delete: <collection>, 
      deletes: [
         { 
           q : <query>, 
           limit : <integer>, 
           collation: <document>,
           hint: <document|string>
         },
         ...
      ],
      comment: <any>,
      let: <document>, // Added in MongoDB 5.0
      ordered: <boolean>,
      writeConcern: { <write concern> },
      maxTimeMS: <integer>
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - delete
  - string
  - .. _delete-command-delete:

    The name of the target collection.

* - deletes
  - array
  - .. _delete-command-deletes:

    An array of one or more delete statements to perform in the named
    collection.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

* - let
  - document
  - .. _delete-let-syntax:

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
    see delete-let-example.

    **New in version:** 5.0

* - ordered
  - boolean
  - .. _delete-command-ordered:

    Optional. If `true`, then when a delete statement fails, return without
    performing the remaining delete statements. If `false`, then when a
    delete statement fails, continue with the remaining delete
    statements, if any. Defaults to `true`.

* - writeConcern
  - document
  - .. _delete-command-wc:

    Optional. Specifies the write concern.
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
              

 
 
Each element of the `deletes` array contains the following fields:
 
 

* - Field
  - Type
  - Description

* - q
  - document
  - .. _deletes-array-q:

    The query that matches documents to delete.

* - limit
  - integer
  - .. _deletes-array-limit:

    The number of matching documents to delete. Specify either a `0` to
    delete all matching documents or `1` to delete a single document.

* - collation
  - document
  - .. _deletes-array-collation:

    Optional. 

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

* - hint
  - Document or string
  - .. _deletes-array-hint:

    Optional. A document or string that specifies the index to use to support the query predicate.

    The option can take an index specification document or the
    index name string.

    If you specify an index that does not exist, the operation
    errors.

    For an example, see ex-delete-command-hint.
 

## Behavior

### Sharded Collections

To use `delete` operations for a sharded
collection that specify the `limit: 1` option: 

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the shard key or the `_id` field in the query
  specification.

### Limits

The total size of all query documents in the `deletes` array must
not exceed the `maximum BSON document size`.

The total number of delete documents in the `deletes` array must not
exceed the `maximum bulk size`.

### Transactions

delete can be used inside distributed transactions.

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
production-considerations.

## Examples

### Limit the Number of Documents Deleted

The following example deletes from the `orders` collection one
document that has the `status` equal to `D` by specifying the
`limit` of `1`:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [ { q: { status: "D" }, limit: 1 } ]
   }
)
```

The returned document shows that the command deleted `1` document.
See delete-command-output for details.

```javascript
{ "ok" : 1, "n" : 1 }
```

**Note:**

To use `delete` operations for a sharded
collection that specify the `limit: 1` option: 

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the shard key or the `_id` field in the query
  specification.

### Delete All Documents That Match a Condition

The following example deletes from the `orders` collection all
documents that have the `status` equal to `D` by specifying the
`limit` of `0`:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [ { q: { status: "D" }, limit: 0 } ],
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The returned document shows that the command deleted `13`
documents. See delete-command-output for details.

```javascript
{ "ok" : 1, "n" : 13 }
```

### Delete All Documents from a Collection

**Note:**

If you are deleting all documents in a large collection, it may be faster 
to drop the collection and recreate it. Before dropping the collection, 
note all indexes on the collection. You must recreate any 
indexes that existed in the original 
collection. If the original collection was sharded, you must also 
shard the recreated collection.

For more information on dropping a collection, see 
`db.collection.drop()`.

Delete all documents in the `orders` collection by specifying an
empty query condition *and* a `limit` of `0`:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [ { q: { }, limit: 0 } ],
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The returned document shows that the command deleted `35`
documents. See delete-command-output for details.

```javascript
{ "ok" : 1, "n" : 35 }
```

### Bulk Delete

The following example performs multiple delete operations on the
`orders` collection:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [
         { q: { status: "D" }, limit: 0 },
         { q: { cust_num: 99999, item: "abc123", status: "A" }, limit: 1 }
      ],
      ordered: false,
      writeConcern: { w: 1, j: true }
   }
)
```

The returned document shows that the command deleted `21`
documents for the two delete statements. See
delete-command-output for details.

```javascript
{ "ok" : 1, "n" : 21 }
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
db.runCommand({
   delete: "myColl",
   deletes: [
     { q: { category: "cafe", status: "a" }, limit: 0, collation: { locale: "fr", strength: 1 } }
   ]
})
```

### Specify `hint` for Delete Operations

In `mongosh`, create a `members` collection
with the following documents:

```javascript
db.members.insertMany([
   { "_id" : 1, "member" : "abc123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 2, "member" : "xyz123", "status" : "A", "points" : 60,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" },
   { "_id" : 3, "member" : "lmn123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 4, "member" : "pqr123", "status" : "D", "points" : 20,  "misc1" : "Deactivated", "misc2" : null },
   { "_id" : 5, "member" : "ijk123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 6, "member" : "cde123", "status" : "A", "points" : 86,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" }
])
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following delete operation explicitly hints to use the index
`{ status: 1 }`:

```javascript
db.runCommand({
   delete: "members",
   deletes: [
     { q: { "points": { $lte: 20 }, "status": "P" }, limit: 0, hint: { status: 1 } }
   ]
})
```

**Note:**

If you specify an index that does not exist, the operation errors.

To see the index used, run `explain` on the operation:

```javascript
db.runCommand(
   {
     explain: {
       delete: "members",
       deletes: [ 
         { q: { "points": { $lte: 20 }, "status": "P" }, limit: 0, hint: { status: 1 } }
       ]
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
uses the variable to delete the strawberry cake flavor:

```javascript
db.runCommand( {
   delete: db.cakeFlavors.getName(),
   deletes: [ {
      q: { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
      limit: 1
   } ],
   let : { targetFlavor: "strawberry" }
} )
```

## Output

The returned document contains a subset of the following fields:

**`delete.ok`**

The status of the command.

**`delete.n`**

The number of documents deleted.

**`delete.writeErrors`**

An array of documents that contains information regarding any error
encountered during the delete operation. The
`writeErrors` array contains an error document for
each delete statement that fails.

Each error document contains the following information:

**`delete.writeErrors.index`**

An integer that identifies the delete statement in the
`deletes` array, which uses a zero-based index.

**`delete.writeErrors.code`**

An integer value identifying the error.

**`delete.writeErrors.errmsg`**

A description of the error.

**`delete.writeConcernError`**

An array of documents that contains information regarding any
error encountered during the delete operation.

**Changed in version:** 7.0.6

(*also available in 6.0.14 and 5.0.30*): When `delete` executes
on `mongos`, write concern errors are always
reported, even when one or more write errors occur.
In previous releases, the occurrence of write errors could
cause the `delete` to not report write concern errors.

Each error document contains the following fields:

**`delete.writeConcernError.code`**

An integer value identifying the cause of the write concern error.

**`delete.writeConcernError.errmsg`**

A description of the cause of the write concern error.

**`delete.writeConcernError.errInfo.writeConcern`**

The write concern object used for the corresponding operation. For
information on write concern object fields, see wc-specs.

The write concern object may also contain the following field,
indicating the source of the write concern:

**`delete.writeConcernError.errInfo.writeConcern.provenance`**

A string value indicating where the write concern originated (known as
write concern `provenance`). The following table shows the possible
values for this field and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

The following is an example document returned for a successful
`delete` command:

```javascript
{ ok: 1, n: 1 }
```

The following is an example document returned for a `delete`
command that encountered an error because it specified a non-existent
index in the `hint` field:

```javascript
{
  n: 0,
  writeErrors: [
    {
      index: 0,
      code: 2,
      errmsg: 'error processing query: ns=test.products: hat $eq "bowler"\n' +
        'Sort: {}\n' +
        'Proj: {}\n' +
        ' planner returned error :: caused by :: hint provided does not correspond to an existing index'
    }
  ],
  ok: 1
}
```
