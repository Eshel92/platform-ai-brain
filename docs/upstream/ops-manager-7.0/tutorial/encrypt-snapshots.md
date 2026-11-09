<!-- Converted from tutorial/encrypt-snapshots.txt (reStructuredText). Includes are inlined. -->

# Encrypted Backup Snapshots

Snapshot encryption depends upon which
version of MongoDB your database is compatible.
This Feature Compatibility Version ranges from the current version
to one version earlier. For MongoDB 4.2, the FCV can be `4.0` or
`4.2`. You can only create encrypted snapshots from encrypted 
clusters.

**fcv42:**

Ops Manager can encrypt any backup job that it had stored in a
snapshot store. The snapshot must come from a database that
ran
`MongoDB Enterprise`
4.2 or later with:

- FCV of 4.2 or later and
- WiredTiger storage engine.

**Warning:**

Ops Manager doesn't support transitioning from local key encryption 
to KMIP (Key Management Interoperability) server-based encryption.

**Note:**

Ops Manager no longer supports the creation of cluster snapshots from
database deployments that use local key encryption.
If you encrypt a database deployment with local key encryption,
the snapshot fails.
To encrypt snapshots, use KMIP (Key Management Interoperability)-based encryption with your database deployments.

To encrypt backups, use a master key that a KMIP (Key Management Interoperability)-compliant
key management appliance generates and maintains. This master
key encrypts key that encrypts the database.

Ops Manager creates snapshots of FCV of 4.2 or later deployments by
copying the bytes on disk from a host's `storage.dbPath` to the
snapshot store. If you enable MongoDB Encryption at Rest for the host
you are backing up, the bytes that Ops Manager copies to the snapshot store
are already encrypted. Ops Manager encrypts data at the storage engine layer 
when you write data to a host's disk.

For FCV of 4.2 or later deployments, Ops Manager components don't
interact with the KMIP (Key Management Interoperability) host when taking snapshots. 

**Important:**

The `Backup Daemon` requires a connection to the
KMIP (Key Management Interoperability) host to process a queryable restore job of an encrypted backup.

**See also:**

MongoDB Encryption at Rest

**fcv40:**

Ops Manager supports encryption for any backup job that was
stored in a `head database` running
`MongoDB Enterprise`
3.4 or later with the
WiredTiger storage engine.

**Warning:**

Ops Manager doesn't support transitioning from local key encryption 
to KMIP (Key Management Interoperability) server-based encryption.

To encrypt backups, you use a master key that a
KMIP (Key Management Interoperability)-compliant key management appliance generates and
maintains. This master key encrypts the
`head databases`. As the
`Backup Daemon` creates snapshots from the head
databases, resulting snapshots from the encrypted head
databases are themselves encrypted.

To restore from an encrypted backup, you need the same master
key used to encrypt the backup and either the same certificate
as is on the `Backup Daemon` host or a new certificate
provisioned with that key from the KMIP (Key Management Interoperability) host. This
corresponds to the value in the **KMIP client certificate
path** field.

## Prerequisites

A host running KMIP (Key Management Interoperability)-compliant key management to generate and store
encryption keys.

**fcv42:**

**Important:**

Clusters running MongoDB FCV 4.2 or later must use
KMIP (Key Management Interoperability) servers. These clusters don't support local key
management using files.

**fcv40:**

- `Head databases` use
  `MongoDB Enterprise`
  3.4 or later with the WiredTiger storage engine.

- A valid KMIP (Key Management Interoperability) client certificate and KMIP (Key Management Interoperability) host Certificate Authority
  files. These files are used to authenticate Ops Manager to the
  KMIP (Key Management Interoperability) host. The client certificate on the Backup Daemon
  host must have access to all keys in the KMIP (Key Management Interoperability) host.

**Important:**

You must maintain all keys, even rotated keys, in the KMIP (Key Management Interoperability) host.

## Set up KMIP Host Configuration for Ops Manager

**Step 1: Navigate to the Backup configuration tab.**

a. Click Admin.
b. Click General.
c. Click Ops Manager Config.
d. Click Backup tab.

**See also:**

admin-console-general-om-config

**Step 2: Complete the KMIP fields.**

Update the following KMIP (Key Management Interoperability) host fields in the
KMIP Server Configuration section:

|  |  |
|---|---|
| `KMIP Server Host` | Type the FQDN (fully qualified domain name) for the KMIP (Key Management Interoperability) host. |
| `KMIP Server Port` | Type the port on which the KMIP (Key Management Interoperability) host is listening for KMIP (Key Management Interoperability) connections. The default KMIP (Key Management Interoperability) port is 5696 <http://www.iana.org/assignments /service-names-port-numbers/service-names-port- numbers.xhtml?&page=95>. |
| `KMIP Server CA File` | Type the absolute path for the Certificate Authority file on the Ops Manager host. This must be the same Certificate Authority file stored on the KMIP (Key Management Interoperability) host. |

**Step 3: Click Save.**

## Configure Your Project to Use KMIP

**Note:**

All deployments in the project use the same KMIP (Key Management Interoperability) client
certificate file to authenticate.

**Step 1: Navigate to the Project Backup configuration page.**

a. Click Admin
b. Click Projects
c. Under the <Project Name>, click More ....
d. In the row for Backup Configuration, click View.

**See also:**

admin-console-general-projects

**Step 2: Complete the KMIP fields.**

|  |  |
|---|---|
| KMIP client certificate path | Type the absolute path for the client certificate file on the Ops Manager host. Ops Manager uses this certificate to authenticate itself to the KMIP server. A single file can hold both the CA and client certificate. |
| KMIP client certificate password | *Optional* Only enter if the certificate specified in KMIP client certificate path is encrypted. |

**Step 3: Click Save Changes.**

## Encrypt Your Backup Job

**fcv42:**

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

  - WiredTiger

    Ops Manager limits backups to deployments with fewer than 100,000
    files. Files includes collections and indexes.

  - `WiredTiger`

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

**Step 5: Click Start.**

**fcv40:**

**Important:**

For existing backups in a project, enabling encryption
requires an initial backup sync to recreate the backups'
head databases.

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
