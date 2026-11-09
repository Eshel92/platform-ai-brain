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

## Data Encryption Keys and the Customer Master Key

In-use encryption uses a multi-level key hierarchy to protect your data,
often called "envelope encryption" or "wrapping keys".

A Customer Master Key (CMK ({+cmk-long+})), sometimes called a
Key Management System (KMS ({+kms-long+})) key, is the top-level key you create in your
customer provisioned key provider, such as a cloud KMS. The CMK ({+cmk-long+})
encrypts Data Encryption Keys (DEK ({+dek-long+})), which in turn encrypt the fields
in your documents. Without access to a CMK ({+cmk-long+}), your client 
application cannot decrypt the associated DEKs.

MongoDB stores DEKs, encrypted with your CMK ({+cmk-long+}), in the
Key Vault collection as BSON documents. MongoDB can never decrypt the DEKs, as key management is
client-side and customer controlled.

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

### Key Rotation

You rotate your CMK ({+cmk-long+}) either manually or automatically on your
provisioned key provider. MongoDB has no visibility into this process.
Once you rotate the CMK ({+cmk-long+}), MongoDB uses it to wrap all new DEKs.
It does not re-wrap existing encrypted DEKs. These are still wrapped 
with the prior CMK ({+cmk-long+}).

To rotate some or all of the encrypted DEKs in your key vault, use
the `KeyVault.rewrapManyDataKey()` method. It seamlessly
re-wraps keys with the new CMK ({+cmk-long+}) specified, without interrupting
your application. The DEKs themselves are left unchanged after 
re-wrapping them with the new CMK ({+cmk-long+}).

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
   listIndexes: "keyVault"
}).cursor.firstBatch;
```

Output:

```
[
   { v: 2, key: { _id: 1 }, name: '_id_' },
   {
     v: 2,
     key: { keyAltNames: 1 },
     name: 'keyAltNames_1',
     unique: true
  }
]
```

Chain `cursor.firstBatch` to the `listIndexes` command to return only index
information including the keys and options used to create the index. The output shows that
the `keyAltNames` field has a unique index named `keyAltNames_1`.

If the unique index does not exist, your application must create it
before performing DEK ({+dek-long+}) management.

To learn how to create a MongoDB collection,
see Databases and Collections.

**Tip:** mongosh Feature

The `mongosh` method
`KeyVault.createKey()` automatically creates a
unique index on the `keyAltNames` field if one does not exist.

To view diagrams detailing how your DEK ({+dek-long+}), CMK ({+cmk-long+}), and 
Key Vault collection interact
in all supported KMS ({+kms-long+}) provider architectures, see
csfle-reference-kms-providers.

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

By default, MongoDB stores the Key Vault collection on the cluster that
hosts your data. MongoDB also supports hosting the Key Vault collection
on a different MongoDB deployment. Applications must have access to
both clusters to perform Queryable Encryption operations.

To protect your DEKs, host your Key Vault collection
on a separate MongoDB deployment. Apply tighter security to that
deployment than to the cluster that hosts your data. This additional
control helps prevent unapproved changes to your Key Vault collection
documents, such as changes to the KMS endpoint configuration.

To specify the cluster that hosts your Key Vault collection, use the
`keyVaultClient` field of your client's `MongoClient` object.
To learn more about the CSFLE-specific configuration options in your
client's `MongoClient` object, see csfle-reference-mongo-client.

### Update a Key Vault Collection

To add a DEK ({+dek-long+}) to your Key Vault collection, use the `createKey` method of a
`ClientEncryption` object.

To delete or update a DEK ({+dek-long+}), use one of the following mechanisms:

- The `rewrapManyDataKey` method
- Standard CRUD operations 

To learn more about the `rewrapManyDataKey` method, see the documentation
of the method for your client or driver:

- MongoDB Shell
- [PyMongo](https://pymongo.readthedocs.io/en/stable/api/pymongo/encryption.html#pymongo.encryption.ClientEncryption.rewrap_many_data_key)
- [MongoDB Node.js driver](https://github.com/mongodb/libmongocrypt/tree/master/bindings/node#RewrapManyDataKeyResult)
- [MongoDB {+csharp-driver-short+}](https://mongodb.github.io/mongo-csharp-driver/2.22/html/M_MongoDB_Driver_Encryption_ClientEncryption_RewrapManyDataKey.htm)
- [MongoDB Java driver](https://mongodb.github.io/mongo-java-driver/4.9/apidocs/mongodb-driver-core/com/mongodb/client/model/vault/RewrapManyDataKeyOptions.html)
- [MongoDB Go driver](https://pkg.go.dev/go.mongodb.org/mongo-driver/v2/mongo#ClientEncryption.RewrapManyDataKey)

**Tip:** mongosh Specific Features

`mongosh` provides the following additional
methods for working with your Key Vault collection:

- `getKeyVault()`
- `KeyVault.getKey()`
- `KeyVault.getKeys()`
- `KeyVault.getKeyByAltName()`
- `KeyVault.createKey()`
- `KeyVault.rewrapManyDataKey()`
- `KeyVault.addKeyAlternateName()`
- `KeyVault.removeKeyAlternateName()`

To view a tutorial that shows how to create a DEK ({+dek-long+}), see
the Quick Start.
