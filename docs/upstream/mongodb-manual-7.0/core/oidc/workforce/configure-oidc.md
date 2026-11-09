<!-- Converted from core/oidc/workforce/configure-oidc.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB with Workforce Identity Federation

Configure MongoDB with Workforce Identity Federation to authenticate users 
across different platforms using a single set of credentials. This 
enhances security and simplifies user management. 

**Important:**

(Include not available offline: includes/fact-OIDC-linux-only.rst)

## Before you Begin

- Ensure that you are on MongoDB Enterprise. 

  To verify that you are using MongoDB Enterprise, pass the `--version`
  command line option to the `mongod` or `mongos`:

  ```bash
  mongod --version
  ```

  In the output from this command, look for the string ``modules:
  subscription` or `modules: enterprise`` to confirm you are using the
  MongoDB Enterprise binaries.

- Configure your external identity provider. For more details, see 
  workforce-external-provider. 

## Steps

**Step 1: Configure the MongoDB server with OpenID Connect (OIDC)**

**Note:**

When configuring MongoDB for Workforce Identity Federation,
omit the `supportsHumanFlows` field in
`oidcIdentityProviders`.

You can configure the MongoDB server using your configuration file or 
command line.

**config file:**

To use your configuration file, specify these parameters in
the file: 

```yaml
setParameter:
   authenticationMechanisms: "MONGODB-OIDC,SCRAM-SHA-256"
   oidcIdentityProviders: |
      [
        {
          "issuer": "https://okta-test.okta.com",
          "audience": "example@kernel.mongodb.com",
          "authNamePrefix": "okta-issuer",
          "authorizationClaim": "groups",
          "clientId": "0zzw3ggfd2ase33"
        }
      ]
```

To specify multiple identity providers, add additional
objects to the `oidcIdentityProviders` array. When you
specify multiple identity providers, you must specify a
`matchPattern` for each provider. For example:

```yaml
setParameter:
   authenticationMechanisms: "MONGODB-OIDC,SCRAM-SHA-256"
   oidcIdentityProviders: |
      [
        {
          "issuer": "https://okta-test.okta.com",
          "audience": "example@kernel.mongodb.com",
          "authNamePrefix": "okta-issuer",
          "authorizationClaim": "groups",
          "matchPattern": "@okta.com$",
          "clientId": "0zzw3ggfd2ase33"
        },
        {
          "issuer": "https://azure-test.azure.com",
          "audience": "example2@kernel.mongodb.com",
          "authNamePrefix": "azure-issuer",
          "authorizationClaim": "groups",
          "matchPattern": "@azure.com$",
          "clientId": "1zzw3ggfd2ase33"
        }
      ]
```

**command line:**

To use the command line, specify the following startup
options: 

```sh
mongod --auth --setParameter authenticationMechanisms=MONGODB-OIDC,SCRAM-SHA-256 --setParameter \ 
'oidcIdentityProviders=[ { 
   "issuer": "https://okta-test.okta.com", 
   "audience": "example@kernel.mongodb.com",
   "authNamePrefix": "okta-issuer",
   "authorizationClaim": "groups",
   "clientId": "0zzw3ggfd2ase33",
} ]'
```

To specify multiple identity providers, add additional
objects to the `oidcIdentityProviders` array. When you
specify multiple identity providers, you must specify a
`matchPattern` for each provider. For example:

```sh
mongod --auth --setParameter authenticationMechanisms=MONGODB-OIDC,SCRAM-SHA-256 --setParameter \ 
'oidcIdentityProviders=[ {
   "issuer": "https://okta-test.okta.com", 
   "audience": "example@kernel.mongodb.com", 
   "authNamePrefix": "okta-issuer",
   "authorizationClaim": "groups",
   "matchPattern": "@okta.com$",
   "clientId": "0zzw3ggfd2ase33", 
}, {
   "issuer": "https://azure-test.azure.com", 
   "audience": "example2@kernel.mongodb.com", 
   "authNamePrefix": "azure-issuer", 
   "authorizationClaim": "groups",
   "matchPattern": "@azure.com$", 
   "clientId": "1zzw3ggfd2ase33",       
} ]'
```

**Step 2: *(Optional)* Enable internal authorization**

To enable internal authorization, set the
`useAuthorizationClaim` field of the `oidcIdentityProviders`
parameter to `false`. This setting enables more flexible user
management by relying on user documents rather than authorization
claims from the identity provider.

**Important:**

If `useAuthorizationClaim` is set to `false`, **do not**
include the `authorizationClaim` field.

**update internal auth:**

```yaml
setParameter:
   authenticationMechanisms: "MONGODB-OIDC,SCRAM-SHA-256"
   oidcIdentityProviders: |
      [
        {
          "issuer": "https://okta-test.okta.com",
          "audience": "example@kernel.mongodb.com",
          "authNamePrefix": "okta-issuer",
          "useAuthorizationClaim": false,
          "clientId": "0zzw3ggfd2ase33"
        }
      ]
```

To specify multiple identity providers, add additional
objects to the `oidcIdentityProviders` array. For example:

```yaml
setParameter:
   authenticationMechanisms: "MONGODB-OIDC,SCRAM-SHA-256"
   oidcIdentityProviders: |
      [
        {
          "issuer": "https://okta-test.okta.com",
          "audience": "example@kernel.mongodb.com",
          "authNamePrefix": "okta-issuer",
          "useAuthorizationClaim": false,
          "clientId": "0zzw3ggfd2ase33"
        },
        {
          "issuer": "https://azure-test.azure.com",
          "audience": "example2@kernel.mongodb.com",
          "authNamePrefix": "azure-issuer",
          "useAuthorizationClaim": false,
          "clientId": "1zzw3ggfd2ase33"
        }
      ]
```

**update command line internal auth:**

```
mongod --auth --setParameter authenticationMechanisms=MONGODB-OIDC,SCRAM-SHA-256 --setParameter \ 
'oidcIdentityProviders=[ { 
   "issuer": "https://okta-test.okta.com", 
   "audience": "example@kernel.mongodb.com", 
   "authNamePrefix": "okta-issuer",
   "useAuthorizationClaim": false,
   "clientId": "0zzw3ggfd2ase33"
} ]'
```

To specify multiple identity providers, add additional
objects to the `oidcIdentityProviders` array. For example:

```
mongod --auth --setParameter authenticationMechanisms=MONGODB-OIDC,SCRAM-SHA-256 --setParameter \ 
'oidcIdentityProviders=[ { 
      "issuer": "https://okta-test.okta.com", 
      "audience": "example@kernel.mongodb.com", 
      "authNamePrefix": "okta-issuer", 
      "useAuthorizationClaim": false, 
      "clientId": "0zzw3ggfd2ase33"
   }, {
      "issuer": "https://azure-test.azure.com", 
      "audience": "example2@kernel.mongodb.com", 
      "authNamePrefix": "azure-issuer", 
      "useAuthorizationClaim": false, 
      "clientId": "1zzw3ggfd2ase33"
   } ]'
```

When you set `useAuthorizationClaim` to `false`, users who
authenticate with the `MONGODB-OIDC` mechanism obtain their
authorization rights from a user document in `$external`. The
server searches for a user document with an `_id` matching the
value of the `authNamePrefix/principalName` claim for every OIDC
based authentication attempt for a user of your identity provider.

**Step 3: *(Conditional)* CA Certificates for Internal X509 TLS**

(Include not available offline: includes/oidc-ca-certificates-note.rst)
