<!-- Converted from core/csfle/reference/encryption-components.txt (reStructuredText). Includes are inlined. -->

# CSFLE Encryption Components

## Diagram

The following diagram illustrates the relationships between a MongoDB
driver or `mongosh` and each component of Client-Side Field Level Encryption
(CSFLE):

(Figure: /images/client-side-field-level-encryption-diagram.svg)

## Components

The following sections discuss the individual components of the preceding
diagram.

### libmongocrypt

`libmongocrypt` is the [Apache-licensed open-source](https://github.com/mongodb/libmongocrypt) core cryptography
library used by the official MongoDB drivers and `mongosh` to 
power Client-Side Field Level Encryption. Some drivers may require specific integration steps to install 
or link the library.

To view steps for installing `libmongocrypt`,
see the libmongocrypt reference page.

### mongocryptd

`mongocryptd` supports automatic encryption and is only available
with MongoDB Enterprise. `mongocryptd` does not perform
cryptographic functions.

To learn more about `mongocryptd`, see
csfle-reference-mongocryptd.

### Key Vault collection

The Key Vault collection is a standard MongoDB collection
that stores all Data Encryption Keys used to encrypt application data.
Data Encryption Keys are themselves encrypted using a Customer Master Key
(CMK ({+cmk-long+})) prior to storage in the Key Vault collection. You can host
your Key Vault collection on a different MongoDB cluster than
the cluster storing your encrypted application data.

To learn more about the Key Vault collection, see
csfle-reference-keys-key-vaults.

### Key Management System

The Key Management System (KMS ({+kms-long+})) stores the
Customer Master Key (CMK ({+cmk-long+})) used to encrypt Data Encryption Keys.

To view a list of all KMS ({+kms-long+}) providers MongoDB supports,
see csfle-reference-kms-providers.

### MongoDB Cluster

The MongoDB cluster which stores the encrypted data may also enforce
Client-Side Field Level Encryption. For more information on server-side schema enforcement,
see csfle-reference-server-side-schema.
