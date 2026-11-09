<!-- Converted from tutorial/suspend-automation.txt (reStructuredText). Includes are inlined. -->

# Suspend or Resume Automation for a Process

Ops Manager Automation enables you to configure and maintain MongoDB nodes
and clusters. You may suspend Ops Manager Automation to perform for manual
maintenance. Automation ignores the process until you re-enable
Automation's control.

## Suspend Automation for a Process

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click the name of the deployment that contains the process that you want to suspend. Ops Manager opens the deployment Overview.**

**Step 3: Click the Actions dropdown for the process that you want to suspend.**

**Step 4: Click Suspend.**

**Step 5: Click Suspend Automation to confirm.**

**Step 6: At the top of the deployment Overview, click Review & Deploy**

**Step 7: Click Confirm and Deploy.**

## Resume Automation for a Process

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click the name of the deployment that contains the process that you want to resume. Ops Manager opens the deployment Overview.**

**Step 3: Click the Actions dropdown for the process that you want to resume.**

**Step 4: Click Resume.**

**Step 5: Click Confirm.**

**Step 6: At the top of the deployment Overview, click Review & Deploy**

**Step 7: Click Confirm and Deploy.**

**Note:**

When you resume automating a process, Ops Manager:

1. Reverts any manual changes.
2. Update the process' config based on any changes that occurred
   while Automation was suspended.

## Next Steps

To remove a process from automation, see
/tutorial/unmanage-deployment.
