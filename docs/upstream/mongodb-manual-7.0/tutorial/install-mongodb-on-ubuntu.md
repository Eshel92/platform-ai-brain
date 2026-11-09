<!-- Converted from tutorial/install-mongodb-on-ubuntu.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community Edition on Ubuntu

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Community Edition on
LTS (long-term support) releases of Ubuntu Linux using the
APT package manager.

### MongoDB Version

This tutorial installs MongoDB 7.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

## Considerations

### Platform Support

MongoDB 7.0 Community Edition supports the following
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

MongoDB 7.0 Community Edition on Ubuntu also supports the
ARM64 architecture on
select platforms.

See prod-notes-supported-platforms for more information.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

### Official MongoDB Packages

To install MongoDB Community on your Ubuntu system, these
instructions will use the official `mongodb-org` package, which is
maintained and supported by MongoDB Inc. The official `mongodb-org`
package always contains the latest version of MongoDB and is available
from its own dedicated repo.

**Important:**

The `mongodb` package provided by Ubuntu is **not**
maintained by MongoDB Inc. and conflicts with the official
`mongodb-org` package. If you already installed the `mongodb`
package on your Ubuntu system, you **must** first uninstall
the `mongodb` package before proceeding with these instructions.

See ubuntu-package-content for the complete list of official
packages.

## Install MongoDB Community Edition

Follow these steps to install MongoDB Community Edition using the
APT package manager.

**Step 1: Import the public key.**

From a terminal, install `gnupg` and `curl` if they are not already
available:

```bash
sudo apt-get install gnupg curl
```

To import the MongoDB public GPG key, run the following command:

```bash
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
```

**Step 2: Create the list file.**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-7.0.list` for
your version of Ubuntu.

**jammy:**

Create the list file for Ubuntu 22.04 (Jammy):

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```

**focal:**

Create the list file for Ubuntu 20.04 (Focal):

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```

**Step 3: Reload the package database.**

Issue the following command to reload the local package database:

```bash
sudo apt-get update
```

**Step 4: Install MongoDB Community Server.**

You can install either the latest stable version of MongoDB or a
specific version of MongoDB.

**latest:**

To install the latest stable version, issue the following

```bash
sudo apt-get install -y mongodb-org
```

**specific:**

To install a specific release, you must specify each component package
individually along with the version number.

```sh
sudo apt-get install -y \
   mongodb-org=7.0.24 \
   mongodb-org-database=7.0.24 \
   mongodb-org-server=7.0.24 \
   mongodb-mongosh \
   mongodb-org-shell=7.0.24 \
   mongodb-org-mongos=7.0.24 \
   mongodb-org-tools=7.0.24 \
   mongodb-org-database-tools-extra=7.0.24
```

If you only install `mongodb-org=7.0.24`
and do not include the component packages, the latest
version of each MongoDB package will be installed
regardless of what version you specified.

Optional. Although you can specify any available version of MongoDB,
`apt-get` will upgrade the packages when a newer version becomes
available. To prevent unintended upgrades, you can pin the package
at the currently installed version:

```bash
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-database hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-mongosh hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
echo "mongodb-org-database-tools-extra hold" | sudo dpkg --set-selections
```

For help with troubleshooting errors encountered while installing
MongoDB on Ubuntu, see our
troubleshooting guide.

## Run MongoDB Community Edition

### ulimit Considerations

Most Unix-like operating systems limit the system resources that a
process may use. These limits may negatively impact MongoDB operation,
and should be adjusted. See /reference/ulimit for the recommended
settings for your platform. 

**Note:**

If the `ulimit` value for number of open files is under `64000`, MongoDB 
generates a startup warning.

### Directories

If you installed through the package manager, the data directory
`/var/lib/mongodb` and the log directory `/var/log/mongodb` are
created during the installation.

By default, MongoDB runs using the `mongodb` user account. If
you change the user that runs the MongoDB process, you **must** also
modify the permission to the data and log directories to give this
user access to these directories.

### Configuration File

The official MongoDB package includes a configuration file (`/etc/mongod.conf`). These settings (such as the
data directory and log directory specifications) take effect
upon startup. That is, if you change the configuration file while
the MongoDB instance is running, you must restart the instance for the
changes to take effect.

### Procedure

Follow these steps to run MongoDB Community Edition on your system.
These instructions assume that you are using the official `mongodb-org`
package -- not the unofficial `mongodb` package provided by
Ubuntu --  and are using the default settings.

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

## Uninstall MongoDB Community Edition

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
sudo apt-get purge "mongodb-org*"
```

**Step 3: Remove Data Directories.**

Remove MongoDB databases and log files.

```sh
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
```

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

### MongoDB Community Edition Packages

MongoDB Community Edition is available from its own dedicated
repository, and contains the following officially-supported packages:

* - Package Name
  - Description

* - `mongodb-org`
  - A `metapackage` that automatically installs the component
    packages listed below.

* - `mongodb-org-database`
  - A `metapackage` that automatically installs the component
    packages listed below.

    | Package Name | Description |
    |---|---|
    | `mongodb-org-server` | Contains the `mongod` daemon, associated init script, and a configuration file (`/etc/mongod.conf`). You can use the initialization script to start `mongod` with the configuration file. For details, see the "Run MongoDB Community Edition" section, above. |
    | `mongodb-org-mongos` | Contains the `mongos` daemon. |

* - `mongodb-mongosh`
  - Contains the MongoDB Shell (`mongosh`).

* - `mongodb-org-tools`
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

    * - `mongodb-org-database-tools-extra`
      - Contains the install-compass script
