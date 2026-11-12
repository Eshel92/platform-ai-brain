<!-- Part 1 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

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
