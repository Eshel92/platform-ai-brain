<!-- Converted from tutorial/manage-s3-blockstore-storage.txt (reStructuredText). Includes are inlined. -->

# Manage S3-Compatible Snapshot Storage

Ops Manager can back up MongoDB databases as snapshots
to one or more of the following storage options:

- Another MongoDB database, called a `blockstore`,
- As files stored on a local or network-attached file system, and/or
- An [S3-compatible](https://aws.amazon.com/s3/) bucket.

This tutorial covers backing up your MongoDB databases as snapshots
stored in S3-compatible storage and S3-compatible storage\-compatible buckets. Ops Manager stores the metadata
for `S3 snapshot stores` in a MongoDB
database.

**Note:**

You might have issues that require you to use more than one snapshot
store. These issues could include needing more capacity, localizing
data, or meeting privacy regulations.

To learn how to assign snapshot stores to different data centers,
see /tutorial/assign-snapshot-stores-to-data-center.

## Considerations

### Requires a Dedicated Bucket

Ops Manager must be the only manager on the S3-compatible storage bucket that you use for snapshots.
You also need to configure the S3-compatible storage bucket to avoid using features that
Ops Manager does not support.

When configuring the S3-compatible storage bucket:

- Do not create subfolders in the S3-compatible storage buckets that you use with Ops Manager.
  Ops Manager only supports using entire S3-compatible storage buckets.
- Disable S3-compatible storage bucket versioning. Versioning is not supported in Ops Manager for
  the S3-compatible storage buckets used for snapshots.
- Do not create S3-compatible storage lifecycle rules. Lifecycle rules that expire or transition
  current versions of Ops Manager snapshot objects to archives results in incomplete snapshots
  that you can't use to restore the configuration.

### Can't Move the S3-Compatible Snapshot Store

After you create an S3-compatible snapshot store, you cannot move it to another S3-compatible storage bucket.
If you need to use a different S3-compatible storage bucket to host your S3-compatible snapshot store, you
must create a new S3-compatible snapshot store in that S3-compatible storage bucket.

### Supports the Storage API

MongoDB supports endpoints for:

- S3-compatible storage `API`
- IBM Cloud Object Storage API
- Dell EMC Elastic Cloud Storage API

IBM and Dell EMC support a subset of the full S3-compatible storage API (Application Programming Interface).

You can use other S3-compatible storage endpoints. Ops Manager attempts to validate
these endpoints when you save the S3-compatible snapshot store setup. If validation
passes, Ops Manager saves the configuration. If validation fails, Ops Manager
displays an error and doesn't save the configuration.

## Prerequisites

### Metadata Storage Prerequisites

- Deploy the dedicated MongoDB instance(s)
  to serve the `S3 snapshot store` metadata
  and `Oplog Store`. Serve these
  instances on separate hosts from the Ops Manager host and the
  application database to avoid performance and backup issues. Attach one or more
  storage volumes with enough capacity to store the databases these
  instances manage.

- Ensure the host serving the Ops Manager `Backup Daemon` service
  has enough capacity to store the head database for FCV 4.0
  deployments and queryable restores in the head directory.

  **Note:**

  If you have not previously set the head directory,
  set it in the Head Directory box.

- Secure the instance that stores your
  `S3 snapshot store` metadata database
  using authentication and
  TLS. S3-compatible snapshot store metadata databases
  support `all authentication mechanisms`.

### AWS S3 Storage Prerequisites

1. Verify that you have an
   `IAM user`
   on AWS (Amazon Web Services).

#. Create your own
   `AWS access keys`
   for your IAM (Identity and Access Management) user. This allows you to create S3-compatible storage buckets and
   store snapshot files in them. MongoDB does not create or issue AWS (Amazon Web Services)
   access keys.

#. Create your own `S3 bucket`
   to store your `S3 snapshot store`
   snapshots.

   **Note:**

   The IAM (Identity and Access Management) user that you created the AWS (Amazon Web Services) access keys for must
   have at least the following `read and write permissions`
   for the S3-compatible storage Bucket:

   - `s3:PutObject`
   - `s3:GetObject`
   - `s3:ListObject`
   - `s3:DeleteObject`

#. (Optional) If you serve your Ops Manager instance on AWS (Amazon Web Services) EC2,
   `create an IAM Role`
   to handle authorization.

   This role needs:

   - AWS service as the trusted entity.
   - EC2 as the use case.
   - Permissions to read and write access to your S3-compatible storage bucket.

   To learn more, see:

   - `Attach IAM role`

   - `Set up S3 bucket access`

### IBM Cloud Object Storage Prerequisites

1. Create an Access Key and Secret Key using IBM credential tools.
#. Create your own S3-compatible storage bucket.

### Dell EMC Elastic Cloud Storage Prerequisites

1. Create an Access Key and Secret Key from your [ECS User ID](https://www.delltechnologies.com/en-us/storage/ecs/index.htm).
#. Create your own S3-compatible storage bucket.

### Other S3-Compatible Storage

Other S3-compatible storage endpoints can be used. Ops Manager attempts to validate
these endpoints when you save the configuration. If validation passes,
the configuration, Ops Manager saves it. If validation fails, Ops Manager displays
an error and doesn't save the configuration.

## Procedures

The format of the Username and Password depend upon the authentication
mechanism. Select one of the following tabs:

**scramsha:**

**x509:**

**kerberos:**

**ldap:**

### Add One S3-Compatible Snapshot Store

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Click Create New S3 Blockstore.**

**Step 3: Provide the S3 blockstore details.**

* - Field
  - Necessity
  - Contents

* - Name
  - Required
  - Type the label for the S3-compatible snapshot store.

* - S3 Bucket Name
  - Required
  - Enter the name of the S3-compatible storage bucket where you want to host the S3-compatible
    snapshot or oplog store. For AWS S3 buckets, enter the bucket's name without the
    S3 URI (Uniform Resource Identifier) prefix.

* - Region Override
  - Conditional
  - Type the region where your S3-compatible storage bucket resides.

    Use this field only if your S3-compatible storage store's **S3 Endpoint** doesn't support region
    scoping. Don't provide a value for this field with AWS S3 buckets.

* - S3 Endpoint
  - Required
  - Enter the URL for this S3-compatible storage bucket. If AWS needs to comply with Amazon S3 regular
    endpoints, use the path-style format: `https://s3.{region}.amazonaws.com`. For more
    details, see the `AWS S3 documentation`.

* - S3 Max Connections
  - Required
  - Type a positive integer indicating the maximum number of
    connections to this S3-compatible storage bucket.

* - Path Style Access
  - Optional
  - Select to use a path-style URL (Uniform Resource Locator) endpoint (`s3.region.amazonaws.com/<bucket>`)
    instead of a virtual-host-style URL (Uniform Resource Locator) endpoint (`<bucket>.s3.amazonaws.com`).

    For more details, see `Path-style requests` in the AWS
    documentation. 

    IMPORTANT: Select this option when using the Amazon S3 service.

* - Server Side Encryption
  - Optional
  - Select to enable `server-side encryption`.
    Clear to disable server-side encryption.

* - S3 Authorization Mode
  - Required
  - Select the method used to authorize access to the S3-compatible storage bucket
    specified in S3 Bucket Name.

    If you select Keys, Ops Manager uses AWS
    Access Key and AWS Secret Key to authorize access
    to your S3-compatible storage bucket.

    If you select IAM Role, Ops Manager uses an AWS (Amazon Web Services) IAM (Identity and Access Management)
    role to authorize access to your S3-compatible storage bucket. AWS
    Access Key and AWS Secret Key fields are ignored.

* - Keys with Custom CA Bundle
  - Conditional
  - Click Choose file to add a custom Certificate Authority
    chain. This chain can validate against a self-signed
    certificate on the S3-compatible storage bucket.

* - AWS Access Key
  - Conditional
  - Type your AWS (Amazon Web Services) Access Key ID.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

* - AWS Secret Key
  - Conditional
  - Type your AWS (Amazon Web Services) Secret Access Key.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

* - Datastore Type
  - Required
  - Select Standalone, Replica Set or
    Sharded Cluster. This MongoDB database stores
    the metadata for the blockstore.

* - MongoDB Host List
  - Conditional
  - Type a comma-separated list of `mongod` instances (for a
    Replica Set) or `mongos` instances (for a Sharded Cluster) in
    the `<hostname:port>` format that comprise the blockstore
    metadata database.

    For example:

    ```ini
    h1.ex.com:27017,h2.ex.com:27017,h2.ex.com:27018
    ```

    Ops Manager displays this field when you set
    Datastore Type to Replica Set or
    Sharded Cluster.

* - MongoDB Hostname
  - Conditional
  - Type the hostname of the S3-compatible snapshot store metadata
    database.

    Ops Manager displays this field when you set
    Datastore Type to Standalone.

* - MongoDB Port
  - Conditional
  - Type the port number of the S3-compatible snapshot store metadata
    database.

    Ops Manager displays this field when you set
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
  - Add additional configuration file options for the MongoDB instance.

    This field supports unescaped values only.

    TLS options do not work here.
    Configure TLS in the `conf-mms.properties` file using the `mongodb.ssl.CAFile` option.

    For proper syntax, see Connection String URI
    Format in the MongoDB manual.

* - Deployment Id
  - Optional
  - Unique identifier of the Deployment Region
    in which to host the bucket.

* - Encrypted Credentials
  - Optional
  - Select if the credentials for the database were encrypted
    using the
    credentialstool.
    The credentials include the Username, Password, AWS (Amazon Web Services) Access
    Key ID and AWS (Amazon Web Services) Secret Key.

* - Use TLS/SSL
  - Optional
  - Select if the S3-compatible snapshot store metadata database only accepts connection
    encrypted using TLS (Transport Layer Security).

    Beyond this checkbox, to connect this S3-compatible snapshot store using TLS (Transport Layer Security), you
    must enable
    TLS on the S3 blockstore database.

* - New Assignment Enabled
  - Optional
  - Select if you want to enable this S3-compatible snapshot store after creating it.
    This is selected by default so the S3-compatible storage blockstore can be
    assigned backup jobs. If you clear this checkbox, the S3-compatible snapshot store
    is created but you cannot assign backups to this S3-compatible snapshot store.

* - Disable Proxy Settings
  - Optional
  - Select if you want to disable proxying to this S3-compatible snapshot store after
    creating it. AWS S3 respects the `HTTP_PROXY` and the
    `HTTPS_PROXY` environment variables. If you set either of
    these environment variables, S3-compatible storage still enables the proxy.

**Step 4: Click Create.**

### Edit One Existing S3-Compatible Snapshot Store

Ops Manager lists S3-compatible snapshot store\s in a table on the
Snapshot Storage page. Each row contains the
settings for one S3-compatible snapshot store.

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Go to the row for the S3-compatible snapshot store you want to edit.**

**Step 3: Update any editable values that need to be changed.**

In the MongoDB Connection column, update any editable values that
need to be changed in the following fields:

* - Field
  - Necessity
  - Editable
  - Contents

* - S3 Bucket Name
  - Required
  - no
  - Type the name of the S3-compatible storage bucket where you want to host the
    the S3-compatible snapshot store.

* - Region Override
  - Conditional
  - no
  - Type the region where your S3-compatible storage bucket resides.

    Use this field only if your S3-compatible storage store's 
    **S3 Endpoint** doesn't support region scoping. Don't provide 
    a value for this field with AWS (Amazon Web Services) S3 buckets.

* - S3 Endpoint
  - Required
  - no
  - Type the URL (Uniform Resource Locator) for this S3-compatible storage bucket.

* - S3 Max Connections
  - Required
  - yes
  - Type a positive integer indicating the maximum number of
    connections to this S3-compatible storage bucket.

* - Path Style Access
  - Optional
  - yes
  - Select to use a path-style URL (Uniform Resource Locator) endpoint (`s3.region.amazonaws.com/<bucket>`)
    instead of a virtual-host-style URL (Uniform Resource Locator) endpoint (`<bucket>.s3.amazonaws.com`).

    For more details, see `Path-style requests` in the AWS
    documentation.

* - Server Side Encryption
  - Optional
  - yes
  - Click to enable `server-side encryption`.
    Clear to disable server-side encryption.

* - S3 Authorization Mode
  - Required
  - yes
  - Select the method used to authorize access to the S3-compatible storage bucket
    specified in S3 Bucket Name.

    |  |  |
    |---|---|
    | Keys | Ops Manager uses AWS Access Key and AWS Secret Key to authorize access to your S3-compatible storage bucket. |
    | IAM Role | Ops Manager uses an AWS (Amazon Web Services) IAM (Identity and Access Management) role to authorize access to your S3-compatible storage bucket. AWS Access Key and AWS Secret Key fields are ignored. |

* - Keys with Custom CA Bundle
  - Conditional
  - yes
  - Click Choose file to add a custom Certificate Authority
    chain. This chain can validate against a self-signed
    certificate on the S3-compatible storage bucket.

* - AWS Access Key
  - Conditional
  - yes
  - Type your AWS (Amazon Web Services) Access Key ID.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

* - AWS Secret Key
  - Conditional
  - yes
  - Type your AWS (Amazon Web Services) Secret Access Key.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

    Ops Manager doesn't display the existing Secret Access Key.

* - <hostname>:<port>
  - Required
  - yes
  - Type in one or more hosts that comprise the S3-compatible storage Snapshot
    Store metadata database in the `<hostname:port>` format.

    If the S3-compatible snapshot store metadata database is a Replica
    Set or Sharded Cluster, type a comma-separated list of
    `mongod` instances (for a Replica Set) or `mongos`
    instances (for a Sharded Cluster).

    For example:

    ```ini
    host1.example.com:27017,host2.example.com:27017,host2.example.com:27018
    ```

    - If the S3-compatible snapshot store metadata database is a
      standalone MongoDB instance, type the `hostname:port` of
      the instance.

* - MongoDB Auth Username
  - Optional
  - yes
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
  - Optional
  - yes
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

    **Note:**

    Ops Manager doesn't display the existing
    MongoDB Auth Password.

* - Encrypted Credentials
  - Optional
  - yes
  - Select if the credentials for the database were encrypted
    using the
    credentialstool.
    The credentials include the Username, Password, AWS (Amazon Web Services) Access
    Key ID and AWS (Amazon Web Services) Secret Key.

* - Use TLS/SSL
  - Optional
  - yes
  - Select if the blockstore database only accepts connection
    encrypted using TLS (Transport Layer Security).

    Beyond this checkbox, to connect this S3-compatible snapshot store
    using TLS (Transport Layer Security), you must enable
    TLS on the S3 blockstore database.

* - Connection Options
  - Optional
  - yes
  - Type any additional configuration file options for the MongoDB instance.
    This field supports unescaped values only.

    For proper syntax, see Connection String URI
    Format in the MongoDB manual.

* - Assignment Labels
  - Optional
  - yes
  - Type a comma-separated list of labels to assign the
    S3 blockstores to specific projects.

* - Load Factor
  - Optional
  - yes
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

    Load Factor can be set to `0`. When one snapshot
    store's Load Factor is set to `0`, it performs
    no backup work at all. If a snapshot store's
    Load Factor is changed while backup work is in
    progress, all jobs or tasks running on that snapshot store
    are allowed to finish. All future backup work then is re-
    distributed among the remaining snapshot stores with a
    Load Factor of `1` or greater and have
    Assignment Enabled selected.

* - Write Concern
  - Required
  - yes
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

Select if you want to enable this S3-compatible snapshot store after creating
it. This is selected by default so the S3-compatible snapshot store can be
assigned backup jobs. If you clear this checkbox, the S3-compatible storage Snapshot
Store is created but you cannot assign backups to this S3-compatible storage Snapshot
Store.

**Step 5: Click Save.**

**Step 6: Restart Ops Manager instances if needed.**

If you change any connection string values or the Write Concern,
restart all the Ops Manager instances including those running Backup
Daemons.

**Warning:**

Modifying the connection string values or the Write Concern for an
existing blockstore requires all Ops Manager components, including
those only running the Backup Daemon, to be restarted to apply
those changes. Connection parameters include:

- <hostname>:
- MongoDB Auth Username
- MongoDB Auth Password
- Encrypted Credentials
- Use TLS/SSL
- Connection Options
- Write Concern

If you change to another blockstore host, the data on the
existing blockstore is not copied automatically to the other
blockstore.

**See also:**

For more details on the MongoDB connection string URI (Uniform Resource Identifier), see
Connection String URI Format
in the MongoDB Manual.

### Delete One S3-Compatible Snapshot Store

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Deselect ASSIGNMENT ENABLED.**

**Step 3: Click the Delete link under the name of the S3 blockstore you want to delete.**
