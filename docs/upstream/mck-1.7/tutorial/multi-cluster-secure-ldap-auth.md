<!-- Converted from tutorial/multi-cluster-secure-ldap-auth.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure Multi-Cluster LDAP Authentication

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

You can use the Kubernetes Operator to configure LDAP (Lightweight Directory Access Protocol) to authenticate your
client applications that connect to your multi-Kubernetes cluster MongoDB deployments. This guide
describes how to configure LDAP (Lightweight Directory Access Protocol) authentication from client applications
to your multi-Kubernetes cluster MongoDB deployments.

## Considerations

- To configure LDAP (Lightweight Directory Access Protocol) in [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/), use the parameters under the
  `spec.security.authentication.ldap` and other
  security LDAP settings specific to the
  MongoDB Agent, from the Kubernetes Operator MongoDB resource specification.
  The procedures in this section describe the required settings and
  provide examples of LDAP (Lightweight Directory Access Protocol) configuration.

- To improve security, consider deploying a
  TLS-encrypted multi-cluster.
  Encryption with TLS (Transport Layer Security) is optional. By default, LDAP (Lightweight Directory Access Protocol) traffic is sent
  as plain text. This means that username and password are exposed to
  network threats. Many modern directory services, such as Microsoft
  Active Directory, require encrypted connections. Consider using
  LDAP (Lightweight Directory Access Protocol) over TLS (Transport Layer Security)/SSL (Secure Sockets Layer) to encrypt authentication requests in your
  Kubernetes Operator MongoDB deployments.

## Prerequisites

Before you secure your multi-Kubernetes cluster MongoDB deployment using TLS (Transport Layer Security)
encryption, complete the following tasks:

- Follow the steps in the Quick Start Prerequisites.
- Deploy a multi-cluster using a multi-cluster-quick-start-ref.

## Configure LDAP Client Authentication for a Multi-Kubernetes-Cluster Replica Set

**Step 1: Update your `MongoDBMultiCluster` resource to enable LDAP (Lightweight Directory Access Protocol) authentication.**

Update your MongoDBMultiCluster custom resource
with security settings from the Kubernetes Operator
MongoDBMultiCluster resource specification.

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
   # the LDAP server doesn't accept TLS. You must enable TLS when
   # you deploy the multi-cluster resource to use this setting.
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

For a full list of LDAP settings, see security settings in the Kubernetes Operator
MongoDBMultiCluster resource specification.
Also see the `spec.security.authentication.agents.automationUserName`
setting for the MongoDB Agent user in your LDAP-enabled Kubernetes Operator
deployment.

**Step 2: Verify that the `MongoDBMultiCluster` resources are running.**

a. For member clusters, run the following commands to verify that
   the MongoDB Pods are in the running state:

   ```sh
   kubectl get pods \
    --context=$MDB_CLUSTER_1_FULL_NAME \
    --namespace mongodb
   ```

   ```sh
   kubectl get pods \
    --context=$MDB_CLUSTER_2_FULL_NAME \
    --namespace mongodb
   ```

   ```sh
   kubectl get pods \
    --context=$MDB_CLUSTER_3_FULL_NAME \
    --namespace mongodb
   ```

#.  In the central cluster, run the following command to verify that
    the `MongoDBMultiCluster` resource is in the running state:

    ```sh
    kubectl --context=$MDB_CENTRAL_CLUSTER_FULL_NAME \
      --namespace mongodb \
      get mdbmc multi-replica-set -o yaml -w
    ```
