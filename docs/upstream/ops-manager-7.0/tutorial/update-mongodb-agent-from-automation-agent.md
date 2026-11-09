<!-- Converted from tutorial/update-mongodb-agent-from-automation-agent.txt (reStructuredText). Includes are inlined. -->

# Update from Deployments with Managed and Unmanaged Agents

You have a project with automated MongoDB deployments that may include
both Automation-managed and standalone Backup and Monitoring Agents.
You want to update to the MongoDB Agent.

To update to the MongoDB Agent, use the following procedures:

- For any standalone legacy Agents:

  - /tutorial/update-mongodb-agent-from-monitoring-agent

  - /tutorial/update-mongodb-agent-from-backup-and-monitoring-agents

- For those hosts where Automation manages Monitoring/Backup Agents:

  - /tutorial/update-mongodb-agent-from-all-agents

**Note:** Review the Prerequisites First

If you want to start or continue using Automation to manage your
MongoDB deployments, please review the
/tutorial/install-mongodb-agent-prereq before updating to the
MongoDB Agent.

## Procedure

**Step 1: Log in to the Ops Manager Application.**

**Step 2: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 3: Update automated hosts to MongoDB Agent.**

If your project has hosts that use Automation, you can
update the Agents on those hosts to the MongoDB Agent.

a. Click Update All.

b. Wait until all hosts show Updated.

c. Click Next.

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

The legacy Automation Agent credentials become the MongoDB Agent
credentials used for Automation. These credentials should not need
modification. However, if you need to modify them, navigate to
Deployment
arrow-right Security
arrow-right Settings
arrow-right Edit Settings.

**Step 4: Finish the installation of the MongoDB Agent.**

At the Final Steps modal, the legacy Backup and
Monitoring Agents are put into standby mode. Click
Finish.

## Next Steps

After the MongoDB Agent update completes:

- If you did not update Backup or Monitoring Agents when you installed
  the MongoDB Agent, you can activate
  Backup,
  Monitoring, or both on your MongoDB
  deployment.

- Stop and
  remove the legacy
  Monitoring Agent.

- Stop and
  remove the legacy Backup
  Agent.
