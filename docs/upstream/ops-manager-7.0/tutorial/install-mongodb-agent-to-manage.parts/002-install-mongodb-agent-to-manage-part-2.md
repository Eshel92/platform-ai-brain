<!-- Part 2 of 2 of tutorial/install-mongodb-agent-to-manage.md (split because the page is big). -->

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
