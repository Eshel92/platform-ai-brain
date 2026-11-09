<!-- Converted from tutorial/update-fatal-log-rotation.txt (reStructuredText). Includes are inlined. -->

# Update Agent to Enable Fatal Log Rotation

For MongoDB Agent versions below 12.0.21, you must reinstall the 
MongoDB Agent to enable fatal log file rotation.

If you have upgraded the MongoDB Agent to 12.0.21 or later from  12.0.20
or earlier, you must manually reinstall your current MongoDB Agent version (12.0.21+) 
to enable fatal log file rotation.

For new installations of the MongoDB Agent (12.0.21+), fatal log file rotation is automatically enabled.

**Note:**

Fatal log file rotation helps to maintain a 
useful `automation-agent-fatal.log` file by rotating the file on a 
regular basis and deleting only the oldest logs.

## Reinstall the MongoDB Agent

To reinstall the MongoDB Agent to enable fatal log file rotation, follow 
the procedure for your distribution:

**log-update-rpm:**

**Step 1: Stop the MongoDB Agent.**

Stop the MongoDB Agent using the appropriate command for your agent 
process. 

If you started your agent process with `systemd`, run the following 
command:

```sh
sudo systemctl stop mongodb-mms-automation-agent.service
```

If you started your agent process with `init.d`, run the following 
command:

```sh
sudo service mongodb-mms-automation-agent stop
```

**Step 2: Reinstall the MongoDB Agent.**

Use the installation instructions that apply to your MongoDB Agent 
use case:

- If you use MongoDB Agent to manage deployments, follow the 
  instructions to 
  Install the MongoDB Agent to Manage Deployments, or

- If you use MongoDB Agent to only monitor or back up deployments, 
  follow the instructions to 
  Install the MongoDB Agent to Only Monitor or Backup Deployments.

At the top of the installation page, select 
`RHEL/CentOS/SLES/AMZ` and follow the procedure to install 
the MongoDB Agent.

**Step 3: Start the MongoDB Agent.**

Using your terminal, start the MongoDB Agent with the appropriate 
command for your system:

To start the agent process with `systemd`, run the following 
command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

To start the agent process with `init.d`, run the following 
command:

```sh
sudo service mongodb-mms-automation-agent start
```

The reinstalled MongoDB Agent rotates the `automation-agent-fatal.log` file when the MongoDB Agent restarts or when the file reaches 100 MiB.

The MongoDB Agent retains the new `automation-agent-fatal.log` file and five rotated logs.

**log-update-deb:**

**Step 1: Stop the MongoDB Agent.**

Stop the MongoDB Agent using the following command:

```sh
sudo systemctl stop mongodb-mms-automation-agent.service
```

**Step 2: Reinstall the MongoDB Agent.**

Use the installation instructions that apply to your MongoDB Agent 
use case:

- If you use MongoDB Agent to manage deployments, follow the 
  instructions to 
  Install the MongoDB Agent to Manage Deployments, or

- If you use MongoDB Agent to only monitor or back up deployments, 
  follow the instructions to 
  Install the MongoDB Agent to Only Monitor or Backup Deployments.

At the top of the installation page, select 
`Ubuntu/ Debian` and follow the procedure to install 
the MongoDB Agent.

**Step 3: Start the MongoDB Agent.**

Using your terminal, start the MongoDB Agent with the following 
command:

```sh
sudo systemctl start mongodb-mms-automation-agent.service
```

The reinstalled MongoDB Agent rotates the `automation-agent-fatal.log` file when the MongoDB Agent restarts or when the file reaches 100 MiB.

The MongoDB Agent retains the new `automation-agent-fatal.log` file and five rotated logs.

**log-update-tar:**

**Step 1: Stop the MongoDB Agent.**

Stop the MongoDB Agent using the following command:

```sh
pkill -f mongodb-mms-automation-agent
```

**Step 2: Reinstall the MongoDB Agent.**

Use the installation instructions that apply to your MongoDB Agent 
use case:

- If you use MongoDB Agent to manage deployments, follow the 
  instructions to 
  Install the MongoDB Agent to Manage Deployments, or

- If you use MongoDB Agent to only monitor or back up deployments, 
  follow the instructions to 
  Install the MongoDB Agent to Only Monitor or Backup Deployments.

At the top of the installation page, select 
`Linux` and follow the procedure to install 
the MongoDB Agent.

**Step 3: Start the MongoDB Agent.**

Using your terminal, run the following command with:

- The path to your configuration file
- The path to save the fatal log file

```sh
nohup /bin/bash -c "./mongodb-mms-automation-agent --config=./example/path/to/config 2>&1 | ./fatallogger -logfile ./example/path/to/log 2>&1"
```
