<!-- Converted from tutorial/secure-ldap-auth.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure Single Cluster LDAP Authentication

[MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise)
supports:

- Proxying authentication requests to a Lightweight Directory Access
  Protocol (LDAP) service.
- Simple and SASL binding to LDAP servers. MongoDB Enterprise can bind
  to an LDAP server via `saslauthd` or through the operating system
  libraries.

To learn more, see the LDAP Proxy Authentication
and LDAP Authorization sections
in the MongoDB Server documentation.

You can use the Kubernetes Operator to configure LDAP to authenticate your
client applications that connect to your MongoDB deployments. This guide
describes how to configure LDAP authentication from client applications
to your MongoDB deployments.

**Note:** You can't secure a Standalone Instance of MongoDB in a Kubernetes cluster.

## Considerations

- To configure LDAP (Lightweight Directory Access Protocol) in [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/), use the parameters under the
  `spec.security.authentication.ldap` and other
  security LDAP settings specific to the
  MongoDB Agent, from the Kubernetes Operator MongoDB resource specification.
  The procedures in this section describe the required settings and
  provide examples of LDAP configuration.

- To improve security, consider deploying a
  TLS-encrypted replica set or a 
  TLS-encrypted sharded cluster.
  Encryption with TLS (Transport Layer Security) is optional. By default, LDAP (Lightweight Directory Access Protocol) traffic is sent
  as plain text. This means that username and password are exposed to
  network threats. Many modern directory services, such as Microsoft
  Active Directory, require encrypted connections. Consider using
  LDAP (Lightweight Directory Access Protocol) over TLS (Transport Layer Security)/SSL (Secure Sockets Layer) to encrypt authentication requests in your
  Kubernetes Operator MongoDB deployments.

## General Prerequisites

Before you configure LDAP authentication for your MongoDB deployments,
complete the following tasks:

- Ensure that you deploy the MongoDB Enterprise database resource.
  MongoDB Community databases don't support LDAP authentication.
- Deploy the replica set or
  deploy the sharded cluster
  whose client authentication you want to secure with LDAP (Lightweight Directory Access Protocol).

## Configure LDAP Client Authentication for a Replica Set

**Step 1: Copy the sample replica set resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired replica set configuration.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  opsManager:
    configMapRef:
            # Must match metadata.name in ConfigMap file
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  type: ReplicaSet
  persistent: true
```

```yaml
  security:
    tls:
      ca: <custom-ca>
    certsSecretPrefix: <prefix>
...
```

**Step 2: Paste the copied example section into your existing replica set resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
at the end of your resource file in the `spec` section.

**Step 3: Configure the LDAP settings for your replica set resource.**

To enable LDAP (Lightweight Directory Access Protocol) in your deployment, configure the following
settings in your Kubernetes object:

| Key | Type and necessity | Description | Example |
|---|---|---|---|
| \| `spec.security` \| `.authentication.enabled` | \| boolean, \| required | Set to `true` to enable LDAP authentication. | `true` |
| \| `spec.security` \| `.authentication.ldap.bindQueryUser` | \| string, \| required | Specify the LDAP Distinguished Name to which MongoDB binds when connecting to the LDAP server. | `cn=admin,dc=example,dc=org` |
| \| `spec.security` \| `.authentication.ldap.bindQueryPasswordSecretRef` | \| string, \| required | Specify the name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the LDAP Bind Distinguished Name's password with which MongoDB binds when connecting to an LDAP server. | `<secret-name>` |
| \| `spec.security` \| `.authentication.ldap.caConfigMapRef.name` | \| string, \| optional | Add the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)\'s name that stores the custom CA (Certificate Authority) that you used to sign your deployment's TLS (Transport Layer Security) certificates. | `<configmap-name>` |
| \| `spec.security` \| `.authentication.ldap.caConfigMapRef.key` | \| string, \| optional | Add the field name that stores the CA (Certificate Authority) which validates the LDAP server's TLS (Transport Layer Security) certificate. | `<configmap-key>` |
| \| `spec.security` \| `.authentication.ldap.servers` | \| array of strings, \| required | Specify the list of `hostname:port` combinations of one or more LDAP servers. For each server, use a separate line. | `<example.com:636>` |
| \| `spec.security` \| `.authentication.ldap.transportSecurity` | \| string, \| optional | Set to `tls` to use LDAPS (LDAP over TLS (Transport Layer Security)). Leave blank if your LDAP server doesn't accept TLS. You must enable TLS when you deploy the database resource to use this setting. | `tls` |
| \| `spec.security` \| `.authentication.ldap.userToDNMapping` | \| string, \| required | Specify the mapping that maps the username provided to `mongod` or `mongos` for authentication to an LDAP Distinguished Name (DN). To learn more, see security.ldap.userToDNMapping and LDAP Query Templates in the MongoDB Server documentation. | `<match: "(.+)",substitution: "uid={0},ou=groups,dc=example,dc=org">` |
| \| `spec.security` \| `.authentication.modes` | \| string, \| required | Set to `LDAP` to enable authentication through LDAP. | `LDAP` |

The resulting configuration may look similar to the following
example:

```yaml
security:
 authentication:
   enabled: true
   # Enabled LDAP Authentication Mode
   modes:
     - "LDAP"
     - "SCRAM"
     # LDAP related configuration
   ldap:
   # Specify the hostname:port combination of one or
   # more LDAP servers
     servers:
       - "ldap1.example.com:636"
       - "ldap2.example.com:636"

   # Set to "tls" to use LDAP over TLS. Leave blank if
   # the LDAP server doesn't accept TLS. You must enable TLS when you deploy the database resource to use this setting.
   transportSecurity: "tls"

   # If TLS is enabled, add a reference to a ConfigMap that
   # contains a CA certificate that validates the LDAP server's
   # TLS certificate.
   caConfigMapRef:
     name: "<configmap-name>"
     key: "<configmap-entry-key>"

   # Specify the LDAP Distinguished Name to which
   # MongoDB binds when connecting to the LDAP server
   bindQueryUser: "cn=admin,dc=example,dc=org"

   # Specify the password with which MongoDB binds
   # when connecting to an LDAP server. This is a
   # reference to a Secret Kubernetes Object containing
   # one "password" key.
   bindQueryPasswordSecretRef:
     name: "<secret-name>"
```

For a full list of LDAP settings, see security settings in the Kubernetes Operator MongoDB resource specification.
Also see the `spec.security.authentication.agents.automationUserName`
setting for the MongoDB Agent user in your LDAP-enabled Kubernetes Operator
deployment.

**Step 4: Configure the LDAP settings for the MongoDB Agent.**

Update your MongoDB resource
with security settings specific to the Agent,
from the Kubernetes Operator MongoDB resource specification. The resulting
configuration may look similar to the following example:

```yaml
security:
  authentication:
    agents:
      automationPasswordSecretRef:
        key: automationConfigPassword
        name: automation-config-password
      automationUserName: mms-automation-agent
      clientCertificateSecretRef:
        name: agent-client-cert
      mode: LDAP
    enabled: true
    ldap:
      bindQueryPasswordSecretRef:
        name: bind-query-password
      bindQueryUser: cn=admin,dc=example,dc=org
      servers:
        - openldap.namespace.svc.cluster.local:389
      userToDNMapping: '[{match: "(.+)",substitution: "uid={0},ou=groups,dc=example,dc=org"}]'
    modes:
      - LDAP
      - SCRAM
    requireClientTLSAuthentication: false
```

**Step 5: Save your replica set config file.**

**Step 6: Apply your changes to your replica set deployment.**

Invoke the following Kubernetes command to update your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 7: Track the status of your deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.

## Configure LDAP Client Authentication for a Sharded Cluster

**Step 1: Copy the sample sharded cluster resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired sharded cluster configuration.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-sharded-cluster>
spec:
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 3
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
            # Must match metadata.name in ConfigMap file
  credentials: <mycredentials>
  type: ShardedCluster
  persistent: true
```

```yaml
  security:
    tls:
      ca: <custom-ca>
    certsSecretPrefix: <prefix>
...
```

**Step 2: Paste the copied example section into your existing sharded cluster resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
at the end of your resource file in the `spec` section.

**Step 3: Configure the LDAP settings for your sharded cluster resource.**

To enable LDAP (Lightweight Directory Access Protocol) in your deployment, configure the following
settings in your Kubernetes object:

| Key | Type and necessity | Description | Example |
|---|---|---|---|
| \| `spec.security` \| `.authentication.enabled` | \| boolean, \| required | Set to `true` to enable LDAP authentication. | `true` |
| \| `spec.security` \| `.authentication.ldap.bindQueryUser` | \| string, \| required | Specify the LDAP Distinguished Name to which MongoDB binds when connecting to the LDAP server. | `cn=admin,dc=example,dc=org` |
| \| `spec.security` \| `.authentication.ldap.bindQueryPasswordSecretRef` | \| string, \| required | Specify the name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the LDAP Bind Distinguished Name's password with which MongoDB binds when connecting to an LDAP server. | `<secret-name>` |
| \| `spec.security` \| `.authentication.ldap.caConfigMapRef.name` | \| string, \| optional | Add the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)\'s name that stores the custom CA (Certificate Authority) that you used to sign your deployment's TLS (Transport Layer Security) certificates. | `<configmap-name>` |
| \| `spec.security` \| `.authentication.ldap.caConfigMapRef.key` | \| string, \| optional | Add the field name that stores the CA (Certificate Authority) which validates the LDAP server's TLS (Transport Layer Security) certificate. | `<configmap-key>` |
| \| `spec.security` \| `.authentication.ldap.servers` | \| array of strings, \| required | Specify the list of `hostname:port` combinations of one or more LDAP servers. For each server, use a separate line. | `<example.com:636>` |
| \| `spec.security` \| `.authentication.ldap.transportSecurity` | \| string, \| optional | Set to `tls` to use LDAPS (LDAP over TLS (Transport Layer Security)). Leave blank if your LDAP server doesn't accept TLS. You must enable TLS when you deploy the database resource to use this setting. | `tls` |
| \| `spec.security` \| `.authentication.ldap.userToDNMapping` | \| string, \| required | Specify the mapping that maps the username provided to `mongod` or `mongos` for authentication to an LDAP Distinguished Name (DN). To learn more, see security.ldap.userToDNMapping and LDAP Query Templates in the MongoDB Server documentation. | `<match: "(.+)",substitution: "uid={0},ou=groups,dc=example,dc=org">` |
| \| `spec.security` \| `.authentication.modes` | \| string, \| required | Set to `LDAP` to enable authentication through LDAP. | `LDAP` |

The resulting configuration may look similar to the following
example:

```yaml
security:
 authentication:
   enabled: true
   # Enabled LDAP Authentication Mode
   modes:
     - "LDAP"
     - "SCRAM"
     # LDAP related configuration
   ldap:
   # Specify the hostname:port combination of one or
   # more LDAP servers
     servers:
       - "ldap1.example.com:636"
       - "ldap2.example.com:636"

   # Set to "tls" to use LDAP over TLS. Leave blank if
   # the LDAP server doesn't accept TLS. You must enable TLS when you deploy the database resource to use this setting.
   transportSecurity: "tls"

   # If TLS is enabled, add a reference to a ConfigMap that
   # contains a CA certificate that validates the LDAP server's
   # TLS certificate.
   caConfigMapRef:
     name: "<configmap-name>"
     key: "<configmap-entry-key>"

   # Specify the LDAP Distinguished Name to which
   # MongoDB binds when connecting to the LDAP server
   bindQueryUser: "cn=admin,dc=example,dc=org"

   # Specify the password with which MongoDB binds
   # when connecting to an LDAP server. This is a
   # reference to a Secret Kubernetes Object containing
   # one "password" key.
   bindQueryPasswordSecretRef:
     name: "<secret-name>"
```

For a full list of LDAP settings, see security settings in the Kubernetes Operator MongoDB resource specification.
Also see the `spec.security.authentication.agents.automationUserName`
setting for the MongoDB Agent user in your LDAP-enabled Kubernetes Operator
deployment.

**Step 4: Configure the LDAP settings for the MongoDB Agent.**

Update your MongoDB resource
with security settings specific to the Agent,
from the Kubernetes Operator MongoDB resource specification. The resulting
configuration may look similar to the following example:

```yaml
security:
  authentication:
    agents:
      automationPasswordSecretRef:
        key: automationConfigPassword
        name: automation-config-password
      automationUserName: mms-automation-agent
      clientCertificateSecretRef:
        name: agent-client-cert
      mode: LDAP
    enabled: true
    ldap:
      bindQueryPasswordSecretRef:
        name: bind-query-password
      bindQueryUser: cn=admin,dc=example,dc=org
      servers:
        - openldap.namespace.svc.cluster.local:389
      userToDNMapping: '[{match: "(.+)",substitution: "uid={0},ou=groups,dc=example,dc=org"}]'
    modes:
      - LDAP
      - SCRAM
    requireClientTLSAuthentication: false
```

**Step 5: Save your sharded cluster config file.**

**Step 6: Apply your changes to your sharded cluster deployment.**

Invoke the following Kubernetes command to update your
sharded cluster:

```sh
kubectl apply -f <sharded-cluster-conf>.yaml
```

**Step 7: Track the status of your deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.
