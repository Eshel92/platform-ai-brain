<!-- Converted from tutorial/install-mongodb-on-os-x.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community Edition on macOS

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free tier to get started.

## Overview

Use this tutorial to install MongoDB 6.0 Community Edition on
macOS using the third-party [Homebrew](https://brew.sh)
package manager.

Starting with MongoDB 4.4.1, installing MongoDB via Homebrew also
installs the `MongoDB Database Tools`. See
brew-installs-dbtools for more information.

### MongoDB Version

This tutorial installs MongoDB 6.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

## Considerations

### Platform Support

**Note:** EOL Notice

- MongoDB 5.0 Community Edition removes support for macOS 10.13

MongoDB 6.0 Community Edition supports macOS 10.14 or later.

See prod-notes-supported-platforms for more information.

### Production Notes

Before deploying MongoDB in a production environment, consider the
/administration/production-notes document which offers
performance considerations and configuration recommendations for
production MongoDB deployments.

## Install MongoDB Community Edition

### Prerequisites

Ensure your system meets each of the following prerequisites. You only
need to perform each prerequisite step once on your system. If you
have already performed the prerequisite steps as part of an earlier
MongoDB installation using Homebrew, you can skip to the
installation procedure.

#### Install Xcode Command-Line Tools

Homebrew requires the Xcode command-line tools from Apple's Xcode.

- Install the Xcode command-line tools by running the following
  command in your macOS Terminal:

  ```bash
  xcode-select --install
  ```

#### Install Homebrew

macOS does not include the Homebrew `brew` package by default.

- Install `brew` using the official
  [Homebrew installation instructions](https://brew.sh/#install).

### Installing MongoDB 6.0 Community Edition

Follow these steps to install MongoDB Community Edition using Homebrew's
`brew` package manager. Be sure that you have followed the
installation prerequisites above before proceeding.

#. Tap the [MongoDB Homebrew Tap](https://github.com/mongodb/homebrew-brew) to download the official
   Homebrew formula for MongoDB and the Database Tools, by running the
   following command in your macOS Terminal:

   ```bash
   brew tap mongodb/brew
   ```

   If you have already done this for a previous installation of MongoDB,
   you can skip this step.

#. To update Homebrew and all existing formulae:

   ```bash
   brew update
   ```

#. To install MongoDB, run the following command in your macOS Terminal
   application:

   ```bash
   brew install mongodb-community@6.0
   ```

**Tip:**

Alternatively, you can specify a previous version of MongoDB if
desired. You can also maintain multiple versions of MongoDB side by
side in this manner.

**Tip:**

If you have previously installed an older version of the formula,
you may encounter a ChecksumMismatchError. To resolve, see
troubleshooting-checksumerror.

The installation includes the following binaries:

- The `mongod` server
- The `mongos` sharded cluster query router
- The MongoDB Shell, `mongosh`

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

Starting with MongoDB 4.4.1, the installation also includes the
`MongoDB Database Tools`.
See brew-installs-dbtools for more information.

## Run MongoDB Community Edition

Follow these steps to run MongoDB Community Edition. These instructions
assume that you are using the default settings.

You can run MongoDB as a macOS service using `brew`, or you can run
MongoDB manually as a background process. It is recommended to run
MongoDB as a macOS service, as doing so sets the correct system
`ulimit` values automatically (see
ulimit settings for more information).

- To run MongoDB (i.e. the `mongod` process) **as a
  macOS service**, run:

  ```bash
  brew services start mongodb-community@6.0
  ```

  To stop a `mongod` running as a macOS service, use the
  following command as needed:

  ```bash
  brew services stop mongodb-community@6.0
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

  You should see the service `mongodb-community` listed as
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

For information on CRUD (Create,Read,Update,Delete) operations, see:

- /tutorial/insert-documents
- /tutorial/query-documents
- /tutorial/update-documents
- /tutorial/remove-documents

## Using the MongoDB Database Tools

Starting in MongoDB 4.4.1, installing MongoDB via `brew` also installs
the MongoDB Database Tools.

The `MongoDB Database Tools` are a collection of
command-line utilities for working with a MongoDB deployment,
including data backup and import/export tools like
`mongoimport` and `mongodump` as well as monitoring
tools like `mongotop`.

Once you have installed the MongoDB Server in the steps above, the
Database Tools are available directly from the command line in your
macOS Terminal application. For example you could run `mongotop`
against your running MongoDB instance by invoking it in your
macOS Terminal like so:

```bash
mongotop
```

It should start up, connect to your running `mongod`, and start
reporting usage statistics.

See the `MongoDB Database Tools Documentation` for usage information for
each of the Database Tools.

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

### Troubleshooting ChecksumMismatchError

If you have previously installed an older version of the formula,
you may encounter a `ChecksumMismatchError` resembling the following:

```bash
Error: An exception occurred within a child process:

  ChecksumMismatchError: SHA256 mismatch

Expected: c7214ee7bda3cf9566e8776a8978706d9827c1b09017e17b66a5a4e0c0731e1f

  Actual: 6aa2e0c348e8abeec7931dced1f85d4bb161ef209c6af317fe530ea11bbac8f0

 Archive: /Users/kay/Library/Caches/Homebrew/downloads/a6696157a9852f392ec6323b4bb697b86312f0c345d390111bd51bb1cbd7e219--mongodb-macos-x86_64-4.2.0.tgz

To retry an incomplete download, remove the file above.
```

To fix:

#. Remove the downloaded `.tgz` archive.

#. Retap the formula.

   ```bash
   brew untap mongodb/brew && brew tap mongodb/brew
   ```

#. Retry the install.

   ```bash
   brew install mongodb-community@6.0
   ```
