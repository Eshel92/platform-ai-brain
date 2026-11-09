<!-- Converted from core/csfle.txt (reStructuredText). Includes are inlined. -->

# Client-Side Field Level Encryption

## Introduction

Client-Side Field Level Encryption (CSFLE) enables you to encrypt data in your
application before you send it over the network to MongoDB. With
CSFLE enabled, no MongoDB product has access to your
data in an unencrypted form.

You can set up CSFLE using the following mechanisms:

- Automatic Encryption: Enables you to perform encrypted read and
  write operations without adding explicit calls to encrypt and
  decrypt fields.
- Explicit Encryption: Enables you to perform encrypted read and write
  operations through your MongoDB driver's encryption library. You must
  specify the logic for encryption with this library throughout your
  application.

## Considerations

When implementing an application that uses Client-Side Field Level Encryption, consider the points listed in Security Considerations.

For limitations, see CSFLE limitations.

### Compatibility

The following table shows which MongoDB server products support which CSFLE
mechanisms:

| Product Name | Supports Automatic Encryption | Supports Explicit Encryption |
|---|---|---|
| \| MongoDB Atlas | \| Yes | \| Yes |
| \| MongoDB Enterprise Advanced | \| Yes | \| Yes |
| \| MongoDB Community Edition | \| No | \| Yes |

To learn which MongoDB drivers support CSFLE, see 
csfle-compatibility-reference.

## Features

To learn about the security benefits of CSFLE for your
applications, see the csfle-features page.

## Install

To learn what you must install to use CSFLE, see
the csfle-install page.

## Quick Start

To start using CSFLE, see the csfle-quick-start.

Throughout this guide, code examples use placeholder text. 
Before you run the examples, substitute your own values for 
these placeholders.

For example:

```go
dek_id := "<Your Base64 DEK ID>"
```

You would replace everything between quotes with your DEK ({+dek-long+}) ID.

```go
dek_id := "abc123"
```

## Fundamentals

To learn how CSFLE works and how to set it up, see the
csfle-fundamentals section.

The fundamentals section contains the following pages:

- csfle-fundamentals-automatic-encryption
- csfle-fundamentals-manual-encryption
- csfle-fundamentals-create-schema
- csfle-reference-keys-key-vaults
- csfle-fundamentals-manage-keys
- csfle-reference-encryption-algorithms

## Tutorials

To learn how to perform specific tasks with CSFLE, see the
csfle-tutorials section.

## Reference

To learn about encryption key management, see qe-reference-keys-key-vaults.

For reference on CSFLE-enabled applications, see the
csfle-reference section:

- csfle-compatibility-reference
- csfle-reference-encryption-limits
- csfle-reference-encryption-schemas
- csfle-reference-server-side-schema
- csfle-reference-automatic-encryption-supported-operations
- csfle-reference-mongo-client
- csfle-reference-kms-providers
- csfle-reference-encryption-components
- csfle-reference-decryption
- csfle-reference-cryptographic-primitives
- csfle-reference-mongocryptd
- csfle-reference-libmongocrypt
