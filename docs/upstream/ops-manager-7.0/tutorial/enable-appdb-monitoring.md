<!-- Converted from tutorial/enable-appdb-monitoring.txt (reStructuredText). Includes are inlined. -->

# Enable Application Database Monitoring

## Prerequisites

To enable application database monitoring, including `dbStats`
and database profiling
information, the database account connecting to AppDB must authenticate as a
user with the following minimum role:

| Required Role | Database |
|---|---|
| `clusterMonitor` | `admin` |

**debian:**

Use this procedure to enable monitoring on an application
database:

**x86:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

On x86_64 architecture running Debian 10 or 11, and
Ubuntu 18.04, 20.04, or 22.04:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Debian 9, Ubuntu 16.X/18.X - DEB.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forUbuntu 18.04/20.04/22.04 or Debian 9/10/11 for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.amd64.ubuntu1604.deb
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Edit the MongoDB Agent configuration file.**

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

**Step 6: Configure the MongoDB Agent to use a proxy server.**

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

**Step 7: Prepare the data directory.**

The data directory stores MongoDB data. For an existing MongoDB
deployment, ensure that the directory is owned by the `mongodb`
user. If no MongoDB deployment exists, create the directory and set
the owner.

To create a data directory and set the owner as the `mongodb` user:

```sh
sudo mkdir -p /data; sudo chown mongodb:mongodb /data
```

**Step 8: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

**Step 9: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 10: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 11: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 12: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 13: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 14: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 15: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**s390x:**

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

On zSeries architecture running Ubuntu 18.04 using a `deb`
package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Ubuntu 18.X Z-Series (s390x) - DEB.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forUbuntu 18.04 for IBM zSeries:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.s390x.ubuntu1804.deb
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Edit the MongoDB Agent configuration file.**

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

**Step 6: Configure the MongoDB Agent to use a proxy server.**

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

**Step 7: Prepare the data directory.**

The data directory stores MongoDB data. For an existing MongoDB
deployment, ensure that the directory is owned by the `mongodb`
user. If no MongoDB deployment exists, create the directory and set
the owner.

To create a data directory and set the owner as the `mongodb` user:

```sh
sudo mkdir -p /data; sudo chown mongodb:mongodb /data
```

**Step 8: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

**Step 9: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 10: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 11: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 12: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 13: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 14: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 15: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**rhel:**

Use this procedure to enable monitoring on an application
database:

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

Running RHEL / CentOS 6.x using an
`rpm` package:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Amazon Linux - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer for64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.x86_64.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Edit the MongoDB Agent configuration file.**

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

**Step 6: Configure the MongoDB Agent to use a proxy server.**

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

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 9: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 10: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 11: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 12: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 13: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 14: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**v7:**

RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or 8.x), 
SUSE12, SUSE15, or Amazon Linux 2:

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

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X), SUSE12, Amazon Linux2 - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forRHEL 7 for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.x86_64.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Edit the MongoDB Agent configuration file.**

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

**Step 6: Configure the MongoDB Agent to use a proxy server.**

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

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 9: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 10: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 11: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 12: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 13: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 14: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X), SUSE12, Amazon Linux 2 - TAR.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forRHEL for 64-bit x86:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.rhel7_x86_64.tar.gz
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.rhel7_x86_64.tar.gz
```

**Step 6: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.rhel7_x86_64
```

**Step 7: Edit the MongoDB Agent configuration file.**

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

**Step 8: Configure the MongoDB Agent to use a proxy server.**

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

**Step 9: Create the binary, log, and data directories.**

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

**Step 10: Assign permissions to the system user that runs the MongoDB Agent.**

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

**Step 11: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 12: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 13: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 14: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 15: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 16: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 17: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 18: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**ppc:**

On RHEL / CentOS (7.x) on PowerPC architecture (managing
MongoDB 3.4 or later deployments):

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

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X), SUSE12, Amazon Linux2 - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forRHEL 7 for PowerPC:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.ppc641e.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Edit the MongoDB Agent configuration file.**

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

**Step 6: Configure the MongoDB Agent to use a proxy server.**

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

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 9: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 10: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 11: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 12: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 13: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 14: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**tar:**

Using a `tar` archive:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL/CentOS (7.X) Power (ppc64le) - TAR.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forRHEL 7 for PowerPC:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.rhel7_ppc64le.tar.gz
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.rhel7_ppc64le.tar.gz
```

**Step 6: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.rhel7_ppc64le
```

**Step 7: Edit the MongoDB Agent configuration file.**

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

**Step 8: Configure the MongoDB Agent to use a proxy server.**

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

**Step 9: Create the binary, log, and data directories.**

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

**Step 10: Assign permissions to the system user that runs the MongoDB Agent.**

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

**Step 11: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 12: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 13: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 14: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 15: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 16: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 17: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 18: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**s390x:**

On zSeries architecture (managing MongoDB 4.4 or later
deployments), use RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or 
8.x):

**Important:**

Starting with version 11.0.5.6967-1, when you install the MongoDB Agent 
using `deb` or `rpm` packages, the package doesn't add
MongoDB binaries to the `PATH` environment variable.

If your deployment depends on the presence of MongoDB binaries in 
the `PATH`, you must manually add the paths to MongoDB
binaries to the `PATH`. To learn how to update environment
variables, refer to your operating system's documentation.

Running RHEL (7.x, 8.x, or 9.x) or CentOS (7.x or 8.x) 
using the `rpm` package manager:

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select RHEL 7.X/8X Z-Series (s390x) - RPM.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forRHEL 7.X/8.X for IBM zSeries:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.s390x.rhel<version>.rpm
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Edit the MongoDB Agent configuration file.**

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

**Step 6: Configure the MongoDB Agent to use a proxy server.**

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

**Step 7: Start the MongoDB Agent.**

Issue the following command:

```sh
sudo service mongodb-mms-automation-agent start
```

**Step 8: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 9: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 10: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 11: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 12: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 13: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 14: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**linux:**

Use this procedure to install enable monitoring on an application
database on Linux systems that do not use `deb` or `rpm`
packages.

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Enable Application Database Monitoring.**

To enable application database monitoring:

a. Click the Admin link in the upper-right corner of the
   Ops Manager console.

b. Click Enable from either:

   i.  The banner introducing the monitoring capability or
   ii. The `Enable Monitoring` setting.

**Step 3: Install the MongoDB Agent.**

a. Click View Agent Install Instructions. The
   Install Agent Instructions modal opens.
b. From the Select Your Server's Operating System menu,
   select Other Linux - TAR.
c. Click Next. The
   Install New MongoDB Agent modal opens.

**Step 4: Download the latest version of the MongoDB Agent.**

Starting with this step, follow the MongoDB Agent
installation modal and copy the commands provided into the
Linux shell.

From a system shell on the host that will run the MongoDB Agent,
issue the following `curl` command to download the installer forGeneric 64-bit Linux:

```shell
curl -OL https://<OpsManagerHost>:<Port>/download/agent/automation/mongodb-mms-automation-agent-manager-latest.linux_x86_64.tar.gz
```

**Note:**

Replace `<OpsManagerHost>:<Port>` with the hostname and port of
your Ops Manager Application. If present, replace `<version>` with the 
major version of the operating system. For example, replace 
`<version>` with `7` for RHEL 7.x.

**Step 5: Extract the MongoDB Agent.**

You can install the MongoDB Agent in any directory. If you want
to move the archive to another directory before extracting, you may
do so.

To install the MongoDB Agent, extract the archive:

```sh
tar -xvzf mongodb-mms-automation-agent-<VERSION>.linux_x86_64.tar.gz
```

**Step 6: Change to the extracted binary directory.**

Change into the directory that was created after extracting the
MongoDB Agent binary:

```sh
cd mongodb-mms-automation-agent-<VERSION>.linux_x86_64
```

**Step 7: Edit the MongoDB Agent configuration file.**

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

**Step 8: Configure the MongoDB Agent to use a proxy server.**

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

**Step 9: Create the binary, log, and data directories.**

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

**Step 10: Assign permissions to the system user that runs the MongoDB Agent.**

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

**Step 11: Start the MongoDB Agent.**

From the directory in which you installed the MongoDB Agent and
as the system user you created in the last step, issue the following
command:

```sh
nohup ./mongodb-mms-automation-agent \
  --config=local.config \
  >> /var/log/mongodb-mms-automation/automation-agent-fatal.log 2>&1 &
```

**Step 12: Verify that the MongoDB Agent is running.**

In the Install Agent Instructions modal,
wait for each deployment to show Verified in the
Install the MongoDB Agent step.

Click Continue.

**Step 13: Enable monitoring of the Backing Databases.**

In the Set Up Ops Manager Monitoring modal,
wait for the agent to show Monitoring as enabled.

Click Continue.

**Step 14: Provide the Connection Details for the Backing Databases.**

Complete the following fields:

| Hostname | Provide the hostname of the host that serves the backing database. |
|---|---|
| Port | Provide the port of the backing database. |
| Enable Authentication | Toggle this to enable authentication. |
| Use TLS/SSL | Toggle to enable TLS. |

After Ops Manager displays Deployment found, click
Continue.

**Step 15: Confirm the Backing Databases setup.**

Ops Manager displays the host serving the backing databases and the
running agent. Click Continue.

**Step 16: Enable operational monitoring for the Application Database.**

Operational monitoring allows you to track CPU, memory, and disk 
capacity of the Application Database servers and set up alert 
notification when a specified alert condition occurs.

To disable operational monitoring, click No, Just Monitor.

To enable operational monitoring: 

a. Review the requirements to add Automation in read-only mode 
   for operational monitoring on each server in your deployment.

#. Select the checkbox to confirm that you have read the requirements 
   and risks listed in the page. 

#. Click Continue. 

**Step 17: Install Automation Agent on each of your servers.**

a. Select Automation from the Install Agent 
   dropdown list.

#. Click Initialize Automation.

**Step 18: Review and confirm your deployment for operational monitoring.**

The MongoDB Agent gathers detailed information about the MongoDB 
processes for operational monitoring. 

a. To review the information gathered by the MongoDB Agent, click 
   Review Deployment.

#. Review the settings 
   in the AppDB: Review Your Changes modal and click 
   Confirm & Deploy.

**Note:**

If you can't view monitoring data, verify that at least one host has
monitoring enabled.
