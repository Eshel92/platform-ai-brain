<!-- Converted from core/queryable-encryption/reference/compatibility.txt (reStructuredText). Includes are inlined. -->

# Queryable Encryption Compatibility

This page describes the MongoDB and driver versions with which Queryable Encryption
is compatible.

→ Use the **Select your language** drop-down menu to select your driver
and see its compatibility with Queryable Encryption.

## MongoDB Edition, Topology, and Version Compatibility

Queryable Encryption with automatic encryption is only available with MongoDB Enterprise
Edition and MongoDB Atlas. You can use Queryable Encryption on a
MongoDB replica set or sharded cluster, but not a standalone instance.

Explicit encryption is
available with MongoDB Community and Enterprise Edition.

## Driver Compatibility

**c:**

To use Queryable Encryption with the `C` driver, install the following components:

- Driver version 1.24.0 or later
- libmongocrypt version 1.8.0 or later

**cpp:**

To use Queryable Encryption with the `C++` driver, install the following components:

- Driver version 3.8.0 or later
- libmongocrypt version 1.8.0 or later

**csharp:**

To use Queryable Encryption with the `.NET/C#` driver, install driver version
2.20.0 or later.

(Include not available offline: /includes/installation/libmongocrypt-csharp.txt)

**go:**

To use Queryable Encryption with the `Go` driver, install the following components:

- Driver version 1.12 or later
- libmongocrypt version 1.8.0 or later

**java-sync:**

To use Queryable Encryption with the `Java Sync` driver, install the
following components:

- Driver version 4.10.0 or later
- [mongodb-crypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt)
  version 1.8.0 or later

**java-async:**

To use Queryable Encryption with the [Java Reactive Streams](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/)
driver, install the following components:

- Driver version 4.10.0 or later
- [mongodb-crypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt)
  version 1.8.0 or later

**nodejs:**

To use Queryable Encryption with the `Node.js` driver, install the following components:

- Driver version 5.5.0 or later
- [mongodb-client-encryption](https://www.npmjs.com/package/mongodb-client-encryption/)
  version 2.8.0 or later

(Include not available offline: /includes/installation/libmongocrypt-node.txt)

**php:**

To use Queryable Encryption with the `PHP` driver, install driver version 1.16 or
later.

**python:**

To use Queryable Encryption with `PyMongo`, install the following components:

- Driver version 4.4 or later
- [pymongocrypt](https://pypi.org/project/pymongocrypt/) version 1.6 or later

**ruby:**

To use Queryable Encryption with the `Ruby` driver, install the following components:

- Driver version 2.19 or later
- [libmongocrypt-helper](https://rubygems.org/gems/libmongocrypt-helper/) version
  1.8.0 or later

**rust:**

To use Queryable Encryption with the `Rust` driver, install the following components:

- Driver version 2.4.0 or later
- libmongocrypt version 1.8.0 or later

**scala:**

To use Queryable Encryption with the `Scala` driver, install the following components:

- Driver version 4.10.0 or later
- [mongodb-crypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt) version
  1.8.0 or later
