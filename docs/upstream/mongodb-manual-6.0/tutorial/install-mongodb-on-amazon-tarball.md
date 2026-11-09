<!-- Converted from tutorial/install-mongodb-on-amazon-tarball.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community on Amazon Linux using .tgz Tarball

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free tier to get started.

## Overview

Use this tutorial to manually install MongoDB 6.0 Community
Edition on Amazon Linux using a downloaded `.tgz` tarball.

### Verify Linux Distribution

You can verify which Linux distribution you are running by running the
following command on the command-line:

```none
grep ^NAME  /etc/*release
```

The result should be **Amazon Linux** or **Amazon Linux AMI**. If using
a different Linux distribution, please see the
install instructions for your platform.

### MongoDB Version

This tutorial installs MongoDB 6.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

### Installation Method

While MongoDB can be installed manually via a downloaded `.tgz`
tarball as described in this document, it is recommended to use the
`yum` package manager on your system to install MongoDB if
possible. Using a package manager automatically installs all needed
dependencies, provides an example `mongod.conf` file to get you
started, and simplifies future upgrade and maintenance tasks.

→ See Install MongoDB using the yum Package Manager
for instructions.

## Considerations

### MongoDB Shell, `mongosh`

When you use the `.tgz` package to install the server, you need to
follow the `mongosh installation instructions` to
download and install `mongosh` separately.

### Platform Support

**Important:** Amazon Linux 2023 Availability

MongoDB is **not** currently available on Amazon Linux 2023.

MongoDB 6.0 Community Edition supports the following
64-bit Amazon Linux release on 
x86_64 architecture:

- Amazon Linux 2

MongoDB only supports the 64-bit versions of this platform.

MongoDB 6.0 Community Edition on Amazon Linux also supports the
ARM64 architecture on
select platforms.

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

```bash
sudo yum install libcurl openssl xz-libs
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

Using an archive manager program or the `tar` command, extract the
files. For example, to extract from the terminal shell, you can use the
following `tar` command:

**Tip:**

If you downloaded a different MongoDB 6.0 point release,
be sure to modify the command to reflect the correct `.tgz`
file name.

```bash
tar -zxvf mongodb-linux-x86_64-*-6.0.21.tgz
```

**Step 3: Optional. Ensure the binaries are in a directory listed in your `PATH` environment variable.**

The MongoDB binaries are in the `<mongodb-install-directory>/bin`
directory. To avoid having to specify the path to the MongoDB
binaries, add the contents of the
`<mongodb-install-directory>/bin/` directory to a directory in the
`$PATH` such as `/usr/bin/`. For example, you can either:

- Copy the binaries into `/usr/bin/`.

  ```bash
  sudo cp <mongodb-install-directory>/bin/* /usr/bin/
  ```

  **-OR-**

- Create symbolic links to each of these binaries to `/usr/bin/`:

  ```bash
  sudo ln -s /full/path/to/<mongodb-install-directory>/bin/* /usr/bin/
  ```

  Replace `/full/path/to` with the full path to the extracted
  directory contents.

**Step 4: Install the MongoDB Shell (`mongosh`).**

`Install` `mongosh` then use the MongoDB Shell
to connect to your deployment.

Download the package for the version of `mongosh` you need from the
[MongoDB Download Center](https://www.mongodb.com/try/download/community?tck=docs_server) and uncompress the package.

## Run MongoDB Community Edition

ulimit Considerations
   Most Unix-like operating systems limit the system resources that a
   process may use. These limits may negatively impact MongoDB operation,
   and should be adjusted. See /reference/ulimit for the recommended
   settings for your platform. 

   **Note:**

   If the `ulimit` value for number of open files is under `64000`, MongoDB 
   generates a startup warning.

Directories
   By default, a MongoDB instance stores:

   - its data files in `/var/lib/mongo`

   - its log files in `/var/log/mongodb`

   If you installed via the package manager, these default directories are
   created during the installation.

   If you installed manually by downloading the tarballs, you can create
   the directories using `mkdir -p <directory>` or ``sudo mkdir -p
   <directory>`` depending on the user that will run MongoDB. (See your
   linux man pages for information on `mkdir` and `sudo`.)

   By default, MongoDB runs using the `mongod` user account. If you
   change the user that runs the MongoDB process, you **must** also modify
   the permission to the `/var/lib/mongo` and `/var/log/mongodb`
   directories to give this user access to these directories.

   To specify a different log file directory and data file directory, edit
   the `systemLog.path` and `storage.dbPath` settings in
   the `/etc/mongod.conf`. Ensure that the user running MongoDB has
   access to these directories.

### Procedure

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
