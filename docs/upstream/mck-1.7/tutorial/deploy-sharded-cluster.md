<!-- Converted from tutorial/deploy-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Deploy a Sharded Cluster

**Note:**

At any place on this page that says *Ops Manager*, you can substitute *Cloud Manager*.

**Important:**

- You can use the Kubernetes Operator to deploy MongoDB resources with
  Cloud Manager and with Ops Manager version 6.0.x or later.

- You can use the Atlas Operator
  to deploy MongoDB resources to Atlas.

**Warning:**

Kubernetes Operator doesn't support arbiter nodes.

Sharded clusters provide horizontal scaling
for large data sets and enable high throughput operations by
distributing the data set across a group of servers.

To learn more about sharding, see
Sharding Introduction in the
MongoDB manual.

Use this procedure to deploy a new sharded cluster that `Ops Manager` manages.
Later, you can use `Ops Manager` to add shards and perform other maintenance
operations on the cluster.

## Considerations

### Do Not Deploy Monitoring Agents Inside and Outside Kubernetes

Due to Kubernetes network translation, a Monitoring Agent outside Kubernetes
cannot monitor MongoDB instances inside Kubernetes. For this reason, k8s
and non-k8s deployments in the same project are not supported. Use
separate projects.

### Choose Whether to Encrypt Connections

When you deploy your sharded cluster via the Kubernetes Operator, you must
choose whether to encrypt connections using TLS (Transport Layer Security) certificates.

The following procedure for TLS-Encrypted connections:

- Establishes TLS (Transport Layer Security)-encrypted connections between cluster shards.
- Establishes TLS (Transport Layer Security)-encrypted connections between client applications
  and MongoDB deployments.
- Requires valid certificates for TLS (Transport Layer Security) encryption.

The following procedure for Non-Encrypted Connections:

- Doesn't encrypt connections between cluster shards.
- Doesn't encrypt connections between client applications
  and MongoDB deployments.
- Has fewer setup requirements than a deployment with TLS (Transport Layer Security)-encrypted
  connections.

**Note:** You can't secure a Standalone Instance of MongoDB in a Kubernetes cluster.

To set up TLS (Transport Layer Security) encryption for a replica set, see 
deploy-replica-set.

Select the appropriate tab based on whether you want to encrypt your
replica set connections with TLS (Transport Layer Security).

## Prerequisites

**encrypted:**

To deploy a sharded cluster using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

- Have or create an `Ops Manager instance` or a `Cloud Manager organization`.

- Have or install the MongoDB Controllers for Kubernetes Operator.

- Create or generate a Kubernetes Operator ConfigMap.

- Create credentials for the Kubernetes Operator or 
  configure a different secret storage tool.

**Note:**

To avoid storing secrets in single-cluster Kubernetes deployments, you can
migrate all [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to a secret storage tool.
Deployments on multiple Kubernetes clusters don't support storing secrets
in secret storage tools, such as [HashiCorp Vault](https://www.vaultproject.io/).

- Generate one TLS (Transport Layer Security) certificate for each of the following components:

  - Each shard in your sharded cluster. Ensure that you add SAN (Subject Alternative Name)\s for 
    each Kubernetes pod that hosts a shard member to the certificate.

    In your TLS (Transport Layer Security) certificates, the SAN (Subject Alternative Name)
    for each shard pod must use the following format:

    ```none
    <pod-name>.<metadata.name>-sh.<namespace>.svc.cluster.local
    ```

  - Your config servers. Ensure that you add SAN (Subject Alternative Name)\s for 
    each Kubernetes pod that hosts your config servers to the certificate. 

    In your TLS (Transport Layer Security) certificates, the SAN (Subject Alternative Name)
    for each config server pod must use the following format:

    ```none
    <pod-name>.<metadata.name>-cs.<namespace>.svc.cluster.local
    ```

  - Your `mongos` instances. Ensure that you add SAN (Subject Alternative Name)\s for 
    each Kubernetes pod that hosts a `mongos` to the certificate. 

    In your TLS (Transport Layer Security) certificates, the SAN (Subject Alternative Name) for each `mongos` pod must use this 
    format:

    ```none
    <pod-name>.<metadata.name>-svc.<namespace>.svc.cluster.local
    ```

  - Your project's MongoDB Agent. For the MongoDB Agent certificate, 
    ensure that you meet the following requirements:

    - The Common Name in the TLS (Transport Layer Security) certificate is not empty.
    - The combined Organization and Organizational Unit in each TLS (Transport Layer Security)
      certificate differs from the Organization and
      Organizational Unit in the TLS (Transport Layer Security) certificate for your
      replica set members.

- You must possess the CA (Certificate Authority) certificate and the key that you used to 
  sign your TLS (Transport Layer Security) certificates.

**Important:**

The Kubernetes Operator uses `kubernetes.io/tls` secrets
to store TLS (Transport Layer Security) certificates and private keys for Ops Manager and MongoDB
resources. Starting in Kubernetes Operator version 1.17.0, the 
Kubernetes Operator doesn't support concatenated PEM (Privacy-Enhanced Mail) files stored as
`Opaque secrets`.

**non-encrypted:**

To deploy a sharded cluster using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

- Have or create an `Ops Manager instance` or a `Cloud Manager organization`.

- Have or install the MongoDB Controllers for Kubernetes Operator.

- Create or generate a Kubernetes Operator ConfigMap.

- Create credentials for the Kubernetes Operator or 
  configure a different secret storage tool.

**Note:**

To avoid storing secrets in single-cluster Kubernetes deployments, you can
migrate all [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to a secret storage tool.
Deployments on multiple Kubernetes clusters don't support storing secrets
in secret storage tools, such as [HashiCorp Vault](https://www.vaultproject.io/).

## Deploy a Sharded Cluster

**encrypted:**

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Create the secret for your Shards' TLS certificates.**

Run this `kubectl` command to create a new [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores
the sharded cluster shards' certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-0-cert \
  --cert=<shard-0-tls-cert> \
  --key=<shard-0-tls-key>

kubectl -n mongodb create secret tls <prefix>-<metadata.name>-1-cert \
  --cert=<shard-1-tls-cert> \
  --key=<shard-1-tls-key>
```

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

**Step 3: Create the secret for your config servers' TLS certificate.**

Run this `kubectl` command to create a new secret that stores
the sharded cluster config servers' certificate:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-config-cert \
  --cert=<config-tls-cert> \
  --key=<config-tls-key>
```

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

**Step 4: Create the secret for your mongos servers' TLS certificate.**

Run this `kubectl` command to create a new secret that stores
the sharded cluster `mongos` certificate:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-mongos-cert \
  --cert=<mongos-tls-cert> \
  --key=<mongos-tls-key>
```

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

**Step 5: Create the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your agent's TLS certificate.**

Run this `kubectl` command to create a new [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores
the agent's TLS certificate:

```sh
kubectl create secret tls <prefix>-<metadata.name>-agent-certs \
  --cert=<agent-tls-cert> \
  --key=<agent-tls-key>
```

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

**Step 6: Create the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to link your CA (Certificate Authority) with your deployment.**

Run this `kubectl` command to link your CA (Certificate Authority) to your sharded
cluster and specify the CA (Certificate Authority) certificate file that you must always
name `ca-pem` for the `MongoDB` resource:

```sh
kubectl create configmap custom-ca --from-file=ca-pem=<your-custom-ca-file>
```

**Step 7: Copy the sample sharded cluster resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired sharded cluster configuration.

Change the settings to match your desired
sharded cluster configuration.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-sharded-cluster>
spec:
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 3
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
            # Must match metadata.name in ConfigMap file
  credentials: <mycredentials>
  type: ShardedCluster
  persistent: true
...
```

```yaml
  security:
    tls:
      ca: <custom-ca>
    certsSecretPrefix: <prefix>
...
```

**Step 8: Paste the copied example to create a new sharded cluster resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
into a new text file.

**Step 9: Configure the settings highlighted in the preceding step as follows.**

* - Key
  - Type
  - Description
  - Example

* - `metadata.name`
  - string
  - Label for this Kubernetes sharded cluster [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

    Resource names must be 44 characters or less.

    To learn more, see `metadata.name` and
    Kubernetes documentation on `names`.

  - `myproject`

* - `spec.shardCount`
  - integer
  - Number of shards to deploy.
  - `2`

* - `spec.mongodsPerShardCount`
  - integer
  - Number of shard members per shard.
  - `3`

* - `spec.mongosCount`
  - integer
  - Number of shard routers to deploy.
  - `2`

* - `spec.configServerCount`
  - integer
  - Number of members of the config server replica set.
  - `3`

* - `spec.version`
  - string
  - Version of MongoDB that this sharded cluster should run.

    The format should be `X.Y.Z` for the Community edition and
    `X.Y.Z-ent` for the Enterprise edition.

    IMPORTANT: Ensure that you choose a compatible MongoDB
    Server version. Compatible versions
    differ depending on the base image that the MongoDB database resource
    uses.

    To learn more about MongoDB versioning, see
    release-version-numbers in the MongoDB Manual.
  - .. include:: /includes/facts/fact-which-appdb-version.rst

* - `spec.opsManager.configMapRef.name`
  - string
  - Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection
    configuration. The
    `spec.cloudManager.configMapRef.name` setting is an
    alias for this setting and can be used in its place.

    This value must exist on the *same* namespace as the resource
    you want to create.

    IMPORTANT: The Kubernetes Operator tracks any changes to the
    ConfigMap and reconciles the state of the `MongoDB` resource.

  - `<myproject>`

* - `spec.credentials`
  - string
  - Name of the secret you
    created as `Ops Manager` API (Application Programming Interface)
    authentication credentials for the Kubernetes Operator to
    communicate with Ops Manager.

    The `Ops Manager` Kubernetes Secret object
    holding the Credentials must exist on the **same** Namespace as
    the resource you want to create.

    IMPORTANT: The Kubernetes Operator tracks any changes to the Secret
    and reconciles the state of the `MongoDB` resource.

  - `<mycredentials>`

* - `spec.type`
  - string
  - Type of `MongoDB` resource to create.

  - `ShardedCluster`

* - `spec.persistent`
  - string
  - *Optional.*

    Flag indicating if this `MongoDB` resource should use [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for
    storage. Persistent volumes are not deleted when the
    `MongoDB` resource is stopped or restarted.

    If this value is `true`, then the following values are set
    to their default value of `16Gi`:

    - `spec.shardPodSpec.persistence.single`
    - `spec.configSrvPodSpec.persistence.single`

    To change your [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) configuration, configure the
    following collections to meet your deployment requirements:

    - If you want one [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the
      `spec.shardPodSpec.persistence.single` and
      `spec.configSrvPodSpec.persistence.single`
      collections.

    - If you want separate [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for data, journals, and
      logs for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the following
      collections:

      - In the `spec.configSrvPodSpec.persistence.multiple`
        collection:
        - `.data`
        - `.journal`
        - `.logs`

      - In the `spec.shardPodSpec.persistence.multiple` collection:
        - `.data`
        - `.journal`
        - `.logs`

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

  - `true`

**Step 10: Configure the TLS settings for your sharded cluster resource using a custom certificate authority (CA).**

To enable TLS (Transport Layer Security) in your deployment, configure the following
settings in your Kubernetes object:

| Key | Type | Necessity | Description | Example |
|---|---|---|---|---|
| \| `spec.security` \| `.tls.ca` | string | Required | Add the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)\'s name that stores the custom CA (Certificate Authority) that you used to sign your deployment's TLS (Transport Layer Security) certificates. | `<custom-ca>` |
| \| `spec.security` \| `.certsSecretPrefix` | string | Required | Add the `<prefix>` of the secret name that contains your MongoDB deployment's TLS (Transport Layer Security) certificates. For example, if you call your deployment `my-deployment` and you set the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, you must name the TLS (Transport Layer Security) secret for internal cluster authentication (if enabled) `mdb-my-deployment-clusterfile`. | `devDb` |

**Step 11: Add any additional accepted settings for a sharded cluster deployment.**

You can also add any of the following optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file for a sharded cluster
deployment:

- `spec.backup.assignmentLabels`
- `spec.backup.mode`
- `spec.backup.snapshotSchedule.snapshotIntervalHours`
- `spec.backup.snapshotSchedule.snapshotRetentionDays`
- `spec.backup.snapshotSchedule.dailySnapshotRetentionDays`
- `spec.backup.snapshotSchedule.weeklySnapshotRetentionWeeks`
- `spec.backup.snapshotSchedule.monthlySnapshotRetentionMonths`
- `spec.backup.snapshotSchedule.pointInTimeWindowHours`
- `spec.backup.snapshotSchedule.referenceHourOfDay`
- `spec.backup.snapshotSchedule.referenceMinuteOfHour`
- `spec.backup.snapshotSchedule.fullIncrementalDayOfWeek`
- `spec.backup.snapshotSchedule.clusterCheckpointIntervalMin`
- `spec.clusterDomain`
- `spec.connectivity.replicaSetHorizons`
- `spec.featureCompatibilityVersion`
- `spec.logLevel`

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**For config server**

- `spec.configSrv.additionalMongodConfig`
- `spec.configSrvPodSpec.persistence.single`
- `spec.configSrvPodSpec.persistence.multiple.data`
- `spec.configSrvPodSpec.persistence.multiple.journal`
- `spec.configSrvPodSpec.persistence.multiple.logs`
- `spec.configSrvPodSpec.podTemplate.spec.affinity.podAffinity`
- `spec.configSrvPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.configSrvPodSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.configSrvPodSpec.podTemplate.metadata`
- `spec.configSrvPodSpec.podTemplate.spec`

**For shard routers**

- `spec.mongos.additionalMongodConfig`
- `spec.mongosPodSpec.podTemplate.spec.affinity.podAffinity`
- `spec.mongosPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.mongosPodSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.mongosPodSpec.podTemplate.metadata`
- `spec.mongosPodSpec.podTemplate.spec`

**For shard members**

- `spec.shard.additionalMongodConfig`
- `spec.shardPodSpec.persistence.single`
- `spec.shardPodSpec.persistence.multiple.data`
- `spec.shardPodSpec.persistence.multiple.journal`
- `spec.shardPodSpec.persistence.multiple.logs`
- `spec.shardPodSpec.podTemplate.spec.affinity.podAffinity`
- `spec.shardPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.shardPodSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.shardPodSpec.podTemplate.metadata`
- `spec.shardPodSpec.podTemplate.spec`
- `spec.shardSpecificPodSpec`

**Step 12: Save this file with a `.yaml` file extension.**

**Step 13: Start your sharded cluster deployment.**

Invoke the following Kubernetes command to create your
sharded cluster:

```sh
kubectl apply -f <sharded-cluster-conf>.yaml
```

Check the log after running this
command. If the creation was successful, you should see a message
similar to the following:

```sh
2018-06-26T10:30:30.346Z INFO operator/shardedclusterkube.go:52 Created! {"sharded cluster": "my-sharded-cluster"}
```

**Step 14: Track the status of your sharded cluster deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.

After you encrypt your database resource with TLS (Transport Layer Security), you can secure the
following:

- Client authentication with LDAP
- Client authentication with X.509
- Internal authentication with X.509
- Client authentication with OIDC

### Renew TLS Certificates for a Sharded Cluster

Renew your TLS (Transport Layer Security) certificates periodically
using the following procedure:

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your Shards' TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the sharded cluster shards' certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-0-cert \
  --cert=<shard-0-tls-cert> \
  --key=<shard-0-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -

kubectl -n mongodb create secret tls <prefix>-<metadata.name>-1-cert \
  --cert=<shard-1-tls-cert> \
  --key=<shard-1-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -
```

**Step 3: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your config server's TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the sharded cluster config server's certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-config-cert \
  --cert=<config-tls-cert> \
  --key=<config-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -
```

**Step 4: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your mongos server's TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the sharded cluster `mongos` certificates:

```sh
kubectl -n mongodb create secret tls <prefix>-<metadata.name>-mongos-cert \
  --cert=<mongos-tls-cert> \
  --key=<mongos-tls-key> \
  --dry-run=client \
  -o yaml |
kubectl apply -f -
```

**non-encrypted:**

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Copy the sample sharded cluster resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired sharded cluster configuration.

This is a YAML (Yet Another Markup Language) file that you can modify to meet your desired
configuration. Change the settings to match your desired
sharded cluster configuration.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-sharded-cluster>
spec:
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 3
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
            # Must match metadata.name in ConfigMap file
  credentials: <mycredentials>
  type: ShardedCluster
  persistent: true
...
```

**Step 3: Paste the copied example to create a new sharded cluster resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
into a new text file.

**Step 4: Configure the settings highlighted in the preceding step as follows.**

* - Key
  - Type
  - Description
  - Example

* - `metadata.name`
  - string
  - Label for this Kubernetes sharded cluster [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

    Resource names must be 44 characters or less.

    To learn more, see `metadata.name` and
    Kubernetes documentation on `names`.

  - `myproject`

* - `spec.shardCount`
  - integer
  - Number of shards to deploy.
  - `2`

* - `spec.mongodsPerShardCount`
  - integer
  - Number of shard members per shard.
  - `3`

* - `spec.mongosCount`
  - integer
  - Number of shard routers to deploy.
  - `2`

* - `spec.configServerCount`
  - integer
  - Number of members of the config server replica set.
  - `3`

* - `spec.version`
  - string
  - Version of MongoDB that this sharded cluster should run.

    The format should be `X.Y.Z` for the Community edition and
    `X.Y.Z-ent` for the Enterprise edition.

    IMPORTANT: Ensure that you choose a compatible MongoDB
    Server version. Compatible versions
    differ depending on the base image that the MongoDB database resource
    uses.

    To learn more about MongoDB versioning, see
    release-version-numbers in the MongoDB Manual.
  - .. include:: /includes/facts/fact-which-appdb-version.rst

* - `spec.opsManager.configMapRef.name`
  - string
  - Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection
    configuration. The
    `spec.cloudManager.configMapRef.name` setting is an
    alias for this setting and can be used in its place.

    This value must exist on the *same* namespace as the resource
    you want to create.

    IMPORTANT: The Kubernetes Operator tracks any changes to the
    ConfigMap and reconciles the state of the `MongoDB` resource.

  - `<myproject>`

* - `spec.credentials`
  - string
  - Name of the secret you
    created as `Ops Manager` API (Application Programming Interface)
    authentication credentials for the Kubernetes Operator to
    communicate with Ops Manager.

    The `Ops Manager` Kubernetes Secret object
    holding the Credentials must exist on the **same** Namespace as
    the resource you want to create.

    IMPORTANT: The Kubernetes Operator tracks any changes to the Secret
    and reconciles the state of the `MongoDB` resource.

  - `<mycredentials>`

* - `spec.type`
  - string
  - Type of `MongoDB` resource to create.

  - `ShardedCluster`

* - `spec.persistent`
  - string
  - *Optional.*

    Flag indicating if this `MongoDB` resource should use [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for
    storage. Persistent volumes are not deleted when the
    `MongoDB` resource is stopped or restarted.

    If this value is `true`, then the following values are set
    to their default value of `16Gi`:

    - `spec.shardPodSpec.persistence.single`
    - `spec.configSrvPodSpec.persistence.single`

    To change your [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) configuration, configure the
    following collections to meet your deployment requirements:

    - If you want one [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the
      `spec.shardPodSpec.persistence.single` and
      `spec.configSrvPodSpec.persistence.single`
      collections.

    - If you want separate [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for data, journals, and
      logs for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the following
      collections:

      - In the `spec.configSrvPodSpec.persistence.multiple`
        collection:
        - `.data`
        - `.journal`
        - `.logs`

      - In the `spec.shardPodSpec.persistence.multiple` collection:
        - `.data`
        - `.journal`
        - `.logs`

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

  - `true`

**Step 5: Add any additional accepted settings for a sharded cluster deployment.**

You can also add any of the following optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file for a sharded cluster
deployment:

- `spec.backup.assignmentLabels`
- `spec.backup.mode`
- `spec.backup.snapshotSchedule.snapshotIntervalHours`
- `spec.backup.snapshotSchedule.snapshotRetentionDays`
- `spec.backup.snapshotSchedule.dailySnapshotRetentionDays`
- `spec.backup.snapshotSchedule.weeklySnapshotRetentionWeeks`
- `spec.backup.snapshotSchedule.monthlySnapshotRetentionMonths`
- `spec.backup.snapshotSchedule.pointInTimeWindowHours`
- `spec.backup.snapshotSchedule.referenceHourOfDay`
- `spec.backup.snapshotSchedule.referenceMinuteOfHour`
- `spec.backup.snapshotSchedule.fullIncrementalDayOfWeek`
- `spec.backup.snapshotSchedule.clusterCheckpointIntervalMin`
- `spec.clusterDomain`
- `spec.connectivity.replicaSetHorizons`
- `spec.featureCompatibilityVersion`
- `spec.logLevel`

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**For config server**

- `spec.configSrv.additionalMongodConfig`
- `spec.configSrvPodSpec.persistence.single`
- `spec.configSrvPodSpec.persistence.multiple.data`
- `spec.configSrvPodSpec.persistence.multiple.journal`
- `spec.configSrvPodSpec.persistence.multiple.logs`
- `spec.configSrvPodSpec.podTemplate.spec.affinity.podAffinity`
- `spec.configSrvPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.configSrvPodSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.configSrvPodSpec.podTemplate.metadata`
- `spec.configSrvPodSpec.podTemplate.spec`

**For shard routers**

- `spec.mongos.additionalMongodConfig`
- `spec.mongosPodSpec.podTemplate.spec.affinity.podAffinity`
- `spec.mongosPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.mongosPodSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.mongosPodSpec.podTemplate.metadata`
- `spec.mongosPodSpec.podTemplate.spec`

**For shard members**

- `spec.shard.additionalMongodConfig`
- `spec.shardPodSpec.persistence.single`
- `spec.shardPodSpec.persistence.multiple.data`
- `spec.shardPodSpec.persistence.multiple.journal`
- `spec.shardPodSpec.persistence.multiple.logs`
- `spec.shardPodSpec.podTemplate.spec.affinity.podAffinity`
- `spec.shardPodSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.shardPodSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.shardPodSpec.podTemplate.metadata`
- `spec.shardPodSpec.podTemplate.spec`
- `spec.shardSpecificPodSpec`

**Step 6: Save this file with a `.yaml` file extension.**

**Step 7: Start your sharded cluster deployment.**

Invoke the following Kubernetes command to create your
sharded cluster:

```sh
kubectl apply -f <sharded-cluster-conf>.yaml
```

Check the log after running this
command. If the creation was successful, you should see a message
similar to the following:

```sh
2018-06-26T10:30:30.346Z INFO operator/shardedclusterkube.go:52 Created! {"sharded cluster": "my-sharded-cluster"}
```

**Step 8: Track the status of your sharded cluster deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.
