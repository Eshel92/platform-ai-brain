<!-- Converted from reference/command/insert.txt (reStructuredText). Includes are inlined. -->

# insert (database command)

## Definition

**`insert`**

Inserts one or more documents into a collection and returns a
status document. MongoDB driver insert methods use this command
internally.

   `db.collection.insertMany()` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.insertOne()` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

:returns:

   A document that contains the status of the operation.
   See insert-command-output for details.

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
      insert: <collection>,
      documents: [ <document>, <document>, <document>, ... ],
      ordered: <boolean>,
      maxTimeMS: <integer>,
      writeConcern: { <write concern> },
      bypassDocumentValidation: <boolean>,
      comment: <any>
   }
)
```

  

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `insert` | string | The name of the target collection. |
| `documents` | array | An array of one or more documents to insert into the named collection. |
| `ordered` | boolean | Optional. If `true`, when an insert fails, return without inserting any remaining documents. If `false`, when an insert fails, continue inserting the remaining documents. Defaults to `true`. |
| `maxTimeMS` | non-negative integer | Optional. Specifies a time limit in milliseconds. If you do not specify a value for `maxTimeMS`, operations will not time out. A value of `0` explicitly specifies the default unbounded behavior. MongoDB terminates operations that exceed their allotted time limit using the same mechanism as `db.killOp()`. MongoDB only terminates an operation at one of its designated interrupt points. |
| `writeConcern` | document | Optional. Specifies the write concern. Omit to use the default write concern. Do not explicitly set the write concern for the operation if run in a transaction. To use write concern with transactions, see transactions-write-concern. |
| `bypassDocumentValidation` | boolean | Optional. Enables `insert` to bypass schema validation during the operation. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Behavior

### Size Limit

The total size of all `documents` array elements must not exceed
the `maximum BSON document size`.

The total number of documents in the `documents` array must not
exceed the `maximum bulk size`.

### Schema Validation

The `insert` command adds support for the
`bypassDocumentValidation` option, which lets you bypass
schema validation when
inserting or updating documents in a collection with validation    
rules.

### Transactions

`insert` can be used inside distributed transactions.

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

#### Collection Creation in Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

If you specify an insert on a non-existing collection
in a transaction, MongoDB creates the collection implicitly.

#### Write Concerns and Transactions

Do not explicitly set the write concern for the operation if run in
a transaction. To use write concern with transactions, see
transactions-write-concern.

### Insert Inaccuracies

Even if you encounter a server error during an insert, some documents 
may have been inserted. 

After a successful insert, the system returns `insert.n`, the number 
of documents inserted into the collection. If the insert 
operation is interrupted by a replica set state change,
the system may continue inserting documents. As a result,
`insert.n` may report fewer documents than actually inserted.

## Examples

### Insert a Single Document

Insert a document into the `users` collection:

```javascript
db.runCommand(
   {
      insert: "users",
      documents: [ { _id: 1, user: "abc123", status: "A" } ]
   }
)
```

The operation returns the following document:

```javascript
{ "ok" : 1, "n" : 1 }
```

### Bulk Insert

Insert three documents into the `users` collection:

```javascript
db.runCommand(
   {
      insert: "users",
      documents: [
         { _id: 2, user: "ijk123", status: "A" },
         { _id: 3, user: "xyz123", status: "P" },
         { _id: 4, user: "mop123", status: "P" }
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The operation returns the following document:

```javascript
{ "ok" : 1, "n" : 3 }
```

### Using Insert with `bypassDocumentValidation`

If schema validation
`validationActions` are set to `error`, the insert command returns
an error for documents that fail validation. To insert documents that
violate validation rules, set `bypassDocumentValidation: true`.

Create the `user` collection with a validation rule on the `status`
fields.

The validation rule validates that the status must be "Unknown"
or "Incomplete":

```javascript
db.createCollection("users", { 
   validator:
      { 
         status: {
            $in: [ "Unknown", "Incomplete" ]
         }
      }
})
```

Insert a document that violates the validation rule:

```javascript
db.runCommand({
      insert: "users",
      documents: [ {user: "123", status: "Active" } ]
})
```

The insert returns a write error message:

```javascript
{
   n: 0,
   writeErrors: [
      {
         index: 0,
         code: 121,
         errInfo: {
            failingDocumentId: ObjectId('6197a7f2d84e85d1cc90d270'),
            details: {
               operatorName: '$in',
               specifiedAs: { status: { '$in': [Array] } },
               reason: 'no matching value found in array',
               consideredValue: 'Active'
            }
         },
         errmsg: 'Document failed validation'
      }
   ],
   ok: 1
}
```

Set `bypassDocumentValidation: true` and rerun the insert:

```javascript
db.runCommand({
   insert: "users",
   documents: [ {user: "123", status: "Active" } ], 
   bypassDocumentValidation: true
})
```

The operation succeeds.

To check for documents that violate schema validation rules, use the 
`validate` command.

## Output

The returned document contains a subset of the following fields:

**`insert.ok`**

The status of the command.

**`insert.n`**

The number of documents inserted.

**`insert.writeErrors`**

An array of documents that contains information regarding any error
encountered during the insert operation. The
`writeErrors` array contains an error document for
each insert that errors.

Each error document contains the following fields:

**`insert.writeErrors.index`**

An integer that identifies the document in the
`documents` array, which uses a zero-based index.

**`insert.writeErrors.code`**

An integer value identifying the error.

**`insert.writeErrors.errmsg`**

A description of the error.

**`insert.writeConcernError`**

An array of documents that contains information regarding any
error encountered during the insert operation.

**Changed in version:** 7.0.6

(*also available in 6.0.14 and 5.0.30*): When `insert` executes
on `mongos`, write concern errors are always
reported, even when one or more write errors occur.
In previous releases, the occurrence of write errors could
cause the `insert` to not report write concern errors.

Each error document contains the following fields:

**`insert.writeConcernError.code`**

An integer value identifying the cause of the write concern error.

**`insert.writeConcernError.errmsg`**

A description of the cause of the write concern error.

**`insert.writeConcernError.errInfo.writeConcern`**

The write concern object used for the corresponding operation. For
information on write concern object fields, see wc-specs.

The write concern object may also contain the following field,
indicating the source of the write concern:

**`insert.writeConcernError.errInfo.writeConcern.provenance`**

A string value indicating where the write concern originated (known as
write concern `provenance`). The following table shows the possible
values for this field and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

The following shows an example output for a successful
single-document insert:

```javascript
{ ok: 1, n: 1 }
```

The following shows an example output when one document inserts
successfully and a second document fails:

```javascript
{
   "ok" : 1,
   "n" : 1,
   "writeErrors" : [
      {
         "index" : 1,
         "code" : 11000,
         "errmsg" : "insertDocument :: caused by :: 11000 E11000 duplicate key error index: test.users.$_id_  dup key: { : 1.0 }"
      }
   ]
}
```
