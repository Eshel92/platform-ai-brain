<!-- Converted from tutorial/install-mongodb-on-amazon.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community Edition on Amazon Linux

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free tier to get started.

## Overview

Use this tutorial to install MongoDB 6.0 Community Edition on
Amazon Linux using the `yum` package manager.

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

## Considerations

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

Follow these steps to install MongoDB Community Edition using the
`yum` package manager. Select the tab for your version of
Amazon Linux:

**Step 1: Configure the repository.**

Create a `/etc/yum.repos.d/mongodb-org-6.0.repo`
file so that you can install MongoDB directly using `yum`:

```cfg
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+version+}.asc
```

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.org/yum/amazon/).
Downloads are organized by Amazon Linux 2023 version (for
example, `2023`), then MongoDB version (`6.0`), then
architecture (`x86_64`).

Prior to MongoDB 5.0, odd-numbered MongoDB release versions, such as
`4.3`, were development releases. Beginning with MongoDB 5.1,
MongoDB has quarterly rapid releases. For more information on the
differences between rapid and long-term support releases, see
release-version-numbers.

**Step 2: Install MongoDB Community Server.**

**latest:**

To install the latest stable version of MongoDB, run the
following command:

```sh
sudo yum install -y mongodb-org
```

**specific:**

To install a specific release of MongoDB, specify
each component package individually and append the version
number to the package name, as in the following example:

(Include not available offline: /includes/release/pin-repo-to-version-yum.rst)

**Note:**

`yum` automatically upgrades packages when newer versions
become available. To prevent updates, configure `yum`
to exclude the relevant packages in the
`/etc/yum.conf` file:

```ini
exclude=mongodb-org,mongodb-org-database,mongodb-org-server,mongodb-mongosh,mongodb-org-mongos,mongodb-org-tools
```

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
sudo yum erase $(sudo rpm -qa | grep mongodb-org)
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
