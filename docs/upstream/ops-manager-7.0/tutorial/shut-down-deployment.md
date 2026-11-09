<!-- Converted from tutorial/shut-down-deployment.txt (reStructuredText). Includes are inlined. -->

# Shut Down MongoDB Processes

Ops Manager supports shutting down individual `mongod` and `mongos`
processes, as well as replica sets and
sharded clusters. When you shut down a
process, cluster, or replica set, Ops Manager continues to manage it.

After the process shuts down, you can
restart or
remove your processes.

**Note:** No Alert Raised if User Shuts Down a MongoDB Process

If you shut down a MongoDB process, Ops Manager doesn't trigger a
host is down (`HOST_DOWN`) alert.

## Shut Down One Entire Deployment

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Shut down the deployment.**

a. Click `ellipsis` for the deployment that you want to
   shut down.

#. Click Shutdown.

#. Click Shutdown Process to confirm.

**Step 3: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.

## Shut Down One Process in One Deployment

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Select the deployment.**

Click Modify for the deployment with the process that you
want to shut down.

Ops Manager displays the Editing page.

**Step 3: Shut down the deployment.**

a. Scroll to Member Configuration section of the page.

#. Click `ellipsis` for the process that you want to
   shut down.

#. Click Shutdown.

#. Click Shutdown Process to confirm.

**Step 4: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.
