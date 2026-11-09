<!-- Converted from tutorial/install-mongodb-enterprise-on-ubuntu-tarball.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise on Ubuntu using .tgz Tarball

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to manually install MongoDB 7.0 Enterprise
Edition on LTS (long-term support) releases of Ubuntu Linux using a
downloaded `.tgz` tarball.

MongoDB Enterprise Edition
is available on select platforms and contains support for several
features related to security and monitoring.

### MongoDB Version

This tutorial installs MongoDB 7.0 Enterprise
Edition. To install a different version of MongoDB Enterprise,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

### Installation Method

While you can install MongoDB manually using a downloaded `.tgz`
tarball as described in this document, we recommend using the
`apt` package manager on your system if
possible. Using a package manager automatically installs all needed
dependencies, provides an example `mongod.conf` file,
and simplifies future upgrade and maintenance tasks.

→ See Install MongoDB using the apt Package Manager
for instructions.

## Considerations

### MongoDB Shell, `mongosh`

When you use the `.tgz` package to install the server, you need to
follow the `mongosh installation instructions` to
download and install `mongosh` separately.

### Platform Support

MongoDB 7.0 Enterprise Edition supports the following
64-bit Ubuntu LTS (long-term support) releases on 
x86_64 architecture:

- 22.04 LTS (Long Term Support) ("Jammy")

- 20.04 LTS (Long Term Support) ("Focal")

MongoDB only supports the 64-bit versions of these platforms. To
determine which Ubuntu release your host is running, run the following
command on the host's terminal:

```bash
cat /etc/lsb-release
```

MongoDB 7.0 Enterprise Edition on Ubuntu also supports the
ARM64 architecture on
select platforms.

See prod-notes-supported-platforms for more information.

For earlier MongoDB Enterprise versions that support Ubuntu 16.04
POWER/PPC64LE:

Due to a lock elision bug present in older versions
of the `glibc` package on Ubuntu 16.04 for POWER, you must
upgrade the `glibc` package to at least `glibc 2.23-0ubuntu5`
before running MongoDB. Systems with older versions of the
`glibc` package will experience database server crashes and
misbehavior due to random memory corruption, and are unsuitable
for production deployments of MongoDB

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

## Install MongoDB Enterprise Edition

### Prerequisites

Use the following command to install the required dependencies for the
MongoDB Enterprise `.tgz` tarball:

**ubuntu22:**

```bash
sudo apt-get install libcurl4 libgssapi-krb5-2 libldap-2.5-0 libwrap0 libsasl2-2 libsasl2-modules libsasl2-modules-gssapi-mit snmp openssl liblzma5
```

**ubuntu20:**

```bash
sudo apt-get install libcurl4 libgssapi-krb5-2 libldap-2.4-2 libwrap0 libsasl2-2 libsasl2-modules libsasl2-modules-gssapi-mit openssl liblzma5
```

### Procedure

Follow these steps to manually install MongoDB Enterprise Edition from
the `.tgz`.

**Step 1: Download the tarball.**

After you have installed the required prerequisite packages,
download the MongoDB Enterprise `tgz` tarball from the
following link:

→ [MongoDB Download Center](https://www.mongodb.com/try/download/enterprise)

a. In the Version dropdown, select the version of
   MongoDB to download.

#. In the Platform dropdown, select your operating system
   version and architecture.

#. In the Package dropdown, select tgz.

#. Click Download.

**Step 2: Extract the files.**

Using an archive manager program or the `tar` command, extract
the files. For example, from a system shell, you can extract
using the `tar` command:

```bash
tar -zxvf mongodb-*-7.0.24.tgz
```

**Step 3: (Optional) Ensure binaries in PATH.**

The MongoDB binaries are in the `bin/` directory of the
tarball. You can either:

- Copy the binaries into a directory listed in your `PATH`
  variable, such as `/usr/local/bin` (Update
  `/path/to/the/mongodb-directory/` with your installation
  directory as appropriate)

  ```bash
  sudo cp /path/to/the/mongodb-directory/bin/* /usr/local/bin/
  ```

- Create symbolic links to the binaries from a directory listed
  in your `PATH` variable, such as `/usr/local/bin` (Update
  `/path/to/the/mongodb-directory/` with your installation
  directory as appropriate):

  ```bash
  sudo ln -s  /path/to/the/mongodb-directory/bin/* /usr/local/bin/
  ```

**Step 4: (Optional) Install MongoDB Shell (mongosh).**

`Install` `mongosh` then use the
MongoDB Shell to connect to your deployment.

Download the package for the version of `mongosh` you need from the
[MongoDB Download Center](https://www.mongodb.com/try/download/enterprise) and uncompress the package.

## Run MongoDB Enterprise Edition

### ulimit Considerations

Most Unix-like operating systems limit the system resources that a
process may use. These limits may negatively impact MongoDB operation,
and should be adjusted. See /reference/ulimit for the recommended
settings for your platform. 

**Note:**

If the `ulimit` value for number of open files is under `64000`, MongoDB 
generates a startup warning.

### Configuration

You can configure the MongoDB instance (such as the
data directory and log directory specifications) using
either the command-line options or a configuration file.

### Procedure

Follow these steps to run MongoDB Enterprise Edition. These instructions
assume that you are using the default settings.

**Step 1: Create the data and log directories.**

Create a directory where the MongoDB instance stores its data. For
example:

```bash
sudo mkdir -p /var/lib/mongo
```

Create a directory where the MongoDB instance stores its log. For example:

```bash
sudo mkdir -p /var/log/mongodb
```

The user that starts the MongoDB process must have read and write
permission to these directories. For example, if you intend to run
MongoDB as yourself:

```bash
sudo chown `whoami` /var/lib/mongo     # Or substitute another user
sudo chown `whoami` /var/log/mongodb   # Or substitute another user
```

**Step 2: Run MongoDB.**

To run MongoDB, run the `mongod` process at the system prompt.

```bash
mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork
```

For details on the command-line options `--dbpath` and `--logpath`, see
mongod-options.

**Step 3: Verify that MongoDB has started successfully.**

Verify that MongoDB has started successfully by
checking the process output for the following line in the
log file `/var/log/mongodb/mongod.log`:

```none
[initandlisten] waiting for connections on port 27017
```

You may see non-critical warnings in the process
output. As long as you see the log line shown above, you can safely
ignore these warnings during your initial evaluation of MongoDB.

**Step 4: Begin using MongoDB.**

Start a `mongosh` session on the same host machine as the 
`mongod`. You can run `mongosh`
without any command-line options to connect to a
`mongod` that is running on your localhost with default
port 27017.

```shell
mongosh
```

For more information on connecting using `mongosh`,
such as to connect to a `mongod` instance running
on a different host and/or port, see the
`mongosh documentation`.

To help you start using MongoDB, MongoDB provides Getting
Started Guides in various driver editions. For the
driver documentation, see `Start Developing with MongoDB`.

## Additional Information

### Localhost Binding by Default

By default, MongoDB launches with `bindIp` set to
`127.0.0.1`, which binds to the localhost network interface. This
means that the `mongod` can only accept connections from
clients that are running on the same machine. Remote clients will not be
able to connect to the `mongod`, and the `mongod` will
not be able to initialize a replica set unless this value is set
to a valid network interface which is accessible from the remote clients.

This value can be configured either:

- in the MongoDB configuration file with `bindIp`, or
- via the command-line argument `--bind_ip`

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

For more information on configuring `bindIp`, see
/core/security-mongodb-configuration.
