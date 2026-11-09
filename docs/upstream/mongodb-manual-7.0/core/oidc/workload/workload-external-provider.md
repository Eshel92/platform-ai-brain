<!-- Converted from core/oidc/workload/workload-external-provider.txt (reStructuredText). Includes are inlined. -->

# Configure Workload Identity Federation

To configure Workload Identity Federation using OAuth 2.0, register your 
OAuth 2.0 application with an external identity provider like Microsoft 
Azure or Google Cloud Platform (GCP). This enables secure authentication 
and streamlines user management.

## About this Task

Workload Identity Federation uses OAuth2.0 access tokens. These tokens 
can be issued by any external identity provider.

The following procedures configure Microsoft Azure Entra 
ID and Google Cloud Platform as external identity providers for 
MongoDB.

## Before you Begin

- To use Microsoft Azure as an identity provider, you must have a [Microsoft Azure account](https://azure.microsoft.com/en-us/get-started/azure-portal).

- To use Google Cloud as an identity provider, you must have a [Google Cloud account](https://cloud.google.com). 

## Steps

**azure-oauth:**

In order to access self-managed MongoDB instances with Azure 
Managed Identities or Azure Service Principals, you need to 
register an Azure Entra ID application. If you have an existing 
application registration for Workforce 
(human user) access, we recommended that you register a separate 
application for Workload access.

**Step 1: Register an application**

1. Navigate to App registrations.

   a. In your [Azure portal](https://portal.azure.com/) 
      account, search and click Microsoft Entra ID.

   #. In the Manage section of the left navigation, 
      click App registrations.

#. Click New registration.

#. Apply the following values.

   | Field | Value |
   |---|---|
   | Name | MongoDB - Workload |
   | Supported Account Types | Accounts in this organizational directory only (single tenant) |
   | Redirect URI | Web |

**Step 2: (Optional) Add groups claim**

For application access, it is a best practice to use service 
principal identifiers as MongoDB user identifiers while defining 
access rights in self-managed MongoDB deployments. If you plan to 
use this common approach, skip this step. However, if you prefer to 
use group identifiers such as Azure AD Security Group identifier 
instead, you can set groups claim in your application registration 
with below steps.

1. Navigate to Token Configuration.

   In the Manage section of the left navigation,
   click Token Configuration.

#. Click Add groups claim.

#. In the Edit groups claim modal, select Security.

   What groups you select depend on the type of groups you configured
   in your Azure environment. You may need to select a different
   type of group to send the appropriate group information.

#. In the Customize token properties by type section, ensure that 
   you only select Group ID.

   When you select Group ID, Azure sends the
   security group's Object ID.

#. Click Add.

   To learn more about adding a group claim, see 
   [Azure Documentation](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/connect/how-to-connect-fed-group-claims).

**Step 3: Enable an Application ID URI**

1. Navigate to Expose an API 
   in the left sidebar and enable Application ID URI.

#. Enable an Application ID URI.

   Keep the default Application ID URI assigned by Azure, 
   which is `<application_client_id>`. Copy and store this value, 
   as self-managed MongoDB deployments and all MongoDB drivers require 
   this value for Workload Identity Federation configuration.

**Step 4: Update the manifest**

1. In the Manage section of the left navigation, click Manifest.

#. Update the requestedAccessTokenVersion from `null` to `2`.

   The number `2` represents Version 2 of Microsoft's access
   tokens. Other applications can use this as proof of 
   the Active Directory-managed user's identity.
   Version 2 ensures that the token is a JSON Web Token that
   MongoDB understands.

#. Click Save.

To learn more about adding an optional claim, see [Azure Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest).

**Step 5: Remember metadata**

1. In the left navigation, click Overview.

#. In the top navigation, click Endpoints.

   Copy the OpenID Connect metadata document value, 
   excluding `/.well-known/openid-configuration`.

   You can also retrieve this value by following the
   OpenID Connect metadata document URL 
   and copying the value for `issuer`.

The following table shows what these Microsoft Entra ID UI values 
map to in the MongoDB `oidcIdentityProviders` 
parameter:

| Microsoft Entra ID UI | MongoDB `oidcIdentityProviders` Parameter Field |
|---|---|
| OpenID Connect metadata document (without /.well-known/openid-configuration) | `issuer` |
| Application ID URI | `audience` |

**gcp-oauth:**

You don't need to make any configuration changes in your Google 
Cloud service account.
