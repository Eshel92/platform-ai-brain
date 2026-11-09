<!-- Converted from tutorial/edit-replica-set.txt (reStructuredText). Includes are inlined. -->

# Edit a Replica Set

## Overview

You can add, remove, and reconfigure members in a replica set
directly in the Ops Manager console.

**Note:**

Ops Manager restarts a node in a replica set or sharded cluster when you
change configuraton file options
for the MongoDB process running on the node. The following options trigger
a restart only for the specified changes:

- `security.clusterAuthMode`: Changing the value from `keyfile`
  to `sendKeyFile` triggers a restart. All other changes to this
  option do not.

- `net.tls.mode`: Changing the value from `disabled` to
  `allowTLS` triggers a restart. All other changes to this option
  do not.

A restarted node triggers an election if the node was the primary.
In addition, modifying the member settings
of the current primary may trigger an election.

## Procedures

### Add a Replica Set Member

You must have an existing server to which to deploy the new replica set
member. To add a member to an existing
replica set, increasing the size of the set:

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the card with the replica set, click Modify.**

**Step 3: In Member Configuration, click Add a Mongod.**

**Step 4: In Hostname, select the host that you want to add as a new member of the replica set.**

Use the following procedure to add the host if it doesn't appear
in the Hostname list:

a. In Hostname, select New Server.

   If no hosts have yet been added to the project, the
   Hostname list does not appear. Click
   Install Agent instead.

b. In the Add New Server dialog, select your operating
   system and click Next.

c. Follow the
   instructions to install
   a MongoDB Agent on the new host.

**Note:**

When adding a new member to a replica set, set `Build Indexes`
to `True` if you want the member's `mongod` to build indexes.
You cannot change this value after the Automation adds the
new member to the replica set. To learn more, see
`members[n].buildIndexes`.

**Warning:**

If your replica set uses TLS (Transport Layer Security), you must create and install the
necessary TLS (Transport Layer Security) certificates on the new replica set member host first.
Then, set the TLS (Transport Layer Security) settings for the `mongod` or `mongos` process
for the new replica set member on that host. Automation does not
create and install the certificates and configure these settings
automatically. If you do not configure TLS (Transport Layer Security) on the new member,
you cannot add it to the existing TLS (Transport Layer Security)-enabled replica set. To
learn how to enable TLS (Transport Layer Security) on the new replica set member, see
/tutorial/enable-ssl-for-a-deployment.

d. In the Replica Set Configuration section, complete
   the following fields for the new member:

   |  |  |
   |---|---|
   | Auth Schema Version | Select the schema for storing the user data for your deployment. See Upgrade to SCRAM for more information. |
   | Feature Compatibility (Optional) | Select the feature compatibility set. This field appears if your deployment MongoDB version is `3.4` or later. |
   | Version | Select the MongoDB version for your replica set. Ops Manager lists only the MongoDB versions that are available for your deployment. To disable this filtering, see `automation.versions.download.baseUrl.allowOnlyAvailableBuilds`. |
   | Data Directory | Specify the full path of the directory where the `mongod` process will store data files. |
   | Log File | Specify the location and name of the log file for the `mongod` process on the new host. |

**Step 5: Click Save.**

**Step 6: Click Review & Deploy to review your changes.**

**Step 7: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Important:**

To avoid disrupting majority writes, new members are now
added to replica sets as `priority=0`,
`votes=0` until they reach secondary state, after which Ops Manager
automatically updates the configuration to match the
priority
and votes value
specified in the deployment.

### Edit a Replica Set Member

To reconfigure a member as an arbiter,
see replace-member-with-arbiter

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the card with the replica set, click Modify.**

**Step 3: In Member Configuration, modify the settings for the replica set member that you want to edit.**

You can modify the following settings:

|  |  |
|---|---|
| Votes | Specify whether the replica set member votes in elections. A value of `1` indicates the member votes, while a value of `0` indicates that the member does not vote. |
| Priority | Specify the priority of the replica set member during elections. Non-voting members must have a priority of `0`. |
| Delay | Specify whether the member is a delayed replica set member. |
| Build Indexes | Specify whether the replica set member builds indexes. |
| Tags | Enter JSON that defines the tag set that you want to add to the replica set member. |

**Note:**

After deploying the replica set, you can't modify a replica set 
member's hostname or `port`.

**Step 4: Click Save.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

### Replace a Member with an Arbiter

You cannot directly reconfigure a member as an arbiter. Instead, you must must
add a new member to the replica set as an arbiter. Then you must shut down an
existing secondary.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the card with the replica set, click Modify.**

**Step 3: Add a new member to the replica set.**

Select Arbiter from the Member list when you
add-member-to-rs.

**Step 4: Click Save.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 7: Remove the secondary member of the replica set member that you want to replace with the arbiter.**

**Note:**

To determine which processes are secondaries, click the Metrics
tab and select secondaries in Toggle Members.

a. Click Modify next to the replica set.

#. Select Remove from Replica Set.

#. Click Save.

**Step 8: Click Review & Deploy.**

**Step 9: Click Confirm & Deploy.**

Upon completion, Ops Manager removes the member from the replica set. Ops Manager
converts the member's mongod to a standalone
process and shuts it down.

### Remove a Replica Set Member

When you remove a member from a replica set, Ops Manager converts the
member's mongod to a standalone process and shuts it down.

When removing members, you must keep a majority of voting members active with
respect to the original number of voting members. Without a majority, the
primary replica set member steps down and the replica set becomes read-only. 
For more information on voting, see Replica Set Elections
and Replica Set High Availability in the MongoDB Manual.

Removing members might affect the ability of the replica set to acknowledge
writes, depending on the level of write concern you use. For more
information, see Write Concern in the
MongoDB manual.

To remove a member:

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the card with the replica set, click Modify.**

**Step 3: In Member Configuration, click the ellipsis next to the replica set member that you want to remove and select Remove from Replica Set.**

**Step 4: Click Remove from Replica Set to confirm.**

**Step 5: Click Save.**

**Step 6: Click Review & Deploy to review your changes.**

**Step 7: Click Confirm & Deploy.**

Upon completion, Ops Manager removes the member from the replica set. Ops Manager
converts the member's mongod to a standalone
process and shuts it down.

### Edit a Cluster Configuration

To edit a cluster configuration:

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the card with the replica set, click Modify.**

**Step 3: Configure the replica set.**

In the Replica Set Configuration section, complete the
following fields.

|  |  |
|---|---|
| Auth Schema Version | Select the schema for storing the user data for your deployment. If you are upgrading from a MongoDB version older than 3.0, MongoDB 3.0 uses a different schema for user data than previous versions. |
| Feature Compatibility (Optional) | Select the feature compatibility set. This field appears if your deployment MongoDB version is `3.4` or later. |
| Version | Select the MongoDB version for your replica set. Ops Manager lists only the MongoDB versions that are available for your deployment. To disable this filtering, see `automation.versions.download.baseUrl.allowOnlyAvailableBuilds`. |
| Log File | Specify the location and name of the log file for the `mongod` process. The location must exist on the host. |

**Step 4: Click Save.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

### Edit Replication Settings

To edit replication settings:

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the card with the replica set, click Modify.**

If you do not see the replica set, click the Processes tab, then the Topology view.

**Step 3: In Replication Settings, modify the desired replication setting.**

See [Replica Set Configuration Fields](https://www.mongodb.com/docs/manual/reference/replica-configuration/#replica-set-configuration-fields)
for descriptions of all fields and which versions of MongoDB support each field.

**Step 4: Click Save.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## Additional Information

For more information on replica set configuration options, see,
Replica Set Configuration in the
MongoDB manual.
