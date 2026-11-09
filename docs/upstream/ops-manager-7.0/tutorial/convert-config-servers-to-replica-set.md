<!-- Converted from tutorial/convert-config-servers-to-replica-set.txt (reStructuredText). Includes are inlined. -->

# Convert Config Servers to a Replica Set

**Important:** Deprecation notice

This procedure was deprecated as of 15 August 2019. It is no
longer supported.

In a sharded cluster, config servers store the
metadata for the sharded cluster. For a
sharded cluster to be fully operational, the config servers must be
available and the metadata must be consistent across the config
servers.

Config servers that run the WiredTiger storage engine can be
deployed as replica sets. Running config servers as replica sets
improves consistency and increases availability for the config
servers. Ops Manager automatically deploys config servers as replica sets
for all new sharded cluster deployments using
MongoDB 3.2 or later.
However, you must must convert config servers to replica sets for
existing MongoDB 3.2 sharded cluster deployments before you can
upgrade. You can manage config server replica sets just as you would
any other replica set.

**Note:** Feature Availability

- For deployments running MongoDB 3.2.4 or Later.
- Requires Ops Manager version 2.0.3 or greater.

**Warning:**

If you have backup enabled and if you convert a sharded cluster's
config servers to a replica set, then Ops Manager Automation can no longer
use snapshots created before the conversion to restore the sharded
cluster. Automation can only use snapshots created after the
conversion.

## Prerequisites

- .. include:: /includes/extracts/csrs-conversion-cloud-services-version-prereq.rst

- MongoDB 3.2.4 or Later
    To convert the config servers to a replica set, the sharded cluster
    must be running MongoDB 3.2.4 or later. To upgrade the
    MongoDB version, see /tutorial/change-mongodb-version.

- Three Config Servers to Convert
    The sharded cluster must be running exactly three config servers to
    convert. After the conversion of the config servers to a replica
    set, you can add additional members to the config server replica
    set.

- Write Permission for Parent Directory of `dbPath`
    The Automation must have write permission on the **parent**
    directory of the `dbPath` of each config server.

## Procedure

**Note:**

During the conversion of the config servers to a replica set,

- If the config servers use the MMAPv1 storage engine, Ops Manager
  changes the storage engine to
  WiredTiger.

- The MongoDB Agent creates temporary config servers as part of the
  conversion process and deletes them after the conversion. If your
  MongoDB Agent detects them at any point during the
  conversion, they appear as unreachable hosts in your
  deployments list. After the conversion, you can safely delete them
  from the list. See /tutorial/unmanage-deployment.

**Step 1: If you have not upgraded your sharded cluster to MongoDB 3.2.4 or later, do so now.**

See /tutorial/change-mongodb-version.

**Step 2: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 3: Click the ellipsis icon next to a config server and select Convert Config Servers to Replica Sets.**

**Step 4: Enter a name for the new replica set.**

**Step 5: Enter the ports for the temporary config servers created during the conversion and click Upgrade.**

During conversion, the Automation creates temporary config servers.
These temporary config servers must be network accessible from all
nodes in the cluster. During the procedure, specify
distinct available ports for these temporary config servers.

**Step 6: Click Save.**

**Step 7: Click Review & Deploy.**

**Step 8: Click Confirm & Deploy.**
