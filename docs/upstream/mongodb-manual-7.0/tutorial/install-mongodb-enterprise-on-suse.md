<!-- Converted from tutorial/install-mongodb-enterprise-on-suse.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise Edition on SUSE

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Enterprise Edition
on SUSE Linux Enterprise Server (SLES) using the ZYpp package
manager.

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

**Note:** EOL Notice

- MongoDB 5.0 Enterprise Edition removes support for
  SLES12 on s390x

MongoDB 7.0 Enterprise Edition supports the following
64-bit SUSE Linux Enterprise Server (SLES) releases on 
x86_64 architecture:

- SLES (SUSE Linux Enterprise Server) 15

- SLES (SUSE Linux Enterprise Server) 12

MongoDB only supports the 64-bit versions of these platforms.

See prod-notes-supported-platforms for more information.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

## Install MongoDB Enterprise Edition

Follow these steps to install MongoDB Enterprise Edition using the
ZYpp package manager.

**Step 1: Import the public key.**

```sh
sudo rpm --import https://pgp.mongodb.com/server-7.0.asc
```

**Step 2: Add the repository.**

Configure the MongoDB Enterprise repository for SUSE.

**suse15:**

To add the repository file for SUSE Enterprise Linux 15, run the
following command:

```sh
sudo zypper addrepo --gpgcheck "https://repo.mongodb.com/zypper/suse/15/mongodb-enterprise/7.0/x86_64/" mongodb
```

**suse12:**

To add the repository file for SUSE Enterprise Linux 12, run the
following command:

```sh
sudo zypper addrepo --gpgcheck "https://repo.mongodb.com/zypper/suse/12/mongodb-enterprise/7.0/x86_64/" mongodb
```

**Step 3: Install MongoDB packages.**

You can install either the latest stable release of MongoDB or a
specific release of MongoDB.

**latest:**

To install the latest version of MongoDB, run the
following command:

```sh
sudo zypper -n install mongodb-enterprise
```

**specific:**

To install a specific release of MongoDB, specify each
component package individually and append the version
number to the package name.

```sh
sudo zypper install \
   mongodb-enterprise-7.0.24 \
   mongodb-enterprise-database-7.0.24 \
   mongodb-enterprise-server-7.0.24 \
   mongodb-mongosh \
   mongodb-enterprise-cryptd-7.0.24 \
   mongodb-enterprise-mongos-7.0.24 \
   mongodb-enterprise-tools-7.0.24 \
   mongodb-enterprise-tools-extra-7.0.24
```

You can specify any available version of MongoDB. However,
zypper upgrades the packages when a newer version becomes
available. To prevent unintended upgrades, pin the
packages by running the following command:

```sh
sudo zypper addlock \\
   mongodb-enterprise-7.0.24 \
   mongodb-enterprise-database-7.0.24 \
   mongodb-enterprise-server-7.0.24 \
   mongodb-mongosh \
   mongodb-enterprise-cryptd-7.0.24 \
   mongodb-enterprise-mongos-7.0.24 \
   mongodb-enterprise-tools-7.0.24 \
   mongodb-enterprise-tools-extra-7.0.24
```

Previous versions of MongoDB packages use a different
repository location. Refer to the version of the
documentation appropriate for your MongoDB version.

## Run MongoDB Enterprise Edition

By default, a MongoDB instance stores:

- its data files in `/var/lib/mongo`

- its log files in `/var/log/mongodb`

If you installed using the package manager, these default directories are
created during installation.

If you installed manually by downloading the tarballs, create
the directories using `mkdir -p <directory>` or ``sudo mkdir -p
<directory>`` depending on the user that will run MongoDB. See your
linux man pages for information on `mkdir` and `sudo`.

By default, MongoDB runs using the `mongod` user account. If you
change the user that runs the MongoDB process, you **must** also modify
the permission to the `/var/lib/mongo` and `/var/log/mongodb`
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

Follow these steps to run MongoDB Enterprise Edition. These instructions
assume that you are using the default settings.

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

You can verify that the `mongod` process has started
successfully by issuing the following command:

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

You can start the `mongod` process by issuing the following
command:

```sh
sudo service mongod start
```

**Step 2: Verify that MongoDB has started successfully**

You can verify that the `mongod` process has started
successfully by checking the contents of the log file at
`/var/log/mongodb/mongod.log`
for a line reading

```none
[initandlisten] waiting for connections on port <port>
```

where `<port>` is the port configured in `/etc/mongod.conf`, `27017` by default.

You can optionally ensure that MongoDB will start following a system
reboot by issuing the following command:

```sh
sudo chkconfig mongod on
```

**Step 3: Stop MongoDB.**

As needed, you can stop the `mongod` process by issuing the
following command:

```sh
sudo service mongod stop
```

**Step 4: Restart MongoDB.**

You can restart the `mongod` process by issuing the following
command:

```sh
sudo service mongod restart
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
sudo zypper remove $(rpm -qa | grep mongodb-enterprise)
```

**Step 3: Remove Data Directories.**

Remove MongoDB databases and log files.

```sh
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongo
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
