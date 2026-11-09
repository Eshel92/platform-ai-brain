<!-- Converted from tutorial/enable-backup.txt (reStructuredText). Includes are inlined. -->

# Back up a Deployment

You can back up your MongoDB deployment.

**Important:**

Sharded clusters and replica sets are the only deployment types you can back up if
your databases run MongoDB FCV 4.2 and earlier. To back up a
standalone mongod process
running MongoDB FCV 4.2 or earlier, you must
convert it to a single-member replica set.

**fcv42:**

**fcv40:**

## Prerequisites

### Unique Names for Deployment Items

Ensure your deployment items have unique names before creating backups.

**Important:**

Replica set, sharded cluster, and shard names within the same
project must be unique. Failure to have unique names for the
deployments will result in broken backup snapshots.

### Replica Set Requirements

A Replica Set must:

**fcv42:**

**fcv42:**

- Be monitored by Ops Manager.
- Run MongoDB Enterprise with an FCV (Feature Compatibility Version) of 4.2 or later.
- Have an active primary node.
- Have one node with WiredTiger set as its
  storage engine. 

### Sharded Cluster Requirements

A Sharded Cluster must:

**fcv42:**

**fcv42:**

- Be monitored by Ops Manager.
- Run MongoDB Enterprise with an FCV (Feature Compatibility Version) of 4.2 or later on all nodes
  including the config server. 
- Have an active primary node of each shard and the
  config server.
- Have one node per shard or config server with WiredTiger set as its storage engine.

### MongoDB Compatibility

All FCV (Feature Compatibility Version) 4.2 and later databases must fulfill the appropriate
backup considerations.

### MongoDB Compatibility

The MongoDB version and Ops Manager version must meet the
compatibility requirements.

### Data Protection Plan

Decide how to back up the data and what data to back up.

## Procedure

**fcv42:**

You can back up your entire MongoDB deployment.

**Note:**

We recommend that you review the amount of data that you are backing up
to the blockstore. If the amount of data that you back up negatively 
affects the performance of the blockstore or if you can't meet your
RTO (Recovery Time Objective) requirements with a single
blockstore, distribute the workload across multiple blockstores to
balance the backup operations. You can even configure a single
blockstore per shard to meet your scaling needs. 

You can create additional blockstores any time and configure your backup
jobs to use the blockstores manually: 

- To learn more about allocating specific blockstores to a project, see
  admin-manage-backup-resources. 
- To learn more about configuring shard backups to use specific
  blockstores, see manual-blockstore-maintenance.

**Step 1: Click Continuous Backup.**

If you have not yet enabled Ops Manager Backup, click
Begin Setup and complete the wizard. This results in a
completed backup setup, so you can skip the rest of this procedure.

**Step 2: Start backing up the process.**

From the list of processes, navigate to the Status column
for the process you want to back up and click Start.

**Step 3: Set Authentication Mechanisms.**

If Automation doesn't manage your deployment and your deployment
requires authentication, specify the authentication mechanism and
credentials.

Specify the following, as appropriate:

* - Auth Mechanism

  - The authentication mechanism
    that the MongoDB host uses.

    MongoDB Community options include:

    - Username/Password

    - X.509 Client Certificate

    MongoDB Enterprise options also include:

    - Kerberos
    - LDAP

* - DB Username

  - For `Username/Password` or `LDAP` authentication, the
    username used to authenticate the MongoDB Agent with the MongoDB
    deployment.

    See
    /tutorial/configure-mongodb-agent-for-scram or
    /tutorial/configure-mongodb-agent-for-ldap.

* - DB Password

  - For `Username/Password` or `LDAP` authentication, the
    password used to authenticate the MongoDB Agent with the MongoDB
    deployment.

* - Allows TLS for connections

  - If checked, Backup uses TLS (Transport Layer Security) to connect to MongoDB.

    See /tutorial/configure-mongodb-agent-for-tls.

**Step 4: (Conditional) Assign Deployment Regions for Regional Backup.**

If you want to enable regional-backup for your replica set
or sharded cluster, assign deployment regions. For a sharded cluster, you must assign
a deployment region for every sharded cluster member, including every
shard and config server.   

To start a single or multi-region backup: 

a. Select Turn on Multi-Region Backups checkbox.
#. Select the deployment region from the dropdown. 

   If you want to set the same deployment region for every member
   of the sharded cluster, click Set. Alternatively,
   select a different region from the dropdown for each sharded
   cluster member. 

**Step 5: Click Start.**

If you enabled regional backup for your sharded cluster, click
Start for each shard separately to initiate distinct backup
jobs for each. If you initiate a single backup job at the level of the
sharded cluster, Ops Manager can't guarantee regional data isolation.

**fcv40:**

You can choose to back up all databases and collections in your
MongoDB deployment or specific ones.

**Note:**

We recommend that you review the amount of data that you are backing up
to the blockstore. If the amount of data that you back up negatively 
affects the performance of the blockstore or if you can't meet your
RTO (Recovery Time Objective) requirements with a single
blockstore, distribute the workload across multiple blockstores to
balance the backup operations. You can even configure a single
blockstore per shard to meet your scaling needs. 

You can create additional blockstores any time and configure your backup
jobs to use the blockstores manually: 

- To learn more about allocating specific blockstores to a project, see
  admin-manage-backup-resources. 
- To learn more about configuring shard backups to use specific
  blockstores, see manual-blockstore-maintenance.

**Step 1: Click Continuous Backup.**

If you have not yet enabled Ops Manager Backup, click
Begin Setup and complete the wizard. This results in a
completed backup setup, so you can skip the rest of this procedure.

**Step 2: Start backing up the process.**

From the list of processes, navigate to the Status column
for the process you want to back up and click Start.

**Step 3: In the Start Backup sidebar, configure the backup source and storage engine.**

* - Menu
  - Possible Values
  - Default Value

* - Sync source

  - - *Any* secondary (Ops Manager chooses)

    - Any specific secondary

    - The primary node

  - `any secondary`

    Using a secondary is preferred because it minimizes
    performance impact on the primary.

* - Storage Engine

  - - MongoDB Memory Mapped Files or

    - WiredTiger.

      If you select this option, Ops Manager limits backups to
      deployments with fewer than 100,000 files. Files includes
      collections and indexes.

    See the considerations in Storage Engines.

  - Same storage engine as the primary node of the database being
    backed up.

If the storage engine is WiredTiger, you can enable
encryption. To enable encryption, select Enable
Encryption. Select only if you have set up KMIP server for your backups and configured the
project to use KMIP.

**Step 4: Set Authentication Mechanisms.**

If Automation doesn't manage your deployment and your deployment
requires authentication, specify the authentication mechanism and
credentials.

Specify the following, as appropriate:

* - Auth Mechanism

  - The authentication mechanism
    that the MongoDB host uses.

    MongoDB Community options include:

    - Username/Password

    - X.509 Client Certificate

    MongoDB Enterprise options also include:

    - Kerberos
    - LDAP

* - DB Username

  - For `Username/Password` or `LDAP` authentication, the
    username used to authenticate the MongoDB Agent with the MongoDB
    deployment.

    See
    /tutorial/configure-mongodb-agent-for-scram or
    /tutorial/configure-mongodb-agent-for-ldap.

* - DB Password

  - For `Username/Password` or `LDAP` authentication, the
    password used to authenticate the MongoDB Agent with the MongoDB
    deployment.

* - Allows TLS for connections

  - If checked, Backup uses TLS (Transport Layer Security) to connect to MongoDB.

    See /tutorial/configure-mongodb-agent-for-tls.

**Step 5: To filter which namespaces get backed up, click Advanced Settings.**

To exclude databases and collections from this backup:

a.  Click Blacklist.

b.  Enter the first database and collection in the text box. For
    collections, enter the full namespace:
    `<database>.<collection>`.

c.  To exclude additional databases or collections, click the
    Add another link then repeat the previous step.

To include only certain databases and collections for this backup:

a.  Click Access List.

b.  Enter the first database and collection in the text box. For
    collections, enter the full namespace:
    `<database>.<collection>`.

c.  To include additional databases or collections, click the
    Add another link then repeat the previous step.

**Step 6: Click Start.**
