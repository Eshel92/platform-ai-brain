<!-- Converted from tutorial/update-mongodb-agent-from-monitoring-agent.txt (reStructuredText). Includes are inlined. -->

# Update from the legacy Monitoring Agent

You have a project with monitored MongoDB deployments that Automation
does not manage and want to update to the MongoDB Agent.

**Note:** Review the Prerequisites First

If you want to start or continue using Automation to manage your
MongoDB deployments, please review the
/tutorial/install-mongodb-agent-prereq before updating to the
MongoDB Agent.

## Procedure

**windows:**

Use this procedure to update to the MongoDB Agent on x86_64
architecture running Microsoft Windows:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Download the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Windows - MSI.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Install the MongoDB Agent.**

The MongoDB Agent Installation Instructions box
displays the following information:

- Base URL

  *Required for binding to a project.*

- Project ID
  (Required for binding to a project)

- API Key

  If you do not have an API Key, click plus
  Generate Key.

**Warning:**

Some or all of these values are required in a later step. Copy
these values then store them where you can access them later.

**Step 6: Run the MongoDB Agent Windows Installer.**

tabs:
  - id: interactive
    name: Interactive
    content: |

      a. After the `MSI` downloads, double-click:

         `mongodb-mms-automation-agent-<VERSION>.windows_x86_64.msi`

         **Note:**

         The use of `mongodb-mms-automation` in the
         filename is a legacy artifact and does not mean
         that the MongoDB Agent is being installed with
         Automation configured.

      #. If a security warning appears, click Run.

      #. At the Configuration/Log Folder step

         Provide the directory into which these files are saved.

      #. At the Key Type step, select Agent
         API Key to bind to a specific `project`.

      #. Enter the appropriate Agent keys.

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
         installing the MongoDB Agent, disable it now.
         Stealth Mode significantly degrades the performance
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
      in either the Command Prompt or PowerShell. To learn
      more about unattended installs, see Microsoft's
      documentation on [Standard Installer Command-Line Options](https://docs.microsoft.com/en-us/windows/desktop/msi/standard-installer-command-line-options)

      To run the `MSI` installer unattended from the command
      line, invoke `msiexec.exe` with the `/q` and `/i`
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

      To install the MongoDB Agent unattended,
      invoke `msiexec.exe` with the following options:

      ```powershell
      msiexec.exe /q /i "C:\PATH\TO\mongodb-mms-automation-agent-<VERSION>.windows_x86_64.msi" MMSGROUPID=<GROUP.ID> MMSAPIKEY=<AGENT.API.ID> MMSBASEURL="<http://opsmanager.example.com:8080>" LOGFILE="C:\MMSData\Server\Log\automation-agent.log" MMSCONFIGBACKUP="C:\MMSData\MongoDB\mms-cluster-config-backup.json"
      ```

**Step 7: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 8: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 9: (Optional) Change the location of the MongoDB Agent binaries and configuration backup files.**

Your system policies or practices may require the MongoDB binaries
and Ops Manager configuration backup file to be located somewhere other
than the default location of `%SystemDrive%\MMSMongoDB\versions`.

**Note:**

Windows sets the `%SystemDrive%` environment variable to the
drive on which you installed Windows. By default, you are
directed to install Windows on the `C:` drive. To find your
`%SystemDrive%`, issue with following command from [PowerShell](https://msdn.microsoft.com/en-us/powershell/):

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

   Make sure that the system user that runs the MongoDB Agent can write
   to this new directory. This is usually the `SYSTEM` user,
   which requires no additional configuration unless you changed
   the user.

**To change the location of the MongoDB Agent configuration backup**

a. Open the MongoDB Agent configuration file in your preferred text
   editor.

#. Change the `mmsConfigBackup` setting to the new path
   for the configuration backup file. Replace `X` in the following example with the drive
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

**Step 10: Repeat the installation procedure for each MongoDB host.**

**debian:**

Use this procedure to update to the MongoDB Agent:

**x86:**

On x86_64 architecture running Debian 9, Ubuntu 18.04,
Ubuntu 20.04, or Ubuntu 22.04:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Debian 9, Ubuntu 16.X/18.X - DEB.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for Ubuntu 18.04/20.04/22.04 or Debian 9/10/11 for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.amd64.ubuntu1604.deb
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Edit the MongoDB Agent configuration file.**

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

**Step 7: Configure the MongoDB Agent to use a proxy server.**

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

**Step 8: Prepare the data directory.**

The data directory stores MongoDB data. For an existing MongoDB
deployment, ensure that the directory is owned by the `mongodb`
user. If no MongoDB deployment exists, create the directory and set
the owner.

To create a data directory and set the owner as the `mongodb` user:

```sh
sudo mkdir -p /data; sudo chown mongodb:mongodb /data
```

**Step 9: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

**Step 10: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**s390x:**

On zSeries architecture running Ubuntu 18.x using a
`deb` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Ubuntu 18.X Z-Series (s390x) - DEB.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for Ubuntu 18.04 for IBM zSeries:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.s390x.ubuntu1804.deb
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Edit the MongoDB Agent configuration file.**

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

**Step 7: Configure the MongoDB Agent to use a proxy server.**

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

**Step 8: Prepare the data directory.**

The data directory stores MongoDB data. For an existing MongoDB
deployment, ensure that the directory is owned by the `mongodb`
user. If no MongoDB deployment exists, create the directory and set
the owner.

To create a data directory and set the owner as the `mongodb` user:

```sh
sudo mkdir -p /data; sudo chown mongodb:mongodb /data
```

**Step 9: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

**Step 10: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**rhel:**

Use this procedure to update to the MongoDB Agent:

**x86:**

On x86_64 architecture:

**v6:**

Running RHEL / CentOS 6.x using an `rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Amazon Linux - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 6 for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.x86_64.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Edit the MongoDB Agent configuration file.**

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

**Step 7: Configure the MongoDB Agent to use a proxy server.**

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

**Step 8: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 9: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 10: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**v7:**

Running RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or
8.x), SUSE12, SUSE15, or Amazon Linux 2:

**rpm:**

Using an `rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X), SUSE12, Amazon Linux2 - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

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

**Step 6: Edit the MongoDB Agent configuration file.**

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

**Step 7: Configure the MongoDB Agent to use a proxy server.**

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

**Step 8: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 9: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 10: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X), SUSE12, Amazon Linux 2 - TAR.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.rhel7_x86_64.tar.gz
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.rhel7_x86_64.tar.gz
```

**Step 7: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.rhel7_x86_64
```

**Step 8: Edit the MongoDB Agent configuration file.**

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

**Step 9: Configure the MongoDB Agent to use a proxy server.**

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

**Step 10: Create the binary, log, and data directories.**

If you have an existing Monitoring Agent user and do not plan on
activating Automation, you only need to create the log directory.

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

**Step 11: Assign permissions to the system user that runs the MongoDB Agent.**

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

**Step 12: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 13: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 14: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 15: Repeat the installation procedure for each MongoDB host.**

**ppc:**

On RHEL / CentOS (7.x) on PowerPC architecture
(managing MongoDB 3.4 or later deployments):

**rpm:**

Using an `rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X), SUSE12, Amazon Linux2 - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 7 for PowerPC:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.ppc641e.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Edit the MongoDB Agent configuration file.**

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

**Step 7: Configure the MongoDB Agent to use a proxy server.**

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

**Step 8: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 9: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 10: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X) Power (ppc64le) - TAR.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for RHEL 7 for PowerPC:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.rhel7_ppc64le.tar.gz
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.rhel7_ppc64le.tar.gz
```

**Step 7: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.rhel7_ppc64le
```

**Step 8: Edit the MongoDB Agent configuration file.**

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

**Step 9: Configure the MongoDB Agent to use a proxy server.**

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

**Step 10: Create the binary, log, and data directories.**

If you have an existing Monitoring Agent user and do not plan on
activating Automation, you only need to create the log directory.

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

**Step 11: Assign permissions to the system user that runs the MongoDB Agent.**

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

**Step 12: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 13: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 14: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 15: Repeat the installation procedure for each MongoDB host.**

**s390x:**

On zSeries architecture (managing MongoDB 4.0 or
later deployments):

Running RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or 8.x) 
using the `rpm` package manager:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL 7.X/8X Z-Series (s390x) - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

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

**Step 6: Edit the MongoDB Agent configuration file.**

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

**Step 7: Configure the MongoDB Agent to use a proxy server.**

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

**Step 8: Prepare the data directory.**

The data directory stores MongoDB data and must be owned by the
`mongod` user. For an existing MongoDB deployment, ensure the
directory has the `mongod` user as owner. If no MongoDB deployment
exists, create the directory and set the owner.

The following commands create a data directory and set the owner as
the `mongod` user:

```sh
sudo mkdir /data; sudo chown mongod:mongod /data
```

**Step 9: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 10: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 11: Finish the installation of the MongoDB Agent.**

In the Install Agent Instructions modal, click
Done.

**Step 12: Repeat the installation procedure for each MongoDB host.**

**linux:**

Use this procedure to install update to the MongoDB Agent on
Linux systems that do not use `deb` or `rpm` packages.

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Add any existing configuration options for your legacy Monitoring Agent.**

If Automation did not manage your Monitoring Agent, you can add any
Monitoring settings you had before at the Add Custom
Configuration Options for your MongoDB Agent (Optional) step.

To add options that you had for your
Monitoring Agent, under the
Monitoring Configurations section:

a. Type the desired
   setting in the
   Setting box and the corresponding value in the
   Value box.

#. To add more than one Setting, click the
   + Add Setting link. Another row appears.

#. Repeat until all settings have been added.

#. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 4: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Other Linux - TAR.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 5: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the 
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for Generic 64-bit Linux:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.linux_x86_64.tar.gz
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 6: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.linux_x86_64.tar.gz
```

**Step 7: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.linux_x86_64
```

**Step 8: Edit the MongoDB Agent configuration file.**

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

**Step 9: Configure the MongoDB Agent to use a proxy server.**

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

**Step 10: Create the binary, log, and data directories.**

If you have an existing Monitoring Agent user and do not plan on
activating Automation, you only need to create the log directory.

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

**Step 11: Assign permissions to the system user that runs the MongoDB Agent.**

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

**Step 12: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 13: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

Click Next.

**Step 14: Finish the installation of the MongoDB Agent.**

At the Final Steps modal, the legacy Backup and
Monitoring Agents are put into standby mode. Click
Finish.

**Step 15: Repeat the installation procedure for each MongoDB host.**

## Next Steps

After the MongoDB Agent update completes:

- If Automation did not previously manage your Monitoring Agent,
  activate Backup and/or
  Monitoring on your MongoDB deployment.

- If Automation did previously manage your Monitoring
  Agent, it is now activated. To verify that Automation
  is activated, click Deployment arrow-right
  Servers.

- If you want to activate Automation,
  add a deployment to your MongoDB
  project.

- Stop and
  remove the legacy
  Monitoring Agent.

- Stop and
  remove the legacy Backup
  Agent.
