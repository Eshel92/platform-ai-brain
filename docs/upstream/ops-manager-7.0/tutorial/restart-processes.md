<!-- Converted from tutorial/restart-processes.txt (reStructuredText). Includes are inlined. -->

# Restart Processes

You can restart a running sharded cluster, replica set,
or standalone process directly from the Ops Manager console. Instead of restarting
an entire deployment, you can also restart individual Ops Manager-managed 
MongoDB member processes of a deployment.

**Note:**

If Ops Manager Automation manages a `mongos` process and that process
remains unreachable for 30 days, Ops Manager removes that process from the
Deployment tab view. If you restart the `mongos`
process, Ops Manager detects it again. To learn more, see the
host is down (`HOST_DOWN`) alert.

## Restart One Entire Deployment

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Restart the deployment.**

a. Click the ellipsis icon [ ellipsis-h] 
   for the deployment that you want to restart.

#. Click Restart.

#. Click Confirm.

**Note:**

If you are restarting a running deployment,  
Ops Manager restarts the deployment after the next publish.
Deployments with multiple members remain available as Ops Manager 
performs a rolling restart. During an Ops Manager rolling restart,
several processes can go offline at once, but the majority of
processes remain available.

**Step 3: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.

## Restart One Process in One Deployment

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Restart the process in your deployment.**

a. Click on the name of the deployment.

#. Click the Actions dropdown next to the 
   member process that you want to restart. 

#. Click Restart.

#. Click Confirm.

**Step 3: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.
