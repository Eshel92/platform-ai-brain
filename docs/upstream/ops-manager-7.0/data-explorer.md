<!-- Converted from data-explorer.txt (reStructuredText). Includes are inlined. -->

# Interact with Your Data

You can use the Ops Manager UI to interact with data in the following ways:

- View databases, collections, and indexes in your cluster.

- Create and drop databases, collections, and indexes.

- Insert/edit/delete documents.

- Create and run aggregation pipelines to process your data.

## Ops Manager UI Read Behavior

The Ops Manager UI reads from the primary unless the primary is
unavailable. If the primary is unavailable, the Ops Manager UI
reads from a non-hidden, non-delayed secondary member.

The Ops Manager UI uses the Automation to retrieve all data. No Ops Manager
configuration changes are required to access data in the Ops Manager UI.

## Disable Ops Manager UI Data Interaction

To interact with your data in the Ops Manager UI, you have the 
Data Explorer setting enabled. The 
Data Explorer setting is enabled by default.

**Important:** Required Privileges

To enable or disable the Data Explorer setting for a 
project, you must have the `Project Owner`  role for the 
project or the `Organization Owner` role on its parent 
organization.

To disable the Data Explorer setting:

**Step 1: Go to your Project Settings.**

Click Settings in the left navigation.

**Step 2: Set the Data Explorer toggle to Off.**

**Note:**

To enable the Data Explorer setting, set the toggle to 
On.

## Interact with Data in the Ops Manager UI

**Note:**

To interact with your data in the Ops Manager UI, you must have one of 
the following roles:

- `Project Owner` or
  `Organization Owner`

- `Project Data Access Admin`

- `Project Data Access Read/Write`

- `Project Data Access Read Only`

To interact with data in the Ops Manager UI:

1. Click Deployment in the left navigation.

#. Select the desired MongoDB deployment.

#. Select the Data tab.

## Manage Your Data in the Ops Manager UI

The following pages show how you can use the Ops Manager UI to manage your 
databases, collections, indexes, documents, and data
within documents:

- Manage Databases and Collections

- Manage Documents

- Manage Indexes

- Create Aggregation Pipelines
