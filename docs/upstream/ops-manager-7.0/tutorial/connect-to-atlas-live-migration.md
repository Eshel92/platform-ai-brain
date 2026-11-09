<!-- Converted from tutorial/connect-to-atlas-live-migration.txt (reStructuredText). Includes are inlined. -->

# Connect to Atlas for Live Migration

In Stage 2 of the Live Migration workflow,
you must connect from Ops Manager to Atlas.

To connect an organization in Ops Manager to Atlas, enter
the link-token that you generated in Atlas
into the Settings page of your Ops Manager organization.

Use one link-token per Ops Manager organization. If you have
other organizations in Ops Manager that contain deployments you want to
migrate, create a link-token in Atlas for each organization
and then specify it in the corresponding organization's settings.
You can run Live Migration processes in parallel for each
Ops Manager organization connected to Atlas.
For each organization, you can use the same link-token to live
migrate that organization's deployments from Ops Manager to Atlas,
one at a time.

## Prerequisites

Before you connect to Atlas:

- Review the workflow for Live Migration to Atlas.
- Complete Stage 1: Generate a link-token in Atlas.
- If you are migrating from Ops Manager, verify that you specified an
  external IP address of the Ops Manager instance to Atlas.
  To learn more, see Prerequisites for Live Migration.

## Procedure

**Step 1: Navigate to the Settings page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click the Organization Settings icon next to the
   Organizations menu.

**Step 2: Connect to Atlas.**

In the Organization Settings, the General Settings
tab displays the configurable settings for the organization.

a. Click the General Settings tab.

#. In the Live Migration: Connect to Atlas section,
   click Connect to Atlas. The Connect to Atlas
   dialog opens.

#. Paste the link-token that you copied from Atlas.
   The link-token contains details of your connection to Atlas.

#. Click Connect to Atlas.

**See also:**

- migrate-to-atlas
- provision-migration-host

## Next Steps

Once you connect to Atlas, you can
provision a migration host.
