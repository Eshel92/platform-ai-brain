<!-- Converted from installation.txt (reStructuredText). Includes are inlined. -->

# Install the MongoDB Database Tools

[Download from the MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/). To install with a package manager, select your operating
system and package management method in the following steps.

## Steps

**Note:**

If you already installed the MongoDB Server with your system's
package manager, you likely already have the Database Tools
installed. The following command determines if the
Database Tools are already installed on your system:

```shell
sudo dpkg -l mongodb-database-tools
```

**Step 1: Download the Database Tools `.deb` package.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/).
Using the drop-down menu on the right-hand side of the page:

#. Select your Linux Platform and Architecture.
#. Select the `deb` Package.
#. Click the Download button.

If installing on a headless Linux system, click Copy Link
to the right of the Download button to copy the download
link, then use a command line tool such as `wget` or `curl` to
download the `.deb` directly on your Linux system.

**Step 2: Install the downloaded package.**

Navigate to the directory containing the downloaded `.deb` package,
then run the following command to install the Database Tools using
the `apt` package manager:

```sh
sudo apt install ./mongodb-database-tools-*-{+version+}.deb
```

**Note:**

Be sure to include the leading `./` in the command above,
which instructs `apt` to look for this file in the local    
directory instead of searching remote repositories.

**Step 3: Run the installed Tools.**

After you install, you can run any of the Database Tools directly
from your system's command line. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

**Note:**

If you already installed the MongoDB Server with your system's
package manager, you likely already have the Database Tools
installed. The following command determines if the
Database Tools are already installed on your system:

```shell
sudo yum list installed mongodb-database-tools
```

**Step 1: Download the Database Tools `.rpm` package.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/).
Using the drop-down menu on the right-hand side of the page:

#. Select your Linux Platform and Architecture
#. Select the `rpm` Package
#. Click the Download button

If installing on a headless Linux system, click Copy Link
to the right of the Download button to copy the download
link, then use a command line tool such as `wget` or `curl` to
download the `.rpm` directly on your Linux system.

**Step 2: Install the downloaded package.**

Navigate to the directory containing the downloaded `.rpm` package,
then run the following command to install the Database Tools using
the `yum` package manager:

```sh
sudo yum install -y mongodb-database-tools-*-{+version+}.rpm
```

**Step 3: Run the installed Tools.**

After you install, you can run any of the Database Tools directly
from your system's command line. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

**Step 1: Download the Database Tools `.tgz` archive.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/).
Using the drop-down menu on the right-hand side of the page:

#. Select your Linux Platform and Architecture.
#. Select the `tgz` Package.
#. Click the Download button.

If installing on a headless Linux system, click Copy Link
to the right of the Download button to copy the download
link, then use a command line tool such as `wget` or `curl` to
download the `.tgz` directly on your Linux system.

**Step 2: Extract the files from the downloaded archive.**

Run the following command from the directory containing the
downloaded `.tgz` package:

```sh
tar -zxvf mongodb-database-tools-*-{+version+}.tgz
```

**Step 3: Make the DB Tools available in your `PATH`.**

You may wish to make the Database Tools available in your system's
`PATH` environment variable, which allows referencing each tool
directly on the command line by name, without needing to specify its
full path, or first navigating to its parent directory.

You can either:

- Copy the DB Tools binaries from the extracted directory into a
  directory already listed in your `PATH`, such as
  `/usr/local/bin`. Navigate into the extracted directory, then run
  the following command to copy the binaries:

  ```sh
  sudo cp * /usr/local/bin/
  ```

- Add the DB Tools installation directory to your PATH, by editing
  your shell's configuration file. For example, in `bash`, you
  would edit the `~/.bash_profile` file.

**Step 4: Run the installed Tools.**

Once installed, you can run any of the Database Tools directly
from your system's command line. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

**Note:**

Installing the MongoDB Server with Homebrew also installs the Database Tools. The
following command determines if the Database Tools are already
installed on your system:

```shell
brew list | grep mongodb-database-tools
```

**Step 1: Install Homebrew.**

macOS does not include the Homebrew `brew` package by default.
Install `brew` using the official
[Homebrew installation instructions](https://brew.sh/#install).

**Step 2: Tap the MongoDB formula.**

In your macOS Terminal, run the following command to download the
official [MongoDB Homebrew formulae](https://github.com/mongodb/homebrew-brew) for MongoDB and the
Database Tools:

```sh
brew tap mongodb/brew
```

Then, mark the tap as a trusted source:

```sh
brew trust mongodb/brew
```

**Step 3: Install the MongoDB Database Tools.**

In your macOS Terminal, run the following command to install the
MongoDB Database Tools:

```sh
brew install mongodb-database-tools
```

**Tip:**

Once installed, you can later update the Database Tools with:

```sh
brew upgrade mongodb-database-tools
```

**Step 4: Run the installed Tools.**

Once installed, you can run any of the Database Tools directly
from your macOS Terminal. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

**Step 1: Download the Database Tools Zip archive.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/).
Using the drop-down menu on the right-hand side of the page:

#. Select the `macOS x86_64` Platform.
#. Select the `zip` Package.
#. Click the Download button.

**Step 2: Extract the files from the downloaded archive.**

You can either:

- Double-click the downloaded Zip archive to unpack it.
- In your MacOS Terminal, navigate to the directory containing the
  downloaded Zip archive, then run the following command:

  ```sh
  unzip mongodb-database-tools-*-{+version+}.zip
  ```

**Step 3: Make the DB Tools available in your `PATH`.**

You may wish to make the Database Tools available in your system's
`PATH` environment variable, which allows referencing each tool
directly on the command line by name, without needing to specify its
full path, or first navigating to its parent directory.

You can either:

- Copy the DB Tools binaries into a directory listed in your
  `PATH` variable, such as `/usr/local/bin`. Run the following
  command from the directory containing the DB Tools binaries:

  ```sh
  sudo cp * /usr/local/bin/
  ```

- Add the DB Tools installation directory to your PATH, by editing
  your shell's configuration file. For example, in `bash`, you
  would edit the `~/.bash_profile` file.

**Step 4: Run the installed Tools.**

Once installed, you can run any of the Database Tools directly
from your macOS Terminal. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

**Step 1: Download the Database Tools MSI installer.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/).
Using the drop-down menu on the right-hand side of the page:

#. Select the `Windows x86_64` Platform.
#. Select the `msi` Package.
#. Click the Download button.

**Step 2: Run the MSI installer.**

Double-click the downloaded MSI installer to install the
Database Tools. During the install you may customize the
installation directory if desired.

**Step 3: Make the DB Tools available in your `PATH`.**

You may wish to make the Database Tools available in your system's
`PATH` environment variable, which allows referencing each tool
directly on the command prompt by name, without needing to specify
its full path, or first navigating to its parent directory.

Once you've installed the Database Tools, follow the instructions
below to add the install directory to your system's `PATH`
environment variable.:

#. Open the Control Panel.
#. In the System and Security category, click 
   System.
#. Click Advanced system settings. The **System 
   Properties** modal displays.
#. Click Environment Variables.
#. In the *System variables* section, select `Path` and click 
   Edit. The **Edit environment variable** modal 
   displays.
#. Click New and add the filepath to the location where
   you installed the Database Tools.
#. Click OK to confirm your changes. On each other 
   modal, click OK to confirm your changes.

Once set, you can run any of the Database Tools directly
from your command prompt. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

**Step 1: Download the Database Tools Zip archive.**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/database-tools/).
Using the drop-down menu on the right-hand side of the page:

#. Select the `Windows x86_64` Platform.
#. Select the `zip` Package.
#. Click the Download button.

**Step 2: Copy the files from the downloaded archive.**

Double-click the downloaded Zip archive to unpack it and copy the
Database Tools from the `bin` directory to your computer's
filesystem.

**Step 3: Make the DB Tools available in your `PATH`.**

You may wish to make the Database Tools available in your system's
`PATH` environment variable, which allows referencing each tool
directly on the command prompt by name, without needing to specify
its full path, or first navigating to its parent directory.

Once you've copied the Database Tools to the desired location on
your filesystem, follow the instructions below to add that location
to your system's `PATH` environment variable.:

#. Open the Control Panel.
#. In the System and Security category, click 
   System.
#. Click Advanced system settings. The **System 
   Properties** modal displays.
#. Click Environment Variables.
#. In the *System variables* section, select `Path` and click 
   Edit. The **Edit environment variable** modal 
   displays.
#. Click New and add the filepath to the location where
   you copied the Database Tools.
#. Click OK to confirm your changes. On each other 
   modal, click OK to confirm your changes.

Once set, you can run any of the Database Tools directly
from your command prompt. For tool details, see the tool's
reference page.

To check the version installed, run the following command:

```sh
mongodump --version
```

## Overview of Binaries

The Database Tools include the following
binaries:

|  |  |
|---|---|
| Binary Import / Export |  |
| \|nbspc\| \|nbspc\| `mongodump` | Creates a binary export of the contents of a `mongod` database. |
| \|nbspc\| \|nbspc\| `mongorestore` | Restores data from a `mongodump` database dump into a `mongod` or `mongos`. |
| \|nbspc\| \|nbspc\| `bsondump` | Converts BSON dump files into JSON. |
| Data Import / Export |  |
| \|nbspc\| \|nbspc\| `mongoimport` | Imports content from an Extended JSON, CSV, or TSV export file. |
| \|nbspc\| \|nbspc\| `mongoexport` | Produces a JSON or CSV export of data stored in a `mongod` instance. |
| Diagnostic Tools |  |
| \|nbspc\| \|nbspc\| `mongostat` | Provides a quick overview of the status of a currently running `mongod` or `mongos` instance. |
| \|nbspc\| \|nbspc\| `mongotop` | Provides an overview of the time a `mongod` instance spends reading and writing data. |
| GridFS Tools |  |
| \|nbspc\| \|nbspc\| `mongofiles` | Supports manipulating files stored in your MongoDB instance in GridFS objects. |

## Release Artifact Reports

Every release artifact of the Database Tools contains a Software Bill of
Materials (SBOM) report and a static analysis report. Both reports are JSON
files named after the artifact that contains them:

- The SBOM report uses the [CycloneDX](https://cyclonedx.org/)
  format and ends with `.cdx.json`.
- The static analysis report uses the [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)
  format and ends with `.sarif.json`.

For operating system packages, reports are installed with the
package's documentation. For example,
`mongodb-database-tools_100.20.1_amd64.deb` installs them to:

- `/usr/share/doc/mongodb-database-tools/mongodb-database-tools_100.20.1_amd64.deb.cdx.json`
- `/usr/share/doc/mongodb-database-tools/mongodb-database-tools_100.20.1_amd64.deb.sarif.json`

For archives, reports are located at the top level of the archive.
For example, `mongodb-database-tools-ubuntu2404-x86_64-100.20.1.tgz` 
contains:

- `mongodb-database-tools-ubuntu2404-x86_64-100.20.1.tgz.cdx.json`
- `mongodb-database-tools-ubuntu2404-x86_64-100.20.1.tgz.sarif.json`

## Common Tasks

After you install the Database Tools, use the following tools to
work with your MongoDB data:

- To back up a database, see mongodump.
- To restore data from a backup, see mongorestore.
- To import data into a collection, see mongoimport.
- To export data from a collection, see mongoexport.
