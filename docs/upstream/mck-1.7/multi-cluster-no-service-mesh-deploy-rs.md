<!-- Converted from multi-cluster-no-service-mesh-deploy-rs.txt (reStructuredText). Includes are inlined. -->

# Deploy Replica Sets in a Multi-Kubernetes Cluster without a Service Mesh

Use this procedure to deploy a replica set in a multi-Kubernetes cluster MongoDB deployment without
using a service mesh for establishing external connectivity between member
Kubernetes clusters.

As an alternative to using this procedure, you can use the
multi-cluster-quick-start-ref, which uses a service mesh.

## Before You Begin

- Learn about multi-Kubernetes-cluster deployments.
- Review the list of multi-Kubernetes-cluster services and tools.

- Complete the prerequisites, but don't set up a service mesh.
  Instead, decide whether you need a service mesh.
  If you choose to deploy without a service mesh,
  use external domains and configure DNS to enable external connectivity.
- As part of completing the prerequisites, generate valid certificates for
  TLS (Transport Layer Security) encryption. To learn more, see multi-cluster-tls-prereqs.
- Deploy the Ops Manager resources.
- Install the Kubernetes Operator in a multi-Kubernetes cluster MongoDB deployment. See multi-cluster-quick-start-ref.

## Overview

In a multi-Kubernetes cluster MongoDB deployment without a service mesh, use the following
`MongoDBMultiCluster` resource settings:

- Use the spec.clusterSpecList.externalAccess.externalService
  setting so that the Kubernetes Operator creates an external service, and as part of
  its default configuration, configures a load balancer with default settings.
  Configure the load balancer to serve as the TCP proxy with a TLS (Transport Layer Security) passthrough
  (no TLS termination in the load balancer).

- Customize external services that the Kubernetes Operator creates for each Pod
  in the Kubernetes cluster. Use the global "all-clusters" configuration in the
  spec.externalAccess settings and
  Kubernetes cluster-specific overrides in the spec.clusterSpecList.externalAccess.externalService settings.

- Specify cloud provider-specific annotations for the load balancer in
  the spec.clusterSpecList.externalAccess.externalService.annotations
  for each Kubernetes cluster.

- Specify an external domain in spec.clusterSpecList.externalAccess.externalDomain.
  This allows the Kubernetes Operator to register `mongod` processes by using
  the domain suffix. This enables external connections to the `mongod` processes
  in a multi-Kubernetes cluster MongoDB deployment.

## Deploy a `MongoDBMultiCluster` Resource  without a Service Mesh

The following procedure establishes TLS (Transport Layer Security)-encrypted connections between
MongoDB hosts in a replica set, and between client applications and
MongoDB deployments.

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
# Provides statefulSet override per cluster

apiVersion: mongodb.com/v1
kind: MongoDBMultiCluster
metadata:
  name: multi-replica-set
spec:
  version: 8.0.0
  type: ReplicaSet
  credentials: my-credentials
  opsManager:
    configMapRef:
      name: my-project
  externalAccess:
    externalService: 
      annotations:
        # Global cloud-specific annotations added to external services in all clusters
       spec:
        # ServiceSpec attributes to override in external services in all clusters
  clusterSpecList:
    - clusterName: cluster1.example.com
      members: 2
      externalAccess:
        # Domain suffix that mongod processes will use in cluster1
        externalDomain: cluster1.example.com
        externalService:
          annotations:
            # Cloud-specific annotations for external services
          spec:
            # ServiceSpec attributes to override if necessary
    - clusterName: cluster2.example.com
      members: 1
      externalAccess:
        # Domain suffix that mongod processes will use in cluster2
        externalDomain: cluster2.example.com
        externalService:
          annotations:
            # Cloud-specific annotations for external services
          spec:
            # ServiceSpec attributes to override if necessary
    - clusterName: cluster3.example.com
      members: 1
      externalAccess:
        # Domain suffix that mongod processes will use in cluster3
        externalDomain: cluster3.example.com
        externalService:
          annotations:
            # Cloud-specific annotations for external services
          spec:
            # ServiceSpec attributes to override if necessary

...
```

**Step 5: Define external connectivity settings.**

Specify global values that affect all clusters in a multi-Kubernetes cluster MongoDB deployment using
the spec.externalAccess settings and
cluster-specific overrides using the
spec.clusterSpecList.externalAccess.externalService settings.

When you provide these settings in the `MongoDBMultiCluster` resource specification,
the Kubernetes Operator creates external services for each Pod in all
Kubernetes clusters. You then use these services to establish external
connectivity to all `mongod` processes in your deployment.

**Step 6: Define an external domain for each Kubernetes member cluster.**

Define an external domain for each member cluster using the
spec.clusterSpecList.externalAccess.externalDomain
setting.

As a result, the Kubernetes Operator registers all `mongod` processes in the
Kubernetes member cluster under a hostname according to the following convention:

```sh
<pod-name>.<externalDomain>
```

For example, a `mongod` process may have the following hostname:
`my-replica-set-0-0.cluster-1.example.com`.

**Step 7: Change the settings to your preferred values.**

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

**Step 8: Add any additional accepted settings for a `MongoDBMultiCluster` resource deployment.**

You can also add any optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. See multi-cluster-specification.

**Step 9: Save this replica set config file with a `.yaml` extension.**

**Step 10: Start your replica set deployment.**

In any directory, invoke the following Kubernetes command to create your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 11: Verify external connectivity for each member cluster.**

1. Check the status of external services in all member clusters:

   ```sh
   kubectl get services
   ```

   Kubernetes should return one external service created for each Pod of the replica set in all member clusters.

#. Verify that each external service is exposed externally and is reachable.
   Run the command similar to the following example:

   ```sh
   mongosh mongodb://my-replica-set-0-0.cluster-0.example.com:27017 \
   -tls -tlsCAFile "issuer-ca.pem"
   ```

   Connecting to `my-replica-set-0-0.cluster-0.example.com:27017` should
   direct client traffic to an external service named `my-replica-set-0-0-svc-external`,
   which, in turn, directs traffic to the `mongod` process.

#. Configure your DNS (Domain Name System) zone for the specified external domain to point to
   the corresponding external services. This configuration depends on
   your environment or the cloud provider you are using.

**Step 12: Track the status of your multi-Kubernetes cluster MongoDB deployment.**

To check the status of your `MongoDBMultiCluster` resource, use the following
command on the central cluster:

```sh
kubectl get mdbmc <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.
