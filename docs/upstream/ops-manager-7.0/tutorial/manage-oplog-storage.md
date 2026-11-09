<!-- Converted from tutorial/manage-oplog-storage.txt (reStructuredText). Includes are inlined. -->

# Manage Oplog Storage

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

This tutorial covers creating additional Oplog Stores to store oplog
entries. Like any MongoDB instance,
`Oplog Stores` can exist on any host
running MongoDB that the Ops Manager application can access.

## Prerequisites

Before creating any Oplog Stores:

- Ensure storage volume(s) with sufficient capacity to store the oplog
  MongoDB database are attached to the Ops Manager or MongoDB host.

- Deploy the dedicated MongoDB instance(s)
  to host the oplog stores.

- Ensure the host running the Ops Manager `Backup Daemon` service
  has sufficient capacity to store the head database for FCV 4.0
  deployments and queryable restores in the head directory.

  **Note:**

  If you have not previously set the head directory,
  set it in the Head Directory box.

- Secure the instance that stores your
  `Oplog Stores` using
  authentication and
  TLS. Oplog stores support
  `all authentication mechanisms`.

## Procedures

The format of the Username and Password depend upon the authentication
mechanism. Select one of the following tabs:

**scramsha:**

**x509:**

**kerberos:**

**ldap:**

### Add One Oplog Store

**Step 1: Navigate to the Oplog Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Oplog Storage page.

**Step 2: Click Create New Oplog Store.**

**Step 3: Provide the Oplog Store details.**

* - Field
  - Necessity
  - Action

* - Name
  - Required
  - Type the label for the Oplog Store.

* - Datastore Type
  - Required
  - Select Standalone, Replica Set or
    Sharded Cluster.

* - MongoDB Host List
  - Conditional
  - Type a comma-separated list of `mongod` instances (for a
    Replica Set) or `mongos` instances (for a Sharded Cluster) in
    the `<hostname:port>` format that comprise the Oplog Store
    database.

    For example: 

    ```ini
    host1.example.com:27017, host2.example.com:27017, host2.example.com:27018
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
  - Type additional connection string options for the MongoDB instance.
    This field supports unescaped values only.

    TLS options do not work here.
    Configure TLS in the `conf-mms.properties` file using the `mongodb.ssl.CAFile` option.

    You must provide a value for the `authMechanism` option to
    set your authentication method. For more information about
    authentication options for connection strings, see 
    connection-string-auth-options.

    For proper syntax and examples, see 
    Connection String URI
    Format in the MongoDB manual.

* - Deployment Id
  - Optional
  - Unique identifier of the Deployment Region
    in which to host the oplog store.

* - Encrypted Credentials
  - Optional
  - Select if the credentials for the database were encrypted
    using the
    credentialstool.
    The credentials include the Username, Password, AWS (Amazon Web Services) Access
    Key ID and AWS (Amazon Web Services) Secret Key.

* - Use TLS/SSL
  - Optional
  - Select if the Oplog Store database only accepts connection
    encrypted using TLS (Transport Layer Security).

    Beyond this checkbox, to connect this oplog store using
    TLS (Transport Layer Security), you must enable
    TLS on the oplog store database.

* - New Assignment Enabled
  - Optional
  - Select if you want to enable this Oplog Store after creating
    it. This is selected by default so the Oplog Store can be
    assigned backup jobs. If you clear this checkbox, the
    Oplog Store is created but you cannot assign backups to this
    Oplog Store.

**Step 4: Click Create.**

### Edit One Existing Oplog Store

Ops Manager lists `Oplog Stores` in a table
on the Oplog Storage page. Each row
contains the settings for each local and S3-compatible storage oplog store.

**Step 1: Navigate to the Oplog Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Oplog Storage page.

**Step 2: Go to the row for the Oplog Store you want to edit.**

**Step 3: Update any values that need to be changed.**

In the MongoDB Connection column, update any values that
need to be changed in the following fields:

* - Field
  - Action

* - <hostname>:<port>

  - Type in one or more hosts that comprise the Oplog Store
    database in the `<hostname:port>` format.

    IMPORTANT: If these hosts are changed, the Oplog Store database they
    host must have the same data as the original Oplog Store
    database. Changing the host to a new Oplog Store database
    results in data loss.

    If the Oplog Store database is a Replica Set or Sharded
    Cluster, type a comma-separated list of `mongod` instances
    (for a Replica Set) or `mongos` instances (for a Sharded
    Cluster).

    For example:

    ```ini
    host1.example.com:27017,host2.example.com:27017,host2.example.com:27018
    ```

    If the Oplog Store database is a standalone MongoDB
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

  - Select if the credentials for the database were encrypted
    using the
    credentialstool.
    The credentials include the Username, Password, AWS (Amazon Web Services) Access
    Key ID and AWS (Amazon Web Services) Secret Key.

* - Use TLS/SSL

  - Select if the Oplog Store database only accepts connection
    encrypted using TLS (Transport Layer Security).

    Beyond this checkbox, to connect this oplog store using
    TLS (Transport Layer Security), you must enable
    TLS on the oplog store database.

* - Connection Options

  - Type any additional connection string options for the MongoDB instance.
    This field supports unescaped values only.

* - Assignment Labels

  - Type a comma-separated list of labels to assign the
    Oplog Stores to specific projects.

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

Select if you want to enable this Oplog Store after creating it. This
is selected by default so the Oplog Store can be assigned backup
jobs. If you clear this checkbox, the Oplog Store is created but you
cannot assign backups to this Oplog Store.

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

If you change to another Oplog Store host, the data on the
existing Oplog Store is not copied automatically to the other
Oplog Store.

**See also:**

For more details on the MongoDB connection string URI (Uniform Resource Identifier), see
Connection String URI Format
in the MongoDB Manual.

### Delete One Oplog Store

**Step 1: Navigate to the Oplog Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Oplog Storage page.

**Step 2: Click the Delete link.**

Click Delete beneath the name of the oplog
store you want to delete.
