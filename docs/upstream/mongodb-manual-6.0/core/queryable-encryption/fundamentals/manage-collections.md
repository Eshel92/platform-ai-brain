<!-- Converted from core/queryable-encryption/fundamentals/manage-collections.txt (reStructuredText). Includes are inlined. -->

# Encrypted Collection Management

In this guide, you can learn how to manage your encrypted collections,
and the storage and write costs of Queryable Encryption.

## Overview

Queryable Encryption introduces the ability to encrypt sensitive fields in your documents
using randomized encryption, while still being able to query the encrypted
fields.

With Queryable Encryption, a given plaintext value always encrypts to a different
ciphertext, while still remaining queryable. To enable
this functionality, Queryable Encryption uses four data structures:

- Three metadata collections
- A field in every document in the encrypted collection called `__safeContent__`

**Important:**

It is critical that these data structures are not modified or deleted,
or query results **will be** incorrect.

## Metadata Collections

When you create an encrypted collection using Queryable Encryption, MongoDB creates three
metadata collections:

- `enxcol_.<collectionName>.esc`, referred to as `ESC`
- `enxcol_.<collectionName>.ecc`, referred to as `ECC`
- `enxcol_.<collectionName>.ecoc`, referred to as `ECOC`

**Example:**

If you create a collection called "patients", MongoDB creates the
following metadata collections:

- `enxcol_.patients.esc`
- `enxcol_.patients.ecc`
- `enxcol_.patients.ecoc`

When you insert documents with encrypted fields that you wish to query on,
MongoDB updates the metadata collections to maintain an index
that enables you to query. MongoDB refers to this as "indexed field". This
comes at a cost in storage and write speed.

## Storage Costs

Storage and write costs increase based on the number of indexed fields
per document.

**Important:** Technical Preview

MongoDB's guidance during the technical preview is to expect two to
three times the storage requirement for a Queryable Encryption collection and
associated metadata collections. For example, a 1 GB collection may
have a storage requirement of 2-3 GB for associated metadata collections.

This guidance will be tuned in a future release.

## Write Costs

### Insert Operations

When inserting a document, each indexed field requires two writes to
metadata collections.

- One write to `ESC`
- One write to `ECOC`

**Example:**

Inserting a document with two indexed fields requires:

- One write to the encrypted collection.
- Four writes to the metadata collections.

### Update Operations

When updating a document, each indexed field requires four writes to
metadata collections.

- One write to `ESC`
- One write to `ECC`
- Two writes to `ECOC`

**Example:**

Updating a document with two indexed fields requires:

- One write to the encrypted collection.
- Eight writes to the metadata collections.

### Delete Operations

When deleting a document, each indexed field requires two writes to the
metadata collections.

- One write to `ECC`
- One write to `ECOC`

**Example:**

Deleting a document with two indexed fields requires:

- One write into the encrypted collection.
- Four writes to the metadata collections.

## Index Compaction

**Important:** Technical Preview

You are required to run index compaction during the technical preview.
MongoDB plans to automatically run index compaction in a future release.

As you insert, update, and delete documents, the metadata collections
change and grow. Index compaction is a process that prunes the metadata
collections and reduces their size.

You should run index compaction when the size of `ECOC` exceeds 1 GB.

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

**Important:**

You must configure your client for Queryable Encryption to run index compaction.

To run index compaction, use `mongosh` and run the
`db.collection.compactStructuredEncryptionData()` command to reduce
the size of the metadata collections.

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
