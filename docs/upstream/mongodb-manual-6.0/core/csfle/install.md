<!-- Converted from core/csfle/install.txt (reStructuredText). Includes are inlined. -->

# Installation Requirements

## Overview

Learn about the applications and libraries you must install to use
Client-Side Field Level Encryption (CSFLE).

## What You Need

Before you can use CSFLE, you must set up the following items
in your development environment:

- (Optional) Download the Automatic Encryption Shared Library. 
  The shared library is a preferred alternative to mongocryptd and
  does not require spawning a new process. `mongocryptd` is still supported.
- Install MongoDB Enterprise Edition.
- Install a MongoDB Driver Compatible with CSFLE.
- Install [OpenSSL](https://docs.openssl.org/master/) *optional*.
- Start a
  MongoDB instance
  or
  Atlas Cluster.
- Install specific driver dependencies. To see the list of
  dependencies for your driver, select the tab corresponding to the language you
  would like to use to complete this guide:

**java-sync:**

| Dependency Name | Description |
|---|---|
| [mongodb-crypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt) | The `mongodb-crypt` library contains bindings to communicate with the native library that manages the encryption. |

**nodejs:**

| Dependency Name | Description |
|---|---|
| [mongodb-client-encryption](https://www.npmjs.com/package/mongodb-client-encryption) | NodeJS wrapper for the `libmongocrypt` encryption library. The `libmongocrypt` library contains bindings to communicate with the native library that manages the encryption. |

**python:**

| Dependency Name | Description |
|---|---|
| [pymongocrypt](https://pypi.org/project/pymongocrypt/) | Python wrapper for the `libmongocrypt` encryption library. The `libmongocrypt` library contains bindings to communicate with the native library that manages the encryption. |

**csharp:**

| Dependency Name | Description |
|---|---|
| x64 Support | CSFLE requires x64 support. |
| [MongoDB.Driver.Encryption](https://www.nuget.org/packages/MongoDB.Driver.Encryption) | Required when using C#/.NET driver version 3.0 or later. This NuGet package is needed to enable automatic encryption. The [libmongocrypt library](https://www.mongodb.com/docs/manual/core/csfle/reference/libmongocrypt/) contains bindings to communicate with the native library that manages the encryption. If your application uses driver version 3.0 or later and runs on linux, install the library manually. Then, set the `LIBMONGOCRYPT_PATH` environment variable to the absolute path to the `libmongocrypt` file. |

**go:**

| Dependency Name | Description |
|---|---|
| csfle-reference-libmongocrypt | The `libmongocrypt` library contains bindings to communicate with the native library that manages the encryption. |

## Learn More

To start using CSFLE, see csfle-quick-start.

To learn how to use CSFLE with a remote Key Management Service
provider, see csfle-tutorial-automatic-encryption.
