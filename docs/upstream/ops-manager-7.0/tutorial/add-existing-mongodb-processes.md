<!-- Converted from tutorial/add-existing-mongodb-processes.txt (reStructuredText). Includes are inlined. -->

# Add Existing MongoDB Processes to Ops Manager

Ops Manager provides a wizard for adding your existing MongoDB deployments to
monitoring and management. The wizard prompts you to:

- Install the MongoDB Agent if you don't have it installed
- Identify the sharded cluster, the replica set,
  or the standalone to add. You can choose to add the deployment to
  Monitoring or to both
  Monitoring and
  Automation.

  If you are adding a deployment that you intend to
  live migrate to Atlas,
  you need to add the deployment (and its credentials)  only for
  Monitoring.

## Considerations

### Unique Names

Deployments must have unique names within the projects.

**Important:**

Replica set, sharded cluster, and shard names within the same
project must be unique. Failure to have unique names for the
deployments will result in broken backup snapshots.

### MongoDB Configuration Options

Automation doesn't support all MongoDB options, which can result in 
failed import attempts. To learn more, see 
om-unsupported-mdb-settings.

### TLS (Transport Layer Security)

If you enable TLS (Transport Layer Security), the FQDN (fully qualified domain name) for the host serving a MongoDB process
must match the SAN (Subject Alternative Name) for the TLS (Transport Layer Security)
certificate on that host.

**Important:**

To prevent man-in-the-middle attacks, keep the scope of TLS (Transport Layer Security) certificates
as narrow as possible. Although you can use one TLS (Transport Layer Security) certificate with
many SANs (Subject Alternative Names), or a wildcard TLS (Transport Layer Security)
certificate on each host, you should not. To learn more, see
RFC 2818, section 3.1.

### Preferred Hostnames

Set up a preferred hostname if you:

- Require a specific hostname, FQDN (fully qualified domain name), IPv4 (Internet Protocol version 4) address or IPv6 (Internet Protocol version 6)
  address to access the MongoDB process, or
- Must specify the hostname to use for hosts with multiple aliases.

To learn more, see the Preferred Hostnames setting
in group-settings-page.

### Restore a Previously Removed Host

If you have not completely removed a host from Ops Manager and want to
restore that host, you can reimport the deleted MongoDB process.

If you have completely removed a host from Ops Manager, restore
that host before you reimport it. To search for a deleted host, you
must have the `Global Owner` role.

To locate and restore a deleted host:

1. Navigate to the Deployment view.
#. From the More menu, click Deleted Hosts.
#. Select the trash-alt to restore the host.

After the host is restored, you can
import existing process procedure.

**Note:**

If your host does not appear in the Deleted Hosts list,
you can
reimport the process 
immediately.

### Managing Windows MongoDB Services

If you are adding an existing MongoDB process that runs as a Windows
Service to Automation, Automation:

- Stops and disables the existing service
- Creates and starts a new service

### Authentication Credentials on Source and Destination Clusters

If the Ops Manager project has MongoDB authentication settings enabled for its
deployments, the MongoDB deployment you import must support the project's
authentication mechanism.

We recommend that you import to a **new** destination project that has no
running processes and doesn't have authentication enabled.

If the source cluster uses authentication, and the destination Ops Manager project
doesn't have any existing managed processes, Ops Manager enables authentication
in the destination project, imports the existing keyfile from the source
cluster, and uses it to authenticate the user that conducts the import process.

If the source cluster and the destination Ops Manager project both use authentication,
and the project has processes, Ops Manager attempts to use existing authentication
settings in the destination project during the import process. For the
import process to succeed, authentication credentials on the source cluster
and the Ops Manager destination project must be the same.

To ensure that import is successful, before you start the import process,
add the Ops Manager destination project's credentials on the source cluster.
To learn more, see Rotate Keys for Replica Set
or Rotate Keys for Sharded Clusters.

### Authentication Use Cases

If your MongoDB deployment requires authentication, when you add the
deployment to Ops Manager for monitoring, you must
provide the necessary credentials.

- If the deployment doesn't use Automation, but *did* use Backup, Monitoring,
  or both, you can find those credentials where the credentials were
  before updating to the MongoDB Agent.

- If the deployment doesn't use Automation, but *will* use Backup,
  Monitoring, or both:

  1. Create the credentials for the MongoDB Deployment. To learn more, see
     Required Access for MongoDB Agent for Monitoring
     and Required Access for MongoDB Agent for Backup.

  2. Add the credentials that you granted to those functions to Ops Manager after
     you add the MongoDB processes. To learn more, see
     Add Credentials for Monitoring
     and Add Credentials for Backup.

- If the deployment *uses* Automation, Ops Manager uses the credentials from
  the MongoDB Agent. You can delete the credentials from the legacy Backup,
  and Monitoring Agents. The MongoDB Agent uses those credentials for its
  Automation, Backup, and Monitoring functions.

- If the deployment *will* use Automation but didn't use it before you
  import it, add the `mms-automation` user to the database processes
  you imported and add the user's credentials to Ops Manager.

To learn more, see add-auth-credentials-automation.

### Automation and Updated Security Settings Upon Import

Adding a MongoDB deployment to automation may affect the security
settings of the Ops Manager project and the MongoDB deployment.

- **Automation enables the Project Security Setting**. If the
  MongoDB deployment requires authentication but the Ops Manager project doesn't
  have authentication settings enabled, when you add the MongoDB deployment
  to automation, Ops Manager updates the project's security settings to the security
  settings of the newly imported deployment.

  The import process only updates the Ops Manager project's security setting
  if the project's security setting is currently disabled. The import
  process doesn't disable the project's security setting or change its
  enabled authentication mechanism.

- **Automation Imports MongoDB Users and Roles**. The following statements
  apply to situations where a MongoDB deployment requires authentication
  or the Ops Manager project has authentication settings enabled.

  If the MongoDB deployment contains users or user-defined roles, you can
  choose to import these users and roles for Ops Manager to manage. The imported
  users and roles are Synced to all managed deployments in
  the Ops Manager project.

  - If you set the project's Enforce Consistent Set value to `Yes`,
    Ops Manager deletes from the MongoDB deployments those users and roles
    that are *not* imported.

  - If you set the project's Enforce Consistent Set value to `No`,
    Ops Manager stops managing non-imported users and roles in the project. These
    users and roles remain in the MongoDB deployment. To manage these
    users and roles, you must connect directly to the MongoDB deployment.

  If you don't want the Ops Manager project to manage specific users and roles,
  use the Authentication & Users and
  Authentication & Roles pages to remove these users and roles
  during import before you confirm and deploy the changes. To learn more,
  see manage-unmanage-mongodb-users.

  If the imported MongoDB deployment already has `mms-backup-agent` and
  `mms-monitoring-agent` users in its `admin` database, the import
  process overrides these users' roles with the roles for `mms-backup-agent`
  and `mms-monitoring-agent` users as set in the Ops Manager project.

- **Automation Applies to All Deployments in the Project**.
  The project's updated security settings, including all users and roles
  managed by the Ops Manager project, apply to *all* deployments in the project,
  including the imported MongoDB deployment.

  Ops Manager restarts all deployments in the project with the new setting,
  including the imported MongoDB deployment. After import, all deployments
  in the project use the Ops Manager automation keyfile upon restart.

  The deployment that you import must use the same keyfile as the existing
  processes in the destination project or the import process may not
  proceed. To learn more, see Authentication Credentials on Source
  and Destination Clusters.

  If the existing deployments in the project require a different security
  profile from the imported process, create a new project into which you
  can import the source MongoDB deployment.

#### Examples of Imported Users

The following examples apply to situations where the MongoDB deployment
requires authentication or the Ops Manager project has authentication settings enabled.

If you import the MongoDB users and custom roles, once the Ops Manager project
begins to manage the MongoDB deployment, the following happens, regardless
of the Enforce Consistent Set value:

- The Ops Manager project enables authentication, manages imported users and roles,
  and syncs the new users and roles to all its managed deployments.
- The MongoDB deployment's access control is enabled and requires
  authentication. The MongoDB deployment has all users and roles that
  the Ops Manager project manages. These users and roles have `Synced` set to
  `Yes`.

If you don't import the MongoDB users and custom roles, once the Ops Manager
project begins to manage the MongoDB deployment, the following happens:

If Enforce Consistent Set is set to `Yes`:

- The Ops Manager project enables authentication and doesn't change its managed
  users and roles.
- The MongoDB deployment's access control is enabled and requires authentication.
- Ops Manager deletes the non-imported MongoDB users and roles from the deployment.
- The MongoDB deployment has all users and roles that the Ops Manager project
  manages. These users and roles have `Synced` set to `Yes`.

If Enforce Consistent Set is set to `No`:

- The Ops Manager project enables authentication and doesn't change its security
  settings, including users and roles.
- The MongoDB deployment's access control is enabled and requires authentication.
- The non-imported MongoDB users and roles remain in the MongoDB deployment.
- The MongoDB deployment has all users and roles managed by the Ops Manager project.
  These users and roles have `Synced` set to `Yes`.

## Prerequisites

- If mongod is enabled as a service on the deployment, 
  a race condition might result where `systemd` starts `mongod` on reboot, 
  rather than the Automation. To prevent this issue, ensure the `mongod` 
  service is disabled before you add your deployment to Automation:

  1. Verify whether the `mongod` service is enabled:

     ```sh
     sudo systemctl is-enabled mongod.service
     ```

  2. If the service is enabled, disable it:

     ```sh
     sudo systemctl disable mongod.service
     ```

- If the Ops Manager project doesn't have authentication settings enabled but
  the MongoDB process requires authentication, add the MongoDB Agent user
  for the Ops Manager project with the appropriate roles. The import process
  displays the required roles for the user. The added user becomes the
  project's MongoDB Agent user.

- If the Ops Manager project has authentication settings enabled, add the
  Ops Manager project's MongoDB Agent user to the MongoDB process.

  - To find the MongoDB Agent user, click Deployments, then
    Security, then Users.

  - To find the password for the Ops Manager project's MongoDB Agent user, use
    one of the following methods:

    **ui:**

    Follow the steps in the Add MongoDB Processes procedure to launch the wizard in the UI.
    When you reach the modal that says Do you want to add automation to this deployment?:

    1. Select 
       Add Automation and Configure Authentication.
    #. Click Show Password.

    **api:**

    Use the /reference/api/automation-config endpoint:

    ```sh
    curl --user "{username}:{apiKey}" --digest \
      --header "Accept: application/json" \
      --include \
      --request GET "<host>/api/public/v1.0/groups/<Group-ID>/automationConfig"
    ```

    **file:**

    Open the `mmsConfigBackup` file in your preferred text editor and find the `autoPwd` value.

  - In `mongosh`, use the `db.createUser()` method to add the
    Ops Manager project's MongoDB Agent user to the MongoDB process.
    For example, if the Ops Manager project uses Username/Password authentication,
    run the following command to add the `mms-automation` user to
    the `admin` database in the MongoDB deployment to import:

    ```javascript
    db.getSiblingDB("admin").createUser(
      {
        user: "mms-automation",
        pwd: "<password>",
        roles: [
          'clusterAdmin',
          'dbAdminAnyDatabase',
          'readWriteAnyDatabase',
          'userAdminAnyDatabase',
          'restore',
          'backup',
          'directShardOperations'  // Required for sharded clusters
        ]
      }
    )
    ```

    You must specify the `directShardOperations` role for sharded cluster
    automation. This role allows the automation agent to perform maintenance
    operations that require direct access to shards, such as adding shards to
    existing clusters. For non-sharded deployments (standalone or replica sets),
    you can omit this role.

- When you add a cluster under Ops Manager, Ops Manager automatically enables log
  rotation, which could collide
  with your existing `logRotate` configuration for `mongod` or
  `mongos` logs. To prevent this collision, do the following:  

  - Disable your `logRotate` configuration for `mongod` or `mongos`
    processes. 
  - Remove the `systemLog.logRotate` and `systemLog.logAppend`
    options from the 
    `mongod` or `mongos` process configuration to use the
    default of Ops Manager. 

- The import process requires that the authentication credentials and
  keyfiles are the same on the source and destination clusters. To learn
  more, see Authentication Credentials on Source and Destination Clusters.

- To successfully import an existing replica set to Ops Manager, 
  the instance must be healthy.

**Important:**

If you are adding a sharded cluster, you must create this user through
the mongos *and* on every shard. That is, create the user
both as a cluster wide user through mongos as well as a
shard local user on each shard.

## Procedures

### Add MongoDB Processes

To add existing MongoDB processes to Ops Manager:

**Step 1: Navigate to the Deployment page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

**Step 2: Click Add and select Existing MongoDB Deployment.**

**Step 3: Follow the prompts to add the deployment.**

### Add Authentication Credentials to your Deployment

After you add existing MongoDB process to Ops Manager, you might have to add
authentication credentials for the new deployments if authentication is
enabled for the project into which you imported the deployment. See
add-existing-mongodb-processes-auth to learn in which situations
you must add Automation, Monitoring, or Backup credentials for your new
deployment.

If you are adding a deployment that you intend to
live migrate to Atlas,
you need to add the deployment (and its credentials)  only for
Monitoring.

Select the authentication mechanism that you want to use:

**scramsha:**

**ldap:**

**kerberos:**

**x509:**

#### Add Credentials for Automation

To add credentials for a deployment that will use Automation but didn't
use it before you imported it to Ops Manager:

**Step 1: Add the MongoDB Agent user to your databases.**

The MongoDB Agent user performs automation tasks for your MongoDB
databases. Make sure this MongoDB user has the
proper privileges.

**Step 2: Navigate to the Security Settings dialog for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click the Settings tab.
#. Perform one of the following actions:

   - If this is your first time configuring TLS (Transport Layer Security),
     authentication, or authorization settings for this project, click
     Get Started.
   - If you have already configured TLS (Transport Layer Security) authentication, or
     authorization settings for this project, click Edit.

**Step 3: Click Edit Credentials.**

**Step 4: Continue through the modal until you see the Configure Ops Manager Agents page.**

**Step 5: Add the appropriate credentials:**

**scramsha:**

| Setting | Value |
|---|---|
| MongoDB Agent Username | Enter the MongoDB Agent username. |
| MongoDB Agent Password | Enter the password for MongoDB Agent Username. |

**ldap:**

| Setting | Value |
|---|---|
| MongoDB Agent LDAP Username | Enter the LDAP (Lightweight Directory Access Protocol) username. |
| MongoDB Agent LDAP Password | Enter the password for MongoDB Agent's LDAP (Lightweight Directory Access Protocol) Username. |
| MongoDB Agent LDAP Group DN | Enter the Distinguished Name for the MongoDB Agent's LDAP (Lightweight Directory Access Protocol) Group. Provide the MongoDB Agent's LDAP (Lightweight Directory Access Protocol) Group DN (Distinguished Name) only if you use LDAP (Lightweight Directory Access Protocol) Authorization. Each MongoDB Agent should have and use its own LDAP (Lightweight Directory Access Protocol) Group DN (Distinguished Name). |

**kerberos:**

The required values depend upon whether you are connecting to a
Linux-served KDC (Key Distribution Center) or Windows Active Directory Server.

**Linux KDC:**

| Setting | Value |
|---|---|
| Monitoring Kerberos Principal | Kerberos Principal. |
| Monitoring Keytab Path | Absolute file path to the MongoDB Agent's Keytab. |
| Monitoring LDAP Group DN | Enter the Distinguished Name for the MongoDB Agent's LDAP (Lightweight Directory Access Protocol) Group. The LDAP (Lightweight Directory Access Protocol) Group DN is then created as a role in MongoDB to grant the MongoDB Agent the appropriate privileges. You only need to provide the LDAP Group DN if you use LDAP Authorization. |

**Windows Active Directory:**

| Setting | Value |
|---|---|
| MongoDB Agent Username | Active Directory user name. |
| MongoDB Agent Password | Active Directory password. |
| Domain | NetBIOS name of a domain in Active Directory Domain Services. Must be in all capital letters. |

**x509:**

| Setting | Value |
|---|---|
| MongoDB Agent Username | Enter the LDAP (Lightweight Directory Access Protocol)\v3 distinguished name derived from the MongoDB Agent's PEM (Privacy-Enhanced Mail) Key file. |
| TLS/SSL CA File Path | The path on disk that contains the trusted certificate authority (CA) certificates in PEM (Privacy-Enhanced Mail) format. These certificates verify the server certificate returned from any MongoDB instances running with TLS (Transport Layer Security)/SSL (Secure Sockets Layer). You must enter at least one TLS (Transport Layer Security)/SSL (Secure Sockets Layer) CA file path. |
| MongoDB Agent PEM Key file | If your MongoDB deployment requires client certificates, on the line for the appropriate operating system, provide the path and `.pem` filename for the client certificate used by the MongoDB Agent's PEM (Privacy-Enhanced Mail) Key file on the server. You must enter a value for at least one MongoDB Agent PEM Key File. |
| MongoDB Agent PEM Key Password | Provide the password to the PEM (Privacy-Enhanced Mail) Key file if it was encrypted. |
| MongoDB Agent LDAP Group DN | Enter the Distinguished Name for the MongoDB Agent's LDAP (Lightweight Directory Access Protocol) Group. You only need to provide MongoDB Agent's LDAP (Lightweight Directory Access Protocol) Group DN if you use LDAP (Lightweight Directory Access Protocol) Authorization. |

#### Add Credentials for Monitoring

To add credentials for a deployment that will not use Automation but
will use Monitoring:

**Step 1: Navigate to the Monitoring Settings dialog for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click `ellipsis`, then click Monitoring
   Settings next to the deployment for which you want to view
   monitoring settings.

**Step 2: Click Credentials.**

**Step 3: Add the appropriate credentials:**

**scramsha:**

| Setting | Value |
|---|---|
| Monitoring Username | Enter the Monitoring username. |
| Monitoring Password | Enter the password for Monitoring Username. |

**ldap:**

| Setting | Value |
|---|---|
| Monitoring LDAP Username | Enter the LDAP (Lightweight Directory Access Protocol) username. |
| Monitoring LDAP Password | Enter the password for Monitoring's LDAP (Lightweight Directory Access Protocol) Username. |
| Monitoring LDAP Group DN | Enter the Distinguished Name for the Monitoring's LDAP (Lightweight Directory Access Protocol) Group. Provide the Monitoring's LDAP (Lightweight Directory Access Protocol) Group DN (Distinguished Name) only if you use LDAP (Lightweight Directory Access Protocol) Authorization. Each Monitoring should have and use its own LDAP (Lightweight Directory Access Protocol) Group DN (Distinguished Name). |

**kerberos:**

The required values depend upon whether you are connecting to a
Linux-served KDC (Key Distribution Center) or Windows Active Directory Server.

**Linux KDC:**

| Setting | Value |
|---|---|
| Monitoring Kerberos Principal | Kerberos Principal. |
| Monitoring Keytab Path | Absolute file path to the Monitoring's Keytab. |
| Monitoring LDAP Group DN | Enter the Distinguished Name for the Monitoring's LDAP (Lightweight Directory Access Protocol) Group. The LDAP (Lightweight Directory Access Protocol) Group DN is then created as a role in MongoDB to grant the Monitoring the appropriate privileges. You only need to provide the LDAP Group DN if you use LDAP Authorization. |

**Windows Active Directory:**

| Setting | Value |
|---|---|
| Monitoring Username | Active Directory user name. |
| Monitoring Password | Active Directory password. |
| Domain | NetBIOS name of a domain in Active Directory Domain Services. Must be in all capital letters. |

**x509:**

| Setting | Value |
|---|---|
| Monitoring Username | Enter the LDAP (Lightweight Directory Access Protocol)\v3 distinguished name derived from the Monitoring's PEM (Privacy-Enhanced Mail) Key file. |
| Monitoring PEM Key file | Provide the path and filename for the Monitoring's PEM (Privacy-Enhanced Mail) Key file on the server on the line for the appropriate operating system. |
| Monitoring PEM Key Password | Provide the password to the PEM (Privacy-Enhanced Mail) Key file if it was encrypted. |
| Monitoring LDAP Group DN | Enter the Distinguished Name for the Monitoring's LDAP (Lightweight Directory Access Protocol) Group. You only need to provide the Monitoring's LDAP (Lightweight Directory Access Protocol) Group DN if you use LDAP (Lightweight Directory Access Protocol) Authorization. |

#### Add Credentials for Backup

To add credentials for a deployment that will not use Automation but
will use Backup:

**Step 1: Navigate to the Continuous Backup page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Continuous Backup in the sidebar.

**Step 2: For your deployment, Click `ellipsis`, then click Edit Credentials.**

**Step 3: Add the appropriate credentials:**

**scramsha:**

| Setting | Value |
|---|---|
| Backup Username | Enter the Backup username. |
| Backup Password | Enter the password for Backup Username. |

**ldap:**

| Setting | Value |
|---|---|
| Backup LDAP Username | Enter the LDAP (Lightweight Directory Access Protocol) username. |
| Backup LDAP Password | Enter the password for Backup's LDAP (Lightweight Directory Access Protocol) Username. |
| Backup LDAP Group DN | Enter the Distinguished Name for the Backup's LDAP (Lightweight Directory Access Protocol) Group. Provide the Backup's LDAP (Lightweight Directory Access Protocol) Group DN (Distinguished Name) only if you use LDAP (Lightweight Directory Access Protocol) Authorization. Each Backup should have and use its own LDAP (Lightweight Directory Access Protocol) Group DN (Distinguished Name). |

**kerberos:**

The required values depend upon whether you are connecting to a
Linux-served KDC (Key Distribution Center) or Windows Active Directory Server.

**Linux KDC:**

| Setting | Value |
|---|---|
| Monitoring Kerberos Principal | Kerberos Principal. |
| Monitoring Keytab Path | Absolute file path to the Backup's Keytab. |
| Monitoring LDAP Group DN | Enter the Distinguished Name for the Backup's LDAP (Lightweight Directory Access Protocol) Group. The LDAP (Lightweight Directory Access Protocol) Group DN is then created as a role in MongoDB to grant the Backup the appropriate privileges. You only need to provide the LDAP Group DN if you use LDAP Authorization. |

**Windows Active Directory:**

| Setting | Value |
|---|---|
| Backup Username | Active Directory user name. |
| Backup Password | Active Directory password. |
| Domain | NetBIOS name of a domain in Active Directory Domain Services. Must be in all capital letters. |

**x509:**

| Setting | Value |
|---|---|
| Backup Username | Enter the LDAP (Lightweight Directory Access Protocol)\v3 distinguished name derived from the Backup's PEM (Privacy-Enhanced Mail) Key file. |
| Backup PEM Key file | Provide the path and filename for the Backup's PEM (Privacy-Enhanced Mail) Key file on the server on the line for the appropriate operating system. |
| Backup PEM Key Password | Provide the password to the PEM (Privacy-Enhanced Mail) Key file if it was encrypted. |
| Backup LDAP Group DN | Enter the Distinguished Name for the Backup's LDAP (Lightweight Directory Access Protocol) Group. You only need to provide Backup's LDAP (Lightweight Directory Access Protocol) Group DN if you use LDAP (Lightweight Directory Access Protocol) Authorization. |
