<!-- Converted from tutorial/add-shard-using-automation.txt (reStructuredText). Includes are inlined. -->

# Add a Shard to a MongoDB Cluster

You can use Ops Manager to add a shard to a MongoDB sharded cluster. 

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Click Modify on the cluster where you want to add a shard.**

**Step 3: In the Member Configuration section, add a shard.**

a. Expand SHARD SETTINGS.

b. Click Add a Shard to add `mongod` processes 
   to the shard.

   To add additional `mongod` processes to the shard, 
   click the Add a Mongod link.

**Step 4: Review and update settings for the new shard as needed:**

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

**Step 5: Click Save to add the new shard to the cluster.**

If you enable multi-region backups, this sharded cluster initializes in a 
Misconfigured state, indicated in the Continuous Backup 
dashboard. While the cluster is in the Misconfigured state,
Ops Manager won't take any new snapshots, although oplog tailing continues
uninterrupted for cluster members with assigned regions. You
must select a deployment region for 
each of the newly created shards.
