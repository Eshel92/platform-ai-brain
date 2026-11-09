<!-- Converted from tutorial/install-mongodb-agent-to-manage.txt (reStructuredText). Includes are inlined. -->

# Install the MongoDB Agent to Manage Deployments

You have a project and want to install the MongoDB Agent to manage your
MongoDB deployments. You can also monitor and back up your MongoDB
deployments following this workflow.

**Note:** Review the Prerequisites First

Please review the /tutorial/install-mongodb-agent-prereq
before installing the MongoDB Agent.

**windows:**

Use this procedure to install the MongoDB Agent on x86_64
architecture running Microsoft Windows:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click Windows - MSI.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click Windows - MSI.

**Step 3: Download the MongoDB Agent.**

The MongoDB Agent Installation Instructions box
displays the following information:

- Base URL

  *Required for binding to a project.*

- Project ID
  (Required for binding to a project)

- API Key

  If you do not have an API Key, click plus
  Generate Key.

Some or all of these values are required in a later step. Copy these
values then store them where you can access them later.

**Step 4: Install the MongoDB Agent.**

tabs:
  - id: interactive
    name: Interactive
    content: |

      a. After the `MSI` downloads, double-click:

         `mongodb-mms-automation-agent-<VERSION>.windows_x86_64.msi`

      #. If a security warning appears, click Run.

      #. At the Configuration/Log Folder step

         Provide the directory into which these files are saved.

      #. At the Key Type step, select Agent
         API Key to bind to a specific `project`.

      #. Enter the appropriate agent keys.

         **Note:**

         These keys are provided in the MongoDB
         Agent Installation Instructions modal described in
         the previous step.

         - Type your `Base URL` into the
           Base URL field.

         - Type your Project ID into the Project ID
           field.

         - Type your Agent API Key into the
           Agent API Key field.

      #. At the MongoDB Paths step, specify the Log
         and Backup directories

      #. At the Windows Firewall Configuration step,
         click your preferred firewall configuration.

         If you click Configure firewall rules allowing
         access from only the specified :abbr:IP (Internet Protocol)` addresses.`, type
         the necessary IPv4 (Internet Protocol version 4) addresses into the provided box.

      #. (Conditional) Windows enables [Stealth Mode](https://technet.microsoft.com/en-us/library/dd448557(v=ws.10).aspx)
         for the Windows Firewall by default. If you have not
         disabled it on the MongoDB host on which you are
         installing the MongoDB Agent, you are asked to disable
         it. Stealth Mode significantly degrades the performance
         and capability of the MongoDB Agent. Click
         Disable Stealth Mode.

      #. (Conditional) Windows does not enable [Disk Performance Counters](https://blogs.technet.microsoft.com/askcore/2012/03/16/windows-performance-monitor-disk-counters-explained/)
         by default. If you have not enabled Disk Performance
         Counters for the MongoDB host, click Enable
         Disk Performance Counters. The MongoDB Agent
         uses these counters for some of its hardware monitoring
         activities.

      #. Click Install.

      #. Click Finish once setup is complete.

  - id: unattended
    name: Unattended
    content: |

      After the `MSI` downloads, you can run an unattended
      install. You run an unattended install from the command line
      in either the command interpreter or PowerShell. To learn
      more about unattended installs, see Microsoft's
      documentation on [Standard Installer Command-Line Options](https://docs.microsoft.com/en-us/windows/desktop/msi/standard-installer-command-line-options)

      To run the `MSI` installer unattended from the command
      line, you invoke `msiexec.exe` with the `/q` and `/i`
      flags and a combination of required and optional
      parameters:

      | Parameter | Necessity | Value |
      |---|---|---|
      | `MMSAPIKEY` | Required | Agent API (Application Programming Interface) key of your Ops Manager project. |
      | `MMSBASEURL` | Required | URL (Uniform Resource Locator) of the Ops Manager host. |
      | `MMSGROUPID` | Required | Unique Identifier of your Ops Manager project. |
      | `CONFIGLOGDIR` | Optional | Absolute file path to which Ops Manager should write the MongoDB Agent configuration file. |
      | `LOGFILE` | Optional | Absolute file path to which Ops Manager should write the MongoDB Agent log |
      | `MMSCONFIGBACKUP` | Optional | Absolute file path to the Ops Manager automation configuration backup JSON (Javascript Object Notation) file. |

      **Example:**

      To install the MongoDB Agent unattended, you would
      invoke `msiexec.exe` with the following options:

      ```powershell
      msiexec.exe /q /i "C:\PATH\TO\mongodb-mms-automation-agent-<VERSION>.windows_x86_64.msi" MMSGROUPID=<GROUP.ID> MMSAPIKEY=<AGENT.API.ID> MMSBASEURL="<http://opsmanager.example.com:8080>" LOGFILE="C:\MMSData\Server\Log\automation-agent.log" MMSCONFIGBACKUP="C:\MMSData\MongoDB\mms-cluster-config-backup.json"
      ```

**Step 5: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 6: (Optional) Change the location of the MongoDB Agent binaries and configuration backup files.**

By default, the MongoDB binaries and Ops Manager configuration backup
file are located in `%SystemDrive%\MMSMongoDB\versions`.

**Note:**

Windows sets the `%SystemDrive%` environment variable to the
drive on which you installed Windows. By default, you would be
directed to install Windows on the `C:` drive. To find your
`%SystemDrive%`, issue with following command from `PowerShell
<https://msdn.microsoft.com /en-us/powershell/>`__:

```ps1
get-childitem env:SystemDrive
```

If you want to store these files in a different directory, follow
these procedures:

**To change the location of the MongoDB Agent Binaries**

a. Click Deployment, then Agents, and then
   Downloads & Settings.

#. Below the Download Directory heading, click
   `edit` to the right of the path shown in
   Download Directory (Windows).

#. Change the path to the new path you want.

#. Click Save.

#. Create the new directory you specified on each host that runs
   an MongoDB Agent. Use Windows Explorer to move the file or
   issue the following command from a Command Prompt or
   [PowerShell](https://msdn.microsoft.com/en-us/powershell/):

   ```ps1
   md \<newPath>
   ```

   **Important:**

   Make sure the system user that runs the MongoDB Agent can write
   to this new directory. This is usually the `SYSTEM` user,
   which requires no additional configuration unless you changed
   the user.

**To change the location of the MongoDB Agent configuration backup**

a. Open the MongoDB Agent configuration file in your preferred text
   editor.

#. Change the `mmsConfigBackup` setting to the new path
   for the configuration backup file. Replace `X` with the drive
   letter on which your backup is stored.

   ```ini
   mmsConfigBackup=X:\<newPath>\mms-cluster-config-backup.json
   ```

#. Save the MongoDB Agent configuration file.

#. Move the configuration backup file to the new directory. Use
   Windows Explorer to move the file or issue the following
   command from a Command Prompt or [PowerShell](https://msdn.microsoft.com/en-us/powershell/):

   ```ps1
   move %SystemDrive%\MMSMongoDB\versions\mms-cluster-config-backup.json \<newPath>
   ```

**Step 7: Repeat the installation procedure for each MongoDB host.**

**debian:**

Use this procedure to install the MongoDB Agent:

**x86:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

On x86_64 architecture running Debian 9/10/11 or Ubuntu 18.04/20.04/22.04:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click Debian 9, Ubuntu 16.X/18.X - DEB.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click Debian 9, Ubuntu 16.X/18.X - DEB.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forUbuntu 18.04/20.04/22.04 or Debian 9/10/11 for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager_latest_amd64.ubuntu1604.deb
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor:

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the automation-agent.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 5: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor.

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 6: Prepare the data directory.**

The data directory stores MongoDB data. For an existing MongoDB
deployment, ensure that the directory is owned by the `mongodb`
user. If no MongoDB deployment exists, create the directory and set
the owner.

To create a data directory and set the owner as the `mongodb` user:

```sh
sudo mkdir -p /data; sudo chown mongodb:mongodb /data
```

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

**Step 8: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 9: Repeat the installation procedure for each MongoDB host.**

**rhel:**

Use this procedure to install the MongoDB Agent:

**x86:**

On x86_64 architecture:

**v6:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

Running Amazon Linux using an `rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click Amazon Linux - RPM.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click Amazon Linux - RPM.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.x86_64.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor:

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the automation-agent.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 5: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor.

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 6: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 9: Repeat the installation procedure for each MongoDB host.**

**v7:**

Running RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or 
8.x), SUSE12, SUSE15, or Amazon Linux 2:

**rpm:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

Using an `rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL/CentOS (7.X), SUSE12, Amazon Linux2 - RPM.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL/CentOS (7.X), SUSE12, Amazon Linux2 - RPM.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 7 for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.x86_64.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor:

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the automation-agent.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 5: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor.

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 6: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 9: Repeat the installation procedure for each MongoDB host.**

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL/CentOS (7.X), SUSE12, Amazon Linux 2 - TAR.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL/CentOS (7.X), SUSE12, Amazon Linux 2 - TAR.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-latest.rhel7_x86_64.tar.gz
```

**Note:**

The example commands use the installer for Amazon Linux 2 for
ARM64. The command is similar for the RHEL (8.x or 9.x) installer.
Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.rhel7_x86_64.tar.gz
```

**Step 5: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.rhel7_x86_64
```

**Step 6: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor:

```sh
vi <install-path>/local.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the local.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 7: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor.

```sh
vi <install-path>/local.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 8: Create the binary, log, and data directories.**

Create the following directories to store files that the
MongoDB Agent needs.

**Note:**

The use of `mongodb-mms-automation` in the file path is a
legacy artifact and does not mean that the MongoDB Agent is being
installed with Automation configured.

| Component | Default Directory | Description |
|---|---|---|
| Binaries | `/var/lib/mongodb-mms-automation` | These are the binaries that the MongoDB Agent manages. They include the MongoDB Agent, BI Connector, and MongoDB binaries. |
| MongoDB Agent logs | `/var/log/mongodb-mms-automation` | These are the log files that the MongoDB Agent creates. |
| MongoDB databases | `/data` | These are the databases that the MongoDB Agent creates and manages. |

Run the following commands to create the directories:

```sh
sudo mkdir -m 755 -p /var/lib/mongodb-mms-automation
sudo mkdir -m 755 -p /var/log/mongodb-mms-automation
sudo mkdir -m 755 -p /data
```

By default, the Agent binaries and Ops Manager
configuration backup file are located in 
`/var/lib/mongodb-mms-automation`. 
If you want to store these files in a different
directory, follow these procedures:

**To change the location of the Agent Binaries:**

a. Click Deployment, then Agents, and
   then Downloads & Settings.

b. Below the Download Directory heading, click the
   pencil icon to the right of the path shown in
   Download Directory (Linux).

c. Change the path to the new path you want.

d. Click Save.

e. Create the new directory you specified on each host that runs
   an Agent.

   ```sh
   sudo mkdir -m 755 -p /<newPath>
   ```

**To change the location of the Agent configuration backup:**

a. Open the
   Agent configuration file
   in your preferred text editor.

b. Change the `mmsConfigBackup` setting to the new path for
   the configuration backup file.

   ```ini
   mmsConfigBackup=/<newPath>/mms-cluster-config-backup.json
   ```

c. Save the Agent configuration file.

d. Move the configuration backup file to the new directory.

   ```sh
   sudo mv /var/lib/mongodb-mms-automation/mms-cluster-config-backup.json /<newPath>
   ```

**Step 9: Assign permissions to the system user that runs the MongoDB Agent.**

Run the following commands:

```sh
# Create mongod user and group if they do not exist

if ! sudo /usr/bin/id -g mongod &>/dev/null; then
  sudo /usr/sbin/groupadd -r mongod
fi

# Create mongod user if they do not exist and assign
# them to the mongod group

if ! sudo /usr/bin/id mongod &>/dev/null; then
  sudo /usr/sbin/useradd -M -r -g mongod \
    -d /var/lib/mongo -s /bin/false \
    -c mongod mongod > /dev/null 2>&1
fi

# Grant the mongod:mongod user and group permissions
# to manage deployments.

sudo chown mongod:mongod /var/lib/mongod-mms-automation
sudo chown mongod:mongod /var/log/mongod-mms-automation
sudo chown mongod:mongod /data
```

**Step 10: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**ppc:**

On RHEL / CentOS (7.x) on PowerPC architecture
(managing MongoDB 3.4 or later deployments):

**rpm:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

Using an `rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL/CentOS (7.X) Power (ppc64le) - RPM.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL/CentOS (7.X) Power (ppc64le) - RPM.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 7 for PowerPC:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.ppc64le.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor:

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the automation-agent.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 5: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor.

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 6: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 9: Repeat the installation procedure for each MongoDB host.**

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL/CentOS (7.X) Power (ppc64le) - TAR.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL/CentOS (7.X) Power (ppc64le) - TAR.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 7 for PowerPC:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-latest.rhel7_ppc64le.tar.gz
```

**Note:**

The example commands use the installer for Amazon Linux 2 for
ARM64. The command is similar for the RHEL (8.x or 9.x) installer.
Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.rhel7_ppc64le.tar.gz
```

**Step 5: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.rhel7_ppc64le
```

**Step 6: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor:

```sh
vi <install-path>/local.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the local.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 7: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor.

```sh
vi <install-path>/local.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 8: Create the binary, log, and data directories.**

Create the following directories to store files that the
MongoDB Agent needs.

**Note:**

The use of `mongodb-mms-automation` in the file path is a
legacy artifact and does not mean that the MongoDB Agent is being
installed with Automation configured.

| Component | Default Directory | Description |
|---|---|---|
| Binaries | `/var/lib/mongodb-mms-automation` | These are the binaries that the MongoDB Agent manages. They include the MongoDB Agent, BI Connector, and MongoDB binaries. |
| MongoDB Agent logs | `/var/log/mongodb-mms-automation` | These are the log files that the MongoDB Agent creates. |
| MongoDB databases | `/data` | These are the databases that the MongoDB Agent creates and manages. |

Run the following commands to create the directories:

```sh
sudo mkdir -m 755 -p /var/lib/mongodb-mms-automation
sudo mkdir -m 755 -p /var/log/mongodb-mms-automation
sudo mkdir -m 755 -p /data
```

By default, the Agent binaries and Ops Manager
configuration backup file are located in 
`/var/lib/mongodb-mms-automation`. 
If you want to store these files in a different
directory, follow these procedures:

**To change the location of the Agent Binaries:**

a. Click Deployment, then Agents, and
   then Downloads & Settings.

b. Below the Download Directory heading, click the
   pencil icon to the right of the path shown in
   Download Directory (Linux).

c. Change the path to the new path you want.

d. Click Save.

e. Create the new directory you specified on each host that runs
   an Agent.

   ```sh
   sudo mkdir -m 755 -p /<newPath>
   ```

**To change the location of the Agent configuration backup:**

a. Open the
   Agent configuration file
   in your preferred text editor.

b. Change the `mmsConfigBackup` setting to the new path for
   the configuration backup file.

   ```ini
   mmsConfigBackup=/<newPath>/mms-cluster-config-backup.json
   ```

c. Save the Agent configuration file.

d. Move the configuration backup file to the new directory.

   ```sh
   sudo mv /var/lib/mongodb-mms-automation/mms-cluster-config-backup.json /<newPath>
   ```

**Step 9: Assign permissions to the system user that runs the MongoDB Agent.**

Run the following commands:

```sh
# Create mongod user and group if they do not exist

if ! sudo /usr/bin/id -g mongod &>/dev/null; then
  sudo /usr/sbin/groupadd -r mongod
fi

# Create mongod user if they do not exist and assign
# them to the mongod group

if ! sudo /usr/bin/id mongod &>/dev/null; then
  sudo /usr/sbin/useradd -M -r -g mongod \
    -d /var/lib/mongo -s /bin/false \
    -c mongod mongod > /dev/null 2>&1
fi

# Grant the mongod:mongod user and group permissions
# to manage deployments.

sudo chown mongod:mongod /var/lib/mongod-mms-automation
sudo chown mongod:mongod /var/log/mongod-mms-automation
sudo chown mongod:mongod /data
```

**Step 10: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**s390x:**

On zSeries architecture (managing MongoDB 4.0 or
later deployments):

Running RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or 8.x) 
using the `rpm` package manager:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL 7.X/8X Z-Series (s390x) - RPM.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL 7.X/8X Z-Series (s390x) - RPM.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 7.X/8.X for IBM zSeries:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.s390x.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor:

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the automation-agent.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 5: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor.

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 6: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 9: Repeat the installation procedure for each MongoDB host.**

**arm64:**

On ARM64 architecture running RHEL (8.x or 9.x) or Amazon 
Linux 2:

**rpm:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

Running RHEL (8.x or 9.x) or Amazon Linux 2 using the 
rpm package manager:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL/CentOS (8.X/9.X), Amazon Linux2, Amazon Linux 2023 - RPM (ARM).

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL/CentOS (8.X/9.X), Amazon Linux2, Amazon Linux 2023 - RPM (ARM).

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL (8.x or 9.x) or Amazon Linux 2 for ARM64:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.aarch64.amzn2.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor:

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the automation-agent.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 5: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the automation-agent.config file in your preferred text editor.

```sh
sudo vi /etc/mongodb-mms/automation-agent.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 6: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 9: Repeat the installation procedure for each MongoDB host.**

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click RHEL/CentOS (8.X/9.X), Amazon Linux 2, Amazon Linux 2023 - TAR (ARM).

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click RHEL/CentOS (8.X/9.X), Amazon Linux 2, Amazon Linux 2023 - TAR (ARM).

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL (8.x or 9.x) or Amazon Linux 2 for ARM64:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-latest.amzn2_aarch64.tar.gz
```

**Note:**

The example commands use the installer for Amazon Linux 2 for
ARM64. The command is similar for the RHEL (8.x or 9.x) installer.
Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.amzn2_aarch64.tar.gz
```

**Step 5: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.amzn2_aarch64
```

**Step 6: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor:

```sh
vi <install-path>/local.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the local.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 7: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor.

```sh
vi <install-path>/local.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 8: Create the binary, log, and data directories.**

Create the following directories to store files that the
MongoDB Agent needs.

**Note:**

The use of `mongodb-mms-automation` in the file path is a
legacy artifact and does not mean that the MongoDB Agent is being
installed with Automation configured.

| Component | Default Directory | Description |
|---|---|---|
| Binaries | `/var/lib/mongodb-mms-automation` | These are the binaries that the MongoDB Agent manages. They include the MongoDB Agent, BI Connector, and MongoDB binaries. |
| MongoDB Agent logs | `/var/log/mongodb-mms-automation` | These are the log files that the MongoDB Agent creates. |
| MongoDB databases | `/data` | These are the databases that the MongoDB Agent creates and manages. |

Run the following commands to create the directories:

```sh
sudo mkdir -m 755 -p /var/lib/mongodb-mms-automation
sudo mkdir -m 755 -p /var/log/mongodb-mms-automation
sudo mkdir -m 755 -p /data
```

By default, the Agent binaries and Ops Manager
configuration backup file are located in 
`/var/lib/mongodb-mms-automation`. 
If you want to store these files in a different
directory, follow these procedures:

**To change the location of the Agent Binaries:**

a. Click Deployment, then Agents, and
   then Downloads & Settings.

b. Below the Download Directory heading, click the
   pencil icon to the right of the path shown in
   Download Directory (Linux).

c. Change the path to the new path you want.

d. Click Save.

e. Create the new directory you specified on each host that runs
   an Agent.

   ```sh
   sudo mkdir -m 755 -p /<newPath>
   ```

**To change the location of the Agent configuration backup:**

a. Open the
   Agent configuration file
   in your preferred text editor.

b. Change the `mmsConfigBackup` setting to the new path for
   the configuration backup file.

   ```ini
   mmsConfigBackup=/<newPath>/mms-cluster-config-backup.json
   ```

c. Save the Agent configuration file.

d. Move the configuration backup file to the new directory.

   ```sh
   sudo mv /var/lib/mongodb-mms-automation/mms-cluster-config-backup.json /<newPath>
   ```

**Step 9: Assign permissions to the system user that runs the MongoDB Agent.**

Run the following commands:

```sh
# Create mongod user and group if they do not exist

if ! sudo /usr/bin/id -g mongod &>/dev/null; then
  sudo /usr/sbin/groupadd -r mongod
fi

# Create mongod user if they do not exist and assign
# them to the mongod group

if ! sudo /usr/bin/id mongod &>/dev/null; then
  sudo /usr/sbin/useradd -M -r -g mongod \
    -d /var/lib/mongo -s /bin/false \
    -c mongod mongod > /dev/null 2>&1
fi

# Grant the mongod:mongod user and group permissions
# to manage deployments.

sudo chown mongod:mongod /var/lib/mongod-mms-automation
sudo chown mongod:mongod /var/log/mongod-mms-automation
sudo chown mongod:mongod /data
```

**Step 10: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**linux:**

Use this procedure to install Linux systems that do not use
`deb` or `rpm` packages.

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Begin or Manage a Deployment.**

Your project has no deployments and you see a prompt to get
started.

To create a new deployment:

a. From the Build New Deployment menu, select the type of 
   deployment you wish to add:

   - New Sharded Cluster
   - New Replica Set
   - New Standalone

b. If, on the Create New Deployment
   page, Ops Manager cannot detect any hosts with the
   MongoDB Agent installed, you see a banner
   displayed at the top of the
   Create New Deployment page.

   Click the see instructions link.

c. From the Select Your Server's
   Operating System menu, click Other Linux - TAR.

d. Click Next.

To manage an existing deployment:

a. Click Manage your existing deployment.

b. From the Install Agent menu, click Other Linux - TAR.

**Step 3: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for Generic 64-bit Linux:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-latest.linux_x86_64.tar.gz
```

**Note:**

The example commands use the installer for Amazon Linux 2 for
ARM64. The command is similar for the RHEL (8.x or 9.x) installer.
Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 4: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.linux_x86_64.tar.gz
```

**Step 5: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.linux_x86_64
```

**Step 6: Edit the MongoDB Agent configuration file.**

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor:

```sh
vi <install-path>/local.config
```

Update the following configuration options:

| Key | Value |
|---|---|
| `mmsGroupId` | `ProjectID` of your project. |
| `mmsApiKey` | `Agent API key` of your project. |
| mmsbaseurl | URL (Uniform Resource Locator) (hostname and port) of the Ops Manager Application. |

The resulting changes to the local.config file should
look like the following:

```ini
mmsGroupId=<Project ID>
mmsApiKey=<agent API key>
mmsBaseUrl=<application URL>
```

**Step 7: Configure the MongoDB Agent to use a proxy server.**

To configure the MongoDB Agent to connect to Ops Manager via a proxy
server, you must specify the server in the `httpProxy`
environment variable.

In the directory where you installed the MongoDB Agent, open the local.config file in your preferred text editor.

```sh
vi <install-path>/local.config
```

Add the following configuration key:

| Key | Value |
|---|---|
| `httpProxy` | URL (Uniform Resource Locator) (hostname and port) of to your proxy server. |

**Step 8: Create the binary, log, and data directories.**

Create the following directories to store files that the
MongoDB Agent needs.

**Note:**

The use of `mongodb-mms-automation` in the file path is a
legacy artifact and does not mean that the MongoDB Agent is being
installed with Automation configured.

| Component | Default Directory | Description |
|---|---|---|
| Binaries | `/var/lib/mongodb-mms-automation` | These are the binaries that the MongoDB Agent manages. They include the MongoDB Agent, BI Connector, and MongoDB binaries. |
| MongoDB Agent logs | `/var/log/mongodb-mms-automation` | These are the log files that the MongoDB Agent creates. |
| MongoDB databases | `/data` | These are the databases that the MongoDB Agent creates and manages. |

Run the following commands to create the directories:

```sh
sudo mkdir -m 755 -p /var/lib/mongodb-mms-automation
sudo mkdir -m 755 -p /var/log/mongodb-mms-automation
sudo mkdir -m 755 -p /data
```

By default, the Agent binaries and Ops Manager
configuration backup file are located in 
`/var/lib/mongodb-mms-automation`. 
If you want to store these files in a different
directory, follow these procedures:

**To change the location of the Agent Binaries:**

a. Click Deployment, then Agents, and
   then Downloads & Settings.

b. Below the Download Directory heading, click the
   pencil icon to the right of the path shown in
   Download Directory (Linux).

c. Change the path to the new path you want.

d. Click Save.

e. Create the new directory you specified on each host that runs
   an Agent.

   ```sh
   sudo mkdir -m 755 -p /<newPath>
   ```

**To change the location of the Agent configuration backup:**

a. Open the
   Agent configuration file
   in your preferred text editor.

b. Change the `mmsConfigBackup` setting to the new path for
   the configuration backup file.

   ```ini
   mmsConfigBackup=/<newPath>/mms-cluster-config-backup.json
   ```

c. Save the Agent configuration file.

d. Move the configuration backup file to the new directory.

   ```sh
   sudo mv /var/lib/mongodb-mms-automation/mms-cluster-config-backup.json /<newPath>
   ```

**Step 9: Assign permissions to the system user that runs the MongoDB Agent.**

Run the following commands:

```sh
# Create mongodb user and group if they do not exist

if ! sudo /usr/bin/id -g mongodb &>/dev/null; then
  sudo /usr/sbin/groupadd -r mongodb
fi

# Create mongodb user if they do not exist and assign
# them to the mongodb group

if ! sudo /usr/bin/id mongodb &>/dev/null; then
  sudo /usr/sbin/useradd -M -r -g mongodb \
    -d /var/lib/mongo -s /bin/false \
    -c mongodb mongodb > /dev/null 2>&1
fi

# Grant the mongodb:mongodb user and group permissions
# to manage deployments.

sudo chown mongodb:mongodb /var/lib/mongodb-mms-automation
sudo chown mongodb:mongodb /var/log/mongodb-mms-automation
sudo chown mongodb:mongodb /data
```

**Step 10: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal:

a. Click Verify Agent to make
   sure the MongoDB Agent can connect to Ops Manager.

b. Click Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**
