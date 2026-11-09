<!-- Converted from tutorial/convert-replica-set-to-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Convert a Replica Set to a Sharded Cluster

Ops Manager provides the ability to convert a replica set to
a sharded cluster.

**Note:**

You can't convert a replica set to a sharded cluster in a Kubernetes
environment.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Convert your desired replica set.**

From the ellipsis-h menu on the desired replica set,
click Convert to Sharded Cluster.

**Step 3: Provide Details for your New Sharded Cluster.**

Configure the following settings in the 
Provide details for your new sharded cluster
modal:

a. Name your sharded cluster components:

   | Field | Action |
   |---|---|
   | Cluster Name | Type the name of your new cluster. |
   | CSRS Name (MongoDB 3.2 or later) | Type the name of the CSRS (Config Server Replica Set). |

   **Note:**

   You cannot change these values after you click
   Convert.

b. Set the following values for each `mongod` process
   in your Config Servers. All fields are required.

   **Note:**

   You must deploy at least one configuration server.

   | Field | Action |
   |---|---|
   | Host Name | From the menu, select an existing hostname or type a hostname in the search box above the list to find a host. If you need to add a new host: 1. Click the New Server link. #. Click Next. #. Follow the instructions to install a new Automation on that new host. #. Click Verify Agent. |
   | Port | Type the IANA (Internet Assigned Numbers Authority) port number. |
   | Data Directory | Type the absolute directory path to the database files for each `mongod`. The example path is `/data`. The `mongod` must have exclusive use of these paths on the specified host. The Ops Manager Automation must have file system permission to read, write, and execute all files and folders in this directory. |
   | Log File | Type the absolute file path for the log file for each `mongod`. The example path is `/data/mongodb.log`. The `mongod` must have exclusive use of these paths on the specified host. The Ops Manager Automation must have file system permission to read, write, and execute all files and folders in this directory. |

   **Note:** Adding or Removing Config Servers

   - To add a new configuration server, click 
     Add a Config Server.
   - To remove a config server, click trash-alt to the right
     of the config server you want to remove.

c. Set the following values for each MongoS process in
   your sharded cluster. All fields are required.

   **Note:**

   You must deploy at least one `mongos`.

   | Field | Action |
   |---|---|
   | Host Name | From the menu, select an existing hostname or type a hostname in the search box above the list to find a host. If you need to add a new host: 1. Click the New Server link. #. Click Next. #. Follow the instructions to install a new Automation on that new host. #. Click Verify Agent. |
   | Port | Type the IANA (Internet Assigned Numbers Authority) port number. |
   | Log File | Type the abolute file path for the log of each `mongos` process. The example path is `/data/mongodb.log`. The `mongos` must have exclusive use of these paths on the specified host. The Ops Manager Automation must have file system permission to read, write, and execute all files and folders in this directory. |

   **Note:** Adding or Removing Mongo Shard Routers

   - To add a new `mongos`, click 
     Add a MongoS.
   - To remove a `mongos`, click trash-alt
     to the right of the `mongos` you want to remove.

**Step 4: Click Convert.**

**Step 5: Modify your Application to Connect to the `mongos` Processes Instead of the Replica Set.**

From the Ops Manager UI, click the ellipsis-h icon, then
click Connect to this instance. The 
Connect to your Deployment dialog provides the hostname
and port of a `mongos` in the cluster.

For complete documentation on connecting to an Ops Manager deployment,
see /tutorial/connect-to-mongodb

**Step 6: Change any Cluster-Wide Settings.**

If you want to make any further changes to the
sharded cluster, see the Sharded Cluster tab on
the /tutorial/edit-deployment page.

After you convert a replica set to a sharded cluster, you can enable
sharding for a database and shard collections.

To learn how to shard collections, see Shard a Collection.

If you need to add additional shards to support greater capacity, click
on the wrench menu for the sharded cluster to create additional shards.

**Note:** Effects on Backup after Converting

The converted shard (original replica set) has:

- Backup enabled
- Previous snapshots retained
- Ability to restore snapshots to this shard only

After converting, you should
enable Backup for the entire
sharded cluster. On databases running MongoDB
FCV
4.0 or earlier, activating Backup causes Ops Manager to start an initial
sync on the config servers and the converted shard. Restores to the
entire sharded cluster should use snapshots taken after conversion
only.

If you enabled deployment-regions-interface for the replica
set, you must select a deployment region for the new config server.
Until you select a region, the sharded cluster is in
Misconfigured state. To learn more, see
deployment-regions-assign.
