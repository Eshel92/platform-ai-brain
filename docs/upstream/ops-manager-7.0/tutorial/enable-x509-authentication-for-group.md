<!-- Converted from tutorial/enable-x509-authentication-for-group.txt (reStructuredText). Includes are inlined. -->

# Enable x.509 Authentication for your Ops Manager Project

Ops Manager enables you to configure the Authentication Mechanisms that all
clients, including the Ops Manager Agents, use to connect to your MongoDB
deployments. You can enable multiple authentication mechanisms for each
of your projects, but you must choose only one mechanism for the Agents.

MongoDB supports x.509 client and member certificate authentication for
use with a secure TLS/SSL connection.
The x.509 authentication allows users and other members to authenticate
to servers with certificates rather than with a username and password.

## Prerequisites

**Important:**

A full description of
Transport Layer Security,
public key infrastructure,
X.509 certificates, and
Certificate Authorities
exceeds the scope of this tutorial. This tutorial assumes prior
knowledge of TLS (Transport Layer Security) and access to valid X.509 certificates.

## Procedures

These procedures describe how to configure and enable x.509
authentication when using Automation. If Ops Manager does *not* manage your
agents, you must manually configure them to use x.509 authentication.

**Note:**

To learn more, see
/tutorial/configure-mongodb-agent-for-x509.

### Prepare an Existing Deployment for x.509 Certificate Authentication

**Important:**

Using x.509 client certificate authentication requires TLS (Transport Layer Security)/SSL (Secure Sockets Layer). 
If Ops Manager manages one or more existing deployments, TLS (Transport Layer Security)/SSL (Secure Sockets Layer) must 
be enabled on each process in the MongoDB deployment before 
enabling x.509 authentication.

**Note:**

If TLS (Transport Layer Security)/SSL (Secure Sockets Layer) is already enabled, you may skip this procedure.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the process, click Modify.**

**Step 3: Expand the Advanced Configuration Options section.**

**Step 4: Set the TLS (Transport Layer Security)/SSL (Secure Sockets Layer) startup options.**

a. Click Add Option to add each of the following options:

   * - Option
     - Required
     - Value

   * - `tlsMode`
     - Required
     - Select `requireTLS`.

   * - `tlsCertificateKeyFile`
     - Required
     - Provide the absolute path to the server certificate.

   * - `tlsCertificateKeyFilePassword`
     - Required
     - Provide the PEM key file password if you encrypted it.

       **Important:**

       If the encrypted private key for the `.pem` certificate file 
       is in PKCS #8 format, 
       it must use PBES2 encryption operations. 
       The MongoDB Agent does not support PKCS #8 with other encryption 
       operations.

   * - `tlsFIPSMode`
     - Optional
     - Select `true` if you want to
       enable FIPS mode.

b. After adding each option, click Add.

c. When you have added the required options, click Save.

**Step 5: Click Save.**

**Step 6: Click Review & Deploy to review your changes.**

**Step 7: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

### Configure an Existing Deployment for x.509 Member Certificate Authentication

**Note:**

This procedure is optional. It enables members of a replica set or sharded cluster to also use x.509 certificates to authenticate each other. If it is not configured, replica set and sharded cluster members can still authenticate with each other using `keyFile` authentication.

   

**Warning:** This Procedure is Irreversible

If you enable x.509 member certificate authentication for any 
deployment in a project, you can't disable x.509 member certificate 
authentication for the deployment or disable 
x.509 client authentication at the project level.

Enabling x.509 member certificate authentication for a deployment in
a project doesn't enable or require x.509 member certificate 
authentication for other deployments in the project. You can
optionally enable each other deployment in the project to use x.509 
member certificate authentication.

**Important:**

If you configured the MongoDB Agent PEM 
and set `security.clusterAuthMode`: to `x509`,
a warning that 
`Client connecting with server's own TLS certificate`
displays in the `mongod` log files,
indicating that the client is connecting with 
the server's own TLS certificate.

This is expected behavior, because the MongoDB Agent 
connects to Ops Manager using the internal authorization 
configuration. No action is necessary.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the process, click Modify.**

**Step 3: Expand the Advanced Configuration Options section.**

**Step 4: Set the x.509 startup options.**

a. Click Add Option to add each option.

   | Option | Value |
   |---|---|
   | `clusterAuthMode` | Select `x509`. |
   | `clusterFile` | Provide the path to the member PEM Key file. |

b. After each option, click Add.

**Step 5: Click Save.**

**Step 6: Click Review & Deploy to review your changes.**

**Step 7: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

When you have configured the TLS (Transport Layer Security)/SSL (Secure Sockets Layer) options for each deployed 
process, you can proceed to enable x.509 authentication for your Ops Manager 
project.

### Enable x.509 Client Certificate Authentication for your Ops Manager Project

**Step 1: Navigate to the Security Settings dialog for your deployment.**

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

**Step 2: Specify the TLS (Transport Layer Security) Settings.**

* - Field
  - Action

* - MongoDB Deployment Transport Layer Security (TLS)
  - Toggle this slider to ON.

* - TLS CA File Path
  - The TLS (Transport Layer Security) Certificate Authority file is a `.pem`-format certificate
    file that contains the root certificate chain from the
    Certificate Authority. The MongoDB Agent uses this same Certificate Authority file
    to connect to every item in your deployment.

    The encrypted private key for the `.pem` certificate file must be in
    PKCS #1 format. The MongoDB Agent doesn't support
    the PKCS #8 format.

    Type the file path to the TLS (Transport Layer Security) Certificate Authority file on every host
    running a MongoDB process:

    - Type the file path on all Linux hosts in the first box.

    - Type the file path on all Windows hosts in the second box.

    This enables the `net.tls.CAFile` setting for the
    MongoDB processes in the project.

    Click Validate to test that each host in your
    deployment has a TLS (Transport Layer Security) Certificate Authority at the paths you specified.

* - Client Certificate Mode
  - Select if client applications or MongoDB Agent\s must present a
    TLS (Transport Layer Security) certificate when connecting to a TLS (Transport Layer Security)\-enabled MongoDB
    deployments. Each MongoDB deployment checks for certificates
    from these client hosts when they try to connect. If you
    choose to require the client TLS (Transport Layer Security) certificates, make sure
    they are valid.

    Accepted values are:

    |  |  |
    |---|---|
    | Optional | Every client may present a valid TLS (Transport Layer Security) certificate when connecting to MongoDB deployments. MongoDB Agent\s might use TLS (Transport Layer Security) certificates if you *don't* set the `mongod` `tlsMode` to `None`. |
    | Required | Every MongoDB deployment in this project starts with TLS (Transport Layer Security)\-encrypted network connections. All Agents must use TLS (Transport Layer Security) to connect to any MongoDB deployment. |

**Step 3: Choose the authentication mechanism.**

In the MongoDB Deployment Authentication Mechanism section, 
select X.509 Client Certificate (MONGODB-X509).

**Important:**

If you are not using LDAP authorization, you must add users to the 
`$external` database in your MongoDB deployment. For an example, see 
x.509 Client Certificate Authentication.

**Step 4: Configure the LDAP Authorization Settings.**

**Important:**

Starting with MongoDB 3.4, you can 
authenticate users using LDAP, Kerberos, and X.509 certificates 
without requiring local user documents in the `$external` 
database as long as you enable LDAP authorization first. When such a user successfully
authenticates, MongoDB performs a query against the LDAP server to
retrieve all groups which that LDAP user possesses and transforms those
groups into their equivalent MongoDB roles.

Skip this step if you don't want to enable LDAP authorization.

a. Enter values for the following fields:

   | Setting | Value |
   |---|---|
   | LDAP Authorization | Toggle to ON to enable LDAP authorization. |
   | Authorization Query Template | Specify a template for an LDAP query URL to retrieve a list of LDAP groups for an LDAP user. |

**Step 5: Configure X.509 Client Certificate (MONGODB-X509) for the Agents.**

You can enable more than one authentication mechanism for your MongoDB
deployment, but the Ops Manager Agents can only use *one* authentication
mechanism. Select X.509 Client Certificate (MONGODB-X509) to connect to your MongoDB deployment.

a. Select the X.509 Client Certificate (MONGODB-X509) option from the Agent Auth Mechanism 
   section.

b. Provide credentials for the MongoDB Agent:

   | Setting | Value |
   |---|---|
   | MongoDB Agent Username | Enter the LDAPv3 distinguished name derived from the Agent's PEM Key file. |
   | MongoDB Agent Certificate File | Provide the path and filename for the Agent's PEM Key file on the server on the line for the appropriate operating system. |
   | MongoDB Agent Certificate Password | Provide the password to the PEM Key file if it was encrypted. |

**Step 6: Click Save Settings.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 9: Create MongoDB Roles for LDAP Groups. (Optional)**

After enabling LDAP Authorization, you need to 
create custom MongoDB roles 
for each LDAP Group you specified for LDAP Authorization.
