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

## Common Resource Settings

Every resource type must use the following settings:

### Required

**`apiVersion`**

*Type*: string

Version of the `MongoDB` resource schema.

**`kind`**

*Type*: string

Kind of `MongoDB` resource to create. Set this to `MongoDB`

**`metadata.name`**

*Type*: string

Name of the `MongoDB` resource that you create.

Resource names must be 44 characters or less.

**`spec.credentials`**

*Type*: string

*Required.* Name of the Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) you created as `Ops Manager` API (Application Programming Interface) authentication credentials for
the Kubernetes Operator to communicate with Cloud Manager or Ops Manager.

The `Ops Manager` Kubernetes Secret object
holding the Credentials must exist on the **same** Namespace as
the resource you want to create.

**Important:** Operator manages changes to the Secret

The Kubernetes Operator tracks any changes to the Secret and
reconciles the state of the `MongoDB` resource.

**`spec.persistent`**

*Type*: boolean

*Default*: True

WARNING: Grant your containers permission to write to your [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).
The Kubernetes Operator sets `fsGroup = 2000`, `runAsUser = 2000`, 
and `runAsNonRoot = true` in `securityContext`. Kubernetes Operator 
sets `fsgroup` equal to `runAsUser` to make the volume writable 
for a user that runs the main process in the container. To learn 
more, see `Configure a 
Security Context for a Pod or Container` and the related 
`discussion` in 
the Kubernetes documentation. If redeploying the resource doesn't fix
issues with your Persistent Volume, contact [MongoDB Support](https://support.mongodb.com/welcome).

If you do not use [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), the Disk Usage and
Disk IOPS charts cannot be displayed in either the
Processes tab on the Deployment page or in
the Metrics page when
`reviewing the data` for this
deployment.

**`spec.type`**

*Type*: string

Type of `MongoDB` resource to create. Accepted values are:

- `Standalone`
- `ReplicaSet`
- `ShardedCluster`

**`spec.version`**

*Type*: string

Version of MongoDB that you installed on this `MongoDB` resource.

The format should be `X.Y.Z` for the Community edition and
`X.Y.Z-ent` for the Enterprise edition. 

**Important:**

Ensure that you choose a compatible MongoDB Server version.

Compatible versions differ depending on the base image that the
MongoDB database resource uses.

**Note:**

If you update this value to a later version of MongoDB for your 
database resources, the feature compatibility version remains 
at the MongoDB version you're upgrading from to give you the option to downgrade if necessary.
If you want the feature compatibility version to match the new MongoDB version, you must manually set 
`spec.featureCompatibilityVersion` to the new version or to `AlwaysMatchVersion`.
To learn more, see `spec.featureCompatibilityVersion`.

### Conditional

Every resource must use *one* of the following settings:

**`spec.opsManager.configMapRef.name`**

*Type*: string

Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Cloud Manager or Ops Manager connection
configuration. The `spec.cloudManager.configMapRef.name`
setting is an alias for this setting and can be used in its place.

This value must exist on the *same* namespace as the resource
you want to create.

**Important:** Operator manages changes to the ConfigMap

The Kubernetes Operator tracks any changes to the ConfigMap and
reconciles the state of the `MongoDB` resource.

**`spec.cloudManager.configMapRef.name`**

*Type*: string

Alias for `spec.opsManager.configMapRef.name`.

### Optional

Every resource type may use the following settings:

**`metadata.annotations.mongodb.com/v1.architecture`**

*Type*: string

Determines the container architecture used by a specific deployment:

- The default non-static containers that download the MongoDB binary at runtime, or
-  static-containers that are immutable at runtime.

Accepted values are:

- `static`
- `non-static`

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-project
  annotations:
    mongodb.com/v1.architecture: "static"
```

**`spec.agent.backupAgent.logRotate`**

*Type*: object

Thresholds after which the MongoDB Agent rotates the backup log.

**`spec.agent.backupAgent.logRotate.sizeThresholdMB`**

*Type*: integer

Maximum size, in MB, of a backup log file before the MongoDB Agent rotates the logs.

**`spec.agent.backupAgent.logRotate.timeThresholdHrs`**

*Type*: integer

Number of hours after which the MongoDB Agent rotates the backup log file.

**`spec.agent.mongod.auditlogRotate`**

*Type*: object 

Object that contains the audit log rotation configuration for the MongoDB processes.

**`spec.agent.mongod.auditlogRotate.sizeThresholdMB`**

*Type*: number

Maximum size, in MB, of an audit log file before the MongoDB Agent rotates the logs.

**`spec.agent.mongod.auditlogRotate.timeThresholdHrs`**

*Type*: integer

Number of hours after which the MongoDB Agent rotates the audit log file.

**`spec.agent.mongod.auditlogRotate.numUncompressed`**

*Type*: integer

Maximum number of total audit log files to leave uncompressed, including the 
current log file.

**`spec.agent.mongod.auditlogRotate.numTotal`**

*Type*: integer

Total number of audit log files that Ops Manager retains. If you don't set this 
value, the total number of audit log files defaults to **0**.

**`spec.agent.mongod.auditlogRotate.percentOfDiskspace`**

*Type*: number

Maximum percentage of total disk space that Ops Manager can use to store the log 
files expressed as decimal. If this limit is exceeded, Ops Manager deletes compressed 
log files until it meets this limit. Ops Manager deletes the oldest log files first.

The default is **0.02**.

**`spec.agent.mongod.logRotate`**

*Type*: object

Thresholds after which Ops Manager rotates the MongoDB logs of a process.

**`spec.agent.mongod.logRotate.sizeThresholdMB`**

*Type*: integer

Maximum size in MB for an individual log file before Ops Manager rotates it. 
Ops Manager rotates the log file immediately if it meets the value given in either 
this `sizeThresholdMB` or the `spec.agent.mongod.logRotate.timeThresholdHrs`.

**`spec.agent.mongod.logRotate.timeThresholdHrs`**

*Type*: integer

Maximum duration in hours for an individual log file before the next rotation. The time is since the last rotation.

Ops Manager rotates the log file once the file meets either this `timeThresholdHrs` 
or the `spec.agent.mongod.logRotate.sizeThresholdMB`.

**`spec.agent.monitoringAgent.logRotate`**

*Type*: object

Thresholds after which the MongoDB Agent rotates the monitoring log.

**`spec.agent.monitoringAgent.logRotate.sizeThresholdMB`**

*Type*: integer

Maximum size in MB for an individual log file before the MongoDB Agent rotates 
the monitoring log.

**`spec.agent.monitoringAgent.logRotate.timeThresholdHrs`**

*Type*: integer

Number of hours after which the MongoDB Agent rotates the monitoring log.

**`spec.agent.readinessProbe.environmentVariables`**

*Type*: object

Configures the following environment variables used to control the log files for 
the Readiness Probe:

* readiness-probe-logger-backups
* readiness-probe-logger-compress
* readiness-probe-logger-max-size
* readiness-probe-logger-max-age
* mdb-agent-file-logging
* log-file-path

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-project 
spec:
  agent:
    readinessProbe:
      environmentVariables:
        READINESS_PROBE_LOGGER_BACKUPS: 1
        READINESS_PROBE_LOGGER_MAX_SIZE: 10
        READINESS_PROBE_LOGGER_MAX_AGE: 3
        READINESS_PROBE_LOGGER_COMPRESS: true
        MDB_WITH_AGENT_FILE_LOGGING: false
        LOG_FILE_PATH: /var/log/mongodb-mms-automation/readiness.log
```

**`spec.featureCompatibilityVersion`**

*Type*: string

*Defaults to the prior major MongoDB version after MongoDB upgrade.*

Limits changes to data that occur with an upgrade to a
new major version. For example, if you upgrade from MongoDB 5.0 to MongoDB 6.0, 
the feature compatibility version remains 
at 5.0 to give you the option to downgrade if necessary.

If you want the feature compatibility version to match the new MongoDB version, you must manually set `featureCompatibilityVersion`
to the new version. 
For example, `featureCompatibilityVersion: 6.0`.

Alternatively, you can enable the `AlwaysMatchVersion` option to automatically 
update the feature compatibility version to match the MongoDB version during upgrades. 
For example, `featureCompatibilityVersion: AlwaysMatchVersion`.

To learn more about feature compatibility, see
`setFeatureCompatibilityVersion` in the MongoDB Manual.

**`spec.clusterDomain`**

*Type*: string

*Default*: cluster.local

Domain name of the Kubernetes cluster where you deploy the Kubernetes Operator. When
Kubernetes creates a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), the Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) a
FQDN (fully qualified domain name). To update Cloud Manager or Ops Manager, the Kubernetes Operator calculates the FQDN (fully qualified domain name) for
each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) using a provided cluster name. Kubernetes doesn't provide
an API (Application Programming Interface) to query these hostnames.

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**`spec.clusterName`**

*Type*: string

*Default*: cluster.local

**Important:** `spec.clusterName` is Deprecated

Use `spec.clusterDomain` instead.

Domain name of the Kubernetes cluster where you deploy the Kubernetes Operator.
When Kubernetes creates a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), the Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
a FQDN (fully qualified domain name). To update Cloud Manager or Ops Manager, the Kubernetes Operator calculates the FQDN (fully qualified domain name) for
each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) using a provided cluster name. Kubernetes doesn't provide
an API (Application Programming Interface) to query these hostnames.

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**`metadata.namespace`**

*Type*: string

Kubernetes [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) where you create this `MongoDB` resource and other
[objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

**`spec.service`**

*Type*: string

*Default*: <resource_name>+"-svc" and <resource_name>+"-svc-external"

**Important:** `spec.service` is Deprecated

Use `spec.statefulSet.spec.serviceName` instead.

Name of the Kubernetes service to be created or used for a
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). If the service with this name already exists, the
MongoDB Controllers for Kubernetes Operator does not delete or recreate it. This setting lets
you create your own custom services and lets the Kubernetes Operator
reuse them.

**`spec.logLevel`**

*Type*: string

*Default*: INFO

Configures the level of Automation Agent logging inside the
[Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/). Accepted values include:

- `DEBUG`
- `INFO`
- `WARN`
- `ERROR`
- `FATAL`

**`spec.security.authentication.ignoreUnknownUsers`**

*Type*: boolean

*Default*: `false`

Determines whether you can modify database users that were not
configured through the Kubernetes Operator, or the Cloud Manager or Ops Manager user interface.

To manage database users directly through the `mongod` or `mongos`, set
this setting to `true`.

## Deployment-Specific Resource Settings

Other settings you can and must use in a `MongoDB` resource specification
depend upon which MongoDB deployment item you want to create:

- standalone-settings

- replica-set-settings

- sharded-cluster-settings

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

### Replica Set Settings

**Note:**

All of the standalone-settings also apply to replica set
resources.

The following settings apply to replica set resource types:

**`spec.backup`**

*Type*: collection

The collection container for `spec.backup.mode`,
which enables continuous backups for MongoDB resources in Kubernetes Operator.

**`spec.backup.assignmentLabels`**

*Type*: array

A comma-separated list of labels to assign backup daemons, oplog stores,
blockstores, S3 (Simple Storage Service) snapshot stores, and file system stores to specific
projects or groups. Use assignment labels to identify that specific
backup stores are associated with particular projects.

If you set assignment labels using the Kubernetes Operator, the values that
you set in the Kubernetes configuration file for assignment labels override
the values defined in the `Ops Manager` UI. Assignment labels that you don't set
using the Kubernetes Operator continue to use the values set in the `Ops Manager` UI.

**Note:**

If you set this parameter, the API key linked with the value of 
`spec.credentials` must have a `Global Owner` role.

**`spec.backup.mode`**

*Type*: string

Enables continuous backups for a MongoDB resource.
Possible values are `enabled`, `disabled`, and
`terminated`.

**Note:**

The `spec.backup.mode`
setting relies on Backup that is
enabled in the Ops Manager and requires that
`spec.backup.enabled`
value in the Ops Manager resource specification is set to `true`.

After you enable continuous backups for your MongoDB resource with
`spec.backup.mode`, you can check the backup status.

**`spec.backup.encryption`**

*Type*: object

Object that contains the backup encryption configuration settings.

**`spec.backup.encryption.kmip`**

*Type*: object

Object that contains the KMIP (Key Management Interoperability Protocol) backup encryption configuration 
settings. To learn more, see configure-kmip-backup-encryption.

**`spec.backup.encryption.kmip.client`**

*Type*: object

Object that contains the KMIP (Key Management Interoperability Protocol) backup encryption client 
configuration settings.

**`spec.backup.encryption.kmip.client.clientCertificatePrefix`**

*Type*: string

**`spec.backup.snapshotSchedule`**

*Type*: collection

Collection container for snapshot schedule settings for
continuous backups for MongoDB resources in Kubernetes Operator.

**`spec.backup.snapshotSchedule.snapshotIntervalHours`**

*Type*: number

Number of hours between snapshots. You can set a value of `6`,
`8`, `12`, or `24`.

**`spec.backup.snapshotSchedule.snapshotRetentionDays`**

*Type*: number

Number of days to keep recent snapshots. You can set a value 
between `2` and `5`, inclusive.

**`spec.backup.snapshotSchedule.dailySnapshotRetentionDays`**

*Type*: number

Number of days to keep daily snapshots. You can set a value 
between `1` and `365`, inclusive. Setting the value to `0`
disables this rule.

**`spec.backup.snapshotSchedule.weeklySnapshotRetentionWeeks`**

*Type*: number

Number of weeks to keep weekly snapshots. You can set a value 
between `1` and `52`, inclusive. Setting the value to `0`
disables this rule.

**`spec.backup.snapshotSchedule.monthlySnapshotRetentionMonths`**

*Type*: number

Number of months to keep monthly snapshots. You can set a value 
between `1` and `36`, inclusive. Setting the value to `0`
disables this rule.

**`spec.backup.snapshotSchedule.pointInTimeWindowHours`**

*Type*: number

Number of hours in the past for which you can create a point-in-time
snapshot.

**`spec.backup.snapshotSchedule.referenceHourOfDay`**

*Type*: number

UTC (Coordinated Universal Time) hour of the day to schedule snapshots using a 24 hour clock.
You can set a value between `0` and `23`, inclusive.

**`spec.backup.snapshotSchedule.referenceMinuteOfHour`**

*Type*: number

UTC (Coordinated Universal Time) minute of the hour to schedule snapshots. You can
set a value between `0` and `59`, inclusive.

**`spec.backup.snapshotSchedule.fullIncrementalDayOfWeek`**

*Type*: string

Day of the week when Ops Manager takes a full snapshot. This setting
ensures a recent complete backup. Ops Manager sets the default value to
`SUNDAY`.

**`spec.clusterName`**

*Type*: string

*Default*: cluster.local

**Important:** `spec.clusterName` is Deprecated

Use `spec.clusterDomain` instead.

Domain name of the Kubernetes cluster where you deploy the Kubernetes Operator.
When Kubernetes creates a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), the Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
a FQDN (fully qualified domain name). To update Cloud Manager or Ops Manager, the Kubernetes Operator calculates the FQDN (fully qualified domain name) for
each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) using a provided cluster name. Kubernetes doesn't provide
an API (Application Programming Interface) to query these hostnames.

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**`spec.connectivity.replicaSetHorizons`**

*Type*: collection

Allows you to provide different DNS (Domain Name System) settings for client
applications and the MongoDB Agents. The Kubernetes Operator uses split
horizon DNS (Domain Name System) for replica set members. This feature allows
communication both within the Kubernetes cluster and from outside Kubernetes.

You may add multiple external mappings per host.

Split Horizon Requirements:

- Make sure that each value in this array is unique.

- Make sure that the number of entries in this array matches the
  value given in `spec.members`.

- Provide a value for the
  `spec.security.certsSecretPrefix` setting to
  enable TLS (Transport Layer Security). This method to use split horizons requires the
  Server Name Indication extension of the TLS (Transport Layer Security) protocol.

- Configure the routing for external hostnames.

**Example:**

Replica-set members communicate with one another using the hostnames 
configured in the replication configuration (`members[n].host`). 
The `example-website` horizon provides alternate addresses for clients 
connecting through that horizon.

The names of the stated horizons are arbitrary for the purposes of this 
example. You can name your horizon anything, but make sure the horizon
name is the same for all hostnames that are a part of that horizon.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  type: ReplicaSet
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  persistent: true
```

```yaml
  security:
    tls:
      enabled: true
  connectivity:
    replicaSetHorizons:
      - "example-website": "web1.example.com:30907"
      - "example-website": "web2.example.com:32350"
      - "example-website": "web3.example.com:31185"
...
```

**`spec.externalAccess.externalDomain`**

*Type*: string

An external domain used to externally expose your replica set deployment.

By default, each replica set member uses the Kubernetes Pod's FQDN (fully qualified domain name) 
(`*.svc.cluster.local`) as the default hostname. However, if you add an
external domain to this setting, the replica set uses a hostname that is a 
subdomain of the specified domain instead. This hostname uses the following 
format:

`<replica-set-name>-<pod-idx>.<externalDomain>`

For example:

`replica-set-1.example.com`

After you deploy the replica set with this setting, the
Kubernetes Operator uses the hostname with the external domain to override 
the `processes[n].hostname` field in the Ops Manager `automation configuration`. Then, the MongoDB Agent uses this hostname to 
connect to `mongod`.

To specify other hostnames for connecting to the replica set, you can use the 
`spec.connectivity.replicaSetHorizons` setting. However, the following 
connections still use the hostname with the external domain:

- The MongoDB Agent to connect to `mongod`.
- `mongod` to connect to other `mongod` instances.

WARNING: Specifying this field changes how Ops Manager registers `mongod` processes.
You can't change the value of this field or any `processes[n].hostname` fields 
in the Ops Manager `automation configuration` for a running
replica set deployment.

**`spec.members`**

*Type*: integer

*Required*. Number of Members of the Replica Set.

**`spec.memberConfig`**

*Type*: collection

Specification for each MongoDB replica set member deployed from 
the `MongoDB` resource.

The order of the elements in the array must reflect the order of members 
in the replica set. For example, the first element of the array affects 
the Pod at index `0`, the second element affects index `1`, and so on.

**Example:**

Consider the following example specification for a 
three-member replica set:

```yaml
spec:
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
    - votes: 0
      priority: "0.5"
      tags:
        tag2: "value2"
        environment: "prod"
```

**`spec.memberConfig.priority`**

*Type*: string

Number that indicates the relative likelihood of a MongoDB replica set member to become the [primary](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-primary).

* To increase the relative likelihood that a replica set member becomes the primary, specify a higher `priority` value.

* To decrease the relative likelihood that a replica set member becomes the primary, specify a lower `priority` value.

For example, a member with a `memberConfig.priority` of `1.5` is more likely than a member with a `memberConfig.priority` of `0.5` to become the primary. 

A member with a `memberConfig.priority` of `0` is ineligible to become the primary. To learn more, see Member Priority.

**`spec.memberConfig.tags`**

*Type*: map

Map of replica set tags for directing
read and write operations to specific members of your MongoDB replica set.

**`spec.memberConfig.votes`**

*Type*: number

Determines whether a MongoDB replica set member can vote in an election. Set to `1` to allow the member to vote. Set to `0` to exclude the member from an election.

The following settings apply only to replica set resource types:

**`spec.backup.autoTerminateOnDeletion`**

*Type*: boolean

Flag that controls whether the Kubernetes Operator stops and terminates the
backup when you delete a MongoDB resource. If omitted, the default value is `false`.
Setting this flag to `true` is useful when you want to delete the
MongoDB custom resource while the `spec.backup.mode` setting
is set to `enabled`.

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

## Prometheus Settings

You can use Prometheus with your replica sets or sharded clusters.
Prometheus monitoring is not supported for standalone resources. To
monitor a single-node deployment with Prometheus, deploy a
single-member replica set instead. To learn more, see
deploy-prometheus. To view an example, see
mdb-resource-prometheus.

The following settings apply when you use Prometheus 
with your MongoDB resource:

**`spec.prometheus`**

*Type*: array

*Optional*

List that contains the parameters for exposing metrics to Prometheus.

**`spec.prometheus.metricsPath`**

*Type*: string

*Optional*

*Default*: `"/metrics"`

Human-readable string that indicates the path to the metrics 
endpoint. If you don't specify this setting, the default applies.

**`spec.prometheus.passwordSecretRef`**

*Type*: object

*Conditional*

Object that contains the details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for 
basic HTTP authentication. If you want to use Prometheus with your 
MongoDB resource, you must specify this setting.

**`spec.prometheus.passwordSecretRef.key`**

*Type*: string

*Optional*

*Default*: `"password"`

Human-readable string that indentifies the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) 
that stores the password for basic HTTP authentication. If you don't 
specify this setting, the default applies.

**`spec.prometheus.passwordSecretRef.name`**

*Type*: string

*Conditional*

Human-readable label that identifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains 
the password for basic HTTP authentication. If you want to use 
Prometheus with your MongoDB resource, you must specify this setting.

**`spec.prometheus.port`**

*Type*: integer

*Optional*

*Default:* 9216

Number that identifies the port that the metrics endpoint will 
bind to. If you don't specify this setting, the default applies.

**`spec.prometheus.tlseSecretKeyRef`**

*Type*: object

*Optional*

Object that contains the details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for TLS (Transport Layer Security) 
authentication.

**`spec.prometheus.tlseSecretKeyRef.key`**

*Type*: string

*Optional*

*Default*: `"password"`

Human-readable string that indentifies the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) 
that stores the password for TLS (Transport Layer Security) authentication. If you don't 
specify this setting, the default applies.

**`spec.prometheus.tlseSecretKeyRef.name`**

*Type*: string

*Conditional*

Human-readable label that identifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains 
the password for TLS (Transport Layer Security) authentication. If you want to use 
Prometheus with your MongoDB resource and you want to use TLS (Transport Layer Security) 
authentication, you must specify this setting.

**`spec.prometheus.username`**

*Type*: string

*Conditional*

Human-readable label that identifies the user for basic HTTP 
authentication. If you want to use Prometheus with your MongoDB 
resource, you must specify this setting.

## Security Settings

The following security settings apply only to replica set and sharded
cluster resource types:

**`spec.security.tls.ca`**

*Type*: string

Provide the name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that stores the CA (Certificate Authority) for the `MongoDB` resource.

**Important:**

If you use a custom CA (Certificate Authority) to sign your TLS (Transport Layer Security) certificates for the `MongoDB` resource,
you must specify this parameter.

The Kubernetes Operator requires that you name the
`MongoDB` resource certificate `ca-pem` in the ConfigMap.

**`spec.security.certsSecretPrefix`**

*Type*: string

Text to prefix to the Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that you
created that contain your replica set's or sharded cluster's TLS (Transport Layer Security) 
keys and certificates.

You must prefix your secrets with `<prefix>-<metadata.name>`.

For example, if you call your deployment `my-deployment` and you set
the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the
client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, 
you must name the TLS (Transport Layer Security) secret for internal cluster authentication 
(if enabled) `mdb-my-deployment-clusterfile`.

To learn more about naming the secrets that contain your TLS (Transport Layer Security) 
certificates, see the topic in secure-tls that applies to your 
deployment.

**`spec.security.tls.additionalCertificateDomains`**

*Type*: boolean

List of every domain that should be added to TLS (Transport Layer Security) certificates to
each pod in this deployment. When you set this parameter, every CSR (Certificate Signing Request)
that the Kubernetes Operator transforms into a TLS (Transport Layer Security) certificate includes
a SAN (Subject Alternative Name) in the form `<pod name>.<additional cert domain>`.

Replica set resources don't need this parameter. Use
`spec.connectivity.replicaSetHorizons` instead.

**Note:**

If you add this parameter to a TLS (Transport Layer Security)\-enabled resource, Kubernetes
displays an error when the resource reaches the `Pending` state.
This error displays: ``Please manually remove the CSR (Certificate Signing Request) in order
to proceed.`` To remedy this issue:

1. Remove any existing CSR (Certificate Signing Request)\s so that Kubernetes can generate new
   CSR (Certificate Signing Request)\s. To learn how to delete a resource, see the
   `deleting resources` in the
   Kubernetes documentation.

2. Approve the CSR (Certificate Signing Request)\s after Kubernetes generates them.

**`spec.additionalMongodConfig.net.ssl.mode`**

*Type*: string

*Default*: `requireSSL`

Specifies which `sslMode` is used for network connections.
The following are valid options:

| Value | Description |
|---|---|
| `allowSSL` | Connections between servers do not use TLS (Transport Layer Security). For incoming connections, the server accepts both TLS (Transport Layer Security) and non-TLS. |
| `preferSSL` | Connections between servers use TLS (Transport Layer Security). For incoming connections, the server accepts both TLS (Transport Layer Security) and non-TLS. |
| `requireSSL` | The server uses and accepts only TLS (Transport Layer Security) encrypted connections. |

**`spec.additionalMongodConfig.net.tls.disabledProtocols`**

*Type*: string

*New in MongoDB version 4.2.*

Prevents a MongoDB server running with TLS (Transport Layer Security) from accepting incoming connections 
that use a specific protocol or protocols. To specify multiple protocols, enter 
a comma separated list of protocols. For example, `TLS1_0,TLS1_1`.

This setting recognizes the following protocols: `TLS1_0`, `TLS1_1`, `TLS1_2`, 
and starting in MongoDB 4.0.4 (and 3.6.9), `TLS1_3`. If you specify an unrecognized protocol, the 
server won't start.

On macOS, you can't disable `TLS1_1` and enable both `TLS1_0` and `TLS1_2`. 
You must disable at least `TLS1_0` or `TLS1_2` also. For example, `TLS1_0,TLS1_1` 
disables `TLS1_2` on macOS. 

The list of protocols that you disable replaces the default list of disabled protocols.

Starting in MongoDB version 4.0, MongoDB disables the use of TLS (Transport Layer Security) 1.0 if TLS (Transport Layer Security) 1.1+ 
is available on the system. To enable the disabled TLS (Transport Layer Security) 1.0, specify `none` as the value for  
`spec.additionalMongodConfig.net.tls.disabledProtocols`. 

Members of replica sets and sharded clusters must speak at least one protocol in common.

**`spec.security.authentication`**

*Type*: collection

Authentication specifications for your MongoDB deployment.

**`spec.security.authentication.enabled`**

*Type*: boolean

*Default*: `false`

Specifies whether authentication is enabled on the Cloud Manager or Ops Manager
project. If set to `true`, you must set an authentication mechanism in 
`spec.security.authentication.modes`.

**Important:**

The Kubernetes Operator manages authentication for this MongoDB
resource if you include this setting, even if it's set to
`false`. You can't configure authentication for this
resource using the Cloud Manager or Ops Manager UI  or APIs while this setting
exists in the resource specification.

Omit this setting if you want to manage authentication using the
Cloud Manager or Ops Manager UI or APIs.

**`spec.security.authentication.modes`**

*Type*: array

Specifies the authentication mechanism that your MongoDB deployment 
uses. Valid values are `SCRAM`, `SCRAM-SHA-1`, `MONGODB-CR`, 
`X509`, `LDAP`, and `OIDC`. We recommend `SCRAM-SHA-256` (`SCRAM`) 
over `SCRAM-SHA-1`. If you specify `SCRAM-SHA-1`, you must also 
specify `MONGODB-CR`.

**Note:** X.509 Internal Cluster Authentication

To enable X.509 internal cluster authentication for the Cloud Manager or Ops Manager project, set this
value to `["X509"]` and specify the following settings:

- `spec.security.authentication.internalCluster` `: "X509"`
- provide a value for the
  `spec.security.certsSecretPrefix` setting.`

If you provide more than one value for
`spec.security.authentication.modes`, you must also specify a
value for `spec.security.authentication.agents.mode`.

**`spec.security.authentication.internalCluster`**

*Type*: string

Specifies whether X.509 internal cluster authentication is enabled.

To enable X.509 internal cluster authentication, set to `"X509"`.
Requires that the following settings be specified:

- `spec.security.authentication.modes` `: ["X509"]`
- `spec.security.certsSecretPrefix`

The Kubernetes Operator accepts the following values:

- `["X509"]`: X.509 internal cluster authentication is enabled.
- `""` or omitted: internal cluster authentication is not enabled.

**Important:**

After you enable internal cluster authentication, you can't disable
it.

**`spec.security.authentication.requireClientTLSAuthentication`**

*Type*: boolean

*Default*: `false`

Specifies whether the MongoDB host requires clients to connect using a
TLS (Transport Layer Security) certificate. Defaults to `true` if you enable TLS (Transport Layer Security)
authentication.

To enable TLS (Transport Layer Security) authentication, provide a value for the `spec.security.certsSecretPrefix` setting.

**`spec.security.authentication.ldap`**

*Type*: collection

*Required for LDAP authentication.* 

Configures LDAP (Lightweight Directory Access Protocol) authentication for the Cloud Manager or Ops Manager project. To enable
LDAP (Lightweight Directory Access Protocol) authentication, set
`spec.security.authentication.modes` to `["LDAP"]`.

**`spec.security.authentication.ldap.servers`**

*Type*: array of strings

*Required for LDAP authentication.* 

List of hostnames and ports of the LDAP (Lightweight Directory Access Protocol) servers. Specify
hostnames with their respective ports in the following format:

```yaml
spec:
  security:
    authentication:
      ldap:
        servers: 
          - "<hostname1>:<port1>"
          - "<hostname2>:<port2>"
```

**`spec.security.authentication.ldap.timeoutMS`**

*Type*: integer

Specifies how many milliseconds an authentication request should 
wait before timing out.

**`spec.security.authentication.ldap.transportSecurity`**

*Type*: string

*Required for LDAP authentication.* 

Specifies whether the LDAP (Lightweight Directory Access Protocol) server accepts TLS (Transport Layer Security).

If the LDAP (Lightweight Directory Access Protocol) server accepts TLS (Transport Layer Security), set the value to `tls`. If 
the LDAP (Lightweight Directory Access Protocol) server doesn't accept TLS (Transport Layer Security), leave this value blank or set 
the value to `none`.

**Note:**

If you specify a string other than `none` or `tls`, 
Kubernetes Operator still sets the setting to `tls`.

**`spec.security.authentication.ldap.caConfigMapRef`**

*Type*: collection

*Required for LDAP authentication with TLS.* 

[ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a CA (Certificate Authority) which validates the LDAP (Lightweight Directory Access Protocol) 
server's TLS (Transport Layer Security) certificate.

**`spec.security.authentication.ldap.caConfigMapRef.name`**

*Type*: string

*Required for LDAP authentication with TLS.* 

Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a CA (Certificate Authority) which validates
the LDAP (Lightweight Directory Access Protocol) server's TLS (Transport Layer Security) certificate.

**`spec.security.authentication.ldap.caConfigMapRef.key`**

*Type*: string

*Required for LDAP authentication with TLS.* 

Field name that stores the CA (Certificate Authority) which validates the LDAP (Lightweight Directory Access Protocol)
server's TLS (Transport Layer Security) certificate.

**`spec.security.authentication.ldap.bindQueryUser`**

*Type*: string

*Required for LDAP authentication.* 

LDAP (Lightweight Directory Access Protocol) Distinguished Name to which MongoDB binds when connecting to
the LDAP (Lightweight Directory Access Protocol) server.

**`spec.security.authentication.ldap.bindQueryPasswordSecretRef`**

*Type*: collection

*Required for LDAP authentication.* 

Specifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password with which
MongoDB binds when connecting to the LDAP (Lightweight Directory Access Protocol) server.

**`spec.security.authentication.ldap.bindQueryPasswordSecretRef.name`**

*Type*: string

*Required for LDAP authentication.* 

Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password with which MongoDB
binds when connecting to the LDAP (Lightweight Directory Access Protocol) server.

The [secret](https://kubernetes.io/docs/concepts/configuration/secret/) must contain only one `password` field which stores
the password.

**`spec.security.authentication.ldap.authzQueryTemplate`**

*Type*: string

*Required for LDAP authorization.*

An [RFC4515](https://tools.ietf.org/html/rfc4515) and [RFC4516](https://tools.ietf.org/html/rfc4516) LDAP-formatted query URL
template executed by MongoDB to obtain the LDAP groups that the user
belongs to. The query is relative to the host or hosts
specified in `spec.security.authentication.ldap.servers`.
You can use the following tokens in the template:

- `{USER}` 
      Substitutes the authenticated username, or the
      `transformed`
      username, into the LDAP query.
- `{PROVIDED_USER}`
      Substitutes the supplied username, before either
      authentication or LDAP transformation, into the LDAP query.
      (*Available starting in MongoDB version 4.2*)

**See also:**

LDAP Query Templates in the MongoDB Manual   

**`spec.security.authentication.agents.automationLdapGroupDN`**

*Type*: string

The Distinguished Name (DN) of the LDAP group to which the
MongoDB Agent user belongs.

This setting is required if:

- `spec.security.authentication.ldap.authzQueryTemplate` is
  present, and
- `spec.security.authentication.agents.mode` is `LDAP` or
  `X509`.

**`spec.security.authentication.ldap.userToDNMapping`**

*Type*: string

Maps the username provided to `mongod` or
`mongos` for authentication to a LDAP Distinguished Name
(DN).

**See also:**

security.ldap.userToDNMapping in the MongoDB Manual   

**`spec.security.authentication.ldap.userCacheInvalidationInterval`**

*Type*: integer

Specifies how many seconds MongoDB waits to flush the LDAP user 
cache. Defaults to 30 seconds.

**`spec.security.authentication.oidcProviderConfigs`**

*Type*: collection

*Required*

- MongoDB version has to be 7.0.11+ or 8.0.0+
- MongoDB Enterprise only is supported

**Note:**

At least one element in the collection is required when 
`spec.security.authentication.mode`  is set to `OIDC`.

**`spec.security.authentication.oidcProviderConfigs.audience`**

*Type*: string

*Required*

Entity that your external identity provider (IdP) intends the token for. Enter the 
audience value from the app you registered with your external IdP. 
When more than one IdP is defined, this must be a unique value for each
configuration that shares an `issuerURI`.

**`spec.security.authentication.oidcProviderConfigs.authorizationMethod`**

*Type*: string

*Required*

Valid values are `WorkforceIdentityFederation` and `WorkloadIdentityFederation`. 
Configure single-sign-on for human user access to deployments with Workforce 
Identity Federation. For programmatic application access to deployments, use 
Workload Identity Federation. Only one Workforce Identity Federation IdP can be 
configured per MongoDB resource. To learn more, see [Authentication and Authorization with OIDC/OAuth 2.0](https://www.mongodb.com/docs/manual/core/oidc/security-oidc/).

**`spec.security.authentication.oidcProviderConfigs.authorizationType`**

*Type*: string

*Required*

Valid values are `GroupMembership` and `UserID`. Select `GroupMembership` 
to grant authorization based on IdP user group membership, or select 
`UserID` to grant an individual user authorization.

**`spec.security.authentication.oidcProviderConfigs.clientId`**

*Type*: string

*Required*

Unique identifier for your registered application. Enter the `clientId` 
value from the app you registered with an external Identity Provider.

**`spec.security.authentication.oidcProviderConfigs.configurationName`**

*Type*: string

*Required*

Unique label that identifies this configuration. This label is visible to your 
Ops Manager users and is used when creating users and roles for authorization. 
It is case-sensitive and can only contain the following characters:

- alphanumeric characters (combination of a to z and 0 to 9)
- hyphens (-)
- underscores (_)

**`spec.security.authentication.oidcProviderConfigs.groupsClaim`**

*Type*: string

*Optional*

The identifier of the claim that includes the user principal identity. 
Accept the default value unless your IdP uses a different claim.

**`spec.security.authentication.oidcProviderConfigs.issuerURI`**

*Type*: string

*Required*

Issuer value provided by your registered IdP application. Using this URI, 
MongoDB finds an OpenID Provider Configuration Document, which is 
available in the `/.wellknown/open-id-configuration` endpoint. For MongoDB 
`8.0+`, the combination of `issuerURI` and audience must be unique 
across OIDC provider configurations. For other MongoDB versions, the 
`issuerURI` itself must be unique.

**`spec.security.roleRefs`**

*Type*: array

Array that references `ClusterMongoDBRole` custom resources that give you
fine-grained access control over your MongoDB deployment.

**`spec.security.roleRefs.kind`**

*Type*: string

The kind of the referenced custom resource. For example, `ClusterMongoDBRole`.

**`spec.security.roleRefs.kind`**

*Type*: string

The kind of the referenced custom resource. For example, `ClusterMongoDBRole`.

**`spec.security.authentication.oidcProviderConfigs.requestedScopes`**

*Type*: string

*Optional*

Tokens that give users permission to request data from the authorization 
endpoint. Only used for the Workforce Identity Federation authorization method.

**`spec.security.authentication.oidcProviderConfigs.userClaim`**

*Type*: string

*Required*

The identifier of the claim that includes the user principal 
identity. Accept the default value unless your IdP uses a different claim.

**`spec.security.authentication.agents`**

*Type*: collection

MongoDB Agent authentication configuration for the Cloud Manager or Ops Manager project.

**`spec.security.authentication.agents.mode`**

*Type*: string

The authentication mechanism that the MongoDB Agents for
your MongoDB deployment use. Valid values are `SCRAM`, 
`SCRAM-SHA-1`, `MONGODB-CR`, `X509`, `OIDC`, and
`LDAP`. The value you specify must also be present in
`spec.security.authentication.modes`. We recommend 
`SCRAM-SHA-256` (`SCRAM`) over `SCRAM-SHA-1`. If you specify 
`SCRAM-SHA-1`, you must also specify `MONGODB-CR`.

This setting is required if you specified more than one value for
`spec.security.authentication.modes`.

**`spec.security.authentication.agents.automationUserName`**

*Type*: string

Name of the user that the MongoDB Agents use to interact with your
MongoDB deployment. The username is mapped to an LDAP Distinguished
Name (DN) according to
`spec.security.authentication.ldap.userToDNMapping`. The
resulting DN must already exist in your LDAP deployment.

This setting is required if 
`spec.security.authentication.agents.mode` is `LDAP`.

**`spec.security.authentication.agents.automationPasswordSecretRef`**

*Type*: collection

Details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the
`spec.security.authentication.agents.automationUserName`
user.

This setting is required if 
`spec.security.authentication.agents.mode` is `LDAP`.

**`spec.security.authentication.agents.automationPasswordSecretRef.name`**

*Type*: string

Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the
`spec.security.authentication.agents.automationUserName`
user. You must create this secret in the same namespace to which you
deploy the Kubernetes Operator:

```sh
kubectl create secret generic ldap-agent-user \
--from-literal="password=<password>" -n <metadata.namespace>
```

This secret must contain one key, the value of which matches the
password of the
`spec.security.authentication.agents.automationUserName` user
in your LDAP deployment.

This setting is required if 
`spec.security.authentication.agents.mode` is `LDAP`.

**`spec.security.authentication.agents.automationPasswordSecretRef.key`**

*Type*: string

Key in the
`spec.security.authentication.agents.automationPasswordSecretRef.name`
[secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the user in
`spec.security.authentication.agents.automationUserName`.

This setting is required if 
`spec.security.authentication.agents.mode` is
`LDAP`.

**`spec.security.authentication.agents.clientCertificateSecretRef.name`**

*Type*: string

Specifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the MongoDB Agent\'s
TLS (Transport Layer Security) certificate. If omitted, defaults to `agent-certs`.

You must create this secret in the same namespace to which you
deploy the Kubernetes Operator and the secret must be
of type `kubernetes.io/tls`.

**`spec.security.roles`**

*Type*: array

Array that defines User-defined roles that give you
fine-grained access control over your MongoDB deployment.

To enable user-defined roles, the
`spec.security.authentication.enabled` must be `true`.

**Example:**

In this example, a user-defined role named `customRole` allows
users assigned this role to:

- Insert documents into the `cats` collection in the `pets`
  database, and
- Find and insert documents into the `dogs` collection in the
  `pets` database.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  type: ReplicaSet
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  persistent: true
  security:
    authentication:
      enabled: true
      modes:
        - "SCRAM"
    roles:
      - role: "customRole"
        db: admin    
        privileges:
        - actions:
          - insert
          resource:
            collection: cats
            db: pets
        - actions:
          - insert
          - find
          resource:
            collection: dogs
            db: pets
...
```

**`spec.security.roles.role`**

*Type*: string

Name of the user-defined role.

**`spec.security.roles.db`**

*Type*: string

The database in which you want to store the user-defined role.

**Example:**

`admin`

**`spec.security.roles.authenticationRestrictions`**

*Type*: array

Array that defines the IP address from which and to which users
assigned this `spec.security.roles.role` can
connect.

**`spec.security.roles.authenticationRestrictions.clientSource`**

*Type*: array

Array of IP addresses or CIDR blocks from which users assigned this
`spec.security.roles.role` can connect. 

MongoDB servers reject connection requests from users with this role
if the requests come from a client that is not present in this array.

**`spec.security.roles.authenticationRestrictions.serverAddress`**

*Type*: array

Array of IP addresses or CIDR blocks to which users assigned this
`spec.security.roles.role` can connect. 

MongoDB servers reject connection requests from users with this role
if the client requests to connect to a server that is not present in
this array.

**`spec.security.roles.privileges`**

*Type*: array

Array that describes the privileges that users granted this role
possess.

**`spec.security.roles.privileges.actions`**

*Type*: array

List of actions that users granted this role can perform. For a list
of accepted values, see Privilege Actions in the
MongoDB Manual for the MongoDB versions you deploy with the
Kubernetes Operator.

**`spec.security.roles.privileges.resource`**

*Type*: collection

Resources for which the privilege
`actions`
apply.

This collection must include either:

- The
  `spec.security.roles.privileges.resource.database`
  and
  `spec.security.roles.privileges.resource.collection`
  settings, or
- The
  `spec.security.roles.privileges.resource.cluster`
  setting with a value of `true`.

**`spec.security.roles.privileges.resource.database`**

*Type*: string

Database for which the privilege
`actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.security.roles.privileges.resource.collection`.

**`spec.security.roles.privileges.resource.collection`**

*Type*: string

Collection in the
`database`
for which the privilege
`actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.security.roles.privileges.resource.database`.

**`spec.security.roles.privileges.resource.cluster`**

*Type*: boolean

*Default*: False

Flag that indicates that the privilege
`actions`
apply to all databases and collections in the MongoDB deployment. If
omitted, defaults to `false`.

If set to true, do not provide values for
`spec.security.roles.privileges.resource.database`
and 
`spec.security.roles.privileges.resource.collection`.

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
