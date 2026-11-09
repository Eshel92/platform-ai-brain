<!-- Converted from tutorial/convert-standalone-to-replica-set.txt (reStructuredText). Includes are inlined. -->

# Convert a Standalone to a Replica Set

## Overview

Ops Manager provides the ability to convert a standalone instance to
a replica set. When converted, the replica set will have the
former standalone instance as its primary.

## Procedure

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click the ... ellipses for the process and select Convert to Replica Set.**

**Step 3: Enter the replica set name.**

Enter the replica set name and click the Convert button.

**Important:**

The replica set name is immutable once deployed. This setting 
corresponds to the `_id` replica 
configuration option.

Ops Manager displays the Editing Replica Set view.
The following steps describe the contents of each section
in that view.

**Step 4: Configure Cluster-Wide Settings**

The Replica Set Configuration section contains the 
following cluster-wide configuration settings. Settings
whose values are grey and non-interactive are immutable.

| Setting | Description |
|---|---|
| Replica Set Id | .. include:: /includes/extracts/deploy-replica-set-id.rst |
| Auth Schema Version | .. include:: /includes/extracts/deploy-replica-set-auth-schema-version.rst |
| Feature Compatibility Version | .. include:: /includes/extracts/deploy-replica-set-feature-compatibility-version.rst |
| Replica Set Settings | .. include:: /includes/extracts/deploy-replica-set-settings.rst |
| Process Name | .. include:: /includes/extracts/deploy-process-name.rst |
| Version | .. include:: /includes/extracts/deploy-version.rst |
| Data Directory | .. include:: /includes/extracts/deploy-data-directory.rst |
| Log File | .. include:: /includes/extracts/deploy-log-file.rst |

**Step 5: Configure each Replica Set Member.**

Ops Manager lists each replica set member under the
MongoD Settings heading of the
Member Configuration section. Each replica set member
has the following options:

| Setting | Description |
|---|---|
| Member | .. include:: /includes/extracts/deploy-member-configuration-member.rst |
| Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
| Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
| Votes | .. include:: /includes/extracts/deploy-member-configuration-votes.rst |
| Priority | .. include:: /includes/extracts/deploy-member-configuration-priority.rst |
| Delay | .. include:: /includes/extracts/deploy-member-configuration-delay.rst |
| Build Indexes | .. include:: /includes/extracts/deploy-member-configuration-build-indexes.rst |
| Tags | .. include:: /includes/extracts/deploy-member-configuration-tags.rst |
| Add a Mongod | .. include:: /includes/extracts/deploy-member-configuration-add-mongod.rst |

**Step 6: Configure the Replica Set Settings.**

The Replication Settings section contains the following
configuration options for the replica set:

| Setting | Description |
|---|---|
| Protocol Version | .. include:: /includes/extracts/deploy-member-replication-protocol-version.rst |
| Chaining Allowed | .. include:: /includes/extracts/deploy-member-replication-chaining-allowed.rst |
| Write Concern Majority Journal Default | .. include:: /includes/extracts/deploy-member-replication-write-concern-majority-journal-default.rst |
| Heartbeat Timeout (secs) | .. include:: /includes/extracts/deploy-member-replication-heartbeat-timeouts.rst |
| Election Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-election-timeout.rst |
| CatchUp Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-timeout.rst |
| CatchUp Takeover Delay (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-takeover-delay.rst |
| Last Error Defaults | .. include:: /includes/extracts/deploy-member-replication-last-error-defaults.rst |
| Force Reconfigure | .. include:: /includes/extracts/deploy-member-replication-force-reconfigure.rst |

**Step 7: Set any advanced configuration options for your MongoDB replica set.**

The Advanced Configuration Options section allows you to 
set MongoDB runtime options for each MongoDB process
in your deployment.

To add an option:

a. Click Add Advanced Options.

#. Click Select a Startup Option and select the
   configuration option.

#. Ops Manager displays a context-sensitive input for configuring an
   acceptable value for the selected option.

#. Click Add to add the selected option and its
   corresponding value to every process of the selected process type
   in the cluster.

Ops Manager lists each process in the cluster grouped logically. Click
the grey arrow to the left of the logical grouping to display
its sub-groupings and processes. You can modify the advanced options
for each process individually as necessary.

For descriptions of the available Advanced Configuration 
Options, see /reference/deployment-advanced-options.

**Step 8: Review the changes.**

Review the details of the replica set. When ready, click the
Save button.

**Step 9: Click Review & Deploy to review your changes.**

**Step 10: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
