<!-- Converted from tutorial/edit-deployment.txt (reStructuredText). Includes are inlined. -->

# Edit a Database Resource

You can modify a deployment's configuration and topology, including its
MongoDB versions, storage engines, and numbers of hosts or shards. You
can make modifications at all levels of a deployment's topology from a
top-level sharded cluster or
replica set to lower levels, such as a replica set within a
sharded cluster, or an individual process within a replica set. You can
also modify standalone processes.

## Considerations

- You can't change individual members of a replica set or sharded cluster.
  You can change only the whole set or cluster.

- If a setting isn't available for a MongoDB resource, you can make changes
  using only the `Ops Manager` or `Cloud Manager` application.

  - .. include:: /includes/admonitions/fact-unsupported-mongod-options.rst

- You can configure certain settings using only the Kubernetes Operator. To
  review the list of settings, see /reference/k8s-op-exclusive-settings.

## Prerequisites

Before you update a MongoDB [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), complete the following procedures:

- k8s-install-configure
- create-k8s-credentials
- create-k8s-project
- k8s-deploy-mdb-resources

## Procedure

**Step 1: Edit the Kubernetes resource specification file.**

**Step 2: Modify or add settings as needed.**

**Step 3: Save your specification file.**

**Step 4: Apply the file.**

```sh
kubectl apply -f <standalone-conf>.yaml
```
