<!-- Converted from tutorial/upgrade-ops-manager.txt (reStructuredText). Includes are inlined. -->

# Upgrade Ops Manager

This tutorial describes how to upgrade an existing Ops Manager
installation.

## Upgrade Path

**Warning:** Upgrade Managed Databases to MongoDB 3.6 or Later

Ops Manager 6.0 doesn't support MongoDB 3.4. If you are using
MongoDB 3.4 or earlier and want to upgrade to Ops Manager 6.0, you must
upgrade to at least MongoDB 3.6. However, we recommend that you upgrade
to at least MongoDB 4.0 before upgrading to Ops Manager 6.0.

The version of your existing Ops Manager installation determines the
upgrade path you must take to upgrade to Ops Manager 4.4 or later.

**Important:**

- If you have an Ops Manager 4.2 or later installation with more than one Ops Manager
  host pointing to the same Application Database, you can upgrade
  Ops Manager without incurring monitoring
  downtime. During this upgrade, Ops Manager enters a state known as **Upgrade Mode**. 
  See Upgrade Mode
  for more information.

- To ensure a successful upgrade, you *must* follow the upgrade path 
  for your existing version to perform necessary database migrations.

- To protect your data, Ops Manager refuses to start direct upgrades
  from versions 1.8.x and 2.0.x to version 3.4 or later.

- There are no supported downgrade paths for Ops Manager.

**Note:**

All upgrades for Ops Manager versions 4.2.x and later use 
the same procedure. To upgrade to a
higher version, you must first use this procedure upgrade to the 
latest available patch of your initial version, then use the 
procedure again to upgrade to the next version. If the following
table has additional information related to the upgrade procedure 
for a given version, review it first.

**Important:** Live Migration (push) Deprecated or Not Supported for Source Deployments Managed or Monitored by Ops Manager

- For source deployments running any MongoDB 6.0.+ versions, where the
  deployments are managed or monitored by Ops Manager, live migration (push)
  is not supported.
- For source deployments running any MongoDB 5.0 and earlier versions,
  where the deployments are managed or monitored by Ops Manager, live
  migration (push) is deprecated.
- For source deployments running MongoDB 6.0.+, where the deployments
  are monitored by Cloud Manager, live migration (push) is supported.
  To learn more, see Live Migrate Your MongoDB Cluster Monitored by Cloud Manager to Atlas.

The following table lists upgrade paths for all versions:

* - Existing Version

  - Upgrade Path

* - 7.0.x
  - Upgrade from Ops Manager 7.0.x to the latest available patch 
    version of 7.0 using 
    this procedure.

    To learn more, see Ops Manager 7.0 release notes.

* - 6.0.x
  - Upgrade from Ops Manager 6.0.x to the latest available patch 
    version of 6.0. Then upgrade to the latest available version of 
    7.0. Use this procedure for both
    upgrades.

    To learn more, see Ops Manager 6.0 release notes.

* - 5.0.x
  - Upgrade from Ops Manager 5.0.x to the latest available patch 
    version of 5.0. Then upgrade to the latest available version of 
    6.0. Use this procedure for both
    processes.

    To learn more, see Ops Manager 5.0 release notes.

* - 4.4.x
  - Upgrade from Ops Manager 4.4.x to the latest available patch 
    version of 4.4. Then upgrade to the latest available version of 
    5.0. Use this procedure for both
    processes.

    IMPORTANT: Ops Manager version 4.4.13 fixes a bug that would re-enable
    Ops Manager instances for API (Application Programming Interface) writes during an upgrade.

    To learn more, see: 

    - Ops Manager 4.4 release notes.
    - Ops Manager 4.4.13 release notes.

* - 4.2.x
  - Upgrade from Ops Manager 4.2.x to the latest available patch 
    version of 4.2. Then upgrade to the latest available version of 
    4.4. Use this procedure for both
    processes.

    An unintentional and temporary disabling of TLS (Transport Layer Security) occurs when
    upgrading to versions earlier than 4.2.24. Upgrading to 4.2.24
    or later first avoids this outcome.

    To learn more, see: 

    - Ops Manager 4.2.23 release notes
    - Ops Manager 4.2.24 release notes
    - [CVE-2021-20335](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20335)

* - 4.0.x
  - Use the
    [v4.2 upgrade tutorial](https://www.mongodb.com/docs/ops-manager/v4.2/tutorial/nav/upgrade-application)
    to upgrade from Ops Manager 4.0.x to version 4.2.24 or later. Then 
    use this procedure to upgrade to 
    the latest available version of 4.2.

    An unintentional and temporary disabling of TLS (Transport Layer Security) occurs when
    upgrading to versions earlier than 4.2.24. Upgrading to 4.2.24
    or later first avoids this outcome.

    To learn more, see: 

    - Ops Manager 4.2.23 release notes
    - Ops Manager 4.2.24 release notes
    - [CVE-2021-20335](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20335)

* - 3.6.x
  - Use the
    [v4.0 upgrade tutorial](https://www.mongodb.com/docs/ops-manager/v4.0/tutorial/nav/upgrade-application)
    to upgrade from Ops Manager 3.6.x to version 4.0.x.

* - 3.4.x
  - Use the
    [v3.6 upgrade tutorial](https://www.mongodb.com/docs/ops-manager/v3.6/tutorial/nav/upgrade-application)
    to upgrade from Ops Manager 3.4.x to version 3.6.x.

* - 2.x or earlier
  - Use the
    [v3.4 upgrade tutorial](https://www.mongodb.com/docs/ops-manager/v3.4/tutorial/nav/upgrade-application/)
    to upgrade from Ops Manager 2.x or earlier.

**debian:**

**Warning:**

To maintain existing settings and availability, back up the 
following in your current Ops Manager instance: 

- `conf-mms.properties` and `gen.key` files to a 
  secure location. The `conf-mms.properties` stores settings
  for the Ops Manager instance. The gen.key 
  provides details to encrypt and decrypt Ops Manager\s
  backing databases and user credentials. Ops Manager might delete 
  these files as part of the upgrade process.

As an extra precaution, you may use `mongodump` to create a binary 
export of the `Application Database`. No officially 
supported backup method exists for the Application Database. If the 
upgrade fails, reach out to [MongoDB Support](https://support.mongodb.com) for help fixing the 
issue with the Ops Manager version.

## Considerations

Before upgrading Ops Manager from 6.0 to 7.0, review the following considerations:

### Backing Databases

Ops Manager 7.0.0 requires a minimum of MongoDB 6.0.0 for Ops Manager backing 
databases.

**Note:**

Your MongoDB version for Ops Manager backing databases can't be later than your Ops Manager version.

### Compatible MongoDB Tools

If Ops Manager manages your MongoDB Tools, the tool versions are upgraded 
when you upgrade Ops Manager.

If you run Ops Manager 7.0.x in local mode, you must download and
install a compatible version of the MongoDB Tools TGZ package to the `versions` directory.

| Ops Manager Server Versions | Compatible MongoDB Database Tools Version |
|---|---|
| 7.0.11 | 100.10.0 |
| 7.0.9 | 100.9.5 |
| 7.0.0 | 100.9.4 |

To access older versions of the MongoDB Tools, click
[Archived releases](https://www.mongodb.com/download-center/database-tools/releases/archive) on the Download page.

### Ops Manager and Automation Platform Support

- Removes Ops Manager and MongoDB Agent support for Debian 10.
- Removes Ops Manager and MongoDB Agent support for Ubuntu 18.04 LTS.

**Important:**

Ops Manager 7.0 deprecates support for RedHat Enterprise Linux 7, 
SUSE Linux Enterprise Server 12, and Ubuntu 20.04 LTS.

### Automation Support Changes

- Removes support for automating, monitoring, and backing up MongoDB 
  versions 4.0 and earlier. Ops Manager can only manage databases that 
  run MongoDB 4.2 or later. 

- Removes support for SNMP (Simple Network Management Protocol) alerts. 

  - You can monitor your clusters with Ops Manager instead. To
    learn about other alert options, see third-party-integrations.

- Removes support for the Manage Sharded Collections UI. 

  - Removes the ability to shard a collection, 
    manage the sharded cluster balancer, and manage sharded 
    zones through the UI. You still have full control
    of your sharded cluster available through the command line 
    by using `mongosh`.

### Migration

- Removes support for the MongoDB Cloud Migration Service in Ops Manager. 
  If you need to use push-based migrations to migrate your 
  deployments to MongoDB Atlas, you can use the Cloud Migration Service in MongoDB Cloud Manager.

### User Interface

- Removes support for Internet Explorer 11.

### Configuration Setting Changes

- Updates the accepted value that represents the Application 
  Database authentication method for the `mms.userSvcClass` 
  setting from `com.xgen.svc.mms.svc.user.UserSvcDb` to 
  `com.xgen.cloud.user._private.svc.UserSvcDb`. 

  **Important:**

  If you use the old accepted value, `com.xgen.svc.mms.svc.user.UserSvcDb`, 
  your Ops Manager instance will not start during preflight checks.

## Prerequisites

### Hardware and Software Requirements

Your servers must meet the /core/requirements.

**Warning:** Potential for Production Failure

Your Ops Manager instance can fail in production if you fail to configure the following:

- Ops Manager hosts per the /core/requirements.

- MongoDB hosts per the
  Production Notes in
  the MongoDB manual. MongoDB instances in Ops Manager include:

  - The Ops Manager Application Database,
  - Each blockstore.
  - Each Ops Manager Backup Daemon `head database`. This only
    applies to FCV 4.0 and earlier. FCV 4.2 and later do not use
    `head databases` for backups.

If your backing databases run the MMAPv1 storage engine, the upgrade
process fails. Ops Manager prompts you to
upgrade the storage engine for those backing databases to WiredTiger.

### Administrator Privileges

You must have administrator privileges on the servers on which you
perform the upgrade.

### Download Software from MongoDB

To download the software, click the download link available on the
customer downloads page. MongoDB provides the URL (Uniform Resource Locator) of that page to its
customers.

- If you can't access this link, visit the
  download page for a current evaluation copy of
  the Ops Manager software. 

- If you need an earlier version of the Ops Manager software, visit the
  Release Archive.

### Download Software to Run in Local Mode

If you plan to run Ops Manager in Local Mode,
download the MongoDB software to your versions library directory. The
required software includes:

- All versions of MongoDB Community or
  Enterprise that you want to install
- [MongoDB Tools](https://www.mongodb.com/docs/database-tools/). The version of MongoDB Tools must
  match the version that the Ops Manager release notes list as compatible with your Ops Manager version. 

### Platform Compatibility

Before you upgrade Ops Manager, make sure:

- The platform of the hosts serving Ops Manager is
  compatible with 5.0.
- The MongoDB Agents managing your MongoDB deployments are
  compatible with
  Ops Manager 5.0.
- The platform of the hosts serving the Ops Manager agents are
  compatible with the Agents.
- If you use BI Connector, upgrade MongoDB to 4.0 or later.

If you upgraded the platform for the MongoDB Agent hosts,
upgrade the MongoDB Agents
*before* upgrading Ops Manager.

## Procedure

**Note:** **Upgrade Mode for Highly Available applications**

If you have an Ops Manager 4.2 or later installation with more than one Ops Manager
host pointing to the same Application Database, you can upgrade
Ops Manager without incurring monitoring
downtime. During this upgrade, Ops Manager enters a state known as
**Upgrade Mode**. This mode enables the following benefits throughout the
upgrade process:

- Alerts and monitoring operate
- Ops Manager instances remain live
- Ops Manager Application may be accessed in read-only mode
- Ops Manager API (Application Programming Interface)\s that write or delete data are disabled

Your Ops Manager instance stays in **Upgrade Mode** until all Ops Manager
hosts have been upgraded and restarted.

You should not upgrade more than one Ops Manager host at a time.

When Ops Manager enters upgrade mode, the `Backup Daemons`
attempt to stop themselves. This process can fail if the Daemons are in the 
middle of a long backup job. In this case, do one of the following:

- Restart the first Ops Manager instance once the Backup Daemons finish the job.
- Stop the Backup Daemons manually.

To manually stop your Backup Daemons:

**debian:**

1. Log into the first host that serves a Backup Daemon.

2. Issue the following command:

   ```sh
   sudo service mongodb-mms-backup-daemon stop
   ```

3. Verify that you shut down the Backup Daemon:

   ```sh
   ps -ef | grep mongodb-mms-backup-daemon
   ```

   If the Backup Daemon continues to run, issue this command:

   ```sh
   sudo /etc/init.d/mongodb-mms-backup-daemon stop
   ```

4. Repeat steps 2 to 3 with every other Backup Daemon host.

**rhel:**

1. Log in to the first host that serves a Backup Daemon.

2. Issue the following command:

   ```sh
   sudo service mongodb-mms-backup-daemon stop
   ```

3. Verify that you shut down the Backup Daemon:

   ```sh
   ps -ef | grep mongodb-mms-backup-daemon
   ```

   If the Backup Daemon continues to run, issue this command:

   ```sh
   sudo /etc/init.d/mongodb-mms-backup-daemon stop
   ```

4. Repeat steps 2 to 3 with every other Backup Daemon host.

**linux:**

1. Log into the first host that serves a Backup Daemon.

2. Issue the following command:

   ```sh
   <install_dir>/bin/mongodb-mms-backup-daemon stop
   ```

3. Verify that you shut down the Backup Daemon:

   ```sh
   ps -ef | grep mongodb-mms-backup-daemon
   ```

   If the Backup Daemon continues to run, issue this command:

   ```sh
   sudo /etc/init.d/mongodb-mms-backup-daemon stop
   ```

4. Repeat steps 2 to 3 with every other Backup Daemon host.

If you're running your Ops Manager Application in a
high availability configuration,
complete this procedure on one Ops Manager host at a time.

**debian:**

Use this procedure to upgrade the Ops Manager Application on hosts installed using `deb` packages:

**Step 1: Download the latest version of the Ops Manager package.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Platforms drop-down menu, click 
   Ubuntu 22.04.

#. From the Packages drop-down menu, click
   DEB for x86_64 architecture.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.deb`,
   where `<version>` is the version number.

**Step 2: Stop your first running Ops Manager instance.**

Issue the following command to stop the Ops Manager Application:

```sh
sudo service mongodb-mms stop
```

**Step 3: Install the Ops Manager package on the host that you are upgrading.**

**Note:** Upgrade Mode for Highly Available Ops Manager Application\s

If you have an Ops Manager 4.4 installation with more than one Ops Manager
host pointing to the same Application Database, this Ops Manager
deployment runs with high availability. After you upgrade one
Ops Manager host of a highly available Ops Manager deployment, that
deployment enters **Upgrade Mode**.

a. Install the `.deb` package on each Ops Manager Application and Backup
   Daemon host. Issue the following command, where  `<version>` is
   the version of the `.deb` package:

   ```sh
   sudo dpkg -i mongodb-mms_<version>_x86_64.deb
   ```

b. When prompted whether to overwrite the currently installed version
   of `mms.conf`, you should type `Y` to replace the existing file.

c. If you modified the ports or the
   JVM settings that Ops Manager uses, you need to re-apply those
   changes to the `mms.conf` file after Ops Manager is upgraded.

   **Warning:**

   Don't add passwords or secrets to JVM (Java Virtual Machine) arguments in the `mms.conf`
   file. Ops Manager exposes them as plain text in the diagnostic archives.

   The upgrade to Ops Manager 4.1 and 4.2 removed the `-d64` flag from
   the `JAVA_MMS_UI_OPTS` parameter.

d. When upgrading to Ops Manager 4.4.11, Ops Manager prompts you to choose which version
   of the `/opt/mongodb/mms/conf/conf-mms.properties` file it should use.
   To avoid having to manually reconfigure Ops Manager, choose the
   current file. For more information, see 4.4.11 Release Notes.

**Step 4: Start Ops Manager on the upgraded host.**

```sh
sudo service mongodb-mms start
```

**Note:**

In high availability instances of Ops Manager, the Ops Manager service startup waits
for all servers to upgrade before starting.

Log into your upgraded Ops Manager host after it restarts. If
your login succeeds, the upgrade succeeded.

**Step 5: *[Optional]* Repeat the preceding steps for all other Ops Manager hosts in your High Availability deployment.**

Ops Manager remains in **Upgrade Mode** until every host is upgraded. For 
high availability configurations, 
this means:

- Your hosts might not be fully operational until the upgrade is completed     
  cluster-wide. If your first host upgrade takes longer than expected, continue 
  upgrading the other hosts.

- Do not stop or cancel processes that seem stuck as this might disrupt the upgrade.

- The logs that Ops Manager generates during startup might temporarily pause 
  at `Starting pre-flight checks` while Ops Manager upgrades all its servers
  to the same version. 

- For multi-version upgrades, do not skip major versions.
  You must upgrade each node in the cluster to the last minor version of each major release one at a time.
  For example, to upgrade from 6.0.26 to 8.0.3, do the following steps on *each node*:

  1. Stop the service on a node (running 6.0.26).
  2. Upgrade to the most recent minor version of 7.0.x.
  3. Start the upgraded host before you move to the next node.
  4. Repeat for all other nodes.
  5. Repeat this process to upgrade each node from 7.0.x to 8.0.3.

**Step 6: Update all Agents.**

Once your upgrade has finished, login to your Ops Manager instance.
Ops Manager displays a banner that says One or more agents
are out of date.

Click Update Software Components, then confirm the changes.

**Important:**

If Ops Manager manages your MongoDB Tools, the tool versions are 
upgraded with the agents.

If Ops Manager manages your BI Connector, the BI Connector version 
is upgraded with the agents.

**rhel:**

Use this procedure to upgrade the Ops Manager Application on hosts installed using `rpm` packages:

**Step 1: Stop your first running Ops Manager instance.**

On RHEL, CentOS, SUSE12 hosts that use
[systemd](https://freedesktop.org/wiki/Software/systemd), issue
the following command to stop the Ops Manager Application:

```sh
sudo service mongodb-mms stop
```

For platforms that use `SysVInit`, issue the following command:

```sh
sudo /etc/init.d/mongodb-mms stop   
```

**Step 2: Download the latest version of the Ops Manager package.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Platforms dropdown menu, click one of the
   following options:

   - Red Hat + CentOS 7, 8, 9 / SUSE 12 + 15 / Amazon Linux 2, Amazon Linux 2023

#. From the Packages dropdown menu, click
   RPM.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.rpm`, where `<version>` is the
   version number.

**Step 3: Install the Ops Manager package on the Ops Manager host that you are upgrading.**

**Note:** Upgrade Mode for Highly Available Ops Manager Application\s

If you have an Ops Manager 4.4 installation with more than one Ops Manager
host pointing to the same Application Database, this Ops Manager
deployment runs with high availability. After you upgrade one
Ops Manager host of a highly available Ops Manager deployment, that
deployment enters **Upgrade Mode**.

To install the `.rpm` package on the upgraded Ops Manager host, issue
the following command, where `<version>` is the Ops Manager version:

```sh
sudo rpm -Uvh mongodb-mms-<version>.x86_64.rpm
```

**Warning:**

`rpm` packages for Ops Manager versions 6.0.0, 6.0.1, and 6.0.2 
contained incorrect version information that could cause standard 
upgrades to fail. If upgrading from any of these versions to 
version 6.0.3 or greater, upgrade the package using the 
`--force` flag:

```sh
sudo rpm -Uvh --force mongodb-mms-<version>.x86_64.rpm
```

When upgrading to Ops Manager 5.0.x, Ops Manager keeps the current
`/opt/mongodb/mms/conf/conf-mms.properties` file. Ops Manager
saves the `conf-mms.properties` installed with this version as
`/opt/mongodb/mms/conf/conf-mms.properties.rpmnew`.

**Warning:**

Don't add passwords or secrets to JVM (Java Virtual Machine) arguments in the `mms.conf`
file. Ops Manager exposes them as plain text in the diagnostic archives.

**Step 4: Start Ops Manager on the upgraded host.**

On RHEL, CentOS, SUSE12 hosts that use
[systemd](https://freedesktop.org/wiki/Software/systemd), issue
the following command:

```sh
sudo service mongodb-mms start
```

For platforms that use `SysVInit`, issue the following command:

```sh
sudo /etc/init.d/mongodb-mms start
```

**Note:**

In high availability instances of Ops Manager, the Ops Manager service startup waits
for all servers to upgrade before starting.

**Step 5: *[Optional]* Repeat the preceding steps for all other Ops Manager hosts in your High Availability deployment.**

Log into the Ops Manager host that you upgraded after it restarts. If
your login succeeds, the upgrade succeeded.

If your login succeeded, repeat these steps on the next host in your
high availability Ops Manager deployment.

**Step 6: Update all Agents.**

Once your upgrade has finished, login to your Ops Manager instance.
Ops Manager displays a banner that says One or more agents
are out of date.

Click Update Software Components, then confirm the changes.

**Important:**

If Ops Manager manages your MongoDB Tools, the tool versions are 
upgraded with the agents.

If Ops Manager manages your BI Connector, the BI Connector version 
is upgraded with the agents.

**linux:**

Use this procedure to upgrade Linux systems that do not use
`deb` or `rpm` packages.

**Step 1: Stop your first running Ops Manager instance.**

Issue the following command to stop the Ops Manager Application:

```sh
<install_dir>/bin/mongodb-mms stop
```

**Step 2: Back up configuration files on the Ops Manager host.**

On the Ops Manager host that you're upgrading, back up your existing
configuration files and logs to a directory other than the install
directory.    

**Important:**

You need the backed-up `<install_dir>/conf/conf-mms.properties`
file for later in this procedure.

**Example:**

The following commands back up the configuration files and logs to
your home directory:

```sh
cp -a <install_dir>/conf ~/mms_conf.backup
cp -a <install_dir>/logs ~/mms_logs.backup
```

If the `Versions Directory` is in `<install_dir>` then back it up.

```sh
cp -a <install_dir>/mongodb-releases ~/mms_versions.backup
```

You must also back up the `gen.key` file that Ops Manager uses to
encrypt and decrypt Ops Manager's backing databases and user credentials. 
Ops Manager requires an identical `gen.key` file on every
server that is part of a highly available Ops Manager deployment. 

**Step 3: Download the latest version of the Ops Manager package.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Version dropdown menu, click one of the
   provided stable versions.

#. From the Platform dropdown menu, click one of the
   following options:

   - Red Hat + CentOS 7, 8, 9 / SUSE 12 + 15 / Amazon Linux 2, Amazon Linux 2023
   - Debian 9, 10, 11 / Ubuntu 18.04

#. From the Package dropdown menu, click
   tar.gz.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.tar.gz`,
   where `<version>` is the version number.

**Step 4: Install the Ops Manager package on each host that you are upgrading.**

**Note:** Upgrade Mode for Highly Available Ops Manager Application\s

If you have an Ops Manager 4.4 installation with more than one Ops Manager
host pointing to the same Application Database, this Ops Manager
deployment runs with high availability. After you upgrade one
Ops Manager host of a highly available Ops Manager deployment, that
deployment enters **Upgrade Mode**.

Navigate to the directory into which you want to install Ops Manager.
Extract the archive to that directory:

```sh
tar -zxf mongodb-mms-<version>.x86_64.tar.gz
```

**Important:**

To install a new version in the same directory as the old version,
follow these steps:

a. Rename the current installation directory.

   ```sh
   mv <install_dir> <install_dir_old>
   ```

b. Create a new directory with the original name of your old
   directory.

   ```sh
   mkdir <install_dir>
   ```

This avoids an empty installation directory and code library
conflicts.

**Step 5: On each Ops Manager host, restore the backed up logs and configuration files into the Ops Manager installation directory.**

All log files should be restored.
Most, but not all, configuration file should be restored. Restore:

`conf-mms.properties`
  The settings for this
  Ops Manager deployment.

`gen.key`
  The encryption key for the
  backing databases of this Ops Manager deployment.

**Example:**

These commands restore the configuration files and logs from
your home directory:

```sh
cp -a ~/mms_logs.backup <install_dir>/logs
cp -a ~/mms_conf.backup/conf-mms.properties <install_dir>/conf/conf-mms.properties
cp -a ~/mms_conf.backup/gen.key <install_dir>/conf/gen.key
```

If you backed up the `Versions Directory` previously, restore it to `<install_dir`>.

```sh
cp -a ~/mms_versions.backup <install_dir>/mongodb-releases.
```

**Note:**

In high availability instances of Ops Manager, the Ops Manager service startup waits
for all servers to upgrade before starting.

**Step 6: *Optional.* On each Ops Manager server, merge any needed changes into the `mms.conf` file from your backup.**

The `mms.conf` file is rarely customized, as it contains port and
JVM (Java Virtual Machine) configuration settings. If you modified the ports or the JVM (Java Virtual Machine) settings that Ops Manager uses,
you need to re-apply those changes from your backup
copy to the `mms.conf` file after Ops Manager is upgraded.

**Warning:**

Don't add passwords or secrets to JVM (Java Virtual Machine) arguments in the `mms.conf`
file. Ops Manager exposes them as plain text in the diagnostic archives.

The upgrade to Ops Manager 4.1 and 4.2 removed the `-d64` flag from
the `JAVA_MMS_UI_OPTS` parameter.

**Step 7: Start Ops Manager on the upgraded host.**

Issue the following command:

```sh
<install_dir>/bin/mongodb-mms start
```

**Step 8: *[Optional]* Repeat the preceding steps for all other Ops Manager hosts in your High Availability deployment.**

Log into the Ops Manager host that you upgraded after it restarts. If
your login succeeds, the upgrade succeeded.

If your login succeeded, repeat these steps on the next host in your
high availability Ops Manager deployment.

**Step 9: Update all Agents.**

Once your upgrade has finished, login to your Ops Manager instance.
Ops Manager displays a banner that says One or more agents
are out of date.

Click Update Software Components, then confirm the changes.

**Important:**

If Ops Manager manages your MongoDB Tools, the tool versions are 
upgraded with the agents.

If Ops Manager manages your BI Connector, the BI Connector version 
is upgraded with the agents.

## Troubleshooting

**debian:**

### Unrecognized VM Option

The pre-flight check output or startup log should include an error like
`Unrecognized VM option 'UseParNewGC'`. This error may occur if any of
the following files have been edited:

- `/etc/rc.d/init.d/mongodb-mms`
- `mms.conf`
- `conf-mms.properties`

Remove `-XX:+UseParNewGC` from the config files to resolve this issue.

### Configuration Setting Changes

Depending on your Linux distribution and local configurations,
Ops Manager may replace any changes you made to your configuration file on
upgrade. In Ops Manager 5.0 and later, if you use RPM packages, Ops Manager no longer
updates the configuration file upon upgrade. If a new Ops Manager version
requires new properties in the configuration file, you must add them to
the file upon upgrade.

When upgrading, update the `mongo.mongoUri` value to include the
new parameters introduced with the [MongoDB Java driver](https://mongodb.github.io/mongo-java-driver/3.11/upgrading/). By
default, this driver enables retryable reads and retryable writes. If you
set custom logic to retry reads and writes, the attempts may take too long.
To disable these default values, add the following to your connection string:

**Example:**

mongodb://SERVER:PORT/?maxPoolSize=150&retryWrites=false&retryReads=false

**rhel:**

### Unrecognized VM Option

The pre-flight check output or startup log should include an error like
`Unrecognized VM option 'UseParNewGC'`. This error may occur if any of
the following files have been edited:

- `/etc/rc.d/init.d/mongodb-mms`
- `mms.conf`
- `conf-mms.properties`

Remove `-XX:+UseParNewGC` from the config files to resolve this issue.

### Configuration Setting Changes

Depending on your Linux distribution and local configurations,
Ops Manager may replace any changes you made to your configuration file on
upgrade. In Ops Manager 5.0 and later, if you use RPM packages, Ops Manager no longer
updates the configuration file upon upgrade. If a new Ops Manager version
requires new properties in the configuration file, you must add them to
the file upon upgrade.

**linux:**

### Unrecognized VM Option

The pre-flight check output or startup log should include an error like
`Unrecognized VM option 'UseParNewGC'`. This error may occur if any of
the following files have been edited:

- `/etc/rc.d/init.d/mongodb-mms`
- `mms.conf`
- `conf-mms.properties`

Remove `-XX:+UseParNewGC` from the config files to resolve this issue.

### Configuration Setting Changes

Depending on your Linux distribution and local configurations,
Ops Manager may replace any changes you made to your configuration file on
upgrade. In Ops Manager 5.0 and later, if you use RPM packages, Ops Manager no longer
updates the configuration file upon upgrade. If a new Ops Manager version
requires new properties in the configuration file, you must add them to
the file upon upgrade.

When upgrading, update the `mongo.mongoUri` value to include the
new parameters introduced with the [MongoDB Java driver](https://mongodb.github.io/mongo-java-driver/3.11/upgrading/). By
default, this driver enables retryable reads and retryable writes. If you
set custom logic to retry reads and writes, the attempts may take too long.
To disable these default values, add the following to your connection string:

**Example:**

mongodb://SERVER:PORT/?maxPoolSize=150&retryWrites=false&retryReads=false

### Illegal Reflective Access

This warning displays due to the version of the [Guice library](https://github.com/google/guice) that Ops Manager uses. You can safely ignore this warning.
