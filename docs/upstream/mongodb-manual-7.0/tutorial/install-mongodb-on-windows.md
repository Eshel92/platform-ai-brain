<!-- Converted from tutorial/install-mongodb-on-windows.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community Edition on Windows

**Note:** MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas/database)
is a hosted MongoDB service option in the cloud which requires no
installation overhead and offers a free cluster to get started.

## Overview

Use this tutorial to install MongoDB 7.0 Community Edition on
Windows using the default installation wizard.

### MongoDB Version

This tutorial installs MongoDB 7.0 Community
Edition. To install a different version of MongoDB Community,
use the version drop-down menu in the upper-left corner of this page to
select the documentation for that version.

### Installation Method

This tutorial installs MongoDB on Windows using the default MSI
installation wizard. You can also install MongoDB on Windows by these other 
methods:

- Install MongoDB using msiexec.exe. 

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

Follow these steps to install MongoDB Community Edition using
the MongoDB Installer wizard. The installation process installs
both the MongoDB binaries as well as the default
configuration file. The
configuration file is located in the installation directory at
`binmongod.cfg`.

**Step 1: Download the installer.**

Download the MongoDB `.msi` installer from the following
link:

→ [MongoDB Download Center](https://www.mongodb.com/try/download/community)

a. In the Version dropdown, select the version of
   MongoDB to download.

#. In the Platform dropdown, select
   Windows.

#. In the Package dropdown, select msi.

#. Click Download.

**Step 2: Run the installer.**

For example, from the Windows Explorer/File Explorer:

a. Go to the directory where you downloaded the MongoDB installer (`.msi` file).
   By default, this is your `Downloads` directory.

#. Double-click the `.msi` file.

**Step 3: Follow the MongoDB installer wizard**

The wizard steps you through the installation of MongoDB and MongoDB
Compass.

a. Choose Setup Type You can choose either the
   Complete (recommended for most users) or
   Custom setup type. The Complete setup
   option installs MongoDB and the MongoDB tools to the default
   location. The Custom setup option allows you to
   specify which executables are installed and where.

#. Service Configuration
   You can set up MongoDB as a Windows service during the
   install or just install the binaries.

   **service:**

   You can configure and start MongoDB as a Windows
   service during the install, and the MongoDB service is
   started upon successful installation.

   - Select Install MongoD as a Service.

   - Select one of these options:

     - Run the service as Network Service user (Default)

       This is a Windows user account that is built-in to
       Windows.

     - Run the service as a local or domain user

       - For an existing local user account, specify a
         period (`.`) for the Account
         Domain and specify the Account Name
         and the Account Password for the
         user.

       - For an existing domain user, specify the
         Account Domain, Account
         Name and Account Password for that
         user.

     - Service Name. Specify the service
       name. Default name is `MongoDB`. If you already
       have a service with the specified name, you must
       choose another name.

     - Data Directory. Specify the data
       directory, which corresponds to the
       `--dbpath`. If the
       directory does not exist, the installer will create
       the directory and sets the directory access to the
       service user.

     - Log Directory. Specify the Log
       directory, which corresponds to the
       `--logpath`. If the
       directory does not exist, the installer will create
       the directory and sets the directory access to the
       service user.

   **mongodb:**

   If you choose not to configure MongoDB as a Windows
   service, uncheck the Install MongoD as a
   Service.

#. Install MongoDB Compass *Optional*. To have the
   wizard install [MongoDB Compass](https:///www.mongodb.com/products/compass), select
   Install MongoDB Compass (Default).

#. When ready, click Install.

### Install `mongosh`

The `.msi` installer does not include `mongosh`. Follow
the `mongosh installation instructions` to download
and install the shell separately.

### If You Installed MongoDB as a Windows Service

The MongoDB service starts upon successful installation.

If you would like to customize the service, you must stop the service. Customize the 
MongoDB instance by editing the configuration file at 
`<install directory>binmongod.cfg`.

For information about the available configuration options, refer to 
configuration-options.

After making changes, start the service again.

### If You Did Not Install MongoDB as a Windows Service

If you only installed the executables and did not install MongoDB as a
Windows service, you must manually start the MongoDB instance.

See run-mongodb-from-cmd for instructions to start a MongoDB
instance.

## Run MongoDB Community Edition as a Windows Service

You can install and configure MongoDB as a Windows Service during 
installation. The MongoDB service starts upon successful installation. 
Configure the MongoDB instance with the configuration file
`<install directory>binmongod.cfg`.

If you have not already done so, follow the
`mongosh installation instructions` to download and
install the MongoDB Shell (`mongosh`).

Be sure to add the path to your `mongosh.exe` binary to your
`PATH` environment variable during installation.
  
Open a new Command Interpreter and enter `mongosh.exe`
to connect to MongoDB.

For more information on connecting to a `mongod` using
`mongosh.exe`, such as connecting to a MongoDB instance
running on a different host and/or port, see
`Connect to a Deployment`.

For information on CRUD (Create, Read, Update, Delete) operations,
see:

- write-op-insert
- read-operations-queries
- write-op-update
- write-op-delete

### Start MongoDB Community Edition as a Windows Service

To start/restart the MongoDB service, use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click Start.

### Stop MongoDB Community Edition as a Windows Service

To stop/pause the MongoDB service, use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click Stop (or Pause).

### Remove MongoDB Community Edition as a Windows Service

To remove the MongoDB service, first use the Services console to stop
the service. Then open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) (`cmd.exe`) as an Administrator, and
run the following command:

```bat
sc.exe delete MongoDB
```

## Run MongoDB Community Edition from the Command Interpreter

You can run MongoDB Community Edition from the Windows command 
prompt/interpreter (`cmd.exe`) instead of as a service.

Open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) 
(`cmd.exe`) as an Administrator.

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
`.msi` automatically upgrades within its release series (e.g. 7.2.1 to 7.2.2).

Upgrading a full release series (e.g. 6.0 to 7.0) requires a new
installation.

### Add MongoDB binaries to the System PATH

If you add `C:\Program Files\MongoDB\Server\7.0\bin` to your
System `PATH` you can omit the full path to the MongoDB Server
binaries. You should also add the path to `mongosh` if you
have not already done so.
