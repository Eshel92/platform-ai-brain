<!-- Converted from mongostat/mongostat-compatibility-and-installation.txt (reStructuredText). Includes are inlined. -->

# mongostat Compatibility and Installation

This page describes software compatibility and installation for version 
`{+version+}` of `mongostat`.

Starting in MongoDB 4.4, the MongoDB Database Tools are released separately from
the MongoDB Server. The MongoDB Database Tools use their own versioning, with an
initial version of `100.0.0`.

## Compatibility

### MongoDB Server Compatibility

`mongostat` version `{+version+}` supports the following versions
of the MongoDB Server:

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

`mongostat` does not support MongoDB Server versions earlier than
4.2. Attempts to connect to an earlier Server version fail.

### Platform Support

`mongostat` version `{+version+}` is supported on the following
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

The `mongostat` tool is part of the *MongoDB Database Tools* package: 

→ Follow the Database Tools Installation Guide to install `mongostat`.

## Learn More

- mongostat
- mongostat Behavior
- mongostat-examples
