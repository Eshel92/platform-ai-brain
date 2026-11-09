<!-- Converted from multi-cluster-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Sharded Cluster

You can distribute MongoDB Sharded Clusters over 
multiple Kubernetes Clusters. With multi-cluster functionality, you can:

- Improve the resilience of your deployment by distributing it across multiple 
  Kubernetes clusters, each in a different geographic region. 
- Configure your deployment for geo sharding by deploying primary nodes of 
  specified shards in different Kubernetes clusters that are located closer to the 
  application or clients that depend on that data, reducing latency.  
- Tune your deployment for improved performance. For example, you can deploy 
  read-only analytical nodes for all or specified shards in different 
  Kubernetes clusters or with customized resource allocations.

Additionally, you can configure shard, mongos, and config server details at 
different levels. This means that you can define a top-level, default 
configuration for shards, config server and mongos, and customize them for 
each Kubernetes cluster independently. Additionally, it is possible to customise 
individual shards to suit your specific needs. 

**Important:**

The multi-cluster sharded cluster functionality makes it possible to deploy
MongoDB resources across multiple Kubernetes clusters in multiple geographic regions; 
however, doing so will likely increase latency for replication operations.

To learn more about the specific configuration options for the multi-cluster 
sharded cluster topology, see the sharded cluster reference.

## Limitations

- Hashicorp Vault support is not available for Kubernetes Secret injection.
- The Kubernetes Operator doesn't automatically shift resources from failed Kubernetes 
  clusters into healthy ones. In case of a member cluster failure, you must redistribute
  resources across remaining healthy Kubernetes clusters manually by
  updating the CRD resource deployed to the central cluster.
- In case of a member cluster failure, you must first manually scale down failed 
  clusters to zero to remove unhealthy processes. Then you can redistribute resources 
  across remaining healthy Kubernetes clusters manually by updating the CRD 
  resource deployed to the central cluster. See Disaster Recovery 
  to learn more.

## Prerequisites

- Prepare your Kubernetes clusters for a multi-cluster deployment.
  
  - Install and configure the Kubernetes Operator for multi-cluster deployments in one of your Kubernetes clusters. 
  - Option 1: Deploy a service mesh across member clusters. 
    You can find a detailed procedure in steps 1 - 6 of the Ops Manager Multi-Cluster Deployment Guide. 
    Note that this procedure is opinionated, and only one of many possible configurations. 
  - Option 2: Configure your Kubernetes clusters for a non-service mesh deployment.

- Deploy a config map with Ops Manager or Cloud Manager and 
  MongoDB project details to your central cluster, which Kubernetes Operator 
  requires to deploy the MongoDB database resource.
- Create credentials for Ops your Manager or Cloud Manager instance and your 
  MongoDB organization and project. 

## Example Sharded Cluster Deployment

When applied to your central cluster, the example below deploys a sharded 
MongoDB cluster with 3 shards that are configured as follows:

- Each shard has nodes distributed over all Kubernetes clusters (1 node per cluster).
  
- By default each shard's Replica Set:
  
  - Has 3 voting members in total deployed across 3 clusters (1 node in each cluster)
  - The primary shard is preferred to be in `kind-e2e-cluster-1`.
  
- With a `shardOverride` for shard `sc-0`, we change the default values (specified in `spec.shard`) to the following:
  
  - 5 members in total
  - 2 members in `kind-e2e-cluster-1`
  - 2 members in `kind-e2e-cluster-2`
  - 1 member in `kind-e2e-cluster-3`
  - When possible, the primary shard is preferred to be in `kind-e2e-cluster-2`

- Customized default storage settings for all shards in all clusters as defined in `spec.shardPodSpec`
- A Config Server Replica Set with 3 members, with 1 member in each cluster
- 3 mongos instances deployed in total, with 1 instance in each cluster

The default configuration consists of three shards, each with
one member on each of the three clusters, for a total of three members per shard. 
But in the overrides we change shard `sc-0` to have five members, two on cluster 
`1`, two on cluster `2`, and cluster `3` still has one shard as per the 
default. 

**Note:** Only unidirectional scaling is supported.

When you scale shard, config server, or mongos replicas you can only scale 
resources up or down in order to ensure the correctness of scaling. This rule 
applies to both single Kubernetes cluster deployments and those that are 
distributed across multiple Kubernetes clusters. Additionally, in multi-cluster 
deployments the unidirectional scaling rule applies to all resource types.
For example, you can't add more nodes (scaling up) to shards while simultaneously 
removing (scaling down) config servers or mongos. You can no longer "move" one 
node from one cluster to another without changing the total number of members. 
Rather, you must first perform a scale-up operation and then execute a separate 
change for scaling down. 

This example configuration also shifts (with `shardOverrides`) the primary to cluster `2`, 
for the shard `sc-0`, which can reduce latency for users operating in the region where  cluster `2` 
is located. In this way, you still have resilience across the clusters 
(and their regions), but if the data in shard `0` is data most relevant to the 
users in in which cluster `2` is deployed, they'll experience lower latency.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: sc
spec:
  topology: MultiCluster
  type: ShardedCluster
  # this deployment will have 3 shards
  shardCount: 3
  # you cannot specify mongodsPerShardCount, configServerCount and mongosCount
  # in MultiCluster topology
  version: 8.0.3
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  persistent: true

  shardPodSpec: # applies to all shards on all clusters
    persistence:
      single:
        # all pods for all shards on all clusters will use that storage size in their
        # PersistentVolumeClaim unless overridden in spec.shard.clusterSpecList or
        # spec.shardOverrides.
        storage: 10G

  configSrvPodSpec: # applies to all config server nodes in all clusters
    persistence:
      multiple:
        data:
          storage: 2G
        journal:
          storage: 1G
        logs:
          storage: 1G

  # consider this section as a default configuration for ALL shards
  shard:
    clusterSpecList:
      - clusterName: kind-e2e-cluster-1
        # each shard will have only one mongod process deployed in this cluster
        members: 1
        memberConfig:
          - votes: 1
            priority: "20" # we increase the priority to have primary in this cluster
      - clusterName: kind-e2e-cluster-2
        # one member in this cluster, no votes and priority defined means it'll get
        # the default values votes=1, priority="1"
        members: 1
      - clusterName: kind-e2e-cluster-3
        members: 1 # one member in this cluster

  shardOverrides: # here you specify customizations for specific shards
    # here you specify to which shard names the following configuration will
    # apply
    - shardNames:
        - sc-0
      clusterSpecList:
        - clusterName: kind-e2e-cluster-1
          # all fields here are optional
          # shard "sc-0" will have two members instead of one, which was defined as the
          # default for all shards in spec.shard.clusterSpecList[0].members
          members: 2
          memberConfig:
            - votes: 1
              # shard "sc-0" should not have primary in this cluster like every other shard
              priority: "1"
            - votes: 1
              priority: "1"
        - clusterName: kind-e2e-cluster-2
          members: 2 # shard "sc-0" will have two members instead of one
          memberConfig:
            - votes: 1
              # both processes of shard "sc-0" in this cluster will have the same
              # likelihood to become a primary member
              priority: "20"
            - votes: 1
              priority: "20"
        # We need to specify the list of all clusters on which this shard will be
        # deployed.
        - clusterName: kind-e2e-cluster-3
          # If the clusterName element is omitted here, it will be considered as an
          # override for this shard, so that the operator shouldn't deploy any member
          # to it.
          # No fields are mandatory in here, though. In case a field is not set, it's
          # not overridden and the default value is taken from a top level spec.shard
          # settings.

  configSrv:
    # the same configuration fields are available as in
    # spec.shard.clusterSpecList.
    clusterSpecList:
      - clusterName: kind-e2e-cluster-1
        members: 1
      - clusterName: kind-e2e-cluster-2
        members: 1
      - clusterName: kind-e2e-cluster-3
        members: 1

  mongos:
    # the same configuration fields are available as in
    # spec.shard.clusterSpecList apart from storage and replica-set related
    # fields.
    clusterSpecList:
      - clusterName: kind-e2e-cluster-1
        members: 1
      - clusterName: kind-e2e-cluster-2
        members: 1
      - clusterName: kind-e2e-cluster-3
        members: 1
```

## Shard Overrides

To deploy a sharded cluster to multiple Kubernetes clusters, you apply the sharded 
cluster configuration (MongoDB custom resource yaml) to your central cluster - 
the Kubernetes cluster on which your MongoDB Operator instance is deployed. This 
configuration's `spec.shard` definition is considered your deployment's base 
shard definition.

If you would like to customize specific shards on specific Kubernetes clusters, 
you can use shard overrides to update the base shard defintion for a given shard. 

The following tables list fields that you can define in order to update or 
extend your base shard definition. The fields are listed in order of precedence. 
The topmost field in a given table represents the setting with the lowest 
precedence, and the bottommost field, if defined, overrides all other fields 
(e.g. specific shard, on a specific cluster).

Additionally, the override policy denoted for each field type describes whether that 
specific field is overridden by the newly defined value, or whether the complete 
object in which that field is defined is overidden. If the entire object is overridden, 
any fields defined in the base shard definition that are not also explicitly 
defined in the override definition are removed.The `merge` value indicates 
that a single field is updated, and the `replace` value indicates that the 
complete parent object is overridden.

### Customize Persistence and Statefulset Settings

| ShardedClusterSpec Field | To Specify | Applies to |
|---|---|---|
| `spec.shardPodSpec` | Persistence and Pod Template | All pods |
| `spec.shardSpecificPodSpec` (deprecated) | Persistence and Pod Template | All pods |
| `spec.shard.clusterSpecList.podSpec` | Persistence (Pod Template field is ignored) | All shards in the cluster |
| `spec.shard.clusterSpecList.statefulSet` | Pod Template | All shards in the cluster |
| `spec.shardOverrides.podSpec` | Persistence (Pod Template field is ignored) | All shards in the cluster |
| `spec.shardOverrides.statefulSet` | Pod Template | One shard in the cluster |
| `spec.shardOverrides.clusterSpecList.podSpec` | Persistence (Pod Template field is ignored) | One shard in a specific cluster |
| `spec.shardOverrides.clusterSpecList.statefulSet` | Pod Template | One shard in a specific cluster |

**Note:** Deprecation of ShardSpecificPodSpec

The `ShardSpecificPodSpec` field is deprecated, but is still supported. 
It was previously used to specify Persistence and Pod Template parameters, 
per shards, for single cluster sharded cluster. Now that it is deprecated, you should migrate to 
`ShardOverrides.PodSpec`, and `ShardOverrides.StatefulSetConfiguration`.
See the provided example YAML file for guidance on updating from 
`shardSpecificPodSpec` and `shardOverrides` for a single cluster deployments.

#### Override pod template and persistence settings in `clusterSpecList`

The following example illustrates how to override custom pod templates and 
persistence settings in `clusterSpecList`.

```yaml
shardPodSpec: # applicable to all shards in all clusters
  persistence:
    single:
      storage: "5G"
  podTemplate:
    spec:
      containers:
        - name: mongodb-enterprise-database
          resources:
            requests:
              cpu: 0.5
              memory: 1.0G
            limits:
              cpu: 1.0
              memory: 2.0G
shard:
  clusterSpecList:
    - clusterName: kind-e2e-cluster-1
      members: 2
      # The below statefulset override is applicable only to pods in kind-e2e-cluster-1
      # Specs will be merged, the "request" field defined above will still be
      # applied to containers in this cluster.
      # However, limits will be replaced with below values, because
      # clusterSpecList.statefulSet.spec.template has a
      # higher priority than shardPodSpec.podTemplate
      statefulSet:
        spec:
          template:
            spec:
              containers:
                - name: mongodb-enterprise-database
                  resources:
                    limits:
                      cpu: 1.0
                      memory: 2.5G
      # In clusterSpecList.podSpec, only persistence field must be used, the
      # podTemplate field is ignored.
      # In kind-e2e-cluster-1, we replace the persistence settings defined in
      # shardPodSpec
      podSpec:
        persistence:
          multiple:
            journal:
              storage: "6G"
            data:
              storage: "7G"
            logs:
              storage: "6G"
    - clusterName: kind-e2e-cluster-2
      members: 1
```

To learn more, you can review [the complete file](https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/public/samples/sharded_multicluster/pod_template_shards_0.yaml).

#### Define custom pod templates and persistence settings with `shardOverrides`

The following example illustrates how to define custom pod templates and persistence settings
in `shardOverrides`.

```yaml
      # In clusterSpecList.podSpec, only persistence field must be used, the
      # podTemplate field is ignored.
      # In kind-e2e-cluster-1, we define custom persistence settings
      podSpec:
        persistence:
          multiple:
            journal:
              storage: "5G"
            data:
              storage: "5G"
            logs:
              storage: "5G"
    - clusterName: kind-e2e-cluster-2
      members: 1

shardOverrides:
  - shardNames: [ "pod-template-shards-1-2" ]
    # This override will apply to shard of index 2
    # Statefulset settings defined at this level (shardOverrides.statefulSet)
    # apply to members of shard 2 in ALL clusters.
    # This field has higher priority than shard.clusterSpecList.statefulSet, but
    # lower than shardOverrides.clusterSpecList.statefulSet
    # It has a merge policy, which means that the limits defined above for the
    # mongodb-enterprise-database container field still apply to all members in
    # that shard, except if overridden.
    statefulSet:
      spec:
        template:
          spec:
            containers:
              - name: sidecar-shard-2
                image: busybox
                command: [ "sleep" ]
                args: [ "infinity" ]
    clusterSpecList:
      - clusterName: kind-e2e-cluster-1
        members: 2
      - clusterName: kind-e2e-cluster-2
        members: 1
        # The below statefulset override is applicable only to members of shard 2, in cluster 1
        # Specs will be merged, the "limits" field defined above will still be applied
        # to containers in this cluster together with the requests field below.
        statefulSet:
          spec:
            template:
              spec:
                containers:
                  - name: mongodb-enterprise-database
                    resources:
                      requests: # We add a requests field in shard 2, cluster 1
                        cpu: 0.5
                        memory: 1.0G

        podSpec:
          # In shardOverrides.clusterSpecList.podSpec, only persistence field must be
          # used, the podTemplate field is ignored.
          persistence: # we assign additional disk resources in shard 2, cluster 1
            multiple:
              journal:
                storage: "6G"
              data:
                storage: "6G"
              logs:
                storage: "6G"
```

To learn more, you can review [the complete file](https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/public/samples/sharded_multicluster/pod_template_shards_1.yaml).

#### Migrating from deprecated `shardSpecificPodSpec` field

The following example illustrates how to update from the deprecated 
`shardSpecificPodSpec` field to the new `shardOverrides` field. 

```yaml
# This file is an example of how to migrate from the old deprecated
# ShardSpecificPodSpec field to the new shardOverrides fields
# for single cluster deployments.
# The settings specified in shardOverrides are the exact equivalent to the
# ones in shardSpecificPodSpec, showing how to replicate them
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: shardspecificpodspec-migration
  namespace: mongodb-test
spec:
  # There are 4 shards in this cluster, but the shardSpecificPodSpec field
  # doesn't need to have on entry per shard, it can have less
  shardCount: 4
  mongodsPerShardCount: 2
  mongosCount: 1
  configServerCount: 3
  topology: SingleCluster
  type: ShardedCluster
  version: 8.0.3
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  persistent: true

  shardPodSpec:
    # default persistence configuration for all shards in all clusters
    persistence:
      single:
        storage: "5G"
  shardSpecificPodSpec: # deprecated way of overriding shards (array)
    - persistence: # shard of index 0
        single:
          storage: "6G"
      # Specify resources settings to enterprise database container in shard 0
      podTemplate:
        spec:
          containers:
            - name: mongodb-enterprise-database
              resources:
                requests:
                  cpu: 0.5
                  memory: 1G
                limits:
                  cpu: 1.0
                  memory: 2.0G
    - persistence: # shard of index 1
        single:
          storage: "7G"
    - persistence: # shard of index 2
        single:
          storage: "7G"

  # The below shardOverrides replicate the same shards configuration as the one
  # specified above in shardSpecificPodSpec
  shardOverrides:
    - shardNames: [ "shardspecificpodspec-migration-0" ] # overriding shard #0
      podSpec:
        persistence:
          single:
            storage: "6G"
      statefulSet:
        spec:
          template:
            spec:
              containers:
                - name: mongodb-enterprise-database
                  resources:
                    requests:
                      cpu: 0.5
                      memory: 1G
                    limits:
                      cpu: 1.0
                      memory: 2.0G

    # The ShardSpecificPodSpec field above has the same configuration for shards
    # 1 and 2. It is possible to specify both shard names in the override and not
    # duplicate that configuration
    - shardNames: [ "shardspecificpodspec-migration-1", "shardspecificpodspec-migration-2" ]
      podSpec:
        persistence:
          single:
            storage: "7G"
```

To learn more, you can review [the complete file](https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/public/samples/sharded_multicluster/shardSpecificPodSpec_migration.yaml).

### External Access Configuration

| Field | Which clusters | Which shards |
|---|---|---|
| `spec.externalAccess` | all | all |
| `spec.shard.externalAccess` | one | all |
| `spec.shard.clusterSpecList.externalAccess` | one | all |

### Members, MemberConfig, Additional MongodConfig, AgentConfig

| ShardedClusterSpec Field | To Specify | Applies to |
|---|---|---|
| `spec.shard` | not applicable | not applicable |
| `spec.shard.clusterSpecList` | applies | applies |
| `spec.shardOverrides` (single cluster only) | applies | applies |
| `spec.sharOverrides` | not applicable | not applicable |
| `spec.shardOverrides.clusterSpecList` | applies | applies |

  

## Config Server Overrides

| ShardedClusterSpec Field | To Specify | Applies to |
|---|---|---|
| `spec.configSrv` | not applicable | not applicable |
| `spec.configSrv` | applies | applies |
| `spec.configSrv.clusterSpecList` | not applicable | not applicable |
| `spec.configSrv.clusterSpecList.podSpec` | applies | ignored |
| `spec.configSrv.clusterSpecList.statefulSet` | not applicable | applies |

```yaml
configSrv:
  clusterSpecList:
    - clusterName: kind-e2e-cluster-1
      members: 2
      # The below statefulset override is applicable only to pods in kind-e2e-cluster-1
      # Specs will be merged, the "request" field defined above will still be applied to containers in this cluster
      # However, limits will be replaced with below values, because clusterSpecList.statefulSet.spec.template has a
      # higher priority than configSrvPodSpec.podTemplate
      statefulSet:
        spec:
          template:
            spec:
              containers:
                - name: mongodb-enterprise-database
                  resources:
                    limits:
                      cpu: 1.0
                      memory: 2.5G
      # In clusterSpecList.podSpec, only persistence field must be used, the podTemplate field is ignored.
      podSpec: # In kind-e2e-cluster-1, we replace the persistence settings defined in configSrvPodSpec
        persistence:
          multiple:
            journal:
              storage: "6G"
            data:
              storage: "7G"
            logs:
              storage: "6G"
    - clusterName: kind-e2e-cluster-2
      members: 1
# doc-highlight-end: configSrv
mongos:
  clusterSpecList:
    - clusterName: kind-e2e-cluster-1
      members: 2
    - clusterName: kind-e2e-cluster-2
      members: 1

shard:
  clusterSpecList:
    - clusterName: kind-e2e-cluster-1
      members: 2
    - clusterName: kind-e2e-cluster-2
      members: 1
```

To learn more, you can review [the complete file](https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/public/samples/sharded_multicluster/pod_template_config_servers.yaml).

## Mongos Overrides

| ShardedClusterSpec Field | To Specify | Applies to |
|---|---|---|
| `ConfigSrvSpec` | not applicable | not applicable |
| `ConfigSrvPodSpec` | applies | not applicable |
| `ConfigSrvSpec.ClusterSpecList` | not applicable | applies |
| `ConfigSrvSpec.ClusterSpecList.PodSpec` | ignored | not applicable |
| `ConfigSrvSpec.ClusterSpecList.StatefulSetConfiguration` | applies | not applicable |
