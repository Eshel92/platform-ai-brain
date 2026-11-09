<!-- Converted from tutorial/delete-monitoring-agent.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Remove Monitoring Agents from Ops Manager

**Important:** Legacy Monitoring Agent is EoL for Ops Manager 4.4

Update
from your self-managed legacy Monitoring Agent to the
MongoDB Agent.

## View Active Agents

To view your active Monitoring Agents, click Deployment, then the
Agents tab, then All Agents.

Active agents are those that have pinged Ops Manager in the last 5 minutes.

## Remove from Ops Manager

To remove a Monitoring Agent from Ops Manager, stop the agent and then wait 5 minutes.

When an agent fails to ping Ops Manager for 5 minutes, Ops Manager views the agent as
inactive and distributes the agent's assignments to other agents (if
available).

**Note:**

The All Agents page  displays an inactive agent for 24 hours
before Ops Manager removes it from the page.

## Delete from the Server

To delete the Monitoring Agent **from a Linux or OSX server**, stop the
agent and then remove the
`mongodb-mms-monitoring-agent` file from the `/usr/bin` directory. If you
installed the agent using a `tar.gz` file, the agent will be in the 
directory you chose during installation.

To delete the Monitoring Agent **from a Windows server**, stop the agent and then use the Windows program uninstaller
to remove the `MongoDB Monitoring Agent` program.
