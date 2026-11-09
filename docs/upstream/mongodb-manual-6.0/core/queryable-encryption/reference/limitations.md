<!-- Converted from core/queryable-encryption/reference/limitations.txt (reStructuredText). Includes are inlined. -->

# Queryable Encryption Limitations

## Atlas Search

Queryable Encryption is incompatible with MongoDB Atlas Search.

## Preview Specific Limitations

**Note:**

The following limitations apply during the technical preview for Queryable Encryption.

### Contention Factor

Contention factor is a setting that helps tune performance based on the
number of concurrent connections.

Contention factor is immutable, and can only be set when specifying a
field for encryption. The default value is `0`.

### Manual Data Key Creation

You must manually create a unique Data Encryption Key for each field you
want to encrypt. In a future release, you will be able to omit the `keyId`
field from your `encryptedFieldsMap` and a Queryable Encryption compatible driver will create the
DEK ({+dek-long+}) automatically.

### Manual Compaction

You will need to manually run index compaction
when your metadata collections exceed 1 GB during the technical preview.
In a future release, compaction will be run automatically when the
metadata collections exceed a defined size.

Compaction is a process that decreases the size of the metadata collections
associated with encrypted fields, and improves performance.

### `encryptedFieldsMap` Modification

Do not modify the `encryptedFieldsMap` passed to your `MongoClient` during the
technical preview. Doing so can result in unexpected and incorrect
behavior when querying.

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

## Topology Support

- Replica sets and sharded clusters are supported
- Standalone deployments are not supported
- Secondary reads are not supported

## Sharding

- Metadata collections must not be sharded
- Shard keys must not be encrypted fields

## CRUD

- Queryable Encryption does not support batch operations. The following operations are
  not supported:
  - `db.collection.insertMany()`
  - `db.collection.updateMany()`
  - `db.collection.deleteMany()`

- Queryable Encryption limits `db.collection.findAndModify()` arguments.
  - `fields` is not allowed
  - `new` must be false

## Collections

- Queryable Encryption supports new collections only. You cannot add or remove Queryable Encryption
  to existing collections.
- You cannot specify `jsonSchema` to `db.createCollection()`
  when creating a Queryable Encryption collection if the `jsonSchema` contains the
  `encrypt` keyword. You cannot use Client-Side Field Level Encryption with Queryable Encryption on the same
  collection.
- You can specify both `encryptedFields` and `jsonSchema` to
  `db.createCollection()` as long as your jsonSchema
  does not contain validation for encrypted fields.
- Queryable Encryption does not support automatic migration from an unencrypted collection.
  You must import the documents one-by-one.
- Queryable Encryption does not support migration from collections encrypted with Client-Side Field Level Encryption.
  You must decrypted your documents and import them one-by-one.
- Queryable Encryption does not support views-landing-page,
  manual-timeseries-collection, or capped collection.
- Queryable Encryption does not support index-feature-ttl or index-type-unique.
- You cannot rename a collection with encrypted fields.
- You cannot disable `jsonSchema` validation.

  - Automatic Encryption document validation when `encryptedFields` is
    present in the collection information.
  - You cannot set `validationLevel` to `none`.
  - You cannot set `validationAction` to `warn`.

### Drop Collection

- Dropping collections from a `MongoClient` that is not configured for Queryable Encryption
  *will not* drop the associated metadata collections.`mongod` logs a
  warning if you drop a collection with encrypted fields before dropping
  the metadata collections.

**Tip:**

Queryable Encryption compatible drivers drop the metadata collections when
dropping the collection when using a `MongoClient` configured for Queryable Encryption.

### Create Collection

You should always explicitly create collections for use with Queryable Encryption. Using
implicit collection creation will not create necessary indexes and
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

While MongoDB version 6.0 or later compatible drivers configured for automatic
encryption have supported operations for automatic encryption,
for unsupported read and write operations the underlying support library
cannot introspect the collection catalog to identify the default
collation. Applications therefore cannot rely on the Queryable Encryption
validation to prevent querying on encrypted fields with
collation defaults.

## Unique Indexes

Unique indexes *cannot* guarantee
uniqueness if the index key specifies any
encrypted fields.

Queryable Encryption *always* produces a different encrypted value given a specific input.
The server considers each encrypted value unique even though the decrypted
value may not be unique. The collection could therefore contain multiple
documents with duplicate plaintext values for fields with an index-enforced
unique constraint.

While MongoDB version 6.0 or later compatible drivers configured for
automatic encryption have supported operations for automatic encryption
for unsupported read and write operations, the underlying support library
cannot introspect the index catalog to identify a given field as unique.
Applications cannot rely on automatic encryption validation to prevent
unique constraint violations on randomly-encrypted fields.

## The _id Field

You cannot instruct Queryable Encryption to encrypt the `_id` field because it relies on
the value auto-generated by MongoDB.

## Read/Write Query Support

Automatic encryption supports a subset of commands, query operators,
update operators, aggregation stages, and aggregation expressions. For
complete documentation, see Supported Operations for Automatic Encryption.
