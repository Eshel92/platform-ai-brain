<!-- Converted from tutorial/multi-cluster-edit-deployment.txt (reStructuredText). Includes are inlined. -->

# Edit a MongoDBMultiCluster Resource

You can modify configuration and topology of the `MongoDBMultiCluster` resource, including
its MongoDB versions, storage engines, and Kubernetes clusters.

## Considerations

- You can't change individual members of a replica set, you can change only
  the whole set or Kubernetes cluster.
  For a complete list of options supported by a `MongoDBMultiCluster` resource,
  see the multi-cluster-specification.

- You can configure certain settings only using Kubernetes Operator. To learn
  more, see k8s-exclusive-settings.

## Prerequisites

To update a `MongoDBMultiCluster` resource, you must have it installed and deployed.

- multi-cluster-quick-start-ref
- multi-cluster-deploy-replica-set

## Procedure

**Step 1: Edit the Kubernetes `MongoDBMultiCluster` resource specification file.**

**Step 2: Modify or add settings as needed.**

To learn about the settings you can change, see the multi-cluster-specification.

**Step 3: Save your specification file.**

**Step 4: Apply the file.**

```sh
kubectl apply -f <mongodb-multi-conf>.yaml
```
