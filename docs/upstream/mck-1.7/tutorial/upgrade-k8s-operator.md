<!-- Converted from tutorial/upgrade-k8s-operator.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Upgrade the MongoDB Controllers for Kubernetes Operator

The following procedure outlines how to upgrade the Kubernetes Operator
to its latest version. This upgrade process parallels the Kubernetes Operator 
installation process.

## Upgrade the MongoDB Controllers for Kubernetes Operator Running in Kubernetes

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

**Step 1: Update the MongoDB CRDs.**

Run the following `kubectl` command to deploy your chosen version of the 
CRDs to your Kubernetes cluster:

```
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 2: Get your currently deployed Kubernetes Operator configuration details.**

Run the following command to get the configuration details of your currently deployed Kubernetes Operator:

```sh
kubectl get deployment <operator-deployment-name> -n <namespace> -o yaml
```

**Step 3: Customize your Kubernetes Operator YAML (Yet Another Markup Language) before upgrading it.**

If needed, find the appropriate example deployment YAML (Yet Another Markup Language) file for your
chosen version of the Kubernetes Operator in the [GitHub repository](https://github.com/mongodb/mongodb-kubernetes/blob/1.4.0/public/).
Then, to avoid breaking changes, customize the example YAML (Yet Another Markup Language) file to match the configuration details
of your currently deployed Kubernetes Operator.

**Step 4: Upgrade to the new version of the Kubernetes Operator.**

Deploy your customized Kubernetes Operator by running the following:

```sh
kubectl apply -f <customized-operator-yaml-file>.yaml
```

If you do not need to modify the provided deployment YAML (Yet Another Markup Language), you can apply it directly as follows:

### Multi-Cluster

```sh
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes-multi-cluster.yaml
```

### Single-Cluster

```sh
kubectl apply -f  https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes.yaml
```

**helm:**

Use the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts).

**Step 1: Update to the latest version of the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts).**

Run the following command to check the version of your current Helm template:

```sh
helm search repo mongodb/mongodb-kubernetes
```

If your currently installed version is not the latest release, run the following 
commmand to update your Helm repo:

```sh
helm repo update mongodb
```

If you don't have the Helm repo installed locally, you can install it by running:

```sh
helm repo add mongodb https://mongodb.github.io/helm-charts
```

**Step 2: Customize your Helm Chart before upgrading it.**

To avoid breaking changes, you should ensure that you select the same settings
as those in your existing deployment. To learn about optional Kubernetes Operator 
installation settings, see Operator Helm Installation Settings.

**Step 3: Apply the CRDs to your Kubernetes cluster.**

Run the following `kubectl` command to deploy the CRDs to your Kubernetes cluster:

```
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 4: Upgrade the Kubernetes Operator.**

Run the following `helm` command to deploy the Kubernetes Operator to the 
default namespace in your Kubernetes cluster:

```sh
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes
```

You can pass the `--namespace` and `--namespace-create` flags to deploy 
the Kubernetes Operator to a non-default namespace, like so:

```
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
--namespace mongodb \
--create-namespace
```

## Upgrade the MongoDB Controllers for Kubernetes Operator Running in OpenShift

The following steps depend on how your environment is configured:

**ocup:**

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

**Step 1: Customize the Kubernetes Operator YAML (Yet Another Markup Language) before upgrading it.**

To avoid breaking changes, you should ensure that you select the same settings
as those in your existing deployment. To learn about optional Kubernetes Operator 
installation settings, see Operator Helm Installation Settings.

You must add your `<openshift-pull-secret>` to the 
`ServiceAccount` definitions:

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

**Step 2: Upgrade the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) for MongoDB deployments.**

Run the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command:

Run the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command to deploy your chosen version of the CRDs to your Kubernetes cluster:

```
oc apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 3: Upgrade to the new version of the Kubernetes Operator.**

Run the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command to deploy your chosen version of the Kubernetes Operator to your Kubernetes cluster:

```sh
oc apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes-openshift.yaml
```

**helm:**

**Step 1: Update to the latest version of the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts).**

Run the following command to check the version of your current Helm template:

```sh
helm search repo mongodb/mongodb-kubernetes
```

If your currently installed version is not the latest release, run the following 
commmand to update your Helm repo:

```sh
helm repo update mongodb
```

If you don't have the Helm repo installed locally, you can install it by running:

```sh
helm repo add mongodb https://mongodb.github.io/helm-charts
```

**Step 2: Customize your Helm Chart before upgrading it.**

To avoid breaking changes, you should ensure that you select the same settings
as those in your existing deployment. To learn about optional Kubernetes Operator 
installation settings, see Operator Helm Installation Settings.

**Step 3: Apply the CRDs to your Kubernetes cluster.**

Run the following `kubectl` command to deploy the CRDs to your Kubernetes cluster:

```
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/crds.yaml
```

**Step 4: Upgrade the Kubernetes Operator.**

Run the following `helm` command to deploy the Kubernetes Operator to the 
default namespace in your Kubernetes cluster:

```sh
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes
```

You can pass the `--namespace` and `--namespace-create` flags to deploy 
the Kubernetes Operator to a non-default namespace, like so:

```
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
--namespace mongodb \
--create-namespace
```

To troubleshoot your Kubernetes Operator, see review-k8s-op-logs
and other troubleshooting topics.

**Important:**

If you need to remove the Kubernetes Operator or the
namespace, you first must
remove MongoDB resources.

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

After upgrading the MongoDB Controllers for Kubernetes Operator, you can:

- Create an instance of Ops Manager

- Configure the Kubernetes Operator to deploy MongoDB resources
