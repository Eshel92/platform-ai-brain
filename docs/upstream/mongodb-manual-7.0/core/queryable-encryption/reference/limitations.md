<!-- Converted from core/queryable-encryption/reference/limitations.txt (reStructuredText). Includes are inlined. -->

# Limitations

## Overview

Consider these limitations and restrictions before enabling Queryable Encryption. Some
operations are unsupported, and others behave differently.

## Atlas Search

Queryable Encryption is incompatible with MongoDB Atlas Search.

## MongoDB Support Limitations

Enabling Queryable Encryption on a collection redacts fields from some diagnostic
commands and omits some operations from the query log. This limits the
data available to MongoDB support engineers, especially when
analyzing query performance. To measure the impact of operations against
encrypted collections, use a third party application performance
monitoring tool to collect metrics.

For details, see the Redaction section.

## Contention Factor

Contention factor is a setting that helps tune performance based on the
number of concurrent operations. When unset, contention uses a default value of
`8`, which provides high performance for most workloads.

You can set the contention factor only when specifying a field for encryption.
Once you specify a field for encryption, the contention factor is immutable.

For more information, see Configuring contention factor.

## Manual Metadata Collection Compaction

Manually run metadata collection compaction
when your metadata collections exceed 1 GB. Compaction decreases the
size of the metadata collections associated with encrypted fields, and
improves performance.

## encryptedFieldsMap Modification

Do not modify the `encryptedFieldsMap` passed to your `MongoClient`. Doing so can
result in unexpected and incorrect behavior when querying.

..
  Queryable Encryption encrypts the set of fields in the  encryptedFieldsMap
  configuration that you pass to your `MongoClient` constructor. If you
  specify a formerly plaintext field in your `encryptedFieldsMap` configuration that
  exists in the collection documents, you can only query on that field for
  documents inserted after you updated your `encryptedFieldsMap` configuration.

  For example, consider a database in which you have inserted documents
  with a plaintext `streetAddress` field. Adding this field to `encryptedFieldsMap`
  and performing subsequent inserts will insert the encrypted value of
  `streetAddress` into the database. The driver will send future queries
  for a specific `streetAddress` as `BinData`. As
  a result, the plaintext values in the original documents will never match
  future queries.

## Read and Write Operation Support

The `mongod` only stores encrypted `BinData` and applies any aggregation expression or query operator
specifying an encrypted field against the `BinData` value. While the
expression or operator may support `BinData` fields, the resulting
value may be incorrect or unexpected when compared to issuing that same
expression or operator against the decrypted value. The `mongod`
throws an error if the expression or operator does not support
`BinData` values.

## Redaction

To improve security, Queryable Encryption redacts fields from some diagnostic commands on encrypted collections, and omits certain operations
from the query log. An encrypted collection is any collection with the
`encryptedFields` option.

### Query Log and Database Profiler Redaction

The CRUD operations below are omitted from the slow operations query log and the Database Profiler `system.profile` collection when you run them on an encrypted collection.

* `aggregate`
* `compactStructuredEncryptionData`
* `count`
* `delete`
* `find`
* `findAndModify`
* `insert`
* `update`
* `db.collection.bulkWrite()`
* The `cleanupStructuredEncryptionData` command

### Command and Aggregation Stage Output Redaction

The `collStats` command and `$collStats`
aggregation stage:

* Omit `"queryExecStats"`
* Omit `"latencyStats"`
* Redact `"WiredTiger"`, if present, to include only the `url` field.

The `currentOp` command and `$currentOp` aggregation stage:

* Omit all fields after `"command"`.
* Redact `"command"` to include only the first element, `$comment`,
  and `$db`.

The `top` command only returns the collection name of
encrypted collections.

The `$planCacheStats` aggregation stage omits
operations against encrypted collections, even though the operations are cached as normal.

## Topology Support

- Replica sets and sharded clusters are supported
- Standalone deployments are not supported
- Secondary reads are not supported

## Sharding

- Metadata collections must not be sharded
- Shard keys must not be encrypted fields
- .. include:: /includes/fact-sharded-transactions-qe-readconcern.rst

## CRUD

- Queryable Encryption does not support multi-document update operations.
  `db.collection.updateMany()` is not supported.
- Queryable Encryption does not support multi-statement update or delete operations.
  `db.collection.bulkWrite()` with more than one update or
  delete operation is not supported.

- Queryable Encryption limits `db.collection.findAndModify()` arguments.

  - `fields` is not allowed
  - `new` must be false

- When performing an upsert operation, any encrypted fields in the
  filter are excluded from the insert.

## Collections

- You cannot use Client-Side Field Level Encryption with Queryable Encryption on the same
  collection.

  - Queryable Encryption does not support migration from collections encrypted with
    Client-Side Field Level Encryption. You must decrypt your documents and insert them
    one-by-one.
  - Queryable Encryption does not support automatic migration from an unencrypted
    collection. You must insert the documents one-by-one.

- Queryable Encryption supports new collections only. You cannot add or remove Queryable Encryption
  to existing collections.
- You cannot rename a collection with encrypted fields.
- You cannot specify `jsonSchema` to `db.createCollection()`
  when creating a Queryable Encryption collection if the `jsonSchema` contains the
  `encrypt` keyword. 

  - You can specify both `encryptedFields` and `jsonSchema` to
    `db.createCollection()` as long as your jsonSchema
    does not contain validation for encrypted fields.

- Queryable Encryption does not support views-landing-page,
  manual-timeseries-collection, or capped collection.
- Queryable Encryption does not support index-feature-ttl or index-type-unique.
- You cannot disable `jsonSchema` validation.
- When a collection uses the `encryptedFields` option:
  
  - You cannot set `validationLevel` to `none`.
  - You cannot set `validationAction` to `warn`.

### Drop Collection

- Dropping collections from a `MongoClient` that is not configured for Queryable Encryption
  doesn't drop the associated metadata collections. `mongod` logs a
  warning if you drop a collection with encrypted fields before dropping
  the metadata collections.

**Tip:**

When dropping a collection with a `MongoClient` configured for
Queryable Encryption, compatible drivers drop the associated metadata
collections as well.

### Create Collection

Always explicitly create any collections that use Queryable Encryption. Implicit collection creation doesn't create the necessary indexes and
metadata collections, resulting in poor query performance.

## Query Types

The query type you specify for a field when creating the collection in
`encryptedFieldsMap` is immutable. You cannot add new query types to an existing field,
and you cannot change the existing query type.

## Encrypted Field Names

Encrypted field names are immutable. For example, if you specify `ssn`
as a field to encrypt, you cannot `$rename` the field name to
`taxPayerID`.

## Views

Applications cannot rely on the automatic encryption
validation to prevent unsupported queries against views on
collections with encrypted fields.

Queries against views on collections
containing values encrypted with Queryable Encryption may return
unexpected or incorrect results if either the underlying view
aggregation pipeline *or* the query references encrypted fields. If
creating a view on a collection containing values encrypted with Queryable Encryption,
avoid operating on encrypted fields to mitigate the
risk of unexpected or incorrect results.

For more information on views, see views.

## Collation

Queryable Encryption ignores user-specified collations or collection default collations.
Encryption obscures the field value and prevents normal collation
behavior. Collation-sensitive queries against encrypted fields may
return unexpected or incorrect results.

For more information on collations, see collation-document-fields.

Queryable Encryption-compatible drivers have a list of supported operations for automatic encryption. For unsupported read and write operations, the underlying support library
cannot introspect the collection catalog to identify the default
collation. Applications therefore cannot rely on the Queryable Encryption
validation to prevent querying on encrypted fields with
collation defaults.

## Indexes on Encrypted Fields

Do not create indexes on encrypted fields. Creating indexes on
encrypted fields that use Queryable Encryption negatively affect performance. Instead, you can 
create an index on the `__safeContent__` field to support queries on encrypted 
fields.

## Unique Indexes

Unique indexes can't guarantee
uniqueness if the index key specifies any encrypted fields.

Queryable Encryption always outputs a different encrypted value, even for the same input. The server considers each encrypted value unique, even though the
decrypted value may not be. This means that even if a collection uses an
index-enforced unique constraint on fields, the collection can still
contain multiple documents with duplicate plaintext values for that 
field.

Queryable Encryption compatible drivers configured for automatic encryption
support some operations for automatic encryption.
For unsupported read and write operations, the underlying
library can't introspect the index catalog to identify a given field as
unique. Applications can't rely on automatic encryption validation to
prevent unique constraint violations on randomly-encrypted fields.

## The _id Field

You cannot configure Queryable Encryption to encrypt the `_id` field because it relies on
the value auto-generated by MongoDB.

## Read/Write Query Support

Automatic encryption supports a subset of commands, query operators,
update operators, aggregation stages, and aggregation expressions. For
the list of supported operations, see Supported Operations for Automatic Encryption.
