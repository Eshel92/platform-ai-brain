<!-- Converted from reference/program.txt (reStructuredText). Includes are inlined. -->

# MongoDB Package Components

## Core Processes

The core components in the MongoDB package are: 

|  |  |
|---|---|
| `mongod` | the core database process |
| `mongos` | the controller and query router for sharded clusters |
| `mongosh` | the interactive shell |

 

## Windows Services

The `mongod.exe` and `mongos.exe` describe the
options available for configuring MongoDB when running as a Windows
Service. The `mongod.exe` and `mongos.exe` binaries
provide a superset of the `mongod` and `mongos`
options.

- /reference/program/mongod.exe
- /reference/program/mongos.exe

## Security Tools

`mongoldap` and `mongokerberos` provide a
method for validating a system's LDAP or Kerberos configuration
respectively, and for testing that the authentication process for each
succeeds for a given username.

## MongoDB Compass

MongoDB is packaged with an `install_compass` script, which
is a platform-specific installer for
MongoDB Compass Community Edition.
