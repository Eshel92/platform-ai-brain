<!-- Converted from multi-cluster-deploy-replica-set.txt (reStructuredText). Includes are inlined. -->

# Deploy Replica Sets in a Multi-Kubernetes Cluster

Use this procedure to create a new replica set in a member Kubernetes cluster in a
multi-Kubernetes cluster MongoDB deployment.

This procedure allows you to set different settings for the replica set
resource, such as overrides for statefulSet configuration. As an
alternative to using this procedure, you can use the
multi-cluster-quick-start-ref, which creates a
multi-Kubernetes cluster MongoDB deployment with default settings.

Before you begin:

- Learn about multi-Kubernetes-cluster deployments.
- Review the list of multi-Kubernetes-cluster services and tools.
- Install the Kubernetes Operator in a multi-Kubernetes cluster MongoDB deployment. See multi-cluster-quick-start-ref.
- Complete the prerequisites.

## Deploy a `MongoDBMultiCluster` Resource

**encrypted-rs:**

You can use the following procedures in this
TLS-Encrypted Connections tab:

- Deploy a `MongoDBMultiCluster` resource
- Renew TLS Certificates for a `MongoDBMultiCluster` resource

These procedures establish TLS (Transport Layer Security)-encrypted connections between
MongoDB hosts in a replica set, and between client applications and
MongoDB deployments.

Before you begin, you must have valid certificates for TLS (Transport Layer Security) encryption.

### Deploy a `MongoDBMultiCluster` Resource

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

**Step 3: Configure `kubectl` to use the central cluster's namespace.**

If you have not done so already, run the following commands to run
all `kubectl` commands on the central cluster in the default
namespace.

```sh
kubectl config use-context $MDB_CENTRAL_CLUSTER_FULL_NAME
kubectl config set-context $(kubectl config current-context) \
  --namespace=mongodb
```

**Step 4: Copy and paste the sample  resource.**

a. Copy the sample replica set YAML (Yet Another Markup Language) file and paste it into a new
   text file.

b. Change the file's settings to match your desired replica set configuration.

```yaml
# This example provides statefulSet overrides per cluster.

apiVersion: mongodb.com/v1
kind: MongoDBMultiCluster
metadata:
  name: multi-replica-set
spec:
  version: 8.0.0
  type: ReplicaSet
  duplicateServiceObjects: false
  credentials: my-credentials
  opsManager:
    configMapRef:
      name: my-project
  clusterSpecList:
    - clusterName: cluster1.example.com
      members: 2
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar1
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          # Use the following settings to override the default storage size of the "data" Persistent Volume.
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi
    - clusterName: cluster2.example.com
      members: 1
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar2
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi
    - clusterName: cluster3.example.com
      members: 1
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar3
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi

...
```

**Step 5: Change the settings to your preferred values.**

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Label for the `MongoDBMultiCluster` resource. Resource names must be 44 characters or less. See also `metadata.name` and `names` in the Kubernetes documentation. | `multi-replica-set` |
| `spec.version` | string | Version of MongoDB that this `MongoDBMultiCluster` resource should run. The format should be `X.Y.Z` for the Community edition and `X.Y.Z-ent` for the Enterprise edition. IMPORTANT: Ensure that you choose a compatible MongoDB Server version. Compatible versions differ depending on the base image that the MongoDB database resource uses. To learn more about MongoDB versioning, see release-version-numbers in the MongoDB Manual. | `8.0.0` |
| \| `spec` \| `.opsManager` \| `.configMapRef` \| `.name` | string | Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection configuration. The `spec.cloudManager.configMapRef.name` setting is an alias for this setting and can be used in its place. This value must exist on the *same* namespace as the resource you want to create. IMPORTANT: The Kubernetes Operator tracks any changes to the ConfigMap and reconciles the state of the `MongoDB` resource. | `<my-project>` |
| \| `spec` \| `.clusterSpecList` \| `.clusterName` | string | Name of the cluster in the `MongoDBMultiCluster` resource. | `cluster1.example.com` |
| \| `spec` \| `.clusterSpecList` \| `.members` | integer | The number of members in this cluster. | `2` |
| \| `spec` \| `.clusterSpecList` \| `.statefulSet` \| `.spec` | collection | *Optional.* Provides the configuration for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) override for each of the cluster's StatefulSets in a multi-Kubernetes cluster MongoDB deployment. If specified at an individual cluster level under `clusterSpecList`, overrides the global configuration for the StatefulSet for the entire multi-Kubernetes cluster MongoDB deployment. See multi-cluster-specification and `StatefulSet v1 apps Kubernetes documentation`. | See the example. |
| \| `spec` \| `.clusterSpecList` \| `.statefulSet` \| `.spec` \| `.volumeClaimTemplates` \| `.spec` | collection | *Optional.* If specified, provides a per-cluster override for the default storage size of the `volumeClaimtemplates`, for the persistent volume that stores the data. | See the example. |
| `spec.credentials` | string | Name of the secret you created as `Ops Manager` API (Application Programming Interface) authentication credentials for the Kubernetes Operator to communicate with Ops Manager. The `Ops Manager` Kubernetes Secret object holding the Credentials must exist on the **same** Namespace as the resource you want to create. IMPORTANT: The Kubernetes Operator tracks any changes to the Secret and reconciles the state of the `MongoDB` resource. | `<mycredentials>` |
| `spec.type` | string | Type of `MongoDB` resource to create. The only supported value for this field is `ReplicaSet`. See Limitations. | `ReplicaSet` |

**Step 6: Add any additional accepted settings for a `MongoDBMultiCluster` resource deployment.**

You can also add any optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. See multi-cluster-specification.

**Step 7: Save this replica set config file with a `.yaml` extension.**

**Step 8: Start your replica set deployment.**

In any directory, invoke the following Kubernetes command to create your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 9: Track the status of your multi-Kubernetes cluster MongoDB deployment.**

To check the status of your `MongoDBMultiCluster` resource, use the following
command on the central cluster:

```sh
kubectl get mdbmc <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.

### Renew TLS Certificates for a `MongoDBMultiCluster` Resource

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

**non-encrypted-rs:**

This procedure doesn't encrypt connections between MongoDB hosts in
a replica set, and between client applications and MongoDB deployments.

### Deploy a `MongoDBMultiCluster` Resource

**Step 1: Configure `kubectl` to use the central cluster's namespace.**

If you have not done so already, run the following commands to run
all `kubectl` commands on the central cluster in the default
namespace.

```sh
kubectl config use-context $MDB_CENTRAL_CLUSTER_FULL_NAME
kubectl config set-context $(kubectl config current-context) \
  --namespace=mongodb
```

**Step 2: Copy and paste the sample  resource.**

a. Copy the sample replica set YAML (Yet Another Markup Language) file and paste it into a new
   text file.

b. Change the file's settings to match your desired replica set configuration.

```yaml
# This example provides statefulSet overrides per cluster.

apiVersion: mongodb.com/v1
kind: MongoDBMultiCluster
metadata:
  name: multi-replica-set
spec:
  version: 8.0.0
  type: ReplicaSet
  duplicateServiceObjects: false
  credentials: my-credentials
  opsManager:
    configMapRef:
      name: my-project
  clusterSpecList:
    - clusterName: cluster1.example.com
      members: 2
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar1
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          # Use the following settings to override the default storage size of the "data" Persistent Volume.
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi
    - clusterName: cluster2.example.com
      members: 1
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar2
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi
    - clusterName: cluster3.example.com
      members: 1
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar3
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi

...
```

**Step 3: Change the settings to your preferred values.**

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Label for the `MongoDBMultiCluster` resource. Resource names must be 44 characters or less. See also `metadata.name` and `names` in the Kubernetes documentation. | `multi-replica-set` |
| `spec.version` | string | Version of MongoDB that this `MongoDBMultiCluster` resource should run. The format should be `X.Y.Z` for the Community edition and `X.Y.Z-ent` for the Enterprise edition. IMPORTANT: Ensure that you choose a compatible MongoDB Server version. Compatible versions differ depending on the base image that the MongoDB database resource uses. To learn more about MongoDB versioning, see release-version-numbers in the MongoDB Manual. | `8.0.0` |
| \| `spec` \| `.opsManager` \| `.configMapRef` \| `.name` | string | Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection configuration. The `spec.cloudManager.configMapRef.name` setting is an alias for this setting and can be used in its place. This value must exist on the *same* namespace as the resource you want to create. IMPORTANT: The Kubernetes Operator tracks any changes to the ConfigMap and reconciles the state of the `MongoDB` resource. | `<my-project>` |
| \| `spec` \| `.clusterSpecList` \| `.clusterName` | string | Name of the cluster in the `MongoDBMultiCluster` resource. | `cluster1.example.com` |
| \| `spec` \| `.clusterSpecList` \| `.members` | integer | The number of members in this cluster. | `2` |
| \| `spec` \| `.clusterSpecList` \| `.statefulSet` \| `.spec` | collection | *Optional.* Provides the configuration for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) override for each of the cluster's StatefulSets in a multi-Kubernetes cluster MongoDB deployment. If specified at an individual cluster level under `clusterSpecList`, overrides the global configuration for the StatefulSet for the entire multi-Kubernetes cluster MongoDB deployment. See multi-cluster-specification and `StatefulSet v1 apps Kubernetes documentation`. | See the example. |
| \| `spec` \| `.clusterSpecList` \| `.statefulSet` \| `.spec` \| `.volumeClaimTemplates` \| `.spec` | collection | *Optional.* If specified, provides a per-cluster override for the default storage size of the `volumeClaimtemplates`, for the persistent volume that stores the data. | See the example. |
| `spec.credentials` | string | Name of the secret you created as `Ops Manager` API (Application Programming Interface) authentication credentials for the Kubernetes Operator to communicate with Ops Manager. The `Ops Manager` Kubernetes Secret object holding the Credentials must exist on the **same** Namespace as the resource you want to create. IMPORTANT: The Kubernetes Operator tracks any changes to the Secret and reconciles the state of the `MongoDB` resource. | `<mycredentials>` |
| `spec.type` | string | Type of `MongoDB` resource to create. The only supported value for this field is `ReplicaSet`. See Limitations. | `ReplicaSet` |

**Step 4: Add any additional accepted settings for a `MongoDBMultiCluster` resource deployment.**

You can also add any optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. See multi-cluster-specification.

**Step 5: Save this replica set config file with a `.yaml` extension.**

**Step 6: Start your replica set deployment.**

In any directory, invoke the following Kubernetes command to create your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 7: Track the status of your multi-Kubernetes cluster MongoDB deployment.**

To check the status of your `MongoDBMultiCluster` resource, use the following
command on the central cluster:

```sh
kubectl get mdbmc <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.
