<!-- Converted from reference/helm-operator-settings.txt (reStructuredText). Includes are inlined. -->

# MongoDB Controllers for Kubernetes Operator Helm Installation Settings

To provide optional settings, pass them to Helm using the `--set` argument.
Use the following files that list value settings for your deployment type:

- Vanilla Kubernetes: [values.yaml](https://raw.githubusercontent.com/mongodb/helm-charts/main/charts/mongodb-kubernetes/values.yaml)
- OpenShift: [values-openshift.yaml](https://raw.githubusercontent.com/mongodb/helm-charts/main/charts/mongodb-kubernetes/values-openshift.yaml)

To learn about optional Kubernetes Operator installation settings,
see Operator Helm Installation Settings.

Run the command as in the following example and the options that you
specified will be passed to your configuration:

```sh
helm upgrade mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
  --set registry.pullPolicy='IfNotPresent'
```

## agent.name

Name of the MongoDB Agent image. This setting gets appended to agentRepo and
sets the agent-image-repo environment variable to the full URL (Uniform Resource Locator) 
from which the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) downloads
the MongoDB Agent image for database deployments. To learn more, see k8s-container-images.

The default value is **mongodb-agent**.

```yaml
agent:
  name: mongodb-agent
```

## appDb.name

Name of the Application Database image.

The default value is **mongodb-kubernetes-appdb**.

```yaml
appDb:
   name: mongodb-kubernetes-appdb
   version: 10.2.15.5958-1_4.2.11
```

## appDb.version

Version of the image that contains the MongoDB Agent that the Application
Database uses.

The default value is 10.2.15.5958-1_4.2.11.

```yaml
appDb:
   name: mongodb-kubernetes-appdb
   version: 10.2.15.5958-1_4.2.11
```

## database.name

Name of the MongoDB Enterprise Database image.

The default value is **mongodb-enterprise-database**.

```yaml
database:
   name: mongodb-enterprise-database
   version: 1.7.0
```

## database.version

Version of the MongoDB Enterprise Database image that the Kubernetes Operator
deploys.

```yaml
database:
   name: mongodb-enterprise-database
   version: 1.7.0
```

## initAppDb.name

Name of the `initContainer` image that contains the Application
Database start-up scripts and the readiness probe.

The default value is **mongodb-kubernetes-init-appdb**.

```yaml
database:
   name: mongodb-kubernetes-init-appdb
   version: 1.7.0
```

## initAppDb.version

Version of the `initContainer` image that contains the Application
Database start-up scripts and the readiness probe.

The default value is **1.7.0**.

```yaml
database:
   name: mongodb-kubernetes-init-appdb
   version: 1.7.0
```

## initDatabase.name

Name of the `initContainer` image that contains the MongoDB Agent
start-up scripts and the readiness probe.

The default value is **mongodb-kubernetes-init-database**.

```yaml
database:
   name: mongodb-kubernetes-init-database
   version: 1.7.0
```

## initDatabase.version

Version of the `initContainer` image that contains the MongoDB Agent
start-up scripts and the readiness probe.

The default value is **1.7.0**.

```yaml
database:
   name: mongodb-kubernetes-init-database
   version: 1.7.0
```

## initOpsManager.name

Version of the `initContainer` image that contains the Ops Manager 
start-up scripts and the readiness probe.

The default value is **mongodb-kubernetes-init-ops-manager**.

```yaml
database:
   name: mongodb-kubernetes-init-ops-manager
   version: 1.7.0
```

## initOpsManager.version

Version of the `initContainer` image that contains the Ops Manager 
start-up scripts and the readiness probe.

The default value is **1.7.0**.

```yaml
database:
   name: mongodb-kubernetes-init-ops-manager
   version: 1.7.0
```

## managedSecurityContext

Flag that determines whether or not the Kubernetes Operator inherits the
**securityContext** settings that your Kubernetes cluster manages.

This value must be **true** if you want to run the Kubernetes Operator
in OpenShift or in a restrictive environment.

**k8s:**

The default value is **false**.

```yaml
# Set this to true if your cluster is managing SecurityContext for you.
# If running OpenShift (Cloud, Minishift, etc.), set this to true.
managedSecurityContext: false
```

**os:**

The default value is **true**.

```yaml
# Set this to true if your cluster is managing SecurityContext for you.
# If running OpenShift (Cloud, Minishift, etc.), set this to true.
managedSecurityContext: true
```

## mongodb.appdbAssumeOldFormat

The default value is `false`, which automatically updates the image suffix.

```yaml
mongodb:
   appdbAssumeOldFormat: false
```

## mongodb.imageType

The suffix of the application database image. 

The default is `ubi8`. We recommend using only `ubi` images for consistency, but if you need to, you can change this setting to `ubuntu2204`.

```yaml
mongodb:
   imageType: ubi8
```

## multiCluster.clusterClientTimeout

Time, in seconds, the Kubernetes Operator attempts to connect to a cluster's [Kubernetes API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) endpoint. This timeout is set for all Kubernetes clusters in multi-Kubernetes cluster MongoDB deployments. If
the Kubernetes Operator doesn't get a response from the Kubernetes API server within the specified time, it logs the cluster's status as "unhealthy". To learn more, see [Troubleshooting Kubernetes Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/).

The default value is **10**.

```yaml
multiCluster:
   clusterClientTimeout: 10
```

## namespace

[namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in which you want to deploy the Kubernetes Operator.

To use a namespace other than the default, specify the namespace in
which you want to deploy the Kubernetes Operator. 

The default value is **mongodb**.

```yaml
# Name of the Namespace to use
namespace: mongodb
```

## needsCAInfrastructure

Determines whether Kubernetes creates a [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) that allows the Kubernetes Operator
to sign TLS (Transport Layer Security) certificates using
the `certificates.k8s.io` API.

```yaml
needsCAInfrastructure: true
```

The default value is **true**.

## operator.deployment_name

Name of the Kubernetes Operator container.

The default value is **mongodb-kubernetes-operator**.

```yaml
operator:
   deployment_name: mongodb-kubernetes-operator
```

## operator.env

Label for the Kubernetes Operator\s deployment environment. This value
affects the default timeouts and the logging level and format:

| If the value is | Log Level is set to | Log Format is set to |
|---|---|---|
| `dev` | debug | text |
| `prod` | info | json |

The default value is **prod**.

```yaml
operator:
   # Execution environment for the operator, dev or prod.
   # Use dev for more verbose logging
   env: prod
```

## operator.maxConcurrentReconciles

The maximum number of concurrent reconciliatios the Kubernetes Operator can perform.
It sets [MaxConcurrentReconciles](https://pkg.go.dev/github.com/kubernetes-sigs/controller-runtime/pkg/controller#Options).
To learn more, see the Kubernetes Operator 
Deploy Multiple MongoDB Replica Sets.

**Example:**

```yaml
operator:
  # Control how many reconciles can be performed in parallel.
  # Increasing the number of concurrent reconciliations decreases the time needed to reconcile all watched resources,
  # but it might result in request load spikes and increased load on the Ops Manager API, and the Kubernetes API server generally. 
  maxConcurrentReconciles: 10
```

## operator.mdbDefaultArchitecture

Determines the container architecture used by all your deployments:

- The default non-static containers that download the MongoDB binary at runtime, or
-  static-containers that are immutable at runtime.

The default is `non-static`.

To enable static containers, set to `static`.

**Note:**

This setting applies to all your deployments, including existing deployments.
To enable static containers for a single deployment, 
use `metadata.annotations.mongodb.com/v1.architecture` in 
the MongoDB resource instead.

```yaml
operator.mdbDefaultArchitecture: static
```

## operator.name

Name that Kubernetes assigns to Kubernetes Operator objects, such as Deployments,
ServiceAccounts, Roles, and Pods.

This value also corresponds to the name of the container registry where
the Kubernetes Operator is located.

The default value is **mongodb-kubernetes-operator**.

```yaml
operator:
   name: mongodb-kubernetes-operator
```

## operator.podSecurityContext

Sets the security context of the Kubernetes Operator pod. You can learn more about pod 
security contexts in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

```yaml
operator:
   podSecurityContext:
      runAsUser: 2000
      runAsNonRoot: true
```

**Note:**

If `managedSecurityContext` is set to `true`, the `operator.podSecurityContext` is not used.

## operator.securityContext

Sets the security context of the Kubernetes Operator container. You can learn more about container 
security contexts in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

```yaml
operator:
   securityContext: {} # Defaults to empty object
```

**Note:**

If `managedSecurityContext` is set to `true`, the `operator.securityContext` is not used.

## operator.telemetry

Enables the Kubernetes Operator to collect and send telemetry.
The default for the following settings is `true`. 

```yaml
operator:
  telemetry:
    # Enables telemetry. Setting this to "false" will stop all telemetry.
    enabled: true
    # Adds RBAC clusterRole for kube-system UID detection for the Kubernetes cluster UID.
    # Adds RBAC clusterRole for RBAC for nodes. We are listing exactly one node to detect the cluster provider (for example, eks).
    # Adds RBAC clusterRole for /version query for detecting Kubernetes server version. 
    installClusterRole: true
    collection:
      # Controls how often the Kubernetes Operator collects and saves the data to the telemetry ConfigMap. It doesn't control whether this data is sent to MongoDB for analysis.
      # Valid time units for frequency are "m", or "h". Anything less than one minute defaults to 1h.
      frequency: 1h
      # Enables the Kubernetes Operator to collect and send cluster-level telemetry.
      # Note: the cluster UUID is unique but random and MongoDB has no way to map this to a customer.
      clusters:
        enabled: true
      # Enables the Kubernetes Operator to collect and send deployment-level telemetry.
      deployments:
        enabled: true
      # Enables the Kubernetes Operator to collect and send Kubernetes Operator-level telemetry.
      operators:
        enabled: true
    # Enables sending the collected telemetry to MongoDB.
    send:
      enabled: true
      # Controls how often the Kubernetes Operator sends the collected the data to MongoDB for analysis.
      # Valid time units are "h". Anything less than one hour defaults to 168h, which is one week.
      frequency: 168h
```

## operator.vaultSecretBackend.enabled

Determines whether the Kubernetes Operator stores secrets in [HashiCorp Vault](https://www.vaultproject.io/).
To learn more, see k8s-set-secret-storage-tool.
If you are using TLS (Transport Layer Security) with Vault, you must also specify
operator.vaultSecretBackend.tlsSecretRef.

The default value is **false**.

```yaml
operator:
   # Set the following setting to "true" so that the MongoDB Kubernetes Operator stores secrets in Vault.
   vaultSecretBackend: false
```

## operator.vaultSecretBackend.tlsSecretRef

Required if you are using TLS (Transport Layer Security) with Vault. The TLS secret used in
your Vault configuration that contains a `ca.crt` entry.
The content of the `ca.crt` entry must match the certificate of
the CA (Certificate Authority) used to generate the Vault TLS certificates.
The Kubernetes Operator stores this TLS secret in its secret storage tool.
To learn more, see Configure Secret Storage.
Requires that operator.vaultSecretBackend.enabled
is set to `true`.

```yaml
operator:
   vaultSecretBackend: true
      tlsSecretRef: "vault-tls-secret"
```

## operator.version

Version of the Kubernetes Operator that you want to deploy.

The default value is **1.7.0**.

```yaml
operator:
   version: 1.7.0
```

## operator.watchNamespace

Namespaces that the Kubernetes Operator watches for `MongoDB` resource
changes. If this [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) differs from the default, ensure that
the Kubernetes Operator ServiceAccount `can access`
this namespace.

- To watch *all namespaces*, specify **\*** and assign the [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) to the
  `mongodb-kubernetes-operator` ServiceAccount that you use to run the
  Kubernetes Operator.

- To watch a *subset of all namespaces*, specify them in a
  comma-separated list, escape each comma with a backslash,
  and surround the list in quotes, such as
  `"operator.watchNamespace=ns1\,ns2"`.

Watching a subset of namespaces is useful in deployments where a single
Kubernetes Operator instance watches a different cluster resource type.
For example, you can configure the Kubernetes Operator to watch `MongoDB` resources
in one subset of namespaces, and to watch `MongoDBMultiCluster` resources in another
subset of namespaces. To avoid race conditions during resource reconciliation,
for each custom resource type that you want the Kubernetes Operator to watch,
ensure that you set scope to a distinct subset of namespaces.

**Important:**

To deploy Ops Manager and `MongoDB` resources to one or more [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) other
than the one where you deploy the Kubernetes Operator,
see k8s-deployment-scopes for values you must use and
additional steps you might have to perform.

The default value is **<metadata.namespace>**.

```yaml
# Watch one namespace
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
   --set operator.watchNamespace='namespace-to-watch' <...>
```

```yaml
# Watch both namespace-a and namespace-b
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
   --set operator.watchNamespace="namespace-a\,namespace-b"
```

```yaml
# Operator with name `mongodb-kubernetes-operator-qa-envs` will
# watch ns-dev, ns-qa and ns-uat namespaces

helm install mongodb-kubernetes-operator-qa-envs mongodb/mongodb-kubernetes \
   --set operator.watchNamespace="ns-dev\,ns-qa\,ns-uat"
```

```yaml
# Operator with name `mongodb-kubernetes-operator-staging` will
# watch ns-staging and ns-pre-prod
helm install mongodb-kubernetes-operator-staging mongodb/mongodb-kubernetes --set operator.watchNamespace="ns-staging\,ns-pre-prod"
```

## operator.watchedResources

Custom resources that the Kubernetes Operator watches.

The Kubernetes Operator installs the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) for and watches only the resources you specify.

The Kubernetes Operator accepts the following values:

| Value | Description |
|---|---|
| `mongodb` | Install the CustomResourceDefinitions for database resources and watch those resources. |
| `mongodbusers` | Install the CustomResourceDefinitions for MongoDB user resources and watch those resources. |
| `opsmanagers` | Install the CustomResourceDefinitions for Ops Manager resources and watch those resources. |

```yaml
operator:
   watchedResources:
      - mongodbusers
      - mongodb 
      - opsmanagers
```

## opsManager.name

Name of the Ops Manager image.

The default value is **mongodb-enterprise-ops-manager**.

```yaml
opsManager:
   name: mongodb-enterprise-ops-manager
```

## registry.agent

URL (Uniform Resource Locator) for the [Quay](https://quay.io/) container registry for MongoDB images. The agent-name-helm 
gets appended and
sets the agent-image-repo environment variable to the full URL (Uniform Resource Locator) 
from which the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) downloads
the MongoDB Agent image for database deployments. To learn more, see k8s-container-images.

The default value is **quay.io/mongodb**.

```yaml
registry:
agent: quay.io/mongodb/
```

## registry.appDb

URL (Uniform Resource Locator) of the repository from which the Kubernetes Operator downloads
the Application Database image.

**k8s:**

The default value is **quay.io/mongodb**.

```yaml
registry:
   appDb: quay.io/mongodb
```

**os:**

The default value is **registry.connect.redhat.com/mongodb**.

```yaml
registry:
   appDb: registry.connect.redhat.com/mongodb
```

## registry.imagePullSecrets

[secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the credentials required to pull
images from the repository.

**Important:**

OpenShift requires this setting. Define it in the
`imagePullSecrets` setting in this file or pass it when you install
the Kubernetes Operator using Helm.
If you use the Kubernetes Operator to deploy MongoDB resources to
multiple namespaces or with a
cluster-wide scope, create the secret
only in the namespace where you installed the Kubernetes Operator.
The Kubernetes Operator synchronizes the secret across all watched
namespaces.

```yaml
registry:
# Specify the secret in the ``imagePullSecrets`` setting. If you
# use the MongoDB Kubernetes Operator to deploy MongoDB resources
# into multiple namespaces, create the secret only in the namespace
# where you installed the Operator. The Operator synchronizes
# the secret across all watched namespaces.
   imagePullSecrets: <openshift-pull-secret>
```

## registry.initAppDb

URL (Uniform Resource Locator) of the repository from which the `initContainer` image that
contains the Application Database start-up scripts and the readiness
probe is downloaded.

**k8s:**

The default value is **quay.io/mongodb**.

```yaml
registry:
   initAppDb: quay.io/mongodb
```

**os:**

The default value is **registry.connect.redhat.com/mongodb**.

```yaml
registry:
   initAppDb: registry.connect.redhat.com/mongodb
```

## registry.initOpsManager

URL (Uniform Resource Locator) of the repository from which the `initContainer` image that
contains the Ops Manager start-up scripts and the readiness probe is 
downloaded.

**k8s:**

The default value is **quay.io/mongodb**.

```yaml
registry:
   initOpsManager: quay.io/mongodb
```

**os:**

The default value is **registry.connect.redhat.com/mongodb**.

```yaml
registry:
   initOpsManager: registry.connect.redhat.com/mongodb
```

## registry.operator

Repository from which the Kubernetes Operator image is pulled.
Specify this value if you want to pull the Kubernetes Operator image
from a private repository.

**k8s:**

The default value is **quay.io/mongodb**.

```yaml
registry:
   operator: quay.io/mongodb
```

**os:**

The default value is **registry.connect.redhat.com/mongodb**.

```yaml
registry:
   operator: registry.connect.redhat.com/mongodb
```

## registry.opsManager

URL (Uniform Resource Locator) of the repository from which the image for an Ops
Manager resource is downloaded.

**k8s:**

The default value is **quay.io/mongodb**.

```yaml
registry:
   opsManager: quay.io/mongodb
```

**os:**

The default value is **registry.connect.redhat.com/mongodb**.

```yaml
registry:
   opsManager: registry.connect.redhat.com/mongodb
```

## operator.resources.requests

Specifications for the [CPU and memory consumption limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) of the Kubernetes Operator.

**Example:**

```yaml
# operator cpu requests and limits
resources:
  requests:
    cpu: 500m
    memory: 200Mi
```

## operator.resources.limits

Specifications for the [CPU and memory consumption limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) of the Kubernetes Operator.

**Example:**

```yaml
# operator cpu requests and limits
resources:
  limits:
    cpu: 1100m
    memory: 1Gi
```

## webhook.installClusterRole

Flag allows you to configure user `validating admission
webhooks` 
for Kubernetes `cluster roles` .

Set this flag to `false` if your deployment doesn't allow Kubernetes cluster
roles.

The default value is **true**.

```yaml
webhook:
  installClusterRole: false
```
