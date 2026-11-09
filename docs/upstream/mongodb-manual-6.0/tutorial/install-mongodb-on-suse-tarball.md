<!-- Converted from tutorial/install-mongodb-on-suse-tarball.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community on SUSE using .tgz Tarball

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free tier to get started.

## Overview

Use this tutorial to manually install MongoDB 6.0 Community
Edition on SUSE Linux Enterprise Server (SLES) using a downloaded
`.tgz` tarball.

### MongoDB Version

This tutorial installs MongoDB 6.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

### Installation Method

While MongoDB can be installed manually via a downloaded `.tgz`
tarball as described in this document, it is recommended to use the
`zypper` package manager on your system to install MongoDB if
possible. Using a package manager automatically installs all needed
dependencies, provides an example `mongod.conf` file to get you
started, and simplifies future upgrade and maintenance tasks.

→ See Install MongoDB using the zypper Package Manager
for instructions.

## Considerations

### MongoDB Shell, `mongosh`

When you use the `.tgz` package to install the server, you need to
follow the `mongosh installation instructions` to
download and install `mongosh` separately.

### Platform Support

**Note:** EOL Notice

- MongoDB 5.0 Community Edition removes support for
  SLES12 on s390x

MongoDB 6.0 Community Edition supports the following
64-bit SUSE Linux Enterprise Server (SLES) releases on 
x86_64 architecture:

- SLES (SUSE Linux Enterprise Server) 15

- SLES (SUSE Linux Enterprise Server) 12

MongoDB only supports the 64-bit versions of these platforms.

See prod-notes-supported-platforms for more information.

### Production Notes

Before deploying MongoDB in a production environment, consider the
/administration/production-notes document which offers
performance considerations and configuration recommendations for
production MongoDB deployments.

## Install MongoDB Community Edition

### Prerequisites

Use the following command to install the dependencies required for the
MongoDB Community `.tgz` tarball:

**suse-15:**

```bash
sudo zypper install libcurl4 libopenssl1_1
```

**suse-12:**

```bash
sudo zypper install libcurl4 libopenssl1_0_0 liblzma5
```

### Procedure

Follow these steps to manually install MongoDB Community Edition from
the `.tgz`.

**Step 1: Download the tarball.**

After you have installed the required prerequisite packages, download
the MongoDB Community `tgz` tarball from the following link:

→ [MongoDB Download Center](https://www.mongodb.com/try/download/community?tck=docs_server)

a. In the Version dropdown, select the version of
   MongoDB to download.

#. In the Platform dropdown, select your operating system
   version and architecture.

#. In the Package dropdown, select tgz.

#. Click Download.

**Step 2: Extract the files from the downloaded archive.**

For example, from a system shell, you can extract using the `tar` command:

```bash
tar -zxvf mongodb-linux-*-6.0.21.tgz
```

**Step 3: Ensure the binaries are in a directory listed in your `PATH` environment variable.**

The MongoDB binaries are in the `bin/` directory of the tarball.
You can either:

- Copy the binaries into a directory listed in your `PATH`
  variable, such as `/usr/local/bin` (Update
  `/path/to/the/mongodb-directory/` with your installation
  directory as appropriate)

  ```bash
  sudo cp /path/to/the/mongodb-directory/bin/* /usr/local/bin/
  ```

- Create symbolic links to the binaries from a directory listed in
  your `PATH` variable, such as `/usr/local/bin` (Update
  `/path/to/the/mongodb-directory/` with your installation
  directory as appropriate):

  ```bash
  sudo ln -s  /path/to/the/mongodb-directory/bin/* /usr/local/bin/
  ```

**Step 4: Install the MongoDB Shell (`mongosh`).**

`Install` `mongosh` then use the MongoDB Shell
to connect to your deployment.

Download the package for the version of `mongosh` you need from the
[MongoDB Download Center](https://www.mongodb.com/try/download/community?tck=docs_server) and uncompress the package.

## Run MongoDB Community Edition

Follow these steps to run MongoDB Community Edition. These instructions
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

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information on configuring `bindIp`, see
/core/security-mongodb-configuration.
