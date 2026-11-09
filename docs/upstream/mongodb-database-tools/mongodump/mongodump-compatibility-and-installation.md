<!-- Converted from mongodump/mongodump-compatibility-and-installation.txt (reStructuredText). Includes are inlined. -->

# mongodump Compatibility and Installation

This page describes software compatibility and installation for version 
`{+version+}` of `mongodump`.

Starting in MongoDB 4.4, the MongoDB Database Tools are released separately from
the MongoDB Server. The MongoDB Database Tools use their own versioning, with an
initial version of `100.0.0`.

## Compatibility

### MongoDB Server Compatibility

`mongodump` version `{+version+}` supports the following versions
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

`mongodump` does not support MongoDB Server versions earlier than
4.2. Attempts to connect to an earlier Server version fail.

**Note:**

`mongodump` also works with Atlas Infinite Database
clusters. For details, see mongodump-behavior.

### Platform Support

`mongodump` version `{+version+}` is supported on these platforms:

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

### Additional Considerations for Ubuntu 18.04

Ubuntu 18.04 may use a non-standard DNS resolver. When you use a
non-standard DNS resolver, `mongodump` returns an error message like:

```shell
error parsing uri: lookup <HOSTNAME> on 127.0.0.53:53: cannot unmarshal DNS message
```

To resolve the problem, edit `/etc/resolv.conf` to point to a
different DNS resolver.

## Installation

The `mongodump` tool is part of the *MongoDB Database Tools* package: 

→ Follow the Database Tools Installation Guide to install `mongodump`.

## Learn More

- mongodump
- mongodump-behavior
- mongodump-examples
