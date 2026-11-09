<!-- Converted from reference/kubectl-operator-settings.txt (reStructuredText). Includes are inlined. -->

# MongoDB Controllers for Kubernetes Operator [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) and [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) Installation Settings

To provide optional settings, edit the YAML (Yet Another Markup Language) file that corresponds to
your deployment type in the directory where you cloned the
Kubernetes Operator repository:

- Vanilla Kubernetes using [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/): **mongodb-kubernetes.yaml**
- OpenShift using [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html): **mongodb-kubernetes-openshift.yaml**

If the setting that you want to add doesn't exist in the YAML (Yet Another Markup Language) file,
add it as a new array of key-value pair mappings in the 
**spec.template.spec.containers.name.env.** collection:

- Set the value of the **spec.template.spec.containers.name.env.name**
  key to the setting's name.
- Set the value of the **spec.template.spec.containers.name.env.value** 
  key to the setting's value.

To fill in values for container images, see Container Images.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: INIT_APPDB_IMAGE_REPOSITORY
              value: quay.io/mongodb/mongodb-kubernetes-init-appdb
```

## AGENT_IMAGE

URL (Uniform Resource Locator) of the repository from which the Kubernetes Operator downloads
the MongoDB Agent image for non-static database deployments. Include the MongoDB Agent 
version. To learn more, see k8s-container-images.

```yaml
spec:
  template:
     spec:
      serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: AGENT_IMAGE
               value: quay.io/mongodb/mongodb-agent:<version>
```

## APPDB_AGENT_VERSION

Version of the image that contains the MongoDB Agent that the Application
Database uses.

The default value is 10.2.15.5958-1_4.2.11.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: APPDB_AGENT_VERSION
              value: 10.2.15.5958-1_4.2.11
```

## APPDB_IMAGE_REPOSITORY

URL (Uniform Resource Locator) of the repository from which the Kubernetes Operator downloads
the Application Database image.

```yaml
spec:
  template:
     spec:
      serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: APPDB_IMAGE_REPOSITORY
               value: quay.io/mongodb/mongodb-kubernetes-appdb-ubi
```

## CLUSTER_CLIENT_TIMEOUT

Time, in seconds, the Kubernetes Operator attempts to connect to a cluster's [Kubernetes API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) endpoint. This timeout is set for all Kubernetes clusters in multi-Kubernetes cluster MongoDB deployments. If
the Kubernetes Operator doesn't get a response from the Kubernetes API server within the specified time, it logs the cluster's status as "unhealthy". To learn more, see [Troubleshooting Kubernetes Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/).

The default value is **10**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: CLUSTER_CLIENT_TIMEOUT
              value: 10
```

## DATABASE_VERSION

Version of the MongoDB Enterprise Database image that the Kubernetes Operator
deploys.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: DATABASE_VERSION
              value: 1.7.0
```

## IMAGE_PULL_POLICY

`Pull policy` for the MongoDB
Enterprise database image the Kubernetes Operator deploys.

The Kubernetes Operator accepts the following values:  **Always**,
**IfNotPresent**, **Never**.

The default value is **Always**.

## INIT_APPDB_IMAGE_REPOSITORY

URL (Uniform Resource Locator) of the repository from which the `initContainer` image that
contains the Application Database start-up scripts and the readiness
probe is downloaded.

```yaml
spec:
  template:
     spec:
       serviceAccountName: mongodb-kubernetes-operator
         containers:
           - name: mongodb-kubernetes-operator
             image: <operatorVersionUrl>
             imagePullPolicy: <policyChoice>
             env:
               - name: INIT_APPDB_IMAGE_REPOSITORY
                 value: quay.io/mongodb/mongodb-kubernetes-init-appdb
```

## INIT_APPDB_VERSION

Version of the `initContainer` image that contains the Application
Database start-up scripts and the readiness probe.

The default value is **1.7.0**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: INIT_APPDB_VERSION
              value: 1.7.0
```

## INIT_DATABASE_IMAGE_REPOSITORY

URL (Uniform Resource Locator) of the repository from which the `initContainer` image that
contains the MongoDB Agent start-up scripts and the readiness probe is
downloaded.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: INIT_DATABASE_IMAGE_REPOSITORY
              value: quay.io/mongodb/mongodb-kubernetes-init-database
```

## INIT_DATABASE_VERSION

Version of the `initContainer` image that contains the MongoDB Agent
start-up scripts and the readiness probe.

The default value is **1.7.0**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: INIT_DATABASE_VERSION
              value: 1.7.0
```

## INIT_OPS_MANAGER_IMAGE_REPOSITORY

URL (Uniform Resource Locator) of the repository from which the `initContainer` image that
contains the Ops Manager start-up scripts and the readiness probe is 
downloaded.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: INIT_OPS_MANAGER_IMAGE_REPOSITORY
             value: quay.io/mongodb/mongodb-kubernetes-init-ops-manager
```

## INIT_OPS_MANAGER_VERSION

Version of the `initContainer` image that contains the Ops Manager 
start-up scripts and the readiness probe.

The default value is **1.7.0**.

```yaml
spec:
  template:
    spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
              - name: INIT_OPS_MANAGER_VERSION
                value: 1.7.0
```

## LOG_FILE_PATH

Path to the rotated `readiness.log` backup files maintained by the 
Readiness Probe.

The default value is `/var/log/mongodb-mms-automation/readiness.log`.

```yaml
spec:
  template:
    spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
              - name: LOG_FILE_PATH
                value: /var/log/mongodb-mms-automation/readiness.log
```

## MANAGED_SECURITY_CONTEXT

Flag that determines whether or not the Kubernetes Operator inherits the
**securityContext** settings that your Kubernetes cluster manages.

This value must be **true** if you want to run the Kubernetes Operator
in OpenShift or in a restrictive environment.

**k8s:**

The default value is **false**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: MANAGED_SECURITY_CONTEXT
              value: false
```

**os:**

The default value is **true**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: MANAGED_SECURITY_CONTEXT
              value: true
```

## MDB_AGENT_IMAGE_REPOSITORY

URL (Uniform Resource Locator) of the repository from which the Kubernetes Operator downloads
the MongoDB Agent image for database deployments. To learn more, see k8s-container-images.

```yaml
spec:
  template:
     spec:
      serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: MDB_AGENT_IMAGE_REPOSITORY
               value: quay.io/mongodb/mongodb-agent
```

## MDB_APPDB_ASSUME_OLD_FORMAT

The default value is `false`, which automatically updates the image suffix. 

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: MDB_APPDB_ASSUME_OLD_FORMAT
              value: false
```

## MDB_AUTOMATIC_RECOVERY_ENABLE

Flag that determines whether or not the Kubernetes Operator 
enables automatic recovery for `MongoDB` resources 
per Pod. 

The default value is **true**.

```yaml
spec:
  template:
     spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: MDB_AUTOMATIC_RECOVERY_ENABLE
               value: false
```

## MDB_AUTOMATIC_RECOVERY_BACKOFF_TIME_S

Number of seconds that a custom resource can remain in a 
`Pending` or `Failed` state before the Kubernetes Operator 
automatically recovers your `MongoDB` resources.

The default value
is **1200** seconds (20 minutes).

To disable automatic recovery, set the 
MDB_AUTOMATIC_RECOVERY_ENABLE 
environment variable to `false`.

```yaml
spec:
  template:
     spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env: 
             - name: MDB_AUTOMATIC_RECOVERY_BACKOFF_TIME_S
               value: 3600
```

## MDB_DEFAULT_ARCHITECTURE

Determines the container architecture used by all your deployments:

- The default non-static containers that download the MongoDB binary at runtime, or
-  static-containers that are immutable at runtime.

To enable static containers for a single deployment, 
use `metadata.annotations.mongodb.com/v1.architecture` in 
the MongoDB resource instead.

The default is `non-static`.

To enable static containers, set to `static`.

```yaml
spec:
  template:
     spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env: 
             - name: MDB_DEFAULT_ARCHITECTURE
               value: static
```

## MDB_IMAGE_TYPE

The suffix of the application database image. 

The default is `-ubi8`.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: MDB_IMAGE_TYPE
              value: ubi8
```

## MDB_WITH_AGENT_FILE_LOGGING

Controls whether log files are output to standard output, such as when 
you run `kubectl describe`.

The default is `true`.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: MDB_WITH_AGENT_FILE_LOGGING
             value: true
```

## MDB_MAX_CONCURRENT_RECONCILES

The number of concurrent reconciliation processes the Kubernetes Operator can perform.

**Example:**

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - env:
          - name: MDB_MAX_CONCURRENT_RECONCILES
            value: "10"
```

## MDB_OPERATOR_TELEMETRY_ENABLED

Enables the Kubernetes Operator to collect and send telemetry to MongoDB for analysis. 
mdb-operator-telemetry-send-enabled must also be set to `true` for the 
Kubernetes Operator to send telemetry to MongoDB.

The default is `true`. If set to `false`, the Kubernetes Operator doesn't collect or send telemetry to MongoDB.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - env:
          - name: MDB_OPERATOR_TELEMETRY_ENABLED
            value: "true"
```

## MDB_OPERATOR_TELEMETRY_SEND_ENABLED

Enables the Kubernetes Operator to send telemetry to MongoDB for analysis. 
mdb-operator-telemetry-enabled must also be set to `true` for the Kubernetes Operator to send telemetry.

The default is `true`. If set to `false`, the Kubernetes Operator collects telemetry 
in the ConfigMap named `mongodb-kubernetes-operator-telemetry`, but doesn't send 
it to MongoDB.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
         - env:
          - name: MDB_OPERATOR_TELEMETRY_SEND_ENABLED
            value: "true"
```

## MDB_PROPAGATE_PROXY_ENV

Enables the Kubernetes Operator to function in proxy-restricted environments. Set 
this variable to `true` along with the standard proxy settings (`HTTP_PROXY`,
`HTTPS_PROXY`, `NO_PROXY`) to propagate these proxy settings from your 
Kubernetes Operator Pod to the MongoDB Agents, allowing all components to communicate
effectively through the specified proxies.

**Example:**

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - env:
          - name: MDB_PROPAGATE_PROXY_ENV
            value: "true"
          - name: HTTP_PROXY
            value: "http://example-http-proxy:7312"
          - name: HTTPS_PROXY
            value: "https://secure-proxy:3242"
          - name: NO_PROXY
            value: "google.com"
```

## MONGODB_ENTERPRISE_DATABASE_IMAGE

URL (Uniform Resource Locator) of the MongoDB Enterprise Database image that the Kubernetes Operator
deploys.

```yaml
spec:
  template:
     spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: MONGODB_ENTERPRISE_DATABASE_IMAGE
               value: quay.io/mongodb/mongodb-kubernetes-database
```

## MONGODB_REPO_URL

URL (Uniform Resource Locator) of the base repository for official MongoDB server images.

The default value is `quay.io/mongodb`.

```yaml
spec:
  template:
     spec:
      serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: MONGODB_REPO_URL
               value: quay.io/mongodb
```

## OPERATOR_ENV

Label for the Kubernetes Operator\s deployment environment. This value
affects the default timeouts and the logging level and format:

| If the value is | Log Level is set to | Log Format is set to |
|---|---|---|
| `dev` | debug | text |
| `prod` | info | json |

The default value is **prod**.

## OPS_MANAGER_IMAGE_PULL_POLICY

`Pull policy` for the
Ops Manager images the Kubernetes Operator deploys.

The Kubernetes Operator accepts the following values: **Always**,
**IfNotPresent**, and **Never**.

The default value is **Always**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: OPS_MANAGER_IMAGE_PULL_POLICY
              value: Always
```

## OPS_MANAGER_IMAGE_REPOSITORY

URL (Uniform Resource Locator) of the repository from which the image for an Ops
Manager resource is downloaded.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: OPS_MANAGER_IMAGE_REPOSITORY
             value: quay.io/mongodb/mongodb-enterprise-ops-manager-ubi
```

## READINESS_PROBE_LOGGER_BACKUPS

The number of rotated `readiness.log` backup files maintained by the 
Readiness Probe.

The default value is **5**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: READINESS_PROBE_LOGGER_BACKUPS
             value: 1
```

## READINESS_PROBE_LOGGER_COMPRESS

Controls whether the rotated `readiness.log` backup files maintained by the 
Readiness Probe are compressed to `readiness.log.gz` files.

The default value is `false`, which leaves the `readiness.log` files uncompressed.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: READINESS_PROBE_LOGGER_COMPRESS
             value: true
```

## READINESS_PROBE_LOGGER_MAX_SIZE

The maximum size of the `readiness.log` file in MB. 

The default value is **100**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: READINESS_PROBE_LOGGER_MAX_SIZE
             value: 125
```

## READINESS_PROBE_LOGGER_MAX_AGE

The maximum number of days to retain rotated `readiness.log` files,
starting with the date in the file timestamp. If set to **0**, the
Kubernetes Operator doesn't remove `readiness.log` files on the basis of
age, instead relying on `READINESS_PROBE_LOGGER_BACKUPS` to determine
retention.

The default value is **0**.

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
           - name: READINESS_PROBE_LOGGER_MAX_AGE
             value: 3
```

## WATCH_NAMESPACE

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
