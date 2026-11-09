<!-- Converted from reference/method/BulkWriteResult.txt (reStructuredText). Includes are inlined. -->

# BulkWriteResult()

**`BulkWriteResult()`**

A wrapper that contains the results of the `Bulk.execute()`
method.

## Compatibility

This method is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Properties

The `BulkWriteResult` has the following properties:

**`BulkWriteResult.nInserted`**

The number of documents inserted using the `Bulk.insert()`
method. For documents inserted through operations with the
`Bulk.find.upsert()` option, see the
`nUpserted` field instead.

**`BulkWriteResult.nMatched`**

The number of existing documents selected for update or replacement.
If the update/replacement operation results in no change to an
existing document, e.g. `$set` expression updates the value
to the current value, `nMatched` can be
greater than `nModified`.

**`BulkWriteResult.nModified`**

The number of existing documents updated or replaced. If the
update/replacement operation results in no change to an existing
document, such as setting the value of the field to its current
value, `nModified` can be less than
`nMatched`. Inserted documents do not affect
the number of `nModified`; refer to the
`nInserted` and
`nUpserted` fields instead.

**`BulkWriteResult.nRemoved`**

The number of documents removed.

**`BulkWriteResult.nUpserted`**

The number of documents inserted through operations with the
`Bulk.find.upsert()` option.

**`BulkWriteResult.upserted`**

An array of documents that contains information for each document
inserted through operations with the `Bulk.find.upsert()`
option.

Each document contains the following information:

**`BulkWriteResult.upserted.index`**

An integer that identifies the operation in the
bulk operations list, which uses a zero-based index.

**`BulkWriteResult.upserted._id`**

The `_id` value of the inserted document.

**`BulkWriteResult.writeErrors`**

An array of documents that contains information regarding any error,
unrelated to write concerns, encountered during the update
operation. The `writeErrors` array contains
an error document for each write operation that errors.

Each error document contains the following fields:

**`BulkWriteResult.writeErrors.index`**

An integer that identifies the write operation in the bulk
operations list, which uses a zero-based index. See also
`Bulk.getOperations()`.

**`BulkWriteResult.writeErrors.code`**

An integer value identifying the error.

**`BulkWriteResult.writeErrors.errmsg`**

A description of the error.

**`BulkWriteResult.writeErrors.op`**

A document identifying the operation that failed. For instance,
an update/replace operation error will return a document
specifying the query, the update, the `multi` and the
`upsert` options; an insert operation will return the document
the operation tried to insert.

**`BulkWriteResult.writeConcernError`**

Document describing errors that relate to the write concern.

**Changed in version:** 6.0.14

(*also available in 5.0.30*): When `BulkWriteResult` is
received from `mongos`, write concern errors are
always reported, even when one or more write errors occur.
In previous releases, the occurrence of write errors could
cause the `BulkWriteResult` to not report write concern errors.

Each error document contains the following fields:

**`BulkWriteResult.writeConcernError.code`**

An integer value identifying the cause of the write concern error.

**`BulkWriteResult.writeConcernError.errmsg`**

A description of the cause of the write concern error.

**`BulkWriteResult.writeConcernError.errInfo.writeConcern`**

**New in version:** 4.4

The write concern object used for the corresponding operation. For
information on write concern object fields, see wc-specs.

The write concern object may also contain the following field,
indicating the source of the write concern:

**`BulkWriteResult.writeConcernError.errInfo.writeConcern.provenance`**

A string value indicating where the write concern originated (known as
write concern `provenance`). The following table shows the possible
values for this field and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |
