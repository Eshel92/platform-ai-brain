<!-- Converted from reference/program/install_compass.txt (reStructuredText). Includes are inlined. -->

# `install_compass`

## Synopsis

`install_compass` (`Install-Compass` in Windows) is a
platform-specific installation script for
MongoDB Compass.

If downloaded as a part of the
[MongoDB Enterprise Server](https://www.mongodb.com/try/download/enterprise)
package, the `install_compass` script installs the standard edition
of MongoDB Compass.

If downloaded as part of the
[MongoDB Community Server](https://www.mongodb.com/try/download/community)
package, the `install_compass` script installs
MongoDB Compass Community edition.

## Installation

**Note:**

The `install_compass` script first removes and replaces any
previously installed versions of the same MongoDB Compass edition (either
MongoDB Compass or MongoDB Compass Community).

For example, if you run the `install_compass` script installed as part of
MongoDB Community Server 5.0, the script removes any installed
versions of MongoDB Compass Community and installs a compatible
version of Compass Community.

### Linux / macOS

On Linux and macOS platforms the `install_compass` script is a Unix
executable script included in the MongoDB Server download. The script
is packaged with the download for each platform.

1. Change to the `bin` directory under the MongoDB Server
   download directory:

   ```bash
   cd <installDirectory>/bin
   ```

2. Install MongoDB Compass using the `install_compass` script:

   ```bash
   ./install_compass
   ```

### Windows

On Windows platforms the `Install-Compass` script is a PowerShell
script included in both the MongoDB Server `.zip` archive and
`.msi` installer downloads.

From the Windows Command Prompt:

1. Change to the `bin` directory under the MongoDB Server
   download directory:

   ```none
   cd <installDirectory>\bin
   ```

2. Install MongoDB Compass using the `install_compass` script:

   ```none
   powershell .\Install-Compass.ps1
   ```

Alternatively, if using the `.msi` installer for MongoDB Server for
Windows, during installation you are presented with a checkbox
indicating whether to install MongoDB Compass with MongoDB server. If
checked, the installer automatically executes the `install_compass`
script.
