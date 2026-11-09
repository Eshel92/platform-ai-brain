<!-- Converted from tutorial/view-agent-status.txt (reStructuredText). Includes are inlined. -->

# View Agent Status

Click Deployment, then the Agents tab, then All Agents.
Ops Manager displays the following information about your agents:

* - Field

  - Description

* - Agent Hostname

  - The hostname of the agent and the agent type, indicated by the
    icon on the left-hand side. The icon to agent type mapping is as
    follows:

    | Icon | Agent Type |
    |---|---|
    | .. image:: /images/icon-automation-agent.png :alt: "A robot icon that maps to the Automation agent type." | Automation |
    | .. image:: /images/icon-backup-agent.png :alt: "A clock icon that maps to the Backup agent type." | Backup |
    | .. image:: /images/icon-monitoring-agent.png :alt: "A graph icon that maps to the Backup agent type." | Monitoring |

* - Last Conf Call

  - The number of seconds since the last time the agent polled Ops Manager.

* - Version

  - The version of the agent software running on this agent instance.

* - Status

  - Indicates whether the agent is active.

* - Action

  - Click View Logs to view the agent's log.

    To access this feature, you must either:

    - Belong to the project

    - Have the Global Monitoring Admin role or the Global Owner role
