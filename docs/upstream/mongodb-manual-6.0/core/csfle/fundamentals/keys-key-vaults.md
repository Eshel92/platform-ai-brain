<!-- Converted from core/csfle/fundamentals/keys-key-vaults.txt (reStructuredText). Includes are inlined. -->

# Keys and Key Vaults

## Overview

In this guide, you can learn details about the following components of
Client-Side Field Level Encryption (CSFLE):

- Data Encryption Keys (DEK ({+dek-long+}))s
- Customer Master Keys (CMK ({+cmk-long+}))s
- Key Vault collections
- Key Management System (KMS ({+kms-long+}))

To view step by step guides demonstrating how to use the preceding
components to set up a CSFLE enabled client, see the following resources:

- csfle-quick-start
- csfle-tutorial-automatic-encryption

## Keys

Your Data Encryption Key (DEK ({+dek-long+})) is the key MongoDB uses to encrypt the fields in your
documents. You store your DEK ({+dek-long+}) in a document in the
Key Vault collection, encrypted with your Customer Master Key (CMK ({+cmk-long+})).

Your Customer Master Key is the key MongoDB uses to encrypt your Data Encryption Keys during creation. Without access to a CMK ({+cmk-long+}), your
client application cannot decrypt the associated DEKs.

If you delete a DEK ({+dek-long+}), all fields encrypted with that
DEK ({+dek-long+}) become permanently unreadable. If you delete a CMK ({+cmk-long+}), all fields encrypted with a DEK ({+dek-long+})
using that CMK ({+cmk-long+}) become permanently unreadable.

**Warning:**

The Customer Master Key is the most sensitive key in Queryable Encryption. If your
CMK ({+cmk-long+}) is compromised, all of your encrypted data can be
decrypted. Use a remote Key Management System to store your CMK ({+cmk-long+}).

**Important:** Use a Remote Key Management Service Provider

Store your Customer Master Key on a remote Key Management System (KMS ({+kms-long+})).

To learn more about why you should use a remote KMS ({+kms-long+}), see
qe-reasons-to-use-remote-kms.

To view a list of all supported KMS ({+kms-long+}) providers, see the
qe-fundamentals-kms-providers page.

To view diagrams detailing how your DEK ({+dek-long+}), CMK ({+cmk-long+}), and 
Key Vault collection interact
in all supported KMS ({+kms-long+}) provider architectures, see
csfle-reference-kms-providers.

## Key Vault Collections

Your Key Vault collection is the MongoDB collection you use to store 
encrypted Data Encryption Key (DEK ({+dek-long+})) documents. DEK ({+dek-long+}) documents
are BSON documents that contain DEKs and have the following structure:

```json
{
  "_id" : UUID(<string>),
  "status" : <int>,
  "masterKey" : {<object>},
  "updateDate" : ISODate(<string>),
  "keyMaterial" : BinData(0,<string>),
  "creationDate" : ISODate(<string>),
  "keyAltNames" : <array>
}
```

You create your Key Vault collection as you would a standard MongoDB
collection. Your Key Vault collection must have a
unique index on the `keyAltNames` field. To
check if the unique index exists, run the `listIndexes`
command against the Key Vault collection:

```json
db.runCommand({
   listIndexes: "__keyVault",
});
```

Output:

```
{
   cursor: {
      id: Long("0"),
      ns: 'encryption.__keyVault',
      firstBatch: [ 
         { v: 2, key: { _id: 1 }, name: '_id_' } 
         ]
   },
   ok: 1,
}
```

If the unique index does not exist, your application must create it
before performing DEK ({+dek-long+}) management.

To learn how to create a MongoDB collection,
see Databases and Collections.

**Tip:** mongosh Feature

The `mongosh` method
`KeyVault.createKey()` automatically creates a
unique index on the `keyAltNames` field if one does not exist.

### Key Vault Collection Name

You may use any non-admin namespace to store your
Key Vault collection. By convention, the examples throughout this
documentation use the  `encryption.__keyVault` namespace.

**Warning:**

Do not use the `admin` database to store encryption-related
collections. If you use the admin database for this collection, your 
MongoDB client may not be able to access or decrypt your data due to 
lack of permissions.

### Permissions

Applications with `read` access to the Key Vault collection can
retrieve encrypted Data Encryption Key (DEK ({+dek-long+}))s by querying the
collection. However, only applications with access to the Customer Master Key
(CMK ({+cmk-long+})) used to encrypt a DEK ({+dek-long+}) can use that DEK ({+dek-long+})
for encryption or decryption. You must grant your application access to
both the Key Vault collection  and your CMK ({+cmk-long+}) to encrypt and 
decrypt documents with a DEK ({+dek-long+}).

To learn how to grant access to a MongoDB collection, see
Manage Users and Roles
in the MongoDB manual.

To learn how to grant your application access to your CMK ({+cmk-long+}), see the
csfle-tutorial-automatic-encryption tutorial.

### Key Vault Cluster

By default, MongoDB stores the Key Vault collection on the connected
cluster. MongoDB also supports hosting the Key Vault collection
on a different MongoDB deployment than the connected cluster.
Applications must have access to both the cluster that hosts your
Key Vault collection and the connection cluster to perform Queryable Encryption operations.

To specify the cluster that hosts your Key Vault collection, use the
`keyVaultClient` field of your client's `MongoClient` object.
To learn more about the CSFLE-specific configuration options in your
client's `MongoClient` object, see csfle-reference-mongo-client.

### Update a Key Vault Collection

To add a DEK ({+dek-long+}) to your Key Vault collection, use the `createKey` method of a
`ClientEncryption` object.

To delete or update a DEK ({+dek-long+}), use standard
CRUD operations. You store a DEK
in MongoDB as a document, and you can apply any document operation to a
DEK.

To view a tutorial that shows how to create a DEK ({+dek-long+}), see
the Quick Start.

**Tip:** mongosh Specific Features

`mongosh` provides the following additional
methods for working with your Key Vault collection:   

- `getKeyVault()`
- `KeyVault.getKey()`
- `KeyVault.getKeys()`
- `KeyVault.getKeyByAltName()`
- `KeyVault.createKey()`
- `KeyVault.addKeyAlternateName()`
- `KeyVault.removeKeyAlternateName()`
