<!-- Converted from tutorial/install-mongodb-enterprise-on-windows-zip.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Enterprise on Windows From a Zip File

## Overview

Use this tutorial to install MongoDB 6.0 Enterprise Edition on
Windows by downloading and extracting the zip file.

MongoDB Enterprise Edition
is available on select platforms and contains support for several
features related to security and monitoring.

### MongoDB Version

This tutorial installs MongoDB 6.0 Enterprise
Edition. To install a different version of MongoDB Enterprise,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

### Installation Method

This tutorial installs MongoDB on Windows by extracting from a zip file. You can 
also install MongoDB on Windows by these other methods:

- Install MongoDB using msiexec.exe

- Install MongoDB using the MSI Installer

## Considerations

### MongoDB Shell, `mongosh`

The MongoDB Shell (`mongosh`) is not installed with
MongoDB Server. You need to follow the `mongosh
installation instructions` to download and install
`mongosh` separately.

### Platform Support

MongoDB 6.0 Enterprise Edition supports the following
64-bit versions of Windows on 
x86_64 architecture:

- Windows Server 2019

- Windows 10 / Windows Server 2016

MongoDB only supports the 64-bit versions of these platforms.

See prod-notes-supported-platforms for more information.

(Include not available offline: includes/fact-wsl-not-supported.rst)

### Virtualization

Oracle offers [experimental support](https://docs.oracle.com/en/virtualization/virtualbox/6.0/admin/hyperv-support.html)
for VirtualBox on Windows hosts where Hyper-V is running. However,
Microsoft does not support [VirtualBox on Hyper-V](https://docs.microsoft.com/en-us/troubleshoot/windows-client/application-management/virtualization-apps-not-work-with-hyper-v).

Disable Hyper-V if you want to install MongoDB on Windows using VirtualBox.

### Production Notes

Before deploying MongoDB in a production environment, consider the
/administration/production-notes document which offers
performance considerations and configuration recommendations for
production MongoDB deployments.

### Full Time Diagnostic Data Capture

MongoDB logs diagnostic data to assist with troubleshooting. For
detailed information, see Full Time Diagnostic Data Capture.

On Windows, to collect system data such as disk, cpu, and memory, FTDC requires Microsoft access permissions from the following groups:

- Performance Monitor Users

- Performance Log Users 

If the user running `mongod` and `mongos` is not an administrator, add them to these groups to log
FTDC data. For more information, see [the Microsoft documentation here](https://learn.microsoft.com/en-us/windows/win32/perfctrs/restricting-access-to-performance-extension--dlls).

## Install MongoDB Enterprise Edition

### Procedure

Follow these steps to install MongoDB Enterprise Edition from the zip file.

**Step 1: Download MongoDB Enterprise Edition.**

Download the MongoDB Enterprise `.zip` file from the following
link:

→ [MongoDB Download Center](https://www.mongodb.com/try/download/enterprise?tck=docs_server)

a. In the Version dropdown, select the version of
   MongoDB to download.

#. In the Platform dropdown, select Windows x64.

#. In the Package dropdown, select zip.

#. Click Download.

**Step 2: Extract the MongoDB files.**

a. Go to the directory where you downloaded the MongoDB `.zip` file. By 
   default, this is your `Downloads` directory. 

#. Double-click the `.zip` file.

#. Extract the files to your preferred location. For example, you may want 
   to use `C:\MongoDB`.

**Step 3: Create Configuration File (Optional).**

You can create a configuration file to specify options for MongoDB. To do so, 
create a file named `mongod.cfg` in the `\bin\` directory within the 
directory where you extracted the MongoDB files 
(`<install directory>\bin\mongod.cfg`). For more information on creating a 
config file, see conf-file.

**Step 4: Create Required and Optional Directories.**

a. MongoDB needs a data directory to store your data. By default,
   it uses `C:\data\db`, but you may specify a different location in 
   your config file. You can create the data directory using the Windows 
   Command Prompt: 

   ```bat
   mkdir c:\data\db
   ```

#. If you specified a log path in the configuration file, create the log 
   directory in the same way.

## Configure MongoDB Enterprise Edition as a Windows Service

You can install and configure MongoDB as a Windows Service.
To do so, follow these steps:

1. Add `<install directory>\bin` to your `PATH` environment variable.

#. Open a Windows Command prompt as an Administrator, change to your MongoDB install 
   directory, and run `mongod` with the `--dbpath`, `--logpath` and `--install` 
   parameters. For example, the following command installs MongoDB as a service 
   that uses `C:\data\db` for its data location and `C:\data\log.txt` for the 
   log file:

   ```bat
   mongod --dbpath=C:\data\db --logpath=C:\data\log.txt --install
   ```

## Start MongoDB Enterprise Edition as a Windows Service

To manually start or restart the MongoDB service, use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click Start.

You can also manually manage the service from the command line. To
start the MongoDB service from the command line, open a `Windows
command prompt/interpreter
<https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/cmd>`__ (`cmd.exe`) as an Administrator, and
run the following command:

**Step 1: Start the MongoDB service.**

Close all other command prompts, then invoke the following command:

```bat
net start MongoDB
```

**Step 2: Verify that MongoDB has started successfully.**

Check your MongoDB log file for the following line:

```none
[initandlisten] waiting for connections on port 27017
```

You may see non-critical warnings in the process
output. As long as you see this message in the MongoDB log, you can
safely ignore these warnings during your initial evaluation of
MongoDB.

**Step 3: Connect to the MongoDB server.**

If you have not already done so, follow the
`mongosh installation instructions` to download
and install the MongoDB Shell (`mongosh`).

Be sure to add the path to your `mongosh.exe` binary to your
`PATH` environment variable during installation. 

Open a new Command Interpreter and enter `mongosh.exe`
to connect to MongoDB.

## Stop MongoDB Enterprise Edition as a Windows Service

To stop/pause the MongoDB service, use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click Stop (or Pause).

You can also manage the service from the command line. To stop the
MongoDB service from the command line, open a `Windows command
prompt/interpreter
<https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/cmd>`__ (`cmd.exe`) as an Administrator, and
run the following command:

```bat
net stop MongoDB
```

## Remove MongoDB Enterprise Edition as a Windows Service

To remove the MongoDB service, first use the Services console to stop
the service. Then open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
(`cmd.exe`) as an Administrator, and run the following
command:

```bat
sc.exe delete MongoDB
```

## Start MongoDB Enterprise Edition from the Command Interpreter

Open a `Windows command prompt/interpreter
<https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/cmd>`__ (`cmd.exe`) as an Administrator.

**Important:**

You must open the command interpreter as an
Administrator.

**Step 1: Create database directory.**

Create the data directory where MongoDB stores data.
MongoDB's default data directory path is the absolute path
`\data\db` on the drive from which you start MongoDB.

From the Command Interpreter, create the data directories:

```bat
cd C:\
md "\data\db"
```

**Step 2: Start your MongoDB database.**

To start MongoDB, run `mongod.exe`.

```bat
"C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"
```

The `--dbpath` option points to your
database directory.

If the MongoDB database server is running correctly, the
Command Interpreter displays:

```bash
[initandlisten] waiting for connections
```

**Important:**

Depending on the
[Windows Defender Firewall](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/)
settings on your Windows host, Windows may display a
Security Alert dialog box about blocking
"some features" of `C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe`
from communicating on networks. To remedy this issue:

a. Click Private Networks, such as my home or work
   network.
b. Click Allow access.

To learn more about security and MongoDB, see the
Security Documentation.

**Step 3: Connect to MongoDB.**

If you have not already done so, follow the
`mongosh installation instructions` to download
and install the MongoDB Shell (`mongosh`).

Be sure to add the path to your `mongosh.exe` binary to your
`PATH` environment variable during installation.

Open a new Command Interpreter and enter `mongosh.exe`
to connect to MongoDB.

For more information on connecting to `mongod` using
`mongosh.exe`, such as connecting to a MongoDB instance
running on a different host and/or port, see
`Connect to a Deployment`.

For information on CRUD (Create, Read, Update, Delete) operations,
see:

- /tutorial/insert-documents
- /tutorial/query-documents
- /tutorial/update-documents
- /tutorial/remove-documents

## Additional Considerations

### Localhost Binding by Default

By default, MongoDB launches with `bindIp` set to
`127.0.0.1`, which binds to the localhost network interface. This
means that the `mongod.exe` can only accept connections from
clients that are running on the same machine. Remote clients will not be
able to connect to the `mongod.exe`, and the `mongod.exe` will
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

### Point Releases and `.msi`

If you installed MongoDB with the Windows installer (`.msi`), the
`.msi` automatically upgrades within the same release series (e.g. 7.2.1 to 7.2.2).

Upgrading a full release series (e.g. 6.0 to 7.0) requires a new
installation.

### Add MongoDB binaries to the System PATH

All command-line examples in this tutorial are provided as absolute
paths to the MongoDB binaries. You can add ``C:\Program
Files\MongoDB\Server\6.0\bin` to your System `PATH`` and then
omit the full path to the MongoDB binaries.
