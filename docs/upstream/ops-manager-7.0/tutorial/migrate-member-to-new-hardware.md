<!-- Converted from tutorial/migrate-member-to-new-hardware.txt (reStructuredText). Includes are inlined. -->

# Migrate a Replica Set Member to a New Server

## Overview

You can replace one member of a managed replica set with another member
from the Ops Manager console. Use this process to migrate members of replica sets to
new underlying servers. This procedure requires that you:

1. Provision the new server.

2. Add an extra member to the replica set.

3. Shut down old member of the replica set.

4. Un-manage the old member (Optional).

## Considerations

### Initial Sync

When you add a new replica set member, the member must perform an
`initial sync`, which takes time to complete, depending on the
size of your data set. For more information on initial sync, see
Replica Set Data Synchronization.

### Migrating Multiple Members

You can remove or migrate multiple replica set members at once, but a majority of the
voting members must remain. If you need to remove more voting members, remove
them one at a time.

**Example:** Example 1

You have a four-node replica set. All nodes are voting members. You can
remove only one node, which preserves the majority of three out of four
voting nodes. You can remove another node from the remaining 
three-node replica set afterward. This preserves the majority of the 
remaining voting nodes.

**Example:** Example 2

You have a four-node replica set. Three nodes are voting members and 
one node is a non-voting member. You can remove one voting member 
and one non-voting member at the same time. This preserves the 
majority of two out of three voting nodes.

To learn more about voting, see Replica Set High Availability and Replica Set Elections.

Removing members during migration might affect the ability of the replica set
to acknowledge writes, depending on the level of write concern you
use. For more information, see Write Concern in the MongoDB manual.

## Procedure

Perform this procedure separately for each member of a replica set to
migrate.

**Step 1: Provision the new server.**

See /tutorial/nav/add-servers.

**Step 2: Navigate to the Processes tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click Processes in the sidebar.

**Step 3: Click Modify for the replica set cluster.**

**Step 4: Add a member to the replica set.**

In the Member Configuration section, click
Add a Mongod to add a new `mongod` member.

Ops Manager displays the following configuration settings for the
`mongod`:

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

Ensure you select the Hostname that corresponds to the
newly provisioned server.

**Step 5: Configure the new `mongod` process.**

From the Replica Set Configuration section, view the
table under the Replica Set Settings heading. The
Process Name column lists the hostname and port of each
replica set member set. Ops Manager initially groups the processes under
the replica set name. Click the caret-right icon to the left
of the replica set name to list all members associated to the replica
set.

Configure the following settings for the
Process Name that corresponds to the newly added member:

| Setting | Description |
|---|---|
| Version | .. include:: /includes/extracts/deploy-version.rst |
| Data Directory | .. include:: /includes/extracts/deploy-data-directory.rst |
| Log File | .. include:: /includes/extracts/deploy-log-file.rst |

**Step 6: Click Apply.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 9: Verify that the new member has synchronized.**

On the Deployment page, click the name of the replica
set to open the cluster view. Verify that the
status for each
new member is no longer in the `Recovering` state.

**Step 10: Remove the old member from the replica set.**

1. From the Deployment view, click Modify. 
#. Navigate to the Member Configuration section.
#. Click the ellipsis-h ellipses button for the member you want 
   to remove.
#. From the menu, select Remove from Replica Set.

**Important:**

Removing the primary replica set member triggers
an election. The
replica set cannot process write operations until the election
completes. For complete documentation on replica set elections,
see Replica Set Elections.

Click Save to return to the Deployment
screen. 

Click Review Changes and then click
Confirm & Deploy. Ops Manager converts the removed
replica set member to a standalone cluster visible in the
Deployment view.

**Step 11: Shut down the old member.**

From the Deployment view, click the standalone's ellipsis 
icon and select Shutdown. Click Review Changes 
and then click Confirm & Deploy.

**Step 11: Remove the old member.**

To remove the member from Ops Manager management, click the
ellipsis-h ellipsis icon and select 
Remove from Ops Manager.

Ops Manager does not automatically shut down a process removed from
management. If you did not shut down the process in the previous
step, you must do so manually by connecting directly to the host
machine.

For complete documentation on removing processes from Ops Manager 
management, see /tutorial/unmanage-deployment.
