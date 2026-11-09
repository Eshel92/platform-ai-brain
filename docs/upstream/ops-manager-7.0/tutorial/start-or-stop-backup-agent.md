<!-- Converted from tutorial/start-or-stop-backup-agent.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Start or Stop the Backup Agent

**Important:** Legacy Backup and Monitoring Agents are EoL for Ops Manager 4.4

Update
from your self-managed legacy Backup and Monitoring Agents to the
MongoDB Agent.

For maintenance or troubleshooting purposes, you may want to
temporarily shut down or restart the Backup Agent. However, for proper
operation of Ops Manager Backup your Ops Manager project must have at least one
Backup Agent running. The project needs only one Backup Agent.

## Procedures

### Start the Backup Agent

#### Start an Agent Installed with an `rpm` Package

If you installed the Backup Agent using an `rpm` package, such as on
RHEL, CentOS, or SUSE, issue the following command to start the agent:

```none
sudo service mongodb-mms-backup-agent start
```

#### Start an Agent Installed with a `deb` Package

If you installed the Backup Agent using a `deb` package, as on
Ubuntu, issue the following command to start the agent:

```none
sudo start mongodb-mms-backup-agent
```

#### Start an Agent Installed with a `tar` File

Use this command if you installed to Linux or OSX using a `tar` file.
Issue the following command from the directory to which you installed
the Backup Agent:

```none
nohup ./mongodb-mms-backup-agent >> backup-agent.log 2>&1 &
```

#### Start the Backup Agent on Windows

In Windows `Control Panel`, open `Administrative Tools` and then
`Services`. In the list of services, select `MongoDB Backup Agent`. Select
the `Action` menu and select `Start`.

### Stop the Backup Agent

If you use Ops Manager Backup, you must have a Backup Agent running to ensure
up-to-date backup data.

#### Stop an Agent Installed with an `rpm` Package

If you installed the Backup Agent using an `rpm` package, such as on
RHEL, CentOS, or SUSE, issue the following command to stop the agent:

```none
sudo service mongodb-mms-backup-agent stop
```

#### Stop an Agent Installed with a `deb` Package

If you installed the Backup Agent using a `deb` package, as on
Ubuntu, issue the following command to stop the agent:

```none
sudo stop mongodb-mms-backup-agent
```

#### Stop an Agent Installed with a `tar` File

If you installed to a Linux system or OSX using a `tar` file, issue
the following command to stop the Backup Agent:

```none
pkill -f mongodb-mms-backup-agent
```

#### Stop the Backup Agent on Windows

In Windows `Control Panel`, open `Administrative Tools` and then
`Services`. In the list of services, select `MongoDB Backup Agent`.
Select the `Action` menu and select `Stop`.

If you receive a message that your Backup Agent is out of date, make
sure you are running an upgradeable version of the Backup Agent. If you
are running the version of the Backup Agent named `MongoDBBackup`,
you must remove it before upgrading. To check if you are running
`MongoDBBackup`, issue the following command in an Administrative
command prompt:

```none
sc query MongoDBBackup
```

If the command returns a result, you must remove the `MongoDBBackup`
agent. To remove it, issue the following:

```none
sc delete MongoDBBackup
```
