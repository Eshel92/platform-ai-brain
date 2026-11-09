<!-- Converted from tutorial/install-mongodb-enterprise-on-red-hat.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise Edition on Red Hat or CentOS

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Enterprise Edition on
Red Hat Enterprise Linux, CentOS Linux, or Oracle Linux [#oracle-linux]_
using the YUM package manager.

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
64-bit versions of Red Hat Enterprise Linux (RHEL), CentOS Linux,
Oracle Linux [#oracle-linux]_, Rocky Linux, and AlmaLinux [#rocky-almalinux]_ 
on x86_64 architecture:

- RHEL (Red Hat Enterprise Linux) / CentOS Stream / Oracle / Rocky / AlmaLinux 10

- RHEL (Red Hat Enterprise Linux) / CentOS Stream / Oracle / Rocky / AlmaLinux 9 

- RHEL (Red Hat Enterprise Linux) / CentOS Stream / Oracle / Rocky / AlmaLinux 8

- RHEL (Red Hat Enterprise Linux) / CentOS / Oracle 7

MongoDB only supports the 64-bit versions of these platforms.

MongoDB 7.0 Enterprise Edition on
RHEL (Red Hat Enterprise Linux) / CentOS / Oracle / Rocky / Alma 
Linux also supports the 
ARM64 architecture on
select platforms.

See prod-notes-supported-platforms for more information.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

## Install MongoDB Enterprise Edition

Follow these steps to install MongoDB Enterprise Edition using the
YUM package manager.

**Step 1: Configure the repository.**

Create an
`/etc/yum.repos.d/mongodb-enterprise-7.0.repo` file so
that you can install MongoDB Enterprise directly using `yum`:

**rhel10:**

```cfg
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/redhat/10/mongodb-enterprise/7.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+version+}.asc
```

**rhel9:**

```cfg
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/redhat/9/mongodb-enterprise/7.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+version+}.asc
```

**rhel8:**

```cfg
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/redhat/8/mongodb-enterprise/7.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+version+}.asc
```

**rhel7:**

```cfg
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/redhat/7/mongodb-enterprise/7.0/$basearch/
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
[MongoDB repository](https://repo.mongodb.com/yum/redhat/).
Downloads are organized by Red Hat / CentOS
version (e.g. `9`), then MongoDB
release version
(e.g. `7.0`), then architecture (e.g. `x86_64`).

**Step 2: Install MongoDB Enterprise Server.**

**latest:**

To install the latest stable version of MongoDB Enterprise
7.0, issue the following command:

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

### ulimit

Most Unix-like operating systems limit the system resources that a
process may use. These limits may negatively impact MongoDB operation,
and should be adjusted. See /reference/ulimit for the recommended
settings for your platform. 

**Note:**

If the `ulimit` value for number of open files is under `64000`, MongoDB 
generates a startup warning.

### Directory Paths

#### To Use Default Directories

By default, MongoDB runs using the `mongod` user account and
uses the following default directories:

- `/var/lib/mongo` (the data directory)

- `/var/log/mongodb` (the log directory)

The package manager creates the default directories during
installation. The owner and group name are `mongod`.

#### To Use Non-Default Directories

To use a data directory and/or log directory other than the default
directories:

#. Create the new directory or directories.

#. Edit the configuration file `/etc/mongod.conf` and modify the
   following fields accordingly:

   - `storage.dbPath` to specify a new data directory path, such as `/some/data/directory`

   - `systemLog.path` to specify a new log file path, such as `/some/log/directory/mongod.log`

#. Ensure that the user running MongoDB has access to the directory or
   directories:

   ```bash
   sudo chown -R mongod:mongod <directory>
   ```

   If you change the user that runs the MongoDB process, you **must**
   give the new user access to these directories.

#. Configure SELinux if enforced. See
   install-enterprise-rhel-configure-selinux.

### Configure SELinux

Starting in MongoDB 5.0, a new SELinux policy is available for 
MongoDB installations that:

- Use an `.rpm` installer.
- Use default configuration settings.
- Run on RHEL7 or later.

For MongoDB Enterprise installations that use LDAP (Lightweight Directory 
Access Protocol) authentication, the following additional SELinux policies must 
be in place: 

- For deployments that use LDAP authentication via OS libraries, MongoDB must have access to the 
  `tcontext=system_u:object_r:ldap_port_t:s0` LDAP ports. You can enable 
  access by running `setsebool -P authlogin_nsswitch_use_ldap 1`.

- For deployments that use LDAP authentication via saslauthd, you must enable cluster mode by running 
  `sudo setsebool -P daemons_enable_cluster_mode 1`.

If your installation does not meet these requirements, refer to the
SELinux Instructions for `.tgz`
packages.

**Note:**

If your MongoDB deployment uses custom settings for any of the
following:

- MongoDB connection ports
- `dbPath`
- `systemLog.path`
- `pidFilePath`

You cannot use the MongoDB supplied SELinux policy. An alternative
is to create a custom SELinux policy, however an 
improperly written custom policy may be less secure or may stop your
`mongod` instance from working.

##### Install the SELinux Policy

#. Ensure you have the following packages installed:

   - `git`
   - `make`
   - `checkpolicy`
   - `policycoreutils`
   - `selinux-policy-devel`

   ```bash
   sudo yum install git make checkpolicy policycoreutils selinux-policy-devel
   ```

#. Download the policy repository.

   ```bash
   git clone https://github.com/mongodb/mongodb-selinux
   ```

#. Build the policy.

   ```bash
   cd mongodb-selinux
   make
   ```

#. Apply the policy.

   ```bash
   sudo make install
   ```

**Important:** Backward-Incompatible Feature

Starting in MongoDB 5.1, you must run the following command from the
directory into which the SELinux policy was previously cloned before you
can downgrade to an earlier MongoDB version:

```bash
sudo make uninstall
```

##### SELinux Policy Considerations

- The SELinux policy is designed to work with the configuration that
  results from a standard MongoDB `.rpm` package installation. See 
  [standard installation assumptions](https://github.com/mongodb/mongodb-selinux/blob/master/README.md#standard-installation)
  for more details.

- The SELinux policy is designed for `mongod` servers. It
  does not apply to other MongoDB daemons or tools such as: 

  - `mongos`
  - `mongosh`
  - mongocryptd

- The [reference policy](https://github.com/SELinuxProject/refpolicy/blob/master/policy/modules/services/mongodb.if) 
  supplied by the SELinux Project includes a `mongodb_admin` macro.
  This macro is not included in the MongoDB SELinux policy. An
  administrator in the `unconfined_t` domain can manage
  `mongod`.

- To uninstall the policy, go to the directory where you downloaded the
  policy repository and run: 

  ```bash
  sudo make uninstall
  ```

### Procedure

Follow these steps to run MongoDB Enterprise Edition on your system.
These instructions assume that you are using the default settings.

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
sudo yum erase $(rpm -qa | grep mongodb-enterprise)
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
