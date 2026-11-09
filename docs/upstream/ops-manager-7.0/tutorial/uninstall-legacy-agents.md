<!-- Converted from tutorial/uninstall-legacy-agents.txt (reStructuredText). Includes are inlined. -->

# Remove Legacy Agents

The legacy Backup and Monitoring Agents can be removed after the
MongoDB Agent has been
installed.

## Remove the Backup Agent from Ops Manager

### Remove from Ops Manager

To remove a Backup Agent from Ops Manager, stop the agent and then wait 24 hours.

### Delete from the Server

To delete the Backup Agent **from a Linux or macOS server**, stop the
agent and then remove the `mongodb-mms-backup-agent`
file from the `/usr/bin` directory. If you installed the agent using a
`tar.gz` file, the agent will be in the directory you chose during
installation.

To delete the Backup Agent **from a Windows server**, stop the agent and then use the Windows program uninstaller to
remove the `MongoDB Backup Agent` program.

## Remove Monitoring Agents from Ops Manager

### Remove from Ops Manager

To remove a Monitoring Agent from Ops Manager, stop the agent and then wait 5 minutes.

When an agent fails to ping Ops Manager for 5 minutes, Ops Manager views the agent as
inactive and distributes the agent's assignments to other agents (if
available).

**Note:**

The All Agents page  displays an inactive agent for 24 hours
before Ops Manager removes it from the page.

### Delete from the Server

To delete the Monitoring Agent **from a Linux or macOS server**, stop the
agent and then remove the
`mongodb-mms-monitoring-agent` file from the `/usr/bin` directory. If you
installed the agent using a `tar.gz` file, the agent will be in the 
directory you chose during installation.

To delete the Monitoring Agent **from a Windows server**, stop the agent and then use the Windows program uninstaller
to remove the `MongoDB Monitoring Agent` program.
