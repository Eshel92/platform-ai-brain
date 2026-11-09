<!-- Converted from tutorial/trigger-resync.txt (reStructuredText). Includes are inlined. -->

# Trigger an Initial Sync for One Process

Use Ops Manager Automation to start an initial sync process on one or
more MongoDB instances. This resynchronizes data stored on MongoDB nodes
in clusters.

## Considerations

- You can only resync secondary nodes.

  A node might become the primary between the time when you trigger a resync
  and when it runs. In this case, the MongoDB Agent waits for
  you to connect to the node manually and run the
  `rs.stepDown` command.

- You can only schedule one node in any given replica set to resync at
  a given time. While one node resyncs, the Ops Manager disables the
  Resync option for all other nodes.

## Trigger Initial Sync

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Choose a cluster with a node you want to resync.**

Click the name of the deployment that contains the process to
resync. Ops Manager opens the deployment Overview.

**Step 3: Choose a node to resync.**

a. Find the node that you want to resync.
b. Click the Actions dropdown for that node.

**Step 4: Click Resync.**

**Step 5: Click Resync to confirm.**

**Step 6: At the top of the deployment Overview, click Review & Deploy**

**Step 7: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes,
   click Cancel.

   Click Modify for the cluster to make additional changes.

**See also:**

lastResync parameter in the Ops Manager
Automation configuration for MongoDB instances.
