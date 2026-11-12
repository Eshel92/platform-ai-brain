<!-- Part 6 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

## Security Settings

The following security settings apply only to replica set and sharded
cluster resource types:

**`spec.security.tls.ca`**

*Type*: string

Provide the name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that stores the CA (Certificate Authority) for the `MongoDB` resource.

**Important:**

If you use a custom CA (Certificate Authority) to sign your TLS (Transport Layer Security) certificates for the `MongoDB` resource,
you must specify this parameter.

The Kubernetes Operator requires that you name the
`MongoDB` resource certificate `ca-pem` in the ConfigMap.

**`spec.security.certsSecretPrefix`**

*Type*: string

Text to prefix to the Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that you
created that contain your replica set's or sharded cluster's TLS (Transport Layer Security) 
keys and certificates.

You must prefix your secrets with `<prefix>-<metadata.name>`.

For example, if you call your deployment `my-deployment` and you set
the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the
client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, 
you must name the TLS (Transport Layer Security) secret for internal cluster authentication 
(if enabled) `mdb-my-deployment-clusterfile`.

To learn more about naming the secrets that contain your TLS (Transport Layer Security) 
certificates, see the topic in secure-tls that applies to your 
deployment.

**`spec.security.tls.additionalCertificateDomains`**

*Type*: boolean

List of every domain that should be added to TLS (Transport Layer Security) certificates to
each pod in this deployment. When you set this parameter, every CSR (Certificate Signing Request)
that the Kubernetes Operator transforms into a TLS (Transport Layer Security) certificate includes
a SAN (Subject Alternative Name) in the form `<pod name>.<additional cert domain>`.

Replica set resources don't need this parameter. Use
`spec.connectivity.replicaSetHorizons` instead.

**Note:**

If you add this parameter to a TLS (Transport Layer Security)\-enabled resource, Kubernetes
displays an error when the resource reaches the `Pending` state.
This error displays: ``Please manually remove the CSR (Certificate Signing Request) in order
to proceed.`` To remedy this issue:

1. Remove any existing CSR (Certificate Signing Request)\s so that Kubernetes can generate new
   CSR (Certificate Signing Request)\s. To learn how to delete a resource, see the
   `deleting resources` in the
   Kubernetes documentation.

2. Approve the CSR (Certificate Signing Request)\s after Kubernetes generates them.

**`spec.additionalMongodConfig.net.ssl.mode`**

*Type*: string

*Default*: `requireSSL`

Specifies which `sslMode` is used for network connections.
The following are valid options:

| Value | Description |
|---|---|
| `allowSSL` | Connections between servers do not use TLS (Transport Layer Security). For incoming connections, the server accepts both TLS (Transport Layer Security) and non-TLS. |
| `preferSSL` | Connections between servers use TLS (Transport Layer Security). For incoming connections, the server accepts both TLS (Transport Layer Security) and non-TLS. |
| `requireSSL` | The server uses and accepts only TLS (Transport Layer Security) encrypted connections. |

**`spec.additionalMongodConfig.net.tls.disabledProtocols`**

*Type*: string

*New in MongoDB version 4.2.*

Prevents a MongoDB server running with TLS (Transport Layer Security) from accepting incoming connections 
that use a specific protocol or protocols. To specify multiple protocols, enter 
a comma separated list of protocols. For example, `TLS1_0,TLS1_1`.

This setting recognizes the following protocols: `TLS1_0`, `TLS1_1`, `TLS1_2`, 
and starting in MongoDB 4.0.4 (and 3.6.9), `TLS1_3`. If you specify an unrecognized protocol, the 
server won't start.

On macOS, you can't disable `TLS1_1` and enable both `TLS1_0` and `TLS1_2`. 
You must disable at least `TLS1_0` or `TLS1_2` also. For example, `TLS1_0,TLS1_1` 
disables `TLS1_2` on macOS. 

The list of protocols that you disable replaces the default list of disabled protocols.

Starting in MongoDB version 4.0, MongoDB disables the use of TLS (Transport Layer Security) 1.0 if TLS (Transport Layer Security) 1.1+ 
is available on the system. To enable the disabled TLS (Transport Layer Security) 1.0, specify `none` as the value for  
`spec.additionalMongodConfig.net.tls.disabledProtocols`. 

Members of replica sets and sharded clusters must speak at least one protocol in common.

**`spec.security.authentication`**

*Type*: collection

Authentication specifications for your MongoDB deployment.

**`spec.security.authentication.enabled`**

*Type*: boolean

*Default*: `false`

Specifies whether authentication is enabled on the Cloud Manager or Ops Manager
project. If set to `true`, you must set an authentication mechanism in 
`spec.security.authentication.modes`.

**Important:**

The Kubernetes Operator manages authentication for this MongoDB
resource if you include this setting, even if it's set to
`false`. You can't configure authentication for this
resource using the Cloud Manager or Ops Manager UI  or APIs while this setting
exists in the resource specification.

Omit this setting if you want to manage authentication using the
Cloud Manager or Ops Manager UI or APIs.

**`spec.security.authentication.modes`**

*Type*: array

Specifies the authentication mechanism that your MongoDB deployment 
uses. Valid values are `SCRAM`, `SCRAM-SHA-1`, `MONGODB-CR`, 
`X509`, `LDAP`, and `OIDC`. We recommend `SCRAM-SHA-256` (`SCRAM`) 
over `SCRAM-SHA-1`. If you specify `SCRAM-SHA-1`, you must also 
specify `MONGODB-CR`.

**Note:** X.509 Internal Cluster Authentication

To enable X.509 internal cluster authentication for the Cloud Manager or Ops Manager project, set this
value to `["X509"]` and specify the following settings:

- `spec.security.authentication.internalCluster` `: "X509"`
- provide a value for the
  `spec.security.certsSecretPrefix` setting.`

If you provide more than one value for
`spec.security.authentication.modes`, you must also specify a
value for `spec.security.authentication.agents.mode`.

**`spec.security.authentication.internalCluster`**

*Type*: string

Specifies whether X.509 internal cluster authentication is enabled.

To enable X.509 internal cluster authentication, set to `"X509"`.
Requires that the following settings be specified:

- `spec.security.authentication.modes` `: ["X509"]`
- `spec.security.certsSecretPrefix`

The Kubernetes Operator accepts the following values:

- `["X509"]`: X.509 internal cluster authentication is enabled.
- `""` or omitted: internal cluster authentication is not enabled.

**Important:**

After you enable internal cluster authentication, you can't disable
it.

**`spec.security.authentication.requireClientTLSAuthentication`**

*Type*: boolean

*Default*: `false`

Specifies whether the MongoDB host requires clients to connect using a
TLS (Transport Layer Security) certificate. Defaults to `true` if you enable TLS (Transport Layer Security)
authentication.

To enable TLS (Transport Layer Security) authentication, provide a value for the `spec.security.certsSecretPrefix` setting.

**`spec.security.authentication.ldap`**

*Type*: collection

*Required for LDAP authentication.* 

Configures LDAP (Lightweight Directory Access Protocol) authentication for the Cloud Manager or Ops Manager project. To enable
LDAP (Lightweight Directory Access Protocol) authentication, set
`spec.security.authentication.modes` to `["LDAP"]`.

**`spec.security.authentication.ldap.servers`**

*Type*: array of strings

*Required for LDAP authentication.* 

List of hostnames and ports of the LDAP (Lightweight Directory Access Protocol) servers. Specify
hostnames with their respective ports in the following format:

```yaml
spec:
  security:
    authentication:
      ldap:
        servers: 
          - "<hostname1>:<port1>"
          - "<hostname2>:<port2>"
```

**`spec.security.authentication.ldap.timeoutMS`**

*Type*: integer

Specifies how many milliseconds an authentication request should 
wait before timing out.

**`spec.security.authentication.ldap.transportSecurity`**

*Type*: string

*Required for LDAP authentication.* 

Specifies whether the LDAP (Lightweight Directory Access Protocol) server accepts TLS (Transport Layer Security).

If the LDAP (Lightweight Directory Access Protocol) server accepts TLS (Transport Layer Security), set the value to `tls`. If 
the LDAP (Lightweight Directory Access Protocol) server doesn't accept TLS (Transport Layer Security), leave this value blank or set 
the value to `none`.

**Note:**

If you specify a string other than `none` or `tls`, 
Kubernetes Operator still sets the setting to `tls`.

**`spec.security.authentication.ldap.caConfigMapRef`**

*Type*: collection

*Required for LDAP authentication with TLS.* 

[ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a CA (Certificate Authority) which validates the LDAP (Lightweight Directory Access Protocol) 
server's TLS (Transport Layer Security) certificate.

**`spec.security.authentication.ldap.caConfigMapRef.name`**

*Type*: string

*Required for LDAP authentication with TLS.* 

Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a CA (Certificate Authority) which validates
the LDAP (Lightweight Directory Access Protocol) server's TLS (Transport Layer Security) certificate.

**`spec.security.authentication.ldap.caConfigMapRef.key`**

*Type*: string

*Required for LDAP authentication with TLS.* 

Field name that stores the CA (Certificate Authority) which validates the LDAP (Lightweight Directory Access Protocol)
server's TLS (Transport Layer Security) certificate.

**`spec.security.authentication.ldap.bindQueryUser`**

*Type*: string

*Required for LDAP authentication.* 

LDAP (Lightweight Directory Access Protocol) Distinguished Name to which MongoDB binds when connecting to
the LDAP (Lightweight Directory Access Protocol) server.

**`spec.security.authentication.ldap.bindQueryPasswordSecretRef`**

*Type*: collection

*Required for LDAP authentication.* 

Specifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password with which
MongoDB binds when connecting to the LDAP (Lightweight Directory Access Protocol) server.

**`spec.security.authentication.ldap.bindQueryPasswordSecretRef.name`**

*Type*: string

*Required for LDAP authentication.* 

Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password with which MongoDB
binds when connecting to the LDAP (Lightweight Directory Access Protocol) server.

The [secret](https://kubernetes.io/docs/concepts/configuration/secret/) must contain only one `password` field which stores
the password.

**`spec.security.authentication.ldap.authzQueryTemplate`**

*Type*: string

*Required for LDAP authorization.*

An [RFC4515](https://tools.ietf.org/html/rfc4515) and [RFC4516](https://tools.ietf.org/html/rfc4516) LDAP-formatted query URL
template executed by MongoDB to obtain the LDAP groups that the user
belongs to. The query is relative to the host or hosts
specified in `spec.security.authentication.ldap.servers`.
You can use the following tokens in the template:

- `{USER}` 
      Substitutes the authenticated username, or the
      `transformed`
      username, into the LDAP query.
- `{PROVIDED_USER}`
      Substitutes the supplied username, before either
      authentication or LDAP transformation, into the LDAP query.
      (*Available starting in MongoDB version 4.2*)

**See also:**

LDAP Query Templates in the MongoDB Manual   

**`spec.security.authentication.agents.automationLdapGroupDN`**

*Type*: string

The Distinguished Name (DN) of the LDAP group to which the
MongoDB Agent user belongs.

This setting is required if:

- `spec.security.authentication.ldap.authzQueryTemplate` is
  present, and
- `spec.security.authentication.agents.mode` is `LDAP` or
  `X509`.

**`spec.security.authentication.ldap.userToDNMapping`**

*Type*: string

Maps the username provided to `mongod` or
`mongos` for authentication to a LDAP Distinguished Name
(DN).

**See also:**

security.ldap.userToDNMapping in the MongoDB Manual   

**`spec.security.authentication.ldap.userCacheInvalidationInterval`**

*Type*: integer

Specifies how many seconds MongoDB waits to flush the LDAP user 
cache. Defaults to 30 seconds.

**`spec.security.authentication.oidcProviderConfigs`**

*Type*: collection

*Required*

- MongoDB version has to be 7.0.11+ or 8.0.0+
- MongoDB Enterprise only is supported

**Note:**

At least one element in the collection is required when 
`spec.security.authentication.mode`  is set to `OIDC`.

**`spec.security.authentication.oidcProviderConfigs.audience`**

*Type*: string

*Required*

Entity that your external identity provider (IdP) intends the token for. Enter the 
audience value from the app you registered with your external IdP. 
When more than one IdP is defined, this must be a unique value for each
configuration that shares an `issuerURI`.

**`spec.security.authentication.oidcProviderConfigs.authorizationMethod`**

*Type*: string

*Required*

Valid values are `WorkforceIdentityFederation` and `WorkloadIdentityFederation`. 
Configure single-sign-on for human user access to deployments with Workforce 
Identity Federation. For programmatic application access to deployments, use 
Workload Identity Federation. Only one Workforce Identity Federation IdP can be 
configured per MongoDB resource. To learn more, see [Authentication and Authorization with OIDC/OAuth 2.0](https://www.mongodb.com/docs/manual/core/oidc/security-oidc/).

**`spec.security.authentication.oidcProviderConfigs.authorizationType`**

*Type*: string

*Required*

Valid values are `GroupMembership` and `UserID`. Select `GroupMembership` 
to grant authorization based on IdP user group membership, or select 
`UserID` to grant an individual user authorization.

**`spec.security.authentication.oidcProviderConfigs.clientId`**

*Type*: string

*Required*

Unique identifier for your registered application. Enter the `clientId` 
value from the app you registered with an external Identity Provider.

**`spec.security.authentication.oidcProviderConfigs.configurationName`**

*Type*: string

*Required*

Unique label that identifies this configuration. This label is visible to your 
Ops Manager users and is used when creating users and roles for authorization. 
It is case-sensitive and can only contain the following characters:

- alphanumeric characters (combination of a to z and 0 to 9)
- hyphens (-)
- underscores (_)

**`spec.security.authentication.oidcProviderConfigs.groupsClaim`**

*Type*: string

*Optional*

The identifier of the claim that includes the user principal identity. 
Accept the default value unless your IdP uses a different claim.

**`spec.security.authentication.oidcProviderConfigs.issuerURI`**

*Type*: string

*Required*

Issuer value provided by your registered IdP application. Using this URI, 
MongoDB finds an OpenID Provider Configuration Document, which is 
available in the `/.wellknown/open-id-configuration` endpoint. For MongoDB 
`8.0+`, the combination of `issuerURI` and audience must be unique 
across OIDC provider configurations. For other MongoDB versions, the 
`issuerURI` itself must be unique.

**`spec.security.roleRefs`**

*Type*: array

Array that references `ClusterMongoDBRole` custom resources that give you
fine-grained access control over your MongoDB deployment.

**`spec.security.roleRefs.kind`**

*Type*: string

The kind of the referenced custom resource. For example, `ClusterMongoDBRole`.

**`spec.security.roleRefs.kind`**

*Type*: string

The kind of the referenced custom resource. For example, `ClusterMongoDBRole`.

**`spec.security.authentication.oidcProviderConfigs.requestedScopes`**

*Type*: string

*Optional*

Tokens that give users permission to request data from the authorization 
endpoint. Only used for the Workforce Identity Federation authorization method.

**`spec.security.authentication.oidcProviderConfigs.userClaim`**

*Type*: string

*Required*

The identifier of the claim that includes the user principal 
identity. Accept the default value unless your IdP uses a different claim.

**`spec.security.authentication.agents`**

*Type*: collection

MongoDB Agent authentication configuration for the Cloud Manager or Ops Manager project.

**`spec.security.authentication.agents.mode`**

*Type*: string

The authentication mechanism that the MongoDB Agents for
your MongoDB deployment use. Valid values are `SCRAM`, 
`SCRAM-SHA-1`, `MONGODB-CR`, `X509`, `OIDC`, and
`LDAP`. The value you specify must also be present in
`spec.security.authentication.modes`. We recommend 
`SCRAM-SHA-256` (`SCRAM`) over `SCRAM-SHA-1`. If you specify 
`SCRAM-SHA-1`, you must also specify `MONGODB-CR`.

This setting is required if you specified more than one value for
`spec.security.authentication.modes`.

**`spec.security.authentication.agents.automationUserName`**

*Type*: string

Name of the user that the MongoDB Agents use to interact with your
MongoDB deployment. The username is mapped to an LDAP Distinguished
Name (DN) according to
`spec.security.authentication.ldap.userToDNMapping`. The
resulting DN must already exist in your LDAP deployment.

This setting is required if 
`spec.security.authentication.agents.mode` is `LDAP`.

**`spec.security.authentication.agents.automationPasswordSecretRef`**

*Type*: collection

Details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the
`spec.security.authentication.agents.automationUserName`
user.

This setting is required if 
`spec.security.authentication.agents.mode` is `LDAP`.

**`spec.security.authentication.agents.automationPasswordSecretRef.name`**

*Type*: string

Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the
`spec.security.authentication.agents.automationUserName`
user. You must create this secret in the same namespace to which you
deploy the Kubernetes Operator:

```sh
kubectl create secret generic ldap-agent-user \
--from-literal="password=<password>" -n <metadata.namespace>
```

This secret must contain one key, the value of which matches the
password of the
`spec.security.authentication.agents.automationUserName` user
in your LDAP deployment.

This setting is required if 
`spec.security.authentication.agents.mode` is `LDAP`.

**`spec.security.authentication.agents.automationPasswordSecretRef.key`**

*Type*: string

Key in the
`spec.security.authentication.agents.automationPasswordSecretRef.name`
[secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the user in
`spec.security.authentication.agents.automationUserName`.

This setting is required if 
`spec.security.authentication.agents.mode` is
`LDAP`.

**`spec.security.authentication.agents.clientCertificateSecretRef.name`**

*Type*: string

Specifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the MongoDB Agent\'s
TLS (Transport Layer Security) certificate. If omitted, defaults to `agent-certs`.

You must create this secret in the same namespace to which you
deploy the Kubernetes Operator and the secret must be
of type `kubernetes.io/tls`.

**`spec.security.roles`**

*Type*: array

Array that defines User-defined roles that give you
fine-grained access control over your MongoDB deployment.

To enable user-defined roles, the
`spec.security.authentication.enabled` must be `true`.

**Example:**

In this example, a user-defined role named `customRole` allows
users assigned this role to:

- Insert documents into the `cats` collection in the `pets`
  database, and
- Find and insert documents into the `dogs` collection in the
  `pets` database.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  type: ReplicaSet
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  persistent: true
  security:
    authentication:
      enabled: true
      modes:
        - "SCRAM"
    roles:
      - role: "customRole"
        db: admin    
        privileges:
        - actions:
          - insert
          resource:
            collection: cats
            db: pets
        - actions:
          - insert
          - find
          resource:
            collection: dogs
            db: pets
...
```

**`spec.security.roles.role`**

*Type*: string

Name of the user-defined role.

**`spec.security.roles.db`**

*Type*: string

The database in which you want to store the user-defined role.

**Example:**

`admin`

**`spec.security.roles.authenticationRestrictions`**

*Type*: array

Array that defines the IP address from which and to which users
assigned this `spec.security.roles.role` can
connect.

**`spec.security.roles.authenticationRestrictions.clientSource`**

*Type*: array

Array of IP addresses or CIDR blocks from which users assigned this
`spec.security.roles.role` can connect. 

MongoDB servers reject connection requests from users with this role
if the requests come from a client that is not present in this array.

**`spec.security.roles.authenticationRestrictions.serverAddress`**

*Type*: array

Array of IP addresses or CIDR blocks to which users assigned this
`spec.security.roles.role` can connect. 

MongoDB servers reject connection requests from users with this role
if the client requests to connect to a server that is not present in
this array.

**`spec.security.roles.privileges`**

*Type*: array

Array that describes the privileges that users granted this role
possess.

**`spec.security.roles.privileges.actions`**

*Type*: array

List of actions that users granted this role can perform. For a list
of accepted values, see Privilege Actions in the
MongoDB Manual for the MongoDB versions you deploy with the
Kubernetes Operator.

**`spec.security.roles.privileges.resource`**

*Type*: collection

Resources for which the privilege
`actions`
apply.

This collection must include either:

- The
  `spec.security.roles.privileges.resource.database`
  and
  `spec.security.roles.privileges.resource.collection`
  settings, or
- The
  `spec.security.roles.privileges.resource.cluster`
  setting with a value of `true`.

**`spec.security.roles.privileges.resource.database`**

*Type*: string

Database for which the privilege
`actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.security.roles.privileges.resource.collection`.

**`spec.security.roles.privileges.resource.collection`**

*Type*: string

Collection in the
`database`
for which the privilege
`actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.security.roles.privileges.resource.database`.

**`spec.security.roles.privileges.resource.cluster`**

*Type*: boolean

*Default*: False

Flag that indicates that the privilege
`actions`
apply to all databases and collections in the MongoDB deployment. If
omitted, defaults to `false`.

If set to true, do not provide values for
`spec.security.roles.privileges.resource.database`
and 
`spec.security.roles.privileges.resource.collection`.
