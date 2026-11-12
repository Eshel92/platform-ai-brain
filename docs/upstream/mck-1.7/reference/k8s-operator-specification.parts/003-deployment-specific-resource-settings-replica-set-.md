<!-- Part 3 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

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
