<!-- Converted from tutorial/plan-k8s-install-single-or-multi-clusters.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Choose Kubernetes Operator Installation Mode: Single- or Multi-Kubernetes Clusters

The Kubernetes Operator can manage custom resources for single- and multi-Kubernetes
clusters. Before you install the Kubernetes Operator, decide which type of
Kubernetes cluster deployment you want to support, single- or multi-Kubernetes cluster.

## Kubernetes Operator Watches Single-Kubernetes Cluster Resources

You can configure the Kubernetes Operator to watch `Ops Manager` resources and `MongoDB` resources
for a replica set or a sharded cluster in a single Kubernetes cluster.
For steps, see Install the Operator.

## Kubernetes Operator Watches Multi-Kubernetes Cluster Resources

You can configure the Kubernetes Operator to watch `Ops Manager` resources, `MongoDB` resources,
and `MongoDBMultiCluster` resources for a replica set in a multi-Kubernetes cluster. For steps,
see Multi-Kubernetes-Cluster Quick Start.

## Kubernetes Operator Watches Resources in a Single- and Multi-Kubernetes Cluster

You can configure the Kubernetes Operator to watch the following types of [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/):

- `MongoDB` resources
- `Ops Manager` resources
- `MongoDBUsers` resources
- `MongoDBMultiCluster` resources

Depending on the watched resources, the Kubernetes Operator reconciles resources
based on the given [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).

To support custom resources deployed in single- and multi-Kubernetes clusters,
set up one instance of the Kubernetes Operator that will watch for and reconcile
custom resources for a single Kubernetes cluster and a multi-Kubernetes cluster MongoDB deployment.
Use different non-overlapping subsets of namespaces for each type of resource.

Set `.Values.operator.watchedResources` as follows:

```yaml
-watch-resource=MongoDB \
-watch-resource=OpsMnagers \
-watch-resource=MongoDBusers \
-watch-resource=MongoDBMultiCluster
```

**Note:**

Install and set up a single Kubernetes Operator instance and configure it
to watch one, many, or all custom resources in different, non-overlapping
subsets of namespaces. See also faq-many-operators

### Next Steps

After deciding how you want to install the Kubernetes Operator, you can:

- Set the scope of your deployments for
  single Kubernetes clusters, or set the multi-Kubernetes cluster deployment's scope.
- Install single-Kubernetes cluster. For single-Kubernetes clusters, review the
  considerations, complete the prerequisites
  and install the Kubernetes Operator.
- Install the Kubernetes Operator in a multi-Kubernetes cluster MongoDB deployment. See the Multi-Kubernetes-Cluster Quick Start.
