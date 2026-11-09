<!-- Converted from tutorial/manage-ops-manager-logs.txt (reStructuredText). Includes are inlined. -->

# Manage Ops Manager Application Logs

You can use Ops Manager to review a variety of log files:

- MongoDB process logs
  (`mongod`, `mongos`)
- MongoDB Agent logs
- Ops Manager access, backup, operations, and startup logs

You can change how long you keep
some Ops Manager logs. Your company may need to keep log data for legal
requirements. You can change your log retention policy to adhere to
those requirements.

## Available Ops Manager Logs

Each host that serves Ops Manager stores its logs in the following path:

```bash
/opt/mongodb/mms/logs/
```

For some logs, Ops Manager uses configuration files. Ops Manager rotates
these logs daily in the following manner:

1. Close the current log file.
#. Compress the closed log file using `gzip`.
#. Start a new log file.

Ops Manager retains each compressed log file for 30 days. After 30 days,
it deletes that compressed file.

You can change the retention policy
of the following logs:

| Log File Name | Log Contents | Configuration File |
|---|---|---|
| `mms[#].log`, typically `mms0.log` | Ops Manager operations | `logback.xml` |
| `daemon.log` | Ops Manager backup operations | `logback.xml` |
| `mms[#]-access.log`, typically `mms0-access.log` | Ops Manager access attempts | `logback-access.xml` |

You can manage the retention policy of the following logs
using your platform's tools:

|  |  |
|---|---|
| `daemon-startup.log` | Ops Manager backup process startup process messages |
| `mms-migration.log` | Ops Manager migration process messages |
| `mms[#]-startup.log`, typically `mms0-startup.log` | Ops Manager startup process messages |

Ops Manager may generate additional log files in extenuating
circumstances. If you find files in the log directory that aren't
listed in these tables, contact [MongoDB Support](https://support.mongodb.com/welcome)
for assistance.

## Change Ops Manager Log Retention

If Ops Manager logs have configuration files, you can change their
log retention using these files. You cannot change log retention of
these log files in the console.

**Important:**

If you upgrade Ops Manager, it overwrites its configuration files. To
set log retention after you upgrade, repeat the steps in this
procedure.

**Step 1: Locate the configuration file.**

Navigate to the `/opt/mongodb/mms/conf/` directory,
and locate the corresponding configuration file.

- To change retention for `mms0.log` or
  `daemon.log`, open `logback.xml`.

- To change retention for `mms0-access.log` or
  `mms0-startup.log`, open
  `logback-access.xml`.

**Step 2: Open the configuration file.**

Open the file in your preferred editor.

**Example:**

The following configuration file excerpt specifies a
log retention policy of **45** days.

```xml
  <appender ...>
   <file>${log_path}.log</file>
     <encoder class ...>
        <pattern>... </pattern>
     </encoder>
     <rollingPolicy class ...>
       <fileNamePattern>...</fileNamePattern>
       <maxHistory>45</maxHistory>
    </rollingPolicy>
  </appender>
```

**Step 3: Specify a new log retention value.**

Change the value between the `<maxHistory>` tags, in days,
to retain compressed log files.

**Step 4: Save the file.**

**Step 5: Restart Ops Manager for the changes to take effect.**

To learn more, see Start and Stop Ops Manager
Application.

## Change Ops Manager Log Rotation Policy

By default, Ops Manager rotates and compresses its logs once per day. If
you have large log files, you can also rotate them by size.
 
To change your rotation policy to rotate logs based on both size and
time:

**Step 1: Locate the configuration file.**

Navigate to the `/opt/mongodb/mms/conf/` directory,
and locate the corresponding configuration file.

- To change the rotation policy for `mms0.log` or
  `daemon.log`, open `logback.xml`.

- To change the rotation policy for `mms0-access.log` or
  `mms0-startup.log`, open
  `logback-access.xml`.

**Step 2: Open the configuration file.**

Open the file in your preferred editor.

**Example:**

The following configuration file excerpt shows 
the default **time based** rotation policy.

```xml
  <appender ...>
   <file>${log_path}.log</file>
     <encoder class ...>
        <pattern>... </pattern>
     </encoder>
     <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
       <fileNamePattern>...</fileNamePattern>
       <maxHistory>...</maxHistory>
    </rollingPolicy>
  </appender>
```

**Step 3: Modify the new log rotation policy.**

Make the following changes to the log configuration file:

a. Change the `class` attribute in the `<rollingPolicy>` tag.
b. Change the value in the `<fileNamePattern>` tag.
c. Add the `<maxFileSize>` and `<totalSizeCap>` tags after
   `<maxHistory>` to modify the log storage settings.

```diff
--- /opt/mongodb/mms/conf/logback-access.xml
+++ /opt/mongodb/mms/conf/logback-access.xml
@@ -1,4 +1,7 @@
-<rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
-  <fileNamePattern>${log_path}.%d{yyyyMMdd}.log.gz</fileNamePattern>
-  <maxHistory>30</maxHistory>
+<rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
+  <fileNamePattern>${log_path}.%d{yyyyMMdd}.%i.log.gz</fileNamePattern>
+  <maxHistory>30</maxHistory>
+  <maxFileSize>100MB</maxFileSize>
+  <totalSizeCap>20GB</totalSizeCap>
 </rollingPolicy>
```

**Step 4: Save the file.**

**Step 5: Restart Ops Manager for the changes to take effect.**

To learn more, see Start and Stop Ops Manager
Application.

**See also:**

- view-mms-realtime-logs
- toggle-log-collection-for-project
- toggle-log-collection-for-deployment
- view-mms-ondisk-logs
- Configure Log Rotation
- View Agent Logs
- Configure Agent Log Rotation
