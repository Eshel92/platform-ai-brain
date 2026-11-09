<!-- Converted from installation.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB

MongoDB is available in two server editions: *Community* and
*Enterprise*.

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

This section contains information on installing MongoDB.

- To upgrade your current deployment to MongoDB 7.0, see
  7.0 Upgrade Procedures.

- To upgrade to the latest patch release for your current version,
  see upgrade-to-latest-revision.

- For documentation of `mongod`, `mongos`,
  and all other tools distributed with MongoDB, see mongodb-package-components.

## MongoDB Installation Tutorials

**Note:**

If you installed MongoDB using a package manager such as APT, DNF,
or Zypper, use your operating system's package management tool to
upgrade within Patch Releases.
For Major and Rapid
follow the installation instructions for your OS.

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

For general guidance on MongoDB version numbering, release types, and
upgrade paths, see versions-and-upgrade-paths.

- /tutorial/upgrade-to-enterprise-standalone
- /tutorial/upgrade-to-enterprise-replica-set
- /tutorial/upgrade-to-enterprise-sharded-cluster

## Supported Platforms

For details on supported platforms, see:

- landing-enterprise-platform-support

- landing-community-platform-support
