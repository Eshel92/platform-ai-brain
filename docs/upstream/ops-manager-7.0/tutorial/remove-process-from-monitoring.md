<!-- Converted from tutorial/remove-process-from-monitoring.txt (reStructuredText). Includes are inlined. -->

# Remove a Process from Monitoring

## Monitored Processes

Removing a process from monitoring means Ops Manager no longer displays
its status or tracks its metrics. You must terminate the
deployment's backups before you can remove a
monitored deployment.

## Remove a Process from Monitoring

Follow this procedure to remove one monitored process from Ops Manager.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click Modify in the cluster from which you want to remove a process.**

**Step 3: In Member Configuration, click the ellipsis icon next to the process that you want to remove and select Remove from Cluster.**

For replica sets, select Remove from Replica Set.
For `mongod` processes in a sharded replica set, select
Remove From Shard. For `mongos` processes,
select Remove from Cluster.

**Step 4: Click Remove from Cluster in the verification dialog.**

For replica sets, select Remove from Replica Set.
For `mongod` processes in a sharded replica set, select
Remove From Shard. For `mongos` processes,
select Remove from Cluster.

**Step 5: Click Save.**

**Step 6: Click Review & Deploy to review your changes.**

**Step 7: Click Confirm and Deploy to deploy your changes.**

The process that you removed earlier now appears as a standalone 
process. However, `mongos` processes are automatically removed 
from the cluster and do not appear.

**Step 8: Click the ellipsis next to the standalone process, and select Remove from Ops Manager.**
