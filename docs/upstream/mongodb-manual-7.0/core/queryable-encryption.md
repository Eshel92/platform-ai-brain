<!-- Converted from core/queryable-encryption.txt (reStructuredText). Includes are inlined. -->

# Queryable Encryption

## Introduction

Queryable Encryption lets you perform the following tasks:

- Encrypt sensitive data fields from the client-side.
- Store sensitive data fields as fully randomized encrypted data on the database
  server-side.
- Run expressive queries on the encrypted data.

The server has no knowledge of the data it processes.

Sensitive data is encrypted throughout its lifecycle: in-transit,
at-rest, in-use, in logs, and in backups. Data is decrypted only
on the client-side, since only you have access to the encryption
keys.

Queryable Encryption introduces an industry-first, fast, searchable encryption
scheme developed by the pioneers in encrypted search. The feature
supports equality and range searches.

You can set up Queryable Encryption using the following mechanisms:

- Automatic Encryption: Enables you to perform encrypted read and
  write operations without adding explicit calls to encrypt and
  decrypt fields.
- Explicit Encryption: Enables you to perform encrypted read and write
  operations through your MongoDB driver's encryption library. You must
  specify the logic for encryption with this library throughout your
  application.

## Considerations

When implementing an application that uses Queryable Encryption, consider the points listed
in Security Considerations.

For limitations, see Queryable Encryption limitations.

### Compatibility

The following table shows which MongoDB server products support which Queryable Encryption
mechanisms:

| Product Name | Supports Automatic Encryption | Supports Explicit Encryption |
|---|---|---|
| \| MongoDB Atlas | \| Yes | \| Yes |
| \| MongoDB Enterprise Advanced | \| Yes | \| Yes |
| \| MongoDB Community Edition | \| No | \| Yes |

To learn which MongoDB drivers support Queryable Encryption, see
qe-compatibility-reference.

### MongoDB Support Limitations

Enabling Queryable Encryption on a collection redacts fields from some diagnostic
commands and omits some operations from the query log. This limits the
data available to MongoDB support engineers, especially when
analyzing query performance. To measure the impact of operations against
encrypted collections, use a third party application performance
monitoring tool to collect metrics.

For details, see qe-redaction.

## Features

To learn about the security benefits of Queryable Encryption for your
applications, see the qe-features page.

## Install

To learn what you must install to use Queryable Encryption, see
the qe-install page.

## Quick Start

To start using Queryable Encryption, see the qe-quick-start.

## Fundamentals

To learn how Queryable Encryption works and how to set it up, see the
qe-fundamentals section.

The fundamentals section contains the following pages:

- qe-fundamentals-encrypt-query
- qe-fundamentals-collection-management
- qe-reference-keys-key-vaults
- qe-fundamentals-manage-keys
- qe-fundamentals-kms-providers

## Tutorials

To learn how to perform specific tasks with Queryable Encryption, see the
qe-tutorials section.

## Reference

For reference, see the qe-reference section.

The reference section contains the following pages:

- qe-compatibility-reference
- qe-reference-encryption-limits
- qe-reference-automatic-encryption-supported-operations
- qe-reference-mongo-client
- qe-reference-shared-library
- qe-reference-libmongocrypt
- qe-reference-mongocryptd
