<!-- Converted from reference/k8s-operator-multi-cluster-specification.txt (reStructuredText). Includes are inlined. -->

# Multi-Kubernetes-Cluster Resource Specification

The `MongoDBMultiCluster` resource defines your multi-Kubernetes cluster MongoDB deployment and gives the MongoDB Controllers for Kubernetes Operator the information it needs to create or update your clusters, `Ops Manager` deployment, [statefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), services, and other Kubernetes resources.  

## Example

The following example shows a resource specification for a multi-Kubernetes cluster MongoDB deployment:

```yaml
# This example provides statefulSet overrides per cluster.

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
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar1
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          # Use the following settings to override the default storage size of the "data" Persistent Volume.
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi
    - clusterName: cluster2.example.com
      members: 1
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar2
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi
    - clusterName: cluster3.example.com
      members: 1
      statefulSet:
        spec:
          template:
            spec:
              containers:
                # Example of custom sidecar containers. Remove it before using the file in production.
                - name: sidecar3
                  image: busybox
                  command: [ "sleep" ]
                  args: [ "infinity" ]
          volumeClaimTemplates:
            - metadata:
                name: data
              spec:
                resources:
                  requests:
                    storage: 1Gi

...
```

## Required `MongoDBMultiCluster` Resource Settings

This section describes settings that you must use for your `MongoDBMultiCluster` resource.

`apiVersion`
  *Type*: string

  Version of the MongoDB Kubernetes resource schema.

`kind`
  *Type*: string

  Kind of MongoDB Kubernetes resource to create. Set this to `MongoDBMultiCluster`.

`metadata.name`
  *Type*: string

  Name of the MongoDB Kubernetes resource you are creating.

  Resource names must be 44 characters or less.

`spec.credentials`
  *Type*: string

  Name of the secret you created as `Ops Manager` API (Application Programming Interface)
  authentication credentials for the Kubernetes Operator to communicate with Ops Manager.

  The `Ops Manager` Kubernetes Secret object
  holding the Credentials must exist on the **same** Namespace as
  the resource you want to create.

  **Important:** Operator manages changes to the Secret

  The Kubernetes Operator tracks any changes to the Secret and
  reconciles the state of the `MongoDB` resource.

`spec.type`
  *Type*: string

  Type of MongoDB Kubernetes resource to create. The only accepted value for a multi-Kubernetes cluster MongoDB deployment is **ReplicaSet**.

`spec.version`
  *Type*: string

  Version of MongoDB installed for this `MongoDBMultiCluster` resource.

  **Important:**

  Ensure that you choose a compatible MongoDB Server version.

  Compatible versions differ depending on the base image that the
  MongoDB database resource uses.

## Optional `MongoDBMultiCluster` Resource Settings

`MongoDBMultiCluster` resources can use the following settings:

`spec.additionalMongodConfig`
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

`spec.agent`
  *Type*: collection

  MongoDB Agent configuration settings for the MongoDB database resource.

`spec.agent.startupOptions`
  *Type*: collection

  MongoDB Agent settings with which you want to start the MongoDB database resource.

  You must provide MongoDB Agent settings as key-value pairs. The values
  must be strings.  
  For a list of supported MongoDB Agent settings, see:

  - `MongoDB Agent Settings`
    for Cloud Manager projects.
  - `MongoDB Agent Settings` for the Ops Manager version you
    deployed with the Kubernetes Operator. 

`spec.backup`
  *Type*: collection

  The collection container for spec.backup.mode,
  which enables continuous backups for MongoDB resources in Kubernetes Operator.

`spec.backup.assignmentLabels`
  *Type*: array

  A list of assignment labels for the backup-daemon processes.
  Use assignment labels to identify that specific backup daemon
  processes are associated with particular projects. If you set assignment
  labels using the Kubernetes Operator, the values that you set in the Kubernetes
  configuration file for assignment labels override the values defined
  in the `Ops Manager` UI. Assignment labels that you don't set using the
  Kubernetes Operator continue to use the values set in the `Ops Manager` UI.

`spec.backup.autoTerminateOnDeletion`
  *Type*: boolean

  Flag that indicates whether the Kubernetes Operator stops and terminates the
  backup when you delete a `MongoDBMultiCluster` resource. The default value is `false`.
  Setting this flag to `true` is useful when you want to delete the
  `MongoDBMultiCluster` resource while the spec.backup.mode setting
  is set to `enabled`.

`spec.backup.encryption`
  *Type*: object

  Object that contains the backup encryption configuration settings.

`spec.backup.encryption.kmip`
  *Type*: object

  Object that contains the KMIP (Key Management Interoperability Protocol) backup encryption configuration 
  settings. To learn more, see configure-kmip-backup-encryption.

`spec.backup.encryption.kmip.client`
  *Type*: object

  Object that contains the KMIP (Key Management Interoperability Protocol) backup encryption client configuration 
  settings.

`spec.backup.mode`
  *Type*: string
  
  Enables continuous backups for a `MongoDBMultiCluster` resource.
  Possible values are `enabled`, `disabled`, and
  `terminated`.
  

  **Note:**

  The spec.backup.mode
  setting relies on Backup that is
  enabled in Ops Manager and requires that the
  `spec.backup.enabled`
  value in the Ops Manager resource specification is set to `true`.

  
  After you enable continuous backups for your MongoDB resource with
  spec.backup.mode, you can check the backup status.

`spec.backup.snapshotSchedule`
  *Type*: collection

  Collection container for snapshot schedule settings for
  continuous backups for MongoDB resources in Kubernetes Operator.

`spec.backup.snapshotSchedule.dailySnapshotRetentionDays`
  *Type*: number
  
  Number of days to keep daily snapshots. You can set a value 
  between `1` and `365`, inclusive. Setting the value to `0`
  disables this rule.

`spec.backup.snapshotSchedule.fullIncrementalDayOfWeek`
  *Type*: string
  
  Day of the week when Ops Manager takes a full snapshot. This setting 
  ensures a recent complete backup. Ops Manager sets the default value to
  `SUNDAY`.

`spec.backup.snapshotSchedule.monthlySnapshotRetentionMonths`
  *Type*: number
  
  Number of months to keep monthly snapshots. You can set a value 
  between `1` and `36`, inclusive. Setting the value to `0`
  disables this rule.
 

`spec.backup.snapshotSchedule.pointInTimeWindowHours`
  *Type*: number
  
  Number of hours in the past for which you can create a point-in-time
  snapshot.

`spec.backup.snapshotSchedule.referenceHourOfDay`
  *Type*: number
  
  UTC (Coordinated Universal Time) hour of the day to schedule snapshots using a 24 hour clock.
  You can set a value between `0` and `23`, inclusive.

`spec.backup.snapshotSchedule.referenceMinuteOfHour`
  *Type*: number
  
  UTC (Coordinated Universal Time) minute of the hour to schedule snapshots. You can
  set a value between `0` and `59`, inclusive.

`spec.backup.snapshotSchedule.snapshotIntervalHours`
  *Type*: number
  
  Number of hours between snapshots. You can set a value of `6`,
  `8`, `12`, or `24`.

`spec.backup.snapshotSchedule.snapshotRetentionDays`
  *Type*: number
  
  Number of days to keep recent snapshots. You can set a value 
  between `2` and `5`, inclusive.   

`spec.backup.snapshotSchedule.weeklySnapshotRetentionWeeks`
  *Type*: number
  
  Number of weeks to keep weekly snapshots. You can set a value 
  between `1` and `52`, inclusive. Setting the value to `0`
  disables this rule.

`spec.cloudManager.configMapRef.name`
  *Type*: string

  Alias for spec.opsManager.configMapRef.name.

..
  Feature for unknown future release - ER 7/13/23
  
  `spec.clusterDomain`
  
  *Type*: string
  
  *Default*: cluster.local
  
  Domain name of the Kubernetes cluster where you deploy the Kubernetes Operator. When
  Kubernetes creates a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), the Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) a
  FQDN (fully qualified domain name). To update Cloud Manager or Ops Manager, the Kubernetes Operator calculates the FQDN (fully qualified domain name) for
  each Pod using a provided cluster name. Kubernetes doesn't provide
  an API (Application Programming Interface) to query these hostnames.

  **Warning:**

  You must set `spec.clusterDomain` if your Kubernetes cluster has
  a `default domain`
  other than the default `cluster.local`. If you neither use the
  default nor set the `spec.clusterDomain` option, the
  Kubernetes Operator might not function as expected. 

`spec.clusterSpecList`
  *Type*: collection

  List of specifications for each Kubernetes cluster in a `MongoDBMultiCluster` resource.

`spec.clusterSpecList.clusterName`
  *Type*: string 

  Name of the cluster where the MongoDB Controllers for Kubernetes Operator schedules the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). When the Kubernetes Operator deploys this `MongoDBMultiCluster` resource, it creates `a service account`. This name is what the service account in the central cluster uses to communicate with the workload clusters. 

`spec.clusterSpecList.externalAccess.externalDomain`
  *Type*: string

  An external domain used to externally expose your replica set deployment.

  By default, each replica set member uses the Kubernetes Pod's FQDN (fully qualified domain name) 
  (`*.svc.cluster.local`) as the default hostname. However, if you add an
  external domain to this setting, the replica set uses a hostname that is a 
  subdomain of the specified domain instead. This hostname uses the following 
  format:

  `<replica-set-name>-<cluster-idx>-<pod-idx>.<externalDomain>`

  For example:

  `multi-replica-set-0-1.cluster-0.example.com`

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

  **Important:**

  Use this setting only when deploying a multi-Kubernetes cluster MongoDB deployment replica set *without
  a service mesh*. See multi-cluster-no-service-mesh-deploy-rs.

`spec.clusterSpecList.externalAccess.externalService`
  *Type*: collection

  Configuration for externally exposing a specific cluster in your multi-Kubernetes cluster MongoDB deployment. These settings
  override the global spec.externalAccess.externalService settings.

  When you set the spec.externalAccess setting, the Kubernetes Operator 
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

`spec.clusterSpecList.externalAccess.externalService.annotations`
  *Type*: collection

  Key-value pairs that let you add cloud provider-specific
  configuration settings to a specific cluster in your multi-Kubernetes cluster MongoDB deployment. This setting overrides the global
  setting, spec.externalAccess.externalService.annotations. 
  To learn more, see [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) and the documentation for your Kubernetes cloud provider.

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
  | `{podName}` | Equal to `{resourceName}-{clusterIndex}-{podIndex}`. |
  | `{clusterName}` | The current cluster name set in spec.clusterSpecList.clusterName. |
  | `{clusterIndex}` | The index initially assigned by the Kubernetes Operator for the current cluster name set in spec.clusterSpecList.clusterName. This value might not reflect the order of the member clusters defined in spec.clusterSpecList. Although you can change the order of member clusters in spec.clusterSpecList, the Kubernetes Operator still uses the index that it initially assigned for the current cluster name. |
  | `{statefulSetName}` | The [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). Equal to `{resourceName}-{clusterIndex}`. |
  | `{externalServiceName}` | Generated name of the external service, based on the placeholder values that you specified. Equal to `{resourceName}-{clusterIndex}-{podIndex}-svc-external`. |
  | `{mongodProcessDomain}` | The domain name of the server that is hosting the mongod process. Equal to spec.externalAccess.externalDomain if specified. Otherwise, equal to the domain used for the `mongod` process FQDN (fully qualified domain name). For example, for the process hostname `mdb-rs-1.example.com`, `example.com` is the domain name. |
  | `{mongodProcessFQDN}` | The `mongod` process hostname set in the `automation configuration`. The process hostname depends on your deployment configuration. If you've configured your multi-Kubernetes cluster MongoDB deployment to use external domains, such as for a deployment without service mesh, the process hostname uses the following format: `{resourceName}-{clusterIndex}-{podIndex}.{mongodProcessDomain}` For example: `mdb-rs-0-1.example.com` If your deployment doesn't use external domains, the process hostname uses the following format: `{resourceName}-{clusterIndex}-{podIndex}-svc.{namespace}.svc.cluster.local` For example: `mdb-rs-1-svc.ns.svc.cluster.local` |

  **Note:**

  You must use only known placeholder values as specified in the table 
  and ensure that your placeholders don't use empty or null values. Otherwise, 
  Kubernetes Operator returns an error. For example, you might
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

`spec.clusterSpecList.externalAccess.externalService.spec`
  *Type*: collection

  Configuration for the `ServiceSpec`.
  To learn more, see spec.clusterSpecList.externalAccess.externalService.

`spec.clusterSpecList.memberConfig`
  *Type*: collection

  Specification for each MongoDB replica set and its 
  members in your multi-Kubernetes cluster MongoDB deployment.

  The order of the elements in the object for each replica set
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

  

`spec.clusterSpecList.memberConfig.priority`
  *Type*: string
  
  Number that indicates the relative likelihood of a MongoDB replica set member to become the [primary](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-primary).

  * To increase the relative likelihood that a replica set member becomes the primary, specify a higher `priority` value.
   
  * To decrease the relative likelihood that a replica set member becomes the primary, specify a lower `priority` value.
   
  For example, a member with a `memberConfig.priority` of `1.5` is more likely than a member with a `memberConfig.priority` of `0.5` to become the primary. 
   
  A member with a `memberConfig.priority` of `0` is ineligible to become the primary. To learn more, see Member Priority.

`spec.clusterSpecList.memberConfig.tags`
  *Type*: map

  Map of replica set tags for directing
  read and write operations to specific members of your MongoDB replica set.

`spec.clusterSpecList.memberConfig.votes`
  *Type*: number

  Determines whether a MongoDB replica set member can vote in an election. Set to `1` to allow the member to vote. Set to `0` to exclude the member from an election. 

`spec.clusterSpecList.members`
  *Type*: number

  Number of members in the MongoDB replica set.

`spec.clusterSpecList.service`
  *Type*: string

  *Default*: <resource_name>+"-service"

  Name of the Kubernetes service you want to create or use for a
  [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). If a service with this name already exists, the
  MongoDB Controllers for Kubernetes Operator does not delete or recreate it. This setting lets
  you create your own custom services and lets the Kubernetes Operator
  reuse them.

`spec.clusterSpecList.statefulSet.spec`
  *Type*: collection

  Provides the configuration for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) override for each of
  the cluster's StatefulSets in a multi-Kubernetes cluster MongoDB deployment. To set the global configuration that
  applies to all clusters in your multi-Kubernetes cluster MongoDB deployment, see spec.statefulSet.spec.

  This setting applies only to replica set resource types in multi-Kubernetes cluster MongoDB deployments.

`spec.connectivity.replicaSetHorizons`
  *Type*: collection

  Allows you to provide different DNS (Domain Name System) settings for client
  applications and the MongoDB Agents. The Kubernetes Operator uses split
  horizon DNS (Domain Name System) for replica set members. This feature allows
  communication both within the Kubernetes cluster and from outside Kubernetes.

  You can add multiple external mappings per host.

  **Note:**

  - Make sure that each value in this array is unique.

  - Make sure that the number of entries in this array matches the
    value given in spec.clusterSpecList.members.

  - Provide a value for the
    spec.security.certsSecretPrefix setting to
    enable TLS (Transport Layer Security). This method to use split horizons requires the
    Server Name Indication extension of the TLS (Transport Layer Security) protocol.

  - Configure the routing for external hostnames.

  In this example, clients communicate with the replica set using the `example-website`
  horizon.

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

`spec.duplicateServiceObjects`
  *Type*: boolean

  *Default*: true

  Specifies whether the Kubernetes Operator duplicates a Pod's service mesh object in each cluster to allow DNS (Domain Name System) resolution. Set to `false` if you configure a DNS proxy for your service mesh. For example, see [DNS Proxying](https://istio.io/latest/docs/ops/configuration/traffic-management/dns-proxy/) in the Istio  documentation. 

`spec.externalAccess`
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

`spec.externalAccess.externalService`
  *Type*: collection

  Specification for overriding the default values in `spec.externalAccess`.

  When you set the spec.externalAccess setting, the Kubernetes Operator 
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

`spec.externalAccess.externalService.annotations`
  *Type*: collection

  Key-value pairs that let you add cloud provider-specific
  configuration settings to all clusters in your multi-Kubernetes cluster MongoDB deployment. For cluster-specific overrides,
  see spec.clusterSpecList.externalAccess.externalService.annotations.
  To learn more, see 
  [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) and the documentation for the cloud provider you use 
  for Kubernetes deployments.

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
  | `{podName}` | Equal to `{resourceName}-{clusterIndex}-{podIndex}`. |
  | `{clusterName}` | The current cluster name set in spec.clusterSpecList.clusterName. |
  | `{clusterIndex}` | The index initially assigned by the Kubernetes Operator for the current cluster name set in spec.clusterSpecList.clusterName. This value might not reflect the order of the member clusters defined in spec.clusterSpecList. Although you can change the order of member clusters in spec.clusterSpecList, the Kubernetes Operator still uses the index that it initially assigned for the current cluster name. |
  | `{statefulSetName}` | The [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). Equal to `{resourceName}-{clusterIndex}`. |
  | `{externalServiceName}` | Generated name of the external service, based on the placeholder values that you specified. Equal to `{resourceName}-{clusterIndex}-{podIndex}-svc-external`. |
  | `{mongodProcessDomain}` | The domain name of the server that is hosting the mongod process. Equal to spec.externalAccess.externalDomain if specified. Otherwise, equal to the domain used for the `mongod` process FQDN (fully qualified domain name). For example, for the process hostname `mdb-rs-1.example.com`, `example.com` is the domain name. |
  | `{mongodProcessFQDN}` | The `mongod` process hostname set in the `automation configuration`. The process hostname depends on your deployment configuration. If you've configured your multi-Kubernetes cluster MongoDB deployment to use external domains, such as for a deployment without service mesh, the process hostname uses the following format: `{resourceName}-{clusterIndex}-{podIndex}.{mongodProcessDomain}` For example: `mdb-rs-0-1.example.com` If your deployment doesn't use external domains, the process hostname uses the following format: `{resourceName}-{clusterIndex}-{podIndex}-svc.{namespace}.svc.cluster.local` For example: `mdb-rs-1-svc.ns.svc.cluster.local` |

  **Note:**

  You must use only known placeholder values as specified in the table 
  and ensure that your placeholders don't use empty or null values. Otherwise, 
  Kubernetes Operator returns an error. For example, you might
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

`spec.externalAccess.externalService.spec`
  *Type*: collection

  Configuration for the `ServiceSpec`.
  To learn more, see spec.externalAccess.externalService.

`spec.featureCompatibilityVersion`
  *Type*: number

  Limits changes to data that occur with an upgrade to a
  new major version. This allows you to downgrade to the previous major
  version. To learn more about feature compatibility, see `setFeatureCompatibilityVersion`
  in the MongoDB Manual.

`spec.logLevel`
  *Type*: string

  Configures the level of Automation Agent logging inside the
  [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/). Accepted values include:

  - `DEBUG`
  - `INFO`
  - `WARN`
  - `ERROR`
  - `FATAL`

`spec.opsManager.configMapRef.name`
   *Type*: string

   Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Cloud Manager or Ops Manager connection
   configuration. The spec.cloudManager.configMapRef.name
   setting is an alias for this setting and can be used in its place.

   This value must exist on the *same* namespace as the resource
   you want to create.

   **Important:** Operator manages changes to the ConfigMap

   The Kubernetes Operator tracks any changes to the ConfigMap and
   reconciles the state of the `MongoDB` resource.

`spec.persistent`
  *Type*: boolean  
  
  *Default*: true

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

`spec.security.authentication`
  *Type*: collection

  Authentication specifications for your multi-Kubernetes cluster MongoDB deployment.

`spec.security.authentication.agents`
  *Type*: collection

  MongoDB Agent authentication configuration for the Cloud Manager or Ops Manager project.

`spec.security.authentication.agents.automationLdapGroupDN`
  *Type*: string

  The Distinguished Name (DN) of the LDAP group to which the
  MongoDB Agent user belongs.
  
  This setting is required if:

  - spec.security.authentication.ldap.authzQueryTemplate is
    present, and
  - spec.security.authentication.agents.mode is `LDAP` or
    `X509`.

`spec.security.authentication.agents.automationPasswordSecretRef`
  *Type*: collection

  Details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the
  spec.security.authentication.agents.automationUserName
  user.

  This setting is required if 
  spec.security.authentication.agents.mode is `LDAP`.

`spec.security.authentication.agents.automationPasswordSecretRef.key`
  *Type*: string

  Key in the
  spec.security.authentication.agents.automationPasswordSecretRef.name
  [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the user in
  spec.security.authentication.agents.automationUserName.

  This setting is required if 
  spec.security.authentication.agents.mode is
  `LDAP`.

`spec.security.authentication.agents.automationPasswordSecretRef.name`
  *Type*: string

  Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password for the
  spec.security.authentication.agents.automationUserName
  user. You must create this secret in the same namespace to which you
  deploy the Kubernetes Operator:

  ```sh
  kubectl create secret generic ldap-agent-user \
  --from-literal="password=<password>" -n <metadata.namespace>
  ```

  This secret must contain one key, the value of which matches the
  password of the
  spec.security.authentication.agents.automationUserName user
  in your LDAP deployment.

  This setting is required if 
  spec.security.authentication.agents.mode is `LDAP`.

`spec.security.authentication.agents.automationPasswordSecretRef.optional`
  *Type*: boolean

  Specifies whether these options are required or optional:

  - spec.security.authentication.agents.automationPasswordSecretRef.key
  - spec.security.authentication.agents.automationPasswordSecretRef.name

`spec.security.authentication.agents.automationUserName`
  *Type*: string

  Name of the user that the MongoDB Agents use to interact with your
  multi-Kubernetes cluster MongoDB deployment. The username is mapped to an LDAP Distinguished
  Name (DN) according to
  spec.security.authentication.ldap.userToDNMapping. The
  resulting DN must already exist in your LDAP deployment.

  This setting is required if 
  spec.security.authentication.agents.mode is `LDAP`.

`spec.security.authentication.agents.clientCertificateSecretRef.name`
  *Type*: string

  *Default*: agent-certs

  Specifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the MongoDB Agent\'s
  TLS (Transport Layer Security) certificate.
 
  This secret must contain the `mms-automation-agent-pem` key. The
  value of this key must be a TLS (Transport Layer Security) certificate that can be validated
  by the server.

  You must create this secret in the same namespace to which you
  deploy the Kubernetes Operator:

  ```sh
  kubectl create secret generic agent-certs \
  --from-file=mms-automation-agent-pem=<automation-cert.pem> \
  --namespace=<metadata.namespace>
  ```

`spec.security.authentication.enabled`
  *Type*: boolean

  *Default*: false

  Specifies whether authentication is enabled on the Cloud Manager or Ops Manager
  project. If set to `true`, you must set an authentication mechanism in spec.security.authentication.modes.

  **Important:**

  The Kubernetes Operator manages authentication for this MongoDB
  resource if you include this setting, even if it is set to
  `false`. You can't configure authentication for this
  resource using the Cloud Manager or Ops Manager user interface or APIs while this
  setting exists in the resource specification.

  Omit this setting if you want to manage authentication using the
  Cloud Manager or Ops Manager user interface or APIs.

`spec.security.authentication.agents.mode`
  *Type*: string

  The authentication mechanism that the MongoDB Agents for
  your multi-Kubernetes cluster MongoDB deployment use. Valid values are `SCRAM`, `SCRAM-SHA-1`, `MONGODB-CR`, `X509`, and `LDAP`.
  The value you specify must also be present in
  spec.security.authentication.modes.
  We recommend `SCRAM-SHA-256 (SCRAM)` over `SCRAM-SHA-1`. If you specify `SCRAM-SHA-1`, you must also specify `MONGODB-CR`.

  This setting is required if you specified more than one value for
  spec.security.authentication.modes.

`spec.security.authentication.ignoreUnknownUsers`
  *Type*: boolean

  *Default*: false
   
  Determines whether you can modify database users that were not
  configured through the Kubernetes Operator, or the Cloud Manager or Ops Manager user interface.
  
  To manage database users directly through the `mongod` or `mongos`, set to `true`.

`spec.security.authentication.internalCluster`
  *Type*: string

  Specifies whether X.509 internal cluster authentication is enabled.

  To enable X.509 internal cluster authentication, set to `"X509"`.
  Requires that the following settings be specified:
  
  - spec.security.authentication.modes `: ["X509"]`
  - spec.security.certsSecretPrefix

  The Kubernetes Operator accepts the following values:

  - `["X509"]`: X.509 internal cluster authentication is enabled.
  - `""` or omitted: internal cluster authentication is not enabled.

  **Important:**

  After you enable internal cluster authentication, you can't disable it.

`spec.security.authentication.ldap`
  *Type*: collection

  *Required for LDAP authentication.* 

  Configures LDAP (Lightweight Directory Access Protocol) authentication for the Cloud Manager or Ops Manager project. To enable LDAP (Lightweight Directory Access Protocol) authentication, set
  spec.security.authentication.modes to `["LDAP"]`.

`spec.security.authentication.ldap.authzQueryTemplate`
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
        (*Available starting in MongoDB version 4.2*).

  For more details, see LDAP Query Templates in the MongoDB Manual.

`spec.security.authentication.ldap.bindQueryPasswordSecretRef`
  *Type*: collection

  *Required for LDAP authentication.* 
  
  Specifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password with which
  MongoDB binds when connecting to the LDAP (Lightweight Directory Access Protocol) server.

`spec.security.authentication.ldap.bindQueryPasswordSecretRef.name`
  *Type*: string

  *Required for LDAP authentication.* 
  
  Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the password with which MongoDB
  binds when connecting to the LDAP (Lightweight Directory Access Protocol) server.
  
  The [secret](https://kubernetes.io/docs/concepts/configuration/secret/) must contain only one `password` field which stores
  the password.

`spec.security.authentication.ldap.bindQueryUser`
  *Type*: string

  *Required for LDAP authentication.* 
  
  LDAP (Lightweight Directory Access Protocol) Distinguished Name to which MongoDB binds when connecting to
  the LDAP (Lightweight Directory Access Protocol) server.

`spec.security.authentication.ldap.caConfigMapRef`
  *Type*: collection

  *Required for LDAP authentication with TLS.* 
  
  [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a CA (Certificate Authority) which validates the LDAP (Lightweight Directory Access Protocol) 
  server's TLS (Transport Layer Security) certificate.

`spec.security.authentication.ldap.caConfigMapRef.key`
  *Type*: string

  *Required for LDAP authentication with TLS.* 
  
  Field name that stores the CA (Certificate Authority) which validates the LDAP (Lightweight Directory Access Protocol)
  server's TLS (Transport Layer Security) certificate.

`spec.security.authentication.ldap.caConfigMapRef.name`
  *Type*: string

  *Required for LDAP authentication with TLS.* 
  
  Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that contains a CA (Certificate Authority) which validates
  the LDAP (Lightweight Directory Access Protocol) server's TLS (Transport Layer Security) certificate.

`spec.security.authentication.ldap.caConfigMapRef.optional`
  *Type*: boolean

  Specifies whether these options are required or optional:

  - spec.security.authentication.ldap.caConfigMapRef.key
  - spec.security.authentication.ldap.caConfigMapRef.name

`spec.security.authentication.ldap.servers`  
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

`spec.security.authentication.ldap.timeoutMS`
  *Type*: integer

  Specifies how many milliseconds an authentication request should 
  wait before timing out.

`spec.security.authentication.ldap.transportSecurity`
  *Type*: string

  *Required for LDAP authentication.* 
  
  Specifies whether the LDAP (Lightweight Directory Access Protocol) server accepts TLS (Transport Layer Security).
  
  If the LDAP (Lightweight Directory Access Protocol) server accepts TLS (Transport Layer Security), set the value to `tls`. If 
  the LDAP (Lightweight Directory Access Protocol) server doesn't accept TLS (Transport Layer Security), leave this value blank or set 
  the value to `none`.

  **Note:**

  If you specify a string other than `none` or `tls`, 
  Kubernetes Operator still sets the setting to `tls`.

`spec.security.authentication.ldap.userCacheInvalidationInterval`
  *Type*: integer
   
  Specifies how many seconds MongoDB waits to flush the LDAP (Lightweight Directory Access Protocol) user 
  cache. Defaults to 30 seconds.

`spec.security.authentication.ldap.userToDNMapping`
  *Type*: string

  Maps the username provided to `mongod` or
  `mongos` for authentication to an LDAP Distinguished Name
  (DN).

  For more details, see security.ldap.userToDNMapping in the MongoDB Manual.

`spec.security.authentication.modes`
  *Type*: array

  Specifies the authentication mechanism that your multi-Kubernetes cluster MongoDB deployment uses. Valid values are `SCRAM`, `SCRAM-SHA-1`, `MONGODB-CR`, `X509`, and `LDAP`. We recommend `SCRAM-SHA-256 (SCRAM)` over `SCRAM-SHA-1`. If you specify `SCRAM-SHA-1`, you must also specify `MONGODB-CR`.

  **Note:**

  To enable X.509 internal cluster authentication for the Cloud Manager or Ops Manager project, set this
  value to `["X509"]` and specify the following settings:

  - spec.security.authentication.internalCluster `: "X509"`
  - provide a value for the spec.security.certsSecretPrefix setting.

  If you provide more than one value for
  `spec.security.authentication.modes`, you must also specify a
  value for spec.security.authentication.agents.mode.

`spec.security.authentication.requireClientTLSAuthentication`
  *Type*: boolean

  *Default*: false

  Specifies whether the MongoDB host requires clients to connect using a
  TLS (Transport Layer Security) certificate. Defaults to `true` if you enable TLS (Transport Layer Security)
  authentication.
  
  To enable TLS (Transport Layer Security) authentication, provide a value for the
  spec.security.certsSecretPrefix setting.

`spec.security.certsSecretPrefix`
  *Type*: string

  Text to prefix to the Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that you
  created that contain your replica set's TLS (Transport Layer Security) 
  keys and certificates.

  You must prefix your secrets with `<prefix>-<metadata.name>`.

  For example, if you call your deployment `my-deployment` and you set
  the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the
  client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, 
  you must name the TLS (Transport Layer Security) secret for internal cluster authentication 
  (if enabled) `mdb-my-deployment-clusterfile`.

  To learn more about naming the secrets that contain your TLS (Transport Layer Security) 
  certificates, see the topic in multi-cluster-secure-tls that applies to your 
  deployment.

`spec.security.roles`
  *Type*: array

  Array that defines User-defined roles that give you
  fine-grained access control over your multi-Kubernetes cluster MongoDB deployment.

  To enable user-defined roles, the
  spec.security.authentication.enabled must be `true`.

  **Example:**

  In this example, a user-defined role named `customRole` allows
  users assigned this role to:

  - Insert documents into the `cats` collection in the `pets`
    database, and
  - Find and insert documents into the `dogs` collection in the
    `pets` database.

  ```yaml
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

`spec.security.roles.authenticationRestrictions`
  *Type*: array
   
  Array that defines the IP address from and to which users
  assigned this spec.security.roles.role can
  connect.

`spec.security.roles.authenticationRestrictions.clientSource`
  *Type*: array
 
  Array of IP addresses or CIDR blocks from which users assigned this
  spec.security.roles.role can connect. 

  MongoDB servers reject connection requests from users with this role
  if the requests come from a client that is not present in this array.

`spec.security.roles.authenticationRestrictions.serverAddress`
  *Type*: array

  Array of IP addresses or CIDR blocks to which users assigned this
  spec.security.roles.role can connect. 

  MongoDB servers reject connection requests from users with this role
  if the client requests to connect to a server that is not present in
  this array.

`spec.security.roles.db`
  *Type*: string

  The database in which to store the user-defined role.

  **Example:**

  `admin`

`spec.security.roles.privileges`
  *Type*: array

  Array that describes the privileges that users granted this role
  possess.

`spec.security.roles.privileges.actions`
  *Type*: array

  List of actions that users granted this role can perform. For a list
  of accepted values, see Privilege Actions in the
  MongoDB Manual for the MongoDB versions you deploy with the
  Kubernetes Operator.

`spec.security.roles.privileges.resource`
  *Type*: collection

  Resources for which the privilege
  spec.security.roles.privileges.actions
  apply.

  This collection must include either:

  - The spec.security.roles.privileges.resource.db and spec.security.roles.privileges.resource.collection settings, or
  - The spec.security.roles.privileges.resource.cluster setting with a value of `true`.

`spec.security.roles.privileges.resource.cluster`
  *Type*: boolean

  *Default*: false

  Flag that indicates that the privilege
  spec.security.roles.privileges.actions
  apply to all databases and collections in the MongoDB deployment.

  If set to true, do not provide values for
  spec.security.roles.privileges.resource.db
  and 
  spec.security.roles.privileges.resource.collection.

`spec.security.roles.privileges.resource.collection`
  *Type*: string

  Collection in the
  spec.security.roles.privileges.resource.db
  for which the privilege
  spec.security.roles.privileges.actions
  apply.

  If you provide a value for this setting, you must also provide a value
  for
  spec.security.roles.privileges.resource.db.

`spec.security.roles.privileges.resource.db`
  *Type*: string

  Database for which the privilege
  spec.security.roles.privileges.actions
  apply.

  If you provide a value for this setting, you must also provide a value
  for
  spec.security.roles.privileges.resource.collection.

`spec.security.roles.role`
  *Type*: string
   
  Name of the user-defined role.

`spec.security.tls.additionalCertificateDomains`
  *Type*: collection
  
  List of every domain that should be added to TLS (Transport Layer Security) certificates to
  each Pod in this deployment. When you set this parameter, every CSR (Certificate Signing Request)
  that the Kubernetes Operator transforms into a TLS (Transport Layer Security) certificate includes
  a SAN (Subject Alternative Name) in the form `<pod name>.<additional cert domain>`.

  Replica set resources don't need this parameter. Use
  spec.connectivity.replicaSetHorizons instead.

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

`spec.security.tls.ca`
  *Type*: string

  Provide the name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) that stores the CA (Certificate Authority).

  **Important:**

  If you use a custom CA (Certificate Authority) to sign your TLS (Transport Layer Security) certificates for
  the `MongoDBMultiCluster` resource, you must specify this parameter.

  The Kubernetes Operator requires that you name the certificate for the
  `MongoDBMultiCluster` resource `ca-pem` in the ConfigMap.

`spec.security.tls.enabled`
  *Type*: boolean

  **Important:**

  `spec.security.tls.enabled` is deprecated
  and will be removed in a future Kubernetes Operator release. To enable TLS (Transport Layer Security), provide a value for 
  the spec.security.certsSecretPrefix setting.

  Encrypts communications using TLS certificates between:

  - MongoDB hosts in a replica set or sharded cluster configuration
  - Clients (`mongo` shell, drivers, `MongoDB Compass`, and others) and the MongoDB deployment

`spec.statefulSet.spec`
  *Type*: collection

  Global specification for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
  for your multi-Kubernetes cluster MongoDB deployment.

  To review which fields you can add to
  `spec.statefulSet.spec`, see
  `StatefulSetSpec v1 apps`
  in the Kubernetes documentation.
