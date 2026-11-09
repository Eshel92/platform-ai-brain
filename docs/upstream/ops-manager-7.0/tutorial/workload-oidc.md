<!-- Converted from tutorial/workload-oidc.txt (reStructuredText). Includes are inlined. -->

# Set up Workload Identity Federation with OAuth 2.0

Workload Identity Federation lets your applications access MongoDB Ops Manager 
deployments using external programmatic identities such as Azure Service 
Principals, Azure Managed Identities and Google Service 
Accounts.

## How it Works

Workload Identity Federation allows your applications access to MongoDB 
deployments with OAuth 2.0 access tokens. The access tokens can be issued by 
any external Identity Provider including Azure Entra ID and Google Cloud 
Platform. Ops Manager stores the user identifiers and privileges, but 
not the secrets. This authentication mechanism for your applications 
is only supported by certain MongoDB drivers. 

MongoDB Drivers support two types of authentication flow for Workload Identity Federation: 
Built-in Authentication and Callback Authentication. 

### Built-in Authentication

You can use built-in authentication if you deploy your application on a 
supported infrastructure with a supported principal type. Your application 
can access Ops Manager deployments without supplying a password or 
manually requesting a JWT (JSON Web Token) from your cloud provider's metadata service. Instead, 
your chosen MongoDB driver uses your existing principal identifier to request a 
JWT access token under the hood, which is then passed to the Ops Manager deployment
automatically when your application connects. 

For more implementation details, see your chosen driver's documentation.

**Built-in Authentication Supported Infrastructure and Principal Types**

| Cloud Provider | Infrastructure Type | Principal Type |
|---|---|---|
| GCP | Compute Engine | GCP Service Accounts |
|  | App Engine Standard Environment |  |
|  | App Engine Flexible Environment |  |
|  | Cloud Functions |  |
|  | Cloud Run |  |
|  | Google Kubernetes Engine |  |
|  | Cloud Build |  |
| Azure | Azure VM | Azure Managed Identities (User and System assigned) |

### Callback Authentication

You can use callback authentication with any service supporting OAuth 2.0 
access tokens. Workload Identity Federation calls a callback method, in which you can request 
the required JWT (JSON Web Token) from your authorization server or cloud provider that you must 
pass when your application connects to Ops Manager with Workload Identity Federation. 

Please review your chosen driver's 
documentation for additional implementation details. 

## Required Access

To configure Workload Identity Federation, you must have
`Project Owner` access to Ops Manager.

## Prerequisites

You must have the following:

- MongoDB 7.0 or later.
- At least one other authentication mechanism with MongoDB Agent configured.

  **Note:**

  The MongoDB Agent cannot connect to your deployment via OIDC (OpenID Connect). You must
  enable an additional auth mechanism for the MongoDB Agent. If Ops Manager 
  doesn't manage Monitoring or Backup, you must manually configure
  them to use the alternative authentication mechanism.

## Procedures

To configure Workload Identity Federation, complete the following steps:

1. Configure a Workload Identity Provider (one-time setup).
   
   a. Configure your external identity provider.

   b. Configure workload Identity Provider in Ops Manager.

2. Grant external identities (user principals) or groups access.

3. Authenticate to your Ops Manager deployment.

### Configure An External Identity Provider Application

**Note:**

If you want to 
reset Authentication and TLS settings
for your project, first 
unmanage any MongoDB deployments 
that Ops Manager manages in your project.

**azure-oauth:**

In order to access Ops Manager deployments with Azure Managed Identities 
or Azure Service Principals, you need to register an Azure Entra ID 
application. If you have an existing application registration for 
Workload (human user) access,
we recommended that you register a separate application for Workload access.

**Step 1: Register an application.**

a. Navigate to App registrations.

   i. In your [Azure portal](https://portal.azure.com/) account, search and click Microsoft Entra ID.

   #. In the Manage section of the left navigation, click App registrations.

#. Click New registration.

#. Apply the following values.

   | Field | Value |
   |---|---|
   | Name | Ops Manager Database - Workload |
   | Supported Account Types | Accounts in this organizational directory only (single tenant) |
   | Redirect URI | Web |

**Step 2: (Optional) Add groups claim.**

It is a best practice to use service principal identifiers as MongoDB user 
identifiers while defining access rights in Ops Manager. If you plan to 
use this common approach, skip this step. However, if you prefer to use 
group identifiers such as Microsoft Entra ID Security Group identifier 
instead, you can set groups claim in your application registration 
with below steps.

a. Navigate to Token Configuration.

   In the Manage section of the left navigation,
   click Token Configuration.

#. Click Add groups claim.

#. In the Edit groups claim modal, select
   Security.

   What groups you select depend on the type of groups you configured
   in your Azure environment. You may need to select a different
   type of group to send the appropriate group information.

#. In the Customize token properties by type section, ensure that you only select Group ID.

   When you select Group Id, Azure sends the
   security group's Object ID.

#. Click Add.

   To learn more about adding a group claim, see [Azure Documentation](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/connect/how-to-connect-fed-group-claims).

**Step 3: Enable an Application ID URI.**

a. Navigate to Expose an API 
   in the left sidebar and enable Application ID URI.

#. Enable an Application ID URI.

   i. Keep the default Application ID URI assigned by Azure, 
      which is `<application_client_id>`. Copy and store this value, 
      as Ops Manager and all MongoDB drivers require this value 
      for Workload Identity Federation configuration.

**Step 4: Update the manifest.**

a. In the Manage section of the left navigation, click Manifest.

#. Update the accessTokenAcceptedVersion from `null` to `2`.

   The number `2` represents Version 2 of Microsoft's access
   tokens. Other applications can use this as a signed
   attestation of the Active Directory-managed user's identity.
   Version 2 ensures that the token is a JSON Web Token that
   MongoDB understands.

#. Click Save.

To learn more about adding an optional claim, see [Azure Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest).

**Step 5: Remember metadata.**

a. In the left navigation, click Overview.

#. In the top navigation, click Endpoints.

   Copy the OpenID Connect metadata document value 
   without the `/.well-known/openid-configuration` part.

   You can also retrieve this value by following the
   OpenID Connect metadata document URL (Uniform Resource Locator) and
   copying the value for `issuer`.

The following table shows what Ops Manager Configuration Properties that 
these Microsoft Entra ID UI values map to.

| Microsoft Entra ID UI | Ops Manager Configuration Property |
|---|---|
| OpenID Connect metadata document (without /.well-known/openid-configuration) | Issuer URI. |
| Application ID URI (<Application ID>) | Audience |

**gcp-oauth:**

You don't need to make any configuration changes in your GCP (Google Cloud Platform) account.

### Configure Workload Identity Federation Authentication

  

**Note:**

Workload Identity Federation supports only JWT for authentication. It doesn't 
support opaque access tokens.

**azure-oauth:**

To configure a Workload Identity Federation Identity Provider with Azure Entra ID in Ops Manager:

**Step 1: Navigate to the Security Settings dialog for your deployment.**

a. Select the organization that
   contains your project from the `office` Organizations menu in the
   navigation bar.

#. Select your project
   from the Projects menu in the navigation bar.

#. Click Deployment in 
   the sidebar.
#. Click the Security tab.
#. Click the Settings tab.
#. Perform one of the following actions:

   - If this is your first time configuring TLS (Transport Layer Security),
     authentication, or authorization settings for this project, click
     Get Started.
   - If you have already configured TLS (Transport Layer Security) authentication, or
     authorization settings for this project, click Edit.

**Step 2: Optional: Specify the TLS (Transport Layer Security) Settings.**

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

* - Cluster TLS CA File Path
  - The `.pem` file that contains the root certificate chain from the Certificate Authority
    used to validate the certificate presented by a client establishing a connection.
    Specify the file name of the `.pem` file using relative or absolute paths.
    `net.tls.clusterCAFile` requires that `net.tls.CAFile` is set.

    If you do not specify the `net.tls.clusterCAFile`, the cluster uses the `.pem` file specified in the
    `net.tls.CAFile` option.

    `net.tls.clusterCAFile` lets you use separate Certificate
    Authorities to verify the client-to-server and server-to-client
    portions of the TLS handshake.

* - Client Certificate Mode
  - Select if client applications or MongoDB Agent\s must present a
    TLS (Transport Layer Security) certificate when connecting to TLS (Transport Layer Security)\-enabled MongoDB
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
select Federated Auth (OIDC).

**Step 4: Create a new OIDC (OpenID Connect) IdP (Identity Provider) configuration.**

a. In the OIDC Connection and Authorization (Required for OIDC) section, 
   click + OIDC IdP Configuration.

#. In the OIDC Protocol Settings dialog box, select
   Workload Identity Federation.

**Step 5: Enter the following settings.**

* - Setting
  - Necessity
  - Value

* - Configuration Name
  - Required
  - Unique label that identifies this configuration. This label
    is visible to your Ops Manager users and is used
    when creating users and roles
    for authorization. It is case-sensitive and can 
    only contain the following characters:

    - alphanumeric characters 
      (combination of `a` to `z` and `0` to `9`)
    - hyphens (`-`)
    - underscores (`_`)

    After saving the configuration, 
    you can't edit the configuration name.

* - Issuer URI
  - Required
  - Issuer value provided by your registered IdP (Identity Provider) application.
    Using this URI, MongoDB finds an OpenID Provider Configuration
    Document, which should be available in the
    `/.wellknown/open-id-configuration` endpoint.

* - Audience
  - Required
  - Entity that your external identity provider intends the token for. Enter
    the `audience` value from the app you registered
    with external Identity Provider.

* - Authorization Type
  - Required
  - Select `Group Membership` to grant authorization based on IdP (Identity Provider) 
    user group membership, or select `User ID` to grant an individual 
    user authorization.

    It is more common to use `User ID` for application access. 

* - Customize User Claim
  - Required
  - The identifier of the claim that includes the user principal
    identity. Accept the default value unless your IdP (Identity Provider) uses a
    different claim.

    *Default*: `sub`

* - Customize Group Claim
  - Required
  - Required if you select `Group Membership` as the authorization type. 
    The identifier of the claim that includes the principal's IdP (Identity Provider)
    user group membership information. Accept the default value
    unless your IdP (Identity Provider) uses a different claim, or you need a custom 
    claim. 

    *Default*: `groups`

**Step 6: Click Save Configuration.**

Ops Manager saves the configuration and lists it
in the OIDC Connection and Authorization
(Required for OIDC) section.

**Step 7: Click Save Settings.**

**Step 8: Click Review & Deploy to review your changes.**

**Step 9: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**GCP-oauth:**

To configure a Workload Identity Federation Identity Provider with GCP (Google Cloud Platform) in Ops Manager:

**Step 1: Navigate to the Security Settings dialog for your deployment.**

a. Select the organization that
   contains your project from the `office` Organizations menu in the
   navigation bar.

#. Select your project
   from the Projects menu in the navigation bar.

#. Click Deployment in 
   the sidebar.
#. Click the Security tab.
#. Click the Settings tab.
#. Perform one of the following actions:

   - If this is your first time configuring TLS (Transport Layer Security),
     authentication, or authorization settings for this project, click
     Get Started.
   - If you have already configured TLS (Transport Layer Security) authentication, or
     authorization settings for this project, click Edit.

**Step 2: Optional: Specify the TLS (Transport Layer Security) Settings.**

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

* - Cluster TLS CA File Path
  - The `.pem` file that contains the root certificate chain from the Certificate Authority
    used to validate the certificate presented by a client establishing a connection.
    Specify the file name of the `.pem` file using relative or absolute paths.
    `net.tls.clusterCAFile` requires that `net.tls.CAFile` is set.

    If you do not specify the `net.tls.clusterCAFile`, the cluster uses the `.pem` file specified in the
    `net.tls.CAFile` option.

    `net.tls.clusterCAFile` lets you use separate Certificate
    Authorities to verify the client-to-server and server-to-client
    portions of the TLS handshake.

* - Client Certificate Mode
  - Select if client applications or MongoDB Agent\s must present a
    TLS (Transport Layer Security) certificate when connecting to TLS (Transport Layer Security)\-enabled MongoDB
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
select Federated Auth (OIDC).

**Step 4: Create a new OIDC (OpenID Connect) IdP (Identity Provider) configuration.**

a. In the OIDC Connection and Authorization (Required for OIDC) section, 
   click + OIDC IdP Configuration.

#. In the OIDC Protocol Settings dialog box, select
   Workload Identity Federation.

**Step 5: Enter the following settings.**

* - Setting
  - Necessity
  - Value

* - Configuration Name
  - Required
  - Unique label that identifies this configuration. This label
    is visible to your Ops Manager users and is used
    when creating users and roles
    for authorization. It is case-sensitive and can 
    only contain the following characters:

    - alphanumeric characters 
      (combination of `a` to `z` and `0` to `9`)
    - hyphens (`-`)
    - underscores (`_`)

    After saving the configuration, 
    you can't edit the configuration name.

* - Issuer URI
  - Required
  - Enter the URI `https://accounts.google.com`.

* - Audience
  - Required
  - Specify any custom value. Audience is used while calling MongoDB drivers.

* - Authorization Type
  - Required
  - Select `Group Membership` to grant authorization based on IdP (Identity Provider) 
    user group membership, or select `User ID` to grant an individual 
    user authorization.

    It is more common to use `User ID` for application access. 

* - Customize User Claim
  - Required
  - Don't modify the default value, `sub`.

    *Default*: `sub`

**Step 6: Click Save Configuration.**

Ops Manager saves the configuration and lists it
in the OIDC Connection and Authorization
(Required for OIDC) section.

**Step 7: Click Save Settings.**

**Step 8: Click Review & Deploy to review your changes.**

**Step 9: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

### Configure OIDC Authorization

MongoDB does not explicitly create database users for OIDC (OpenID Connect). It maps
OIDC (OpenID Connect) users to MongoDB roles based on the configuration.

Select a tab depending on the authorization type that you selected
when configuring OIDC authentication.
            

**user:**

If you selected the `User ID` authorization type, 
create a new user to grant an individual user authorization:

**Step 1: Navigate to the MongoDB Users tab for your deployment.**

a. Select the organization that
   contains your project from the `office` Organizations menu in the
   navigation bar.

#. Select your project
   from the Projects menu in the navigation bar.

#. Click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click the MongoDB Users tab.

**Step 3: Click Add New User.**

**Step 4: Add the OIDC user.**

**Note:**

Before you add users, ensure that you've 
created any roles
that you want to assign to the users.

a. Complete the user account fields:

   * - Field
     - Description

   * - Identifier

     - 
       - In the first field, enter the `$external` database.

       - In the second field, enter a username using your OIDC (OpenID Connect) IdP (Identity Provider) configuration
         name and the user principal claim from your configuration separated by a slash `/`:

         ```none
         {configuration_name}/{user_principal_claim}
         ```

   * - Roles

     - Enter any available user-defined roles and built-in
       roles into this box. The combo 
       box provides a list of existing roles when you click in it.

   * - Authentication Restrictions

     - 
       a. Click Add Entry.

       b. Add one or more IP (Internet Protocol) addresses and/or CIDR (Classless Inter-Domain Routing) blocks in 
          either the Client Source or Server 
          Address boxes. Separate multiple addresses or blocks with 
          commas.

          - Client Source restricts which addresses this 
            user can authenticate and use the given roles.

          - Server Address restricts the addresses this 
            user can authenticate and has the given roles.

       c. Click Save.

       d. To add another entry, click Add Entry.

#. Click Add User.

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**group:**

If you selected the `Group Membership` authorization type,
complete the following steps to create a custom role that grants
authorization based on IdP (Identity Provider) user group membership:

**Step 1: Navigate to the MongoDB Roles tab for your deployment.**

a. Select the organization that
   contains your project from the `office` Organizations menu in the
   navigation bar.

#. Select your project
   from the Projects menu in the navigation bar.

#. Click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click the MongoDB Roles tab.

**Step 2: Click Add New Role.**

**Step 3: Create the OIDC role.**

a. Enter the following fields:

   * - Field
     - Necessity
     - Description

   * - Identifier
     - Required
     - In the Database box, enter `admin`.

       In the Name box, enter your OIDC (OpenID Connect) IdP (Identity Provider) configuration
       name and the group name from your external identity provider,
       separated by a slash `/`:

       ```none
       {configuration_name}/{group_name}
       ```

   * - Inherits From
     - Optional
     - A list of role name and database pairs. The format for these
       pairs are `roleName@dbName`.

   * - Authentication Restrictions
     - Optional
     - A list of IP addresses or CIDR notations that you want to
       restrict from your IdP (Identity Provider).

   * - Privilege Actions by Resource
     - Optional
     - Actions permitted on the resource.

       To learn more, see Privilege Actions.

#. Click Add Role. 

### Connect an Application to MongoDB with Workload Identity Federation

Use the following MongoDB Drivers to connect an application to MongoDB
with Workload Identity Federation authentication:

- Java
- `C#/.NET`
- `Go`
- PyMongo
- Node / `Typescript`
- `Kotlin`
- Scala

## Manage an Existing Workload Identity Federation Configuration

To manage your Workload Identity Federation configuration,
you can perform the following actions.

### Revoke JWKS

**Note:**

Don't use this feature to rotate your signing keys. When you rotate 
your OIDC (OpenID Connect) IdP (Identity Provider) signing keys, MongoDB fetches the JWKS automatically
upon expiration of the existing access tokens.

If your private key is compromised, you can immediately revoke your JSON
Web Key Sets (JWKS) cached in MongoDB nodes:

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

**Step 2: Revoke your JWKS token.**

a. Scroll to the OIDC Connection and Authorization
   (Required for OIDC) section.

#. Click the REVOKE JWKS button.

#. In the Revoke JWKS tokens? dialog box, click Revoke.

### Edit a Configuration

To edit your Workload Identity Federation configuration:

**Step 1: Navigate to the Security Settings dialog for your deployment.**

a. Select the organization that
   contains your project from the `office` Organizations menu in the
   navigation bar.

#. Select your project
   from the Projects menu in the navigation bar.

#. Cick Deployment in 
   the sidebar.
#. Click the Security tab.
#. Click the Settings tab.

**Step 2: Edit the configuration.**

a. Scroll to the OIDC Connection and Authorization
   (Required for OIDC) section.

#. For the configuration that you want to edit, click the
   EDIT button.

#. Make changes to the configuration.

**Step 3: Click Save Configuration.**

**Step 4: Click Save Settings.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
      

### Delete a Configuration

To delete your Workload Identity Federation configuration:

**Step 1: Navigate to the Security Settings dialog for your deployment.**

a. Select the organization that
   contains your project from the `office` Organizations menu in the
   navigation bar.

#. Select your project
   from the Projects menu in the navigation bar.

#. Click Deployment in 
   the sidebar.
#. Click the Security tab.
#. Click the Settings tab.

**Step 2: Remove the configuration.**

a. Scroll to the OIDC Connection and Authorization
   (Required for OIDC) section.

#. For the configuration that you want to delete, click the
   REMOVE button.

#. In the Removing OIDC IdP configuration? dialog box, 
   click Remove.
