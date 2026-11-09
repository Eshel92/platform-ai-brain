<!-- Converted from core/csfle/reference/compatibility.txt (reStructuredText). Includes are inlined. -->

# CSFLE Compatibility

This page describes the MongoDB and driver versions with which Client-Side Field Level Encryption
is compatible.

## MongoDB Edition and Version Compatibility

Automatic encryption
with Client-Side Field Level Encryption is only available with MongoDB Enterprise Edition,
version 4.2 or later.

Manual encryption with
Client-Side Field Level Encryption is available with MongoDB Community and Enterprise Edition,
version 4.2 or later.

## Driver Compatibility Table

Client-Side Field Level Encryption is only available the following official compatible driver
versions or later:

| Driver | Supported Versions | Quickstarts / Tutorials |
|---|---|---|
| `Node` | `3.4.0+` | \| [Node.js Quickstart](https://mongodb.github.io/node-mongodb-native/3.4/reference/client-side-encryption/) \| `Client-Side Field Level Encryption Guide` |
| `Java (Synchronous)` | `3.11.0+` | \| [Java Driver Quickstart](https://mongodb.github.io/mongo-java-driver/3.12/driver/tutorials/client-side-encryption/) \| [Java Async Driver Quickstart](https://mongodb.github.io/mongo-java-driver/3.12/driver-async/tutorials/client-side-encryption/) \| `Client-Side Field Level Encryption Guide` |
| [Java Reactive Streams](https://mongodb.github.io/mongo-java-driver-reactivestreams/1.13/) | `1.12.0+` | [Java RS Documentation](https://mongodb.github.io/mongo-java-driver-reactivestreams/1.13/javadoc/) |
| `Python (PyMongo)` | `3.10.0+` | \| [Python Driver Quickstart](https://pymongo.readthedocs.io/en/3.10.0/examples/encryption.html) \| `Client-Side Field Level Encryption Guide` |
| `C#/.NET` | `2.10.0+` | [.NET Driver Quickstart](https://mongodb.github.io/mongo-csharp-driver/2.10/reference/driver/crud/client_side_encryption/) |
| `C++` | `3.6.0` | [C++ Driver Client-Side Field Level Encryption](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/client-side-encryption/) |
| `C` | `1.17.5` | [C Driver Client-Side Field Level Encryption](https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/guides/client-side-field-level-encryption/) |
| `Go` | `1.2+` | [Go Driver Quickstart](https://pkg.go.dev/go.mongodb.org/mongo-driver/mongo?tab=doc#hdr-Client_Side_Encryption/) |
| `Scala` | `2.7.0+` | [Scala Documentation](https://mongodb.github.io/mongo-scala-driver/2.8/) |
| `PHP` | `1.6.0+` | [PHP Driver Quickstart](https://docs.mongodb.com/php-library/current/tutorial/client-side-encryption/) |
| [Ruby](https://docs.mongodb.com/ruby-driver/current/) | `2.12.1+` | [Ruby Driver Quickstart](https://docs.mongodb.com/ruby-driver/current/tutorials/client-side-encryption/) |

**Important:** Key Rotation Support

To use the key rotation API of CSFLE, such as the
`rewrapManyDateKey` method, you must use specific versions
of either your driver's binding package or `libmongocrypt`.

The following list details each driver's key rotation API
dependencies:

- Node.js Driver: Use `mongodb-client-encryption`
  version 2.2.0-alpha.6 or later.
- Java Driver: Use `mongodb-crypt` version 1.5.2 or later.
- pymongo: Use `pymongocrypt` version 1.3.1 or later.
- Go Driver: Use `libmongocrypt` version 1.5.2 or later.
- C#/.NET Driver: Use the MongoDB C#/.NET Driver version 2.17.1 or later.

Please refer to the driver reference documentation for syntax and
implementation examples.
