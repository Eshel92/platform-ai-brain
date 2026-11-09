<!-- Converted from tutorial/install-k8s-operator.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Install the MongoDB Controllers for Kubernetes Operator

## Prerequisites and Considerations

Before you install the Kubernetes Operator, make sure you
plan for your installation:

- Choose a deployment topology.
- Read the Considerations.
- Complete the Prerequisites.

**Note:**

This tutorial presumes some knowledge of Kubernetes and links to
relevant Kubernetes documentation. If you are unfamiliar
with Kubernetes, please review that documentation first.

## Install with Kubernetes

The installation procedure varies based on how you want to configure your
environment:

**kubectl:**

**Note:** Use the same namespace throughout

By default, the Kubernetes Operator deploys all resources in your Kubernetes
cluster to the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) `mongodb`. You can deploy Kubernetes Operator
resources to a different namespace by editing all values for
`metadata.namespace` in `mongodb-kubernetes.yaml`. You must also
update the `subjects[0].namespace` value in every `RoleBinding`
and `ClusterRoleBinding` in the same file. If you omit this value,
the bindings look for the `ServiceAccount` in the default `mongodb`
namespace and can't find it:

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mongodb-kubernetes-operator
  namespace: production

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: mongodb-kubernetes-operator
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: mongodb-kubernetes-operator
subjects:
  - kind: ServiceAccount
    name: mongodb-kubernetes-operator
    namespace: production

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb-kubernetes-operator
  namespace: production

---
# Example truncated
---
...
```

**Step 1: Customize the Kubernetes Operator YAML (Yet Another Markup Language) before installing it.**

To learn about optional Kubernetes Operator installation settings,
see Operator kubectl and oc Installation Settings.

**Note:**

To enable the Public Preview of static containers, 
which improve and simplify security, see static-containers. 
We don't recommend using this feature in production while it's 
in Public Preview. To learn more, see [Preview Features](https://www.mongodb.com/docs/preview-features/). 

**Step 2: Apply the MongoDB CRDs.**

Run the following `kubectl` command to deploy your chosen version of the CRDs to your Kubernetes cluster:

```
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 3: Install the MongoDB Kubernetes Operator.**

Run the following `kubectl` command to deploy your chosen version of the Kubernetes Operator to your Kubernetes cluster:

```sh
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes.yaml
```

**helmonline:**

Use the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts).

**Note:** Helm Chart Repository Deprecation

Installing the Kubernetes Operator from the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts)
repository is deprecated and will be removed in the MCK
version 2.0. To install the Helm chart from the OCI-compliant
registry instead, see the "Using Helm (OCI-Compliant
Registry)" tab.

**Step 1: Add the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts).**

You can add the Kubernetes Operator Helm Chart locally by running:

```sh
helm repo add mongodb https://mongodb.github.io/helm-charts
```

**Step 2: Customize your Helm Chart before deploying it.**

To learn about optional Kubernetes Operator 
installation settings, see Operator Helm Installation Settings.

**Step 3: Apply the CRDs to your Kubernetes cluster.**

Run the following `kubectl` command with your desired Kubernetes Operator version to deploy the CRDs to your Kubernetes cluster:

```
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 4: Deploy the Kubernetes Operator.**

Run the following `helm` command to deploy the Kubernetes Operator to the 
default namespace in your Kubernetes cluster:

```sh
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes
```

You can pass the `--namespace` and `--create-namespace` flags to deploy 
the Kubernetes Operator to a non-default namespace, like so:

```
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
--namespace mongodb \
--create-namespace
```

### Install a Specific Daily Build with Helm

MongoDB rebuilds Kubernetes Operator images every day to integrate the 
latest security and OS updates.

By default, `helm` installs the latest build for the version of 
the Kubernetes Operator you specify.

To install an earlier build, specify the build ID as a parameter with 
`--set build=<build-id>`. Build IDs are always in the format 
`-b<YYYYMMDD>T000000Z`, where `<YYYYMMDD>` is the date that the 
build you want to use was created.

**Example:**

This example shows how to install the Kubernetes Operator with the latest 
image:

```sh
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes
```

This example shows how to install the Kubernetes Operator with the image 
created at midnight on February 5th, 2021:

```sh
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
  --set build=-b20210205T000000Z
```

**Note:**

MongoDB recommends using the default (latest) build.

**helmoci:**

MongoDB also publishes the Kubernetes Operator Helm chart to an
OCI-compliant container registry at
`quay.io/mongodb/helm-charts`. When you install from this
registry, you reference the chart directly instead of adding the
Helm chart repository.

**Step 1: Customize your Helm chart before deploying it.**

To learn about optional Kubernetes Operator installation
settings, see Operator Helm Installation Settings.

**Step 2: Apply the CRDs to your Kubernetes cluster.**

Run the following `kubectl` command with your desired
Kubernetes Operator version to deploy the CRDs to your Kubernetes
cluster:

```
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 3: Deploy the Kubernetes Operator.**

Run the following `helm` command to deploy the
Kubernetes Operator to the default namespace in your Kubernetes
cluster:

```sh
helm upgrade --install mongodb-kubernetes-operator \
   oci://quay.io/mongodb/helm-charts/mongodb-kubernetes
```

To deploy the Kubernetes Operator to a non-default namespace,
pass the `--namespace` and `--create-namespace` flags:

```sh
helm upgrade --install mongodb-kubernetes-operator \
   oci://quay.io/mongodb/helm-charts/mongodb-kubernetes \
   --namespace mongodb \
   --create-namespace
```

## Install with OpenShift

Before you begin, ensure that the `MANAGED_SECURITY_CONTEXT` flag is set
to `true` when you deploy the Kubernetes Operator to OpenShift. This value is
pre-defined in the [values-openshift.yaml](https://raw.githubusercontent.com/mongodb/helm-charts/main/charts/mongodb-kubernetes/values-openshift.yaml) file.

The installation procedure varies based on how you want to configure your
environment:

**os:**

**Note:** Use the same namespace throughout

By default, the Kubernetes Operator deploys all resources in your Kubernetes
cluster to the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) `mongodb`. You can deploy Kubernetes Operator
resources to a different namespace by editing all values for
`metadata.namespace` in `mongodb-kubernetes-openshift.yaml`. You
must also update the `subjects[0].namespace` value in every
`RoleBinding` and `ClusterRoleBinding` in the same file. If you
omit this value, the bindings look for the `ServiceAccount` in the
default `mongodb` namespace and can't find it:

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mongodb-kubernetes-operator
  namespace: production

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: mongodb-kubernetes-operator
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: mongodb-kubernetes-operator
subjects:
  - kind: ServiceAccount
    name: mongodb-kubernetes-operator
    namespace: production

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb-kubernetes-operator
  namespace: production

---
# Example truncated
---
...
```

**Step 1: Clone the MongoDB Controllers for Kubernetes Operator repository and check out the tag for the current release.**

Invoke the following `git` commands:

```sh
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
```

**Step 2: Navigate to the directory in which you cloned the MongoDB Controllers for Kubernetes Operator repository.**

For example, if you cloned the repository in your home directory, run: 

```sh
cd ~/mongodb-kubernetes 
```

**Step 3: Install the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) for MongoDB deployments.**

Invoke the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command:

```sh
oc apply -f crds.yaml
```

**Step 4: Customize the Kubernetes Operator YAML (Yet Another Markup Language) before installing it.**

To learn about optional Kubernetes Operator installation settings,
see Operator kubectl and oc Installation Settings.

**Note:**

To enable the Public Preview of static containers, 
which improve and simplify security, see static-containers. 
We don't recommend using this feature in production while it's 
in Public Preview. To learn more, see [Preview Features](https://www.mongodb.com/docs/preview-features/). 

**Step 5: Add your `<openshift-pull-secret>` to the `ServiceAccount` definitions in the Kubernetes Operator YAML (Yet Another Markup Language) before installing it.**

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: enterprise-operator

  namespace: mongodb

imagePullSecrets:
 - name: <openshift-pull-secret>

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mongodb-kubernetes-appdb

  namespace: mongodb

imagePullSecrets:
 - name: <openshift-pull-secret>

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mongodb-kubernetes-database-pods

  namespace: mongodb

imagePullSecrets:
 - name: <openshift-pull-secret>
```

To learn more, see the `registry.imagePullSecrets` setting in the
Helm installation settings.

**Step 6: Install the Kubernetes Operator using the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command:**

Invoke the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command:

```sh
oc apply -f mongodb-kubernetes-openshift.yaml
```

**os-helm-online:**

Use the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts).

**Note:** Helm Chart Repository Deprecation

Installing the Kubernetes Operator from the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts)
repository is deprecated and will be removed in the MCK
version 2.0. Install the Helm chart from the OCI-compliant
registry at `quay.io/mongodb/helm-charts` instead.

You can install the Kubernetes Operator with [Helm 3](https://helm.sh/docs/intro/install/).

**Step 1: Add the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) repository to Helm.**

```sh
helm repo add mongodb https://mongodb.github.io/helm-charts
```

**Step 2: Install the Kubernetes Operator using `helm`.**

Install [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts):

```sh
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
  --values https://raw.githubusercontent.com/mongodb/helm-charts/main/charts/mongodb-kubernetes/values-openshift.yaml
```

Use the [values-openshift.yaml](https://raw.githubusercontent.com/mongodb/helm-charts/main/charts/mongodb-kubernetes/values-openshift.yaml)
settings. To learn about optional Kubernetes Operator installation settings,
see Operator Helm Installation Settings.

**Note:**

To enable the Public Preview of static containers, 
which improve and simplify security, see static-containers. 
We don't recommend using this feature in production while it's 
in Public Preview. To learn more, see [Preview Features](https://www.mongodb.com/docs/preview-features/). 

### Install a Specific Daily Build with Helm

MongoDB rebuilds Kubernetes Operator images every day to integrate the 
latest security and OS updates.

By default, `helm` installs the latest build for the version of 
the Kubernetes Operator you specify.

To install an earlier build, specify the build ID as a parameter with 
`--set build=<build-id>`. Build IDs are always in the format 
`-b<YYYYMMDD>T000000Z`, where `<YYYYMMDD>` is the date that the 
build you want to use was created.

**Example:**

This example shows how to install the Kubernetes Operator with the latest 
image:

```sh
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes
```

This example shows how to install the Kubernetes Operator with the image 
created at midnight on February 5th, 2021:

```sh
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
  --set build=-b20210205T000000Z
```

**Note:**

MongoDB recommends using the default (latest) build.

## Verify the Installation

To verify that the Kubernetes Operator installed correctly, run the 
following command and verify the output:

**kubectl-verify:**

```sh
kubectl describe deployments mongodb-kubernetes-operator -n <metadata.namespace>
```

**oc-verify:**

```sh
oc describe deployments mongodb-kubernetes-operator -n <metadata.namespace>
```

By default, deployments exist in the `mongodb` namespace. If the 
following error message appears, ensure you use the correct 
namespace:

```sh
Error from server (NotFound): deployments.apps "mongodb-kubernetes-operator" not found
```

To troubleshoot your Kubernetes Operator, see review-k8s-op-logs
and other troubleshooting topics.

**Important:**

If you need to remove the Kubernetes Operator or the
namespace, you first must
remove MongoDB resources.

## Next Steps

After installing the MongoDB Controllers for Kubernetes Operator, you can:

- Create an instance of Ops Manager

- Configure the Kubernetes Operator to deploy MongoDB resources
