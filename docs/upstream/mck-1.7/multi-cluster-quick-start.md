<!-- Converted from multi-cluster-quick-start.txt (reStructuredText). Includes are inlined. -->

# Multi-Kubernetes-Cluster Quick Start

Use the quick start to deploy a MongoDB replica set across three Kubernetes
member clusters, using [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine)
and [Istio](https://istio.io/) service mesh.

Before you begin:

- Learn about multi-Kubernetes-cluster deployments
- Review the list of multi-Kubernetes-cluster services and tools
- Complete the prerequisites

**Note:**

The following procedures scope your multi-Kubernetes cluster MongoDB deployment to a single
[namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) named `mongodb`. You can configure your multi-Kubernetes cluster MongoDB deployment to
watch resources in multiple namespaces
or all namespaces.

## Prefer to Learn by Watching?

Follow along with this video tutorial walk-through that demonstrates how to
create a multi-Kubernetes cluster MongoDB deployment.

*Duration: 12 Minutes*

[Deploying a MongoDB Replica Set across Multiple Kubernetes Clusters](https://www.youtube.com/watch?v=iPvoqxbFJd8)

## Prerequisites

Before you create a multi-Kubernetes cluster MongoDB deployment using the quick start, 
complete the following tasks:

### Review the General Prerequisites

Ensure you meet the general prerequisite before you proceed. To learn 
more, see General Prerequisites.

### Set Environment Variables and GKE Zones

Set the environment variables with cluster names and the
[available GKE zones](https://cloud.google.com/compute/docs/regions-zones#available)
where you deploy the clusters, as in this example:

```sh
export MDB_GKE_PROJECT={GKE project name}

export MDB_CENTRAL_CLUSTER_ZONE="us-west1-a"

export MDB_CLUSTER_1_ZONE="us-west1-b"

export MDB_CLUSTER_2_ZONE="us-east1-b"

export MDB_CLUSTER_3_ZONE="us-central1-a"

export MDB_CENTRAL_CLUSTER_FULL_NAME="gke_${MDB_GKE_PROJECT}_${MDB_CENTRAL_CLUSTER_ZONE}_${MDB_CENTRAL_CLUSTER}"

export MDB_CLUSTER_1_FULL_NAME="gke_${MDB_GKE_PROJECT}_${MDB_CLUSTER_1_ZONE}_${MDB_CLUSTER_1}"
export MDB_CLUSTER_2_FULL_NAME="gke_${MDB_GKE_PROJECT}_${MDB_CLUSTER_2_ZONE}_${MDB_CLUSTER_2}"
export MDB_CLUSTER_3_FULL_NAME="gke_${MDB_GKE_PROJECT}_${MDB_CLUSTER_3_ZONE}_${MDB_CLUSTER_3}"
```

### Set up GKE Clusters

Set up [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters:

**Step 1: Set up your Google Cloud account.**

If you have not done so already, create a Google Cloud project, enable billing on the project, enable the Artifact Registry and GKE APIs, and launch Cloud Shell by following the relevant procedures in the [Google Kubernetes Engine Quickstart](https://cloud.google.com/kubernetes-engine/docs/quickstart) in the Google Cloud documentation.

**Step 2: Create a central cluster and member clusters.**

Create one central cluster and one or more member clusters, specifying the GKE zones, the number of nodes, 
and the instance types, as in these examples:

```sh
gcloud container clusters create $MDB_CENTRAL_CLUSTER \
  --zone=$MDB_CENTRAL_CLUSTER_ZONE \
  --num-nodes=5 \
  --machine-type "e2-standard-2"
```

```sh
gcloud container clusters create $MDB_CLUSTER_1 \
  --zone=$MDB_CLUSTER_1_ZONE \
  --num-nodes=5 \
  --machine-type "e2-standard-2"
```

```sh
gcloud container clusters create $MDB_CLUSTER_2 \
  --zone=$MDB_CLUSTER_2_ZONE \
  --num-nodes=5 \
  --machine-type "e2-standard-2"
```

```sh
gcloud container clusters create $MDB_CLUSTER_3 \
  --zone=$MDB_CLUSTER_3_ZONE \
  --num-nodes=5 \
  --machine-type "e2-standard-2"
```

### Obtain User Authentication Credentials for Central and Member Clusters

Obtain user authentication credentials for the central and member Kubernetes
clusters and save the credentials. You will later use these credentials
for running `kubectl` commands on these clusters.

Run the following commands:

```sh
gcloud container clusters get-credentials $MDB_CENTRAL_CLUSTER \
  --zone=$MDB_CENTRAL_CLUSTER_ZONE

gcloud container clusters get-credentials $MDB_CLUSTER_1 \
  --zone=$MDB_CLUSTER_1_ZONE

gcloud container clusters get-credentials $MDB_CLUSTER_2 \
  --zone=$MDB_CLUSTER_2_ZONE

gcloud container clusters get-credentials $MDB_CLUSTER_3 \
  --zone=$MDB_CLUSTER_3_ZONE
```

## Deploy a MongoDBMultiCluster Resource

Select the appropriate tab based on whether you want to encrypt replica
set connections in your multi-Kubernetes cluster MongoDB deployments using TLS (Transport Layer Security) certificates.

**encrypted:**

You can use the following procedures in this
TLS-Encrypted Connections tab:

- Deploy a `MongoDBMultiCluster` resource
- Renew TLS Certificates for a `MongoDBMultiCluster` resource

These procedures establish TLS (Transport Layer Security)-encrypted connections between
MongoDB hosts in a replica set, and between client applications and
MongoDB deployments.

Before you begin, you must have valid certificates for TLS (Transport Layer Security) encryption.

**Step 1: Create the secret for the TLS certificate of your `MongoDBMultiCluster` resource.**

Run the `kubectl` command to create a new secret that stores the
`MongoDBMultiCluster` resource certificate:

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
  --namespace=<metadata.namespace> \
  create secret tls <prefix>-<metadata.name>-cert \
  --cert=<resource-tls-cert> \
  --key=<resource-tls-key>
```

**Note:**

You must prefix your secrets with `<prefix>-<metadata.name>`.

For example, if you call your deployment `my-deployment` and you set
the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the
client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, 
you must name the TLS (Transport Layer Security) secret for internal cluster authentication 
(if enabled) `mdb-my-deployment-clusterfile`.

**Step 2: Create the ConfigMap to link your CA with your `MongoDBMultiCluster` resource.**

Run the `kubectl` command to link your CA (Certificate Authority) to your `MongoDBMultiCluster` resource.
Specify the CA (Certificate Authority) certificate file that you must always name
`ca-pem` for the `MongoDBMultiCluster` resource:

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
  --namespace=<metadata.namespace> \
  create configmap custom-ca -from-file=ca-pem=<your-custom-ca-file>
```

**Step 3: Run the `kubectl mongodb` plugin.**

By default, the Kubernetes Operator is scoped to the `mongodb` namespace. When you run the following command, the `kubectl mongodb` plugin:

- Creates one central cluster, three member clusters, and a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) labeled `mongodb` in each of the clusters.

- Creates a default ConfigMap with the hard-coded name `mongodb-kubernetes-operator-member-list` that contains all the member clusters. You can't change the ConfigMap's name.

- Creates the [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and `Roles` required for running database workloads in the member clusters.

Run the `kubectl mongodb` plugin:

```sh
kubectl mongodb multicluster setup \
  --central-cluster="${MDB_CENTRAL_CLUSTER_FULL_NAME}" \
  --member-clusters="${MDB_CLUSTER_1_FULL_NAME},${MDB_CLUSTER_2_FULL_NAME},${MDB_CLUSTER_3_FULL_NAME}" \
  --member-cluster-namespace="mongodb" \
  --central-cluster-namespace="mongodb" \
  --create-service-account-secrets \
  --install-database-roles=true
```

**Step 4: Set the Istio injection webhook in each member cluster.**

If you're using Istio, run the following command on the central cluster,
specifying the context for each of the member clusters in the deployment.
To enable [sidecar injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#automatic-sidecar-injection) in Istio, the following commands add
the `istio-injection=enabled` labels to the `mongodb` namespaces
on each member cluster. If you use another service mesh, configure
it to handle network traffic in the created namespaces.

```sh
kubectl label \
  --context=$MDB_CLUSTER_1_FULL_NAME \
  namespace mongodb \
  istio-injection=enabled
```

```sh
kubectl label \
  --context=$MDB_CLUSTER_2_FULL_NAME \
  namespace mongodb \
  istio-injection=enabled
```

```sh
kubectl label \
  --context=$MDB_CLUSTER_3_FULL_NAME \
  namespace mongodb \
  istio-injection=enabled
```

**Step 5: Configure `kubectl` to use the central cluster's namespace.**

If you have not done so already, run the following commands to run
all `kubectl` commands on the central cluster in the default
namespace.

```sh
kubectl config use-context $MDB_CENTRAL_CLUSTER_FULL_NAME
kubectl config set-context $(kubectl config current-context) \
  --namespace=mongodb
```

**Step 6: Deploy the MongoDB Controllers for Kubernetes Operator in the central cluster.**

Deploy the MongoDB Controllers for Kubernetes Operator in the central cluster in the `mongodb` namespace with Helm or `kubectl`.

**deploy-mc-helm:**

a. Add the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) repository to Helm.

   ```sh
   helm repo add mongodb https://mongodb.github.io/helm-charts
   ```

#. Use the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) to deploy the Kubernetes Operator.

   ```sh
   helm upgrade \
     --install \
       mongodb-kubernetes-operator-multi-cluster \
       mongodb/mongodb-kubernetes \
         --namespace mongodb \
         --set namespace=mongodb \
         --version <mongodb-kubernetes-operator-version> \
         --set operator.name=mongodb-kubernetes-operator-multi-cluster \
         --set operator.createOperatorServiceAccount=false \
         --set operator.createResourcesServiceAccountsAndRoles=false \
         --set "multiCluster.clusters={$MDB_CLUSTER_1_FULL_NAME,$MDB_CLUSTER_2_FULL_NAME,$MDB_CLUSTER_3_FULL_NAME}" \
         --set multiCluster.performFailover=false
   ```

**deploy-mc-kubectl:**

a. Apply the Kubernetes Operator custom resources.

   ```sh
   kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
   ```

#. Download the Kubernetes Operator YAML template.

   ```sh
   curl https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes-multi-cluster.yaml -o operator.yaml
   ```

#. Optional: Customize the Kubernetes Operator YAML template.

   To learn about optional Kubernetes Operator installation settings, see meko-op-install-settings-kubectl-oc.

#. Apply the Kubernetes Operator YAML file.

   ```sh
   kubectl apply -f operator.yaml
   ```

#. Verify that the Kubernetes Operator is deployed.

   To verify that the Kubernetes Operator installed correctly,
   run the following command and verify the output:

   ```sh
   kubectl describe deployments mongodb-kubernetes-operator -n <metadata.namespace>
   ```

   By default, deployments exist in the `mongodb`
   namespace. If the following error message appears, ensure
   you use the correct namespace:

   ```sh
   Error from server (NotFound): deployments.apps "mongodb-kubernetes-operator" not found
   ```

   To troubleshoot your Kubernetes Operator, see review-k8s-op-logs
   and other troubleshooting topics.

   **Important:**

   If you need to remove the Kubernetes Operator or the
   namespace, you first must
   remove MongoDB resources.

**Step 7: Create a secret to use with Ops Manager and create a ConfigMap.**

a. Create a secret so that the Kubernetes Operator
   can create and update objects in your `Ops Manager` project.
   To learn more, see create-k8s-credentials.

#. Create a ConfigMap to link the Kubernetes Operator
   to your `Ops Manager` project. To learn more, see create-k8s-project.

**Step 8: Deploy Ops Manager on the central cluster and connect to Ops Manager.**

**Step 9: Deploy the `MongoDBMultiCluster` resource.**

Set `spec.credentials`, 
`spec.opsManager.configMapRef.name`, and 
security settings 
and deploy the `MongoDBMultiCluster` resource.
In the following code sample, `duplicateServiceObjects`
is set to `true` to enable
[DNS proxying](https://istio.io/latest/docs/ops/configuration/traffic-management/dns-proxy/)
in Istio.

**Note:**

To enable the cross-cluster DNS resolution by the Istio
service mesh, this tutorial creates service objects with a
single ClusterIP address per each Kubernetes Pod.

```yaml
kubectl apply -f - <<EOF
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
   certsSecretPrefix: <prefix>
   tls:
     ca: custom-ca
 clusterSpecList:
   - clusterName: ${MDB_CLUSTER_1_FULL_NAME}
     members: 3
   - clusterName: ${MDB_CLUSTER_2_FULL_NAME}
     members: 2
   - clusterName: ${MDB_CLUSTER_3_FULL_NAME}
     members: 3
EOF
```

The Kubernetes Operator copies the ConfigMap with the CA (Certificate Authority) that you
created in previous steps to each member cluster, generates a
concatenated PEM (Privacy-Enhanced Mail) secret, and distributes it to the member clusters.

**Step 10: Verify that the `MongoDBMultiCluster` resources are running.**

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

### Renew TLS Certificates for a MongoDBMultiCluster Resource

Renew your TLS (Transport Layer Security) certificates periodically using the following procedure.

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

**non-encrypted:**

This procedure doesn't encrypt connections between MongoDB hosts in
a replica set, and between client applications and MongoDB deployments.

**Step 1: Run the `kubectl mongodb` plugin.**

By default, the Kubernetes Operator is scoped to the `mongodb` namespace. When you run the following command, the `kubectl mongodb` plugin:

- Creates one central cluster, three member clusters, and a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) labeled `mongodb` in each of the clusters.

- Creates a default ConfigMap with the hard-coded name `mongodb-kubernetes-operator-member-list` that contains all the member clusters. You can't change the ConfigMap's name.

- Creates the [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and `Roles` required for running database workloads in the member clusters.

Run the `kubectl mongodb` plugin:

```sh
kubectl mongodb multicluster setup \
  --central-cluster="${MDB_CENTRAL_CLUSTER_FULL_NAME}" \
  --member-clusters="${MDB_CLUSTER_1_FULL_NAME},${MDB_CLUSTER_2_FULL_NAME},${MDB_CLUSTER_3_FULL_NAME}" \
  --member-cluster-namespace="mongodb" \
  --central-cluster-namespace="mongodb" \
  --create-service-account-secrets \
  --install-database-roles=true
```

**Step 2: Set the Istio injection webhook in each member cluster.**

If you're using Istio, run the following command on the central cluster,
specifying the context for each of the member clusters in the deployment.
To enable [sidecar injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#automatic-sidecar-injection) in Istio, the following commands add
the `istio-injection=enabled` labels to the `mongodb` namespaces
on each member cluster. If you use another service mesh, configure
it to handle network traffic in the created namespaces.

```sh
kubectl label \
  --context=$MDB_CLUSTER_1_FULL_NAME \
  namespace mongodb \
  istio-injection=enabled
```

```sh
kubectl label \
  --context=$MDB_CLUSTER_2_FULL_NAME \
  namespace mongodb \
  istio-injection=enabled
```

```sh
kubectl label \
  --context=$MDB_CLUSTER_3_FULL_NAME \
  namespace mongodb \
  istio-injection=enabled
```

**Step 3: Configure `kubectl` to use the central cluster's namespace.**

If you have not done so already, run the following commands to run
all `kubectl` commands on the central cluster in the default
namespace.

```sh
kubectl config use-context $MDB_CENTRAL_CLUSTER_FULL_NAME
kubectl config set-context $(kubectl config current-context) \
  --namespace=mongodb
```

**Step 4: Deploy the MongoDB Controllers for Kubernetes Operator in the central cluster.**

Deploy the MongoDB Controllers for Kubernetes Operator in the central cluster in the `mongodb` namespace with Helm or `kubectl`.

**deploy-mc-helm:**

a. Add the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) repository to Helm.

   ```sh
   helm repo add mongodb https://mongodb.github.io/helm-charts
   ```

#. Use the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) to deploy the Kubernetes Operator.

   ```sh
   helm upgrade \
     --install \
       mongodb-kubernetes-operator-multi-cluster \
       mongodb/mongodb-kubernetes \
         --namespace mongodb \
         --set namespace=mongodb \
         --version <mongodb-kubernetes-operator-version> \
         --set operator.name=mongodb-kubernetes-operator-multi-cluster \
         --set operator.createOperatorServiceAccount=false \
         --set operator.createResourcesServiceAccountsAndRoles=false \
         --set "multiCluster.clusters={$MDB_CLUSTER_1_FULL_NAME,$MDB_CLUSTER_2_FULL_NAME,$MDB_CLUSTER_3_FULL_NAME}" \
         --set multiCluster.performFailover=false
   ```

**deploy-mc-kubectl:**

a. Apply the Kubernetes Operator custom resources.

   ```sh
   kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
   ```

#. Download the Kubernetes Operator YAML template.

   ```sh
   curl https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes-multi-cluster.yaml -o operator.yaml
   ```

#. Optional: Customize the Kubernetes Operator YAML template.

   To learn about optional Kubernetes Operator installation settings, see meko-op-install-settings-kubectl-oc.

#. Apply the Kubernetes Operator YAML file.

   ```sh
   kubectl apply -f operator.yaml
   ```

#. Verify that the Kubernetes Operator is deployed.

   To verify that the Kubernetes Operator installed correctly,
   run the following command and verify the output:

   ```sh
   kubectl describe deployments mongodb-kubernetes-operator -n <metadata.namespace>
   ```

   By default, deployments exist in the `mongodb`
   namespace. If the following error message appears, ensure
   you use the correct namespace:

   ```sh
   Error from server (NotFound): deployments.apps "mongodb-kubernetes-operator" not found
   ```

   To troubleshoot your Kubernetes Operator, see review-k8s-op-logs
   and other troubleshooting topics.

   **Important:**

   If you need to remove the Kubernetes Operator or the
   namespace, you first must
   remove MongoDB resources.

**Step 5: Create a secret to use with Ops Manager and create a ConfigMap.**

a. Create a secret so that the Kubernetes Operator
   can create and update objects in your `Ops Manager` project.
   To learn more, see create-k8s-credentials.

#. Create a ConfigMap to link the Kubernetes Operator
   to your `Ops Manager` project. To learn more, see create-k8s-project.

**Step 6: Deploy Ops Manager on the central cluster and connect to Ops Manager.**

**Step 7: Deploy the `MongoDBMultiCluster` resource.**

Set `spec.credentials`, 
`spec.opsManager.configMapRef.name`, and 
security settings 
and deploy the `MongoDBMultiCluster` resource.
In the following code sample, `duplicateServiceObjects`
is set to `true` to enable
[DNS proxying](https://istio.io/latest/docs/ops/configuration/traffic-management/dns-proxy/)
in Istio.

**Note:**

To enable the cross-cluster DNS resolution by the Istio
service mesh, this tutorial creates service objects with a
single ClusterIP address per each Kubernetes Pod.

```yaml
kubectl apply -f - <<EOF
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
   certsSecretPrefix: <prefix>
   tls:
     ca: custom-ca
 clusterSpecList:
   - clusterName: ${MDB_CLUSTER_1_FULL_NAME}
     members: 3
   - clusterName: ${MDB_CLUSTER_2_FULL_NAME}
     members: 2
   - clusterName: ${MDB_CLUSTER_3_FULL_NAME}
     members: 3
EOF
```

The Kubernetes Operator copies the ConfigMap with the CA (Certificate Authority) that you
created in previous steps to each member cluster, generates a
concatenated PEM (Privacy-Enhanced Mail) secret, and distributes it to the member clusters.

**Step 8: Verify that the `MongoDBMultiCluster` resources are running.**

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

## Next Steps

After deploying your MongoDB replica set across three Kubernetes
member clusters, you can add a database user so you can connect to your MongoDB database. 
See k8s-manage-db-users.
