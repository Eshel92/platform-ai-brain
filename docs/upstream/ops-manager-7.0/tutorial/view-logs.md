<!-- Converted from tutorial/view-logs.txt (reStructuredText). Includes are inlined. -->

# View, Retrieve, and Manage Logs

Ops Manager collects log information for both MongoDB processes and its
agents. For MongoDB processes, you can access both real-time logs and
on-disk logs.

- The MongoDB logs provide the diagnostic logging information for your
  `mongod` and `mongos` processes.
- The Agent logs provide insight into the behavior of your Ops Manager
  agents.

## MongoDB Real-Time Logs

The MongoDB Agent issues the `getLog` command with every
monitoring ping. This command collects log entries from RAM cache of
each MongoDB process.

Ops Manager enables real-time log collection by default. You can disable log
collection for either
all MongoDB deployments in
an Ops Manager project or for
individual MongoDB deployments.
If you disable log collection, Ops Manager continues to display previously
collected log entries.

### View MongoDB Real-Time Logs

To access this feature, you must have privileges granted by one of
the following roles:

- `Project Automation Admin`
- `Project Backup Admin`
- `Project Monitoring Admin`
- `Project Owner`

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: (Optional) For sharded clusters, filter which process type is listed.**

The four buttons are listed in the following order, left to right:
Shards, Configs, Mongos, and
BIs. 

| Process | Displays |
|---|---|
| Shards | mongod processes that host your data. |
| Configs | mongod processes that run as config servers to store a sharded cluster's metadata. |
| Mongos | mongos processes that route data in a sharded cluster. |
| BIs | BI (Business Intelligence) processes that access data in a sharded cluster. |

**Step 3: On the line listing the process, click Metrics.**

**Step 4: Click the Logs tab.**

The tab displays log information.

**Step 5: Refresh the browser window to view updated entries.**

### Enable or Disable Log Collection for a Deployment

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line for any process, click the ellipsis [...] icon then click Monitoring Settings.**

**Step 3: Toggle Collect Logs For Host as desired.**

a. Click the Logs tab.
b. Toggle the Collect Logs For Host to Off or
   On, as desired.

**Step 4: Click X to close the Monitoring Settings box.**

If you turn off log collection, existing log entries remain in the
Logs tab, but Ops Manager does not collect new entries.

### Enable or Disable Log Collection for the Project

**Step 1: Click Settings, then Project Settings.**

**Step 2: Toggle the Collect Logs For All Hosts option to Yes or No, as desired.**

## MongoDB On-Disk Logs

Ops Manager collects on-disk logs even if the MongoDB instance is not
running. The MongoDB Agent collects the logs from the location you
specified in the MongoDB `systemLog.path`
configuration option. The
MongoDB on-disk logs are a subset of the real-time logs and therefore
less verbose.

You can configure log rotation for
the on-disk logs. Ops Manager rotates logs by default.

This procedure rotates both system and audit logs for Ops Manager.

### View MongoDB On-Disk Logs

To access this feature, you must have privileges granted by one of
the following roles:

- `Project Automation Admin`
- `Project Backup Admin`
- `Project Monitoring Admin`
- `Project Owner`

**Step 1: Click the deployment whose logs you want to download, then click Request Logs**

Click the ellipsis ... icon on the line for any
process, replica set, or sharded cluster in the
project, then click Request Logs.

**Step 2: Select which types of log Ops Manager per process to collect and the maximum cumulative size of these logs.**

To choose logs to download, perform the following actions:

* - Action

  - Purpose

* - Click MongoDB Logs

  - Gather logs from deployed MongoDB processes.

    This option isn't available for deployed MongoDB processes 
    if the systemLog.destination 
    property is set to `syslog`.

* - Click MongoDB FTDC Data

  - Gather the diagnostic data files from the (FTDC
    (full-time diagnostic data capture)) collection mechanism,
    such as server statistics and status messages.

* - Click Automation Logs

  - Gather logs from the deployed Automation Agents.

* - Click Backup Logs

  - Gather logs from all deployed Backup Agents.

    This differs from other logs. The logs collected are not
    limited to the selected hosts, but include all Backup Agent
    logs in the deployment.

* - Click Monitoring Logs

  - Gather logs from all deployed
    Monitoring Agent.

    This differs from other logs. The logs collected are not
    limited to the selected hosts, but include all Monitoring
    Agent logs in the deployment.

* - Set Filter By Size in MB

  - Enter the maximum cumulative uncompressed size in megabytes
    of all selected log files.

    - This limit is *cumulative*.

      - For MongoDB or FTDC (full-time diagnostic data capture) logs, this limits the size of the
        collected logs per process.
      - For Agents, this limits the size of related logs per Agent.

    - Those log files are then archived and compressed.

      For example, if you set this value to `50` MB, Ops Manager gathers a total
      of 50 MB of uncompressed log file from every `mongod` and
      `mongos` process and each Agent for all logs you chose to
      download.

    - If the current log file is less than the specified size,
      Ops Manager gathers the most recent rotated file as well.

    - If the total size of the log files reaches the specified
      size part way through a log file, this last log file is
      truncated to the most recent line that falls within the
      specified size.

    - The maximum amount of log files that can be collected is 20
      GB. This maximum includes all collected log files that have
      not expired. If you request additional logs and collecting
      those logs results in more than 20 GB of logs collected,
      Ops Manager generates an error. The total amount of logs
      collected compared to the limit is displayed as
      Estimated Total Size.

    - This option is not available if you select Filter
      By Date Range.

* - Set Filter By Date Range

  - Enter a date range to limit the logs collected to that range.

    - This option is not available if you select Filter
      By Size.

**Example:**

You choose to collect 20 MB of logs from all processes in a
replica set. This replica set has three mongod
processes on two hosts:

- `host1:27017`
- `host2:27017`
- `host2:27018`

Your deployment runs the following agents:

|  |  |
|---|---|
| Automation Agent | `host1`, `host2`, `host4`, `host5` |
| Backup Agent | `host4` |
| Monitoring Agent | `host4`, `host5` |

When you choose all the log types for this replica set, and limit
to 20 MB per process, Ops Manager shows that the Estimated
Total Size is 220 MB (11 processes * 20 MB) out of 20 GB.

Once the log collection begins, Ops Manager scans the log directories
for the `mongod` processes and their associated FTDC (full-time diagnostic data capture) from the
most current log entry until 20 MB of log files or the end of the
last log is collected. All the Monitoring and Backup Agents in the
deployment are also scanned.

- The Backup Agent has 60 MB of logs.
- Each MongoDB process (3) has 7 MB of logs plus 15 MB of
  FTDC (full-time diagnostic data capture) data per process.
- Each Monitoring Agent (2) has 30 MB of logs.
- Each Automation Agent (2) has 12 MB of logs.

The total size of logs collected is **150 MB**:

(20 + (3 * (7 + 15)) + (2 * 20) + (2 * 12)) = 150

- The maximum of 20 MB of logs from the Backup Agent is collected.
- All of the logs for each MongoDB process are collected:
  7 MB of MongoDB + 15 MB of FTDC (full-time diagnostic data capture) data.
- The maximum of 20 MB of logs from each Monitoring Agent is
  collected.
- All of the Automation Agent logs from `host1` and `host2`
  are collected. `host4` and `host5` do not host any processes
  in the replica set.

The resulting archive structure within the downloaded archive is:

```sh
host1/27017/mongodb
host1/27017/ftdc
host1/automation_agent
host2/27017/mongodb
host2/27017/ftdc
host2/27018/mongodb
host2/27018/ftdc
host2/automation_agent
host4/backup_agent
host4/monitoring_agent
host5/monitoring_agent
```

**Step 3: (Optional) Redact sensitive information from the logs.**

To anonymize your logs, select
Replace IP addresses, hostnames, namespaces, strings with 
randomized values. 

This option replaces IP addresses with a private range (192.168.x.x). 
For hostnames, this option replaces only FQDN (fully qualified domain name). Other hostnames 
remain unchanged. Replacements follow a predictable pattern. For 
example, if `blue.strawberry` replaces one instance of the FQDN (fully qualified domain name) 
`test.internal`, `blue.strawberry` replaces all other instances 
of `test.internal` as well.

**Note:**

This does not use the
$redact
aggregation pipeline. That is a separate capability with a
broader feature set.

**Step 4: Click Request Logs.**

**Step 5: View the progress on the Log Request History page.**

Entry Status shows Collecting Logs... and automatically
updates its status as log collection continues.

- If Ops Manager fails to retrieve log files, click Retry to
  retrieve the failed log files again.

- If a failure has occurred, you can still download the archive. Some
  of the requested log files will be missing.

**Step 6: Download the collected logs archive.**

Click the Download icon.

The size listed for the archive on the Log Request
History page is the uncompressed size. The archive consumes
that amount of disk space on the target host once it is extracted.

This download can only be restarted and not resumed. If the download
fails, you must download the logs again.

The archive is named `mongodb-logfiles_<instance_or_process>_<ISO8601_Format_Date>.tar.gz`.

The extracted files use the following directory structure:

```sh
<host>
  automation_agent
    automation-agent-verbose.log
    automation-agent-verbose.log.<ISO8601_Format_Date>
  backup_agent
    backup-agent-verbose.log
    backup-agent-verbose.log.<ISO8601_Format_Date>
  monitoring_agent
    monitoring-agent-verbose.log
    monitoring-agent-verbose.log.<ISO8601_Format_Date>
  <replica_set> // Sharded Cluster Only
    <port>
      ftdc
        metrics.<ISO8601_Format_Date>
        metrics.interim
      mongodb
        mongodb.log
        mongodb.log.<ISO8601_Format_Date>
  <port> // Replica Set or Standalone
    ftdc
      metrics.<ISO8601_Format_Date>
      metrics.interim
    mongodb
      mongodb.log
      mongodb.log.<ISO8601_Format_Date>
```

**Note:**

When you extract the `tar` archive on a Microsoft Windows host,
use an archive extraction utility that supports [PAX extended headers](https://www.gnu.org/software/tar/manual/html_node/PAX-keywords.html).
Some Windows archive utilities have issues with PAX extended
headers for `tar`.

Collected logs expire and are removed after 7 days. To extend the
lifetime of a particular log file, click the extend link
for that archive on the Log Request History page.

### Configure Log Rotation

Ops Manager can rotate and compress logs for clusters that the MongoDB Agent
manages. If the MongoDB Agent only monitors a cluster, it ignores that
cluster's logs.

**Important:**

If you're running MongoDB Enterprise version 5.0 or later and 
MongoDB Agent 11.0.13.7055 or later, you can:

- Set separate rules for rotating server logs and audit logs.
- Compress and delete audit logs using Ops Manager. For security reasons, we recommend managing
  your audit log compression and deletion outside of Ops Manager.

If you're running earlier versions of MongoDB Enterprise or the
MongoDB Agent, Ops Manager: 

- Uses your System Log Rotation settings to rotate both the
  server logs and the audit logs. 
- Doesn't compress or delete audit logs. If you configure compression and
  deletion, Ops Manager applies these settings to the server logs only.

MongoDB Community users can rotate, compress, and delete the server logs
only.

**Note:**

When you use this feature, disable any platform-based log-rotation
services like `logrotate`. Remove the `reopen` and `rename` 
flags from the process configuration files. If the MongoDB Agent only 
monitors the cluster, that cluster may use platform-based services.

**Step 1: Open the MongoDB Log Settings.**

a. Click Deployment.
b. In the More drop-down list, click MongoDB Log Settings.

**Step 2: Enable log rotation.**

Toggle System Log Rotation to ON to rotate server
logs.

MongoDB Enterprise users running MongoDB Enterprise version 5.0 or later and 
MongoDB Agent 11.0.13.7055 and later can also toggle
Audit Log Rotation to ON
to rotate audit logs and configure audit log rotation separately.

If you're running earlier versions of MongoDB Enterprise or the MongoDB Agent,
setting System Log Rotation to ON also rotates audit logs.

Set log rotation to OFF if you don't want Ops Manager to rotate its
logs. Log rotation is OFF by default. 

After you enable log rotation, Ops Manager displays additional log rotation settings.

**Step 3: Configure the log rotation settings.**

Ops Manager rotates the logs on your MongoDB hosts per the following
settings:

| Field | Necessity | Action | Default |
|---|---|---|---|
| Size Threshold (MB) | Required | Ops Manager rotates log files that exceed this maximum log file size. | `1000` |
| Time Threshold (Hours) | Required | Ops Manager rotates logs that exceed this duration. | `24` |
| Max Uncompressed Files | Optional | Log files can remain uncompressed until they exceed this number of files. Ops Manager compresses the oldest log files first. If you leave this setting empty, Ops Manager will use the default of `5`. | `5` |
| Max Percent of Disk | Optional | Log files can take up to this percent of disk space on your MongoDB host's log volume. Ops Manager deletes the oldest log files once they exceed this disk threshold. If you leave this setting empty, Ops Manager will use the default of `2%`. | `2%` |
| Total Number of Files | Optional | Total number of log files. If a number is not specified, the total number of log files defaults to `0` and is determined by other Rotate Logs settings. | `0` |

When you are done, click Save to review your changes.

**Step 4: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## Agent Logs

Ops Manager collects logs for all your MongoDB Agents.

### View Agent Logs

To access this feature, you must have privileges granted by one of
the following roles:

- `Project Automation Admin`
- `Project Backup Admin`
- `Project Monitoring Admin`
- `Project Owner`

**Step 1: Click Deployment, then the Agents tab, then Agent Logs.**

The page displays logs for the type of agent selected in the View
drop-down list. The page filters logs according to any filters selected in
through the gear icon.

**Step 2: Filter the log entries.**

To display logs for a different type of agent, use the View
drop-down list.

To display logs for a specific hosts or MongoDB processes, click the gear icon
and make your selections.

To clear filters, click the gear icon and click Remove Filters.

To download the selected logs, click the gear icon and click
Download as CSV File.

**Note:**

To view logs for a specific agent, you can alternatively click the
Agents tab's All Agents list and then click
view logs for the agent.

### Configure Agent Log Rotation

If you use Automation to manage your cluster, follow
this procedure to configure rotation of the Agent log files.

**Note:**

If you haven't enabled Automation, see the following documentation
for information about how to manually configure logging settings in
the agent configuration files:

- MongoDB Agent General Logging Settings

- MongoDB Agent Monitoring Logging Settings

- MongoDB Agent Backup Logging Settings

**Step 1: Click Deployment, then the Agents tab.**

**Step 2: Click Downloads & Settings.**

**Step 3: Scroll down to the Agent Log Settings section.**

**Step 4: Edit the log settings.**

Click the pencil icon to edit the Monitoring Agent 
or Backup Agent log settings:

* - Name
  - Type
  - Description

* - Linux Log File Path
  - string
  - *Conditional: Logs on a Linux host.* 
    The path to which the agent writes its logs on a Linux host.

    The suggested value is:

    ```sh
    /var/log/mongodb-mms-automation/monitoring-agent.log
    ```

* - Windows Log File Path
  - string
  - *Conditional: Logs on a Windows host.* 
    The path to which the agent writes its logs on a Windows host.

    The suggested value is:

    ```bat
    %SystemDrive%\MMSAutomation\log\mongodb-mms-automation\monitoring-agent.log
    ```

* - Rotate Logs
  - Toggle
  - A toggle to select if the logs should be rotated.

* - Size Threshold (MB)
  - integer
  - The size where the logs rotate automatically. The default value
    is `1000`.

* - Time Threshold (Hours)
  - integer
  - The duration of time when the logs rotate automatically. The 
    default value is `24`.

* - Max Uncompressed Files
  - integer
  - *Optional.* The greatest number of log files, including the 
    current log file, that should stay uncompressed. The suggested 
    value is `5`.

* - Max Percent of Disk
  - integer
  - *Optional.* The greatest percentage of disk space on your 
    MongoDB hosts that the logs should consume. The suggested 
    value is `2%`.

* - Total Number of Files
  - integer
  - *Optional.* The total number of log files. If a number is not specified, 
    the total number of log files defaults to `0` and is determined by other 
    Rotate Logs settings.

When you are done, click Save.

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## Ops Manager Logs

You can use Ops Manager to review a variety of log files:

- MongoDB process logs
  (`mongod`, `mongos`)
- MongoDB Agent logs
- Ops Manager access, backup, operations, and startup logs

You can change how long you keep
some Ops Manager logs. Your company may need to keep log data for legal
requirements. You can change your log retention policy to adhere to
those requirements.
