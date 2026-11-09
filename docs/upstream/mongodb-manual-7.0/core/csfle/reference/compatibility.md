<!-- Converted from core/csfle/reference/compatibility.txt (reStructuredText). Includes are inlined. -->

# CSFLE Compatibility

This page describes the MongoDB and driver versions with which Client-Side Field Level Encryption
is compatible.

→ Use the **Select your language** drop-down menu to select your driver
and see its compatibility with Client-Side Field Level Encryption.

## MongoDB Edition and Version Compatibility

Automatic encryption
with Client-Side Field Level Encryption is only available with MongoDB Enterprise Edition,
version 4.2 or later.

Explicit encryption with
Client-Side Field Level Encryption is available with MongoDB Community and Enterprise Edition,
version 4.2 or later.

## Driver Compatibility

**c:**

To use Client-Side Field Level Encryption and the Key Rotation API with the `C` driver, install
driver version 1.17.5 or later.

**cpp:**

To use Client-Side Field Level Encryption and the Key Rotation API with the `C++` driver,
install driver version 3.6.0 or later.

**csharp:**

To use Client-Side Field Level Encryption with the `.NET/C#` driver, install driver version
2.10.0 or later. To use the Key Rotation API, install driver version 2.17.1 or later.

(Include not available offline: /includes/installation/libmongocrypt-csharp.txt)

**go:**

To use Client-Side Field Level Encryption, Explicit Encryption, or the Key Rotation
API with the `Go` driver, install Go driver
version 1.2 or later and install
libmongocrypt version
1.5.2 or later.

**java:**

To use Client-Side Field Level Encryption with the `Java Sync` or
[Java Reactive Streams](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/)
driver, install driver version 3.10.0 or later. To use the Key Rotation API, install
`mongodb-crypt` version 1.7.3 or later.

**java-async:**

To use Client-Side Field Level Encryption with the [Java Reactive Streams](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/)
driver, install driver version 1.12.0 or later. To use the Key Rotation API, install
`mongodb-crypt` version 1.7.3 or later.

**nodejs:**

To use Client-Side Field Level Encryption with the `Node.js` driver, install driver version
3.4.0 or later. To use the Key Rotation API, install [mongodb-client-encryption](https://www.npmjs.com/package/mongodb-client-encryption/) version 2.2.0 - 2.x.

(Include not available offline: /includes/installation/libmongocrypt-node.txt)

**php:**

To use Client-Side Field Level Encryption and the Key Rotation API with the `PHP` driver, install
driver version 1.6.0 or later.

**python:**

To use Client-Side Field Level Encryption with `PyMongo`, install driver version 3.10.0 or
later. To use the Key Rotation API, install [pymongocrypt](https://pypi.org/project/pymongocrypt/) version 1.3.1 or later.

**ruby:**

To use Client-Side Field Level Encryption and the Key Rotation API with the `Ruby` driver,
install driver version 2.12.1 or later.

**rust:**

To use Client-Side Field Level Encryption with the `Rust` driver, install driver version 2.4.0
or later. To use the Key Rotation API, install libmongocrypt version 1.8.0 or later.

**scala:**

To use Client-Side Field Level Encryption and the Key Rotation API with the `Scala` driver,
install driver version 2.7.0 or later.

To learn more about the Key Rotation API, see Rotate Encryption Keys.
