<!-- Converted from core/oidc/workforce/workforce-external-provider.txt (reStructuredText). Includes are inlined. -->

# Configure OIDC for Workforce Authentication

To configure Workforce Identity Federation with 
OIDC (OpenID Connect), register your OIDC application with an 
external identity provider, such as Okta or Microsoft Entra ID. This 
ensures secure authentication and facilitates user management.

## About this Task

Workforce Identity Federation uses OIDC. You can use any external identity 
provider that supports the OIDC standard.

You can configure your OIDC application for the following grant types:

- Authorization Code Flow with PKCE (Proof Key of Code Exchange)
- Device Authorization Flow

MongoDB recommends that you use Authorization Code Flow with PKCE for increased
security. Use Device Authorization Flow only if your users need
to access the database from machines with no browser.

**Note:**

Workforce Identity Federation supports only JWT (JSON Web Token) for 
authentication. It doesn't support opaque access tokens.

The following procedures provide detailed configuration instructions for Microsoft 
Entra ID and Okta, and generic configuration instructions for other external identity
providers.

## Before you Begin

- To use Okta as an identity provider, you must have an [Okta account](https://www.okta.com/).

- To use Microsoft Entra ID as an identity provider, you must have a [Microsoft Azure account](https://azure.microsoft.com/en-us/get-started/azure-portal).

## Steps

**azure:**

(Include not available offline: includes/oidc-azure-instructions.rst)

**okta:**

(Include not available offline: includes/oidc-okta-instructions.rst)

**generic:**

(Include not available offline: includes/oidc-generic-instructions.rst)

## Next Steps

- configure-oidc
- database-user-workforce

## Learn More

- [Okta account](https://www.okta.com/)
- [Microsoft Azure](https://azure.microsoft.com/en-us/get-started/azure-portal)
