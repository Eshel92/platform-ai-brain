<!-- Converted from core/queryable-encryption/fundamentals/manual-encryption.txt (reStructuredText). Includes are inlined. -->

# Explicit Encryption

## Overview

Learn how to use the **explicit encryption** mechanism of Queryable Encryption.

Explicit encryption is a mechanism in which you specify how you would
like to encrypt and decrypt fields in your document in each operation you
perform on your database.

Explicit encryption is available in the following MongoDB products
using version 6.0 or later:

- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas

## Use Explicit Encryption

The following sections provide an overview of using explicit encryption in 
your Queryable Encryption-enabled application:

- qe-fundamentals-manual-encryption-client-enc
- qe-fundamentals-manual-encryption-update-operations
- qe-fundamentals-manual-encryption-automatic-decryption

### Create a `ClientEncryption` Instance

`ClientEncryption` is an abstraction used across drivers and
`mongosh` that encapsulates the Key Vault collection
and KMS ({+kms-long+}) operations involved in explicit encryption.

To create a `ClientEncryption` instance, specify:

- A `kmsProviders` object configured with access to the
  KMS ({+kms-long+}) hosting your Customer Master Key
- The namespace of your Key Vault collection
- If you use MongoDB Community Server, set the `bypassQueryAnalysis`
  option to `True`
- A `MongoClient` instance with access to your Key Vault collection

For more `ClientEncryption` options, see qe-reference-mongo-client. 

**Note:**

Code examples are not currently available but are coming soon.

### Encrypt Fields in Read and Write Operations

You must update read and write operations throughout your application
such that your application encrypts fields before performing
read and write operations.

To encrypt fields, use the `encrypt` method of your `ClientEncryption`
instance. Specify the following:

- The value to be encrypted
- The algorithm used, either `Indexed` or `Unindexed`
- The ID of the Data Encryption Key
- The contention factor (if you are using the `Indexed` algorithm)
- If performing a read operation, set the query type defined for your 
  field (if you are using the `Indexed` algorithm)

**Note:** Query Types

The query type only applies to read operations.

To learn more about query types, see qe-query-types. 

#### Algorithm Choice

Use the `Indexed` algorithm if you specify a `queryType` on the 
field.

`Indexed` supports equality queries. `Indexed` fields require an 
index on the server. The index is created by specifying the 
`encryptedFields` option in `db.createCollection()`. 

### Automatic Decryption

To decrypt your fields automatically, you must configure your
`MongoClient` instance as follows:

- Specify a `kmsProviders` object
- Specify your Key Vault collection
- If you use MongoDB Community Server, set the `bypassQueryAnalysis`
  option to `True`

**Note:** Automatic Decryption is Available in MongoDB Community Server

Although automatic encryption requires MongoDB Enterprise or MongoDB
Atlas, automatic decryption is available in the following MongoDB
products using version 6.0 or later:

- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas

## Server-Side Field Level Encryption Enforcement

qe-specify-fields-for-encryption to enforce 
encryption of specific fields in a collection.

`Indexed` fields require an index on the server. The index is created 
by specifying the `encryptedFields` option in 
`db.createCollection()`.

A client performing Queryable Encryption with the explicit encryption
mechanism on a MongoDB instance configured to enforce encryption
of certain fields must encrypt those fields as specified on
the MongoDB instance.

To learn how to set up server-side Queryable Encryption
enforcement, see qe-fundamentals-encrypt-query.

## Learn More

To learn more about Key Vault collections, Data Encryption Keys, and Customer Master Keys,
see qe-reference-keys-key-vaults.

To learn more about KMS ({+kms-long+}) providers and `kmsProviders` objects,
see qe-fundamentals-kms-providers.
