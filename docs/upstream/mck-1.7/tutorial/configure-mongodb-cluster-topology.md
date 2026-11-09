<!-- Converted from tutorial/configure-mongodb-cluster-topology.txt (reStructuredText). Includes are inlined. -->

# Configure Cluster Topology for MongoDB Resources

You can configure the deployment topology of your MongoDB resources within 
Kubernetes by defining `NodeAffinity` and `PodAffinity`. 
`NodeAffinity` and `PodAffinity` specify 
where Kubernetes deploys MongoDB custom resources in your Kubernetes cluster.

You can implement [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) by applying [node labels](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels) to specific 
nodes within your Kubernetes cluster and defining `labelSelector` fields 
with corrosponding labels in your MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). When you apply 
[node labels](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels) and matching `labelSelector` values, Kubernetes only
deploys a given MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) on the nodes you
specify within your Kubernetes cluster. Implementing node affinity rules can be useful when
deploying MongoDB resources in heterogeneous node groups, as it allows you
to deploy specific resources on specific node varieties.

Similarly, you can implement Pod affinity by applying [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to Pods that are 
running in your cluster and aligning those label values with `labelSelector` 
values defined in your MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). When you apply [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) 
and matching `labelSelector` values, Kubernetes colocates MongoDB 
custom resource-managed Pods with Pods with matching labels applied. By 
collocating Pods, you can improve system performance and reduce latency 
between Pods that communicate regularly. You can also define Pod antiaffinity 
rules which allow you to specify Pods which should not be colocated.

For Standalone and Replica Set deployments, you can apply these affinity rules 
to the `spec.podSpec` of your MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). 
For Sharded Cluster deployments, you can apply these affinity rules to the
`spec.configSrvPodSpec`, `spec.shardPodSpec`, 
and `spec.mongosPodSpec` sections of your MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).

You must deploy MongoDB resources, such as `mongos`, shards, 
and config servers in the case of a Sharded Cluster deployment, 
in the same namespace as the MongoDB resource. However, within that namespace, 
you can configure the `nodeAffinity` and `podAffinity` for `mongos`, 
shards, and config server resource types in the `ShardedCluster` [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).

## Prerequisites

To configure the deployment topology for your 
MongoDB deployment, you must either have a MongoDB replica set deployed 
through the MongoDB Kubernetes Operator along with labels applied 
to the Kubernetes resources that will align with `labelSelectors` defined 
in the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) or meet the following prerequisites:

- An Ops Manager instance or a `Cloud Manager organization`.

- The MongoDB Controllers for Kubernetes Operator.

- A Kubernetes Operator ConfigMap.

- Credentials for the Kubernetes Operator or 
  configure a different secret storage tool.

- Labels applied to the Kubernetes resources that will align with `labelSelectors` 
  defined in the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).

## Procedure

**Step 1: Update your MongoDB CRD manifest.**

Populate the `podTemplate.spec.affinity` sections of your MongoDB Sharded Cluster
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
  version: 8.0.0
  service: my-service

  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  type: ShardedCluster

  persistent: true
  configSrvPodSpec:
    podTemplate:
      spec:
        affinity:
          podAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                    - key: security
                      operator: In
                      values:
                        - S1
                topologyKey: failure-domain.beta.kubernetes.io/zone
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
                - matchExpressions:
                    - key: kubernetes.io/e2e-az-name
                      operator: In
                      values:
                        - e2e-az1
                        - e2e-az2
          podAntiAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                topologyKey: nodeId
  mongosPodSpec:
    podTemplate:
      spec:
        affinity:
          podAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                    - key: security
                      operator: In
                      values:
                        - S1
                topologyKey: failure-domain.beta.kubernetes.io/zone
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
                - matchExpressions:
                    - key: kubernetes.io/e2e-az-name
                      operator: In
                      values:
                        - e2e-az1
                        - e2e-az2
          podAntiAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                topologyKey: nodeId
  shardPodSpec:
    podTemplate:
      spec:
        affinity:
          podAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                    - key: security
                      operator: In
                      values:
                        - S1
                topologyKey: failure-domain.beta.kubernetes.io/zone
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
                - matchExpressions:
                    - key: kubernetes.io/e2e-az-name
                      operator: In
                      values:
                        - e2e-az1
                        - e2e-az2
          podAntiAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                topologyKey: nodeId
...
```

**Step 2: Apply your changes.**

```sh
kubectl apply -f mongodb-crd.yaml
```
