<!-- Converted from tutorial/delete-backup-agent.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Remove the Backup Agent from Ops Manager

**Important:** Legacy Backup and Monitoring Agents are EoL for Ops Manager 4.4

Update
from your self-managed legacy Backup and Monitoring Agents to the
MongoDB Agent.

## View Active Agents

To view your active Backup Agents, click Deployment, then the
Agents tab, then All Agents.
The page displays agents that have been active
in the last 24 hours. If an agent fails to report to Ops Manager for more than 24
hours, Ops Manager removes the agent from this page.

## Remove from Ops Manager

To remove a Backup Agent from Ops Manager, stop the agent and then wait 24 hours.

## Delete from the Server

To delete the Backup Agent **from a Linux or OSX server**, stop the
agent and then remove the `mongodb-mms-backup-agent`
file from the `/usr/bin` directory. If you installed the agent using a
`tar.gz` file, the agent will be in the directory you chose during
installation.

To delete the Backup Agent **from a Windows server**, stop the agent and then use the Windows program uninstaller to
remove the `MongoDB Backup Agent` program.
