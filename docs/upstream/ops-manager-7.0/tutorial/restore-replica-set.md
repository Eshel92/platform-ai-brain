<!-- Converted from tutorial/restore-replica-set.txt (reStructuredText). Includes are inlined. -->

# Restore a Replica Set from a Snapshot

When you restore a replica set from backup, Ops Manager provides you with a
restore file for the selected restore point. To learn about the
restore process, please see /tutorial/nav/restore-overview.

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

### Backup Considerations

All FCV (Feature Compatibility Version) databases must fulfill the appropriate
backup considerations.

## Prerequisites

To perform manual restores, you must have the
Backup Admin role in Ops Manager.

To restore from an encrypted backup, you need the same master key
used to encrypt the backup and either the same certificate as is on
the `Backup Daemon` host or a new certificate provisioned 
with that key from the KMIP (Key Management Interoperability) host.

If the snapshot is encrypted, the restore panel displays the KMIP
master key id and the KMIP server information. You can also find
the information when you view the snapshot itself as well as in
the `restoreInfo.txt` file.

### Client Requests During Restoration

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
   | Cluster to Restore to | Select a cluster to which you want to restore the snapshot. Ops Manager *must* manage the target replica set. WARNING: Automation removes all existing data from the cluster. It preserves all backup data and snapshots for the existing cluster. |

b. Click Restore.

   Ops Manager notes how much storage space the restore requires.

**Step 5: Click Restore.**

**manual:**

**Warning:** Consider Automatic Restore

This procedure involves a large number steps. Some of
these steps have severe security implications. If you
don't need to restore to a deployment that Ops Manager doesn't
manage, consider an automated restore.

Retrieve the Snapshots
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	    **Step 1: Click Continuous Backup, then the Overview tab.**

	    **Step 2: Click the deployment, then click Restore or Download.**

	    **Step 3: Select the Restore Point.**

	    a. Choose the point from which you want to restore your backup.

	          :widths: 20 50 30
	          :header-rows: 1

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

	                 :widths: 30 70

	                 * - Timestamp
	                   - Timestamp in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017)

	                 * - Increment
	                   - Order of operation applied in that second as a
	                     32-bit ordinal.

	            - Type an Oplog Timestamp and Increment.

	              Run a query against `local.oplog.rs` on your
	              replica set to find the desired timestamp.

	    b. Click Next.

	    **Step 4: Click Download to Restore the Files Manually.**

	    **Step 5: Configure the snapshot download.**

	    a. Configure the following download options:

	          :widths: 30 70

	          * - Pull Restore Usage Limit
	            - Select how many times the link can be used. If you select
	              `No Limit`, the link is re-usable until it expires.

	          * - Restore Link Expiration (in hours)
	            - Select the number of hours until the link expires. The
	              default value is `1`. The maximum value is the number of
	              hours until the selected snapshot expires.

	    b. Click Finalize Request.

	    c. If you use 2FA,
	       Ops Manager prompts you for your 2FA code. Enter your 2FA code, then
	       click Finalize Request.

	    **Step 6: Retrieve the Snapshots.**

	    Ops Manager creates links to the snapshot. By default, these links are
	    available for an hour and you can use them just once.

	    To download the snapshots:

	    a. If you closed the restore panel, click Continuous Backup, then
	       Restore History.

	    b. When the restore job completes, click (get link)
	       for each replica set that appears.

	    c. Click:

	       - The copy button to the right of the link to copy the link to
	         use it later, or
	       - Download to download the snapshot immediately.

	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	    **Step 1: Unmanage the Target Replica Set.**

	    Before attempting to restore the data manually, remove the
	    replica set from Automation.

	    Choose the
	    Unmanage this item in Ops Managers but continue to 
	    monitor option.

	    **Step 2: Stop the Target Replica Set.**

	    Depending on your path, you may need to specify
	    the path to `mongosh`. Run:

	    ```sh
	    ```

	       mongosh --port <port> \
	             --eval "db.getSiblingDB('admin').shutdownServer()"

	    **Step 3: Verify Hardware and Software Requirements on the Target Replica Set.**

	       :widths: 30 70
	       :stub-columns: 1

	       * - Storage Capacity
	         - The target host's hardware needs to have sufficient free storage
	           space for storing the restored data. If you want to keep any
	           existing cluster data on this host, make sure the host
	           has sufficient free space for the cluster data and the
	           restored data.

	       * - MongoDB Version
	         - The target host on which you are restoring and the source host
	           from which you are restoring  must run the same MongoDB
	           Server version. To check the MongoDB version, run ``mongod
	           --version`` from a terminal or shell.

	    To learn more, see installation.

	    **Step 4: Move the Snapshot Data Files to the Target Host.**

	    Before you move the snapshot's data files to the target host, check
	    whether the target host contains any existing files, and delete all 
	    the files except the `automation-mongod.conf` file.

	    Unpack the snapshot files and move them to the target host as follows:

	    ```sh
	    ```

	       tar -xvf <backupSnapshot>.tar.gz
	       mv <backupSnapshot> </path/to/datafiles>

	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	    **Step 1: Start the Temporary Standalone Instance on the Ephemeral Port.**

	    Start the `mongod` process in standalone mode as a temporary measure.
	    This allows you to add new configuration parameters to the
	    `system.replset` collection in subsequent steps.

	    Use the `<ephemeralPort>` for the temporary standalone `mongod` process
	    in all steps in this procedure  where it is mentioned. This port must
	    differ from the source and target host ports.

	    Run the `mongod` process as follows. Depending on your path, you may
	    need to specify the path to the `mongod` binary.

	    ```sh
	    ```

	       mongod  --dbpath </path/to/datafiles> \
	               --port <ephemeralPort> \

	    If you are restoring
	    from a namespace-filtered snapshot, use the `--restore` option.

	    ```sh
	    ```

	       mongod --dbpath </path/to/datafiles> \
	              --port <ephemeralPort> \
	              --restore

	    After the `mongod` process starts accepting connections, continue.

	    **Step 2: Connect to the Temporary Standalone Instance with `mongosh`.**

	    From the host running this `mongod` process, start `mongosh`. Depending 
	    on your path, you may need to specify the path to `mongosh`.

	    To connect to the `mongod` listening to localhost on
	    the same `<ephemeralPort>` specified in the previous step, run:

	    ```sh
	    ```

	       mongosh  --port <ephemeralPort>

	    After `mongosh` connects to `mongod`, continue.

	    **Step 3: Remove Replica Set-Related Collections from the `local` Database.**

	    To perform manual restores, you must have the
	    Backup Admin role in Ops Manager.

	    Run the following commands to remove the previous replica set
	    configuration and other non-oplog, replication-related collections.

	    ```javascript
	    ```

	       db.getSiblingDB("local").replset.minvalid.drop()
	       db.getSiblingDB("local").replset.oplogTruncateAfterPoint.drop()
	       db.getSiblingDB("local").replset.election.drop()
	       db.getSiblingDB("local").system.replset.remove({})

	    A successful response should look like this:

	    ```javascript
	    ```

	       :copyable: false

	       > db.getSiblingDB("local").replset.minvalid.drop()
	       true
	       > db.getSiblingDB("local").replset.oplogTruncateAfterPoint.drop()
	       true
	       > db.getSiblingDB("local").replset.election.drop()
	       true
	       > db.getSiblingDB("local").system.replset.remove({})
	       WriteResult({ "nRemoved" : 1 })

	    **Step 4: Add a New Replica Set Configuration.**

	    Insert the following document into the `system.replset` collection
	    in the `local` database. Change the following variables:

	    - `<replaceMeWithTheReplicaSetName>` to the name of your replica set. This
	      name does not have to be the same as the old name.
	    - `<host>` to the host serving this replica set member.
	    - `<finalPortNewReplicaSet>` to the final port for the new
	      replica set. For an automated restore, you must specify a 
	      different port than the `<ephemeralPort>` that you specified 
	      previously.

	    Ensure that you include and configure all members of the new replica
	    set in the `members` array.

	    ```javascript
	    ```

	       :linenos:

	       db.getSiblingDB("local").system.replset.insertOne({
	         "_id" : "<replaceMeWithTheReplicaSetName>",
	         "version" : NumberInt(1),
	         "protocolVersion" : NumberInt(1),
	         "members" : [
	           {
	             "_id" : NumberInt(0),
	             "host" : "<host>:<finalPortNewReplicaSet>"
	           },
	           {
	             . . .
	           },
	           . . .
	         ],
	         "settings" : {

	         }
	       })

	    A successful response should look like this:

	    ```javascript
	    ```

	       :copyable: false

	       { "acknowledged" : true, "insertedId" : "<yourReplicaSetName>" }

	    **Step 5: Insert the Minimum Valid Timestamp.**

	    Issue the following command:

	    ```javascript
	    ```

	       db.getSiblingDB("local").replset.minvalid.insertOne({
	         "_id" : ObjectId(),
	         "t" : NumberLong(-1),
	         "ts" : Timestamp(0,1)
	       })

	    A successful response should look like this:

	    ```javascript
	    ```

	       :copyable: false

	       { "acknowledged" : true, "insertedId" : ObjectId("<yourObjectId>") }

	    **Step 6: Set the Restore Point to the Values in `Restore Timestamp` from `restoreInfo.txt`.**

	    Set the `oplogTruncateAfterPoint` document to the
	    values provided in the `Restore Timestamp` field of the
	    restoreInfo.txt file.

	    The `Restore Timestamp` field in that file contains two
	    values. In the following example, the first value is the
	    timestamp, and the second value is the increment.

	    ```sh
	    ```

	       :copyable: false
	       :linenos:
	       :emphasize-lines: 2

	       ...
	       Restore timestamp:  (1609947369, 2)
	       Last Oplog Applied: Wed Jan 06 15:36:09 GMT 2021 (1609947369, 1)
	       MongoDB Version: 4.2.11
	       ...

	    The following example code uses the timestamp value and increment value from the previous example.

	    ```javascript
	    ```

	       truncateAfterPoint = Timestamp(1609947369,2)
	       db.getSiblingDB("local").replset.oplogTruncateAfterPoint.insertOne({
	          "_id": "oplogTruncateAfterPoint",
	          "oplogTruncateAfterPoint": truncateAfterPoint
	       })

	    A successful response should look like this:

	    ```javascript
	    ```

	       :copyable: false

	       WriteResult({ "nInserted" : 1 })

	    **Note:** Restoring MongoDB 4.2 Snapshots using MongoDB 4.4

	       If you try to restore a MongoDB 4.2 snapshot with a `mongod`
	       running MongoDB 4.4, your oplog may contain unneeded documents.

	       To resolve this issue, you can either:

	       - Decrement the timestamp by 1.
	       - Restore using MongoDB 4.2.
	       - Have Ops Manager run an automated restore.

	       This issue doesn't apply to MongoDB 4.4 or later snapshots.

	    Manage Instances
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	    **Step 1: Stop the Temporary Standalone Instance.**

	    Depending on your path, you may need to specify
	    the path to `mongosh`. Run:

	    ```sh
	    ```

	       mongosh --port <ephemeralPort> \
	             --eval "db.getSiblingDB('admin').shutdownServer()"

	    **Step 2: Restart the Instance as an Ephemeral Replica Set Node.**

	    Start the `mongod` using the following command. This action
	    reconciles the `mongod` state with the oplog up to the ``Restore
	    timestamp``. Depending on your path, you might need to specify the
	    path to the `mongod` binary.

	    ```sh
	    ```

	       mongod  --dbpath </path/to/datafiles> \
	               --port <ephemeralPort> \
	               --replSet <replaceMeWithTheReplicaSetName>

	    **Step 3: Stop the Temporary Instance on the Ephemeral Port.**

	    Depending on your path, you may need to specify
	    the path to `mongosh`. Run:

	    ```sh
	    ```

	       mongosh --port <ephemeralPort> \
	             --eval "db.getSiblingDB('admin').shutdownServer()" 

	    Restore Point-in-Time Snapshots
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	    **Step 1: (Point-in-Time Restore Only) Run the MongoDB Backup Restore Utility.**

	    This step is conditional. Run it if you need Point-in-Time Restore.

	    In this step, you download and run the MongoDB Backup Restore Utility 
	    on the target instance for the replica set, and then stop the 
	    instance.

	    a. Download the MongoDB Backup Restore Utility to your host.

	       If you closed the restore panel, click Continuous
	       Backup in Deployment, More, and then
	       Download MongoDB Backup Restore Utility.

	    #. Start a `mongod` instance without authentication
	       enabled using the extracted snapshot directory as the data
	       directory. Depending on your path, you may need to
	       specify the path to the `mongod` binary.

	       ```sh
	       ```

	          mongod  --port <ephemeralPort> \
	                  --dbpath </path/to/datafiles> \
	                  --setParameter ttlMonitorEnabled=false \
	                  --bind_ip <hostname_or_IP>

	       **Warning:**

	          The MongoDB Backup Restore Utility doesn't support
	          authentication, so you can't start this temporary database with
	          authentication.

	    #. Run the MongoDB Backup Restore Utility on your target host.
	       Run it once for the replica set.

	       **Important:** Pre-configured `mongodb-backup-restore-util` command

	          Ops Manager provides the `mongodb-backup-restore-util` with the
	          appropriate options for your restore on the restore panel under
	          Run Binary with PIT Options.

	          You should copy the `mongodb-backup-restore-util` command
	          provided in the Ops Manager Application.

	       ```sh
	       ```

	          ./mongodb-backup-restore-util --https --host <targetHost> \
	            --port <ephemeralPort> \
	            --opStart <opLogStartTimeStamp> \
	            --opEnd <opLogEndTimeStamp> \
	            --logFile <logPath> \
	            --oplogSourceAddr <oplogSourceAddr> \
	            --apiKey <apiKey> \
	            --groupId <groupId> \
	            --rsId <rsId> \
	            --whitelist <database1.collection1, database2, etc.> \
	            --blacklist <database1.collection1, database2, etc.> \
	            --seedReplSetMember \
	            --oplogSizeMB <size> \
	            --seedTargetPort <port> \
	            --ssl \
	            --sslCAFile </path/to/ca.pem> \
	            --sslPEMKeyFile </path/to/pemkey.pem>
	            --sslClientCertificateSubject <distinguishedName> \
	            --sslRequireValidServerCertificates <true|false> \
	            --sslServerClientCertificate </path/to/client.pem> \
	            --sslServerClientCertificatePassword <password> \
	            --sslRequireValidMMSBackupServerCertificate <true|false> \
	            --sslTrustedMMSBackupServerCertificate </path/to/mms-certs.pem> \
	            --httpProxy <proxyURL>

	       The `mongodb-backup-restore-util` command uses the following
	       options:

	          :widths: 35 10 40 5
	          :header-rows: 1

	          * - Option
	            - Necessity
	            - Description
	            - check-circle

	          * - `--host`
	            - Required
	            - Provide the hostname, FQDN (fully qualified domain name), IPv4 (Internet Protocol version 4) address, or IPv6 (Internet Protocol version 6) address
	              for the host that serves the mongod to which the
	              `oplog` should be applied. If you
	              copied the `mongodb-backup-restore-util` command provided in
	              the Ops Manager Application, this field is pre-configured.
	            - check-circle

	          * - `--port`
	            - Required
	            - Provide the ephemeral port for the host that serves the `mongod` 
	              to which the `oplog` should be applied.
	            - check-circle

	          * - `--opStart`
	            - Required
	            - Provide the
	              BSON timestamp
	              for the first `oplog` entry
	              you want to include in the restore. This information appears in
	              the "Last Oplog Applied" entry in the `restoreInfo.txt` file
	              provided with the downloaded snapshot.

	              This value must be less than or equal to the `--opEnd`
	              value.

	            - check-circle

	          * - `--opEnd`
	            - Required
	            - Provide the
	              BSON timestamp
	              for the last `oplog` entry
	              you want to include in the restore.

	              This value cannot be greater than the end of the oplog.

	            - check-circle

	          * - `--logFile`
	            - Optional
	            - Provide a path, including file name, where the
	              MBRU (MongoDB Backup Restore Utility) log is
	              written.
	            -

	          * - `--oplogSourceAddr`
	            - Required
	            - Provide the URL (Uniform Resource Locator) for the Ops Manager resource endpoint.
	            - check-circle

	          * - `--apiKey`
	            - Required
	            - Provide your Ops Manager Agent
	              API Key.
	            - check-circle

	          * - `--groupId`
	            - Required
	            - Provide the `group` ID.
	            - check-circle

	          * - `--rsId`
	            - Required
	            - Provide the replica set ID.
	            - check-circle

	          * - `--whitelist`
	            - Optional
	            - Provide a list of databases and/or collections to which you
	              want to limit the restore.
	            -

	          * - `--blacklist`
	            - Optional
	            - Provide a list of databases and/or collections to which you
	              want to exclude from the restore.
	            -

	          * - `--seedReplSetMember`
	            - Optional
	            - Use if you need a replica set member to re-create the
	              `oplog` collection and seed
	              it with the correct timestamp.

	              Requires `--oplogSizeMB` and `--seedTargetPort`.
	            -

	          * - `--oplogSizeMB`
	            - Conditional
	            - Provide the `oplog` size in MB.

	              Required if `--seedReplSetMember` is set.
	            -

	          * - `--seedTargetPort`
	            - Conditional
	            - Provide the port for the replica set's
	              primary. This may be different from the [ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port?oldid=797306581)
	              used.

	              Required if `--seedReplSetMember` is set.
	            -

	          * - `--ssl`
	            - Optional
	            - Use if you need TLS (Transport Layer Security)/SSL (Secure Sockets Layer) to apply the
	              `oplog` to the `mongod`.

	              Requires `--sslCAFile` and `--sslPEMKeyFile`.
	            -

	          * - `--sslCAFile`
	            - Conditional
	            - Provide the path to the Certificate Authority file.

	              Required if `--ssl` is set.
	            -

	          * - `--sslPEMKeyFile`
	            - Conditional
	            - Provide the path to the PEM (Privacy-Enhanced Mail) certificate file.

	              Required if `--ssl` is set.
	            -

	          * - `--sslPEMKeyFilePwd`
	            - Conditional
	            - Provide the password for the PEM (Privacy-Enhanced Mail) certificate file specified
	              in `--sslPEMKeyFile`.

	              Required if `--ssl` is set and that PEM (Privacy-Enhanced Mail) key file is
	              encrypted.
	            -

	          * - `--sslClientCertificateSubject`
	            - Optional
	            - Provide the Client Certificate Subject or Distinguished Name
	              (DN) for the target MongoDB process.

	              Required if `--ssl` is set.
	            -

	          * - `--sslRequireValidServerCertificates`
	            - Optional
	            - Set a flag indicating if the tool should validate certificates
	              that the target MongoDB process presents.
	            -

	          * - `--sslServerClientCertificate`
	            - Optional
	            - Provide the absolute path to Client Certificate file to use for
	              connecting to the Ops Manager host.
	            -

	          * - `--sslServerClientCertificatePassword`
	            - Conditional
	            - Provide the absolute path to Client Certificate file password to
	              use for connecting to the Ops Manager host.

	              Required if `--sslServerClientCertificate` is set and that
	              certificate is encrypted.
	            -

	          * - `--sslRequireValidMMSBackupServerCertificate`
	            - Optional
	            - Set a flag indicating if valid certificates are required when
	              contacting the Ops Manager host. Default value is `true`.
	            -

	          * - `--sslTrustedMMSBackupServerCertificate`
	            - Optional
	            - Provide the absolute path to the trusted Certificate Authority certificates
	              in PEM (Privacy-Enhanced Mail) format for the Ops Manager host. If this flag is not
	              provided, the system Certificate Authority is used.

	              If Ops Manager is using a self-signed SSL (Secure Sockets Layer) certificate, this
	              setting is required.
	            -

	          * - `--httpProxy`
	            - Optional
	            - Provide the URL (Uniform Resource Locator) of an HTTP (Hypertext Transfer Protocol) proxy server the tool can use.
	            -

	       check-circle means that if you copied the
	       `mongodb-backup-restore-util` command provided in
	       Ops Manager Application, this field is pre-configured.

	    #. Stop the `mongod` on the instance. Depending on your path,
	       you may need to specify the path to `mongosh`. Run:

	       ```sh
	       ```

	          mongosh --port <ephemeralPort> \
	                --eval "db.getSiblingDB('admin').shutdownServer()"

	    **Step 2: (Point-in-Time Restore Only) Restart the Instance to Recover the Oplog.**

	    Start the `mongod` using the following command, specifying these
	    parameters:

	    - `<bind_ip>` to the host serving this replica set member that you
	      specified in the replica set configuration.
	    - `<port>` to the <ephemeralPort> that you
	      specified when you started the temporary standalone instance.

	    This action replays the oplog up to the latest entry, including
	    those inserted when you ran the MongoDB Backup Restore Utility.

	    ```sh
	    ```

	       mongod  --dbpath </path/to/datafiles> \
	               --port <ephemeralPort> \
	               --bind_ip <host-serving-this-replica-set-member>
	               --setParameter recoverFromOplogAsStandalone=true
	               --setParameter takeUnstableCheckpointOnShutdown=true
	               --setParameter startupRecoveryForRestore=true

	    After you complete this step, the actual restore process is completed.

	    **Step 3: (Point-in-Time Restore Only) Stop the Standalone Instance.**

	    Depending on your path, you may need to specify
	    the path to `mongosh`. Run:

	    ```sh
	    ```

	       mongosh --port <port> \
	             --eval "db.getSiblingDB('admin').shutdownServer()"

	    **Step 4: Repeat This Procedure for Each Node in the Replica Set.**

	    Resume Automation
	    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	    **Step 1: Restart All Nodes in a Replica Set.**

	    At this point, the data files in the replica set are in a consistent 
	    state, but the replica set configuration needs to be updated so that 
	    each node is aware of each other.

	    Run the following command:

	    ```sh
	    ```

	       sudo -u mongod <path/to/target_mongod_binary> -f /path/to/datafiles/automation-mongod.conf

	    The following example restarts all nodes with the version 4.4.12 
	    enterprise with the data path `/data6/node3`:

	    ```sh
	    ```

	       sudo -u mongod /var/lib/mongodb-mms-automation/mongodb-linux-x86_64-4.4.12-ent/bin/mongod -f /data6/node3/automation-mongod.conf

	    **Step 2: Reimport the Replica Set.**

	    To manage the replica set with automation again,
	    import the replica set
	    back into Ops Manager.

	    On the Deployment page, click Add, select 
	    Existing MongoDB Deployment, and proceed with adding 
	    Automation back to your cluster.

               

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

   To find the latest Oplog entry, run the following query
   in `mongosh`:

   ```javascript
   db.getSiblingDB('local').oplog.rs.find().sort({$natural:-1}).limit(1).pretty()
   ```

   A successful result should look like this:

   ```json
   {
     "ts": Timestamp(1537559320, 1),
     "h": NumberLong("-2447431566377702740"),
     "v": 2,
     "op": "n",
     "ns": "",
     "wall": ISODate("2018-09-21T19:48:40.708Z"),
     "o": {
       "msg": "initiating set"
     }
   }
   ```

   The parts of the `ts` value correspond to the values
   you need for the Timestamp and
   Increment boxes.

   **Note:**

   To translate the epoch time into a human-readable
   timestamp, try using a tool like
   [Epoch Converter](https://www.epochconverter.com/)

   MongoDB does not endorse this service. Its reference
   is intended only as informational.

   **Step 4: Choose to restore the files to another cluster.**

   a. Click Choose Cluster to Restore to.

   b. Complete the following fields:

      | Field | Action |
      |---|---|
      | Project | Select a `project` to which you want to restore the snapshot. |
      | Cluster to Restore to | Select a cluster to which you want to restore the snapshot. Ops Manager *must* manage the target replica set. WARNING: Automation removes all existing data from the cluster. It preserves all backup data and snapshots for the existing cluster. |

   b. Click Restore.

      Ops Manager notes how much storage space the restore requires.

   **Step 5: Click Restore.**

   **manual:**

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

   To find the latest Oplog entry, run the following query
   in `mongosh`:

   ```javascript
   db.getSiblingDB('local').oplog.rs.find().sort({$natural:-1}).limit(1).pretty()
   ```

   A successful result should look like this:

   ```json
   {
     "ts": Timestamp(1537559320, 1),
     "h": NumberLong("-2447431566377702740"),
     "v": 2,
     "op": "n",
     "ns": "",
     "wall": ISODate("2018-09-21T19:48:40.708Z"),
     "o": {
       "msg": "initiating set"
     }
   }
   ```

   The parts of the `ts` value correspond to the values
   you need for the Timestamp and
   Increment boxes.

   **Note:**

   To translate the epoch time into a human-readable
   timestamp, try using a tool like
   [Epoch Converter](https://www.epochconverter.com/)

   MongoDB does not endorse this service. Its reference
   is intended only as informational.

   **Step 4: Click Download to restore the files manually.**

   **Step 5: Configure the snapshot download.**

   a. Configure the following download options:

      |  |  |
      |---|---|
      | Pull Restore Usage Limit | Select how many times the link can be used. If you select `No Limit`, the link is re-usable until it expires. |
      | Restore Link Expiration (in hours) | Select the number of hours until the link expires. The default value is `1`. The maximum value is the number of hours until the selected snapshot expires. |

   b. Click Finalize Request.

   c. If you use 2FA,
      Ops Manager prompts you for your 2FA code. Enter your 2FA code, then
      click Finalize Request.

   **Step 6: Retrieve the snapshots.**

   Ops Manager creates links to the snapshot. By default, these links are
   available for an hour and can be used just once.

   To download the snapshots:

   a. If you closed the restore panel, click Continuous Backup, then
      Restore History.

   b. When the restore job completes, click (get link)
      for each replica set appears.

   c. Click:

      - The copy button to the right of the link to copy the link to
        use it later, or
      - Download to download the snapshot immediately.

   **Important:** Extra step for point-in-time restores

   For point-in-time and oplog timestamp restores, additional
   instructions are shown. The final step shows the full command
   you must run using the MBRU (MongoDB Backup Restore
   Utility). It includes all of the necessary options to ensure a
   full restore.

   Select and copy the `mongodb-backup-restore-util` command
   provided under Run Binary with PIT Options.

   **Step 7: Restore the snapshot data files to the destination host.**

   **Example:**

   ```sh
   tar -xvf <backupSnapshot>.tar.gz
   mv <backupSnapshot> <temp-database-path>
   ```

   **Step 8: Run the MongoDB Backup Restore Utility (Point-in-Time Restore Only).**

   a. Download the MongoDB Backup Restore Utility to your host.

      **Note:**

      If you closed the restore panel, click Continuous Backup, then
      More and then Download MongoDB Backup
      Restore Utility.

   #. Start a `mongod` instance without authentication
      enabled using the extracted snapshot directory as the data
      directory.

      **Example:**

      ```sh
      mongod --port <port number> \
        --dbpath <temp-database-path> \
        --setParameter ttlMonitorEnabled=false
      ```

      **Warning:**

      The MongoDB Backup Restore Utility doesn't support
      authentication, so you can't start this temporary database with
      authentication.

   #. Run the MongoDB Backup Restore Utility on your destination host.
      Run it once for the replica set.

      **Important:** Pre-configured `mongodb-backup-restore-util` command

      Ops Manager provides the `mongodb-backup-restore-util` with the
      appropriate options for your restore on the restore panel under
      Run Binary with PIT Options.

      You should copy the `mongodb-backup-restore-util` command
      provided in the Ops Manager Application.

      ```sh
      ./mongodb-backup-restore-util --https --host <targetHost> \
        --port <ephemeralPort> \
        --opStart <opLogStartTimeStamp> \
        --opEnd <opLogEndTimeStamp> \
        --logFile <logPath> \
        --oplogSourceAddr <oplogSourceAddr> \
        --apiKey <apiKey> \
        --groupId <groupId> \
        --rsId <rsId> \
        --whitelist <database1.collection1, database2, etc.> \
        --blacklist <database1.collection1, database2, etc.> \
        --seedReplSetMember \
        --oplogSizeMB <size> \
        --seedTargetPort <port> \
        --ssl \
        --sslCAFile </path/to/ca.pem> \
        --sslPEMKeyFile </path/to/pemkey.pem>
        --sslClientCertificateSubject <distinguishedName> \
        --sslRequireValidServerCertificates <true|false> \
        --sslServerClientCertificate </path/to/client.pem> \
        --sslServerClientCertificatePassword <password> \
        --sslRequireValidMMSBackupServerCertificate <true|false> \
        --sslTrustedMMSBackupServerCertificate </path/to/mms-certs.pem> \
        --httpProxy <proxyURL>
      ```

      The `mongodb-backup-restore-util` command uses the following
      options:

      | Option | Necessity | Description | check-circle |
      |---|---|---|---|
      | `--host` | Required | Provide the hostname, FQDN (fully qualified domain name), IPv4 (Internet Protocol version 4) address, or IPv6 (Internet Protocol version 6) address for the host that serves the mongod to which the `oplog` should be applied. If you copied the `mongodb-backup-restore-util` command provided in the Ops Manager Application, this field is pre-configured. | check-circle |
      | `--port` | Required | Provide the ephemeral port for the host that serves the `mongod` to which the `oplog` should be applied. | check-circle |
      | `--opStart` | Required | Provide the BSON timestamp for the first `oplog` entry you want to include in the restore. This information appears in the "Last Oplog Applied" entry in the `restoreInfo.txt` file provided with the downloaded snapshot. This value must be less than or equal to the `--opEnd` value. | check-circle |
      | `--opEnd` | Required | Provide the BSON timestamp for the last `oplog` entry you want to include in the restore. This value cannot be greater than the end of the oplog. | check-circle |
      | `--logFile` | Optional | Provide a path, including file name, where the MBRU (MongoDB Backup Restore Utility) log is written. |  |
      | `--oplogSourceAddr` | Required | Provide the URL (Uniform Resource Locator) for the Ops Manager resource endpoint. | check-circle |
      | `--apiKey` | Required | Provide your Ops Manager Agent API Key. | check-circle |
      | `--groupId` | Required | Provide the `group` ID. | check-circle |
      | `--rsId` | Required | Provide the replica set ID. | check-circle |
      | `--whitelist` | Optional | Provide a list of databases and/or collections to which you want to limit the restore. |  |
      | `--blacklist` | Optional | Provide a list of databases and/or collections to which you want to exclude from the restore. |  |
      | `--seedReplSetMember` | Optional | Use if you need a replica set member to re-create the `oplog` collection and seed it with the correct timestamp. Requires `--oplogSizeMB` and `--seedTargetPort`. |  |
      | `--oplogSizeMB` | Conditional | Provide the `oplog` size in MB. Required if `--seedReplSetMember` is set. |  |
      | `--seedTargetPort` | Conditional | Provide the port for the replica set's primary. This may be different from the [ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port?oldid=797306581) used. Required if `--seedReplSetMember` is set. |  |
      | `--ssl` | Optional | Use if you need TLS (Transport Layer Security)/SSL (Secure Sockets Layer) to apply the `oplog` to the `mongod`. Requires `--sslCAFile` and `--sslPEMKeyFile`. |  |
      | `--sslCAFile` | Conditional | Provide the path to the Certificate Authority file. Required if `--ssl` is set. |  |
      | `--sslPEMKeyFile` | Conditional | Provide the path to the PEM (Privacy-Enhanced Mail) certificate file. Required if `--ssl` is set. |  |
      | `--sslPEMKeyFilePwd` | Conditional | Provide the password for the PEM (Privacy-Enhanced Mail) certificate file specified in `--sslPEMKeyFile`. Required if `--ssl` is set and that PEM (Privacy-Enhanced Mail) key file is encrypted. |  |
      | `--sslClientCertificateSubject` | Optional | Provide the Client Certificate Subject or Distinguished Name (DN) for the target MongoDB process. Required if `--ssl` is set. |  |
      | `--sslRequireValidServerCertificates` | Optional | Set a flag indicating if the tool should validate certificates that the target MongoDB process presents. |  |
      | `--sslServerClientCertificate` | Optional | Provide the absolute path to Client Certificate file to use for connecting to the Ops Manager host. |  |
      | `--sslServerClientCertificatePassword` | Conditional | Provide the absolute path to Client Certificate file password to use for connecting to the Ops Manager host. Required if `--sslServerClientCertificate` is set and that certificate is encrypted. |  |
      | `--sslRequireValidMMSBackupServerCertificate` | Optional | Set a flag indicating if valid certificates are required when contacting the Ops Manager host. Default value is `true`. |  |
      | `--sslTrustedMMSBackupServerCertificate` | Optional | Provide the absolute path to the trusted Certificate Authority certificates in PEM (Privacy-Enhanced Mail) format for the Ops Manager host. If this flag is not provided, the system Certificate Authority is used. If Ops Manager is using a self-signed SSL (Secure Sockets Layer) certificate, this setting is required. |  |
      | `--httpProxy` | Optional | Provide the URL (Uniform Resource Locator) of an HTTP (Hypertext Transfer Protocol) proxy server the tool can use. |  |

      check-circle means that if you copied the
      `mongodb-backup-restore-util` command provided in
      Ops Manager Application, this field is pre-configured.

   **Step 9: Unmanage the Replica Set.**

   Before attempting to restore the data manually, remove the
   replica set from Automation.

   **Step 10: Restore the Replica Set Manually.**

   Follow the tutorial from the MongoDB Manual to
   restore the replica set.

   **Step 11: Reimport the Replica Set.**

   To manage the replica set with automation again,
   import the replica set
   back into Ops Manager.

**Important:** Rotate Master Key after Restoring Snapshots Encrypted with AES256-GCM

If you restore an
encrypted snapshot that Ops Manager
encrypted with AES256-GCM (Advanced Encryption Standards 256-bit Galois/Counter Mode),
rotate your master key
after completing the restore.
