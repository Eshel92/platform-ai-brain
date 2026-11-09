<!-- Converted from reference/method/WriteResult.txt (reStructuredText). Includes are inlined. -->

# WriteResult()

## Definition

**`WriteResult()`**

A wrapper that contains the result status of `mongosh`
write methods.

**See also:**

- `db.collection.insert()`
- `db.collection.update()`
- `db.collection.remove()`

**Note:**

`db.collection.insert()` and
`db.collection.update()` are deprecated. 

The results returned by the replacement methods have a different
format. For output similar to `WriteResult`, consider
using `db.collection.bulkWrite()`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Properties

The `WriteResult` has the following properties:

**`WriteResult.nInserted`**

The number of documents inserted, excluding `upserted` documents.
See `WriteResult.nUpserted` for the number of documents
inserted through an upsert.

**`WriteResult.nMatched`**

The number of documents selected for update. If the update operation
results in no change to the document, e.g. `$set` expression
updates the value to the current value,
`nMatched` can be greater than
`nModified`.

**`WriteResult.nModified`**

The number of existing documents updated. If the update/replacement
operation results in no change to the document, such as setting the
value of the field to its current value,
`nModified` can be less than
`nMatched`.

**`WriteResult.nUpserted`**

The number of documents inserted by an upsert.

**`WriteResult._id`**

The `_id` of the document inserted by an `upsert`. Returned only
if an `upsert` results in an insert.

**`WriteResult.nRemoved`**

The number of documents removed.

**`WriteResult.writeError`**

A document that contains information regarding any error, excluding
write concern errors, encountered during the write operation.

**`WriteResult.writeError.code`**

An integer value identifying the error.

**`WriteResult.writeError.errmsg`**

A description of the error.

**`WriteResult.writeConcernError`**

Document describing errors that relate to the write concern.

**Changed in version:** 6.0.14

(*also available in 5.0.30*): When `WriteResult` is
received from `mongos`, write concern errors are
always reported, even when one or more write errors occur.
In previous releases, the occurrence of write errors could
cause the `WriteResult` to not report write concern errors.

Each error document contains the following fields:

**`WriteResult.writeConcernError.code`**

An integer value identifying the cause of the write concern error.

**`WriteResult.writeConcernError.errmsg`**

A description of the cause of the write concern error.

**`WriteResult.writeConcernError.errInfo.writeConcern`**

The write concern object used for the corresponding operation. For
information on write concern object fields, see wc-specs.

The write concern object may also contain the following field,
indicating the source of the write concern:

**`WriteResult.writeConcernError.errInfo.writeConcern.provenance`**

A string value indicating where the write concern originated (known as
write concern `provenance`). The following table shows the possible
values for this field and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |
