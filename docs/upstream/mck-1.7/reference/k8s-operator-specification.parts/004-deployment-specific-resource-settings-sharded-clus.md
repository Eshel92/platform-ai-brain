<!-- Part 4 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

### Sharded Cluster Settings

**Note:**

All of the replica-set-settings also apply to sharded cluster
resources unless otherwise specified.

The following settings apply only to sharded cluster resource types:

**`spec.backup.snapshotSchedule.clusterCheckpointIntervalMin`**

*Type*: number

Number of minutes between successive cluster checkpoints. This setting
applies only to sharded clusters that run MongoDB with a feature compatibility version of 7.0 or
earlier. This number determines the granularity of point-in-time
restores for sharded clusters. You can set a value of `15`, `30`,
or `60`.

**`spec.configServerCount`**

*Type*: integer

*Required*. Number of members in the config server.

**`spec.configSrv.additionalMongodConfig`**

*Type*: collection

Additional `configuration options` with
which you want to start each config server member.

The Kubernetes Operator supports all configuration options that the MongoDB
version you deploy through the MongoDB Agent supports, except that the 
Kubernetes Operator overrides values that you provide for any of the 
following options:

- `net.tls.certificateKeyFile`
- `net.tls.clusterFile`
- `replication.replSetName`
- `security.clusterAuthMode`
- `sharding.clusterRole`
- `storage.dbPath`
- `systemLog.destination`
- `systemLog.path`

To learn more about the configuration options that the Kubernetes Operator
owns, see k8s-exclusive-settings.

To learn which configuration options you can use, see
`Advanced Options for MongoDB Deployments` in the Ops Manager 
documentation.

**`spec.configSrv.agent`**

*Type*: collection

MongoDB Agent configuration settings for each config server member.

**`spec.configSrv.agent.startupOptions`**

*Type*: collection

MongoDB Agent settings with which you want to start each config server member.

You must provide MongoDB Agent settings as key-value pairs. The values
must be strings.

For a list of supported MongoDB Agent settings, see:

- `MongoDB Agent Settings`
  for Cloud Manager projects.
- `MongoDB Agent Settings` for the Ops Manager version you
  deployed with the Kubernetes Operator. 

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-sharded-cluster-options
spec:
  version: "8.0.0"
  type: ShardedCluster
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  persistent: true
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 1

  mongos:
    agent:
      startupOptions:
        maxLogFiles: "30"

  configSrv:
     agent:
       startupOptions:
         dialTimeoutSeconds: "40"
  shard:
     agent:
       startupOptions:
         serverSelectionTimeoutSeconds: "20"
...
```

**`spec.configSrvPodSpec`**

*Type*: object

Object that contains the specifications for the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) config server Pods.

**`spec.configSrvPodSpec.persistence.single`**

*Type*: collection

Has Kubernetes Operator create one [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount all
three directories for data, journal, and logs to the same [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.multiple`
  collections but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum size of [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that should be mounted. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 5Gi. For example, if each config server member in requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage specified in a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims). You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.configSrvPodSpec.persistence.multiple.data`**

*Type*: collection

Has Kubernetes Operator create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount a
directory for data to its own [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.single`
  collection but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host each config server member on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 16Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for each config server member. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.configSrvPodSpec.persistence.multiple.journal`**

*Type*: collection

Has Kubernetes Operator create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount a
directory for journal to its own [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.single`
  collection but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host each config server member on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 1Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for each config server member. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.configSrvPodSpec.persistence.multiple.logs`**

*Type*: collection

Has Kubernetes Operator create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount a
directory for logs to its own [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.single`
  collection but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host each config server member on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 3Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for each config server member. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.configSrvPodSpec.podTemplate`**

*Type*: collection

`Template`
for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for each config server member.

Template values take precedence over values specified in `spec.configSrvPodSpec`.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.configSrvPodSpec.podTemplate`.

**`spec.configSrvPodSpec.podTemplate.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
each config server member.

To review which fields you can add to `spec.configSrvPodSpec.podTemplate.metadata`, see
the `Kubernetes documentation`.

**`spec.configSrvPodSpec.podTemplate.spec`**

*Type*: collection

Specifications of the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
each config server member.

To review which fields you can add to `spec.configSrvPodSpec.podTemplate.spec`, see the
`Kubernetes PodSpec v1 core API`.

**Note:**

When you add containers to `spec.configSrvPodSpec.podTemplate.spec.containers`, the
Kubernetes Operator adds them to the Kubernetes pod. These containers are
appended to each config server member containers in the pod.

Use this setting to specify the CPU and RAM allocations for each pod. For
examples, see the samples on GitHub.

**`spec.configSrvPodSpec.podTemplate.spec.affinity.podAffinity`**

*Type*: collection

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to determine whether multiple `MongoDB` resource [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
must be co-located with other [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/). To learn more about the use cases,
see [Affinity and Anti-Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) in the Kubernetes documentation.

**`spec.configSrvPodSpec.podTemplate.spec.affinity.nodeAffinity`**

*Type*: collection

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to place [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) for replica set on a
specific range of [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

For optimized read-write performance, use node affinity rules that 
restrict [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), or to prefer 
to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

**`spec.configSrvPodSpec.podTemplate.spec.affinity.podAntiAffinity`**

*Type*: string

*Default*: kubernetes.io/hostname

Sets a [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to spread [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) hosting `MongoDB` resource
to different locations. A location can be a single node, rack, or
region. By default, Kubernetes Operator tries to spread pods across
different nodes.

**`spec.configSrvPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`**

*Type*: string

*Default*: kubernetes.io/hostname

This key defines which
`label`
is used to determine which topology
`domain`
a node belongs to.

**`spec.mongodsPerShardCount`**

*Type*: integer

*Required*. Number of members per shard.

**`spec.mongosCount`**

*Type*: integer

*Required*. Number of `mongos` instances in the sharded cluster.

**`spec.mongos.additionalMongodConfig`**

*Type*: collection

Additional `configuration options` with
which you want to start each mongos instance.

The Kubernetes Operator supports all configuration options that the MongoDB
version you deploy through the MongoDB Agent supports, except that the 
Kubernetes Operator overrides values that you provide for any of the 
following options:

- `net.tls.certificateKeyFile`
- `net.tls.clusterFile`
- `replication.replSetName`
- `security.clusterAuthMode`
- `sharding.clusterRole`
- `storage.dbPath`
- `systemLog.destination`
- `systemLog.path`

To learn more about the configuration options that the Kubernetes Operator
owns, see k8s-exclusive-settings.

To learn which configuration options you can use, see
`Advanced Options for MongoDB Deployments` in the Ops Manager 
documentation.

**`spec.mongos.agent`**

*Type*: collection

MongoDB Agent configuration settings for each `mongos` instance.

**`spec.mongos.agent.startupOptions`**

*Type*: collection

MongoDB Agent settings with which you want to start each `mongos` instance.

You must provide MongoDB Agent settings as key-value pairs. The values
must be strings.

For a list of supported MongoDB Agent settings, see:

- `MongoDB Agent Settings`
  for Cloud Manager projects.
- `MongoDB Agent Settings` for the Ops Manager version you
  deployed with the Kubernetes Operator. 

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-sharded-cluster-options
spec:
  version: "8.0.0"
  type: ShardedCluster
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  persistent: true
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 1

  mongos:
    agent:
      startupOptions:
        maxLogFiles: "30"

  configSrv:
     agent:
       startupOptions:
         dialTimeoutSeconds: "40"
  shard:
     agent:
       startupOptions:
         serverSelectionTimeoutSeconds: "20"
...
```

**`spec.mongosPodSpec`**

*Type*: object

Object that contains the specifications for the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) mongos Pods.

**`spec.mongosPodSpec.podTemplate`**

*Type*: collection

`Template`
for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for each `mongos` instance.

Template values take precedence over values specified in `spec.mongosPodSpec`.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.mongosPodSpec.podTemplate`.

**`spec.mongosPodSpec.podTemplate.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
each `mongos` instance.

To review which fields you can add to `spec.mongosPodSpec.podTemplate.metadata`, see
the `Kubernetes documentation`.

**`spec.mongosPodSpec.podTemplate.spec`**

*Type*: collection

Specifications of the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
each `mongos` instance.

To review which fields you can add to `spec.mongosPodSpec.podTemplate.spec`, see the
`Kubernetes PodSpec v1 core API`.

**Note:**

When you add containers to `spec.mongosPodSpec.podTemplate.spec.containers`, the
Kubernetes Operator adds them to the Kubernetes pod. These containers are
appended to each `mongos` instance containers in the pod.

Use this setting to specify the CPU and RAM allocations for each pod. For
examples, see the samples on GitHub.

**`spec.mongosPodSpec.podTemplate.spec.affinity.podAffinity`**

*Type*: collection

*Optional.* Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to determine if multiple
`MongoDB` resource [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) must be co-located with other [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/).

**`spec.mongosPodSpec.podTemplate.spec.affinity.nodeAffinity`**

*Type*: collection

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to place [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) for replica set on a
specific range of [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

For optimized read-write performance, use node affinity rules that 
restrict [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), or to prefer 
to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

**`spec.mongosPodSpec.podTemplate.spec.affinity.podAntiAffinity`**

*Type*: string

*Default*: kubernetes.io/hostname

Sets a [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to spread [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) hosting `MongoDB` resource
to different locations. A location can be a single node, rack, or
region. By default, Kubernetes Operator tries to spread pods across
different nodes.

**`spec.mongosPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`**

*Type*: string

*Default*: kubernetes.io/hostname

This key defines which
`label`
is used to determine which topology
`domain`
a node belongs to.

**`spec.shardCount`**

*Type*: integer

*Required*. Number of shards in the sharded cluster.

**`spec.shard.additionalMongodConfig`**

*Type*: collection

Additional `configuration options` with
which you want to start each sharded cluster shard member.

The Kubernetes Operator supports all configuration options that the MongoDB
version you deploy through the MongoDB Agent supports, except that the 
Kubernetes Operator overrides values that you provide for any of the 
following options:

- `net.tls.certificateKeyFile`
- `net.tls.clusterFile`
- `replication.replSetName`
- `security.clusterAuthMode`
- `sharding.clusterRole`
- `storage.dbPath`
- `systemLog.destination`
- `systemLog.path`

To learn more about the configuration options that the Kubernetes Operator
owns, see k8s-exclusive-settings.

To learn which configuration options you can use, see
`Advanced Options for MongoDB Deployments` in the Ops Manager 
documentation.

**`spec.shard.agent`**

*Type*: collection

MongoDB Agent configuration settings for each sharded cluster shard member.

**`spec.shard.agent.startupOptions`**

*Type*: collection

MongoDB Agent settings with which you want to start each sharded cluster shard member.

You must provide MongoDB Agent settings as key-value pairs. The values
must be strings.

For a list of supported MongoDB Agent settings, see:

- `MongoDB Agent Settings`
  for Cloud Manager projects.
- `MongoDB Agent Settings` for the Ops Manager version you
  deployed with the Kubernetes Operator. 

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-sharded-cluster-options
spec:
  version: "8.0.0"
  type: ShardedCluster
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  persistent: true
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 1

  mongos:
    agent:
      startupOptions:
        maxLogFiles: "30"

  configSrv:
     agent:
       startupOptions:
         dialTimeoutSeconds: "40"
  shard:
     agent:
       startupOptions:
         serverSelectionTimeoutSeconds: "20"
...
```

**`spec.shardPodSpec`**

*Type*: object

Object that contains the specifications for the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) shard Pods.

**`spec.shardPodSpec.persistence.multiple.data`**

*Type*: collection

Has Kubernetes Operator create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount a
directory for data to its own [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.single`
  collection but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host each sharded cluster shard member on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 16Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for each sharded cluster shard member. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.shardPodSpec.persistence.multiple.journal`**

*Type*: collection

Has Kubernetes Operator create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount a
directory for journal to its own [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.single`
  collection but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host each sharded cluster shard member on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 1Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for each sharded cluster shard member. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.shardPodSpec.persistence.multiple.logs`**

*Type*: collection

Has Kubernetes Operator create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount a
directory for logs to its own [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.single`
  collection but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host each sharded cluster shard member on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 3Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for each sharded cluster shard member. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.shardPodSpec.podTemplate`**

*Type*: collection

`Template`
for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for each sharded cluster shard member.

Template values take precedence over values specified in `spec.shardPodSpec`.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.shardPodSpec.podTemplate`.

**`spec.shardPodSpec.podTemplate.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
each sharded cluster shard member.

To review which fields you can add to `spec.shardPodSpec.podTemplate.metadata`, see
the `Kubernetes documentation`.

**`spec.shardPodSpec.podTemplate.spec`**

*Type*: collection

Specifications of the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
each sharded cluster shard member.

To review which fields you can add to `spec.shardPodSpec.podTemplate.spec`, see the
`Kubernetes PodSpec v1 core API`.

**Note:**

When you add containers to `spec.shardPodSpec.podTemplate.spec.containers`, the
Kubernetes Operator adds them to the Kubernetes pod. These containers are
appended to each sharded cluster shard member containers in the pod.

Use this setting to specify the CPU and RAM allocations for each pod. For
examples, see the samples on GitHub.

**`spec.shardPodSpec.podTemplate.spec.affinity.podAffinity`**

*Type*: string

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to determine whether multiple `MongoDB` resource [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
must be co-located with other [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/). To learn more about the use cases,
see [Affinity and Anti-Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) in the Kubernetes documentation.

**`spec.shardPodSpec.podTemplate.spec.affinity.nodeAffinity`**

*Type*: string

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to place [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) for replica set on a
specific range of [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

For optimized read-write performance, use node affinity rules that 
restrict [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), or to prefer 
to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

**`spec.shardPodSpec.podTemplate.spec.affinity.podAntiAffinity`**

*Type*: string

*Default*: kubernetes.io/hostname

Sets a [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to spread [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) hosting `MongoDB` resource
to different locations. A location can be a single node, rack, or
region. By default, Kubernetes Operator tries to spread pods across
different nodes.

**`spec.shardPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`**

*Type*: string

*Default*: kubernetes.io/hostname

This key defines which
`label`
is used to determine which topology
`domain`
a node belongs to.

**`spec.shardSpecificPodSpec`**

*Type*: array

List that contains [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) overrides per shard.

**`spec.shardSpecificPodSpec.podTemplate`**

*Type*: collection

`Template`
for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for the specific shard.

Template values take precedence over values specified in `spec.shardSpecificPodSpec`.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.shardSpecificPodSpec.podTemplate`.

**`spec.shardSpecificPodSpec.podTemplate.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
the specific shard.

To review which fields you can add to `spec.shardSpecificPodSpec.podTemplate.metadata`, see
the `Kubernetes documentation`.

**`spec.shardSpecificPodSpec.podTemplate.spec`**

*Type*: collection

Specifications of the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
the specific shard.

To review which fields you can add to `spec.shardSpecificPodSpec.podTemplate.spec`, see the
`Kubernetes PodSpec v1 core API`.

**Note:**

When you add containers to `spec.shardSpecificPodSpec.podTemplate.spec.containers`, the
Kubernetes Operator adds them to the Kubernetes pod. These containers are
appended to the specific shard containers in the pod.

Use this setting to specify the CPU and RAM allocations for each pod. For
examples, see the samples on GitHub.

**`spec.shardSpecificPodSpec.podTemplate.spec.affinity.podAffinity`**

*Type*: string

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to determine whether multiple `MongoDB` resource [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
must be co-located with other [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/). To learn more about the use cases,
see [Affinity and Anti-Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) in the Kubernetes documentation.

**`spec.shardSpecificPodSpec.podTemplate.spec.affinity.podAntiAffinity`**

*Type*: string

*Default*: kubernetes.io/hostname

Sets a [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to spread [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) hosting `MongoDB` resource
to different locations. A location can be a single node, rack, or
region. By default, Kubernetes Operator tries to spread pods across
different nodes.

**`spec.shardSpecificPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`**

*Type*: string

*Default*: kubernetes.io/hostname

This key defines which
`label`
is used to determine which topology
`domain`
a node belongs to.

**`spec.topology`**

*Type*: string

*Optional*

*Default*: `SingleCluster`

Defines the topology of the sharded cluster. Cannot be changed for an 
existing deployment. If set to `MultiCluster`:

- All sharded cluster components must have `clusterSpecList` defined:

  - `spec.mongos.clusterSpecList`
  - `spec.configSrv.clusterSpecList`
  - `spec.shard.clusterSpecList`

- The following fields are ignored, as their equivalent values are passed for 
  each cluster in the `spec.<section>.clusterSpecList` objects:

  - `spec.mongodsPerShardCount` is defined in `spec.shard.clusterSpecList.members`
  - `spec.mongosCount` is defined in `spec.mongos.clusterSpecList.members`
  - `spec.configServerCount` is defined in `spec.configSrv.clusterSpecList.members`
  - `spec.shardOverrides.memberConfig` is defined in `spec.shardOverrides.clusterSpecList.memberConfig`
  - `spec.shardOverrides.members` is defined in `spec.shardOverrides.clusterSpecList.members`
  - `spec.shardOverrides.statefulSet` is defined in `spec.shardOverrides.clusterSpecList.statefulSet`

*Example*:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: sc
spec:
  shardCount: 3
  # we don't specify mongodsPerShardCount, mongosCount and configServerCount as they don't make sense for multi-cluster
  topology: MultiCluster
  type: ShardedCluster
  version: 7.0.12
  cloudManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  persistent: true
  shard:
    clusterSpecList:
      - clusterName: member-cluster-0
        members: 2 # each shard will have 2 members in cluster 0, unless overriden
      - clusterName: member-cluster-1
        members: 2
      - clusterName: member-cluster-2
        members: 1

  shardOverrides:
    - shardNames: [sc-2] # this override will apply to the third shard (here, shards are indexed from 0 to 2 as we have 3 shards)
      clusterSpecList:
        - clusterName: member-cluster-0 # all other fields are optional, if not provided the fields from matching member cluster from shard.clusterSpecList will be taken by default
          members: 3
        - clusterName: member-cluster-1 # we don't deploy this shard to member-cluster-1
          # Note that it is also possible to make it explicit with members: 0
        # we don't provide entry for clusterName: member-cluster-1, so it won't be deployed there
        - clusterName: member-cluster-2
          members: 2

  configSrv:
    clusterSpecList:
      - clusterName: member-cluster-0
        members: 2 # config server will have 2 members in this cluster
      - clusterName: member-cluster-1
        members: 1
      - clusterName: member-cluster-2
        members: 2

  mongos:
    clusterSpecList:
      - clusterName: member-cluster-0
        members: 2 # router will have 2 members in this cluster
      - clusterName: member-cluster-1
        members: 1
```

The following fields relate exclusively to deployments in which `topology=MultiCluster`:

**`spec.configSrv.clusterSpecList`**

**Note:**

This field is exclusively available for multi-cluster sharded cluster 
deployments. 

*Type*: array of objects

*Required* if `topology=MultiCluster`

An array of objects for use in multi-cluster sharded cluster deployments 
with the following top-level fields:

`clusterName`
  *Type*: string 

  Name of the cluster where the MongoDB Controllers for Kubernetes Operator schedules the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

`externalAccess`
  *Type*: collection

  Specification to expose your multi-Kubernetes cluster MongoDB deployment for external connections. 
  To learn how to connect to your multi-Kubernetes cluster MongoDB deployment from outside 
  of the Kubernetes cluster, see multi-cluster-connect-from-outside-k8s.

  These settings apply to services across all clusters. 
  To override these global settings in a specific cluster, use 
  spec.clusterSpecList.externalAccess.externalService.

  If you add `spec.externalAccess`, the Kubernetes Operator creates an external service 
  for each Pod in a replica set. External services provide an external entry point 
  for each MongoDB database Pod in a cluster. Each external service has 
  `selectors`
  that match the external service to a specific Pod.

  If you add this setting without any values, the Kubernetes Operator creates 
  an external service with the following default values:

  | Field | Value | Description |
  |---|---|---|
  | `Name` | `<pod-name>-svc-external` | Name of the external service. You can't change this value. |
  | `Type` | `LoadBalancer` | Creates an external `LoadBalancer` service. |
  | `Port` | `<Port Number>` | A port for `mongod`. |
  | `publishNotReadyAddress` | `true` | Specifies that `DNS records` are created even if the Pod isn't ready. Do not set to `false` for any database Pod. |

  **Note:**

  If you set spec.clusterSpecList.externalAccess.externalDomain,
  the external service adds another port (`Port Number + 1`) for backups.

`members`
  *Type*: number

  Number of members in the MongoDB replica set.

**`memberConfig`**

*Type*: collection

Specification for each MongoDB shard and its 
members in your multi-Kubernetes cluster MongoDB deployment.

The order of the elements in the object for shard
must reflect the order of members in the replica set. For example, 
the first element affects the Pod at index `0`, the second 
element affects index `1`, and so on.

**Example:**

Consider the following example specification for a 
multi-Kubernetes cluster MongoDB deployment with three replica sets:

```yaml
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
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod"
          - votes: 1
            priority: "1.5"
            tags:
                  tag2: "value2"
                  environment: "prod"
    - clusterName: cluster2.example.com
      members: 1
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod" 
    - clusterName: cluster3.example.com
      members: 1
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod"
```

`podSpec.persistence`
  *Type*: collection

  Only available in `clusterSpecItem` objects passed to 
  `spec.configSrv.clusterSpecList` and `spec.shard.clusterSpecList`.
  Overrides the existing persistence configuration 
  for a given cluster. 

`statefulSet`
  *Type*: collection

  Provides the configuration for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) override for each of
  the cluster's StatefulSets in a multi-Kubernetes cluster MongoDB deployment. To set the global configuration that
  applies to all clusters in your multi-Kubernetes cluster MongoDB deployment, see spec.statefulSet.spec.

  This setting applies only to replica set resource types in multi-Kubernetes cluster MongoDB deployments.

**`spec.duplicateServiceObjects`**

**Note:**

This field is exclusively available for multi-cluster sharded cluster 
deployments. 

*Type*: boolean

*Optional*

*Default*: `true`

Ignored if topology is not `MultiCluster`. Applies to services for the all 
sharded cluster components: `mongos`, `configSrv` and `shards`.

If set to `true`:
  The Kubernetes Operator creates all `Pod Services` from all
  member clusters in each
  member cluster.

If set to `false`:
  The Kubernetes Operator creates only the `Pod Services` for the
  Pods hosted in each member cluster.

**`spec.mongos.clusterSpecList`**

**Note:**

This field is exclusively available for multi-cluster sharded cluster 
deployments. 

*Type*: array of objects

*Required* if `topology=MultiCluster`

An array of objects for use in multi-cluster sharded cluster deployments 
with the following top-level fields:

`clusterName`
  *Type*: string 

  Name of the cluster where the MongoDB Controllers for Kubernetes Operator schedules the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

`externalAccess`
  *Type*: collection

  Specification to expose your multi-Kubernetes cluster MongoDB deployment for external connections. 
  To learn how to connect to your multi-Kubernetes cluster MongoDB deployment from outside 
  of the Kubernetes cluster, see multi-cluster-connect-from-outside-k8s.

  These settings apply to services across all clusters. 
  To override these global settings in a specific cluster, use 
  spec.clusterSpecList.externalAccess.externalService.

  If you add `spec.externalAccess`, the Kubernetes Operator creates an external service 
  for each Pod in a replica set. External services provide an external entry point 
  for each MongoDB database Pod in a cluster. Each external service has 
  `selectors`
  that match the external service to a specific Pod.

  If you add this setting without any values, the Kubernetes Operator creates 
  an external service with the following default values:

  | Field | Value | Description |
  |---|---|---|
  | `Name` | `<pod-name>-svc-external` | Name of the external service. You can't change this value. |
  | `Type` | `LoadBalancer` | Creates an external `LoadBalancer` service. |
  | `Port` | `<Port Number>` | A port for `mongod`. |
  | `publishNotReadyAddress` | `true` | Specifies that `DNS records` are created even if the Pod isn't ready. Do not set to `false` for any database Pod. |

  **Note:**

  If you set spec.clusterSpecList.externalAccess.externalDomain,
  the external service adds another port (`Port Number + 1`) for backups.

`members`
  *Type*: number

  Number of members in the MongoDB replica set.

**`memberConfig`**

*Type*: collection

Specification for each MongoDB shard and its 
members in your multi-Kubernetes cluster MongoDB deployment.

The order of the elements in the object for shard
must reflect the order of members in the replica set. For example, 
the first element affects the Pod at index `0`, the second 
element affects index `1`, and so on.

**Example:**

Consider the following example specification for a 
multi-Kubernetes cluster MongoDB deployment with three replica sets:

```yaml
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
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod"
          - votes: 1
            priority: "1.5"
            tags:
                  tag2: "value2"
                  environment: "prod"
    - clusterName: cluster2.example.com
      members: 1
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod" 
    - clusterName: cluster3.example.com
      members: 1
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod"
```

`statefulSet`
  *Type*: collection

  Provides the configuration for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) override for each of
  the cluster's StatefulSets in a multi-Kubernetes cluster MongoDB deployment. To set the global configuration that
  applies to all clusters in your multi-Kubernetes cluster MongoDB deployment, see spec.statefulSet.spec.

  This setting applies only to replica set resource types in multi-Kubernetes cluster MongoDB deployments.

**`spec.shard.clusterSpecList`**

**Note:**

This field is exclusively available for multi-cluster sharded cluster 
deployments. 

*Type*: array of objects

*Required* if `topology=MultiCluster`

An array of objects for use in multi-cluster sharded cluster deployments 
with the following top-level fields:

`clusterName`
  *Type*: string 

  Name of the cluster where the MongoDB Controllers for Kubernetes Operator schedules the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

`externalAccess`
  *Type*: collection

  Specification to expose your multi-Kubernetes cluster MongoDB deployment for external connections. 
  To learn how to connect to your multi-Kubernetes cluster MongoDB deployment from outside 
  of the Kubernetes cluster, see multi-cluster-connect-from-outside-k8s.

  These settings apply to services across all clusters. 
  To override these global settings in a specific cluster, use 
  spec.clusterSpecList.externalAccess.externalService.

  If you add `spec.externalAccess`, the Kubernetes Operator creates an external service 
  for each Pod in a replica set. External services provide an external entry point 
  for each MongoDB database Pod in a cluster. Each external service has 
  `selectors`
  that match the external service to a specific Pod.

  If you add this setting without any values, the Kubernetes Operator creates 
  an external service with the following default values:

  | Field | Value | Description |
  |---|---|---|
  | `Name` | `<pod-name>-svc-external` | Name of the external service. You can't change this value. |
  | `Type` | `LoadBalancer` | Creates an external `LoadBalancer` service. |
  | `Port` | `<Port Number>` | A port for `mongod`. |
  | `publishNotReadyAddress` | `true` | Specifies that `DNS records` are created even if the Pod isn't ready. Do not set to `false` for any database Pod. |

  **Note:**

  If you set spec.clusterSpecList.externalAccess.externalDomain,
  the external service adds another port (`Port Number + 1`) for backups.

`members`
  *Type*: number

  Number of members in the MongoDB replica set.

**`memberConfig`**

*Type*: collection

Specification for each MongoDB shard and its 
members in your multi-Kubernetes cluster MongoDB deployment.

The order of the elements in the object for shard
must reflect the order of members in the replica set. For example, 
the first element affects the Pod at index `0`, the second 
element affects index `1`, and so on.

**Example:**

Consider the following example specification for a 
multi-Kubernetes cluster MongoDB deployment with three replica sets:

```yaml
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
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod"
          - votes: 1
            priority: "1.5"
            tags:
                  tag2: "value2"
                  environment: "prod"
    - clusterName: cluster2.example.com
      members: 1
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod" 
    - clusterName: cluster3.example.com
      members: 1
      memberConfig:
          - votes: 1
            priority: "0.5"
            tags:
                tag1: "value1"
                environment: "prod"
```

`podSpec.persistence`
  *Type*: collection

  Only available in `clusterSpecItem` objects passed to 
  `spec.configSrv.clusterSpecList` and `spec.shard.clusterSpecList`.
  Overrides the existing persistence configuration 
  for a given cluster. 

`statefulSet`
  *Type*: collection

  Provides the configuration for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) override for each of
  the cluster's StatefulSets in a multi-Kubernetes cluster MongoDB deployment. To set the global configuration that
  applies to all clusters in your multi-Kubernetes cluster MongoDB deployment, see spec.statefulSet.spec.

  This setting applies only to replica set resource types in multi-Kubernetes cluster MongoDB deployments.

**`spec.shardOverrides`**

*Type*: array of objects

*Optional*

List that contains overrides per shard. Each object contains 
the following fields:

- `shardNames`

  *Required*

  The name of the shard this override applies to.

- `podSpec.Persistence`

  *Optional*

  Defines how the Kubernetes Operator creates and binds persistent volumes to shards. 
  For `topology=MultiCluster` it sets persistence settings for all member 
  clusters. You can define persistence settings for a particular member 
  cluster in `spec.shardOverrides.clusterSpecList.persistence`.

- `additionalMongodConfig`

  *Optional*

  Shard-specific override for `spec.shard.additionalMongodConfig`.

- `agent`

  *Optional*

  Shard-specific override for `spec.shard.agent`. 

- `statefulSet`

  *Optional*

  Shard-specific override for `spec.shardPodSpec.podTemplate` 
  and `spec.shard.clusterSpecList.statefulSet`.

- `members`

  *Optional*

  Only available when `topology=SingleCluster`. Shard-specific override 
  for override for `spec.mongodsPerShardCount`.

- `memberConfig`

  *Optional*

  Only available when `topology=SingleCluster`. Shard-specific override 
  for `spec.shard.memberConfig`.

**`spec.shardPodSpec.persistence.single`**

*Type*: collection

Has Kubernetes Operator create one [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and mount all
three directories for data, journal, and logs to the same [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:**

- You must set the values in this collection if
  `spec.persistent` `: true`.
- You may set this collection or the `persistence.multiple`
  collections but not both.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum size of [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that should be mounted. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 16Gi. For example, if each sharded cluster shard member in requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage specified in a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims). You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |
