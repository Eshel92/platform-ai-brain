<!-- Part 5 of 5 of reference/k8s-operator-om-specification.md (split because the page is big). -->

## Multi-Cluster Settings

### Ops Manager Required Settings

This section describes settings that you must use for your 
multi-cluster Ops Manager deployment in addition to the required Ops Manager settings.

**`spec.clusterSpecList.members`**

*Type*: integer

*Conditional*. The number of Ops Manager members in the Ops Manager cluster
in a multi-Kubernetes cluster MongoDB deployment. When you set `spec.topology` to
`MultiCluster`, you must specify the value for this parameter.
Omit this parameter for single-cluster deployments.
If you set this parameter to zero, this removes this Ops Manager
member cluster from the list
of member clusters in the multi-Kubernetes cluster of Ops Manager
instances.

**`spec.topology`**

*Type*: string

The type of the Kubernetes deployment for the Ops Manager Resource.

- The values are `SingleCluster` or `MultiCluster`. If omitted,
  the default value is `SingleCluster`.
- If you specify `MultiCluster`:

  - Add the
    `MongoDBMultiCluster` resource to the watched resources list. This indicates to
    the Kubernetes Operator that it should work in multi-Kubernetes cluster mode
    and perform configuration actions required for handling
    multi-Kubernetes resources.

  - Specify at least one member cluster on which you want to deploy
    Ops Manager, using `spec.clusterSpecList` and its nested
    `spec.clusterSpecList.clusterName` and
    `spec.clusterSpecList.members` parameters.

  - If you specify `MultiCluster`, the Kubernetes Operator ignores any
    values that you set for `spec.members`.
    See the example of the resource specification.

### Ops Manager Optional Settings

Ops Manager resources can also use the following settings specific to 
multi-cluster Ops Manager deployment\s:

**`spec.clusterSpecList`**

*Type*: collection

*Conditional*. Details of selected Kubernetes member clusters in a multi-Kubernetes
cluster where you intend to deploy Ops Manager or Backup Daemon instances.
See also the example of the resource specification.

- When you set `spec.topology` to `MultiCluster`, you must
  specify the value for `spec.clusterSpecList.members`. All
  other parameters under `spec.clusterSpecList` are optional.

- When you set `spec.topology` to `SingleCluster`,
  the Kubernetes Operator ignores all parameters under `spec.clusterSpecList`.

**`spec.clusterSpecList.clusterName`**

*Type*: string

*Optional*. Name of the member Kubernetes cluster in a multi-Kubernetes cluster MongoDB deployment where
the MongoDB Controllers for Kubernetes Operator schedules the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) for Ops Manager or the Backup
Daemon.

**`spec.clusterSpecList.clusterDomain`**

*Type*: string

*Optional*. An override for `spec.clusterDomain` for the specific
Ops Manager member cluster. If you omit this value, defaults to the value
set in `spec.clusterDomain`.
Kubernetes assigns each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) a FQDN (fully qualified domain name). The Kubernetes Operator
calculates the FQDN (fully qualified domain name) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) using a provided `clusterDomain`
value. Kubernetes doesn't provide an API (Application Programming Interface) to query these hostnames.

**`spec.clusterSpecList.configuration`**

*Type*: collection

*Optional*. Ops Manager configuration properties that override properties
you set in `spec.configuration` for the specific cluster.
See `Ops Manager Configuration Settings` for property names and descriptions.
Each property takes a value of type `string`. For example, setting
these properties allows you to change environment variables that you
must pass to Ops Manager and the Backup Daemon in that particular member
cluster.

If you omit specifying values, defaults to the values
set in `spec.configuration`.

**`spec.clusterSpecList.jvmParameters`**

*Type*: array of strings

*Optional*. JVM (Java Virtual Machine) parameters passed to the Ops Manager and Backup Daemon
instances for this member cluster.

- If you specify this parameter, its values override the values specified
  in `spec.jvmParameters`. For example values,
  see the example of the resource specification.
- If you omit this parameter, values from the `spec.jvmParameters`
  are used for the Ops Manager and Backup Daemon instances in this member cluster.

**`spec.clusterSpecList.externalConnectivity`**

*Type*: collection

*Optional*. Configuration object that enables external connectivity to
Ops Manager for the specific cluster. This is an override for
`spec.externalConnectivity` for the specific cluster.

Specify values for this parameter to change how the Ops Manager application is
exposed externally in different clusters. For example, if you deploy Ops Manager
on Kubernetes nodes across different cloud providers, you might be required
to specify cloud proviver-specific values for this parameter.

If you set this parameter:

- The Kubernetes Operator doesn't use `spec.externalConnectivity` values
  for this member Ops Manager cluster.
- The Kubernetes Operator creates a Kubernetes `service`,
  named `<om-name>-svc-ext`, that allows traffic originating from outside of the Kubernetes cluster
  to reach the Ops Manager application on this member cluster.

If you omit this parameter, the Kubernetes Operator uses values from `spec.externalConnectivity`
for this member cluster.

**`spec.clusterSpecList.statefulSet.spec`**

*Type*: collection

*Optional*. Specification for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that the MongoDB Controllers for Kubernetes Operator creates
for a specific member cluster in the multi-Kubernetes cluster Ops Manager deployment.
This parameter is an override for `spec.statefulSet.spec`.
If you omit it, the Kubernetes Operator uses the values from `spec.statefulSet.spec`.
For example, you can use this parameter to specify different storage
values for each of your Ops Manager clusters in the multi-Kubernetes cluster MongoDB deployment.

To review which fields you can add to `spec.clusterSpecList.statefulSet.spec`, see
`StatefulSetSpec v1 apps`
in the Kubernetes documentation.

**`spec.clusterSpecList[*].backup`**

*Optional*. Backup settings that override values specified under
`spec.backup` for that particular member cluster.

- You can set these values only if `spec.backup.enabled` is
  set to `true`.

- If you omit setting any values for this parameter, they default to values
  specified in settings under `spec.backup`.

- Not all backup settings are supported in this override. You can't override
  the following backup settings because they apply globally to all member
  clusters, if specified under `spec.backup`:

  - `externalServiceEnabled`
  - `headDB`
  - `opLogStores`
  - `blockStores`
  - `s3Stores`
  - `fileSystemStores`
  - `queryableBackupSecretRef`
  - `encryption`

**`spec.clusterSpecList[*].backup.members`**

*Type*: integer

*Optional*. Override for `spec.backup.members`. The number of
Backup Daemon instances to deploy in this cluster. if you omit this value
or provide a value of `0`, the Kubernetes Operator won't deploy Backup Daemon
instances in a particular member cluster.

**`spec.clusterSpecList[*].backup.assignmentLabels`**

*Type*: array of strings

*Optional*. Override for `spec.backup.assignmentLabels`.
If specified, the Kubernetes Operator uses the values you specify in this override for all
Backup Daemon instances in a particular member cluster. If you omit values
for this parameter, the values default to those specified in `spec.backup.assignmentLabels`
for all Backup Daemon instances in a member cluster.

**`spec.clusterSpecList[*].backup.jvmParameters`**

*Type*: array of strings

*Optional*. Override for `spec.backup.jvmParameters`. Allows
you to customize the JVM (Java Virtual Machine) value for Backup Daemon instances in a
particular member cluster.

**`spec.clusterSpecList[*].backup.statefulSet`**

*Type*: string

*Optional*. Override for `spec.backup.statefulSet.spec`.
Allows you to customize the values for a Backup Daemon in a particular
member cluster. To review which fields you can add to
`spec.clusterSpecList[*].backup.statefulSet`, see
`StatefulSetSpec v1 apps`
in the Kubernetes documentation.

### Application Database Required Settings

This section describes settings specific to your 
multi-cluster Ops Manager deployment that you must use for your Application Database.

**`spec.applicationDatabase.clusterSpecList`**

*Type*: collection

Details of selected Kubernetes member clusters in a multi-Kubernetes cluster MongoDB deployment
that serve as nodes that host the Application Database.

**`spec.applicationDatabase.clusterSpecList.clusterName`**

*Type*: string

Name of the member Kubernetes cluster in a multi-Kubernetes cluster MongoDB deployment where the MongoDB Controllers for Kubernetes Operator
schedules the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) for the Application Database.

**Important:**

You can't convert a single cluster Ops Manager instance to a
multi-Kubernetes cluster MongoDB deployment instance by modifying the
`topology` and
the `clusterSpecList`
settings in the CRD.

**`spec.applicationDatabase.clusterSpecList.members`**

*Type*: number

Number of statefulSet nodes in the given member cluster. The member cluster
is one of the member clusters that hosts the Application Database in
a multi-Kubernetes cluster MongoDB deployment.

**`spec.applicationDatabase.topology`**

*Type*: string

The type of the Kubernetes deployment for the Application Database.

- The values are `SingleCluster` or `MultiCluster`. If omitted,
  the default value is `SingleCluster`.
- If you specify `MultiCluster`, you must specify at least one member
- cluster on which you want to deploy the Application Database using
  the `clusterSpecList`,
  `clusterName`, 
  `members`
  parameters.

- If you specify `MultiCluster`, the Kubernetes Operator ignores values
  that you set for the `spec.applicationDatabase.members`
  field.

To learn more, see the example of the multi-cluster resource specification.

### Application Database Optional Settings

This section describes settings specific to your 
multi-cluster Ops Manager deployment that you can use for your Application Database.

**`spec.applicationDatabase.clusterSpecList.externalAccess`**

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

**Important:**

Use this setting only when deploying a Application Database deployment *without
a service mesh*. See reference-architectures-multi-cluster-ops-manager-no-mesh.

**`spec.applicationDatabase.clusterSpecList.memberConfig`**

*Type*: array of strings

Specification for each Application Database replica set member in your multi-cluster Ops Manager deployment.

**Important:**

If you set `spec.topology` to `SingleCluster`, use 
`spec.applicationDatabase.memberConfig` instead of `spec.applicationDatabase.clusterSpecList.memberConfig`.      

The number of elements in the `memberConfig` list must equal 
`spec.applicationDatabase.clusterSpecList.members`.

The order of the elements in the `memberConfig` list must reflect the order 
of members in the replica set. For example, the first element of the array 
affects the Pod at index `0`, the second element affects index `1`, and so on.

**Example:**

Consider the following example specification for a 
three-member replica set for the Application Database:

```yaml
spec:
  replicas: 3
  version: 8.0.0
  backup:
    enabled: true
  storage:
    resources:
      requests:
        storage: 10Gi
      storageClassName: standard
  applicationDatabase:
    clusterSpecList:
      - name: appdb
        members: 3
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

**`spec.applicationDatabase.clusterSpecList.memberConfig.priority`**

*Type*: string

Number that indicates the relative likelihood of an Application Database replica 
set member to become the 
[primary](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-primary).

* To increase the relative likelihood that a replica set member becomes the 
  primary, specify a higher `priority` value.

* To decrease the relative likelihood that a replica set member becomes the 
  primary, specify a lower `priority` value.

For example, a member with a `memberConfig.priority` of `1.5` is more 
likely than a member with a `memberConfig.priority` of `0.5` to become the 
primary. 

A member with a `memberConfig.priority` of `0` is ineligible to become the 
primary. To learn more, 
see Member Priority.

**`spec.applicationDatabase.clusterSpecList.memberConfig.tags`**

*Type*: map

Map of replica set tags 
for directing read and write operations to specific members of your Application Database replica set.

**`spec.applicationDatabase.clusterSpecList.memberConfig.votes`**

*Type*: number

Determines whether an Application Database replica set member can vote in an 
election. Set to `1` 
to allow the member to vote. Set to `0` to exclude the member from an election.
