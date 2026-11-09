<!-- Converted from tutorial/configure-local-mode.txt (reStructuredText). Includes are inlined. -->

# Configure Deployment to Have Limited Internet Access

By default, Ops Manager, MongoDB Agent, and Backup Daemon hosts download
MongoDB installation binaries over the public internet from MongoDB, Inc.

If your environment restricts which hosts can access the public
internet, Ops Manager, MongoDB Agent, and Backup Daemon hosts can download
MongoDB installation binaries from other locations. You can configure 
the following download modes:

## Remote Mode

This is the default configuration when you deploy Ops Manager. 
If your Ops Manager, MongoDB deployment, and Backup Daemon
hosts can access the public internet, no additional configuration is
necessary.

Choose **Remote Mode** when the Ops Manager, MongoDB deployment, and
Backup Daemon hosts can access the public internet or can access an internal
or external HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure) endpoint that hosts the MongoDB installation
binaries.

**Note:**

If your MongoDB deployments run FCV 4.2 or later, your MongoDB
deployments require access to the public internet or an HTTP (Hypertext Transfer Protocol) or
HTTPS (Hypertext Transfer Protocol Secure) endpoint that hosts the MongoDB installation binaries to run
Ops Manager in Remote Mode.

If you want your Ops Manager, MongoDB Agent, and Backup Daemon hosts to
download the MongoDB installation binaries from an HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure)
endpoint, specify the endpoint using the `Base URL` Ops Manager
configuration setting. To learn more, see the **Remote Mode** instructions in
Configure MongoDB Agent to Use Remote Downloads.

## Hybrid Mode

Choose **Hybrid Mode** when only the Ops Manager hosts in your deployment
can access the public internet. Ops Manager hosts download MongoDB
installer binaries from the internet. MongoDB hosts with MongoDB Agents
download these installers from the Ops Manager hosts and then install or
upgrade MongoDB deployments.

To manage MongoDB hosts without internet access, you must
specify that the 
Source for agents to download MongoDB binaries is
hybrid. To learn more, see the **Hybrid Mode** instructions in
Configure MongoDB Agent to Use Hybrid Downloads.

## Local Mode

Choose **Local Mode** when none of the hosts in your deployment can
access the public internet or an internal or external HTTP or HTTPS 
endpoint that hosts the MongoDB installation binaries. Instead, the 
required MongoDB binaries must be loaded onto each Ops Manager host
and then downloaded using MongoDB Backup Daemons and MongoDB Agents.
 

To manage MongoDB hosts and run Ops Manager without internet access, you must
specify that the Source for agents to download MongoDB binaries
is local. To learn more, see the **Local Mode** instructions in
Configure MongoDB Agent to Use Local Downloads.

## Considerations

### MongoDB Community for Windows with TLS (Transport Layer Security) Incompatibility

Ops Manager supports MongoDB Community Edition for Microsoft Windows with
TLS (Transport Layer Security) in the following versions:

- MongoDB versions 3.2.12 or later
- MongoDB versions 3.4.1 or later
- MongoDB release series 3.6, 4.0, and 4.2

To use earlier versions, you must download them from
MongoDB.

## Prerequisites

If you configure an HTTP proxy for Ops Manager,
the Backup Daemon, and the MongoDB Agents:

- Consider adding sites from which to download the version
  manifest to the firewall allow list.

- Exclude internal hosts from the proxy.

### Install MongoDB Enterprise Dependencies

If you plan on running
`MongoDB Enterprise` on Linux
hosts, then you must manually install a set of dependencies to each
host *before installing MongoDB*. The MongoDB manual provides the
appropriate command to install the dependencies. To install the
dependencies, see the instructions for the appropriate host platform:

- Red Hat

- Ubuntu

- Debian

- SUSE

- Amazon AMI

### Required User Role to Change Mode

To configure internet access for Ops Manager and MongoDB Agents,
you must have Global Owner access to
Ops Manager.

## Configure MongoDB Agents to Use Remote, Hybrid, or Local Downloads

**remote:**

### Configure MongoDB Agents to Use Remote Downloads

**Step 1: Set the source for Ops Manager and MongoDB Agents to install binaries to the Ops Manager Application Server.**

a. Click Admin in the upper right corner to open system
   administration.

#. From the General tab, click
   Ops Manager Config.

#. Click the Miscellaneous tab at the top of the page.

#. In the MongoDB Version Management section, select the 
   following settings:

   * - Option
     - Action

   * - Installer Download Source

     - Select remote.

       All necessary installers are downloaded over the internet 
       from MongoDB, Inc. or from another HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure) endpoint 
       that the hosts can access.

   * - Base URL

     - HTTP (Hypertext Transfer Protocol) endpoint to fetch MongoDB binaries from. If the
       endpoint uses HTTPS (Hypertext Transfer Protocol Secure), Ops Manager validates the certificate using
       the Certificate Authority file set in `httpsCAFile`. If
       unset, Ops Manager downloads MongoDB binaries from the remote
       URLs of **mongodb.com** and **fastdl.mongodb.org**.

       Ops Manager Application hosts require an internet connection.

   * - Versions Directory
     - Accept the platform default value unless you need to
       change it to meet a requirement for your environment.

       The default locations for the `Versions Directory`
       depend on your Ops Manager host platform:

       | Platform | Versions Directory Default Path |
       |---|---|
       | RHEL, Ubuntu | `/opt/mongodb/mms/mongodb-releases` |
       | Linux Archive | `<userSelected>/mongodb-releases` |
       | Windows | `C:\MMSData\MongoDBReleases` |

       The Ops Manager Application expects the MongoDB binaries to be
       stored in this directory on every Ops Manager host.

   * - Backup Versions Auto Download
     - Select `true` if your `Backup Daemon` and
       Ops Manager Application run on the same platform (chip
       architectures, operating systems, or operating system
       versions). If they run on separate platforms, select
       `false`.

   * - Backup Versions Auto Download Enterprise Builds
     - Select `true` if you want the Backup Daemon to download
       MongoDB Enterprise builds as well as MongoDB Community
       builds.

       Queryable Backups require MongoDB Enterprise. 

   * - Required Module for Backup
     - Select which build of MongoDB you want the
       `Backup Daemon` to use for the `head database`.
       Select Enterprise Required if you want the
       Backup Daemon to download only MongoDB Enterprise builds.

       FCV `4.2` and later use 
       backup cursors instead of
       `head databases`. For
       more information, see backup-daemon.

**Step 2: Review and approve your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.

#. Otherwise, click Cancel and you can make
   additional changes.

**hybrid:**

### Configure MongoDB Agents to Use Hybrid Downloads

**Step 1: Set the source for Ops Manager and MongoDB Agents to install binaries to the Ops Manager Application Server.**

a. Click Admin in the upper right corner to open system
   administration.

#. From the General tab, click
   Ops Manager Config.

#. Click the Miscellaneous tab at the top of the page.

#. In the MongoDB Version Management section, select the 
   following settings:

   * - Option
     - Action

   * - Installer Download Source

     - Select hybrid.

       All necessary installers are downloaded from Ops Manager Application
       hosts. MongoDB Agent hosts do not need an internet
       connection.

   * - Base URL

     - HTTP (Hypertext Transfer Protocol) endpoint to fetch MongoDB binaries from. If the
       endpoint uses HTTPS (Hypertext Transfer Protocol Secure), Ops Manager validates the certificate using
       the Certificate Authority file set in `httpsCAFile`. If
       unset, Ops Manager downloads MongoDB binaries from the remote
       URLs of **mongodb.com** and **fastdl.mongodb.org**.

       Ops Manager Application hosts require an internet connection.

   * - Versions Directory
     - Accept the platform default value unless you need to
       change it to meet a requirement for your environment.

       The default locations for the `Versions Directory`
       depend on your Ops Manager host platform:

       | Platform | Versions Directory Default Path |
       |---|---|
       | RHEL, Ubuntu | `/opt/mongodb/mms/mongodb-releases` |
       | Linux Archive | `<userSelected>/mongodb-releases` |
       | Windows | `C:\MMSData\MongoDBReleases` |

       The Ops Manager Application expects the MongoDB binaries to be
       stored in this directory on every Ops Manager host.

   * - Backup Versions Auto Download
     - Select `true` if your `Backup Daemon` and
       Ops Manager Application run on the same platform (chip
       architectures, operating systems, or operating system
       versions). If they run on separate platforms, select
       `false`.

   * - Backup Versions Auto Download Enterprise Builds
     - Select `true` if you want the Backup Daemon to download
       MongoDB Enterprise builds as well as MongoDB Community
       builds.

       Queryable Backups require MongoDB Enterprise. 

   * - Required Module for Backup
     - Select which build of MongoDB you want the
       `Backup Daemon` to use for the `head database`.
       Select Enterprise Required if you want the
       Backup Daemon to download only MongoDB Enterprise builds.

       FCV `4.2` and later use 
       backup cursors instead of
       `head databases`. For
       more information, see backup-daemon.

**Step 2: Review and approve your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.

#. Otherwise, click Cancel and you can make
   additional changes.

**local:**

### Determine the Binaries to Store Locally and Download

Use this section to create a list of the binaries that you need 
to store locally and download.

#### MongoDB Server

Determine the version of MongoDB Server required for 
deployments, including the desired operating system, 
architecture, and Community or Enterprise editions.

For all MongoDB versions on all platforms that Ops Manager supports, MongoDB 
provides Community and Enterprise installation binaries that it stores as compressed 
`.tgz` archives for all platforms, except Windows, and as 
`.zip` archives for Windows.

For local mode, you must download the `.tgz` or `.zip` binaries 
for:

- Each platform and version that your current and planned
  MongoDB deployments run.

- Each platform and version along the
  upgrade path of
  any existing MongoDB deployments you want to upgrade.

  **Note:**

  If you download a binary archive using Microsoft Edge, the
  archive downloads with a `.gz` extension instead of a 
  `.tgz` extension. Change this file's extension to `.tgz` 
  before you continue.

  **Example:**

  If you import an existing deployment of MongoDB 3.4
  Community on Ubuntu 14.04 and want to upgrade it to
  MongoDB 4.0 Enterprise on Ubuntu 14.04, you must
  download and store all archived (`.tgz`) binaries for the 
  following versions:

  - MongoDB 3.4 Community Edition
  - MongoDB 3.6 Community Edition
  - MongoDB 4.0 Community Edition
  - MongoDB 4.0 Enterprise Edition

- If you are running backups, you need the MongoDB binary for
  the platform on which the Ops Manager `Backup Daemon`
  runs.

  **Example:**

  If you are running a MongoDB replica set on MongoDB 3.6.8
  on a set of Ubuntu hosts and running Ops Manager on Windows,
  you must download and store archived binaries of MongoDB 
  3.6.8 for Ubuntu (`.tgz`) and for Windows (`.zip`).

- If you are running queryable backups, you need the Enterprise edition of 
  the MongoDB version that your deployment runs.

  **Example:**

  If you are running a MongoDB replica set on MongoDB 3.6.8
  on a set of Ubuntu hosts and want to query backups from
  an Ops Manager install on Windows, you must download and store
  archived binaries of MongoDB Community 3.6.8 for Ubuntu 
  (`.tgz`) and MongoDB Enterprise 3.6.8 Windows (`.zip`).

#### MongoDB Database Tools

Determine the version of MongoDB Tools that your Ops Manager version
requires. Check the mms-changelog to see what MongoDB 
Tools version your Ops Manager version requires. During Ops Manager 
upgrades, ensure you have the latest version that your new 
version of Ops Manager requires.

For each platform and version that you need to support, 
you must download the MongoDB Database Tools in the `.tgz` format into the 
`Versions Directory`. These tools include 
`mongodump` and `mongorestore`.

**Note:**

MongoDB Community and Enterprise Server installation binaries no longer
include the MongoDB Database Tools. You must
download and install the MongoDB Database Tools
separately, in the `.tgz` format. Check the 
release notes to determine
which version of the MongoDB Database Tools you
should install.

Starting with Ops Manager Server 6.0.4 and
Ops Manager Server 5.0.16, Ops Manager uses
Amazon 2 packages instead of RHEL7 packages on Amazon 2 hosts for
MongoDB Tools.

#### MongoDB Shell

If you have Ops Manager 7.0.5 or later, you can optionally download 
`mongosh`. Determine the `mongosh` version that your Ops Manager 
version uses. Check the mms-changelog to see what 
`mongosh` version your Ops Manager version uses. During 
Ops Manager upgrades, ensure you have the latest version that your 
new version of Ops Manager uses.

### Configure MongoDB Agents to Use Local Downloads

**Step 1: Set the source for Backup Daemons and MongoDB Agents to install binaries to the Ops Manager Application Server.**

a. Click Admin in the upper right corner to open system
   administration.

#. From the General tab, click
   Ops Manager Config.

#. Click the Miscellaneous tab at the top of the page.

#. In the MongoDB Version Management section, select the 
   following settings:

   * - Option
     - Action

   * - Installer Download Source

     - Select local.

       All necessary installers are downloaded from Ops Manager
       Application Servers. MongoDB Agent hosts do not need an
       internet connection.

       An Ops Manager administrator provides installers from the
       MongoDB Download Center into the
       `Versions Directory`. Ops Manager serves them to
       MongoDB Agent hosts. The Version Manifest must be
       updated manually.
       No hosts in the deployment require an internet connection.

   * - Versions Directory
     - Accept the plaform default value unless you need to
       change it to meet a requirement for your environment.

       The default locations for the `Versions Directory`
       depend on your Ops Manager host platform:

       | Platform | Versions Directory Default Path |
       |---|---|
       | RHEL, Ubuntu | `/opt/mongodb/mms/mongodb-releases` |
       | Linux Archive | `<userSelected>/mongodb-releases` |
       | Windows | `C:\MMSData\MongoDBReleases` |

       The Ops Manager Application expects the MongoDB binaries to be
       stored in this directory on every Ops Manager host.

   * - Backup Versions Auto Download
     - Select `true` unless your `Backup Daemon` and
       Ops Manager Application run on different platforms (chip
       architectures, operating systems, or operating system
       versions). If they run on separate platforms, select
       `false`.

   * - Backup Versions Auto Download Enterprise Builds
     - Select `true` if you want the Backup Daemon to download
       MongoDB Enterprise builds as well as MongoDB Community
       builds.

   * - Required Module for Backup
     - Select which build of MongoDB you want the
       `Backup Daemon` to use for the `head database`.
       Select Enterprise Required if you want the 
       Backup Daemon to download only MongoDB Enterprise builds.

       FCV `4.2` and later use 
       backup cursors instead of
       `head databases`. For
       more information, see backup-daemon.

**Step 2: Download the required binaries.**

Review the list that you prepared, in the 
om-determine-binaries section before this 
procedure, of the binaries that you need to store locally and 
download.

Using a computer connected to the Internet, go to the
MongoDB Download Center and download the MongoDB
binary archives for the appropriate platforms and versions.

Binaries are stored as compressed archives (`.tgz` for all platforms except Windows,  and `.zip` for Windows).

**Note:**

If you download a binary archive using Microsoft Edge, the
archive downloads with a `.gz` extension instead of a `.tgz`
extension. Change this file extension to `.tgz` before continuing.

a. Download the Community Server, Enterprise Server, or both.

   **community:**

   To download MongoDB Community Server:

   i. Go to the MongoDB Download Center.

   #. Click Servers and then click
      MongoDB Community Server.

   #. In the Version dropdown menu, click the
      desired MongoDB version. By default, this menu displays
      the current release. This menu also provides the
      current version of all active release series and the
      current development series.

   #. In the OS dropdown menu, click the desired
      platform. By default, this menu displays the platform
      of the computer that is accessing this page.

   #. In the Package dropdown menu, click the
      desired packaging for the download. By default, this
      menu displays an archive file format: `.zip` for
      Windows, `.tgz` for all other platforms.

   #. Click Download.

   To download an older version of the Community Server:

   i. Click the All Version Binaries link to the
      right of the Download button.

   #. Download the **archive file** for each MongoDB host
      platform that Ops Manager manages.

   **enterprise:**

   To download
   `MongoDB Enterprise Server`:

   i. Go to the MongoDB Download Center.

   #. Click Servers and then click
      MongoDB Enterprise Server.

   #. In the Version dropdown menu, click the
      desired MongoDB version. By default, this menu displays
      the current release. This menu also provides the
      current version of all active release series and the
      current development series.

   #. In the OS dropdown menu, click the desired
      platform. By default, this menu displays the platform
      of the computer that is accessing this page.

   #. In the Package dropdown menu, click the
      desired packaging for the download. By default, this
      menu displays an archive file format: `.zip` for
      Windows, `.tgz` for all other platforms.

   #. Click Download.

   To download an older version of the Enterprise Server:

   i. To download the older versions, click
      Archived Releases.

   #. For each platform and MongoDB version you want to
      download, click the link to the right of the
      Archive label.

#. Download the MongoDB Database Tools in 
   the `.tgz` format.

#. (Optional) Download MongoDB Shell.

**Step 3: Populate all Ops Manager hosts with the necessary MongoDB binaries and archives.**

On *all* your Ops Manager hosts, copy all of the archived binaries (in `.tgz`
for all platforms other than Windows, or `.zip` for Windows) for
MongoDB Server,
MongoDB Database Tools, and MongoDB Shell into the `Versions Directory`. Include each 
platform and version of these binaries that you plan to support.

`This directory` stores all of the
archived and extracted binaries. Ops Manager needs these binaries in the `.tgz`
or `.zip` formats to install and upgrade MongoDB deployments and tools.

**Step 4: Ensure that the Ops Manager Linux user can read files in the Versions Directory. (Linux only)**

On a Linux platform, the `mongodb-mms` user needs the read
permissions to the `Versions Directory`.

a. Change ownership of all files and  directories in the Versions
   Directory to `mongodb-mms`.

   ```sh
   sudo chown -R mongodb-mms:mongodb-mms <path-to-the-versions-directory>/*
   ```

b. Change permissions on all the files under the
   Versions Directory to allow the:

   - **Owner** to read and write them
   - **Group** to read them

   When you set these permissions, Ops Manager can read and extract the
   archived binaries. Do not remove the execute permission from any
   directories under the
   `Versions Directory`. If you did, the
   `Backup Daemon` cannot access any files inside those
   directories.

   ```sh
   sudo chmod -R 640 <path-to-the-versions-directory>/*.tgz \
     <path-to-the-versions-directory>/*.zip
   ```

If these steps were successful, the resulting list of the
`Versions Directory` should look similar to the following example.
This example may not reflect the list of currently supported versions.

```sh
-rw-r----- 1 mongodb-mms mongodb-mms 116513825 Apr 27 15:06 mongodb-linux-x86_64-2.6.9.tgz
-rw-r----- 1 mongodb-mms mongodb-mms  51163601 May 22 10:05 mongodb-linux-x86_64-amazon-3.0.3.tgz
-rw-r----- 1 mongodb-mms mongodb-mms  50972165 May 22 10:06 mongodb-linux-x86_64-suse12-3.6.4.tgz
-rw-r----- 1 mongodb-mms mongodb-mms  95800685 Apr 27 15:05 mongodb-linux-x86_64-enterprise-amzn64-2.6.9.tgz
-rw-r----- 1 mongodb-mms mongodb-mms  50594134 Apr 27 15:04 mongodb-linux-x86_64-enterprise-amzn64-3.0.2.tgz
-rw-r----- 1 mongodb-mms mongodb-mms  50438645 Apr 27 15:04 mongodb-linux-x86_64-enterprise-suse12-3.6.4.tgz
drwxrwx--- 1 mongodb-mms mongodb-mms      4096 Apr 27 15:04 mongodb-linux-x86_64-enterprise-suse12-3.6.4
```

Repeat these steps on each Ops Manager host.

**Step 5: Update the version manifest for Ops Manager on each Ops Manager host.**

The version manifest provides Ops Manager with a list of all
released MongoDB versions available to your Ops Manager hosts.

a. Log in to Ops Manager.

#. Click Admin in the upper right
   corner to open system administration.

#. Click the General tab.

#. Click Version Manifest.

#. Click the Update MongoDB Version Manifest button.

#. The `version manifest` should update automatically.

If the update via the web browser does not work, you need to
copy and paste the `version manifest` to your Ops Manager
hosts.

a. From a computer that can access both the Internet, download
   the version manifest from [https://opsmanager.mongodb.com/static/version_manifest/7.0.json](https://opsmanager.mongodb.com/static/version_manifest/7.0.json).

#. Transfer the `version manifest` to a computer that can
   connect to your Ops Manager Application.

#. Open the manifest JSON file.

#. Select all of the contents and copy them to the clipboard.

#. Log in to Ops Manager.

#. Click Admin in the upper right
   corner to open system administration.

#. Click the General tab.

#. Click Version Manifest.

#. Click the Update MongoDB Version Manifest button.

#. Paste the version manifest in the box.

#. Click Save.

**Step 6: Ensure you have downloaded MongoDB binaries in your Versions Directory.**

For the selected versions, ensure that you have downloaded and
placed the archived binaries in the
`Versions Directory`. Otherwise, Ops Manager fails a
pre-flight check when starting in Local Mode. 

**See also:**

Start Ops Manager When All Versions Are Not Downloaded.

**Step 7: Review and approve your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.

#. Otherwise, click Cancel and you can make
   additional changes.
