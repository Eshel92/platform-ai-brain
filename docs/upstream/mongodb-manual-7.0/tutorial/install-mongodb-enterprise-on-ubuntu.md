<!-- Converted from tutorial/install-mongodb-enterprise-on-ubuntu.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise Edition on Ubuntu

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Enterprise Edition on
LTS (long-term support) releases of Ubuntu Linux using the
APT package manager.

MongoDB Enterprise Edition
is available on select platforms and contains support for features
related to security and monitoring.

### MongoDB Version

This tutorial installs MongoDB 7.0 Enterprise
Edition. To install a different version of MongoDB Enterprise,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

## Considerations

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

             

### Official MongoDB Packages

To install MongoDB Enterprise on your Ubuntu system, these
instructions will use the official `mongodb-enterprise` package, which is
maintained and supported by MongoDB Inc. The official `mongodb-enterprise`
package always contains the latest version of MongoDB and is available
from its own dedicated repo.

**Important:**

The `mongodb` package provided by Ubuntu is **not**
maintained by MongoDB Inc. and conflicts with the official
`mongodb-enterprise` package. If you already installed the `mongodb`
package on your Ubuntu system, you **must** first uninstall
the `mongodb` package before proceeding with these instructions.

See ubuntu-enterprise-package-content for the complete list of
official packages.

## Install MongoDB Enterprise Edition

Follow these steps to install MongoDB Enterprise Edition using the
APT package manager.

**Step 1: Import the public key.**

From a terminal, install `gnupg` and `curl` if they are not already
available:

```bash
sudo apt-get install gnupg curl
```

To import the MongoDB public GPG key, run the following command:

```bash
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
```

**Step 2: Create the list file.**

Create the list file
`/etc/apt/sources.list.d/mongodb-enterprise-7.0.list` for
your version of Ubuntu.

**jammy:**

Create the list file for Ubuntu 22.04 (Jammy):

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.com/apt/ubuntu jammy/mongodb-enterprise/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise-7.0.list
```

**focal:**

Create the list file for Ubuntu 20.04 (Focal).

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.com/apt/ubuntu focal/mongodb-enterprise/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise-7.0.list
```

**Step 3: Reload the package database.**

Issue the following command to reload the local package database:

```bash
sudo apt-get update
```

**Step 4: Install MongoDB Enterprise Server.**

**latest:**

To install the latest release of MongoDB Enterprise
Server, run the following command:

```bash
sudo apt-get install mongodb-enterprise
```

**specific:**

To install a specific release, you must specify each component package
individually along with the version number.

```sh
sudo apt-get install -y \
   mongodb-enterprise=7.0.24 \
   mongodb-enterprise-database=7.0.24 \
   mongodb-enterprise-server=7.0.24 \
   mongodb-mongosh \
   mongodb-enterprise-shell=7.0.24 \
   mongodb-enterprise-mongos=7.0.24 \
   mongodb-enterprise-tools=7.0.24 \
   mongodb-enterprise-cryptd=7.0.24 \
   mongodb-enterprise-database-tools-extra=7.0.24
```

If you only install
`mongodb-enterprise=7.0.24` and do not
include the component packages, the latest version of each
MongoDB package will be installed regardless of what
version you specified.

Although you can specify any available version of MongoDB,
`apt-get` upgrades the packages when a newer version
becomes available. To prevent unintended upgrades, pin the
package. To pin the version of MongoDB at the currently
installed version, issue the following command sequence:

```bash
echo "mongodb-enterprise hold" | sudo dpkg --set-selections
echo "mongodb-enterprise-server hold" | sudo dpkg --set-selections
echo "mongodb-enterprise-database hold" | sudo dpkg --set-selections
echo "mongodb-mongosh hold" | sudo dpkg --set-selections
echo "mongodb-enterprise-mongos hold" | sudo dpkg --set-selections
echo "mongodb-enterprise-cryptd hold" | sudo dpkg --set-selections
echo "mongodb-enterprise-tools hold" | sudo dpkg --set-selections
echo "mongodb-enterprise-databae-tools-extra hold" | sudo dpkg --set-selections
```

**Note:**

You can also install the MongoDB Shell that uses the system's OpenSSL.
You must have already installed OpenSSL on your system before
installing this version of the MongoDB Shell.

You can install all of the MongoDB Enterprise packages and the
MongoDB Shell that uses the system's OpenSSL without removing the
MongoDB Shell first. For example:

```sh
sudo apt-get install -y mongodb-enterprise mongodb-mongosh-shared-openssl11
```

The following example removes the MongoDB Shell and then installs the
MongoDB Shell that uses the system's OpenSSL 1.1:

```sh
sudo apt-get remove -y mongodb-mongosh && sudo apt-get install -y
mongodb-mongosh-shared-openssl11
```

The following example removes the MongoDB Shell and then installs the
MongoDB Shell that uses the system's OpenSSL 3:

```sh
sudo apt-get remove -y mongodb-mongosh && sudo apt-get install -y
mongodb-mongosh-shared-openssl3
```

You can also choose the MongoDB packages to install.

The following example installs MongoDB Enterprise and tools, and the
MongoDB Shell that uses the system's OpenSSL 1.1:

```sh
sudo apt-get install -y mongodb-enterprise-database
mongodb-enterprise-tools mongodb-mongosh-shared-openssl11
```

The following example installs MongoDB Enterprise and tools, and the
MongoDB Shell that uses the system's OpenSSL 3:

```sh
sudo apt-get install -y mongodb-enterprise-database
mongodb-enterprise-tools mongodb-mongosh-shared-openssl3
```

For help with troubleshooting errors encountered while installing
MongoDB on Ubuntu, see our
troubleshooting guide.

## Run MongoDB Enterprise Edition

By default, a MongoDB instance stores:

- its data files in `/var/lib/mongodb`

- its log files in `/var/log/mongodb`

If you installed using the package manager, these default directories are
created during installation.

If you installed manually by downloading the tarballs, create
the directories using `mkdir -p <directory>` or ``sudo mkdir -p
<directory>`` depending on the user that will run MongoDB. See your
linux man pages for information on `mkdir` and `sudo`.

By default, MongoDB runs using the `mongodb` user account. If you
change the user that runs the MongoDB process, you **must** also modify
the permission to the `/var/lib/mongodb` and `/var/log/mongodb`
directories to give this user access to these directories.

To specify a different log file directory and data file directory, edit
the `systemLog.path` and `storage.dbPath` settings in
the `/etc/mongod.conf`. Ensure that the user running MongoDB has
access to these directories.

Most Unix-like operating systems limit the system resources that a
process may use. These limits may negatively impact MongoDB operation,
and should be adjusted. See /reference/ulimit for the recommended
settings for your platform. 

**Note:**

If the `ulimit` value for number of open files is under `64000`, MongoDB 
generates a startup warning.

### Procedure

Follow these steps to run MongoDB Enterprise Edition on your system.
These instructions assume that you are using the official `mongodb-enterprise`
package, not the unofficial `mongodb` package provided by
Ubuntu, and are using the default settings.

**Init System**

To run and manage your `mongod` process, use
your operating system's built-in init system. Recent versions of
Linux use **systemd**, which uses the `systemctl` command,
while older versions of Linux use **System V init**, which uses
the `service` command.

If you are unsure which init system your platform uses, run the
following command:

```bash
ps --no-headers -o comm 1
```

Then select the appropriate tab below based on the result:

- `systemd` - select the **systemd (systemctl)** tab below.

- `init` - select the **System V Init (service)** tab below.

|

**systemd-systemctl:**

**Step 1: Start MongoDB.**

You can start the `mongod` process by issuing the
following command:

```sh
sudo systemctl start mongod
```

If you receive an error similar to the following when starting
`mongod`:

`Failed to start mongod.service: Unit mongod.service not found.`

Run the following command first:

```sh
sudo systemctl daemon-reload
```

Then run the start command above again.

**Step 2: Verify that MongoDB has started successfully.**

```sh
sudo systemctl status mongod
```

You can optionally ensure that MongoDB will start following a
system reboot by issuing the following command:

```sh
sudo systemctl enable mongod
```

**Step 3: Stop MongoDB.**

As needed, you can stop the `mongod` process by issuing the
following command:

```sh
sudo systemctl stop mongod
```

**Step 4: Restart MongoDB.**

You can restart the `mongod` process by issuing the following
command:

```sh
sudo systemctl restart mongod
```

You can follow the state of the process for errors or important messages
by watching the output in the `/var/log/mongodb/mongod.log` file.

**Step 5: Begin using MongoDB.**

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

**systemvinit-service:**

**Step 1: Start MongoDB.**

Issue the following command to start `mongod`:

```sh
sudo service mongod start
```

**Step 2: Verify that MongoDB has started successfully**

Verify that the `mongod` process has started
successfully:

```sh
sudo service mongod status
```

You can also check the log file for the current status of the
`mongod` process, located at:
`/var/log/mongodb/mongod.log` by default. A running
`mongod` instance will indicate that it is ready for
connections with the following line:

`[initandlisten] waiting for connections on port 27017`

**Step 3: Stop MongoDB.**

As needed, you can stop the `mongod` process by issuing the
following command:

```sh
sudo service mongod stop
```

**Step 4: Restart MongoDB.**

Issue the following command to restart `mongod`:

```sh
sudo service mongod restart
```

**Step 5: Begin using MongoDB.**

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

## Uninstall MongoDB

To completely remove MongoDB from a system, you must remove the MongoDB
applications themselves, the configuration files, and any directories containing
data and logs. The following section guides you through the necessary steps.

**Warning:**

This process will *completely* remove MongoDB, its configuration, and *all*
databases. This process is not reversible, so ensure that all of your
configuration and data is backed up before proceeding.

**Step 1: Stop MongoDB.**

Stop the `mongod` process by issuing the following command:

```sh
sudo service mongod stop
```

**Step 2: Remove Packages.**

Remove any MongoDB packages that you had previously installed.

```sh
sudo apt-get purge mongodb-enterprise*
```

**Step 3: Remove Data Directories.**

Remove MongoDB databases and log files.

```sh
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
```

## Additional Information

### Upgrading MongoDB Enterprise Edition

When upgrading MongoDB Enterprise Edition, ensure that you are using the official packages.
Specify the same version for each component as in this example:

```sh
VERSION=${VERSION} sudo apt-get install -y \
  mongodb-enterprise=${VERSION} \
  mongodb-enterprise-server=${VERSION} \
  mongodb-enterprise-mongos=${VERSION} \
  mongodb-enterprise-tools=${VERSION} \
  --allow-downgrades --allow-change-held-packages
```

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

### MongoDB Enterprise Edition Packages

MongoDB Enterprise Edition is available from its own dedicated
repository, and contains the following officially-supported packages:

* - Package Name
  - Description

* - `mongodb-enterprise`
  - A `metapackage` that automatically installs the component
    packages listed below.

* - `mongodb-enterprise-database`
  - A `metapackage` that automatically installs the component
    packages listed below.

    | Package Name | Description |
    |---|---|
    | `mongodb-enterprise-server` | Contains the `mongod` daemon and associated configuration and init scripts. |
    | `mongodb-enterprise-mongos` | Contains the `mongos` daemon. |
    | `mongodb-enterprise-cryptd` | Contains the mongocryptd binary |

* - `mongodb-mongosh`
  - Contains the MongoDB Shell (`mongosh`).

* - `mongodb-shared-openssl*`
  - Contains the MongoDB Shell that uses the OpenSSL version already
    installed on your computer (`mongosh`).

* - `mongodb-enterprise-tools`
  - A `metapackage` that automatically installs the component
    packages listed below:

    * - Package Name
      - Description

    * - `mongodb-database-tools`
      - Contains the following MongoDB database tools:

        - `mongodump`
        - `mongorestore`
        - `bsondump`
        - `mongoimport`
        - `mongoexport`
        - `mongostat`
        - `mongotop`
        - `mongofiles`

    * - `mongodb-enterprise-database-tools-extra`
      - Contains the following MongoDB support tools:

        - `mongoldap`
        - `mongokerberos`
        - install-compass script
        - `mongodecrypt` binary
