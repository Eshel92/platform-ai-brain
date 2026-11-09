<!-- Converted from tutorial/configure-mongodb-specific-storage.txt (reStructuredText). Includes are inlined. -->

# Configure Storage Options for MongoDB Resources

You can configure your MongoDB resources to bind to specific storage in 
your `MongoDB` [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). The `persistence` field in the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) 
allows you to more precisely manage where Kubernetes stores the logs and metadata 
generated from MongoDB custom resources. Controlling log and metadata storage 
allows you to have more fine-grained control of processes that manage and 
interact with this generated metadata.

You can configure persistence settings per component in the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). 
These settings allow you to specify the relationship between a given 
component and one or more related `PersistentVolume` resources, which
store output from your MongoDB custom resources.

The `persistence` setting specifies the number of and storage capacity 
of `persistentVolumes` associated with MongoDB custom resource-managed objects 
in your Kubernetes cluster.

## Prerequisites

To configure storage options for your 
MongoDB deployment, you must either have a MongoDB replica set deployed 
through the MongoDB Kubernetes Operator or meet the following prerequisites:

- An Ops Manager instance or a `Cloud Manager organization`.

- The MongoDB Controllers for Kubernetes Operator.

- A Kubernetes Operator ConfigMap.

- Credentials for the Kubernetes Operator or 
  configure a different secret storage tool.

## Procedure

To create a single `PersistentVolume` in which a given component will store 
all MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) output, define the component's `persistence` as `single`. To create a 
distinct `PersistentVolume` for the component's `data`, `journal`, 
and `logs`, define the component's `persistence` as `multiple`.

**Step 1: Update your MongoDB custom resource.**

Populate the `persistence` sections of your MongoDB CRD
definition as shown in the following example:

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-sharded-cluster
spec:
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 3
  version: "8.0.0"
  service: my-service
  type: ShardedCluster

  persistent: true

  configSrvPodSpec:
    persistence:
      single: true

  shardPodSpec:
    persistence:
      multiple:
        # if the child of "multiple" is omitted then the default size will be used.
        # 16GB for "data", 1GB for "journal", 3GB for "logs"
        data:
          storage: "20Gi"
          storageClass: standard # You must define a storageClass, as the Operator creates a PVC, which will only create an associated PV with a backing storageClass.
        logs:
          storage: "4Gi"
          storageClass: standard
...
```

**Step 2: Apply your changes.**

```sh
kubectl apply -f mongodb-crd.yaml
```
