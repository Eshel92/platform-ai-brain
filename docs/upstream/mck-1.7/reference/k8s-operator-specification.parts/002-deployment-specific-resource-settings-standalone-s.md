<!-- Part 2 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

### Standalone Settings

**Note:**

All of the standalone-settings also apply to replica set
resources.

**`spec.additionalMongodConfig`**

*Type*: collection

Additional `configuration options` with
which you want to start MongoDB processes.

The Kubernetes Operator supports all configuration options that the MongoDB
version you deploy through the MongoDB Agent supports, except that the 
Kubernetes Operator overrides values that you provide for any of the 
following options:

- `net.port`
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

**`spec.agent`**

*Type*: collection

MongoDB Agent configuration settings for MongoDB database resource.

**`spec.agent.startupOptions`**

*Type*: collection

MongoDB Agent settings with which you want to start MongoDB database resource.

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
  name: my-standalone
spec:
  version: "8.0.0"
  service: my-service

  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  type: Standalone

  persistent: true
  agent:
    startupOptions:
      maxLogFiles: "30"
      dialTimeoutSeconds: "40"
...
```

**`spec.podSpec`**

*Type*: object

Object that contains the specifications for the MongoDB [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) Pods.

**`spec.externalAccess`**

*Type*: collection

Specification to expose your cluster for external connections. 
To learn how to connect to your MongoDB resource from outside of the Kubernetes cluster, see
connect-from-outside-k8s.

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

If you set `spec.externalAccess.externalDomain`,
the external service adds another port (`Port Number + 1`) for backups.

**`spec.externalAccess.externalService`**

*Type*: collection

Specification for overriding the default values in `spec.externalAccess`.

When you set the `spec.externalAccess` setting, the Kubernetes Operator 
automatically creates an external load balancer service with default values. 
You can override certain values or add new values depending on your needs. 
For example, if you intend to create `NodePort services`
and don't need a load balancer, you must configure overrides in your
Kubernetes specification:

```yaml
externalAccess:
  externalService: 
    annotations:
      # cloud-specific annotations for the service
    spec:
      type: NodePort # default is LoadBalancer
      # you can specify other spec overrides if necessary
```

For more information about the Kubernetes specification, see `ServiceSpec` 
in the Kubernetes documentation.

**`spec.externalAccess.externalService.annotations`**

*Type*: collection

Key-value pairs that let you add cloud provider-specific
configuration settings to all clusters in your deployment. 
To learn more, see 
[annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) and the documentation for your Kubernetes cloud provider.

You can use [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to specify 
placeholder values for external services used by
Kubernetes Operator deployments. The Kubernetes Operator automatically 
replaces these values with the correct values as described in 
the following table. Using placeholders allows you to provide specific 
annotations in each service for a specific Pod.

| Value | Description |
|---|---|
| `{resourceName}` | Equal to `metadata.name`. |
| `{namespace}` | Equal to `metadata.namespace`. |
| `{podIndex}` | Index of the Pod assigned by the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) and targeted by the current external service. |
| `{podName}` | Equal to `{resourceName}-{podIndex}`. |
| `{statefulSetName}` | The [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). Equal to `{resourceName}`. |
| `{externalServiceName}` | Generated name of the external service, based on the placeholder values that you specified. Equal to `{resourceName}-{podIndex}-svc-external`. |
| `{mongodProcessDomain}` | The domain name of the server that is hosting the mongod process. Equal to `spec.externalAccess.externalDomain` if specified. Otherwise, equal to the domain used for the `mongod` process FQDN (fully qualified domain name). For example, for the process hostname `mdb-rs-1.example.com`, `example.com` is the domain name. |
| `{mongodProcessFQDN}` | The `mongod` process hostname set in the `automation configuration`. The process hostname depends on your deployment configuration. If you've configured your deployment to use `external domains`, the process hostname uses the following format: `{resourceName}-{podIndex}.{mongodProcessDomain}` For example: `mdb-rs-1.example.com` If your deployment doesn't use external domains, the process hostname uses the following format: `{resourceName}-{podIndex}.{resourceName}-{podIndex}-svc.{namespace}.svc.cluster.local` For example: `mdb-rs-1.mdb-rs-1-svc.ns.svc.cluster.local` |

**Note:**

You must use only known placeholder values as specified in the table 
and ensure that your placeholders don't use empty or null values. 
You also can't use a placeholder 
specific to multi-Kubernetes-cluster deployments
for a single MongoDB resource deployment. 

Otherwise, Kubernetes Operator returns an error. For example, you might
encounter the following error message:

```
error replacing placeholders in map with key=external-dns.alpha.kubernetes.io/hostname, value={resourceName}-{podIndex}-{unknownPlaceholder}.{clusterName}-{clusterIndex}.example.com: missing values for the following placeholders: {clusterName}, {clusterIndex}, {unknownPlaceholder}``
```

**Example:**

The following example specifies the `{resourceName}`,
`{podIndex}`, and `{namespace}` placeholders:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: mdb-rs
  namespace: ns
spec:
  replicas: 3
  externalAccess:
    externalService:
      annotations:
        external-dns.alpha.kubernetes.io/hostname: {resourceName}-{podIndex}-{namespace}.example.com
```

The Kubernetes Operator automatically populates the annotations 
for the external services based on the proper value for each placeholder. 
For example:

```yaml
mdb-rs-0-svc-external:
  annotations:
    external-dns.alpha.kubernetes.io/hostname: mdb-rs-0-ns.example.com
mdb-rs-1-svc-external:
  annotations:
    external-dns.alpha.kubernetes.io/hostname: mdb-rs-1-ns.example.com
mdb-rs-2-svc-external:
  annotations:
    external-dns.alpha.kubernetes.io/hostname: mdb-rs-2-ns.example.com
```

**`spec.externalAccess.externalService.spec`**

*Type*: collection

Configuration for the `ServiceSpec`.
To learn more, see `spec.externalAccess.externalService`.
      

**`spec.podSpec.persistence.single`**

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
| `storage` | string | Minimum size of [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that should be mounted. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 16Gi. For example, if standalone deployment in requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage specified in a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims). You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.podSpec.persistence.multiple.data`**

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
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host standalone deployment on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 16Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for standalone deployment. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.podSpec.persistence.multiple.journal`**

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
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host standalone deployment on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 1Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for standalone deployment. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.podSpec.persistence.multiple.logs`**

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
| `storage` | string | Minimum storage capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to host standalone deployment on Kubernetes. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 3Gi. For example, if this `MongoDB` resource requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage needed for standalone deployment. You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.podSpec.podTemplate`**

*Type*: collection

`Template`
for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for MongoDB database resources.

Template values take precedence over values specified in `spec.podSpec`.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.podSpec.podTemplate`.

**`spec.podSpec.podTemplate.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
MongoDB database resources.

To review which fields you can add to `spec.podSpec.podTemplate.metadata`, see
the `Kubernetes documentation`.

**`spec.podSpec.podTemplate.spec`**

*Type*: collection

Specifications of the Kubernetes Pods that the MongoDB Controllers for Kubernetes Operator creates for
MongoDB database resources.

To review which fields you can add to `spec.podSpec.podTemplate.spec`, see the
`Kubernetes PodSpec v1 core API`.

**Note:**

When you add containers to `spec.podSpec.podTemplate.spec.containers`, the
Kubernetes Operator adds them to the Kubernetes pod. These containers are
appended to MongoDB database resources containers in the pod.

Use this setting to specify the CPU and RAM allocations for each pod. For
examples, see the samples on GitHub.

**`spec.podSpec.podTemplate.spec.affinity.nodeAffinity`**

*Type*: Struct

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to place [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) for replica set on a
specific range of [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

For optimized read-write performance, use node affinity rules that 
restrict [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), or to prefer 
to run on particular [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).

**`spec.podSpec.podTemplate.spec.affinity.podAffinity`**

*Type*: Struct

Kubernetes [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to determine whether multiple `MongoDB` resource [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
must be co-located with other [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/). To learn more about the use cases,
see [Affinity and Anti-Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) in the Kubernetes documentation.

**`spec.podSpec.podTemplate.spec.affinity.podAntiAffinity`**

*Type*: Struct

*Default*: kubernetes.io/hostname

Sets a [rule](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) to spread [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) hosting `MongoDB` resource
to different locations. A location can be a single node, rack, or
region. By default, Kubernetes Operator tries to spread pods across
different nodes.

**`spec.podSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`**

*Type*: Struct

*Default*: kubernetes.io/hostname

This key defines which
`label`
is used to determine which topology
`domain`
a node belongs to.
