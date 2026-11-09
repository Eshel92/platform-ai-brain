<!-- Converted from tutorial/install-mongodb-on-windows-unattended.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community on Windows using `msiexec.exe`

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Community Edition on
Windows in an unattended fashion using `msiexec.exe` from the command
line. This is useful for system administrators who wish to
deploy MongoDB using automation.

### MongoDB Version

This tutorial installs MongoDB 7.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

### Installation Method

This tutorial installs MongoDB on Windows by extracting from a zip file. You can 
also install MongoDB on Windows by these other methods:

- Install MongoDB using the MSI Installer

- Install MongoDB from the zip file

## Considerations

### MongoDB Shell, `mongosh`

The MongoDB Shell (`mongosh`) is not installed with
MongoDB Server. You need to follow the `mongosh
installation instructions` to download and install
`mongosh` separately.

### Platform Support

MongoDB 7.0 Community Edition supports the following
64-bit versions of Windows on x86_64 architecture:

- Windows Server 2022

- Windows Server 2019

- Windows 11

MongoDB only supports the 64-bit versions of these platforms.

For more information, see prod-notes-supported-platforms.

(Include not available offline: includes/fact-wsl-not-supported.rst)

### Virtualization

Oracle offers [experimental support](https://docs.oracle.com/en/virtualization/virtualbox/6.0/admin/hyperv-support.html)
for VirtualBox on Windows hosts where Hyper-V is running. However,
Microsoft does not support [VirtualBox on Hyper-V](https://docs.microsoft.com/en-us/troubleshoot/windows-client/application-management/virtualization-apps-not-work-with-hyper-v).

Disable Hyper-V if you want to install MongoDB on Windows using VirtualBox.

### Production Notes

Before deploying MongoDB in a production environment, see the
/administration/production-notes document for
performance considerations and configuration recommendations.

### Full Time Diagnostic Data Capture

MongoDB logs diagnostic data to assist with troubleshooting. For
detailed information, see Full Time Diagnostic Data Capture.

On Windows, to collect system data such as disk, CPU, and memory, FTDC 
requires Microsoft access permissions from the following groups:

- Performance Monitor Users

- Performance Log Users

If the user running `mongod` and `mongos` is not an administrator, add them to these groups to log
FTDC data. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/perfctrs/restricting-access-to-performance-extension--dlls).

## Install MongoDB Community Edition

### Procedure

Follow these steps to install MongoDB Community Edition unattended on
Windows from the `Windows command prompt/interpreter
<https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/cmd>`__ (`cmd.exe`) using `msiexec.exe`.

**Step 1: Download MongoDB Community Edition.**

Download the MongoDB `.msi` installer from the following
link:

→ [MongoDB Download Center](https://www.mongodb.com/try/download/community)

a. In the Version dropdown, select the version of
   MongoDB to download.

#. In the Platform dropdown, select
   Windows.

#. In the Package dropdown, select msi.

#. Click Download.

**Step 2: Run the Windows Installer from the Windows Command Interpreter.**

**Important:**

You must open the command interpreter as an
Administrator.

Use the `.msi` installer to install all MongoDB binaries, including
[MongoDB Compass](https:///www.mongodb.com/products/compass).

From the Command Interpreter, go to the directory containing the
`.msi` installation binary and run:

(Include not available offline: /includes/release/install-windows-default.rst)

The operation installs the binaries to the default directory
`C:\Program Files\MongoDB\Server\7.0\bin`.

To specify a different installation location for the executables,
add the `INSTALLLOCATION` value.

(Include not available offline: /includes/release/install-windows-addlocation.rst)

To suppress the installation of MongoDB
Compass, you must explicitly include the
`SHOULD_INSTALL_COMPASS="0"` argument.

(Include not available offline: /includes/release/install-windows-nocompass.rst)

To install specific MongoDB component sets, you can specify them in
the `ADDLOCAL` argument using a comma-separated list including one
or more of the following component sets:

| Component Set Name | Binaries Included in the Component Set |
|---|---|
| `ServerNoService` | `mongod.exe` |
| `ServerService` | Set up `mongod.exe` as a Windows service. |
| `Router` | `mongos.exe` |
| `MonitoringTools` | `mongostat.exe`, `mongotop.exe` |
| `ImportExportTools` | `mongodump.exe`, `mongorestore.exe`, `mongoexport.exe`, `mongoimport.exe` |
| `MiscellaneousTools` | `mongodecrypt.exe`, `mongokerberos.exe`, `mongoldap.exe` |

For example, to install the MongoDB server
(`mongod.exe`) with the legacy `mongo`
client and then set up the MongoDB server as a Windows service,
run:

(Include not available offline: /includes/release/install-windows-service.rst)

To include Compass in the installs, remove `SHOULD_INSTALL_COMPASS="0"`.

## Start MongoDB Community Edition from the Command Interpreter

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
"C:\Program Files\MongoDB\Server\7.0\bin\mongod.exe" --dbpath="c:\data\db"
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
"some features" of `C:\Program Files\MongoDB\Server\7.0\bin\mongod.exe`
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
- write-op-delete

## Run MongoDB Community Edition as a Windows Service

### Start MongoDB Community Edition as a Windows Service

You can install and configure MongoDB as a Windows Service during 
the install, and the MongoDB service starts upon successful installation.

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

### Stop MongoDB Community Edition as a Windows Service

To stop/pause the MongoDB service, you can use the Services console:

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

### Remove MongoDB Community Edition as a Windows Service

To remove the MongoDB service, first use the Services console to stop
the service. Then open a `Windows command prompt/interpreter
<https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/cmd>`__ (`cmd.exe`) as an Administrator, and
run the following command:

```bat
sc.exe delete MongoDB
```

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

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

For more information on configuring `bindIp`, see
/core/security-mongodb-configuration.

### Point Releases and `.msi`

If you installed MongoDB with the Windows installer (`.msi`), the
`.msi` automatically upgrades within the same release series (e.g. 7.2.1 to 7.2.2).

Upgrading a full release series (e.g. 6.0 to 7.0) requires a new
installation.

### Add MongoDB binaries to the System PATH

If you add `C:\Program Files\MongoDB\Server\7.0\bin` to your
System `PATH`, you can omit the full path to the MongoDB Server
binaries. You should also add the path to `mongosh` if you
have not already done so.
