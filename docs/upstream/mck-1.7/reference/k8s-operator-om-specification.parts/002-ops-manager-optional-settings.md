<!-- Part 2 of 5 of reference/k8s-operator-om-specification.md (split because the page is big). -->

## Ops Manager Optional Settings

Ops Manager resources can also use the following settings:

**`spec.backup.fileSystemStores`**

*Type:* string

Name that identifies your file system snapshot store. To learn more, 
see configure-file-store.

**`spec.backup.logging.LogBackAccessRef`**

*Type:* string 

Reference to a ConfigMap that contains a custom `logback-access.xml` file 
for configuring Ops Manager backup logs.

The key in the ConfigMap must exactly match the name of the `logback-access.xml` 
to ensure it replaces the default file in the Ops Manager Pods.

To learn more, see k8s-om-log-rotation-crd.

**`spec.backup.logging.LogBackRef`**

*Type:* string 

Reference to a ConfigMap that contains a custom `logback.xml` file. This file
configures the general logging behavior for Ops Manager backups, including log rotation
policies, log levels, and other logging parameters.

The key in the ConfigMap must exactly match the name of the `logback-access.xml` 
to ensure it replaces the default file in the Ops Manager Pods.
To learn more, see k8s-om-log-rotation-crd.

**`spec.logging.LogBackAccessRef`**

*Type:* string 

Reference to a ConfigMap that contains a custom `logback-access.xml` file 
for configuring Ops Manager logs.

The key in the ConfigMap must be exactly `logback-access.xml` to ensure it 
replaces the default file in the Ops Manager Pods.

To learn more, see k8s-om-log-rotation-crd.

**`spec.logging.LogBackRef`**

*Type:* string 

Reference to a ConfigMap that contains a custom `logback.xml` file. This file
configures the general logging behavior for Ops Manager, including log rotation
policies, log levels, and other logging parameters.

The key in the ConfigMap must be exactly `logback.xml` to ensure it replaces
the default file in the Ops Manager Pods.

To learn more, see k8s-om-log-rotation-crd.

**Note:**

If the size of files the Ops Manager dashboard generates is larger than the storage
space available in the `emptyDir` volume, consider overriding the `emptyDir`
volume with a Persistent Volume to prevent pod crashes. To learn more, see
`spec.statefulSet.spec.template.spec.volumes`.

**`spec.opsManagerURL`**

*Type*: string

*Optional*. The URL for the Ops Manager resource in the Kubernetes Operator,
for example: `https://link.to.configured.lb.example.com`.

- If you omit this parameter, then to connect to Ops Manager instances
  the Kubernetes Operator uses the following URL as the default for the
  Ops Manager instance: `<om-name>-svc.{namespace}.svc.cluster.local`.
  This is the FQDN (fully qualified domain name) of the headless service for Ops Manager.

- If you specify this parameter, this allows you to change this URL to a
  different one.

**Note:**

Don't confuse the `spec.opsManagerURL` with the URL that
you specify in a ConfigMap for a particular
deployment to configure MongoDB deployments and Monitoring Agents
for the Application Database. The Kubernetes Operator requires to have the
`spec.opsManagerURL` to directly connect to Ops Manager
instances and to configure Ops Manager and Application Database deployments.
The Kubernetes Operator doesn't use the `spec.opsManagerURL`
to manage particular MongoDB databases.

Change the `spec.opsManagerURL` parameter to a custom URL
in the following cases:

- When you deploy Ops Manager across multiple Kubernetes clusters and the default
  URL is not accessible from the Ops Manager-hosting Pod.  For example, when
  you deploy Ops Manager on other Kubernetes clusters than those on which you
  deploy the Kubernetes Operator, the FQDN (fully qualified domain name) for the Ops Manager service might
  not be accessible. In this case, you can specify a custom URL.

- When you configure external access to the Ops Manager instance on an external
  domain, you can specify a custom URL.
  This also requires the Kubernetes Operator and the Application Database\'s
  Monitoring Agents to use this custom URL instead of the default one.

**`spec.clusterDomain`**

*Type*: string

Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) a FQDN (fully qualified domain name). The Kubernetes Operator calculates
the FQDN (fully qualified domain name) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) using a provided `clusterDomain`.
Kubernetes doesn't provide an API (Application Programming Interface) to query these hostnames.

**`spec.clusterName`**

**Important:** `spec.clusterName` is Deprecated

Use `spec.clusterDomain` instead.

*Type*: string

Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) a FQDN (fully qualified domain name). The Kubernetes Operator calculates
the FQDN (fully qualified domain name) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) using a provided `clusterName`. Kubernetes
doesn't provide an API (Application Programming Interface) to query these hostnames.

**`spec.configuration`**

*Type*: collection

Ops Manager configuration properties.
See `Ops Manager Configuration Settings` for property names and descriptions.
Each property takes a value of type `string`.

**Important:**

If Ops Manager will manage MongoDB resources deployed outside of the 
Kubernetes cluster it's deployed to, you must add the `mms.centralUrl` 
setting to `spec.configuration`.

Set the value to the URL by which Ops Manager is exposed outside of the 
Kubernetes cluster.

To learn more, see mdb-resource-deployment-locations.

**`spec.configuration.mms.featureFlag.automation.verifyDownloads`**

*Type*: string

When set to `enabled`, the MongoDB Agent requires signature files 
for all MongoDB deployments that your Ops Manager instance manages. 

When you upgrade the MongoDB Agent with this option enabled, the current version 
of the MongoDB Agent requires signature files of the new MongoDB Agent binary. 

To learn more, see k8s-signatures.

**`spec.configuration.mms.featureFlag.backup.queryable`**

*Type*: boolean

Set to `false` to disable `queryable backups`.

**`spec.configuration.mms.featureFlag.backup.wt.queryable`**

*Type*: boolean

Set to `false` to disable `queryable backups`
when using WiredTiger.

**`spec.configuration.mms.mongoDbUsage.defaultUsageType`**

*Type*: string

The Kubernetes service's `default server type`.

Accepted values are: `PRODUCTION_SERVER`, `TEST_SERVER`, `DEV_SERVER`, and
`RAM_POOL`.

**`spec.jvmParameters`**

*Type*: array of strings

*Optional*. JVM (Java Virtual Machine) parameters passed to the Ops Manager Application in the
container. Any parameters given replace the default JVM (Java Virtual Machine) parameters
for the Ops Manager Application.

This Kubernetes Operator parameter defaults to an empty list.

```yaml
spec:
  jvmParameters: ["-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=/tmp"]
```

**Important:** Change the JVM Memory Heap values at your own risk

Kubernetes Operator calculates its JVM (Java Virtual Machine) memory heap values of the
Ops Manager Application based on the container's memory. Changing the
`-Xms` and `-Xmx` values can cause issues with Ops Manager.

**`spec.security.certsSecretPrefix`**

*Type*: string

Text to prefix to the Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that you
created that contain Ops Manager\'s TLS (Transport Layer Security) key and certificate.

You must name your secret `<prefix>-<metadata.name>-cert`.

To learn how to configure your Ops Manager instance to run over
HTTPS (Hypertext Transfer Protocol Secure), see deploy-om-container.

**`spec.security.tls.ca`**

Name of the Kubernetes [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a custom CA (Certificate Authority)
file for Ops Manager.

**Important:**

`spec.security.tls.ca` is required if you use a custom
CA (Certificate Authority) to sign your Ops Manager TLS (Transport Layer Security) certificates.

The Kubernetes Operator requires that you name the certificate
for the Ops Manager resource `mms-ca.crt` in the ConfigMap.

This CA (Certificate Authority) signs the certificates that:

- clients use to connect to the Ops Manager Application, and
- agents in the Application Database [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) use to communicate
  with Ops Manager.

**Warning:**

You must concatenate your custom CA (Certificate Authority) file and the entire
TLS (Transport Layer Security) certificate chain from `downloads.mongodb.com` to prevent
Ops Manager from becoming inoperable if the application database
restarts.

**`spec.security.tls.enabled`**

**Important:**

`spec.security.tls.enabled` is 
deprecated and will be removed in a future release. To enable 
TLS (Transport Layer Security), provide a value for the 
`spec.security.certsSecretPrefix` 
setting.

Encrypts communications using TLS (Transport Layer Security) certificates between clients and 
Ops Manager.

**`spec.statefulSet.spec`**

*Type*: collection

Specification for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
for Ops Manager.

To review which fields you can add to
`spec.statefulSet.spec`, see
`StatefulSetSpec v1 apps`
in the Kubernetes documentation.

**`spec.statefulSet.spec.template`**

*Type*: collection

`Template`
for the Kubernetes Pods in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
for the Ops Manager.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.statefulSet.spec.template`.

**`spec.statefulSet.spec.template.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the
MongoDB Controllers for Kubernetes Operator creates for the Ops Manager.

To review which fields you can add to
`spec.statefulSet.spec.template.metadata`, see
the `Kubernetes documentation`.

**`spec.statefulSet.spec.template.spec`**

*Type*: collection

Specifications of the Kubernetes Pods in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the
MongoDB Controllers for Kubernetes Operator creates for the Ops Manager.

To review the complete list of fields you can add to
`spec.statefulSet.spec.template.spec`, see the
`Kubernetes documentation`.

The following example `spec.statefulSet.spec.template.spec` defines
minimum and maximum CPU and memory capacity for one Ops Manager
container the MongoDB Controllers for Kubernetes Operator deploys:

**Tip:**

For more information on the hardware, software, and networking requirements
for the hosts that run the Ops Manager components, see om-system-reqs
in the Ops Manager Documentation.

```yaml
statefulSet:
  spec:
    template:
      spec:
        containers:
          - name: mongodb-ops-manager
            resources:
              requests:
                cpu: "4"
                memory: "16Gi"
              limits:
                cpu: "8"
                memory: "32Gi"
```

**`spec.statefulSet.spec.template.spec.containers`**

*Type*: collection

List of containers that belong to the Kubernetes Pods in the
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates for the
Ops Manager.

To modify the specifications of the Ops Manager container,
you must provide the exact name of the container using the `name`
field, as shown in the following example:

```yaml
backup:
 statefulSet:
   spec:
     template:
       spec:
         containers:
         - name: mongodb-ops-manager
```

**Note:**

When you add containers to
`spec.statefulSet.spec.template.spec.containers`,
the Kubernetes Operator adds them to the Kubernetes pod. These containers
are appended to the Ops Manager containers in the pod.

**`spec.statefulSet.spec.template.spec.containers.resources.requests.cpu`**

*Type*: string

Minimum CPU capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to
host the Ops Manager.

The requested value must be less than or equal to
`spec.statefulSet.spec.template.spec.containers.resources.limits.cpu`.

**`spec.statefulSet.spec.template.spec.containers.resources.limits.cpu`**

*Type*: string

Maximum CPU capacity for the [node](https://kubernetes.io/docs/concepts/architecture/nodes/) being created to host
the Ops Manager. If omitted, this value is set to
`spec.statefulSet.spec.template.spec.containers.resources.requests.cpu`.

**`spec.statefulSet.spec.template.spec.containers.resources.requests.memory`**

*Type*: string

Minimum memory capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/)
to host the Ops Manager on Kubernetes. This value is expressed as
an integer followed by a unit of memory in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation.

**Example:**

If Ops Manager on Kubernetes requires 6 gigabytes of memory, set
this value to `6Gi`.

**Note:**

MongoDB recommends setting this value to at least `5Gi`.

The requested value must be less than or equal to
`spec.statefulSet.spec.template.spec.containers.resources.limits.memory`.

**`spec.statefulSet.spec.template.spec.containers.resources.limits.memory`**

*Type*: string

Maximum memory capacity for the [node](https://kubernetes.io/docs/concepts/architecture/nodes/) being created to host
the Ops Manager. If omitted, this value is set to
`spec.statefulSet.spec.template.spec.containers.resources.requests.memory`.

The Kubernetes Operator calculates and sets parameters for Java heap size
based on the container's memory.

**Warning:** Limit this value to less than 32 GB

Setting this value to a value greater than 32 GB (`32Gi`) can
cause issues with the backup service. Excessive heaps can cause
unpredictable results in Ops Manager.

**`spec.statefulSet.spec.template.spec.volumes`**

*Type*: collection

List of volumes that containers can mount in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the
MongoDB Controllers for Kubernetes Operator creates for Ops Manager.

If you are requesting the logs for a deployment using the Ops Manager dashboard
and the size of the temporary files is significantly large, consider using
a Persistent Volume for the `data` Kubernetes volume in the Ops Manager
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

The `data` Kubernetes volume uses an `emptyDir` type by default. To override
it and use a Persistent Volume, you can add the following configuration
to your `MongoDBOpsManager` resource:

```yaml
statefulSet:
  spec:
    template:
      spec:
        volumes:
          - name: data
            persistentVolumeClaim:
              claimName: <my-pvc>
```

Replace `<my-pvc>` with the name of your Kubernetes
`PersistentVolumeClaim`.

To use a Persistent Volume for only specific paths, such as
`/tmp`, see
`spec.statefulSet.spec.volumeClaimTemplates`.

**`spec.statefulSet.spec.volumeClaimTemplates`**

*Type*: collection

List of [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) templates that the MongoDB Controllers for Kubernetes Operator adds to the
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that it creates for Ops Manager. Each Ops Manager Pod
receives its own [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) for each template.

To review which fields you can add to each template, see the
`Kubernetes documentation`.

Use this setting to replace the default `emptyDir` volume with a
Persistent Volume for specific paths in the Ops Manager container. You
can override the following paths:

- `/tmp`
- `/mongodb-ops-manager/tmp`
- `/mongodb-ops-manager/logs`
- `/etc/mongodb-mms`
- `/mongodb-ops-manager/mongodb-releases`
- `/mongodb-ops-manager/conf`

Paths that you don't override continue to use the `data`
`emptyDir` volume. To override a path, define a template and
mount it at the path in the `mongodb-ops-manager` container. The
following example limits the `/tmp` directory to 50 GB:

```yaml
statefulSet:
  spec:
    volumeClaimTemplates:
      - metadata:
          name: om-tmp
        spec:
          accessModes: ["ReadWriteOnce"]
          resources:
            requests:
              storage: 50Gi
    template:
      spec:
        containers:
          - name: mongodb-ops-manager
            volumeMounts:
              - name: om-tmp
                mountPath: /tmp
```

The `name` in the `volumeMounts` entry must match the
`metadata.name` in the `volumeClaimTemplates` entry.

### External Connectivity Settings

This section describes optional settings related to
external connectivity in Ops Manager. For optional 
external connectivity settings specific to your 
multi-cluster Ops Manager deployment, see om_resource-spec-multi-cluster.

**`spec.externalConnectivity`**

*Type*: collection

Configuration object that enables external connectivity to Ops Manager.
If provided, the Kubernetes Operator creates a Kubernetes `service` that allows traffic
originating from outside of the Kubernetes cluster to reach the Ops Manager
application.

If not provided, the Kubernetes Operator doesn't create a Kubernetes service.
You must create one manually or use a third-party solution that
enables you to route external traffic to the Ops Manager Application in your
Kubernetes cluster.

**`spec.externalConnectivity.type`**

*Type*: string

The Kubernetes service `ServiceType`
that exposes Ops Manager outside of Kubernetes.

*Required* if `spec.externalConnectivity.type` is
present.

Accepted values are: `LoadBalancer` and `NodePort`.
`LoadBalancer` is recommended if your cloud provider supports it.
Use `NodePort` for local deployments.

**`spec.externalConnectivity.port`**

*Type*: integer

Value that indicates which port that a Kubernetes service exposes the
Ops Manager Application should use for external traffic.

- If `spec.externalConnectivity.type` is `NodePort`:

  - The Kubernetes service exposes the Ops Manager Application to external traffic
    through this port.

  - If you don't provide a `spec.externalConnectivity.port`
    value, the Kubernetes service routes traffic to the Ops Manager Application from an
    available port selected randomly from the following default range: `30000`-`32767`.

    **Note:**

    You must configure your network's firewall to allow traffic over
    this port.

- If `spec.externalConnectivity.type` is `LoadBalancer`:

  - The load balancer resource that your cloud provider creates exposes
    the Ops Manager Application through this port.

  - If you don't provide a `spec.externalConnectivity.port`
    value, the Kubernetes service exposes the Ops Manager Application to external
    traffic through the default HTTP (8080) or HTTPS (8443) port.

**`spec.externalConnectivity.loadBalancerIP`**

*Type*: string

The IP address the `LoadBalancer` Kubernetes service uses when the
Kubernetes Operator creates it.

This setting can only be used if your cloud provider supports it and
`spec.externalConnectivity.type` is `LoadBalancer`. To
learn more about the
`Type LoadBalancer`, see the
Kubernetes documentation.

**`spec.externalConnectivity.externalTrafficPolicy`**

*Type*: string

Routing policy for external traffic to the Ops Manager Kubernetes service.
The service routes external traffic to node-local or cluster-wide
endpoints depending the value of this setting.

Accepted values are: `Cluster` and `Local`. To learn which of
values meet your requirements, see `Source IPs in Kubernetes` in the Kubernetes documentation.

**Note:**

If you select `Cluster`, the `Source-IP` of your clients are
lost during the network hops that happen at the Kubernetes
network boundary.

**`spec.externalConnectivity.annotations`**

*Type*: collection

Key-value pairs that allow you to provide cloud provider-specific
configuration settings.

To learn more about
`Annotations`
and
`TLS support on AWS`,
see the Kubernetes documentation.

### Backup Settings

This section describes optional settings related to
backups in Ops Manager. For optional backup settings
specific to your multi-cluster Ops Manager deployment, see 
om_resource-spec-multi-cluster.

**`spec.backup.assignmentLabels`**

*Type*: array of strings

A list of assignment labels for the backup-daemon processes.
Use assignment labels to identify that specific backup daemon
processes are associated with particular projects. If you set assignment
labels using the Kubernetes Operator, the values that you set in the Kubernetes
configuration file for assignment labels override the values defined
in the `Ops Manager` UI. Assignment labels that you don't set using the
Kubernetes Operator continue to use the values set in the `Ops Manager` UI.

**`spec.backup.enabled`**

*Type*: boolean

Flag that enables Backup for your Ops Manager resource. When set to
`false`, Backup is disabled.

Default value is `true`.

**`spec.backup.encryption`**

*Type*: object

Object that contains the backup encryption configuration settings.

**`spec.backup.encryption.kmip`**

*Type*: object

Object that contains the KMIP (Key Management Interoperability Protocol) backup encryption configuration 
settings. To learn more, see configure-kmip-backup-encryption.

**Note:**

If you set this parameter, the API key linked with the value of 
`spec.credentials` must have the `Global Owner` role.

**`spec.backup.encryption.kmip.server`**

*Type*: object

Object that contains the KMIP (Key Management Interoperability Protocol) backup encryption server 
configuration settings.

**`spec.backup.encryption.kmip.server.ca`**

*Type*: string

Human-readable label that identifies the ConfigMap that contains an 
entry for the CA (Certificate Authority) certificate (`ca.pem`) to use for KMIP (Key Management Interoperability Protocol) 
authentication.

**`spec.backup.encryption.kmip.server.url`**

*Type*: string

URL (Uniform Resource Locator) for the KMIP (Key Management Interoperability Protocol) server that uses the `hostname.port` format 
(for example, `192.168.1.3:5696` or 
`my-kmip-server.mycorp.com:5696`).

**`spec.backup.headDB`**

*Type*: collection

Configuration settings for the head database.
Kubernetes Operator creates a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) with the specified configuration.

| Scalar | Data Type | Description |
|---|---|---|
| `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
| `storage` | string | Minimum size of [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that should be mounted. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is `30Gi`. To learn more, see backup-hardware-requirements. For example, if the head database requires 60 gigabytes of storage space, set this value to `60Gi`. |
| `storageClass` | string | Type of storage specified in a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims). You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

**`spec.backup.jvmParameters`**

*Type*: array of strings

*Optional*. JVM (Java Virtual Machine) parameters passed to the Ops Manager backup service
in the container.

This Kubernetes Operator parameter defaults to an empty list.

```yaml
spec:
  backup:
    jvmParameters: ["-XX:+UseStringCache"]
```

**Warning:** Change the JVM Memory Heap values at your own risk

Kubernetes Operator calculates the JVM (Java Virtual Machine) memory heap values of the
backup service based on the container's memory. Changing the
`-Xms` and `-Xmx` values can cause issues with Ops Manager.

**`spec.backup.members`**

*Type*: integer

*Optional*. Number of `backup daemon services`
to deploy in Kubernetes. If not specified, defaults to `1`.
To ensure high availability for your backup service, deploy
`multiple backup daemons`
in Ops Manager.
   

**`spec.backup.opLogStores`**

*Type*: collection

*Required if you enable backup.* Array of oplog stores
used for backup. Each item in the array references a MongoDB database
resource deployed in the Kubernetes cluster by the Kubernetes Operator.

**`spec.backup.opLogStores.assignmentLabels`**

*Type*: array of strings

A list of assignment labels for the oplog store.
Use assignment labels to identify that specific oplog stores are associated
with particular projects. If you set assignment labels using the Kubernetes Operator,
the values that you set in the Kubernetes configuration file for assignment
labels override the values defined in the `Ops Manager` UI. Assignment labels
that you don't set using the Kubernetes Operator continue to use the values
set in the `Ops Manager` UI.

**`spec.backup.opLogStores.name`**

*Type*: string

*Required if you enable Backup.* Name of the oplog store.

**Important:**

Once specified, don't edit the name of the oplog store.

**`spec.backup.opLogStores.mongodbResourceRef.name`**

*Type*: string

*Required if you enable Backup.* Name of the `MongoDB` resource or the `MongoDBMultiCluster` resource
that you create to store oplog slices. You must deploy this resource in
the same namespace as the Ops Manager resource.

The Oplog database only supports the `SCRAM` authentication mechanism.
You cannot enable other authentication mechanisms.

If you enable `SCRAM` authentication on the oplog database, you
must: 

- Create a MongoDB user resource to connect Ops Manager to the oplog 
  database.
- Specify the `name`
  of the user in the Ops Manager resource definition.

If a MongoDB database resource with this name doesn't exist, the
`backup` resource enters a `Pending` state. The Kubernetes Operator
retries every 10 seconds until a MongoDB database resource with this
name is created.

**Note:**

The Kubernetes Operator begins to reconcile the Ops Manager resource 
automatically when you make security changes to the database 
resources you reference in this setting. The Kubernetes Operator updates
the `mongoUri` and `ssl` flags in the Ops Manager configuration
based on your changes.

**`spec.backup.opLogStores.mongodbUserRef.name`**

*Type*: string

*Required if SCRAM authentication is enabled on the oplog
store database.* Name of the MongoDB user resource used to connect to
the oplog store database. Deploy this user resource in the same
namespace as the Ops Manager resource and with all of the following roles:

- readWriteAnyDatabase
- dbAdminAnyDatabase
- clusterMonitor

**`spec.backup.blockStores`**

*Type*: collection

*Required if you enable Backup using a blockstore.* Array of
blockstores used for Backup.
Each item in the array references a MongoDB database resource deployed
in the Kubernetes cluster by the Kubernetes Operator.

**`spec.backup.blockStores.assignmentLabels`**

*Type*: array of strings

A list of assignment labels for the blockstore.
Use assignment labels to identify that specific blockstores are
associated with particular projects. If you set assignment labels using
the Kubernetes Operator, the values that you set in the Kubernetes configuration
file for assignment labels override the values defined in the `Ops Manager` UI.
Assignment labels that you don't set using the Kubernetes Operator continue
to use the values set in the `Ops Manager` UI.

**`spec.backup.blockStores.name`**

*Type*: string

*Required if you enable backup using a blockstore.* Name of the blockstore.

**Important:**

Once specified, don't edit the name of the blockstore.

**`spec.backup.blockStores.mongodbResourceRef.name`**

*Type*: string

*Required if you enable backup using a blockstore.* Name of the MongoDB database
resource that you create for the blockstore. You must deploy this database
resource in the same namespace as the Ops Manager resource.

The blockstore database only supports the `SCRAM` authentication
mechanism. You cannot enable other authentication mechanisms.

If you enable `SCRAM` authentication on the blockstore database,
you must:

- Create a MongoDB user resource to connect Ops Manager to the
  blockstore database.
- Specify the `name`
  of the user in the Ops Manager resource definition.

If a MongoDB database resource with this name doesn't exist, the
`backup` resource enters a `Pending` state. The Kubernetes Operator
retries every 10 seconds until a MongoDB database resource with this
name is created.

**Note:**

The Kubernetes Operator begins to reconcile the Ops Manager resource 
automatically when you make security changes to the database 
resources you reference in this setting. The Kubernetes Operator updates
the `mongoUri` and `ssl` flags in the Ops Manager configuration
based on your changes.

**`spec.backup.blockStores.mongodbUserRef.name`**

*Type*: string

*Required if SCRAM authentication is enabled on the blockstore database.*
Name of the MongoDB user resource used to connect to the blockstore
database. Deploy this user resource in the same namespace as the
Ops Manager resource and with all of the following roles:

- readWriteAnyDatabase
- dbAdminAnyDatabase
- clusterMonitor

**`spec.backup.queryableBackupSecretRef.name`**

*Type*: string

Name of the secret that contains the `queryable.pem`
file from Ops Manager that you will use for accessing and querying backups
based on your deployment's TLS (Transport Layer Security) requirements.The PEM file contains
a public key certificate and its associated private key that are needed
to access and run queries on backup snapshots in Ops Manager.
To query backups, specify the value for this parameter. If not set,
backups are not affected, but you can't query them.

**`spec.backup.statefulSet.spec`**

*Type*: collection

Specification for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
for the `backup daemon service`.

To review which fields you can add to
`spec.backup.statefulSet.spec`, see
`StatefulSetSpec v1 apps` in the Kubernetes documentation.

**`spec.backup.statefulSet.spec.template`**

*Type*: collection

`Template`
for the Kubernetes Pods in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
for the `backup daemon service`.

**Note:**

The Kubernetes Operator doesn't validate the fields you provide
in `spec.backup.statefulSet.spec.template`.

**`spec.backup.statefulSet.spec.template.metadata`**

*Type*: collection

Metadata for the Kubernetes Pods in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the
MongoDB Controllers for Kubernetes Operator creates for the `backup daemon service`.

To review which fields you can add to
`spec.backup.statefulSet.spec.template.metadata`, see
the `Kubernetes documentation`.

**`spec.backup.statefulSet.spec.template.spec`**

*Type*: collection

Specifications of the Kubernetes Pods in the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the
MongoDB Controllers for Kubernetes Operator creates for the `backup daemon service`.

To review the complete list of fields you can add to
`spec.backup.statefulSet.spec.template.spec`, see the
`Kubernetes documentation`.

The following example `spec.backup.statefulSet.spec.template.spec`
defines minimum and maximum CPU and memory capacity for one
`backup daemon service` container the MongoDB Controllers for Kubernetes Operator deploys:

**Tip:**

For more information on the hardware, software, and networking requirements
for the hosts that run the Ops Manager components, see om-system-reqs
in the Ops Manager Documentation.

```yaml
statefulSet:
  spec:
    template:
      spec:
        containers:
        - name: mongodb-backup-daemon
          resources:
            requests:
              cpu: "4"
              memory: "8Gi"
            limits:
              cpu: "8"
              memory: "16Gi"
```

**`spec.backup.statefulSet.spec.template.spec.containers`**

*Type*: collection

List of containers that belong to the Kubernetes Pods in the
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates for the
`backup daemon service`.

To modify the specifications of the `backup daemon service` container,
you must provide the exact name of the container using the `name`
field, as shown in the following example:

```yaml
backup:
 statefulSet:
   spec:
     template:
       spec:
         containers:
         - name: mongodb-backup-daemon
```

**Note:**

When you add containers to
`spec.backup.statefulSet.spec.template.spec.containers`,
the Kubernetes Operator adds them to the Kubernetes pod. These containers
are appended to the backup-daemon containers in the pod.

**`spec.backup.statefulSet.spec.template.spec.containers.resources.requests.cpu`**

*Type*: string

Minimum CPU capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/) to
host the `backup daemon service`.

The requested value must be less than or equal to
`spec.backup.statefulSet.spec.template.spec.containers.resources.limits.cpu`.

**`spec.backup.statefulSet.spec.template.spec.containers.resources.limits.cpu`**

*Type*: string

Maximum CPU capacity for the [node](https://kubernetes.io/docs/concepts/architecture/nodes/) being created to host
the `backup daemon service`.
If omitted, this value is set to
`spec.backup.statefulSet.spec.template.spec.containers.resources.requests.cpu`.

**`spec.backup.statefulSet.spec.template.spec.containers.resources.requests.memory`**

*Type*: string

Minimum memory capacity that must be available on a Kubernetes [node](https://kubernetes.io/docs/concepts/architecture/nodes/)
to host the `backup daemon service` on Kubernetes.
This value is expressed as an integer followed by a unit of memory
in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation.

**Note:**

Set this value to at least `4.5Gi`. Values of less than `4.5Gi`
might result in an error.

The requested value must be less than or equal to
`spec.backup.statefulSet.spec.template.spec.containers.resources.limits.memory`.

**`spec.backup.statefulSet.spec.template.spec.containers.resources.limits.memory`**

*Type*: string

Maximum memory capacity for the [node](https://kubernetes.io/docs/concepts/architecture/nodes/) being created to host
the `backup daemon service`. If omitted,
this value is set to `spec.backup.statefulSet.spec.template.spec.containers.resources.requests.memory`.

The Kubernetes Operator calculates and sets parameters for Java heap size
based on the container's memory.

**Warning:** Limit this value to less than 32 GB

Setting this value to a value greater than 32 GB (`32Gi`) can
cause issues with the backup service. Excessive heaps can cause
unpredictable results in Ops Manager.

### S3 Settings

You can configure Ops Manager to use S3 (Simple Storage Service) for storing oplogs and backup
snapshots, and secure connections to S3 (Simple Storage Service) with TLS (Transport Layer Security) using keys 
issued by custom CA (Certificate Authority). 

To configure custom CA keys, use the ConfigMap with which you 
configured TLS (Transport Layer Security) for your Application Database as described on
the TLS-Encrypted Connection (HTTPS) tab of 
deploy-om-container.
Set `spec.applicationDatabase.security.tls.ca` to this ConfigMap.

You can use TLS (Transport Layer Security) for both S3 (Simple Storage Service) and your Application Database, or for 
S3 (Simple Storage Service) only. 

- To use TLS (Transport Layer Security) for both, get certificates for both purposes from the 
  same `ca-pem` referenced in the ConfigMap.
- To use TLS (Transport Layer Security) for S3 (Simple Storage Service) only, don't define 
  `spec.security.applicationDatabase.certsSecretPrefix` in 
  your ConfigMap.

**`spec.backup.s3OpLogStores.assignmentLabels`**

*Type*: array of strings

A list of assignment labels for S3 (Simple Storage Service) oplog stores. Use assignment labels
to identify that specific S3 (Simple Storage Service) oplog stores are associated with particular
projects. If you set assignment labels using the Kubernetes Operator, the values
that you set in the Kubernetes configuration file for assignment labels override
the values defined in the `Ops Manager` UI. Assignment labels that you don't set
using the Kubernetes Operator continue to use the values set in the `Ops Manager` UI.

**`spec.backup.s3OpLogStores.customCertificate`**

*Type*: boolean

*Deprecated*. Use
`spec.backup.s3OpLogStores.customCertificateSecretRefs`
instead. 

Flag that indicates whether you use AppDB certificates
(`appdb-ca`) as the custom TLS (Transport Layer Security) certificate for your S3 (Simple Storage Service) oplog
store. The default is `False`. 

**`spec.backup.s3OpLogStores.customCertificateSecretRefs`**

*Type*: array of objects

List of custom certificates for your S3 (Simple Storage Service) oplog store using Kubernetes
[secrets](https://kubernetes.io/docs/concepts/configuration/secret/). The base64-encoded x.509 certificate must already be
present in a Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) with a key and must be parsable by
the [Java CertifcateFactory](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/security/cert/CertificateFactory.html).
You can't specify multiple certificates in a chain in one secret. If
you specify multiple certificates in a chain in one secret,
Kubernetes Operator uses only the first certificate in the chain. If you
also provide the
`customCertificate` setting,  
Kubernetes Operator uses the
`spec.applicationDatabase.security.tls.ca` as the custom
certificate for backups.   

Each entry in the list specifies the
`name`
and the
`key`.
If you specify multiple secrets, Kubernetes Operator uses all the
certificates in the specified secrets. 

If you don't provide this setting, Ops Manager uses the JVM (Java
Virtual Machine) Default Trust Store used by Ops Manager.

**`spec.backup.s3OpLogStores.customCertificateSecretRefs.name`**

*Type*: string

*Required to use custom certificates for your S3 oplog store.* Kubernetes
[secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the custom certificate.

**`spec.configuration.mms.mongoDbUsage.defaultUsageType`**

*Type*: string

The Kubernetes service's `default server type`.

**`spec.backup.s3OpLogStores.customCertificateSecretRefs.key`**

*Type*: string

*Required to use custom certificates for your S3 oplog store.* File that
represents the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the base64-encoded x.509
certificate. If you don't specify this setting, the Kubernetes Operator can't
utilize the custom certificate for S3 (Simple Storage Service) oplog store backups. 

**`spec.backup.s3OpLogStores.irsaEnabled`**

*Type*: boolean

Flag that enables using AWS (Amazon Web Services) `IAM roles for service accounts`
in AWS (Amazon Web Services) `EKS` to configure
an S3 (Simple Storage Service) oplog store. The default is `False`. If you aren't using
AWS (Amazon Web Services) EKS, this flag has no effect. When set to `False`, using AWS (Amazon Web Services)
IAM roles for service accounts in EKS to configure an S3 (Simple Storage Service) oplog store
is disabled. To learn more, see
`IAM roles for service accounts in EKS`.

**`spec.backup.s3OpLogStores.name`**

*Type*: string

*Required to store the oplog using an S3 store.* Name of the S3 (Simple Storage Service) oplog store.

**`spec.backup.s3OpLogStores.mongodbResourceRef.name`**

*Type*: string

Name of the MongoDB database resource that you create to store
metadata for the S3 (Simple Storage Service) oplog store. You must deploy this database
resource in the same namespace as the Ops Manager resource.

**Note:**

Omit this setting to use the Application Database to store
metadata for the S3 (Simple Storage Service) oplog store.

If you omit this setting, you must also omit the
`spec.backup.s3OpLogStores.mongodbUserRef.name` setting.
The Kubernetes Operator handles `SCRAM` user authentication
internally.

If you enable `SCRAM` authentication on this database, you must:

- Create a MongoDB user resource to connect Ops Manager to the
  database.
- Specify the
  `name` of the
  user in the Ops Manager resource definition.

**`spec.backup.s3OpLogStores.mongodbUserRef.name`**

*Type*: string

*Required if you created a MongoDB database resource to store
S3 oplog metadata and SCRAM is enabled on this database.* Name of the
MongoDB user resource used to connect to the metadata database of the
S3 (Simple Storage Service) oplog store. Deploy this user resource in the same namespace as
the Ops Manager resource and with all of the following roles:

- readWriteAnyDatabase
- dbAdminAnyDatabase
- clusterMonitor

**Important:**

Once specified, don't edit the name of the S3 (Simple Storage Service) metadata oplog
store username.

**`spec.backup.s3OpLogStores.s3SecretRef.name`**

*Type*: string

Required to store the oplog using an S3 store if `spec.backup.s3OpLogStores.irsaEnabled` 
is not set to `true`.

Name of the secret that contains the `accessKey` and `secretKey` fields. 
The `backup daemon service`
uses the values of these fields as credentials to access your
AWS (Amazon Web Services) S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket. To configure the S3 (Simple Storage Service) oplog 
store, you must specify both keys in the secret.

If you set `spec.backup.s3OpLogStores.irsaEnabled` to `true`, you don't need 
to set the `s3SecretRef`, because the AWS S3 credentials are mounted as 
pod environment variables.

**`spec.backup.s3OpLogStores.pathStyleAccessEnabled`**

*Type*: boolean

*Required to store the oplog using an S3 store.* Indicates the
style of the bucket endpoint URL.

| Value | Description | Example |
|---|---|---|
| `true` | Path-style URL | `s3.amazonaws.com/<bucket>` |
| `false` | Virtual-host-style URL | `<bucket>.s3.amazonaws.com` |

To learn more about
[annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
and
`TLS support on AWS`,
see the Kubernetes documentation.

**`spec.backup.s3OpLogStores.s3BucketEndpoint`**

*Type*: string

*Required to store the oplog using an S3 store.* URL of the AWS (Amazon Web Services) S3 (Simple Storage Service)
bucket or S3 (Simple Storage Service)-compatible bucket that hosts the oplog store.

**Note:**

If your endpoint doesn't include a region in its URL (Uniform Resource Locator), 
specify the `s3RegionOverride` 
field.

**`spec.backup.s3OpLogStores.s3BucketName`**

*Type*: string

*Required to store the oplog using an S3 store.* Name of the AWS (Amazon Web Services)
S3 (Simple Storage Service) bucket or S3 (Simple Storage Service)-compatible bucket that hosts the oplog store.

**`spec.backup.s3OpLogStores.s3RegionOverride`**

*Type*: string

Region where your S3 (Simple Storage Service)-compatible bucket resides. Use this 
field only if your S3 (Simple Storage Service) oplog store's
`s3BucketEndpoint`
doesn't support region scoping. Region scoping is when your endpoint doesn't include a region in its URL (Uniform Resource Locator).

Don't use this field with AWS (Amazon Web Services) S3 (Simple Storage Service) buckets. For more information, see 
`S3 Blockstore Configuration`.

**`spec.backup.s3Stores.assignmentLabels`**

*Type*: array of strings

A list of assignment labels for the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible buckets
where `stores` the
database backup snapshots. Use assignment labels to identify that
specific S3 (Simple Storage Service) stores are associated with particular projects.
If you set assignment labels using the Kubernetes Operator, the values that
you set in the Kubernetes configuration file for assignment labels override
the values defined in the `Ops Manager` UI. Assignment labels that you don't set
using the Kubernetes Operator continue to use the values set in the `Ops Manager` UI.

**`spec.backup.s3Stores.customCertificate`**

*Type*: boolean

*Deprecated*. Use
`spec.backup.s3Stores.customCertificateSecretRefs`
instead. 

Flag that indicates whether you use Application Database\'s certificates
(`appdb-ca`) as the custom TLS (Transport Layer Security) certificate for your S3 (Simple Storage Service) backups.
The default is `False`. 

**`spec.backup.s3Stores.customCertificateSecretRefs`**

*Type*: array of objects

List of custom certificates for your S3 (Simple Storage Service) snapshot store using Kubernetes
[secrets](https://kubernetes.io/docs/concepts/configuration/secret/). The base64-encoded x.509 certificate must already be
present in a Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) with a key and must be parsable by
the [Java CertifcateFactory](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/security/cert/CertificateFactory.html).
You can't specify multiple  certificates in a chain in one secret. If
you specify multiple certificates in a chain in one secret,
Kubernetes Operator uses only the first certificate in the chain. If you
also provide the `spec.backup.s3Stores.customCertificate`
setting, Kubernetes Operator uses the
`spec.applicationDatabase.security.tls.ca` as the
custom certificate for backups.

Each entry in the list specifies the
`name`
and the
`key`.
If you specify multiple secrets, Kubernetes Operator uses all the
specified secrets. 

If you don't provide this setting, the Kubernetes Operator uses the
JVM (Java Virtual Machine) Default Trust Store used by
Ops Manager for backups. 

**`spec.backup.s3Stores.customCertificateSecretRefs.name`**

*Type*: string

*Required to use custom certificates for your S3 oplog store.* Kubernetes
[secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the custom certificate.

**`spec.backup.s3Stores.customCertificateSecretRefs.key`**

*Type*: string

*Required to use custom certificates for your S3 oplog store.* File that
represents the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the
base64-encoded x.509 certificate. If you don't specify this setting,
Kubernetes Operator can't utilize the custom certificate for S3 (Simple Storage Service) snapshot
store and defaults to the default JVM {Java Virtual Machine)
trust store used by Ops Manager. 

**`spec.backup.s3Stores.irsaEnabled`**

*Type*: boolean

Flag that enables using AWS (Amazon Web Services) `IAM roles for service accounts`
in AWS (Amazon Web Services) `EKS` to configure
an S3 (Simple Storage Service) snapshot store. The default is `False`. If you aren't using
AWS (Amazon Web Services) EKS, this flag has no effect. When set to `False`, using AWS (Amazon Web Services)
IAM roles for service accounts in EKS to configure an S3 (Simple Storage Service) snapshot
store is disabled. To learn more, see
`IAM roles for service accounts in EKS`.

**`spec.backup.s3Stores.name`**

*Type*: string

*Required to store the oplog using an S3 store.* Name of the S3 (Simple Storage Service) snapshot store.

**Important:**

Once specified, don't edit the name of the S3 (Simple Storage Service) snapshot store. This change will likely fail if
backups use the old name. The consequences of
a successful change are unpredictable.

**`spec.backup.s3Stores.mongodbResourceRef.name`**

*Type*: string

Name of the `MongoDB` resource or `MongoDBMultiCluster` resource that you create to store
metadata for the S3 (Simple Storage Service) snapshot store. You must deploy this database
resource in the same namespace as the Ops Manager resource.

**Note:**

Omit this setting to use the Application Database to store
metadata for the S3 (Simple Storage Service) snapshot store.

If you omit this setting, you must also omit the
`spec.backup.s3Stores.mongodbUserRef.name` setting.
The Kubernetes Operator handles `SCRAM` user authentication
internally.

If you enable `SCRAM` authentication on this database, you must:

- Create a MongoDB user resource to connect Ops Manager to the
  database.
- Specify the
  `name` of the
  user in the Ops Manager resource definition.

**Important:**

Once specified, don't edit the name of the S3 (Simple Storage Service) snapshot store.
This change will likely fail if backups use the old name. The
consequences of a successful change are unpredictable.

If a MongoDB database resource with this name doesn't exist, the
`backup` resource enters a `Pending` state. The Kubernetes Operator
retries every 10 seconds until a MongoDB database resource with this
name is created.

**Note:**

The Kubernetes Operator begins to reconcile the Ops Manager resource 
automatically when you make security changes to the database 
resources you reference in this setting. The Kubernetes Operator updates
the `mongoUri` and `ssl` flags in the Ops Manager configuration
based on your changes.

**`spec.backup.s3Stores.mongodbUserRef.name`**

*Type*: string

*Required if you created a MongoDB database resource to store
S3 (Simple Storage Service) snapshot metadata and SCRAM is enabled on this database.* Name of
the MongoDB user resource used to connect to the metadata
database of the S3 (Simple Storage Service) snapshot store. Deploy this user resource in the
same namespace as the Ops Manager resource and with all of the following roles:

- readWriteAnyDatabase
- dbAdminAnyDatabase
- clusterMonitor

**Important:**

Once specified, don't edit the name of the S3 (Simple Storage Service) metadata snapshot
store username.

**`spec.backup.s3Stores.s3SecretRef.name`**

*Type*: string

Required if you enable Backup using an S3 store and you don't set 
`spec.backup.s3Stores.irsaEnabled` to `true`.

Name of the secret that contains the `accessKey` and `secretKey` fields. 
The `backup daemon service`
uses the values of these fields as credentials to access your
AWS (Amazon Web Services) S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket. The S3 (Simple Storage Service) snapshot store
can't be configured if the secret is missing either key.

If you set `spec.backup.s3Stores.irsaEnabled` to `true`, you don't need
to set the `s3SecretRef`, because the AWS S3 credentials are mounted as
pod environment variables.

**`spec.backup.s3Stores.objectLockEnabled`**

*Type*: boolean

Specifies whether the AWS (Amazon Web Services) S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket
backing this snapshot store has Object Lock enabled. Set this
field to `true` to enable immutable backups for the store.

This field is supported only with Ops Manager version 8.0.19 or
later. For information about configuring immutable backups in
Ops Manager, see `Set Immutable Backup`.

Default value is `false`.

**`spec.backup.s3Stores.pathStyleAccessEnabled`**

*Type*: boolean

*Required if you enable Backup using an S3 store.* Indicates the
style of the bucket endpoint URL.

| Value | Description | Example |
|---|---|---|
| `true` | Path-style URL | `s3.amazonaws.com/<bucket>` |
| `false` | Virtual-host-style URL | `<bucket>.s3.amazonaws.com` |

**`spec.backup.s3Stores.s3BucketEndpoint`**

*Type*: string

*Required if you enable Backup using an S3 store.* URL of the AWS (Amazon Web Services) S3 (Simple Storage Service)
bucket or S3 (Simple Storage Service)-compatible bucket that hosts the snapshot store. 

**Note:**

If your endpoint doesn't include a region in its URL (Uniform Resource Locator), 
specify the `s3RegionOverride` 
field.

**`spec.backup.s3Stores.s3BucketName`**

*Type*: string

*Required if you enable Backup using an S3 store.* Name of the AWS (Amazon Web Services) S3 (Simple Storage Service)
bucket or S3 (Simple Storage Service)-compatible bucket that hosts the snapshot store.

**`spec.backup.s3Stores.s3RegionOverride`**

*Type*: string

Region where your S3 (Simple Storage Service)-compatible bucket resides. Use this 
field only if your S3 (Simple Storage Service) store's 
`s3BucketEndpoint`
doesn't support region scoping. Region scoping is when your endpoint doesn't include a region in its URL (Uniform Resource Locator).

Don't use this field with AWS (Amazon Web Services) S3 (Simple Storage Service) buckets. For more information, see 
`S3 Blockstore Configuration`.
