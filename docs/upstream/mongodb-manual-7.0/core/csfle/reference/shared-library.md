<!-- Converted from core/csfle/reference/shared-library.txt (reStructuredText). Includes are inlined. -->

# Automatic Encryption Shared Library for CSFLE

## Overview

The Automatic Encryption Shared Library is a **dynamic library** that enables your client
application to perform Client-Side Field Level Encryption.
A dynamic library is a set of functionality accessed
by an application at runtime rather than compile time.
The Automatic Encryption Shared Library performs the following tasks:

- Reads the encryption schema to determine which fields to encrypt or decrypt
- Prevents your application from executing unsupported operations on encrypted
  fields

The Automatic Encryption Shared Library *does not* do any of the following:

- Perform data encryption or decryption
- Access the encryption key material
- Listen for data over the network

The Automatic Encryption Shared Library is a preferred alternative to `mongocryptd` and does
not require you to spawn another process to perform automatic encryption.

**Tip:**

While we recommend using the Automatic Encryption Shared Library, `mongocryptd` is still supported.

To learn more about `mongocryptd`, see csfle-reference-mongocryptd.

To learn more about automatic encryption, see
csfle-features.

## Download the Automatic Encryption Shared Library

Download the Automatic Encryption Shared Library from the [MongoDB Download Center](https://www.mongodb.com/try/download/enterprise) by selecting the
version and platform, then the library: 

#. In the Version dropdown, select `{+shared-library-version+} (current)`.
#. In the Platform dropdown, select your platform.
#. In the Package dropdown, select `crypt_shared`.
#. Click Download.

**Tip:**

To view an expanded list of available releases and packages, see
[MongoDB Enterprise Downloads](https://www.mongodb.com/download-center/enterprise/releases).

## Configuration

You can configure how your driver searches for the Automatic Encryption Shared Library
through the following parameters:

| Name | Description |
|---|---|
| cryptSharedLibPath | \| Specifies the absolute path to the Automatic Encryption Shared Library package, \| `crypt_shared`. \| **Default**: `undefined` |
| cryptSharedLibRequired | \| Specifies if the driver must use the Automatic Encryption Shared Library. If `true`, \| the driver raises an error if the Automatic Encryption Shared Library is unavailable. \| If `false`, the driver performs the following sequence of actions: #. Attempts to use the Automatic Encryption Shared Library. #. If the Automatic Encryption Shared Library is unavailable, the driver attempts to spawn and connect to `mongocryptd`. \| **Default**: `false` |

To view an example demonstrating how to configure these parameters, see
the Quick Start.
