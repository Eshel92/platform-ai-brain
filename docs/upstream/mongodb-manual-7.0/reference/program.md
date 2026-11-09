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

The `mongod.exe` and `mongos.exe` binaries configure
MongoDB as a Windows Service. They provide a superset of the
`mongod` and `mongos` options.

- /reference/program/mongod.exe
- /reference/program/mongos.exe

## Security Tools

`mongoldap` validates a system's LDAP configuration, and
`mongokerberos` validates a system's Kerberos
configuration. Both tools test that authentication succeeds for a
specified username.

## MongoDB Compass

MongoDB is packaged with an `install_compass` script, which
is a platform-specific installer for
MongoDB Compass Community Edition.
