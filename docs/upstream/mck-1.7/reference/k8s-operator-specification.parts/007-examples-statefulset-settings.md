<!-- Part 7 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

## Examples

tabs:
  - id: standalone
    name: Standalone Pod
    content: |

      The following example shows a resource specification for a
      standalone deployment with every setting provided:

      ```yaml
      apiVersion: mongodb.com/v1
      kind: MongoDB
      metadata:
        name: my-standalone
      spec:
        version: "8.0.0"
        service: my-service
        opsManager: # Alias of cloudManager
          configMapRef:
            name: my-project
        credentials: my-credentials
        persistent: true
        type: Standalone
        additionalMongodConfig:
          systemLog:
            logAppend: true
            verbosity: 4
          operationProfiling:
            mode: slowOp
        podSpec:
          persistence:
            single:
              storage: "12Gi"
              storageClass: standard
              labelSelector:
                matchExpressions:
                - {key: environment, operator: In, values: [dev]}
          podTemplate:
            metadata:
              labels:
                label1: mycustomlabel
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
                  preferredDuringSchedulingIgnoredDuringExecution:
                    - podAffinityTerm:
                        topologyKey: "mykey"
                      weight: 50
      ...
      ```

  - id: replicaset
    name: Replica Set Pod
    content: |

      The following example shows a resource specification for a
      replica set with every setting provided:

      ```yaml
      ---
      apiVersion: mongodb.com/v1
      kind: MongoDB
      metadata:
        name: my-replica-set
      spec:
        members: 3
        version: "8.0.0"
        service: my-service
        opsManager: # Alias of cloudManager
          configMapRef:
            name: my-project
        credentials: my-credentials
        persistent: true
        type: ReplicaSet
        podSpec:
          persistence:
            multiple:
              data:
                storage: "10Gi"
              journal:
                storage: "1Gi"
                labelSelector:
                  matchLabels:
                    app: "my-app"
              logs:
                storage: "500M"
                storageClass: standard
          podTemplate:
            metadata:
              labels:
                label1: mycustomlabel
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
                  preferredDuringSchedulingIgnoredDuringExecution:
                    - podAffinityTerm:
                        topologyKey: "mykey"
                      weight: 50
        security:
          certsSecretPrefix: "prefix"
          tls:
            ca: custom-ca
          authentication:
            enabled: true
            modes: ["X509"]
            internalCluster: "X509"
        statefulSet:
          spec:
            serviceName: my-service
        additionalMongodConfig:
          net:
            ssl:
              mode: preferSSL
      ...
      ```

  - id: shardedcluster
    name: Sharded Cluster Pod
    content: |

      The following example shows a resource specification for a
      sharded cluster with every setting provided:

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

        ## Please Note: The default Kubernetes cluster name is
        ## `cluster.local`.
        ## If your cluster has been configured with another name, you can
        ## specify it with the `clusterDomain` attribute.

        opsManager: # Alias of cloudManager
          configMapRef:
            name: my-project
        credentials: my-credentials

        persistent: true
        configSrvPodSpec:

          # if "persistence" element is omitted then Operator uses the
          # default size (5Gi) for mounting single Persistent Volume

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
          persistence:
            multiple:
              # if the child of "multiple" is omitted then the default size will be used.
              # 16GB for "data", 1GB for "journal", 3GB for "logs"
              data:
                storage: "20Gi"
              logs:
                storage: "4Gi"
                storageClass: standard
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
        mongos:
          additionalMongodConfig:
            systemLog:
              logAppend: true
              verbosity: 4
        configSrv:
          additionalMongodConfig:
            operationProfiling:
              mode: slowOp
        shard:
          additionalMongodConfig:
            storage:
              journal:
                commitIntervalMs: 50
        security:
          certsSecretPrefix: "prefix"
          tls:
           ca: custom-ca
          authentication:
            enabled: true
            modes: ["X509"]
            internalCluster: "X509"
        statefulSet:
          spec:
            serviceName: my-service
      ...
      ```


## StatefulSet Settings

The following [statefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) settings apply only to replica set and
sharded cluster resource types.

The Kubernetes Operator supports overriding the Kubernetes Operator default
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) and PVC (PersistentVolumeClaim) settings by
specifying values for `spec.statefulSet.spec` fields in the MongoDB
resource specification. However, only certain fields are preserved
during the merge process. The following tables list the supported
override fields.

**`spec.statefulSet.spec`**

*Type*: collection

Specification for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
for `MongoDB` resources.

### StatefulSet Override Fields

The following fields are merged in and take precedence over default
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) settings when you specify values in
`spec.statefulSet.spec`. Field paths are relative to the
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) definition, so `spec.replicas` corresponds to
`spec.statefulSet.spec.replicas` in the MongoDB resource specification.

| Field |
|---|
| `spec.replicas` |
| `spec.selector` |
| `spec.podManagementPolicy` |
| `spec.revisionHistoryLimit` |
| `spec.updateStrategy.type` |
| `spec.updateStrategy.rollingUpdate` |
| `spec.serviceName` |
| `spec.template` |
| `spec.volumeClaimTemplates` |

**`spec.statefulSet.spec.serviceName`**

*Type*: string

*Default*: `<resource_name>-svc` and `<resource_name>-svc-external`

Name of the Kubernetes service to be created or used for a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).
If the service with this name already exists, the MongoDB Controllers for Kubernetes Operator doesn't
delete or recreate it. This setting lets you create your own custom
services and lets the Kubernetes Operator reuse them.

### PVC (VolumeClaimTemplates) Override Fields

The Kubernetes Operator merges a volume claim template that you specify in
`spec.statefulSet.spec.volumeClaimTemplates` only if its
`metadata.name` matches the name of an existing volume claim template.
The following table shows which PVC (PersistentVolumeClaim)
fields the Kubernetes Operator preserves and which it drops when you specify
values in `spec.statefulSet.spec.volumeClaimTemplates`. Field paths are
relative to an individual volume claim template, so `spec.volumeMode`
corresponds to
`spec.statefulSet.spec.volumeClaimTemplates.spec.volumeMode` in the
MongoDB resource specification.

| Supported (Preserved) | Not Supported (Dropped) |
|---|---|
| \| `metadata.namespace` \| `metadata.labels` \| `metadata.annotations` \| `spec.volumeMode` \| `spec.storageClassName` \| `spec.accessModes` [#pvc-access-modes]_ \| `spec.selector` \| `spec.resources.limits` \| `spec.resources.requests` \| `spec.dataSource` | \| `spec.volumeAttributesClassName` \| `spec.dataSourceRef` \| `spec.volumeName` |
