<!-- Converted from tutorial/enable-kerberos-authentication-for-group.txt (reStructuredText). Includes are inlined. -->

# Enable Kerberos Authentication for your Ops Manager Project

## Overview

Ops Manager enables you to configure the Authentication Mechanisms that all
clients, including the Ops Manager Agents, use to connect to your MongoDB
deployments. You can enable multiple authentication mechanisms for each
of your projects, but you must choose only one mechanism for the Agents.

[MongoDB Enterprise](https://www.mongodb.com/products/mongodb-enterprise-advanced)
supports authentication using a Kerberos service. Kerberos is an
industry standard authentication protocol for large client/server
systems.

**Important:**

Setting up and configuring a Kerberos deployment is beyond the scope
of this document. This tutorial assumes you have configured a
Kerberos principal for each Agent and you have a valid
keytab file for each Agent.

To authenticate MongoDB with Kerberos, you must:

1. Have a properly configured Kerberos deployment,
2. Configure *Kerberos service principals* for MongoDB, and
3. Add the *Kerberos user principals* for the Agents.

The Kerberos Authentication section of the
MongoDB Manual provides more detail about using MongoDB with Kerberos.

## Considerations

`Kerberos (GSSAPI)` is only available on MongoDB Enterprise builds. If
you have existing deployments running on a MongoDB Community
build, you must upgrade them to MongoDB Enterprise before you can enable
`Kerberos (GSSAPI)` for your Ops Manager project.

This tutorial describes how to enable Kerberos for one of your Ops Manager
projects and how to configure your Ops Manager Agents to connect to your
Kerberos-enabled deployment.

**Note:**

If you want to 
reset Authentication and TLS settings
for your project, first 
unmanage any MongoDB deployments 
that Ops Manager manages in your project.

## Procedures

These procedures describe how to configure and enable Kerberos
authentication when using Automation. If Ops Manager does *not* manage your
Monitoring or Backups, you must manually configure them to
authenticate using Kerberos.

See
/tutorial/configure-mongodb-agent-for-kerberos for instructions.

### Configure an Existing Linux Deployment for Kerberos-based Authentication

If you use Ops Manager to manage existing deployments on Linux in your project, all
MongoDB deployments in the project must be configured for Kerberos
authentication before you can enable Kerberos authentication for your
project.

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

**Step 4: Set the `kerberosKeytab` option.**

If `kerberosKeytab` is not already set:

a. Click Add Option.

b. Expand the Select a Startup Option list.

c. Search for and select the kerberosKeytab option, then 
   click Add.

d. In the kerberosKeytab column, provide the absolute 
   path to the keytab file.

e. Click Save.

When you have configured the Kerberos options for each deployment,
you can proceed to enable Kerberos for your Ops Manager project.

### Enable Kerberos for your Ops Manager Project

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

TLS is not required for use with Kerberos (GSSAPI) authentication.

**Step 3: Choose the authentication mechanism.**

a. In the MongoDB Deployment Authentication Mechanism section,
   select Kerberos (GSSAPI).

b. Input your [SASL Service Name](http://www.iana.org/assignments/gssapi-service-names/gssapi-service-names.xhtml).

   The SASL Service Name is the Kerberos Service Principal Name for mongod
   or mongos.

**Important:**

If you are not using LDAP authorization, you must add users to the 
`$external` database in your MongoDB deployment. For an example, see 
Kerberos Authentication.

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

**Step 5: Configure Kerberos (GSSAPI) for the Agents.**

You can enable more than one authentication mechanism for your
MongoDB deployment, but the Ops Manager Agents can only use *one*
authentication mechanism. Select Kerberos (GSSAPI) to connect to your
MongoDB deployment.

a. Select the Kerberos (GSSAPI) option from the Agent Auth Mechanism 
   section.

b. Provide credentials for the MongoDB Agent:

   If using Linux, configure:

   | Setting | Value |
   |---|---|
   | MongoDB Agent Kerberos Principal | The Kerberos Principal. |
   | MongoDB Agent Keytab Path | The path for the Agent's Keytab. |

   If using Windows, configure:

   | Setting | Value |
   |---|---|
   | MongoDB Agent Username | The Active Directory user name. |
   | MongoDB Agent Password | The Active Directory password. |
   | Domain | The NetBIOS name of a domain in Active Directory Domain Services. Must be in all capital letters. |

**Step 6: Click Save Settings.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 9: Create MongoDB Roles for LDAP Groups. (Optional)**

After enabling LDAP Authorization, you need to 
create custom MongoDB roles 
for each LDAP Group you specified for LDAP Authorization.
