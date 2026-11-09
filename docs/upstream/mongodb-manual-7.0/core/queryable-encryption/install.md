<!-- Converted from core/queryable-encryption/install.txt (reStructuredText). Includes are inlined. -->

# Install a Queryable Encryption Compatible Driver and Dependencies

## Overview

Learn about the applications and libraries you must install to use
Queryable Encryption.

## What You Need

Before you can use Queryable Encryption, set up the following items
in your development environment:

- (Optional) Download the Automatic Encryption Shared Library. 
  The Automatic Encryption Shared Library replaces mongocryptd and
  does not require spawning a new process.
  
- Install a MongoDB Driver Compatible with Queryable Encryption.
- Start an Atlas cluster by following the steps in Get Started with Atlas, or start a
  MongoDB Enterprise instance

  **Warning:**

  You can use Queryable Encryption only with MongoDB 7.0 and later, which
  may not yet be available in MongoDB Atlas.

  
- Install specific driver dependencies. To see the list of
  dependencies for your driver, select the tab corresponding to the language you
  would like to use to complete this guide:

**java-sync:**

| Dependency Name | Description |
|---|---|
| [mongodb-crypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt) | The `mongodb-crypt` library contains bindings to communicate with the native library that manages the encryption. |

**nodejs:**

* - Dependency Name
  - Description

* - [mongodb-client-encryption](https://www.npmjs.com/package/mongodb-client-encryption)

  - NodeJS wrapper for the `libmongocrypt` encryption library.
    The `libmongocrypt` library contains bindings to communicate
    with the native library that manages the encryption.

    **Note:**

    When using Node.js driver version `6.0.0` or later,
    `mongodb-client-encryption` must have the same major version number as the driver.

    For example, Node.js driver v6.x.x requires `mongodb-client-encryption`
    v6.x.x.

**python:**

| Dependency Name | Description |
|---|---|
| [pymongocrypt](https://pypi.org/project/pymongocrypt/) | Python wrapper for the `libmongocrypt` encryption library. The `libmongocrypt` library contains bindings to communicate with the native library that manages the encryption. |

**csharp:**

| Dependency Name | Description |
|---|---|
| x64 Support | Queryable Encryption requires x64 support. |

**go:**

| Dependency Name | Description |
|---|---|
| qe-reference-libmongocrypt | The `libmongocrypt` library contains bindings to communicate with the native library that manages the encryption. |

## Learn More

To start using Queryable Encryption, see qe-quick-start.

To learn how to use Queryable Encryption with a remote Key Management System, see qe-tutorial-automatic-encryption.
