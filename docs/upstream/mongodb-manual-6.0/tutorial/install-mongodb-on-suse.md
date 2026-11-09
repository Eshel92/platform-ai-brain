<!-- Converted from tutorial/install-mongodb-on-suse.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community Edition on SUSE

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free tier to get started.

## Overview

Use this tutorial to install MongoDB 6.0 Community
Edition on SUSE Linux Enterprise Server (SLES) using the
`zypper` package manager.

### MongoDB Version

This tutorial installs MongoDB 6.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

## Considerations

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

Follow these steps to install MongoDB Community Edition using the
`zypper` package manager.

**Step 1: Import the public key.**

```sh
sudo rpm --import https://pgp.mongodb.com/server-6.0.asc
```

**Step 2: Add the repository.**

Configure the MongoDB Community repository for SUSE.

**suse15:**

To add the repository file for SUSE Enterprise Linux 15, run the
following command:

```sh
sudo zypper addrepo --gpgcheck "https://repo.mongodb.org/zypper/suse/15/mongodb-org/6.0/x86_64/" mongodb
```

**suse12:**

To add the repository file for SUSE Enterprise Linux 12, run the
following command:

```sh
sudo zypper addrepo --gpgcheck "https://repo.mongodb.org/zypper/suse/12/mongodb-org/6.0/x86_64/" mongodb
```

**Step 3: Install MongoDB packages.**

You can install either the latest stable release of MongoDB or a
specific release of MongoDB.

**latest:**

To install the latest version of MongoDB, run the
following command:

```sh
sudo zypper -n install mongodb-org
```

**specific:**

To install a specific release of MongoDB, specify each
component package individually and append the version
number to the package name, as in the following example:

```sh
sudo zypper install \
   mongodb-org-6.0.21 \
   mongodb-org-database-6.0.21 \
   mongodb-org-server-6.0.21 \
   mongodb-mongosh \
   mongodb-org-mongos-6.0.21 \
   mongodb-org-tools-6.0.21 \
   mongodb-org-database-tools-extra-6.0.21
```

You can specify any available version of MongoDB. However,
zypper upgrades the packages when a newer version becomes
available. To prevent unintended upgrades, pin the
packages by running the following command:

```sh
sudo zypper addlock \
   mongodb-org-6.0.21 \
   mongodb-org-database-6.0.21 \
   mongodb-org-server-6.0.21 \
   mongodb-mongosh \
   mongodb-org-mongos-6.0.21 \
   mongodb-org-tools-6.0.21 \
   mongodb-org-database-tools-extra-6.0.21
```

Previous versions of MongoDB packages use a different
repository location. Refer to the version of the
documentation appropriate for your MongoDB version.

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

**Init System**

To run and manage your `mongod` process, you will be using
your operating system's built-in init system. Recent versions of
Linux tend to use **systemd** (which uses the `systemctl` command),
while older versions of Linux tend to use **System V init** (which uses
the `service` command).

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
sudo zypper remove $(rpm -qa | grep mongodb-org)
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

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

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
