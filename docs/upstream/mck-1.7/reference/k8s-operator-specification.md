<!-- Converted from reference/k8s-operator-specification.txt (reStructuredText). Includes are inlined. -->

# MongoDB Database Resource Specification

**Note:**

At any place on this page that says *Ops Manager*, you can substitute *Cloud Manager*.

The MongoDB Controllers for Kubernetes Operator
creates Kubernetes [statefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) from specification files that you write.

The Kubernetes Operator creates MongoDB-specific resources in Kubernetes as
`custom resources`.

To manage these custom resources, use the following process:

1. Create or update a `MongoDB` resource specification.
2. Direct MongoDB Controllers for Kubernetes Operator to apply it to your Kubernetes environment.
   As a result, Kubernetes Operator performs these actions:

   - Creates the defined [statefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), services and other Kubernetes resources.
   - Updates the `Ops Manager` deployment configuration to reflect changes.

| Deployment Type | StatefulSets | Size of StatefulSet |
|---|---|---|
| Standalone | 1 | 1 [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) |
| Replica Set | 1 | 1 [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) per member |
| Sharded Cluster | <numberOfShards> + 2 | 1 [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) per `mongos`, shard, or config server member |

Each `MongoDB` resource uses an object specification in YAML (Yet Another Markup Language) to define the
characteristics and settings of the MongoDB object: standalone,
replica set, and sharded cluster.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `k8s-operator-specification.parts/`)

- `001-common-resource-settings-deployment-specific-resou.md`: Common Resource Settings … Deployment-Specific Resource Settings
- `002-deployment-specific-resource-settings-standalone-s.md`: Deployment-Specific Resource Settings › Standalone Settings
- `003-deployment-specific-resource-settings-replica-set-.md`: Deployment-Specific Resource Settings › Replica Set Settings
- `004-deployment-specific-resource-settings-sharded-clus.md`: Deployment-Specific Resource Settings › Sharded Cluster Settings
- `005-prometheus-settings.md`: Prometheus Settings
- `006-security-settings.md`: Security Settings
- `007-examples-statefulset-settings.md`: Examples … StatefulSet Settings
