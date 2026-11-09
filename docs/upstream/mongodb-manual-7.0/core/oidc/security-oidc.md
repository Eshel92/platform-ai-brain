<!-- Converted from core/oidc/security-oidc.txt (reStructuredText). Includes are inlined. -->

# Authentication and Authorization with OIDC/OAuth 2.0

MongoDB Enterprise supports OpenID Connect (OIDC) and OAuth 2.0 
authentication and authorization for both human users and applications.
These protocols enable Workforce and Workload Identity Federation, which 
streamline authentication and authorization by integrating with external 
identity providers. This lets you simplify your security management and 
enhance your system's scalability and flexibility.

**Important:**

(Include not available offline: includes/fact-OIDC-linux-only.rst)

## Use Cases

Workload and Workforce Identity Federation use OIDC and OAuth 2.0 as 
follows: 

- Workforce Identity Federation uses OIDC to enable human users to 
  authenticate and get authorized using an external identity provider (IdP).

- Workload Identity Federation uses OAuth 2.0 to enable your applications to 
  access MongoDB using external programmatic identities such as Azure Service 
  Principals, Azure Managed Identities, and Google Service Accounts.

## Behavior

To use Workforce and Workload Identity Federation, you must use MongoDB 
Enterprise and have MongoDB 7.0.11 or later.

To verify that you are using MongoDB Enterprise, pass the `--version`
command line option to the `mongod` or `mongos`:

```bash
mongod --version
```

In the output from this command, look for the string ``modules:
subscription` or `modules: enterprise`` to confirm you are using the
MongoDB Enterprise binaries.

## Get Started

Select an authentication method to get started:

| Authentication method | User type | Supported protocols |
|---|---|---|
| workforce | Human users | OIDC |
| workload | Programmatic users | OAuth 2.0 |
