<!-- Converted from tutorial/restore-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Restore a Sharded Cluster from a Snapshot

When you restore a cluster from a snapshot, Ops Manager provides you with
restore files for the selected restore point.

To learn about the restore process, see
/tutorial/nav/restore-overview.

**Important:** Changed in Ops Manager 3.6: Point-in-Time Restores

Prior to 3.6, the `Backup Daemon` created the complete point-
in-time restore on its host. With 3.6, you download a client-side
tool along with your snapshot. This tool downloads and
applies the oplog to a snapshot on your client system. This
reduces network and storage needs for your Ops Manager deployment.

**fcv42:**

**fcv40:**

## Considerations

### Review change to `BinData` BSON sub-type

The [BSON specification](http://bsonspec.org/spec.html) changed the
default subtype for the BSON binary datatype (`BinData`) from `2`
to `0`. Some binary data stored in a snapshot may be `BinData`
subtype 2. The Backup automatically detects and converts snapshot
data in `BinData` subtype 2 to `BinData` subtype 0. If your
application code expects `BinData` subtype 2, you must update your
application code to work with `BinData` subtype 0.

**See also:**

The notes on the [BSON specification](http://bsonspec.org/spec.html) explain the particular specifics
of this change.

### Restore using settings given in `restoreInfo.txt`

The backup restore file includes a metadata file named
`restoreInfo.txt`. This file captures the options the database used
when the snapshot was taken. The database must be run with the listed
options after it has been restored. This file contains:

- *Group name*

- *Replica Set name*

- *Cluster ID* (if applicable)

- *Snapshot timestamp* (as Timestamp at UTC)

- *Restore timestamp* (as a BSON Timestamp at UTC)

- *Last Oplog applied* (as a BSON Timestamp at UTC)

- *MongoDB version*

- *Storage engine type*

- mongod startup options used on the database
  when the snapshot was taken

- *Encryption*
  (Only appears if encryption is enabled on the snapshot)

- *Master Key UUID*
  (Only appears if encryption is enabled on the snapshot)

  If restoring from an encrypted backup, you must have a certificate
  provisioned for this Master Key.

### Snapshots when Agent Cannot Stop Balancer

Ops Manager displays a warning next to cluster snapshots taken while the
balancer is enabled. If you restore from such a
snapshot, you run the risk of lost or orphaned data. For more
information, see snapshot-while-balancer-enabled.

### Backup Considerations

All FCV (Feature Compatibility Version) databases must fulfill the appropriate
backup considerations.

### Encryption Considerations

To restore from an encrypted backup, you need the same master key
used to encrypt the backup and either the same certificate as is on
the `Backup Daemon` host or a new certificate provisioned 
with that key from the KMIP (Key Management Interoperability) host.

If the snapshot is encrypted, the restore panel displays the KMIP
master key id and the KMIP server information. You can also find
the information when you view the snapshot itself as well as in
the `restoreInfo.txt` file.

### Disable Client Requests to MongoDB during Restore

You must ensure that the MongoDB deployment does not receive client
requests during restoration. You must either:

- Restore to new systems with new hostnames and reconfigure your
  application code once the new deployment is running, *or*

- Ensure that the MongoDB deployment will *not* receive client
  requests while you restore data.

## Restore a Snapshot

**fcv42:**

**automatic:**

To have Ops Manager automatically restore the snapshot:

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Click the deployment, then click Restore or Download.**

**Step 3: Select the restore point.**

a. Choose the point from which you want to restore your backup.

   * - Restore Type

     - Description

     - Action

   * - Snapshot

     - Allows you to choose one stored snapshot.

     - Select an existing snapshot to restore.

   * - Point In Time

     - Creates a custom snapshot that includes all operations up to but
       not including the selected time. By default, the Oplog Store
       stores 24 hours of data.

       For example, if you select `12:00`, the last operation in the restore
       is `11:59:59` or earlier.

       **Important:**

       In FCV 4.0, you cannot perform a PIT (Point in Time) restore
       that covers any time prior to the latest backup resync. For the
       conditions that cause a resync, see
       resync-backup. This note does not apply to FCV 4.2
       or later.

     - Select a Date and Time.

   * - Oplog Timestamp

     - Creates a custom snapshot that includes all operations up to and
       including the entered Oplog timestamp. The Oplog Timestamp contains two fields:

       |  |  |
       |---|---|
       | Timestamp | Timestamp in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) |
       | Increment | Order of operation applied in that second as a 32-bit ordinal. |

     - Type an Oplog Timestamp and Increment.

       Run a query against `local.oplog.rs` on your
       replica set to find the desired timestamp.

b. Click Next.

**Step 4: Choose to restore the files to another cluster.**

a. Click Choose Cluster to Restore to.

b. Complete the following fields:

   | Field | Action |
   |---|---|
   | Project | Select a `project` to which you want to restore the snapshot. |
   | Cluster to Restore to | Select a cluster to which you want to restore the snapshot. Ops Manager *must* manage the target sharded cluster. WARNING: Automation removes all existing data from the cluster. It preserves all backup data and snapshots for the existing cluster. |

b. Click Restore.

   Ops Manager notes how much storage space the restore requires in its UI.

**Step 5: Click Restore.**

**Important:** Rotate Master Key after Restoring Snapshots Encrypted with AES256-GCM

If you restore an
encrypted snapshot that Ops Manager
encrypted with AES256-GCM (Advanced Encryption Standards 256-bit Galois/Counter Mode),
rotate your master key
after completing the restore.

**manual:**

The manual restore process assumes that:

- The target host has no data in place.
- You have not used an encrypted snapshot.
- You have not enabled two-factor authentication.

**Warning:**

Restore the snapshot manually only if you can't run an
automatic restore. If you determine that you must use
a manual restore, contact MongoDB Support
for help. This section provides a high-level overview of
the stages in the manual restore procedure.

The manual restore process has the following high-level stages that you
perform with help from MongoDB Support:

1. Connect to each replica set and the Config Server Replica Set (CSRS)
   with either the legacy `mongo` shell or `mongosh`.

2. (Optional). :v4.2:`Review the configuration file of each replica set and CSRS </tutorial/restore-sharded-cluster/#a-optional-review-replica-set-configurations>`.
   After you complete the restore process, you can reconstruct the
   configuration on the restored replica sets using the saved
   configuration files.

3. :v4.2:`Prepare the target hosts </tutorial/restore-sharded-cluster/#b-prepare-the-target-host-for-restoration>`.

   - Stop all `mongod` processes running on the target hosts.
   - Provision enough storage space to hold the restored data.
   - Prepare directories for data and logs.
   - Add a configuration file to your
     MongoDB Server directory with the target host's storage and log
     paths, and configuration for replicas and sharding roles.

4. :v4.2:`Restore the CSRS </tutorial/restore-sharded-cluster/#c-restore-config-server-replica-set>`.
5. :v4.2:`Restore each shard's replica set </tutorial/restore-sharded-cluster#d-restore-each-shard-replica-set>`.
6. :v4.2:`Restart each mongos process in the target cluster </tutorial/restore-sharded-cluster/#e-restart-each-mongos>`.
7. :v4.2:`Verify that you can connect to the cluster </tutorial/restore-sharded-cluster/#f-validate-cluster-accessibility>`.

The full manual restore procedure can be found in the
:v4.2:`MongoDB Server 4.2 </tutorial/restore-sharded-cluster/>`
documentation. For MongoDB 4.4 or later deployments, refer to the
corresponding versions of the manual.

**fcv40:**

**automatic:**

To have Ops Manager automatically restore the snapshot:

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Click the deployment, then click Restore or Download.**

**Step 3: Select the restore point.**

a. Choose the point from which you want to restore your backup.

   * - Restore Type

     - Description

     - Action

   * - Snapshot

     - Allows you to choose one
       stored snapshot.

     - Select an existing snapshot to restore.

   * - Point In Time

     - Allows you to choose a date and time as your restore time
       objective for your snapshot. By default, the
       Oplog Store stores 24 hours of data.

       **Example:**

       If you select `12:00`, the last operation in the
       restore is `11:59:59` or earlier.

       **Important:**

       - If you are restoring a sharded cluster that runs
         FCV of 4.0 or earlier, you must enable
         cluster checkpoints to
         perform a PIT (point in time) restore on a sharded cluster.

         If no checkpoints that include your date and time are
         available, Ops Manager asks you to
         choose another point in time.

       - You cannot perform a PIT (point in time) restore that covers any
         time prior to the latest backup resync. For the
         conditions that cause a resync, see
         /tutorial/resync-backup.

     - Select a Date and Time.

b. Click Next.

c. If you are restoring a sharded cluster that runs FCV of 4.0
   or earlier and you chose Point In Time:

   i.  A list of Checkpoints closest to the time you
       selected appears.

   ii. To start your point in time restore, you may:

       - Choose one of the listed checkpoints, or
       - Click Choose another point in time to remove the
         list of checkpoints and select another date and time from
         the menus.

**Step 4: Choose to restore the files to another cluster.**

a. Click Choose Cluster to Restore to.

b. Complete the following fields:

   | Field | Action |
   |---|---|
   | Project | Select a `project` to which you want to restore the snapshot. |
   | Cluster to Restore to | Select a cluster to which you want to restore the snapshot. Ops Manager *must* manage the target sharded cluster. WARNING: Automation removes all existing data from the cluster. It preserves all backup data and snapshots for the existing cluster. |

b. Click Restore.

   Ops Manager notes how much storage space the restore requires in its
   console.

**Step 5: Click Restore.**

**Important:** Rotate Master Key after Restoring Snapshots Encrypted with AES256-GCM

If you restore an
encrypted snapshot that Ops Manager
encrypted with AES256-GCM (Advanced Encryption Standards 256-bit Galois/Counter Mode),
rotate your master key
after completing the restore.

**manual:**

The manual restore process assumes that:

- The target host has no data in place.
- You have not used an encrypted snapshot.
- You have not enabled two-factor authentication.

**Warning:**

Restore the snapshot manually only if you can't run an
automatic restore. If you determine that you must use
a manual restore, contact MongoDB Support
for help. This section provides a high-level overview of
the stages in the manual restore procedure.

The manual restore process has the following high-level stages that you
perform with help from MongoDB Support:

1. Connect to each replica set and the Config Server Replica Set (CSRS)
   with either the legacy `mongo` shell or `mongosh`.

2. (Optional). :v4.0:`Review the configuration file of each replica set and CSRS </tutorial/restore-sharded-cluster/#a-optional-review-replica-set-configurations>`.
   After you complete the restore process, you can reconstruct the
   configuration on the restored replica sets using the saved
   configuration files.

3. :v4.0:`Prepare the target hosts </tutorial/restore-sharded-cluster/#b-prepare-the-target-host-for-restoration>`.

   - Stop all `mongod` processes running on the target hosts.
   - Provision enough storage space to hold the restored data.
   - Prepare directories for data and logs.
   - Add a configuration file to your
     MongoDB Server directory with the target host's storage and log
     paths, and configuration for replicas and sharding roles.

4. :v4.0:`Restore the CSRS </tutorial/restore-sharded-cluster/#c-restore-config-server-replica-set>`.
5. :v4.0:`Restore each shard's replica set </tutorial/restore-sharded-cluster#d-restore-each-shard-replica-set>`.
6. :v4.0:`Restart each mongos process in the target cluster </tutorial/restore-sharded-cluster/#e-restart-each-mongos>`.
7. :v4.0:`Verify that you can connect to the cluster </tutorial/restore-sharded-cluster/#f-validate-cluster-accessibility>`.

The full manual restore procedure can be found in the
:v4.0:`MongoDB Server documentation </tutorial/restore-sharded-cluster/>`.
