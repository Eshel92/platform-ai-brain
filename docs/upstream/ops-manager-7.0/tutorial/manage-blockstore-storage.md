<!-- Converted from tutorial/manage-blockstore-storage.txt (reStructuredText). Includes are inlined. -->

# Manage Blockstore Snapshot Storage

Ops Manager can back up MongoDB databases as snapshots
to one or more of the following storage options:

- Another MongoDB database, called a `blockstore`,
- As files stored on a local or network-attached file system, and/or
- An [S3-compatible](https://aws.amazon.com/s3/) bucket.

This tutorial covers backing up your MongoDB databases to snapshots
stored in other MongoDB databases.
Blockstores can exist on any
MongoDB instance that Ops Manager can access.

**Note:**

You might have issues that require you to use more than one snapshot
store. These issues could include needing more capacity, localizing
data, or meeting privacy regulations.

To learn how to assign snapshot stores to different data centers,
see /tutorial/assign-snapshot-stores-to-data-center.

## Prerequisites

Before creating any blockstore snapshot stores:

- Ensure storage volumes with sufficient capacity to store the
  blockstore connected to Ops Manager. The
  `Oplog Store` doesn't *need* to reside
  on the same host as the blockstore. The Oplog Store *can* be created
  using the same replica set as the blockstore if you need to
  conserve storage and compute resources.

- Deploy the dedicated MongoDB instance(s)
  to host the blockstore database.

- Ensure the host running the Ops Manager `Backup Daemon` service
  has sufficient capacity to store the head database for FCV 4.0
  deployments and queryable restores in the head directory.

  **Note:**

  If you have not previously set the head directory,
  set it in the Head Directory box.

- Secure the instance that stores your
  blockstores using
  authentication and
  TLS. Blockstores support
  `all authentication mechanisms`.

## Procedures

The format of the Username and Password depend upon the authentication
mechanism. Select one of the following tabs:

**scramsha:**

**x509:**

**kerberos:**

**ldap:**

### Add One Blockstore

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Click Create New Blockstore.**

**Step 3: Provide the blockstore details.**

* - Field
  - Necessity
  - Action

* - Name
  - Required
  - Type a label for the blockstore.

* - Datastore Type
  - Required
  - Select Standalone, Replica Set or
    Sharded Cluster.

* - MongoDB Host List
  - Conditional
  - Type a comma-separated list of mongod instances
    (for a Replica Set) or mongos instances (for a
    Sharded Cluster) in the `<hostname:port>` format that
    comprise the blockstore database.

    For example: 

    ```ini
    h1.ex.com:27017,h2.ex.com:27017,h2.ex.com:27018
    ```

    This field displays only if you set
    Datastore Type to Replica Set or
    Sharded Cluster.

* - MongoDB Hostname
  - Conditional
  - Type the hostname of the standalone MongoDB instance.

    This field displays only if you set
    Datastore Type to Standalone.

* - MongoDB Port
  - Conditional
  - Type the port number of the standalone MongoDB instance.

    This field displays only if you set
    Datastore Type to Standalone.

* - Username
  - Optional
  - If you set this value:

    **scramsha:**

    Type the name of the user authorized to access the this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring SCRAM authentication, see 
    SCRAM.

    **x509:**

    Type the 2253\-formatted subject from the client
    certificate of the user authorized to access this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring x.509 authentication, see 
    x.509.

    **kerberos:**

    Type the UPN (User Principal Name) of the user authorized to access this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring Kerberos authentication, see 
    Kerberos.

    **ldap:**

    Type the name of the LDAP (Lightweight Directory Access Protocol) user authorized to access this
    database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring LDAP authentication, see 
    LDAP.

* - Password
  - Optional
  - If you set this value:

    **scramsha:**

    Type the password associated with the username that can access
    this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring SCRAM authentication, see 
    SCRAM.

    **x509:**

    Leave it blank.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring x.509 authentication, see 
    x.509.

    **kerberos:**

    Kerberos retrieves the password from its
    keytab file.
    Don't type a password into this field.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring Kerberos authentication, see 
    Kerberos.

    **ldap:**

    Type the password of the LDAP (Lightweight Directory Access Protocol) user authorized to access this
    database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring LDAP authentication, see
    LDAP.

    WARNING: If you did not use the 
    credentialstool to
    encrypt this password, it is stored as plaintext in the database.

* - Connection Options
  - Optional
  - Add additional connection string options for the MongoDB instance.
    This field supports unescaped values only.

    TLS options do not work here.
    Configure TLS in the `conf-mms.properties` file by using the `mongodb.ssl.CAFile` option.

    You must provide a value for the `authMechanism` option to
    set your authentication method. For more information about
    authentication options for connection strings, see 
    connection-string-auth-options.

    For proper syntax, see Connection String URI
    Format in the MongoDB manual.

* - Deployment Id
  - Optional
  - Unique identifier of the Deployment Region
    in which to host the database.

* - Encrypted Credentials
  - Optional
  - Select if the Username and Password for the database were
    encrypted using the credentialstool.

* - Use TLS/SSL
  - Optional
  - Select if the blockstore database requires TLS (Transport Layer Security) encryption.

    Beyond this checkbox, to connect this blockstore using
    TLS (Transport Layer Security), you must enable
    TLS on the blockstore database.

* - New Assignment Enabled
  - Optional
  - Select if you want to enable this blockstore after creating
    it. This is selected by default so the blockstore can be
    assigned backup jobs. If you clear this checkbox, the
    blockstore is created but you cannot assign backups to this
    blockstore.

**Step 4: Click Create.**

### Edit One Existing Blockstore

Ops Manager lists blockstores in a table on the
Snapshot Storage page. Each row
contains the settings for one blockstore.

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Go to the row for the blockstore you want to edit.**

**Step 3: Update any values that need to be changed.**

In the MongoDB Connection column, update any values that
need to be changed in the following fields:

* - Field

  - Contents

* - <hostname>:<port>

  - Type in one or more hosts that comprise the blockstore
    database in the `<hostname:port>` format.

    IMPORTANT: If these hosts are changed, the blockstore database they
    host must have the same data as the original blockstore database. 
    Changing the host to a new blockstore databases results in data loss.

    If the blockstore database is a Replica Set or Sharded Cluster, 
    type a comma-separated list of mongod
    instances (for a Replica Set) or mongos
    instances (for a Sharded Cluster).

    For example: 

    ```ini
    host1.example.com:27017,host2.example.com:27017,host2.example.com:27018
    ```

    If the blockstore database is a standalone MongoDB
    instance, type the `hostname:port` of the instance.

* - MongoDB Auth Username

  - If you set this value:

    **scramsha:**

    Type the name of the user authorized to access the this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring SCRAM authentication, see 
    SCRAM.

    **x509:**

    Type the 2253\-formatted subject from the client
    certificate of the user authorized to access this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring x.509 authentication, see 
    x.509.

    **kerberos:**

    Type the UPN (User Principal Name) of the user authorized to access this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring Kerberos authentication, see 
    Kerberos.

    **ldap:**

    Type the name of the LDAP (Lightweight Directory Access Protocol) user authorized to access this
    database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring LDAP authentication, see 
    LDAP.

* - MongoDB Auth Password

  - If you set this value:

    **scramsha:**

    Type the password associated with the username that can access
    this database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring SCRAM authentication, see 
    SCRAM.

    **x509:**

    Leave it blank.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring x.509 authentication, see 
    x.509.

    **kerberos:**

    Kerberos retrieves the password from its
    keytab file.
    Don't type a password into this field.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring Kerberos authentication, see 
    Kerberos.

    **ldap:**

    Type the password of the LDAP (Lightweight Directory Access Protocol) user authorized to access this
    database.

    If your Ops Manager Application Database uses authentication or TLS (Transport Layer Security), you must have 
    connections configured to the application database. To learn 
    more, see configure-connections-to-app-db.

    To learn more about configuring LDAP authentication, see
    LDAP.

    Ops Manager doesn't display the existing
    MongoDB Auth Password.

    WARNING: If you did not use the 
    credentialstool to
    encrypt this password, it is stored as plaintext in the database.

* - Encrypted Credentials

  - Select if the Username and Password for the database were
    encrypted using the credentialstool.

* - Use TLS/SSL

  - Select if the blockstore database requires TLS (Transport Layer Security) encryption.

    Beyond this checkbox, to connect this blockstore using TLS (Transport Layer Security),
    you must enable
    TLS on the blockstore database.

* - Connection Options

  - Type any additional connection string options for the MongoDB instance.
    This field supports unescaped values only.

* - Assignment Labels

  - Type a comma-separated list of labels to assign the
    blockstores to specific projects.

* - Blockstore Max Capacity (GB)

  - .. include:: /includes/api/maxCapacityGB-description.rst

* - Load Factor

  - Type any positive integer that expresses how much backup work
    you want this snapshot store to perform compared to another
    snapshot store.

    Backup work includes running backups, restoring snapshots or
    grooming blockstores. The ratio of backup work
    assigned to a single snapshot store is called its *Load
    Factor*.         

    IMPORTANT: If you have only one snapshot store,
    Load Factor represents the number of concurrent 
    backup work processes the snapshot store performs at a time.
    To avoid performance costs associated with running multiple 
    concurrent processes when you have one snapshot store, 
    omit this setting to assign your snapshot store the 
    default Load Factor of `1`. 

    When you have multiple snapshot stores, the default Load Factor 
    of `1` assigns each snapshot store the same amount of work. If a snapshot 
    store's Load Factor is set to `0`, 
    it performs no backup work at all. 

    If a snapshot store's Load Factor is changed while 
    backup work is in progress, all jobs or tasks running on that snapshot store
    are allowed to finish. All future backup work is then re-
    distributed among the remaining snapshot stores that have a
    Load Factor of `1` or greater and 
    Assignment Enabled selected. 

    As a snapshot store's Load Factor increases, it
    performs more backup work compared to another snapshot store.
    For example, if the Load Factor of snapshot store `A` is set
    to `2` and the Load Factor of snapshot store
    `B` is set to `1`, then `A` performs two times the backup
    work of `B`.

    Snapshot stores with greater computer or storage performance
    should be given a greater Load Factor. 
    For example, consider a five-shard sharded cluster with the
    following backup storage configuration:

    - File system store (`F`) manages the backup work for
      one shard in the cluster. `F` is running on a single
      two-core physical server.

    - Blockstore (`B`) manages the backup work for four
      shards in the cluster. `B` is running as a four-node
      sharded cluster on four physical servers with two cores
      on each server.

    In this example, `B` has four times the capability of
    `F`. You should set the Load Factor\s of `B` to `4` and `F` to `1`. 
    For every `1` backup task `F` performs, `B` performs `4`.

    For more examples comparing the storage capabilities of 
    different backup configurations, see:  

    - A file system store with 16-cores and 128 GB of RAM can
      back up more databases in less time than a file system
      store with only 2 cores and 8 GB of RAM.

    - A blockstore backed by a 10-node sharded cluster can back
      up more databases and groom more databases than a
      blockstore backed by a single replica set.

* - Write Concern

  - Select your preferred
    Write Concern:

    * - Default
      -

        | Deployment Type | Default Write Concern |
        |---|---|
        | Standalone | Journaled |
        | Replica sets or sharded clusters | W2 |

    * - Journaled
      - A primary or standalone MongoDB instance
        acknowledged the write and wrote that write to their on-disk
        journals.

    * - Acknowledged
      - A primary or standalone acknowledged the write.

    * - W2
      - More than one of the cluster members acknowledged the write.

    * - Majority
      - A majority of the replica set members acknowledged the write.

**Step 4: Select the checkbox in the Assignment Enabled column.**

Select if you want to enable this blockstore after creating it. This
is selected by default so the blockstore can be assigned backup jobs.
If you clear this checkbox, the blockstore is created but you cannot
assign backups to this blockstore.

**Step 5: Click Save.**

**Step 6: Restart Ops Manager instances if needed.**

If you change any connection string values or the Write Concern,
restart all the Ops Manager instances including those running Backup
Daemons.

**Warning:**

Modifying the connection string values or the Write Concern for
an existing blockstore requires you to restart all Ops Manager
components, including those only running the Backup Daemon to
apply those changes. Connection parameters include:

- <hostname>:
- MongoDB Auth Username
- MongoDB Auth Password
- Encrypted Credentials
- Use TLS/SSL
- Connection Options
- Write Concern

If you change to another blockstore host, the data on the existing
blockstore is not copied automatically to the other blockstore.

**See also:**

For more details on the MongoDB connection string uri, see
Connection String URI Format
in the MongoDB Manual.

### Delete One Blockstore

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Deselect ASSIGNMENT ENABLED.**

**Step 3: Click the Delete link under the name of the blockstore you want to delete.**
