<!-- Converted from tutorial/rotate-master-kmip-keys.txt (reStructuredText). Includes are inlined. -->

# Rotate Master KMIP Keys

Most regulatory requirements mandate that a managed key used to decrypt
sensitive data must be rotated out and replaced with a new key once a
year. Ops Manager provides the option to rotate the master KMIP key.

**Important:**

Setting `kmipKeyIdentifier` in the
deployment's advanced options
disables the Rotate the KMIP Master Key option.
To use this procedure, first clear `kmipKeyIdentifier`
from the deployment's advanced options or rotate the key manually.

## Procedure

**Step 1: Navigate to the Processes tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click Processes in the sidebar.

**Step 2: Find the deployment for which you wish to rotate the key.**

**Step 3: Rotate the KMIP Master key.**

In the card for the deployment:

a. Click `ellipsis`
b. Select Rotate the KMIP Master Key.
c. Click Rotate Key.

**Step 4: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.
