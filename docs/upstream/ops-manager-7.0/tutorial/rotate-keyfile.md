<!-- Converted from tutorial/rotate-keyfile.txt (reStructuredText). Includes are inlined. -->

# Rotate Keyfile

If your cluster uses keyfile authentication,
it is recommended that you rotate the keyfile periodically. Ops Manager
provides an automated procedure for keyfile rotation with no downtime.

To rotate the keyfile using the API instead of the user interface, see rotate-key-api-tutorial.

## Prerequisites

To perform a rolling keyfile rotation:

- Authentication must be enabled.
- At least one cluster in the project must be configured with the
  clusterAuthMode
  option set to `keyFile` or `sendKeyFile`.
- All clusters in the project must be running MongoDB version 4.2 or
  higher.

## Procedure

**Step 1: Navigate to the Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.

#. Click the Settings tab.

**Step 2: Click Rotate Keyfile.**

**Step 3: Review your changes.**

a. Click Review & Deploy.
#. The modal window contains a summary of the keyfile rotation
   procedure. If it all looks correct, click
   Confirm & Deploy.
