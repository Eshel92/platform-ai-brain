<!-- Converted from index.txt (reStructuredText). Includes are inlined. -->

# The MongoDB Database Tools Documentation

## Overview of Binaries

The MongoDB Database Tools are a collection of command-line utilities for working
with a MongoDB deployment. The Database Tools include the following
binaries:

|  |  |
|---|---|
| Binary Import / Export |  |
| \|nbspc\| \|nbspc\| `mongodump` | Creates a binary export of the contents of a `mongod` database. |
| \|nbspc\| \|nbspc\| `mongorestore` | Restores data from a `mongodump` database dump into a `mongod` or `mongos`. |
| \|nbspc\| \|nbspc\| `bsondump` | Converts BSON dump files into JSON. |
| Data Import / Export |  |
| \|nbspc\| \|nbspc\| `mongoimport` | Imports content from an Extended JSON, CSV, or TSV export file. |
| \|nbspc\| \|nbspc\| `mongoexport` | Produces a JSON or CSV export of data stored in a `mongod` instance. |
| Diagnostic Tools |  |
| \|nbspc\| \|nbspc\| `mongostat` | Provides a quick overview of the status of a currently running `mongod` or `mongos` instance. |
| \|nbspc\| \|nbspc\| `mongotop` | Provides an overview of the time a `mongod` instance spends reading and writing data. |
| GridFS Tools |  |
| \|nbspc\| \|nbspc\| `mongofiles` | Supports manipulating files stored in your MongoDB instance in GridFS objects. |

You can use the MongoDB Database Tools to migrate from a self-hosted deployment
to [MongoDB Atlas](https://www.mongodb.com/docs/atlas). MongoDB
Atlas is the fully managed service for MongoDB deployments in the
cloud. To learn more, see [Seed with mongorestore](https://www.mongodb.com/docs/atlas/import/mongorestore/).

To learn all the ways you can migrate to MongoDB Atlas, see
[Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/).

## Versioning

**Important:**

It is recommended you always use the latest release version of the 
MongoDB Database Tools. To check your current version of the MongoDB Database Tools, run the 
following command on your terminal:

```shell
mongodump --version
```

To download the latest version, go to the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools).

The MongoDB Database Tools are now released separately
from the MongoDB Server and use their own versioning, with an initial
version of `100.0.0`. Previously, these tools were released
alongside the MongoDB Server and used matching versioning.

## Compatibility

### MongoDB Server Compatibility

MongoDB Database Tools version `{+version+}` supports the following versions
of the MongoDB server:

- MongoDB 9.0
- MongoDB 8.3
- MongoDB 8.2
- MongoDB 8.1
- MongoDB 8.0
- MongoDB 7.0
- MongoDB 6.0
- MongoDB 5.0
- MongoDB 4.4
- MongoDB 4.2

The MongoDB Database Tools do not support MongoDB Server versions earlier than
4.2. Attempts to connect to an earlier Server version fail.

**Note:**

The MongoDB Database Tools also work with Atlas Infinite Database
clusters. For tool-specific details, see mongodump-behavior
and mongorestore-behavior-access-usage.

### Platform Support

The MongoDB Database Tools version `{+version+}` are supported on the following
platforms:

|  | x86_64 | ARM64 | PPC64LE | s390x |
|---|---|---|---|---|
| Amazon Linux 2023 | ✓ | ✓ |  |  |
| Amazon 2 | ✓ | ✓ |  |  |
| Debian 12 | ✓ |  |  |  |
| Debian 11 | ✓ |  |  |  |
| Debian 10 | ✓ |  |  |  |
| Debian 9 | ✓ |  |  |  |
| RHEL (Red Hat Enterprise Linux) / CentOS 9 | ✓ | ✓ | ✓ | ✓ |
| RHEL (Red Hat Enterprise Linux) / CentOS 8 | ✓ |  | ✓ | ✓ |
| RHEL (Red Hat Enterprise Linux) / CentOS 7 | ✓ |  | ✓ | ✓ |
| RHEL (Red Hat Enterprise Linux) / CentOS 6 | ✓ |  |  |  |
| SUSE 15 | ✓ |  |  |  |
| SUSE 12 | ✓ |  |  |  |
| Ubuntu 24.04 | ✓ | ✓ |  |  |
| Ubuntu 22.04 | ✓ | ✓ |  |  |
| Ubuntu 20.04 | ✓ | ✓ |  |  |
| Ubuntu 18.04 | ✓ | ✓ |  |  |
| Ubuntu 16.04 | ✓ | ✓ | ✓ |  |
| Windows 11 and later | ✓ |  |  |  |
| Windows Server 2016 and later | ✓ |  |  |  |
| macOS 11 and later | ✓ | ✓ |  |  |
| macOS 10.12 - 10.15 | ✓ |  |  |  |

## Installation

The MongoDB Database Tools can be downloaded from the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools).

Please see the installation guide for your platform for specific installation instructions.
