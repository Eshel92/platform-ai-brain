<!-- Converted from tutorial/enable-oidc-authentication-for-group.txt (reStructuredText). Includes are inlined. -->

# Enable Authentication and Authorization with OIDC/OAuth 2.0

You can authenticate and authorize access to Ops Manager deployments for both human users 
and applications with your own identity provider that supports OIDC (OpenID Connect) or OAuth 2.0. 

You can use your existing identity provider to configure single-sign-on for 
human user access to Ops Manager deployments with 
Workforce Identity Federation. You can similarly use your existing cloud provider application users, 
such as Azure Service Principals, Azure Managed Identities, or GCP Service 
Accounts, for application access to Ops Manager deployments with Workload Identity Federation.

You can manage authentication all in one place, either using your OIDC (OpenID Connect) 
provider for human user access, or your OAuth 2.0 provider for application 
access. The following table compares the OIDC (OpenID Connect) and OAuth 2.0 access options.

**Note:**

If you already use other authentication mechanisms, such as SCRAM or X.509,
you can continue to use them for database access.

| Authentication method | User type | Supported protocols |
|---|---|---|
| Workforce Identity Federation | Human users | OIDC (OpenID Connect) |
| Workload Identity Federation | Programmatic users | OAuth 2.0 |

     
Choose one of the following tutorials to learn how to configure
Workforce or Workload Identity Federation:

- Workforce Identity Federation (Humans)
- Workload Identity Federation (Applications)
