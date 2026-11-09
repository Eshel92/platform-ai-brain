<!-- Converted from tutorial/manage-s3-oplog-storage.txt (reStructuredText). Includes are inlined. -->

# Manage S3-Compatible Oplog Storage

Throughout the lifecycle of a backup, MongoDB Agent tails the
oplog of each replica set and sends new oplog entries
to Ops Manager. The Agent sends the oplog entries in compressed bundles of
approximately 10 MB in size called oplog slices.
These oplog slices are stored in one or more MongoDB databases called
`oplog stores`. Every Ops Manager deployment
needs at least one oplog store.

When you enable backups, Ops Manager prompts you to create your first oplog
store. This can be a local oplog store or an S3-compatible oplog store. Once you create
the first oplog store, you manage it separately from your snapshot
stores. You can create additional oplog stores.

This tutorial covers creating additional S3-compatible oplog store\s to store oplog
entries. Like any MongoDB instance, an S3-compatible oplog store can exist on any host
running MongoDB and S3-compatible storage bucket (without subfolders) that the Ops Manager
application can access.

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

### Can't Move the S3-Compatible Oplog Store

After you create an S3-compatible oplog store, you can't move it. Instead, you can 
create a new S3-compatible oplog store in a separate S3-compatible storage bucket within the same AWS (Amazon Web Services) 
region. The S3-compatible storage snapshot bucket must be different than the oplog S3-compatible storage 
bucket.

### Supports the Storage API

MongoDB supports endpoints for:

- S3-compatible storage `API`
- IBM Cloud Object Storage API
- Dell EMC Elastic Cloud Storage API.

IBM and Dell EMC support a subset of the full S3-compatible storage API (Application Programming Interface).

You can use other S3-compatible endpoints. Ops Manager attempts to validate
these endpoints when you save the S3-compatible oplog store setup. If validation
passes, Ops Manager saves the configuration. If validation fails, Ops Manager
displays an error and doesn't save the configuration.

## Prerequisites

### Metadata Storage Prerequisites

- Deploy the dedicated MongoDB instance(s)
  to serve the S3-compatible oplog store metadata and
  `Oplog Store`. Serve these instances on
  the same hosts as the Ops Manager host, the backing databases,
  or snapshot stores. Attach one or more storage volumes with enough
  capacity to store the databases these instances manage.

- Secure the instance that stores your S3-compatible oplog store metadata database
  using authentication and
  TLS. S3-compatible oplog store metadata databases
  support all authentication mechanisms.

### AWS S3 Storage Prerequisites

1. Make sure you have an
   `IAM user`
   on AWS (Amazon Web Services).

#. Create your own
   `AWS access keys`
   for your IAM (Identity and Access Management) user. This allows you to create S3-compatible storage buckets and
   store oplog files in them. MongoDB does not create or issue AWS (Amazon Web Services)
   access keys.

#. Create your own `S3 bucket`
   to store your S3-compatible oplog store\s.

   **Note:**

   The IAM (Identity and Access Management) user for which you created the AWS (Amazon Web Services) access keys must
   `own`
   the S3-compatible storage bucket.

### IBM Cloud Object Storage Prerequisites

1. Create an Access Key and Secret Key using IBM credential tools.
#. Create your own S3-compatible storage bucket.

### Dell EMC Elastic Cloud Storage Prerequisites

1. Create an Access Key and Secret Key from your
   [ECS User ID](https://www.delltechnologies.com/en-us/storage/ecs/index.htm).
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

### Add One S3-Compatible Oplog Store

**Step 1: Navigate to the Oplog Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Oplog Storage page.

**Step 2: Click Create New S3 Oplog Store.**

**Step 3: Provide the S3 Oplog Store Details.**

* - Field
  - Necessity
  - Contents

* - Name
  - Required
  - Enter the label for the S3-compatible oplog store.

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
  - Enter a positive integer indicating the maximum number of
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

    |  |  |
    |---|---|
    | Keys | Ops Manager uses AWS Access Key and AWS Secret Key to authorize access to your S3-compatible storage bucket. |
    | IAM Role | Ops Manager uses an AWS (Amazon Web Services) IAM (Identity and Access Management) role to authorize access to your S3-compatible storage bucket. AWS Access Key and AWS Secret Key fields are ignored. To learn more, see the `AWS documentation` |

* - Keys with Custom CA Bundle
  - Conditional
  - Click Choose file to add a custom Certificate Authority
    chain. This chain can validate against a self-signed
    certificate on the S3-compatible storage bucket.

* - AWS Access Key
  - Conditional
  - Enter your AWS (Amazon Web Services) Access Key ID.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

* - AWS Secret Key
  - Conditional
  - Enter your AWS (Amazon Web Services) Secret Access Key.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

* - Datastore Type
  - Required
  - Select Standalone, Replica Set or
    Sharded Cluster. This MongoDB database stores
    the metadata for the blockstore.

* - MongoDB Host List
  - Conditional
  - Enter a comma-separated list of `mongod` instances (for a
    Replica Set) or `mongos` instances (for a Sharded Cluster) in
    the `<hostname:port>` format that comprise the blockstore
    metadata database.

    For example: 

    ```ini
    host1.example.com:27017,host2.example.com:27017,host2.example.com:27018
    ```

    Ops Manager displays this field when you set
    Datastore Type to Replica Set or
    Sharded Cluster.

    IMPORTANT: Ops Manager uses this metadata store as a sync store. Make
    sure to provision this store with sufficient storage space.

* - MongoDB Hostname
  - Conditional
  - Enter the hostname of the S3-compatible oplog store metadata database.

    Ops Manager displays this field when you set
    Datastore Type to Standalone.

    IMPORTANT: Ops Manager uses this metadata store as a sync store. Make
    sure to provision this store with sufficient storage space.

* - MongoDB Port
  - Conditional
  - Enter the port number of the S3-compatible oplog store metadata
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
  - Enter additional configuration file options for the MongoDB instance.

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
  - Select if the S3-compatible oplog store metadata database only
    accepts connection encrypted using TLS (Transport Layer Security).

    Beyond this checkbox, to connect this S3-compatible oplog store
    using TLS (Transport Layer Security), you must enable
    TLS on the S3 oplog store database.

* - New Assignment Enabled
  - Optional
  - Select if you want to enable this S3-compatible oplog store after creating it.
    This is selected by default so the S3-compatible oplog store can be
    assigned backup jobs. If you clear this checkbox, the S3-compatible oplog store
    is created but you cannot assign backups to this S3-compatible oplog store.

**Step 4: Click Create.**

### Edit One Existing S3-Compatible Oplog Store

Ops Manager lists `oplog stores` in a table
on the Oplog Storage page. Each row
contains the settings for each local and S3-compatible oplog store.

**Step 1: Navigate to the Oplog Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Oplog Storage page.

**Step 2: Go to the row for the S3-compatible oplog store you want to edit.**

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
  - Enter the name of the S3-compatible storage bucket where you want to host the
    the S3-compatible oplog store.

* - Region Override
  - Conditional
  - no
  - Type the region where your S3-compatible storage bucket resides.

    Use this field only if your S3-compatible storage store's **S3 Endpoint** doesn't support region
    scoping. Don't provide a value for this field with AWS S3 buckets.

* - S3 Endpoint
  - Required
  - no
  - Enter the URL (Uniform Resource Locator) for this S3-compatible storage bucket.

* - S3 Max Connections
  - Required
  - yes
  - Enter a positive integer indicating the maximum number of
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
    | IAM Role | Ops Manager uses an AWS (Amazon Web Services) IAM (Identity and Access Management) role to authorize access to your S3-compatible storage bucket. AWS Access Key and AWS Secret Key fields are ignored. To learn more, see the `AWS documentation` |

* - Keys with Custom CA Bundle
  - Conditional
  - yes
  - Click Choose file to add a custom Certificate Authority
    chain. This chain can validate against a self-signed
    certificate on the S3-compatible storage bucket.

* - AWS Access Key
  - Conditional
  - yes
  - Enter your AWS (Amazon Web Services) Access Key ID.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

* - AWS Secret Key
  - Conditional
  - yes
  - Enter your AWS (Amazon Web Services) Secret Access Key.

    Ops Manager displays this field when you set
    S3 Authorization Mode to Keys.

    Ops Manager doesn't display the existing AWS Secret Key.       

* - <hostname>:<port>
  - Required
  - yes
  - Enter in one or more hosts that comprise the S3-compatible storage Snapshot
    Store metadata database in the `<hostname:port>` format.

    If the S3-compatible oplog store metadata database is a Replica
    Set or Sharded Cluster, type a comma-separated list of
    `mongod` instances (for a Replica Set) or `mongos`
    instances (for a Sharded Cluster).

    For example:

    ```ini
    host1.example.com:27017,host2.example.com:27017,host2.example.com:27018
    ```

    If the S3-compatible oplog store metadata database is a standalone MongoDB
    instance, type the `hostname:port` of the instance.

    IMPORTANT: S3 Oplog Hosting Concerns: 

    - Ops Manager uses this metadata store as a sync store. Make
      sure to provision this store with sufficient storage
      space.

    - If you change these hosts, the S3-compatible oplog store they host must have
      the same data as the original S3-compatible oplog store. Changing the host
      to a new S3-compatible oplog store results in data loss.

    - If the S3-compatible oplog store metadata database is a Replica
      Set or Sharded Cluster, type a comma-separated list of
      `mongod` instances (for a Replica Set) or `mongos`
      instances (for a Sharded Cluster).

      **Example:**

      `host1.example.com:27017,host2.example.com:27017,host2.example.com:27018`

    - If the S3-compatible oplog store metadata database is a standalone MongoDB
      instance, type the `hostname:port` of the instance.

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

* - Encrypted Credentials
  - Optional
  - yes
  - Select if the credentials for the database were encrypted
    using the
    credentialstool.
    The credentials include the Username, Password, AWS (Amazon Web Services) Access
    Key ID and AWS (Amazon Web Services) Secret Key.

* - Use TLS (Transport Layer Security)/SSL (Secure Sockets Layer)
  - Optional
  - yes
  - Select if the S3-compatible oplog store database only accepts connection
    encrypted using TLS (Transport Layer Security).

    Beyond this checkbox, to connect this S3-compatible oplog store
    using TLS (Transport Layer Security), you must enable
    TLS on the S3 oplog store database.

* - Connection Options
  - Optional
  - yes
  - Enter any additional configuration file options for the MongoDB instance.
    This field supports unescaped values only.

    To review the proper syntax, see Connection String
    URI Format in the MongoDB
    manual.

* - Assignment Labels
  - Optional
  - yes
  - Enter a comma-separated list of labels to assign the
    S3-compatible oplog store\s to specific projects.

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

**Step 4: Set the S3 Oplog Store to Accept Backup Jobs.**

To enable this S3-compatible oplog store, select Assignment Enabled.

This is selected by default so the S3-compatible oplog store can be assigned backup
jobs. If you clear this checkbox, Ops Manager creates the S3-compatible oplog store but you
cannot assign backups to it.

**Step 5: Click Save.**

**Step 6: Restart Ops Manager Instances If Needed.**

If you change any connection string values or the Write Concern,
restart all the Ops Manager instances including those running Backup
Daemons.

**Warning:**

Modifying the connection string values or the Write Concern for
an existing S3-compatible oplog store requires you to restart all Ops Manager
components, including those only running the Backup Daemon to
apply those changes. Connection parameters include:

- <hostname>:
- MongoDB Auth Username
- MongoDB Auth Password
- Encrypted Credentials
- Use TLS/SSL
- Connection Options
- Write Concern

If you change to another S3-compatible oplog store host, Ops Manager doesn't copy the data
on the existing S3-compatible oplog store to the other S3-compatible oplog store.

**See also:**

To learn more about the MongoDB connection string URI (Uniform Resource Identifier), see
Connection String URI Format
in the MongoDB Manual.

### Delete One S3-Compatible Oplog Store

**Step 1: Navigate to the Oplog Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Oplog Storage page.

**Step 2: Click the Delete link.**

Click Delete beneath the name of the S3-compatible oplog store
you want to delete.
