<!-- Converted from core/queryable-encryption/fundamentals/manage-collections.txt (reStructuredText). Includes are inlined. -->

# Encrypted Collection Management

It is important that you understand the performance and storage costs of field level encryption. Each encrypted field:

- Adds writes to insert and update operations.
- Requires additional storage, because MongoDB maintains an encrypted field index.

This section lists the writes per operation and explains how to compact
encrypted collection indexes so that you can minimize write and storage
costs.

## Overview

Queryable Encryption introduces the ability to encrypt sensitive fields in your documents
using randomized encryption, while still being able to query the encrypted
fields.

With Queryable Encryption, a given plaintext value always encrypts to a different
ciphertext, while still remaining queryable. To enable
this functionality, Queryable Encryption uses three data structures:

- Two metadata collections
- A field in every document in the encrypted collection called `__safeContent__`

**Important:**

It is critical that these data structures are not modified or
deleted, or query results will be incorrect.

## Metadata Collections

When you create an encrypted collection, MongoDB creates two
metadata collections:

- `enxcol_.<collectionName>.esc`, referred to as `ESC`
- `enxcol_.<collectionName>.ecoc`, referred to as `ECOC`

**Example:**

If you create a collection called "patients", MongoDB creates the
following metadata collections:

- `enxcol_.patients.esc`
- `enxcol_.patients.ecoc`

When you insert documents with a queryable encrypted field,
MongoDB updates the metadata collections to maintain an index
that enables querying. The field becomes an "indexed field". This
comes at a cost in storage and write speed for every such field.

## Dropping Encrypted Collections

When you drop an encrypted collection, drop the associated
metadata collections `enxcol_.<collectionName>.esc` and
`enxcol_.<collectionName>.ecoc` immediately afterwards. Otherwise,
re-creating the collection with the same name puts the metadata
collections in a conflicted state that consumes excess storage space and
degrades CRUD performance.

## Storage Costs

Storage and write costs increase based on the number of indexed fields
per document.

**Important:**

Expect a Queryable Encryption collection to have 2-3 times the storage requirements
of the documents, to account for metadata collections. For example, a
1 GB collection may have a storage requirement of 2-3 GB.

## Write Costs

### Insert Operations

When inserting a document, each indexed field requires two additional writes to
metadata collections.

- One write to `ESC`
- One write to `ECOC`

**Example:**

Inserting a document with two indexed fields requires:

- One write to the encrypted collection.
- Four writes to the metadata collections.

### Update Operations

When updating a document, each indexed field requires two additional writes to
metadata collections.

- One write to `ESC`
- One write to `ECOC`

**Example:**

Updating a document with two indexed fields requires:

- One write to the encrypted collection.
- Four writes to the metadata collections.

### Delete Operations

When deleting a document, indexed fields do not require any additional writes.

## Metadata Collection Compaction

As you insert or update documents, the metadata collections
change and grow. Metadata collection compaction prunes the metadata
collections and reduces their size.

**Important:**

You must manually run metadata collection compaction. Compaction only
works on clients configured for Queryable Encryption.

Run compaction when the size of `ECOC` exceeds 1 GB.

You can check the size of your collections using `mongosh`
and issuing the `db.collection.totalSize()` command.

**Example:**

In this example, the encrypted collection is named "patients".

```javascript
db.enxcol_.patients.ecoc.totalSize()
```

Output:

```sh
1407960328
```

To run metadata collection compaction, use `mongosh` and
run the `db.collection.compactStructuredEncryptionData()` command to
reduce the size of the metadata collections.

**Example:**

```javascript
const eDB = "encryption"
const eKV = "__keyVault"
const secretDB = "records"
const secretCollection = "patients"
const localKey = fs.readFileSync("master-key.txt")

const localKeyProvider = { key: localKey }

const queryableEncryptionOpts = {
  kmsProviders: { local: localKeyProvider },
  keyVaultNamespace: `${eDB}.${eKV}`,
}

const encryptedClient = Mongo("localhost:27017", queryableEncryptionOpts)

const encryptedDB = encryptedClient.getDB(secretDB)
const encryptedCollection = encryptedDB.getCollection(secretCollection)
encryptedCollection.compactStructuredEncryptionData()
```

Output:

```json
{
  "stats": {
     ...
  },
  "ok": 1,
  ...
}
```
