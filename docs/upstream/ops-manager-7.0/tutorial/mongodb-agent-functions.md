<!-- Converted from tutorial/mongodb-agent-functions.txt (reStructuredText). Includes are inlined. -->

# Manage the MongoDB Agent Functions

## Manage Backup Function

### Activate Backup

1. From your Context menu, click the project that has the
   hosts you want to configure.

#. Click Deployments.

#. Click Servers.

#. On the host where you want to activate Backup, click
   `ellipsis`.

#. Click Activate Backup.

#. From the banner, click Review & Deploy.

#. If you want to activate Backup, click
   Confirm & Deploy.
   Otherwise click Cancel, then Discard Changes
   to cancel activating Backup.

   **Note:**

   On the Server tab, the host that is tailing the oplog
   from each primary displays Backup - active. Any
   other host with Backup activated displays 
   Backup - standby.

### Deactivate Backup

1. From your Context menu, click the project that has the
   hosts you want to configure.

#. Click Deployments.

#. Click Servers.

#. On the host where you want to deactivate Backup, click
   `ellipsis`.

#. Click Deactivate Backup.

#. From the banner, click Review & Deploy.

#. If you want to activate Backup, click
   Confirm & Deploy.
   Otherwise click Cancel, then Discard Changes
   to cancel deactivating Backup.

## Manage Monitoring Function

### Activate Monitoring

1. From your Context menu, click the project that has the
   hosts you want to configure.

#. Click Deployments.

#. Click Servers.

#. On the host where you want to activate Monitoring, click
   `ellipsis`.

#. Click Activate Monitoring.

#. From the banner, click Review & Deploy.

#. If you want to activate Monitoring, click
   Confirm & Deploy.
   Otherwise click Cancel, then Discard Changes
   to cancel activating Monitoring.

   **Note:**

   On the Server tab, the host that distributes
   monitoring work to each running monitoring agent displays
   Monitoring - active. Any other host with Monitoring
   activated displays Monitoring - standby.

You can activate Monitoring
on multiple MongoDB Agents to distribute monitoring assignments and
provide failover. Ops Manager distributes monitoring assignments among up
to 100 running MongoDB Agents. Each MongoDB Agent running active
Monitoring monitors a different set of MongoDB processes. One
MongoDB Agent running active Monitoring per project is the primary
Monitor. The primary Monitor reports the cluster's status to Ops Manager.
As MongoDB Agents have Monitoring enabled or disabled, Ops Manager
redistributes assignments. If the primary Monitor fails, Ops Manager
assigns another MongoDB Agent running active Monitoring to be the
primary Monitor.

If you run more than 100 MongoDB Agents with active Monitoring, the
additional MongoDB Agents run as standby MongoDB Agents. A standby
MongoDB Agent is idle, except to log its status as a standby and
periodically ask Ops Manager if it should begin monitoring.

To tune the frequency at which standby MongoDB Agents check to see
if they should begin monitoring and the interval Ops Manager uses to
determine if a standby agent should start monitoring, see
standby-monitoring-agent.

If you install multiple Monitoring Agents, ensure that *all* the
MongoDB Agents with active Monitoring can reach all the `mongod`
processes in the deployment.

To activate Monitoring on multiple MongoDB Agents, repeat the
activation process on multiple
MongoDB Agents.

### Deactivate Monitoring

1. From your Context menu, click the project that has the
   hosts you want to configure.

#. Click Deployments.

#. Click Servers.

#. On the host where you want to deactivate Monitoring, click
   `ellipsis`.

#. Click Deactivate Monitoring.

#. From the banner, click Review & Deploy.

#. If you want to deactivate Monitoring, click
   Confirm & Deploy.
   Otherwise click Cancel, then Discard Changes
   to cancel activating Monitoring.

## Manage Automation Function

### Activate Automation

Automation is activated when you:

- Deploy a standalone MongoDB instance
- Deploy a replica set
- Deploy a sharded cluster
- Import an existing MongoDB deployment into Ops Manager.
