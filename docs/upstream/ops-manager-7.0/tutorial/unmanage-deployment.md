<!-- Converted from tutorial/unmanage-deployment.txt (reStructuredText). Includes are inlined. -->

# Stop Managing and/or Monitoring One Deployment

Ops Manager uses Automation to manage your deployments but can monitor and
back up your deployments without Automation.

If you no longer want to use Ops Manager for one or both of these 
capabilities, you can stop Ops Manager from either:

- Managing your deployment while *still* monitoring it and backing it
  up, or
- Managing, monitoring, *and* backing up your deployment 

After you stop Ops Manager from managing a deployment, you cannot use Ops Manager 
to upgrade, stop, start, or change that deployment's configuration in 
any way. If you want to
shut down your deployment
before stop Ops Manager from managing it, *do that first*. Otherwise, you
must connect to each process using `mongosh` to
shut down the process directly.

If you stop using Ops Manager to monitor your deployment, any associated 
snapshots are deleted and all historic monitoring data is removed.

Stopping Ops Manager from managing or monitoring your deployment does not
affect the deployment's `mongod` and `mongos` processes. These
processes continue to run uninterrupted unless you explicitly shut it
down first.

## Considerations

### Restore a Previously Removed Host

If you have not completely removed a host from Ops Manager and want to
restore that host, you can reimport the deleted MongoDB process.

If you have completely removed a host from Ops Manager, restore
that host before you reimport it. To search for a deleted host, you
must have the `Global Owner` role.

To locate and restore a deleted host:

1. Navigate to the Deployment view.
#. From the More menu, click Deleted Hosts.
#. Select the trash-alt to restore the host.

After the host is restored, you can
import existing process procedure.

**Note:**

If your host does not appear in the Deleted Hosts list,
you can
reimport the process 
immediately.

### MongoDB Agent Binaries

If you stop using Ops Manager to manage a deployment and completely 
remove the deployment from Ops Manager, Ops Manager deletes the 
binaries under the MongoDB Agent's `/bin` directory.

## Prerequisites

This tutorial explains how to stop Ops Manager Automation from managing your
deployment. You may need to complete some additional tasks before you 
remove your deployment from Ops Manager Automation. The following table 
highlights which actions you need to take before starting this 
tutorial.

| If you want to... | You first need to... |
|---|---|
| Stop monitoring a deployment | Stop backing up the deployment |
| Terminate a deployment | Shut down the deployment |
| Stop Ops Manager from managing a Sharded Cluster | Shut down any `mongos` processes associated with a sharded cluster. The Remove from Ops Manager option is unavailable for running `mongos` processes. |

## Procedure

**Note:**

As an alternative to disabling automation for a deployment,
you can temporarily suspend
automation for that deployment. 

This is useful if you need to temporarily shut down the deployment 
for maintenance, and do not want Ops Manager to automatically start the 
deployment back up until you are ready.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click the ... ellipsis icon next to the desired deployment.**

**Step 3: Select Remove from Ops Manager.**

**Step 4: Choose to stop managing and/or monitoring the deployment.**

Select one of the following:

|  |  |
|---|---|
| Unmanage this item in Ops Manager but continue to monitor | Removes the process from management only. You can no longer control the process through Ops Manager, but Ops Manager continues to display its status and track its metrics. |
| Completely remove from Ops Manager | Removes the processes from both management and monitoring. Ops Manager no longer displays the process. |

**Step 5: Confirm that you want automation and/or monitoring disabled for the deployment.**

a. Click Remove.

   Deployment stands in for the deployment being
   removed: Sharded Cluster, Replica Set or
   Standalone

b. If prompted for a verification code, enter the code and then
   click Remove again. 

**Step 6: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.
