<!-- Converted from core/queryable-encryption/reference/compatibility.txt (reStructuredText). Includes are inlined. -->

# Queryable Encryption Compatibility

This page describes the MongoDB and driver versions with which Queryable Encryption
is compatible.

## MongoDB Edition, Topology, and Version Compatibility

Automatic encryption with Queryable Encryption is only available with MongoDB Enterprise
Edition and MongoDB Atlas, version 6.0 or later. You can use Queryable Encryption on a
MongoDB replica set or sharded cluster, but not a standalone instance.

..
  Manual encryption (TODO: link to discussion of manual encryption) with
  Queryable Encryption is available with MongoDB Community and Enterprise Edition,
  version 4.2 or later.

## Driver Compatibility Table

Queryable Encryption is only available the following official compatible driver
versions or later:

| Driver | Encryption Library |
|---|---|
| `Node.js` version `4.7.0` or later. | [mongodb-client-encryption](https://www.npmjs.com/package/mongodb-client-encryption/v/2.2.0-alpha.6) version `2.2.0-alpha.6` or later |
| `C#/.NET` version `2.17.1` or later. | No additional dependency |
| `Java (Synchronous)` version `4.7.1` or later. | [MongoCrypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt) version `1.5.2` or later |
| `Pymongo` version `4.1.1` or later. | [pymongocrypt](https://pypi.org/project/pymongocrypt/) version `1.3.1` or later |
| `Go` version `1.10.0-beta1` or later. | libmongocrypt version `1.5.2` or later |
| `C` version `1.22.0` or later. | libmongocrypt version `1.5.2` or later |
| `PHP` version `1.14.0beta1` or later. | No additional dependency |
| `Ruby` version `2.18.0.beta1` or later. | libmongocrypt version `1.5.2` or later |
