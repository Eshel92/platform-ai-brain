<!-- Part 4 of 5 of reference/k8s-operator-om-specification.md (split because the page is big). -->

## Application Database Optional Settings

This section describes optional settings related to
your Ops Manager Application Database. For optional application 
database settings specific to your multi-cluster Ops Manager deployment, see 
om_resource-spec-multi-cluster.

**`spec.applicationDatabase`**

*Type*: collection

Ops Manager `Application Database`
resource definition.

The following settings from the
replica set resource specification are
optional.

**`spec.applicationDatabase.agent.logLevel`**

*Type*: string

*Default*: INFO

Configures the level of Automation Agent logging inside the
[Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/). Accepted values include:

- `DEBUG`
- `INFO`
- `WARN`
- `ERROR`
- `FATAL`

**`spec.applicationDatabase.agent.<component>.logRotate`**

*Type*: object

Replace  *component*  with one of the following values:

-  `mongod`
-  `monitoringAgent`

MongoDB configuration object for rotating the MongoDB logs of a process. To use 
the `agent.<component>.logRotate` settings, you must set 
`systemLog.destination` 
to `file` because you can't use the `agent.<component>.logRotate` settings if you're writing 
logs to the host's syslog system.

**Note:**

If the size of files the Ops Manager dashboard generates is larger than the storage
space available in the `emptyDir` volume, consider overriding the `emptyDir`
volume with a Persistent Volume to prevent pod crashes. To learn more, see
`spec.statefulSet.spec.template.spec.volumes`.

**`spec.applicationDatabase.agent.mongod.logRotate.numTotal`**

*Type*: integer

*Default*: `0`

Total number of log files that `Ops Manager` retains. If you don't change the default,
`Ops Manager` bases rotation on your other `agent.<compenet>.logRotate` settings.

**`spec.applicationDatabase.agent.mongod.logRotate.numUncompressed`**

*Type*: integer

*Default*: `5`

Maximum number of total log files to leave uncompressed,
including the current log file.

**`spec.applicationDatabase.agent.mongod.logRotate.percentOfDiskspace`**

*Type*: number

*Default*: `0.02`

Maximum percentage of total disk space that `Ops Manager` can use to
store the log files expressed as decimal. If this limit is
exceeded, `Ops Manager` deletes compressed log files until it meets this
limit. `Ops Manager` deletes the oldest log files first.

**`spec.applicationDatabase.agent.<component>.logRotate.sizeThresholdMB`**

*Type*: number

Replace  *component*  with one of the following values:

-  `mongod`
-  `monitoringAgent`

*Required if rotating logs.* Maximum size in MB for an individual log file
before `Ops Manager` rotates it. `Ops Manager` rotates the log file immediately if it meets
the value given in either this `sizeThresholdMB` or the
`logRotate.timeThresholdHrs <spec.applicationDatabase.agent.` limit.

**`spec.applicationDatabase.agent.<component>.logRotate.timeThresholdHrs`**

*Type*: integer

Replace  *component*  with one of the following values:

-  `mongod`
-  `monitoringAgent`

*Required if rotating logs*. Maximum duration in hours for an individual
log file before the next rotation. The time is since the last rotation.
`Ops Manager` rotates the log file immediately if it meets the value given in
either `timeThresholdHrs` or
the `logRotate.sizeThresholdM <spec.applicationDatabase.agent.`
limit.

**`spec.applicationDatabase.agent.mongod.auditlogRotate`**

*Type*: object

MongoDB configuration object for rotating the MongoDB audit logs of a process.

**`spec.applicationDatabase.agent.mongod.auditlogRotate.numTotal`**

*Type*: integer

*Default*: `0`

Total number of audit log files that `Ops Manager` retains. If you don't change the default value,
`Ops Manager` bases rotation on your other `agent.mongod.auditlogRotate` settings.

**`spec.applicationDatabase.agent.mongod.auditlogRotate.numUncompressed`**

*Type*: integer

*Default*: `5`

Maximum number of total audit log files to leave uncompressed,
including the current audit log file.

**`spec.applicationDatabase.agent.mongod.auditlogRotate.percentOfDiskspace`**

*Type*: number

*Default*: `0.02`

Maximum percentage of total disk space that `Ops Manager` can use to
store the audit log files expressed as decimal. If you exceed this limit, 
`Ops Manager` deletes compressed audit log files until it meets this
limit. `Ops Manager` deletes the oldest audit log files first.

**`spec.applicationDatabase.agent.mongod.auditlogRotate.sizeThresholdMB`**

*Type*: number

*Required if rotating audit logs.* Maximum size in MB for an individual audit log file
before `Ops Manager` rotates it. `Ops Manager` rotates the audit log file immediately if it reaches
the value in either `sizeThresholdMB` or the
`auditlogRotate.timeThresholdHrs` limit.

**`spec.applicationDatabase.agent.mongod.auditlogRotate.timeThresholdHrs`**

*Type*: integer

*Required if rotating audit logs*. Maximum duration in hours for an individual
audit log file before the next rotation. The time is since the last rotation.
`Ops Manager` rotates the audit log file immediately if it reaches the value in
either `timeThresholdHrs` or
the `auditlogRotate.sizeThresholdM`
limit.

**`spec.applicationDatabase.agent.startupOptions`**

*Type*: object

MongoDB configuration object for startup options. 
See `MongoDB Agent Settings` for available fields.

**`spec.applicationDatabase.agent.systemLog`**

*Type*: object

MongoDB configuration object for configuring the `systemLog` options.

**`spec.applicationDatabase.agent.systemLog.path`**

*Type*: string

*Default:* `/var/log/mongodb-mms-automation/mongodb.log`

The path of the log file to which `mongod` or `mongos` should send all diagnostic 
logging information, rather than the standard output or the host's 
syslog. 
MongoDB creates the log file at the specified path.

The Linux package init scripts don't expect `systemLog.path` to change from the defaults. 
If you use the Linux packages and change `systemLog.path`, you will have to use your own 
init scripts and disable the built-in scripts.

**`spec.applicationDatabase.agent.systemLog.logAppend`**

*Type:* boolean

*Default:* `false`

When `true`, `mongos` or `mongod` appends new entries to the end of the existing 
log file when the `mongos` or `mongod` instance restarts. Without this option, `mongod` 
will back up the existing log and create a new file.  

**`spec.applicationDatabase.agent.systemLog.destination`**

*Type:* string

The destination to which MongoDB sends all log output. Specify either `file` or `syslog`. 
If you specify `file`, you must also specify 
`systemLog.path`.

If you don't specify 
`systemLog.path`, MongoDB 
sends all log output to standard output.

**Warning:**

The syslog daemon generates timestamps when it logs a message, not when MongoDB 
issues the message. This behavior can lead to misleading timestamps for log entries, 
especially when the system is under heavy load. We recommend using the `file`
option for production systems to ensure accurate timestamps.

**`spec.applicationDatabase.externalAccess`**

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

**`spec.applicationDatabase.memberConfig`**

*Type*: array of objects

Specification for each Application Database replica set member in your Ops Manager deployment.

**Important:**

If you set `spec.topology` to `MultiCluster`, use 
`spec.applicationDatabase.clusterSpecList.memberConfig` instead 
of `spec.applicationDatabase.memberConfig`.
In a multi-cluster Ops Manager deployment, the Kubernetes Operator ignores all parameters under 
`spec.applicationDatabase.memberConfig`.      

The number of elements in the `memberConfig` list must equal 
`spec.applicationDatabase.members`.

The order of the elements in the `memberConfig` list must reflect the order 
of members in the replica set. For example, the first element of the array 
affects the Pod at index `0`, the second element affects index `1`, and so on.

**Example:**

Consider the following example specification for a 
three-member replica set for the Application Database:

```yaml
spec:
  applicationDatabase:
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
        priority: "0"
        tags:
          tag2: "value2"
          environment: "prod"
```

**`spec.applicationDatabase.memberConfig.priority`**

*Type*: string

Number that indicates the relative likelihood of an Application Database replica set member to become the [primary](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-primary).

* To increase the relative likelihood that a replica set member becomes the primary, specify a higher `priority` value.

* To decrease the relative likelihood that a replica set member becomes the primary, specify a lower `priority` value.

For example, a member with a `memberConfig.priority` of `1.5` is more likely than a member with a `memberConfig.priority` of `0.5` to become the primary. 

A member with a `memberConfig.priority` of `0` is ineligible to become the primary. To learn more, see Member Priority.

**`spec.applicationDatabase.memberConfig.tags`**

*Type*: map

Map of replica set tags for directing
read and write operations to specific members of your Application Database replica set.

**`spec.applicationDatabase.memberConfig.votes`**

*Type*: number

Determines whether an Application Database replica set member can vote in an election. Set to `1` to allow the member to vote. Set to `0` to exclude the member from an election. 

**`spec.applicationDatabase.passwordSecretKeyRef.name`**

*Type*: string

Name of the secret that contains the
password for the Ops Manager database user `mongodb-ops-manager`.
Ops Manager uses this password to authenticate to the Application
Database.

**`spec.applicationDatabase.passwordSecretKeyRef.key`**

*Type*: string

Name of the field in the secret that
contains the password for the Ops Manager database user
`mongodb-ops-manager`. Ops Manager uses this password to
authenticate to the Application Database.

The default value is `password`.

**`spec.applicationDatabase.security.certsSecretPrefix`**

*Type*: string

Text to prefix to the Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that you
created that contains your Application Database's TLS (Transport Layer Security) key and 
certificate.

You must name your secret `<prefix>-<metadata.name>-db-cert`.

To learn how to configure your Ops Manager instance to run over
HTTPS (Hypertext Transfer Protocol Secure), see deploy-om-container.

**`spec.applicationDatabase.security.tls.ca`**

*Type*: string

Name of the Kubernetes [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) containing the CA (Certificate Authority) file for
the Application Database.

**Important:**

`spec.applicationDatabase.security.tls.ca` is required
if you use a custom CA (Certificate Authority) to sign your Application Database's
TLS (Transport Layer Security) certificates.

The Kubernetes Operator requires that you name the Application Database's
certificate `ca-pem` in the ConfigMap.

The CA (Certificate Authority) specified in this section is also used for 
configuring custom TLS (Transport Layer Security) certificates for S3 (Simple Storage Service) storage when either
`spec.backup.s3OpLogStores.customCertificate` or
`spec.backup.s3Stores.customCertificate` are set to 
`true`.

This CA (Certificate Authority) signs the certificates that:

- the Application Database replica set members use to communicate
  with one another, and
- Ops Manager uses to communicate with the Application Database replica
  set.

**Warning:**

You must concatenate your custom CA (Certificate Authority) file and the entire
TLS (Transport Layer Security) certificate chain from `downloads.mongodb.com` to prevent
Ops Manager from becoming inoperable if the application database
restarts.

**`spec.applicationDatabase.security.tls.enabled`**

**Important:**

`spec.security.applicationDatabase.tls.enabled` is 
deprecated and will be removed in a future release. To enable 
TLS (Transport Layer Security), provide a value for the 
`spec.security.applicationDatabase.certsSecretPrefix` 
setting.

Encrypts communications using TLS (Transport Layer Security) certificates between Ops Manager and
the Application Database.

### Prometheus Settings

The following settings apply when you use Prometheus with your 
Application Database:

**`spec.applicationDatabase.prometheus`**

*Type*: array

*Optional*. List that contains the parameters for exposing metrics to Prometheus.

**`spec.applicationDatabase.prometheus.metricsPath`**

*Type*: string

*Default*: `"/metrics"`

*Optional*. Human-readable string that indicates the path to the metrics
endpoint. If you don't specify this setting, the default applies.

**`spec.applicationDatabase.prometheus.passwordSecretRef`**

*Type*: object

*Conditional* Object that contains the details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for 
basic HTTP authentication. If you want to use Prometheus with your 
Application Database, you must specify this setting.

**`spec.applicationDatabase.prometheus.passwordSecretRef.key`**

*Type*: string

*Default*: `"password"`

*Optional*. Human-readable string that identifies the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/)
that stores the password for basic HTTP authentication. If you don't specify
this setting, the default applies.

**`spec.applicationDatabase.prometheus.passwordSecretRef.name`**

*Type*: string

*Conditional*

Human-readable label that identifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains 
the password for basic HTTP authentication. If you want to use 
Prometheus with your Application Database, you must specify this 
setting.

**`spec.applicationDatabase.prometheus.port`**

*Type*: integer

*Default:* 9216

*Optional*. Number that identifies the port that the metrics endpoint will
bind to. If you don't specify this setting, the default applies.

**`spec.applicationDatabase.prometheus.tlseSecretKeyRef`**

*Type*: object

*Optional*. Object that contains the details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for TLS (Transport Layer Security)
authentication.

**`spec.applicationDatabase.prometheus.tlseSecretKeyRef.key`**

*Type*: string

*Default*: `"password"`

*Optional*. Human-readable string that identifies the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the password for TLS (Transport Layer Security) authentication. If you don't specify this
setting, the default applies.

**`spec.applicationDatabase.prometheus.tlseSecretKeyRef.name`**

*Type*: string

*Conditional*. Human-readable label that identifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/)
that contains the password for TLS (Transport Layer Security) authentication. If you want to use
Prometheus with your Application Database and you want to use TLS (Transport Layer Security)
authentication, you must specify this setting.

**`spec.applicationDatabase.prometheus.username`**

*Type*: string

*Conditional*. Human-readable label that identifies the user for basic
HTTP authentication. If you want to use Prometheus with your application
database, you must specify this setting.
