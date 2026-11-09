<!-- Converted from tutorial/scale-resources.txt (reStructuredText). Includes are inlined. -->

# Scale a Deployment

You can scale your replica set and sharded cluster
deployments up or down to match your desired configuration. Scaling up
increases the number of members and/or shards in the deployment,
thereby improving your deployment's redundancy and availability. The
scale of your deployment is configured in its corresponding
[custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

Scale a Replica Set
  To scale your replica set deployment, set the `spec.members`
  setting to the desired number of replica set members. To learn more 
  about replication, see Replication in the
  MongoDB manual. 

Scale a Sharded Cluster
  To scale your sharded cluster deployment, set the following settings
  as desired:

  | Setting | Description |
  |---|---|
  | `spec.shardCount` | Number of shards in the sharded cluster. |
  | `spec.mongodsPerShardCount` | Number of members per shard. |
  | `spec.mongosCount` | Number of Shard Routers. |
  | `spec.configServerCount` | Number of members in the Config Server. |

  To learn more about sharded cluster configurations, see
  Sharded Cluster Components in the MongoDB manual.

## Considerations

- The Kubernetes Operator does not support modifying deployment types.
  For example, you cannot convert a standalone deployment to a
  replica set. To modify the type of a deployment,
  we recommend the following procedure:

  1. Create the new deployment with the desired configuration.

  #. `Back up the data` from
     your current deployment.

  #. `Restore the data` from your current
     deployment to the new deployment.

  #. Test your application connections to the new deployment as needed.

  #. Once you have verified that the new deployment contains the
     required data and can be reached by your application(s), bring
     down the old deployment.

## Procedure

To scale up your deployment, select the desired tab based on the deployment 
configuration you want to scale:

**repl:**

**Step 1: Adjust the `spec.members` setting from 3 to 4:**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  opsManager:
    configMapRef:
           # Must match metadata.name in ConfigMap file
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  type: ReplicaSet
  persistent: true
...
```

```yaml
spec: 
  members: 4
```

**Step 2: Reapply the configuration to Kubernetes:**

```sh
kubectl apply -f <repl-set-config>.yaml
```

**shard:**

**Step 1: Adjust the following settings to the desired values:**

- `spec.shardCount`
- `spec.mongodsPerShardCount`
- `spec.mongosCount`
- `spec.configServerCount`

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-secure-sharded-cluster>
spec:
  shardCount: 3
  mongodsPerShardCount: 3
  mongosCount: 3
  configServerCount: 4
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  type: ShardedCluster
  persistent: true
...
```

```yaml
spec: 
  shardCount: 3
  mongodsPerShardCount: 3
  mongosCount: 3
  configServerCount: 4
```

**Step 2: Reapply the configuration to Kubernetes:**

```sh
kubectl apply -f <sharded-cluster-config>.yaml
```
