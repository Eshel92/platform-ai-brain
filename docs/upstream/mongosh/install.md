<!-- Converted from install.txt (reStructuredText). Includes are inlined. -->

# Install mongosh

This section describes how to install `mongosh` on Windows
through the MSI installer.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Prerequisites

To use the MongoDB Shell, you must have a MongoDB deployment to connect
to. 

- For a free cloud-hosted deployment, you can use
  [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

- To learn how to run a local MongoDB deployment, see
  Install MongoDB.

### Supported MongoDB Versions

You can use the MongoDB Shell to connect to MongoDB version 7.0 or
greater.

## Supported Operating Systems

You can install MongoDB Shell on these Windows operating systems:

- Microsoft Windows Server 2016+
- Microsoft Windows 10+

## Procedure

**Note:**

On Windows, `mongosh` preferences and configuration options
are stored in the `%APPDATA%/mongodb/mongosh` directory.

**Step 1: Open the MongoDB Shell download page.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 2: In the Platform dropdown, select Windows 64-bit (10+) (MSI)**

**Step 3: Click Download.**

**Step 4: Double-click the installer file.**

**Step 5: Follow the prompts to install mongosh.**

**Step 6: Confirm that mongosh installed successfully.**

To confirm that `mongosh` installed successfully, open a
command prompt and run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you installed.

This section describes how to install `mongosh` on Windows
through the .zip archive.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Prerequisites

To use the MongoDB Shell, you must have a MongoDB deployment to connect
to. 

- For a free cloud-hosted deployment, you can use
  [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

- To learn how to run a local MongoDB deployment, see
  Install MongoDB.

### Supported MongoDB Versions

You can use the MongoDB Shell to connect to MongoDB version 7.0 or
greater.

## Supported Operating Systems

You can install MongoDB Shell on these Windows operating systems:

- Microsoft Windows Server 2016+
- Microsoft Windows 10+

## Procedure

**Note:**

On Windows, `mongosh` preferences and configuration options
are stored in the `%APPDATA%/mongodb/mongosh` directory.

**Step 1: Open the MongoDB Shell download page.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 2: Download the mongosh installation archive for your operating system.**

Download `mongosh` from the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 3: Extract the files from the downloaded archive.**

Open a `cmd` terminal and run the following command from the
directory that has the `mongosh` `.zip` archive:

```sh
tar -xf mongosh-2.14.1-win32-x64.zip
```

The extracted archive has a `bin` folder that contains two files,
`mongosh.exe` and `mongosh_crypt_v1.dll`.

**Step 4: Add the mongosh binary to your PATH environment variable.**

Ensure that the extracted MongoDB Shell binary is in the desired 
location in your filesystem, then add that location to your `PATH` 
environment variable.

To add the MongoDB Shell binary's location to your 
`PATH` environment variable:

a. Open the Control Panel.

#. In the System and Security category, click 
   System.

#. Click Advanced system settings. The **System 
   Properties** modal displays.

#. Click Environment Variables.

#. In the *System variables* section, select `Path` and click 
   Edit. The **Edit environment variable** modal 
   displays.

#. Click New and add the filepath to your `mongosh` 
   binary.

#. Click OK to confirm your changes. On each other 
   modal, click OK to confirm your changes.

To confirm that your `PATH` environment variable is correctly 
configured to find `mongosh`, open a command prompt and enter the 
`mongosh --help` command. If your `PATH` is configured
correctly, a list of valid commands displays.

**Step 5: Confirm that mongosh installed successfully.**

To confirm that `mongosh` installed successfully, open a
command prompt and run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you installed.

This section describes how to install `mongosh` on macOS through
the Homebrew package manager. To learn how to manually install
`mongosh` from an archive instead, select .zip file
from the Installation Method menu at the top of this
page.

**Important:**

In versions of `mongosh` older than 2.5.8, if you're using
`Node.js` versions ^20.19.5, ^22.18.0, or ^24.3.0, the tab
autocomplete may execute code up to and including potentially
destructive operations. For example,
`db.collection.deleteMany({}).<tab>`.

If you already have `mongosh` installed, to check your
`mongosh` and Node.js versions, run:

```sh
<path-to-mongosh-binary> --build-info
```

Output:

```javascript
{
  "version": "2.5.8",
  "distributionKind": "packaged",
  "buildArch": "x64",
  "buildPlatform": "linux",
  "buildTarget": "unknown",
  "buildTime": "2025-09-09T10:18:30.614Z",
  "gitVersion": "7b6bd25a97ce617f8d5bfa26c36db6d99dc92419",
  "nodeVersion": "v24.9.0",
  "opensslVersion": "3.6.0",
  "sharedOpenssl": true,
  "runtimeArch": "x64",
  "runtimePlatform": "darwin",
  "runtimeGlibcVersion": "N/A",
  "deps": {
    "nodeDriverVersion": "6.19.0",
    "kerberosVersion": "2.2.2"
  }
}
```

To upgrade to the latest `mongosh` and Node.js versions, see
mdb-shell-upgrade.

`mongosh` installed with Homebrew does not provide the same
stability and feature completeness guarantees as the official
builds. For example, Homebrew `mongosh` installations don't
support automatic client-side field level encryption.

## Prerequisites

To use the MongoDB Shell, you must have a MongoDB deployment to connect
to. 

- For a free cloud-hosted deployment, you can use
  [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

- To learn how to run a local MongoDB deployment, see
  Install MongoDB.

### Supported MongoDB Versions

You can use the MongoDB Shell to connect to MongoDB version 7.0 or
greater.

### Homebrew Requirements

To view the complete list of system requirements for Homebrew,
see the
[Homebrew Website](https://docs.brew.sh/Installation).

## Supported Operating Systems

You can install MongoDB Shell on macOS 11 or greater (x64 or
ARM64).

## Procedure

To install `mongosh` with Homebrew:

**Step 1: Install Homebrew.**

Refer to the [Homebrew](https://brew.sh/) website
for the steps to install Homebrew on macOS.

**Step 2: Install the mongosh package.**

Issue the following command from the terminal to install the
`mongosh` package:

```sh
brew install mongosh
```

**Step 3: Confirm that mongosh installed successfully.**

To confirm that `mongosh` installed successfully, run the
following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you installed.

This section describes how to install `mongosh` on macOS using a
downloaded `.zip` file.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

You can install MongoDB Shell on macOS 11 or greater (x64 or
ARM64).

## Procedure

To manually install `mongosh` using a downloaded `.zip`
file:

**Step 1: Open the MongoDB Shell download page.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 2: Download the mongosh installation archive for your operating system.**

Download the appropriate version of `mongosh` for your operating
system. MongoDB provides versions of `mongosh` for Intel and ARM 
architectures.

**Step 3: Extract the files from the downloaded archive.**

Go to the directory that contains the `mongosh` `.zip` archive,
then unpack the `.zip` file. 

If your computer is Intel based, run:

```sh
unzip mongosh-2.14.1-darwin-x64.zip
```

If your computer is ARM based (M1 or M2), run:

```sh
unzip mongosh-2.14.1-darwin-arm64.zip
```

The extracted archive has a `bin` folder that contains two files,
`mongosh` and `mongosh_crypt_v1.dylib`.

If your web browser automatically extracts the archive as part of the
download, or if you extract the archive without using the `unzip`
command, you may need to make the binary executable. 

To make the binary executable, run the following command in the
directory where you extracted the archive:

```sh
chmod +x bin/mongosh
```

**Step 4: Add the downloaded binaries to your PATH environment variable.**

You can either:

- Copy the `mongosh` binary into a directory listed in your
  `PATH` variable, such as `/usr/local/bin`. Run the following
  commands from the directory where you extracted the download file:

  ```sh
  sudo mkdir -p /usr/local/bin/
  sudo mkdir -p /usr/local/lib
  sudo cp mongosh /usr/local/bin/
  sudo cp mongosh_crypt_v1.dylib /usr/local/lib/
  ```

- Create symbolic links to the `MongoDB Shell`. Switch to the
  directory where you extracted the files from the `.tgz` archive.
  Run the following command to create links to a directory already
  in your `PATH` such as `/usr/local/bin`. 

  ```sh
  sudo ln -s $(pwd)/bin/* /usr/local/bin/
  ```

**Step 5: Allow macOS to run mongosh.**

macOS may prevent `mongosh` from running after installation. If
you receive a security error when starting `mongosh` indicating
that the developer could not be identified or verified, perform
the following actions:

a. Open *System Preferences*.

#. Select the *Security and Privacy* pane.

#. Under the *General* tab, click the button to the right of the
   message about `mongosh`, labelled either Open Anyway
   or Allow Anyway depending on your version of macOS.

**Step 6: Confirm that mongosh installed successfully.**

To confirm that `mongosh` installed successfully, run the
following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you installed.

This section describes how to install `mongosh` on Ubuntu 24.04
(Noble).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is available as a PPA (Personal Package Archive)
for these Ubuntu versions:

- Ubuntu 24.04 (Noble)
- Ubuntu 22.04 (Jammy)
- Ubuntu 20.04 (Focal)
- Ubuntu 18.04 (Bionic) (*Deprecated support*)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-8.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-8.3.list`
for your version of Ubuntu:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.3 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.3.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with the included
OpenSSL libraries:

```sh
sudo apt-get install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Ubuntu 22.04
(Jammy).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is available as a PPA (Personal Package Archive)
for these Ubuntu versions:

- Ubuntu 24.04 (Noble)
- Ubuntu 22.04 (Jammy)
- Ubuntu 20.04 (Focal)
- Ubuntu 18.04 (Bionic) (*Deprecated support*)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-8.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-8.3.list`
for your version of Ubuntu:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.3 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.3.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with the included
OpenSSL libraries:

```sh
sudo apt-get install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Ubuntu 20.04
(Focal).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is available as a PPA (Personal Package Archive)
for these Ubuntu versions:

- Ubuntu 24.04 (Noble)
- Ubuntu 22.04 (Jammy)
- Ubuntu 20.04 (Focal)
- Ubuntu 18.04 (Bionic) (*Deprecated support*)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-8.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-8.3.list`
for your version of Ubuntu:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/8.3 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.3.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with the included
OpenSSL libraries:

```sh
sudo apt-get install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Ubuntu 18.04
(Bionic).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

**Important:**

Support for Ubuntu 18.04 (Bionic) is deprecated.

## Supported Operating Systems

MongoDB Shell is available as a PPA (Personal Package Archive)
for these Ubuntu versions:

- Ubuntu 24.04 (Noble)
- Ubuntu 22.04 (Jammy)
- Ubuntu 20.04 (Focal)
- Ubuntu 18.04 (Bionic) (*Deprecated support*)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-7.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-7.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-7.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-7.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-7.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-7.0.list`
for your version of Ubuntu:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with the included
OpenSSL libraries:

```sh
sudo apt-get install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Debian 13
(Trixie).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is supported on Debian versions 11 and greater.

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-8.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-8.3.list`
for your version of Debian:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/debian trixie/mongodb-org/8.3 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.3.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with
its bundled OpenSSL libraries, run the following command.
This build is self-contained and does not depend on the
OpenSSL version installed on your system:

```sh
sudo apt-get install -y mongodb-mongosh
```

Alternatively, you can install a build of `mongosh` that
uses your system's OpenSSL libraries. Choose the package
that matches your system's OpenSSL version. In Debian 13
(Trixie), the default OpenSSL version is 3.0.

To use your system's OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

To use your system's OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Debian 12
(Bookworm).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is supported on Debian versions 11 and greater.

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-8.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-8.3.list`
for your version of Debian:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/debian bookworm/mongodb-org/8.3 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.3.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with
its bundled OpenSSL libraries, run the following command.
This build is self-contained and does not depend on the
OpenSSL version installed on your system:

```sh
sudo apt-get install -y mongodb-mongosh
```

Alternatively, you can install a build of `mongosh` that
uses your system's OpenSSL libraries. Choose the package
that matches your system's OpenSSL version. In Debian 12
(Bookworm), the default OpenSSL version is 3.0.

To use your system's OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

To use your system's OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Debian 11
(Bullseye).

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is supported on Debian versions 11 and greater.

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Import the public key used by the package management system**

From a terminal, run the following command to import
the MongoDB public GPG key from
<https://www.mongodb.org/static/pgp/server-8.0.asc>:

```sh
wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
```

The previous command writes the GPG key to your
system's `/etc/apt/trusted.gpg.d` folder and
displays the key in your terminal. You do not need to
copy or save the key.

If you receive an error indicating that `gnupg` is
not installed, perform the following steps:

#. Install `gnupg` and its required libraries using
   the following command:

   ```sh
   sudo apt-get install gnupg
   ```

#. Retry importing the key:

   ```sh
   wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc
   ```

**Step 2: Create a list file for MongoDB**

Create the list file
`/etc/apt/sources.list.d/mongodb-org-8.3.list`
for your version of Debian:

```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/debian bullseye/mongodb-org/8.3 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.3.list
```

**Step 3: Reload the local package database**

```sh
sudo apt-get update
```

**Step 4: Install the mongosh package**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with
its bundled OpenSSL libraries, run the following command.
This build is self-contained and does not depend on the
OpenSSL version installed on your system:

```sh
sudo apt-get install -y mongodb-mongosh
```

Alternatively, you can install a build of `mongosh` that
uses your system's OpenSSL libraries. Choose the
package that matches your system's OpenSSL version. In
Debian 11 (Bullseye), the default OpenSSL version is 1.1.

To use your system's OpenSSL 3.0 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl3
```

To use your system's OpenSSL 1.1 libraries:

```sh
sudo apt-get install -y mongodb-mongosh-shared-openssl11
```

**Step 5: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Red Hat
Enterprise Linux 10 or Oracle Linux 10 using the `yum` package
manager.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

`mongosh` is available as `yum` package for the
following RHEL (Red Hat Enterprise Linux) platforms:

- RHEL (Red Hat Enterprise Linux) 8+ (x64, ARM64, ppc64le,
  and s390x)
- Oracle Linux 8+ running the Red Hat Compatible Kernel (RHCK).

  MongoDB Shell does not support the Unbreakable Enterprise Kernel
  (UEK).

## Procedure

**Step 1: Configure the package management system (yum)**

Create a
`/etc/yum.repos.d/mongodb-org-8.3.repo` file
with the following contents:

```none
[mongodb-org-8.3]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/10/mongodb-org/8.3/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc
```

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.org/yum/redhat/). Downloads are
organized in the following order:

1. Red Hat or CentOS version (for example, `10`)

#. MongoDB edition (for example, `mongodb-enterprise`)

#. MongoDB release version
   (for example, `8.3`)

#. Architecture (for example, `x86_64`)

**Step 2: Install mongosh**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

**Note:**

If the MongoDB Shell fails to start with the following error on
RHEL 9+ and derivatives such as Amazon Linux 2023, install the
`mongodb-mongosh-shared-openssl3` package:

```none
mongosh: OpenSSL configuration error: ...:error:030000A9:digital
envelope routines:alg_module_init:unknown
option:../deps/openssl/openssl/crypto/evp/evp_cnf.c:61:name=rh-allow-sha1-signatures,
value=yes
```

To install the latest stable version of `mongosh` with the
included OpenSSL libraries:

```sh
sudo yum install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl3
```

This section describes how to install `mongosh` on Red Hat
Enterprise Linux 9 or Oracle Linux 9 using the `yum` package
manager.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

`mongosh` is available as `yum` package for the
following RHEL (Red Hat Enterprise Linux) platforms:

- RHEL (Red Hat Enterprise Linux) 8+ (x64, ARM64, ppc64le,
  and s390x)
- Oracle Linux 8+ running the Red Hat Compatible Kernel (RHCK).

  MongoDB Shell does not support the Unbreakable Enterprise Kernel
  (UEK).

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Configure the package management system (yum)**

Create a
`/etc/yum.repos.d/mongodb-org-8.3.repo` file
with the following contents:

```none
[mongodb-org-8.3]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/8.3/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc
```

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.org/yum/redhat/). Downloads are
organized in the following order:

1. Red Hat or CentOS version (for example, `9`)

#. MongoDB edition (for example, `mongodb-enterprise`)

#. MongoDB release version
   (for example, `8.3`)

#. Architecture (for example, `x86_64`)

**Step 2: Install mongosh**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

**Note:**

If the MongoDB Shell fails to start with the following error on
RHEL 9+ and derivatives such as Amazon Linux 2023, install the
`mongodb-mongosh-shared-openssl3` package:

```none
mongosh: OpenSSL configuration error: ...:error:030000A9:digital
envelope routines:alg_module_init:unknown
option:../deps/openssl/openssl/crypto/evp/evp_cnf.c:61:name=rh-allow-sha1-signatures,
value=yes
```

To install the latest stable version of `mongosh` with the
included OpenSSL libraries:

```sh
sudo yum install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl3
```

**Step 3: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Red Hat
Enterprise Linux 8 or Oracle Linux 8 using the `yum` package
manager.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

`mongosh` is available as `yum` package for the
following RHEL (Red Hat Enterprise Linux) platforms:

- RHEL (Red Hat Enterprise Linux) 8+ (x64, ARM64, ppc64le,
  and s390x)
- Oracle Linux 8+ running the Red Hat Compatible Kernel (RHCK).

  MongoDB Shell does not support the Unbreakable Enterprise Kernel
  (UEK).

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Configure the package management system (yum)**

Create a
`/etc/yum.repos.d/mongodb-org-8.3.repo` file
with the following contents:

```none
[mongodb-org-8.3]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/8/mongodb-org/8.3/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc
```

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.org/yum/redhat/). Downloads are
organized in the following order:

1. Red Hat or CentOS version (for example, `8`)

#. MongoDB edition (for example, `mongodb-enterprise`)

#. MongoDB release version
   (for example, `8.3`)

#. Architecture (for example, `x86_64`)

**Step 2: Install mongosh**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with the
included OpenSSL libraries:

```sh
sudo yum install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl3
```

**Step 3: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Amazon Linux
2023 using the `yum` package manager.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

`mongosh` is available as `yum` package for the
following Amazon Linux platforms:

- Amazon Linux 2023 (x64 and ARM64)
- Amazon Linux 2 (x64 and ARM64)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Configure the package management system (yum)**

Create a
`/etc/yum.repos.d/mongodb-org-8.3.repo` file
with the following contents:

```none
[mongodb-org-8.3]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/8.3/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc
```

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.org/yum/amazon/). Downloads are
organized in the following order:

1. Amazon Linux version (for example, `2023`)

#. MongoDB release version
   (for example, `8.3`)

#. Architecture (for example, `x86_64`)

**Step 2: Install mongosh**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

**Note:**

If the MongoDB Shell fails to start with the following error on
RHEL 9+ and derivatives such as Amazon Linux 2023, install the
`mongodb-mongosh-shared-openssl3` package:

```none
mongosh: OpenSSL configuration error: ...:error:030000A9:digital
envelope routines:alg_module_init:unknown
option:../deps/openssl/openssl/crypto/evp/evp_cnf.c:61:name=rh-allow-sha1-signatures,
value=yes
```

To install the latest stable version of `mongosh` with the
included OpenSSL libraries:

```sh
sudo yum install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl3
```

**Step 3: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Amazon Linux
2 using the `yum` package manager.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

`mongosh` is available as `yum` package for the
following Amazon Linux platforms:

- Amazon Linux 2023 (x64 and ARM64)
- Amazon Linux 2 (x64 and ARM64)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Configure the package management system (yum)**

Create a
`/etc/yum.repos.d/mongodb-org-8.3.repo` file
with the following contents:

```none
[mongodb-org-8.3]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/8.3/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc 
```

You can also download the `.rpm` files directly from the
[MongoDB repository](https://repo.mongodb.org/yum/amazon/). Downloads are
organized in the following order:

1. Amazon Linux version (for example, `2023`)

#. MongoDB release version
   (for example, `8.3`)

#. Architecture (for example, `x86_64`)

**Step 2: Install mongosh**

`mongosh` supports OpenSSL. You can also configure `mongosh` to use
your system's OpenSSL installation.

To install the latest stable version of `mongosh` with the
included OpenSSL libraries:

```sh
sudo yum install -y mongodb-mongosh
```

To install `mongosh` with your OpenSSL 1.1 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl11
```

To install `mongosh` with your OpenSSL 3.0 libraries:

```sh
sudo yum install -y mongodb-mongosh-shared-openssl3
```

**Step 3: Confirm that mongosh installed successfully**

To confirm that `mongosh` installed successfully,
run the following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you
installed.

This section describes how to install `mongosh` on Linux
distributions using a `.tgz` archive.

If you already have `mongosh` installed and want to upgrade to the
latest version, see mdb-shell-upgrade.

## Supported Operating Systems

MongoDB Shell is supported on the following Linux versions:

- Amazon Linux 2023 (x64 and ARM64)
- Amazon Linux 2 (x64 and ARM64)
- Debian 11+
- Oracle Linux 8+ running the Red Hat Compatible Kernel (RHCK).
  MongoDB Shell does not support the Unbreakable Enterprise Kernel (UEK).
- Red Hat Enterprise Linux (RHEL) 8+ (x64, ARM64, ppc64le, and s390x)
- SLES 15
- Ubuntu 20.04+ (x64 and ARM64)

**Note:**

If you are running an older or unsupported Linux distribution,
such as Red Hat Enterprise Linux (RHEL) 7, and do not see a
matching package in the standard install flow, you can try
searching for an archived `mongosh` release from the [mongosh releases page on GitHub](https://github.com/mongodb-js/mongosh/releases). However,
MongoDB doesn't officially support or test these archived
releases.

When you choose an archived asset, select one that matches
your:

- Package format (`.rpm`, `.deb`, or archive)
- CPU architecture (for example, `x86_64`/`amd64` or
  `arm64`)
- Library or runtime requirements shown in the filename (for
  example, an OpenSSL version)

## Procedure

**Step 1: Open the MongoDB Shell download page.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 2: Download the Linux 64-bit .tgz package.**

Download the appropriate version of `mongosh` for your operating
system. MongoDB also provides versions of `mongosh` that use your
system's OpenSSL installation.

See the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 3: Extract the files from the downloaded archive.**

Go to the directory that contains the `.tgz` archive, then unpack
the archive. 

The name of the `.tgz` package varies depending on the version you
downloaded. Replace the `.tgz` package name in the following
command with the name of the package you downloaded and run the
command.

```sh
tar -zxvf mongosh-2.14.1-linux-x64.tgz
```

The extracted archive has a `bin` folder that contains two files,
`mongosh` and `mongosh_crypt_v1.so`.

If your web browser automatically extracts the archive as part of the
download, or if you extract the archive without using the `tar`
command, you may need to make the binary executable.

To make the binary executable, run the following command in the
directory where you extracted the archive:

```sh
chmod +x bin/mongosh
```

**Step 4: Add the downloaded binaries to your PATH environment variable.**

You can either:

- Copy the `mongosh` binary into a directory listed in your
  `PATH` variable, such as `/usr/local/bin`. Run the following
  commands from the directory where you extracted the download file:

  ```sh
  sudo mkdir -p /usr/local/bin/
  sudo mkdir -p /usr/local/lib
  sudo cp mongosh /usr/local/bin/
  sudo cp mongosh_crypt_v1.dylib /usr/local/lib/
  ```

- Create symbolic links to the `MongoDB Shell`. Switch to the
  directory where you extracted the files from the `.tgz` archive.
  Run the following command to create links to a directory already
  in your `PATH` such as `/usr/local/bin`. 

  ```sh
  sudo ln -s $(pwd)/bin/* /usr/local/bin/
  ```

**Step 5: Confirm that mongosh installed successfully.**

To confirm that `mongosh` installed successfully, run the
following command:

```sh
mongosh --version
```

The command returns the version of `mongosh` you installed.

## Next Steps

Now that you've installed `mongosh`, your next step is to
connect to a MongoDB deployment. To learn how to connect
`mongosh` to a local or Atlas deployment, see
mdb-shell-connect.

MongoDB provides a programmatically accessible list of `mongosh`
[downloads](https://downloads.mongodb.com/compass/mongosh.json) that
can be accessed through your application.
