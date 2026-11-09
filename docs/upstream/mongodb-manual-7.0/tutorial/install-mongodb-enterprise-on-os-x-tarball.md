<!-- Converted from tutorial/install-mongodb-enterprise-on-os-x-tarball.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise on macOS (.tgz)

## Overview

Use this tutorial to manually install MongoDB 7.0 Enterprise
Edition on macOS using a downloaded `.tgz` tarball.

MongoDB Enterprise Edition
is available on select platforms and contains support for features
related to security and monitoring.

### MongoDB Version

This tutorial installs MongoDB 7.0 Enterprise
Edition. To install a different version of MongoDB Enterprise,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

## Considerations

### MongoDB Shell, `mongosh`

When you use the `.tgz` package to install the server, you need to
follow the `mongosh installation instructions` to
download and install `mongosh` separately.

### Platform Support

MongoDB 7.0 Enterprise Edition supports macOS 15 or later, and
requires a Haswell or newer CPU architecture.

For more information, see prod-notes-supported-platforms.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

## Install MongoDB Enterprise Edition

To manually install MongoDB Enterprise Edition from the `.tgz`,
complete the following steps:

**intel:**

**Step 1: Download the tarball.**

After you have installed the required prerequisite packages,
download the MongoDB Enterprise `tgz` tarball from the
following link:

→ [MongoDB Download Center](https://www.mongodb.com/try/download/enterprise/)

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
[MongoDB Download Center](https://www.mongodb.com/try/download/enterprise/) and uncompress the package.

**apple:**

**Step 1: Download the tarball.**

Download the MongoDB Enterprise `tgz` tarball from the following link: 

→ [MongoDB Download Center](https://www.mongodb.com/try/download/enterprise/) 

a. In the Version dropdown, select the version of MongoDB 
   to download. 

#. In the Platform dropdown, select macOS ARM 64. 

#. In the Package dropdown, select tgz. 

#. Click Download.

**Step 2: Extract the files from the downloaded archive.**

```sh
tar -zxvf mongodb-macos-arm64-enterprise-7.0.tgz
```

If your web browser automatically unzips the file as part of the download, the 
file ends in `.tar` instead.

**Step 3: Ensure the binaries are in a directory listed in your `PATH` environment variable.**

The MongoDB binaries are in the `bin/` directory of the tarball. You can 
either:

- Copy the binaries into a directory listed in your `PATH` variable, such as 
  `/usr/local/bin`. Replace `/path/to/the/mongodb-directory/` with your 
  installation directory.

  ```bash
  sudo cp /path/to/the/mongodb-directory/bin/* /usr/local/bin/ 
  ```

- Create symbolic links to the binaries from a directory listed in your `PATH` 
  variable, such as `/usr/local/bin`. Replace 
  `/path/to/the/mongodb-directory/` with your installation directory. 

  ```bash
  sudo ln -s  /path/to/the/mongodb-directory/bin/* /usr/local/bin/
  ```

## Run MongoDB Enterprise Edition

ulimit Considerations
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

**Step 1: Create the data directory.**

Before you start MongoDB for the first time, you must create the
directory to which the `mongod` process will write data.

For example, to create the `~/data/db` directory:

```sh
sudo mkdir -p ~/data/db
```

**Step 2: Create the log directory.**

You must also create the directory in which the `mongod` process
will write its log file:

For example, to create the `~/data/log/mongodb` directory:

```sh
sudo mkdir -p ~/data/log/mongodb
```

**Step 3: Set permissions for the data and log directories.**

Ensure that the user account running `mongod` has read
and write permissions for these two directories. If you are running
`mongod` as your own user account, and you just created
the two directories above, they should already accessible to your
user. Otherwise, you can use `chown` to set ownership,
substituting the appropriate *user*:

```sh
sudo chown <user> ~/data/db
sudo chown <user> ~/data/log/mongodb
```

**Step 4: Run MongoDB.**

To run MongoDB, run the `mongod` process at the system
prompt, providing the two parameters `dbpath` and `logpath`
from above, and the `fork` parameter to run `mongod`
in the background. Alternatively, you may choose to store the values
for `dbpath`, `logpath`, `fork`, and many other parameters in a
configuration file.

Run the `mongod` process at the system prompt,
providing the three necessary parameters directly on the
command-line:

```sh
mongod --dbpath ~/data/db --logpath ~/data/log/mongodb/mongo.log --fork
```

Run the `mongod` process at the system prompt,
providing the path to a
configuration file
with the `config` parameter:

```sh
mongod --config /usr/local/etc/mongod.conf
```

macOS may prevent `mongod` from running after installation. If
you receive a security error when starting `mongod`
indicating that the developer could not be identified or verified,
do the following to grant `mongod` access to run:

- Open *System Preferences*
- Select the *Security and Privacy* pane.
- Under the *General* tab, click the button to the right of the
  message about `mongod`, labelled either Open
  Anyway or Allow Anyway depending on your version of
  macOS.

**Step 5: Verify that MongoDB has started successfully.**

Verify that MongoDB has started successfully:

```none
ps aux | grep -v grep | grep mongod
```

If you do not see a `mongod` process running, check the logfile for
any error messages.

**Step 6: Begin using MongoDB.**

Start a `mongosh` session on the same host machine as the 
`mongod`. You can run `mongosh`
without any command-line options to connect to a
`mongod` that is running on your *localhost* with the
default port of *27017*:

```shell
mongosh
```

For more information on connecting using `mongosh`,
such as to connect to a `mongod` instance running
on a different host and/or port, see the
`mongosh documentation`.

To help you start using MongoDB, MongoDB provides Getting
Started Guides in various driver editions. See
getting-started for the available editions.

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
