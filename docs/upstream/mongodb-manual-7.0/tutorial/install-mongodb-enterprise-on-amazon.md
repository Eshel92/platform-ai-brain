<!-- Converted from tutorial/install-mongodb-enterprise-on-amazon.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise Edition on Amazon Linux

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Enterprise Edition
on Amazon Linux using the YUM package manager.

MongoDB Enterprise Edition
is available on select platforms and contains support for features
related to security and monitoring.

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

This tutorial installs MongoDB 7.0 Enterprise
Edition. To install a different version of MongoDB Enterprise,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

## Considerations

### Platform Support

MongoDB 7.0 Enterprise Edition supports the following
64-bit Amazon Linux release on 
x86_64 architecture:

- Amazon Linux 2023

- Amazon Linux 2

MongoDB only supports the 64-bit versions of this platform.

MongoDB 7.0 Enterprise Edition on Amazon Linux also supports the
ARM64 architecture on
select platforms.

See prod-notes-supported-platforms for more information.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

## Install MongoDB Enterprise Edition

Follow these steps to install MongoDB Enterprise Edition using the
YUM package manager. Select the tab for your version of
Amazon Linux:

**Step 1: Configure the repository.**

Create a `/etc/yum.repos.d/mongodb-enterprise-7.0.repo`
file so that you can install MongoDB directly using `yum`:

**amazon2023:**

```cfg
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/amazon/2023/mongodb-enterprise/7.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+version+}.asc
```

**amazon2:**

```cfg
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/amazon/2/mongodb-enterprise/7.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+version+}.asc
```

**Note:**

If you have a `mongodb-enterprise.repo` file
in this directory from a previous installation of MongoDB, you
should remove it. Use the `mongodb-enterprise-7.0.repo`
file above to install MongoDB 7.0.

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.com/yum/amazon/).
Downloads are organized by Amazon Linux version (for example,
`2023`), then MongoDB release version (`7.0`), then
architecture (`x86_64`).

**Step 2: Install MongoDB Enterprise Server.**

**latest:**

To install the latest stable version of MongoDB Enterprise
7.0, run the following command:

```sh
sudo yum install -y mongodb-enterprise
```

**specific:**

To install a specific release, you must specify each
component package individually along with the version
number.

```
sudo yum install -y \
   mongodb-enterprise-7.0.24 \
   mongodb-enterprise-database-7.0.24 \
   mongodb-enterprise-server-7.0.24 \
   mongodb-mongosh \
   mongodb-enterprise-mongos-7.0.24 \
   mongodb-enterprise-tools-7.0.24 \
   mongodb-enterprise-cryptd-7.0.24 \
   mongodb-enterprise-database-tools-extra-7.0.24
```

**Note:**

Although you can specify any available version of MongoDB
Enterprise, `yum` upgrades the packages when a newer
version becomes available. To prevent unintended upgrades,
pin the package by adding the following `exclude` directive
to your `/etc/yum.conf` file:

```ini
exclude=mongodb-enterprise,mongodb-enterprise-database,mongodb-enterprise-server,mongodb-enterprise-shell,mongodb-enterprise-mongos,mongodb-enterprise-tools
```

**Note:**

You can also install the MongoDB Shell that uses the system's OpenSSL.
You must have already installed OpenSSL on your system before
installing this version of the MongoDB Shell.

You can install all of the MongoDB Enterprise packages and the
MongoDB Shell that uses the system's OpenSSL without removing the
MongoDB Shell first. For example:

```sh
sudo yum install -y mongodb-enterprise mongodb-mongosh-shared-openssl11
```

The following example removes the MongoDB Shell and then installs the
MongoDB Shell that uses the system's OpenSSL 1.1:

```sh
sudo yum remove -y mongodb-mongosh && sudo yum install -y
mongodb-mongosh-shared-openssl11
```

The following example removes the MongoDB Shell and then installs the
MongoDB Shell that uses the system's OpenSSL 3:

```sh
sudo yum remove -y mongodb-mongosh && sudo yum install -y
mongodb-mongosh-shared-openssl3
```

If the MongoDB Shell fails to start with the following error, install
the `mongodb-mongosh-shared-openssl3` package by using the preceding
commands:

```none
mongosh: OpenSSL configuration error: ...:error:030000A9:digital
envelope routines:alg_module_init:unknown
option:../deps/openssl/openssl/crypto/evp/evp_cnf.c:61:name=rh-allow-sha1-signatures,
value=yes
```

The error affects RHEL 9+ and derivatives such as Amazon Linux 2023.

You can also choose the MongoDB packages to install.

The following example installs MongoDB Enterprise and tools, and the
MongoDB Shell that uses the system's OpenSSL 1.1:

```sh
sudo yum install -y mongodb-enterprise-database
mongodb-enterprise-tools mongodb-mongosh-shared-openssl11
```

The following example installs MongoDB Enterprise and tools, and the
MongoDB Shell that uses the system's OpenSSL 3:

```sh
sudo yum install -y mongodb-enterprise-database
mongodb-enterprise-tools mongodb-mongosh-shared-openssl3
```

   

## Run MongoDB Enterprise Edition

### ulimit Considerations

Most Unix-like operating systems limit the system resources that a
process may use. These limits may negatively impact MongoDB operation,
and should be adjusted. See /reference/ulimit for the recommended
settings for your platform. 

**Note:**

If the `ulimit` value for number of open files is under `64000`, MongoDB 
generates a startup warning.

### Directories

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
sudo yum erase $(sudo rpm -qa | grep mongodb-enterprise)
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
