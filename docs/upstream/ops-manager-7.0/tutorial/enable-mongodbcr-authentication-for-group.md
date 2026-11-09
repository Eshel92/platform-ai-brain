<!-- Converted from tutorial/enable-mongodbcr-authentication-for-group.txt (reStructuredText). Includes are inlined. -->

# Enable Username and Password Authentication for your Ops Manager Project

## Overview

Ops Manager enables you to configure the Authentication Mechanisms that all
clients, including the Ops Manager Agents, use to connect to your MongoDB
deployments. You can enable multiple authentication mechanisms for each
of your projects, but you must choose only one mechanism for the Agents.

MongoDB users can use usernames and passwords to authenticate themselves against a MongoDB database.

| MongoDB Version | Default authentication mechanism |
|---|---|
| MongoDB 4.0 and later | Salted Challenge Response Authentication Mechanism (SCRAM) using the SHA-1 and SHA-256 hashing algorithms (`SCRAM-SHA-1` and `SCRAM-SHA-256`). |
| MongoDB 3.4 to 3.6 | Salted Challenge Response Authentication Mechanism (SCRAM) using the SHA-1 hashing algorithm (`SCRAM-SHA-1`). |

### `SCRAM-SHA-1` and `SCRAM-SHA-256`

SCRAM-SHA-1 (RFC 5802) and
SCRAM-SHA-256  (RFC 7677)
are IETF (Internet Engineering Task Force) standards that define best practice methods for
implementation of challenge-response mechanisms for authenticating
users with passwords.

`SCRAM-SHA-1` and `SCRAM-SHA-256` verify supplied user credentials
using the user's name, password and authentication database. The
authentication database is the database where the user was created.

## Considerations

This tutorial describes how to enable Username and Password
authentication for your Ops Manager MongoDB deployment.

**Note:**

The MongoDB Community version supports Username and Password
authentication and x.509 authentication.

**Note:**

If you want to 
reset Authentication and TLS settings
for your project, first 
unmanage any MongoDB deployments 
that Ops Manager manages in your project.

## Procedure

This procedure describes how to configure and enable username and
password authentication when using Automation. If Ops Manager does not manage
your MongoDB Agents, you must manually configure them to use Usernames
and Passwords. To learn how to configure authentication, see
/tutorial/configure-mongodb-agent-for-scram.

**Note:**

If you configure the Ops Manager application to authenticate using
SCRAM-SHA-256, you cannot deploy pre-4.0 MongoDB clusters.

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

TLS is not required for use with Username/Password (MONGODB-CR/SCRAM-SHA-1) or Username/Password (SCRAM-SHA-256)
authentication.

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

In the MongoDB Deployment Authentication Mechanism
section, select Username/Password (MONGODB-CR/SCRAM-SHA-1) or Username/Password (SCRAM-SHA-256).

**Step 4: Configure Username/Password (MONGODB-CR/SCRAM-SHA-1) or Username/Password (SCRAM-SHA-256) for the Agent.**

You can enable more than one authentication mechanism for your MongoDB
deployment, but the Ops Manager Agents can only use *one* authentication
mechanism.

In the MongoDB Deployment Authentication Mechanism section,
select Username/Password (MONGODB-CR/SCRAM-SHA-1) and/or Username/Password (SCRAM-SHA-256).

Ops Manager automatically generates the Agents' usernames and passwords.

Ops Manager creates users for the agents with the required user roles in
the admin database for each existing deployment in Ops Manager. When you
add a new deployment, Ops Manager creates the required users in the new
deployment.

**Step 5: Click Save Settings.**

**Step 6: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
