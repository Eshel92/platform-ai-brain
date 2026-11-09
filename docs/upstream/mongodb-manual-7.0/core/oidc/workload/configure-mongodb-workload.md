<!-- Converted from core/oidc/workload/configure-mongodb-workload.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB with Workload Identity Federation

Configure MongoDB with Workload Identity Federation to authenticate 
services across different platforms. This enhances security and simplifies 
service identity management.

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
  workload-external-provider. 

## Steps

**Step 1: Configure the MongoDB server with OpenID Connect (OIDC)**

To configure the MongoDB server, enable the MONGODB-OIDC authentication mechanism and use the
`oidcIdentityProviders` to specify identity provider
(IDP) configurations.

**Note:**

When configuring MongoDB for Workload Identity Federation, set
the `supportsHumanFlows` field in
`oidcIdentityProviders` to `false`.

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
          "supportsHumanFlows": false
        }
      ]
```

To specify multiple identity providers, add additional
objects to the `oidcIdentityProviders` array. For example:

```javascript
setParameter:
   authenticationMechanisms: "MONGODB-OIDC,SCRAM-SHA-256"
   oidcIdentityProviders: |
      [
        {
          "issuer": "https://okta-test.okta.com",
          "audience": "example@kernel.mongodb.com",
          "authNamePrefix": "okta-issuer",
          "authorizationClaim": "groups",
          "supportsHumanFlows": false
        },
        {
          "issuer": "https://azure-test.azure.com",
          "audience": "example2@kernel.mongodb.com",
          "authNamePrefix": "azure-issuer",
          "authorizationClaim": "groups",
          "supportsHumanFlows": false
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
   "supportsHumanFlows": false
} ]'
```

To specify multiple identity providers, add additional
objects to the `oidcIdentityProviders` array. For example:

```sh
mongod --auth --setParameter authenticationMechanisms=MONGODB-OIDC,SCRAM-SHA-256 --setParameter \ 
'oidcIdentityProviders=[ {
   "issuer": "https://okta-test.okta.com", 
   "audience": "example@kernel.mongodb.com", 
   "authNamePrefix": "okta-issuer",
   "authorizationClaim": "groups",
   "supportsHumanFlows": false
}, {
   "issuer": "https://azure-test.azure.com", 
   "audience": "example2@kernel.mongodb.com", 
   "authNamePrefix": "azure-issuer", 
   "authorizationClaim": "groups",
   "supportsHumanFlows": false    
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
          "supportsHumanFlows": false
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
          "supportsHumanFlows": false
        },
        {
          "issuer": "https://azure-test.azure.com",
          "audience": "example2@kernel.mongodb.com",
          "authNamePrefix": "azure-issuer",
          "useAuthorizationClaim": false,
          "supportsHumanFlows": false
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
   "supportsHumanFlows": false
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
      "supportsHumanFlows": false
   }, {
      "issuer": "https://azure-test.azure.com",
      "audience": "example2@kernel.mongodb.com",
      "authNamePrefix": "azure-issuer",
      "useAuthorizationClaim": false,
      "supportsHumanFlows": false
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

## Next Steps

- database-user-workload

## Learn More

- OpenID Connect Authentication
