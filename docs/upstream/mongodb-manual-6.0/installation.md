<!-- Converted from installation.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB

MongoDB is available in two server editions: *Community* and
*Enterprise*.

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free tier to get started.

This section of the manual contains information on installing
MongoDB. 

- For instructions on upgrading your current deployment to MongoDB
  6.0, see 6.0-upgrade instead.

- For instructions on upgrading to the latest patch release for your
  current version, see /tutorial/upgrade-revision instead.

- For documentation of `mongod`, `mongos`,
  and all other tools distributed with MongoDB, see mongodb-package-components.

## MongoDB Installation Tutorials

MongoDB installation tutorials are available for the following
platforms, for both the Community Edition and the
Enterprise Edition:

| Platform | Community Edition | Enterprise Edition |
|---|---|---|
| Linux | \| /tutorial/install-mongodb-on-red-hat \| /tutorial/install-mongodb-on-ubuntu \| /tutorial/install-mongodb-on-debian \| /tutorial/install-mongodb-on-suse \| /tutorial/install-mongodb-on-amazon | \| /tutorial/install-mongodb-enterprise-on-red-hat \| /tutorial/install-mongodb-enterprise-on-ubuntu \| /tutorial/install-mongodb-enterprise-on-debian \| /tutorial/install-mongodb-enterprise-on-suse \| /tutorial/install-mongodb-enterprise-on-amazon |
| macOS | /tutorial/install-mongodb-on-os-x | /tutorial/install-mongodb-enterprise-on-os-x |
| Windows | /tutorial/install-mongodb-on-windows | /tutorial/install-mongodb-enterprise-on-windows |
| Docker | docker-mongodb-community-install | docker-mongodb-enterprise-install |

## Upgrade Community Edition to Enterprise Edition Tutorials

**Important:**

Do not use these instructions to upgrade to another release version.
To upgrade release versions, refer to the appropriate release
upgrade instructions, such as Upgrade to MongoDB 6.0.

- /tutorial/upgrade-to-enterprise-standalone
- /tutorial/upgrade-to-enterprise-replica-set
- /tutorial/upgrade-to-enterprise-sharded-cluster

## Supported Platforms

**Changed in version:** 3.4

MongoDB no longer supports 32-bit x86 platforms.

**Important:** v5.0 End of Life

v5.0 reached end of life on October 31, 2024 and is no longer 
supported by MongoDB. 

| Platform | Architecture | Edition | 8.0 | 7.0 | 6.0 | 5.0 |
|---|---|---|---|---|---|---|
| Amazon Linux 2023 | x86_64 | Enterprise | ✓ | ✓ |  |  |
| Amazon Linux 2023 | x86_64 | Community | ✓ | ✓ |  |  |
| Amazon Linux V2 | x86_64 | Enterprise |  | ✓ | ✓ | ✓ |
| Amazon Linux V2 | x86_64 | Community |  | ✓ | ✓ | ✓ |
| Debian 12 | x86_64 | Enterprise | ✓ | ✓ |  |  |
| Debian 12 | x86_64 | Community | ✓ | ✓ |  |  |
| Debian 11 | x86_64 | Enterprise |  | ✓ | ✓ | 5.0.8+ |
| Debian 11 | x86_64 | Community |  | ✓ | ✓ | 5.0.8+ |
| Debian 10 | x86_64 | Enterprise |  |  | ✓ | ✓ |
| Debian 10 | x86_64 | Community |  |  | ✓ | ✓ |
| Debian 9 | x86_64 | Enterprise |  |  |  | ✓ |
| Debian 9 | x86_64 | Community |  |  |  | ✓ |
| RHEL/Rocky/Alma/Oracle Linux 9.0+ [#oracle-support]_ | x86_64 | Enterprise | ✓ | ✓ | 6.0.4+ |  |
| RHEL/Rocky/Alma/Oracle Linux 9.0+ [#oracle-support]_ | x86_64 | Community | ✓ | ✓ | 6.0.4+ |  |
| RHEL/Rocky/Alma/Oracle Linux 8.0+ [#oracle-support]_ | x86_64 | Enterprise | ✓ | ✓ | ✓ | ✓ |
| RHEL/Rocky/Alma/Oracle Linux 8.0+ [#oracle-support]_ | x86_64 | Community | ✓ | ✓ | ✓ | ✓ |
| RHEL/Oracle Linux 7.0+ [#oracle-support]_ | x86_64 | Enterprise |  | ✓ | ✓ | ✓ |
| RHEL/Oracle Linux 7.0+ [#oracle-support]_ | x86_64 | Community |  | ✓ | ✓ | ✓ |
| SLES 15 | x86_64 | Enterprise | ✓ | ✓ | ✓ | ✓ |
| SLES 15 | x86_64 | Community | ✓ | ✓ | ✓ | ✓ |
| SLES 12 | x86_64 | Enterprise |  | ✓ | ✓ | ✓ |
| SLES 12 | x86_64 | Community |  | ✓ | ✓ | ✓ |
| Ubuntu 24.04 | x86_64 | Enterprise | ✓ |  |  |  |
| Ubuntu 24.04 | x86_64 | Community | ✓ |  |  |  |
| Ubuntu 22.04 | x86_64 | Enterprise | ✓ | ✓ | 6.0.4+ |  |
| Ubuntu 22.04 | x86_64 | Community | ✓ | ✓ | 6.0.4+ |  |
| Ubuntu 20.04 | x86_64 | Enterprise | ✓ | ✓ | ✓ | ✓ |
| Ubuntu 20.04 | x86_64 | Community | ✓ | ✓ | ✓ | ✓ |
| Ubuntu 18.04 | x86_64 | Enterprise |  |  | ✓ | ✓ |
| Ubuntu 18.04 | x86_64 | Community |  |  | ✓ | ✓ |
| Windows 11 | x86_64 | Enterprise | ✓ | ✓ | ✓ |  |
| Windows 11 | x86_64 | Community | ✓ | ✓ | ✓ |  |
| Windows Server 2022 | x86_64 | Enterprise | ✓ | ✓ | ✓ |  |
| Windows Server 2022 | x86_64 | Community | ✓ | ✓ | ✓ |  |
| Windows Server 2019 | x86_64 | Enterprise |  | ✓ | ✓ | ✓ |
| Windows Server 2019 | x86_64 | Community |  | ✓ | ✓ | ✓ |
| Windows 10 / Server 2016 | x86_64 | Enterprise |  |  | ✓ | ✓ |
| Windows 10 / Server 2016 | x86_64 | Community |  |  | ✓ | ✓ |
| macOS 14 | x86_64 | Enterprise | ✓ |  |  |  |
| macOS 14 | x86_64 | Community | ✓ |  |  |  |
| macOS 13 | x86_64 | Enterprise | ✓ | ✓ |  |  |
| macOS 13 | x86_64 | Community | ✓ | ✓ |  |  |
| macOS 12 | x86_64 | Enterprise |  | ✓ | ✓ |  |
| macOS 12 | x86_64 | Community |  | ✓ | ✓ |  |
| macOS 11 | x86_64 | Enterprise |  | ✓ | ✓ |  |
| macOS 11 | x86_64 | Community |  | ✓ | ✓ |  |
| macOS 10.15 | x86_64 | Enterprise |  |  | ✓ | ✓ |
| macOS 10.15 | x86_64 | Community |  |  | ✓ | ✓ |
| macOS 10.14 | x86_64 | Enterprise |  |  |  | ✓ |
| macOS 10.14 | x86_64 | Community |  |  |  | ✓ |
| macOS 14 | arm64 | Enterprise | ✓ |  |  |  |
| macOS 14 | arm64 | Community | ✓ |  |  |  |
| macOS 13 | arm64 | Enterprise | ✓ | ✓ |  |  |
| macOS 13 | arm64 | Community | ✓ | ✓ |  |  |
| macOS 12 | arm64 | Enterprise |  | ✓ | ✓ |  |
| macOS 12 | arm64 | Community |  | ✓ | ✓ |  |
| macOS 11 | arm64 | Enterprise |  | ✓ | ✓ |  |
| macOS 11 | arm64 | Community |  | ✓ | ✓ |  |
| Amazon Linux 2023 | arm64 | Enterprise | ✓ | ✓ |  |  |
| Amazon Linux 2023 | arm64 | Community | ✓ | ✓ |  |  |
| Amazon Linux 2 | arm64 | Enterprise |  | ✓ | ✓ | ✓ |
| Amazon Linux 2 | arm64 | Community |  | ✓ | ✓ | ✓ |
| RHEL/CentOS/Rocky/Alma 9 | arm64 | Enterprise | ✓ | ✓ | ✓ |  |
| RHEL/CentOS/Rocky/Alma 9 | arm64 | Community | ✓ | ✓ | ✓ |  |
| RHEL/CentOS/Rocky/Alma 8 | arm64 | Enterprise | ✓ | ✓ | ✓ | ✓ |
| RHEL/CentOS/Rocky/Alma 8 | arm64 | Community | ✓ | ✓ | ✓ | ✓ |
| Ubuntu 24.04 | arm64 | Enterprise | ✓ |  |  |  |
| Ubuntu 24.04 | arm64 | Community | ✓ |  |  |  |
| Ubuntu 22.04 | arm64 | Enterprise | ✓ | ✓ | 6.0.4+ |  |
| Ubuntu 22.04 | arm64 | Community | ✓ | ✓ | 6.0.4+ |  |
| Ubuntu 20.04 | arm64 | Enterprise | ✓ | ✓ | ✓ | ✓ |
| Ubuntu 20.04 | arm64 | Community | ✓ | ✓ | ✓ | ✓ |
| Ubuntu 18.04 | arm64 | Enterprise |  |  | ✓ | ✓ |
| Ubuntu 18.04 | arm64 | Community |  |  | ✓ | ✓ |
| RHEL/Rocky/Alma 8 [#RHEL8-tcmalloc-support]_ | ppc64le | Enterprise | ✓ | ✓ | ✓ | ✓ |
| RHEL/CentOS 7 | ppc64le | Enterprise |  |  | 6.0.7+ | ✓ |
| RHEL/Rocky/Alma 9 | s390x | Enterprise | ✓ | ✓ |  |  |
| RHEL/Rocky/Alma 8 | s390x | Enterprise | ✓ | ✓ | ✓ | 5.0.9+ |
| RHEL/CentOS 7 | s390x | Enterprise |  |  | ✓ | ✓ |
| RHEL/CentOS 7 | s390x | Community |  |  |  | ✓ |
