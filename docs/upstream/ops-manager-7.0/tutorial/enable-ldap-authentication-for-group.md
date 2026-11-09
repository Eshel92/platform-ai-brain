<!-- Converted from tutorial/enable-ldap-authentication-for-group.txt (reStructuredText). Includes are inlined. -->

# Enable LDAP Authentication for your Ops Manager Project

Ops Manager enables you to configure the Authentication Mechanisms that all
clients, including the Ops Manager Agents, use to connect to your MongoDB
deployments. You can enable multiple authentication mechanisms for each
of your projects, but you must choose only one mechanism for the Agents.

[MongoDB Enterprise](https://www.mongodb.com/products/mongodb-enterprise-advanced)
supports proxying authentication requests to a Lightweight Directory
Access Protocol (LDAP) service.

`LDAP` is only available on MongoDB Enterprise builds. If
you have existing deployments running on a MongoDB Community
build, you must upgrade them to MongoDB Enterprise before you can enable
`LDAP` for your Ops Manager project.

## Considerations

MongoDB Enterprise supports simple and SASL binding to Lightweight
Directory Access Protocol (LDAP) servers via `saslauthd` and operating system
libraries:

- MongoDB Enterprise for Linux can bind to an LDAP server either via
  `saslauthd` or, starting in MongoDB 3.4, through the operating system
  libraries.

- Starting in MongoDB version 3.4, MongoDB Enterprise for Windows can
  bind to an LDAP server through the operating system libraries.

The LDAP Proxy Authentication and
LDAP Authorization sections in
the MongoDB manual provide more information about LDAP and MongoDB.
Setting up LDAP and SASL is beyond the scope of this document.

## Procedure

This procedure describes how to configure and enable LDAP
authentication when using Automation. If Ops Manager doesn't manage
Monitoring or Backup, you must manually configure them to use
LDAP (Lightweight Directory Access Protocol). To configure LDAP (Lightweight Directory Access Protocol), see
/tutorial/configure-mongodb-agent-for-ldap

**Note:**

If you want to 
reset Authentication and TLS settings
for your project, first 
unmanage any MongoDB deployments 
that Ops Manager manages in your project.

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

**Warning:** Recommend Using TLS (Transport Layer Security)/SSL (Secure Sockets Layer) with LDAP (Lightweight Directory Access Protocol)

By default, LDAP (Lightweight Directory Access Protocol) traffic is sent as plain text. This means that
credentials (username and password) are exposed to basic network
threats like sniffers and replay. Use LDAPS (Secure Lightweight Directory Access Protocol) (LDAP (Lightweight Directory Access Protocol) over 
TLS (Transport Layer Security)/SSL (Secure Sockets Layer)) to encrypt authentication. Many modern directory 
services, such as Active Directory, require encrypted  
connections.

**Step 3: Choose the authentication mechanism.**

a. In the MongoDB Deployment Authentication Mechanism section,
   select LDAP.

b. Select the appropriate type of LDAP authentication.

   **Important:**

   - If you are using LDAP authorization,
     you must select Native LDAP Authentication.
   - If you are not using LDAP authorization, you must add users to the 
     `$external` database in your MongoDB deployment. For an example, see 
     LDAP Authentication. 

**Step 4: Configure the LDAP Authorization Settings. (Optional)**

**Important:**

Starting with MongoDB 3.4, you can 
authenticate users using LDAP, Kerberos, or X.509 certificates 
without requiring local user documents in the `$external` 
database as long as you enable LDAP authorization first. When such a user successfully
authenticates, MongoDB performs a query against the LDAP server to
retrieve all groups which that LDAP user possesses and transforms those
groups into their equivalent MongoDB roles.

MongoDB processes restart in a rolling fashion when you apply 
these changes.

Skip this step if you selected Saslauthd in the previous
step.

If you selected Native LDAP Authentication, complete the following steps:

a. Provide the following values:

   * - Setting

     - Value

   * - Server URL

     - Specify the `hostname:port` combination of one or more LDAP servers.

   * - Transport Security 

     - Select `TLS` to encrypt your LDAP queries. If you do not
       need to encrypt the LDAP queries, select `None`.

   * - Timeout (ms)  

     - Specify how long an authentication request should wait before timing out.

   * - Bind Method  

     - Select either `SASL` or `Simple`. 

       **Important:**

       If you choose the `Simple` bind method, select `TLS`
       from the Transport Security because the
       `Simple` bind method passes the password in plain text.

   * - SASL Mechanisms  

     - Specify which SASL authentication service MongoDB uses with 
       the LDAP server.

   * - Query User (LDAP Bind DN)

     - Specify the LDAP Distinguished Name to which MongoDB binds when 
       connecting to the LDAP server.

   * - Query Password (LDAP Bind DN)

     - Specify the password with which MongoDB binds when connecting to an 
       LDAP server.

   * - LDAP User Cache Invalidation Interval (s)  

     - Specify how long MongoDB waits to flush the LDAP user cache.
       Defaults to `30` seconds.

   * - User to Distinguished Name Mapping

     - Specify an array of JSON documents that provide the ordered
       transformation(s) MongoDB performs on the authenticated MongoDB
       usernames. MongoDB then matches the transformed username 
       against the LDAP DNs.

   * - Validate LDAP Server Config

     - Select `ON` to validate the LDAP server configuration
       or `OFF` to skip validation.

       If `ON` and the configuration is invalid, the MongoDB
       deployment will not start.

#. In the LDAP Authorization section, enter values for the
   following fields:

   | Setting | Value |
   |---|---|
   | LDAP Authorization | Toggle to ON to enable LDAP authorization. |
   | Authorization Query Template | Specify a template for an LDAP query URL to retrieve a list of LDAP groups for an LDAP user. |
   | User to Distinguished Name Mapping | Specify an array of JSON documents that provide the ordered transformation(s) MongoDB performs on the authenticated MongoDB usernames. MongoDB then matches the transformed username against the LDAP DNs. |

**Step 5: Configure the Agents to use LDAP to connect to your MongoDB deployment.**

**Note:** Remember

Ops Manager limits Agents to using one mechanism per deployment.

a. Select the LDAP option from the Agent Auth Mechanism 
   section.

b. Provide credentials for the MongoDB Agent:

   | Setting | Value |
   |---|---|
   | MongoDB Agent Username | Enter the LDAP (Lightweight Directory Access Protocol) username. |
   | MongoDB Agent Password | Enter the password for Agent's LDAP (Lightweight Directory Access Protocol) Username. |
   | MongoDB Agent LDAP Group DN | If you enabled LDAP Authorization, enter the DN (Distinguished Name) of the group of which the MongoDB Agent user is a member. |

**Step 6: Click Save Settings.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 9: Create MongoDB Roles for LDAP Groups. (Optional)**

After enabling LDAP Authorization, you need to 
create custom MongoDB roles 
for each LDAP Group you specified for LDAP Authorization.
