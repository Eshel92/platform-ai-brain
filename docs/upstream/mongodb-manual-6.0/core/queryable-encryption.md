<!-- Converted from core/queryable-encryption.txt (reStructuredText). Includes are inlined. -->

# Queryable Encryption

## Introduction

Queryable Encryption gives you the ability to perform the following tasks: 

- Encrypt sensitive data fields from the client-side.
- Store sensitive data fields as fully randomized encrypted data on the database 
  server-side. 
- Run expressive queries on the encrypted data.

These tasks are all completed without the server having knowledge of the data 
it's processing.

Sensitive data is encrypted throughout its lifecycle - in-transit, at-rest, in-use, 
in logs, and backups - and only ever decrypted on the client-side, since only you 
have access to the encryption keys.

Queryable Encryption introduces an industry-first fast, searchable encryption 
scheme developed by the pioneers in encrypted search. The feature supports equality 
and range searches, with additional query types such as prefix, suffix, and substring 
planned for future releases.

You can set up Queryable Encryption using the following mechanisms:

- Automatic Encryption: Enables you to perform encrypted read and
  write operations without you having to write code to specify how to
  encrypt fields.
- Explicit Encryption: Enables you to perform encrypted read and write
  operations through your MongoDB driver's encryption library. You must
  specify the logic for encryption with this library throughout your
  application.

## Considerations

When implementing an application that uses Queryable Encryption, consider the points listed
in Security Considerations.

For other limitations, see Queryable Encryption limitations.

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

To view information to help you develop your Queryable Encryption enabled applications,
see the qe-reference section.

The reference section contains the following pages:

- qe-compatibility-reference
- qe-reference-encryption-limits
- qe-reference-automatic-encryption-supported-operations
- qe-reference-mongo-client
- qe-reference-shared-library
- qe-reference-libmongocrypt
- qe-reference-mongocryptd
