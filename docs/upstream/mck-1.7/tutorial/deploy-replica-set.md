<!-- Converted from tutorial/deploy-replica-set.txt (reStructuredText). Includes are inlined. -->

# Deploy a Replica Set

**Note:**

At any place on this page that says *Ops Manager*, you can substitute *Cloud Manager*.

**Important:**

- You can use the Kubernetes Operator to deploy MongoDB resources with
  Cloud Manager and with Ops Manager version 6.0.x or later.

- You can use the Atlas Operator
  to deploy MongoDB resources to Atlas.

**Warning:**

Kubernetes Operator doesn't support arbiter nodes.

A replica set is a group of MongoDB deployments that maintain
the same data set. Replica sets provide redundancy and high
availability and are the basis for all production deployments.

To learn more about replica sets, see the
Replication Introduction in
the MongoDB manual.

Use this procedure to deploy a new replica set that `Ops Manager` manages.
After deployment, use `Ops Manager` to manage the replica set, including such
operations as adding, removing, and reconfiguring members.

## Considerations

When you deploy your replica set via the Kubernetes Operator, you must
choose whether to encrypt connections using TLS (Transport Layer Security) certificates.

The following procedure for TLS-Encrypted connections:

- Establishes TLS (Transport Layer Security)-encrypted connections between MongoDB hosts in the
  replica set.
- Establishes TLS (Transport Layer Security)-encrypted connections between client applications
  and MongoDB deployments.
- Requires valid certificates for TLS (Transport Layer Security) encryption.

The following procedure for Non-Encrypted Connections:

- Doesn't encrypt connections between MongoDB hosts in the
  replica set.
- Doesn't encrypt connections between client applications
  and MongoDB deployments.
- Has fewer setup requirements than a deployment with TLS (Transport Layer Security)-encrypted
  connections.

**Note:** You can't secure a Standalone Instance of MongoDB in a Kubernetes cluster.

To set up TLS (Transport Layer Security) encryption for a sharded cluster, see 
deploy-sharded-cluster.

Select the appropriate tab based on whether you want to encrypt your
replica set connections with TLS (Transport Layer Security).

## Prerequisites

**encrypted:**

To deploy a replica set using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

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

  - Your replica set. Ensure that you add SAN (Subject Alternative Name)\s for each Kubernetes pod 
    that hosts a member of your replica set to the certificate. 

    In your TLS (Transport Layer Security) certificate, the SAN (Subject Alternative Name) for each pod must use the 
    following format:

    ```none
    <pod-name>.<metadata.name>-svc.<namespace>.svc.cluster.local
    ```

    **Important:**

    If you're using an ACME (Automatic Certificate Management Environment) based service provider such as [Let's Encrypt](https://letsencrypt.org) to issue TLS (Transport Layer Security) certificates, the provider 
    might prohibit you from adding the Pod's default FQDN (fully qualified domain name)\s (`*.svc.cluster.local`)
    to SAN (Subject Alternative Name)\s in the certificate.

    To use an ACME (Automatic Certificate Management Environment) based certificate, you must configure 
    the certificate for your replica set resource. 
    To learn more, see the step about ACME (Automatic Certificate Management Environment) based TLS (Transport Layer Security) 
    certificates in the procedure.

  - Your project's MongoDB Agent. For the MongoDB Agent certificate, 
    ensure that you meet the following requirements:

    - The Common Name in the TLS (Transport Layer Security) certificate is not empty.
    - The combined Organization and Organizational Unit in each TLS (Transport Layer Security)
      certificate differs from the Organization and
      Organizational Unit in the TLS (Transport Layer Security) certificate for your
      replica set members.

- You must have the CA (Certificate Authority) certificate file and name it `ca-pem`.
- You must have the key that you used to sign your TLS (Transport Layer Security) certificates.

**Important:**

The Kubernetes Operator uses `kubernetes.io/tls` secrets
to store TLS (Transport Layer Security) certificates and private keys for Ops Manager and MongoDB
resources. Starting in Kubernetes Operator version 1.17.0, the 
Kubernetes Operator doesn't support concatenated PEM (Privacy-Enhanced Mail) files stored as
`Opaque secrets`.

**non-encrypted:**

To deploy a replica set using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

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

## Deploy a Replica Set

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

**Step 2: Create the secret for your replica set's TLS (Transport Layer Security) certificate.**

Run this `kubectl` command to create a new [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores
the replica set's certificate:

```sh
kubectl create secret tls <prefix>-<metadata.name>-cert \
  --cert=<replica-set-tls-cert> \
  --key=<replica-set-tls-key>
```

**Note:**

You must prefix your secrets with `<prefix>-<metadata.name>`.

For example, if you call your deployment `my-deployment` and you set
the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the
client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, 
you must name the TLS (Transport Layer Security) secret for internal cluster authentication 
(if enabled) `mdb-my-deployment-clusterfile`.

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

To learn about your options for secret
storage, see Configure Secret Storage.

**Step 3: Create the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your agent's TLS certificate.**

Run this `kubectl` command to create a new [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores
the agent's TLS certificate:

```sh
kubectl create secret tls <prefix>-<metadata.name>-agent-certs \
  --cert=<agent-tls-cert> \
  --key=<agent-tls-key>
```

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

**Step 4: Create the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to link your CA (Certificate Authority) with your deployment.**

Run this `kubectl` command to link your CA (Certificate Authority) to your replica
set and specify the CA (Certificate Authority) certificate file.

**Important:**

The Kubernetes Operator requires that the certificate for the `MongoDB` resource
is named `ca-pem` in the ConfigMap.

```sh
kubectl create configmap custom-ca --from-file=ca-pem=<your-custom-ca-file>
```

**Step 5: Copy the sample replica set resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired replica set configuration.

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
  security:
    tls:
      ca: <custom-ca>
    certsSecretPrefix: <prefix>
...
```

**Step 6: Paste the copied example to create a new replica set resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
into a new text file.

**Step 7: Change the settings to your preferred values.**

* - Key
  - Type
  - Description
  - Example

* - `metadata.name`
  - string
  - Label for this Kubernetes replica set [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

    Resource names must be 44 characters or less.

    To learn more, see `metadata.name` and
    Kubernetes documentation on
    `names`.

  - `myproject`

* - `spec.members`
  - integer
  - Number of members of the replica set.
  - `3`

* - `spec.version`
  - string
  - Version of MongoDB that this replica set should run.

    The format should be `X.Y.Z` for the Community edition and
    `X.Y.Z-ent` for the Enterprise edition.

    IMPORTANT: Ensure that you choose a compatible MongoDB
    Server version. Compatible versions
    differ depending on the base image that the MongoDB database resource
    uses.

    To learn more about MongoDB versioning, see
    release-version-numbers in the MongoDB Manual.
  - `8.0.0`

* - | `spec`
    | `.opsManager`
    | `.configMapRef`
    | `.name`
  - string
  - Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection
    configuration. The
    `spec.cloudManager.configMapRef.name` setting is an
    alias for this setting and can be used in its place.

    This value must exist on the *same* namespace as the resource
    you want to create.

    IMPORTANT: The Kubernetes Operator tracks any changes to the
    ConfigMap and reconciles the state of the `MongoDB` resource.

  - `<myconfigmap>`

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

  - `ReplicaSet`

* - `spec.persistent`
  - string
  - *Optional.*

    Flag indicating if this `MongoDB` resource should use [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for
    storage. Persistent volumes are not deleted when the
    `MongoDB` resource is stopped or restarted.

    If this value is `true`, then
    `spec.podSpec.persistence.single` is set to its
    default value of `16Gi`.

    To change your [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) configuration, configure the
    following collections to meet your deployment requirements:

    - If you want one [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the
      `spec.podSpec.persistence.single` collection.

    - If you want separate [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for data, journals, and
      logs for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the following
      collections:

      - `spec.podSpec.persistence.multiple.data`
      - `spec.podSpec.persistence.multiple.journal`
      - `spec.podSpec.persistence.multiple.logs`

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

**Step 8: Configure the TLS settings for your replica set resource using a custom certificate authority (CA).**

To enable TLS (Transport Layer Security) in your deployment, configure the following
settings in your Kubernetes object:

| Key | Type | Necessity | Description | Example |
|---|---|---|---|---|
| \| `spec.security` \| `.tls.ca` | string | Required | Add the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)\'s name that stores the custom CA (Certificate Authority) that you used to sign your deployment's TLS (Transport Layer Security) certificates. | `<custom-ca>` |
| \| `spec.security` \| `.certsSecretPrefix` | string | Required | Add the `<prefix>` of the secret name that contains your MongoDB deployment's TLS (Transport Layer Security) certificates. For example, if you call your deployment `my-deployment` and you set the prefix to `mdb`, you must name the TLS (Transport Layer Security) secret for the client TLS (Transport Layer Security) communications `mdb-my-deployment-cert`. Also, you must name the TLS (Transport Layer Security) secret for internal cluster authentication (if enabled) `mdb-my-deployment-clusterfile`. | `devDb` |

**Step 9: Configure ACME (Automatic Certificate Management Environment) based TLS (Transport Layer Security) certificates for your replica set resource.**

If you're using an ACME (Automatic Certificate Management Environment) based service provider such as [Let's Encrypt](https://letsencrypt.org) to issue TLS (Transport Layer Security) certificates, the provider 
might prohibit you from adding the Pod's default FQDN (fully qualified domain name)\s (`*.svc.cluster.local`)
to SAN (Subject Alternative Name)\s in the certificate.

To configure a certificate that doesn't contain the pod's FQDN (fully qualified domain name)\s:

a. Issue the certificate for an external domain. For more information, see the 
   [Let's Encrypt documentation](https://letsencrypt.org/how-it-works/) or 
   the documentation for your provider.

#. Ensure that your certificate contains all hostnames that you plan to deploy in the 
   replica set. Alternatively, you can issue a wildcard certificate for `*.<externalDomain>`.

#. To use a certificate containing only external domains for your replica set deployment, 
   you must change the default hostname used by the replica set: 

   - If you prefer to configure the hostname while creating your Kubernetes cluster, change the 
     `default domain` 
     from `cluster.local` to the external domain when creating or recreating your Kubernetes cluster. 
     Then, set this domain in your MongoDB resource by using the `spec.clusterDomain` setting.

   - Otherwise, create your MongoDB deployment with the following settings configured in your Kubernetes 
     object:

* - Key
  - Type
  - Necessity
  - Description

* - | `spec.externalAccess`
    | `.externalDomain`
  - string
  - Required
  - .. include:: /includes/facts/fact-external-domain-spec.rst

* - | `spec.externalAccess`
    | `.externalService.spec`
  - collection
  - Optional
  - Configuration for the `ServiceSpec`.

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

* - | `spec.externalAccess`
    | `.externalService.annotations`
  - collection
  - Optional
  -  .. include:: /includes/facts/fact-external-service-annotation-spec.rst

     You can specify placeholder values to customize your annotations.
     To learn more, see `spec.externalAccess.externalService.annotations`.

**Step 10: Add any additional accepted settings for a replica set deployment.**

You can also add any of the following optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file for a replica set deployment:

- `spec.additionalMongodConfig`
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
- `spec.clusterDomain`
- `spec.connectivity.replicaSetHorizons`
- `spec.featureCompatibilityVersion`
- `spec.logLevel`
- `spec.podSpec.persistence.single`
- `spec.podSpec.persistence.multiple.data`
- `spec.podSpec.persistence.multiple.journal`
- `spec.podSpec.persistence.multiple.logs`
- `spec.podSpec.podTemplate.spec.affinity.podAffinity`
- `spec.podSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.podSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.podSpec.podTemplate.metadata`
- `spec.podSpec.podTemplate.spec`

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**Step 11: Save this replica set config file with a `.yaml` extension.**

**Step 12: Start your replica set deployment.**

In any directory, invoke the following Kubernetes command to create your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 13: Track the status of your replica set deployment.**

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

### Renew TLS Certificates for a Replica Set

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

**Step 2: Renew the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for your TLS certificates.**

Run this `kubectl` command to renew an existing [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
stores the replica set's certificates:

```sh
kubectl create secret tls <prefix>-<metadata.name>-cert \
  --cert=<replica-set-tls-cert> \
  --key=<replica-set-tls-key> \
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

**Step 2: Copy the sample replica set resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired replica set configuration.

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

**Step 3: Paste the copied example to create a new replica set resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
into a new text file.

**Step 4: Change the settings to your preferred values.**

* - Key
  - Type
  - Description
  - Example

* - `metadata.name`
  - string
  - Label for this Kubernetes replica set [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

    Resource names must be 44 characters or less.

    To learn more, see `metadata.name` and
    Kubernetes documentation on
    `names`.

  - `myproject`

* - `spec.members`
  - integer
  - Number of members of the replica set.
  - `3`

* - `spec.version`
  - string
  - Version of MongoDB that this replica set should run.

    The format should be `X.Y.Z` for the Community edition and
    `X.Y.Z-ent` for the Enterprise edition.

    IMPORTANT: Ensure that you choose a compatible MongoDB
    Server version. Compatible versions
    differ depending on the base image that the MongoDB database resource
    uses.

    To learn more about MongoDB versioning, see
    release-version-numbers in the MongoDB Manual.
  - `8.0.0`

* - | `spec`
    | `.opsManager`
    | `.configMapRef`
    | `.name`
  - string
  - Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection
    configuration. The
    `spec.cloudManager.configMapRef.name` setting is an
    alias for this setting and can be used in its place.

    This value must exist on the *same* namespace as the resource
    you want to create.

    IMPORTANT: The Kubernetes Operator tracks any changes to the
    ConfigMap and reconciles the state of the `MongoDB` resource.

  - `<myconfigmap>`

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

  - `ReplicaSet`

* - `spec.persistent`
  - string
  - *Optional.*

    Flag indicating if this `MongoDB` resource should use [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for
    storage. Persistent volumes are not deleted when the
    `MongoDB` resource is stopped or restarted.

    If this value is `true`, then
    `spec.podSpec.persistence.single` is set to its
    default value of `16Gi`.

    To change your [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) configuration, configure the
    following collections to meet your deployment requirements:

    - If you want one [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the
      `spec.podSpec.persistence.single` collection.

    - If you want separate [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for data, journals, and
      logs for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), configure the following
      collections:

      - `spec.podSpec.persistence.multiple.data`
      - `spec.podSpec.persistence.multiple.journal`
      - `spec.podSpec.persistence.multiple.logs`

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

**Step 5: Add any additional accepted settings for a replica set deployment.**

You can also add any of the following optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file for a replica set deployment:

- `spec.additionalMongodConfig`
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
- `spec.clusterDomain`
- `spec.connectivity.replicaSetHorizons`
- `spec.featureCompatibilityVersion`
- `spec.logLevel`
- `spec.podSpec.persistence.single`
- `spec.podSpec.persistence.multiple.data`
- `spec.podSpec.persistence.multiple.journal`
- `spec.podSpec.persistence.multiple.logs`
- `spec.podSpec.podTemplate.spec.affinity.podAffinity`
- `spec.podSpec.podTemplate.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`
- `spec.podSpec.podTemplate.spec.affinity.nodeAffinity`
- `spec.podSpec.podTemplate.metadata`
- `spec.podSpec.podTemplate.spec`

**Warning:**

You must set `spec.clusterDomain` if your Kubernetes cluster has
a `default domain`
other than the default `cluster.local`. If you neither use the
default nor set the `spec.clusterDomain` option, the
Kubernetes Operator might not function as expected. 

**Step 6: Save this replica set config file with a `.yaml` extension.**

**Step 7: Start your replica set deployment.**

In any directory, invoke the following Kubernetes command to create your
replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 8: Track the status of your replica set deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.
