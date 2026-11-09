<!-- Converted from reference/method/BulkWriteResult.txt (reStructuredText). Includes are inlined. -->

# BulkWriteResult() (mongosh method)

**`BulkWriteResult()`**

A wrapper that contains the results of the `Bulk.execute()`
method.

## Compatibility

This method is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Properties

`BulkWriteResult` has the following properties:

**`BulkWriteResult.acknowledged`**

Boolean indicating whether or not the bulk write was acknowledged.

**`BulkWriteResult.deletedCount`**

Count of deleted documents.

**`BulkWriteResult.insertedCount`**

Count of inserted documents.

**`BulkWriteResult.insertedIds`**

| `mongosh` Version | Description | Example |
|---|---|---|
| v1.x | Array of inserted documents by `ObjectId`. | `[ ObjectId(...), ObjectId(...), ObjectId(...) ]` |
| v2.x | Map from each inserted document index to its `ObjectId`. | `{ 0: ObjectId(...), 1: ObjectId(...), 2: ObjectId(...) }`` |

**`BulkWriteResult.matchedCount`**

Count of matched documents.

**`BulkWriteResult.modifiedCount`**

Count of modified documents.

**`BulkWriteResult.upsertedCount`**

Count of upserted documents.

**`BulkWriteResult.upsertedIds`**

| `mongosh` Version | Description | Example |
|---|---|---|
| v1.x | Array of upserted documents by `ObjectId`. | `[ ObjectId(...), ObjectId(...), ObjectId(...) ]` |
| v2.x | Map from each upserted document index to its `ObjectId`. | `{ 0: ObjectId(...), 1: ObjectId(...), 2: ObjectId(...) }`` |

## writeErrors Exception

If there is a write error while processing the bulk write,
`mongosh` raises an exception that contains a `writeErrors`
property with the following fields:

**`writeErrors`**

An array of documents that contains information regarding any error,
unrelated to write concerns, encountered during the update
operation. `writeErrors` contains an error document for each write 
operation that errors.

Each error document contains the following fields:

**`writeErrors.index`**

Integer that identifies the write operation in the bulk
operations list, which uses a zero-based index. See also
`Bulk.getOperations()`.

**`writeErrors.code`**

Integer value identifying the error.

**`writeErrors.errmsg`**

Description of the error.

**`writeErrors.op`**

A document identifying the operation that failed. For instance,
an update or replace operation error will return a document
specifying the query, the update, the `multi`, and the
`upsert` options. An insert opertation returns the document
the operation tried to insert.

## writeConcernError Exception

If there is a write concern error while processing the bulk write,
`mongosh` raises an exception that contains a `writeConcernError`
property with the following fields:

**`writeConcernError`**

Document describing errors that relate to the write concern.

**Changed in version:** 7.0.6

(*also available in 6.0.14 and 5.0.30*): When `BulkWriteResult` is
received from `mongos`, write concern errors are
always reported, even when one or more write errors occur.
In previous releases, the occurrence of write errors could
cause the `BulkWriteResult` to not report write concern errors.

Each error document contains the following fields:

**`writeConcernError.code`**

Integer value identifying the cause of the write concern error.

**`writeConcernError.errmsg`**

Description of the cause of the write concern error.

**`writeConcernError.errInfo.writeConcern`**

The write concern object used for the corresponding operation. For
information on write concern object fields, see wc-specs.

The write concern object may also contain the following field,
indicating the source of the write concern:

**`writeConcernError.errInfo.writeConcern.provenance`**

A string value indicating where the write concern originated (known as
write concern `provenance`). The following table shows the possible
values for this field and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |
