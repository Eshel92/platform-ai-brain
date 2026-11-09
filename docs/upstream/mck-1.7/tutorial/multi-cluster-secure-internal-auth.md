<!-- Converted from tutorial/multi-cluster-secure-internal-auth.txt (reStructuredText). Includes are inlined. -->

# Configure Multi-Cluster Internal Auth (X.509)

This guide instructs you on how to configure:

- X.509 internal authentication between MongoDB nodes in each cluster in
  your multi-Kubernetes cluster MongoDB deployments.
- X.509 authentication from clients to your MongoDB instances.

## Prerequisites

Before you secure your multi-Kubernetes cluster MongoDB deployment using TLS (Transport Layer Security)
encryption, complete the following tasks:

- Follow the steps in the Multi-Cluster Quick Start Prerequisites.
- Deploy a  TLS-encrypted multi-Kubernetes-cluster.
- Create credentials for the Kubernetes Operator.

Enabling X.509 authentication at the project level configures all
agents to use X.509 client authentication when communicating with
MongoDB deployments.

X.509 client authentication requires one of the following:

- Cloud Manager
- Ops Manager version compatible with
  your Kubernetes Operator version.

## Configure X.509 Internal Authentication for a MongoDBMultiCluster Resource

**Step 1: Create the secret for your agent's X.509 certificate of your `MongoDBMultiCluster` resource.**

Run the `kubectl` command to create a new secret that stores the agent's X.509 certificate:

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
  --namespace=<metadata.namespace> \
create secret tls <prefix>-<metadata.name>-agent-certs \
  --cert=<agent-tls-cert> \
  --key=<agent-tls-key>
```

**Step 2: Create the secret for the member cluster's internal X.509 certificate.**

Run the `kubectl` command to create a new secret that stores the internal
cluster member's X.509 certificate. The member clusters are defined in
your `MongoDBMultiCluster` resource.

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
  --namespace=<metadata.namespace> \
create secret tls <prefix>-<metadata.name>-clusterfile \
  --cert=<resource-clusterfile-tls-cert> \
  --key=<resource-clusterfile-tls-key>
```

**Step 3: Update your `MongoDBMultiCluster` resource to enable X509 authentication.**

Update your MongoDBMultiCluster custom resource
with security settings from the Kubernetes Operator
MongoDBMultiCluster resource specification.
Add the `internalCluster` setting, under `spec.authentication`, and set it
to `"X509"`. The resulting configuration may look similar to the following example:

```yaml
  apiVersion: mongodb.com/v1
  kind: MongoDBMultiCluster
  metadata:
   name: multi-replica-set
  spec:
   version: 8.0.0
   type: ReplicaSet
   persistent: false
   duplicateServiceObjects: true
   credentials: my-credentials
   opsManager:
     configMapRef:
       name: my-project
   security:
     tls:
        a: custom-ca
     certsSecretPrefix: <prefix>
   authentication:
     enabled: true
     modes: ["X509"]
     agents: 
       mode: "X509"
     internalCluster: "X509"
   clusterSpecList:
     - clusterName: ${MDB_CLUSTER_1_FULL_NAME}
       members: 3
     - clusterName: ${MDB_CLUSTER_2_FULL_NAME}
       members: 2
     - clusterName: ${MDB_CLUSTER_3_FULL_NAME}
       members: 3

The Kubernetes Operator copies the ConfigMap with the :abbr:`CA (Certificate Authority)` created in
the central cluster to each member cluster, generates a concatenated
:abbr:`PEM (Privacy-Enhanced Mail)` secret, and distributes it to the member clusters.
```

**Step 4: Verify that the `MongoDBMultiCluster` resources are running.**

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

## Renew Internal Authentication X.509 Certificates for a MongoDBMultiCluster Resource

If you have already created certificates, renew them periodically using
the following procedure.

**Step 1: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for a `MongoDBMultiCluster` resource.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores the certificates for the `MongoDBMultiCluster` resource:

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
--namespace=<metadata.namespace> \
create secret tls <prefix>-<metadata.name>-cert \
--cert=<resource-tls-cert> \
--key=<resource-tls-key> \
--dry-run=client \
-o yaml |
kubectl apply -f -
```

**Step 2: Renew the secret for your agent's X.509 certificates.**

Run the `kubectl` command to renew an existing secret that stores
the `MongoDBMultiCluster` resource agent certificates:

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
  --namespace=<metadata.namespace> \
create secret tls <prefix>-<metadata.name>-agent-certs \
  --cert=<agent-tls-cert> \
  --key=<agent-tls-key> \
  --dry-run=client \
  -o yaml | kubectl apply -f -
```

**Step 3: Renew the secret for internal members's X.509 certificates of the `MongoDBMultiCluster` resource.**

Run the `kubectl` command to renew an existing secret that stores
X.509 certificates for internal members of the `MongoDBMultiCluster` resource:

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
  --namespace=<metadata.namespace> \
create secret tls <prefix>-<metadata.name>-clusterfile \
  --cert=<resource-clusterfile-tls-cert> \
   --key=<resource-clusterfile-tls-key> \
   --dry-run=client \
   -o yaml | kubectl apply -f -
```
