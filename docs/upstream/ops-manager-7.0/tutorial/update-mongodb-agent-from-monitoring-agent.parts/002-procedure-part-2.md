<!-- Part 2 of 3 of tutorial/update-mongodb-agent-from-monitoring-agent.md (split because the page is big). -->

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
