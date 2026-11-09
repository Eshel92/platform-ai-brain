<!-- Converted from tutorial/deploy-standalone.txt (reStructuredText). Includes are inlined. -->

# Deploy a Standalone MongoDB Instance

**Note:**

At any place on this page that says *Ops Manager*, you can substitute *Cloud Manager*.

**Important:**

- You can use the Kubernetes Operator to deploy MongoDB resources with
  Cloud Manager and with Ops Manager version 6.0.x or later.

- You can use the Atlas Operator
  to deploy MongoDB resources to Atlas.

You can deploy a standalone MongoDB instance for `Ops Manager` to
manage. Use standalone instances for testing and development.
*Do not* use these deployments for production systems as they lack
replication and high availability. For all production deployments
use replica sets. To learn about replica sets, see
/tutorial/deploy-replica-set.

## Prerequisites

To deploy a standalone using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

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

## Procedure

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

**Step 2: Copy the following example standalone Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).**

This is a YAML (Yet Another Markup Language) file that you can modify to meet your desired
configuration. Change the highlighted settings to match your desired
standalone configuration.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-standalone>
spec:
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
            # Must match metadata.name in ConfigMap file
  credentials: <mycredentials>
  type: Standalone
  persistent: true
...
```

**Step 3: Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification into a new text file.**

**Step 4: Configure the settings highlighted in the preceeding step as follows.**

* - Key
  - Type
  - Description
  - Example

* - `metadata.name`
  - string
  - Label for this Kubernetes standalone [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

    Resource names must be 44 characters or less.

    To learn more, see `metadata.name` and
    Kubernetes documentation on `names`.

  - `my-project`

* - `spec.version`
  - string
  - Version of MongoDB that is installed on this
    standalone.

    The format should be `X.Y.Z` for the Community edition and
    `X.Y.Z-ent` for the Enterprise edition.

    IMPORTANT: Ensure that you choose a compatible MongoDB
    Server version. Compatible versions
    differ depending on the base image that the MongoDB database resource
    uses.

    To learn more about MongoDB versioning, see
    release-version-numbers in the MongoDB Manual.
  - .. include:: /includes/facts/fact-which-appdb-version.rst

* - | `spec.opsManager`
    | `.configMapRef.name`
  - string
  - Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) with the Ops Manager connection
    configuration. The
    `spec.cloudManager.configMapRef.name` setting is an
    alias for this setting and can be used in its place.

    This value must exist on the *same* namespace as the resource
    you want to create.

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

  - `Standalone`

* - `spec.persistent`
  - string
  - *Optional.*

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

**Step 5: Add any additional accepted settings for a Standalone deployment.**

You can also add any of the following optional settings to the
[object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file for a Standalone deployment:

- `spec.additionalMongodConfig`
- `spec.logLevel`
- `spec.featureCompatibilityVersion`
- `spec.podSpec.persistence.single`
- `spec.podSpec.persistence.multiple.data`
- `spec.podSpec.persistence.multiple.journal`
- `spec.podSpec.persistence.multiple.logs`
- `spec.podSpec.podTemplate.spec.affinity.podAffinity`
- `spec.podSpec.podTemplate`
- `spec.podSpec.podTemplate.spec.affinity.nodeAffinity`

**Step 6: Save this file with a `.yaml` file extension.**

**Step 7: Start your Standalone deployment.**

Invoke the following Kubernetes command to create your standalone:

```sh
kubectl apply -f <standalone-conf>.yaml
```

**Step 8: Track the status of your standalone deployment.**

To check the status of your `MongoDB` resource, use the following
command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```

With the `-w` (watch) flag set, when the configuration changes, the output
refreshes immediately until the status phase achieves the `Running` state.
To learn more about resource deployment statuses, see /reference/troubleshooting.

To troubleshoot your sharded cluster, see:

- find-one-k8s-pod
- review-one-k8s-pod
