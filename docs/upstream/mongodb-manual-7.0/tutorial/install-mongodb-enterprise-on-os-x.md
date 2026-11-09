<!-- Converted from tutorial/install-mongodb-enterprise-on-os-x.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise on macOS

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Enterprise Edition on
macOS using the third-party [Homebrew](https://brew.sh)
package manager.

Installing MongoDB through Homebrew also installs the `MongoDB
Database Tools`. See brew-installs-dbtools for more
information.

## Considerations

### Platform Support

MongoDB 7.0 Enterprise Edition supports macOS 15 or later, and
requires a Haswell or newer CPU architecture.

For more information, see prod-notes-supported-platforms.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

## Before You Begin

Ensure your system meets each of the following prerequisites. You only
need to perform each prerequisite step once on your system. If you
have already performed the prerequisite steps as part of an earlier
MongoDB installation using Homebrew, you can skip to the
installation procedure.

### Install Xcode Command-line Tools

Homebrew requires the Xcode command-line tools from Apple's Xcode.

To install the Xcode command-line tools, run the following command:

```zsh
xcode-select --install
```

### Install Homebrew

macOS does not include the Homebrew `brew` package by default.

To install Homebrew, use the official [Homebrew](https://brew.sh/#install) installation instructions.

## Install MongoDB Enterprise Edition

To install MongoDB Enterprise Edition using Homebrew, complete the
following steps:

**Step 1: Add the MongoDB Homebrew tap.**

The [MongoDB Homebrew](https://github.com/mongodb/homebrew-brew)
tap makes the official MongoDB and Database Tools Homebrew
formulae available on your system.

To add the MongoDB Homebrew tap, run the following command:

```bash
brew tap mongodb/brew
```

Then, mark the tap as trusted:

```bash
brew trust mongodb/brew
```

If you have already done this for a previous installation of
MongoDB, you can skip this step.

**Step 2: Update Homebrew.**

To update Homebrew and all existing formulae, run the following
command:

```bash
brew update
```

**Step 3: Install MongoDB Enterprise.**

To install MongoDB Enterprise, run the following command:

```bash
brew install mongodb-enterprise@7.0
```

**Tip:**

Alternatively, you can specify a previous version of MongoDB if
desired. You can also maintain multiple versions of MongoDB side by
side in this manner.

**Tip:**

If you have previously installed an older version of the formula, you
may encounter a `ChecksumMismatchError`. To resolve, see
troubleshooting-checksumerror.

## Run MongoDB Enterprise Edition

Follow these steps to run MongoDB Enterprise Edition. These instructions
assume that you are using the default settings.

You can run MongoDB as a macOS service using `brew`, or you can run
MongoDB manually as a background process.

**Note:**

For macOS systems that have installed MongoDB using the Homebrew
installation method, the open files limit might not be automatically set
when starting MongoDB through `brew services`. You might need to
manually configure the `ulimit` values.

See Ulimit Settings for more information.

- To run MongoDB (that is, the `mongod` process) **as a
  macOS service**, run:

  ```bash
  brew services start mongodb-enterprise@7.0
  ```

  To stop a `mongod` running as a macOS service, use the
  following command as needed:

  ```bash
  brew services stop mongodb-enterprise@7.0
  ```

- To run `mongod` **manually as a background process**
  using a config file:

  - If your deployment does not use TLS connections, use the `--fork` option:

    - For macOS running on Intel processors, run:

      ```bash
      mongod --config /usr/local/etc/mongod.conf --fork
      ```

    - For macOS running on [Apple Silicon processors](https://support.apple.com/en-us/HT211814), run:

      ```bash
      mongod --config /opt/homebrew/etc/mongod.conf --fork
      ```

  - If your deployment uses TLS connections, use [GNU Screen](https://www.gnu.org/software/screen/).

    - For macOS running on Intel processors:

      **Step 1: Start your screen.**

      ```bash
      screen -S <name-of-screen>
      ```

      **Step 2: Start `mongod`.**

      ```bash
      mongod --config /usr/local/etc/mongod.conf 
      ```

      **Step 3: Detach from screen.**

      Detach from your screen by typing `Ctrl+a`, then
      clicking `d`.

      **Step 4: View all active screens.**

      ```bash
      screen -ls
      ```

    - For macOS running on [Apple Silicon processors](https://support.apple.com/en-us/HT211814):

      **Step 1: Start your screen.**

      ```bash
      screen -S <name-of-screen>
      ```

      **Step 2: Start `mongod`.**

      ```bash
      mongod --config /opt/homebrew/etc/mongod.conf
      ```

      **Step 3: Detach from screen.**

      Detach from your screen by typing `Ctrl+a`, then
      clicking `d`.

      **Step 4: View all active screens.**

      ```bash
      screen -ls
      ```

- To run `mongod` **manually as a background process** specifying 
  `--dbpath` and `--logpath` on the command line, run:

  ```bash
  mongod --dbpath /path/to/dbdir --logpath /path/to/mongodb.log --fork
  ```

  To stop a `mongod` running as a background process,
  connect to the `mongod` using `mongosh`,
  and issue the `shutdown` command as needed.

Both methods use the `mongod.conf` file created
during the install. You can add your own MongoDB
configuration options to
this file as well.

**Note:** macOS Prevents `mongod` From Opening

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

To verify that MongoDB is running, perform one of the following:

- If you started MongoDB **as a macOS service**:

  ```bash
  brew services list
  ```

  You should see the service `mongodb-enterprise` listed as
  `started`.

- If you started MongoDB **manually as a background process**:

  ```bash
  ps aux | grep -v grep | grep mongod
  ```

  You should see your `mongod` process in the output.

You can also view the log file to see the current status of your
`mongod` process: `/usr/local/var/log/mongodb/mongo.log`.

### Connect and Use MongoDB

To begin using MongoDB, connect `mongosh` to the
running instance. From a new terminal, issue the following:

```bash
mongosh
```

For information on CRUD (Create, Read, Update, Delete) operations, see:

- write-op-insert
- read-operations-queries
- write-op-update
- write-op-delete

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

### Included Binaries

The installation includes the following binaries:

- The `mongod` server
- The `mongos` sharded cluster query router
- The MongoDB Shell, `mongosh`

**Note:**

The installation also includes the `MongoDB Database Tools`. See brew-installs-dbtools for more information.

### File Paths

In addition, the installation creates the following files and
directories at the location specified below, depending on your Apple
hardware:

|  | Intel Processor | Apple Silicon Processor |
|---|---|---|
| configuration file | `/usr/local/etc/mongod.conf` | `/opt/homebrew/etc/mongod.conf` |
| `log directory` | `/usr/local/var/log/mongodb` | `/opt/homebrew/var/log/mongodb` |
| `data directory` | `/usr/local/var/mongodb` | `/opt/homebrew/var/mongodb` |

See [Apple's documentation](https://support.apple.com/en-us/HT211814)
for the current list of Apple hardware using the Apple Silicon processor. You 
can also run the following command to check where `brew` has installed
these files and directories:

```bash
brew --prefix
```
