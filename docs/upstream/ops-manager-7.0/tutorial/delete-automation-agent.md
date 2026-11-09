<!-- Converted from tutorial/delete-automation-agent.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Remove the Automation Agent from Ops Manager

**Important:** Legacy Automation Agent is EoL for Ops Manager 4.4

Update
from the legacy Automation Agent to the
MongoDB Agent.

## View Active Agents

To view your active Automation Agents:

1. Click Deployment.
#. Click the Agents tab.
#. Click All Agents. 

The page displays agents that have been active in the last 24 hours. If
an agent fails to report to Ops Manager for more than 24 hours, Ops Manager removes
the agent from this page.

## Remove from Ops Manager

To remove an Automation Agent from Ops Manager:

1. Stop the agent.
#. Wait for the agent to clear the agent list in about 24 hours.

## Delete from a Host

To delete the Automation Agent from:

**linux:**

1. Stop the agent.
#. Delete the `mongodb-mms-automation-agent` file from the
   `/usr/bin` directory.

   **Note:**

   If you installed the agent using a `tar.gz` file, the
   agent is found in the directory you chose during
   installation.

**rpm:**

1. Stop the agent.

2. Uninstall the package:

   **x86rpm:**

   Use the following command on hosts running RHEL 5.X,
   6.x, 7.x; CentOS 5.x, 6.x, 7.x; or Amazon Linux on
   x86_64 architecture:

   ```sh
   sudo yum remove mongodb-mms-automation-agent-manager.x86_64
   ```

   **x86suse:**

   Use the following command on hosts running SUSE 12 on
   x86_64 architecture:

   ```sh
   sudo zypper remove mongodb-mms-automation-agent-manager.x86_64
   ```

   **ppcrpm:**

   Use the following command on hosts running RHEL 7.x or
   CentOS 7.x on PowerPC architecture:

   ```sh
   sudo yum remove mongodb-mms-automation-agent-manager.ppc641e
   ```

**deb:**

1. Stop the agent.

2. Uninstall the package:

   ```sh
   dpkg --remove mongodb-mms-automation-agent-manager
   ```

**windows:**

1. Stop the agent.
#. Click the `windows` button.
#. Click Control Panel.
#. Click Programs and Features.
#. Click MongoDB Automation Agent.
#. Click Uninstall.
#. Follow the wizard to complete the removal.
