<!-- Converted from tutorial/secure-x509-auth.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Secure Client Authentication with X.509

The MongoDB Controllers for Kubernetes Operator can use X.509 certificates to authenticate your
client applications to your MongoDB deployments.

This guide instructs you on how to configure X.509 authentication from
clients to your MongoDB instances.

**Note:** You can't secure a Standalone Instance of MongoDB in a Kubernetes cluster.

## General Prerequisites

Before you secure your MongoDB deployment using TLS (Transport Layer Security) encryption,
complete the following:

- Install the Kubernetes Operator
- Create Credentials for the Kubernetes Operator

Enabling X.509 authentication at the project level configures all
agents to use X.509 client authentication when communicating with
MongoDB deployments.

## Configure X.509 Client Authentication for a Replica Set

### Prerequisites

Before you secure your replica set using X.509, 
deploy a TLS-encrypted replica set.

### Enable X.509 Client Authentication

**Step 5: Copy the sample replica set resource.**

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
    authentication:
      enabled: true
      modes: ["X509"]
...
```

**Step 6: Paste the copied example section into your existing replica set resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
at the end of your resource file in the `spec` section.

**Step 7: Configure the general X.509 settings for your replica set resource.**

To enable TLS (Transport Layer Security) and X.509 in your deployment, configure the following
settings in your Kubernetes object:

| Key | Type | Necessity | Description | Example |
|---|---|---|---|---|
| \| `spec.security` \| `.authentication` \| `.enabled` | boolean | Required | Set this value to `true` to enable authentication on the MongoDB deployment. | `true` |
| \| `spec.security` \| `.authentication` \| `.modes` | array | Conditional | Set this value to `["X509"]`. | `["X509"]` |

**Step 8: Save your replica set config file.**

**Step 9: Apply your changes to your replica set deployment.**

Invoke the following Kubernetes command to update your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 10: Track the status of your deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.

### Renew X.509 Certificates for a Replica Set

If you have already created certificates, we recommend that you renew
them periodically using the following procedure.

**Note:**

To automate certificate renewal for Ops Manager deployments, consider setting up the cert-manager integration.

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the replica set's certificates:

```sh
kubectl create secret tls <prefix>-<metadata.name>-cert \
  --cert=<replica-set-tls-cert> \
  --key=<replica-set-tls-key> \
  --dry-run=client \
   -o yaml |
kubectl apply -f -
```

**Step 3: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your agents' X.509 certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the agents' X.509 certificates:

```sh
kubectl create secret tls <prefix>-<metadata.name>-agent-certs \
  --cert=<agent-tls-cert> \
  --key=<agent-tls-key> \
  --dry-run=client \
   -o yaml |
kubectl apply -f -
```

## Configure X.509 Client Authentication for a Sharded Cluster

### Prerequisites

Before you secure your sharded cluster using X.509, 
deploy a TLS-encrypted sharded cluster.

### Enable X.509 Client Authentication

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
    authentication:
      enabled: true
      modes: ["X509"]
...
```

**Step 2: Paste the copied example section into your existing sharded cluster resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
at the end of your resource file in the `spec` section.

**Step 3: Configure the general X.509 settings for your sharded cluster resource.**

To enable TLS (Transport Layer Security) and X.509 in your deployment, configure the following
settings in your Kubernetes object:

| Key | Type | Necessity | Description | Example |
|---|---|---|---|---|
| \| `spec.security` \| `.authentication` \| `.enabled` | boolean | Required | Set this value to `true` to enable authentication on the MongoDB deployment. | `true` |
| \| `spec.security` \| `.authentication` \| `.modes` | array | Conditional | Set this value to `["X509"]`. | `["X509"]` |

**Step 4: Save your sharded cluster config file.**

**Step 5: Update and restart your sharded cluster deployment.**

In any directory, invoke the following Kubernetes command to update and 
restart your sharded cluster:

```sh
kubectl apply -f <sharded-cluster-conf>.yaml
```

**Step 6: Track the status of your deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.

### Renew X.509 Certificates for a Sharded Cluster

If you have already created certificates, we recommend that you renew
them periodically using the following procedure.

**Note:**

To automate certificate renewal for Ops Manager deployments, consider setting up the cert-manager integration.

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your Shards' TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the sharded cluster shards' certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-0-cert \
  --cert=<shard-0-tls-cert> \
  --key=<shard-0-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -

kubectl -n mongodb create secret tls <prefix>-<metadata.name>-1-cert \
  --cert=<shard-1-tls-cert> \
  --key=<shard-1-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -
```

**Step 3: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your config server's TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the sharded cluster config server's certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-config-cert \
  --cert=<config-tls-cert> \
  --key=<config-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -
```

**Step 4: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your mongos server's TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the sharded cluster `mongos` certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-mongos-cert \
  --cert=<mongos-tls-cert> \
  --key=<mongos-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -
```

**Step 5: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your agents' X.509 certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the agents' X.509 certificates:

```sh
kubectl create secret tls <prefix>-<metadata.name>-agent-certs \
  --cert=<agent-tls-cert> \
  --key=<agent-tls-key> \
  --dry-run=client \
   -o yaml |
kubectl apply -f -
```
