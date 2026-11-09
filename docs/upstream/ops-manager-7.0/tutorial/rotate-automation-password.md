<!-- Converted from tutorial/rotate-automation-password.txt (reStructuredText). Includes are inlined. -->

# Rotate Automation Password

We recommend that you rotate the automation user's password 
periodically. Ops Manager provides an automated procedure for password 
rotation with no downtime.

## Prerequisites

To enable password rotation for the automation user, you must meet the 
following requirement:

- SCRAM-SHA-1 or SCRAM-SHA-256 set up as a supported authentication 
  mechanism for the Automation.

## Procedure

**Step 1: Navigate to the MongoDB Users tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Users.

**Step 2: On the line for the automation user, click Rotate Password.**

**Step 3: Click Review & Deploy to review your changes.**

**Step 4: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
