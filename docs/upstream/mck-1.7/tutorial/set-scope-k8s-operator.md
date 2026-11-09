<!-- Converted from tutorial/set-scope-k8s-operator.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Set Scope for MongoDB Controllers for Kubernetes Operator Deployment

Before you install the Kubernetes Operator, you can set the scope of the
Kubernetes Operator deployment. The scopes depend on the namespaces in
which you choose to deploy Ops Manager and `MongoDB` resources.

## Kubernetes Operator Deployment Scopes

You can set one of these scopes:

- ns-scope-same-ns *(Default)*
- ns-scope-different-ns
- cluster-wide-scope

### Operator Uses the Same Single Namespace as Resources

You can set the scope for the Kubernetes Operator to use the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) as
resources. In this case, the Kubernetes Operator watches Ops Manager and
`MongoDB` resources in that same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

When you install the Kubernetes Operator, it
uses the default namespace.

### Operator Uses a Subset of Namespaces

You can set the scope for the Kubernetes Operator to use one or more [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
that differ from the namespace used by the Kubernetes Operator resources.
In this case, the Kubernetes Operator watches Ops Manager and `MongoDB` resources
in a subset of [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) that you specify.

To install the Kubernetes Operator instances with this
scope, use `helm` with the helm-watch-namespace parameter.

Watching a subset of namespaces is useful in deployments where a single
Kubernetes Operator instance watches a different cluster resource type.
For example, you can configure the Kubernetes Operator to watch `MongoDB` resources
in one subset of namespaces, and to watch `MongoDBMultiCluster` resources in another
subset of namespaces. To avoid race conditions during resource reconciliation,
for each custom resource type that you want the Kubernetes Operator to watch,
ensure that you set scope to a distinct subset of namespaces.

Follow the relevant installation instructions for `helm`, but specify one or more namespaces
in the helm-watch-namespace parameter for the Kubernetes Operator to
watch:

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

When installing the Kubernetes Operator to watch resources in one or more
namespaces other than the namespace in which the Kubernetes Operator is
deployed:

1. Create the following resources:

   - A [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) with access to multiple resources. For the full resource
     definition, see the
     operator roles templates
     example. This is a cluster-scoped resource.

   - Create a [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) to link [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) with ServiceAccount. This
     `clusterRoleBinding` will bind the `clusterRole` that you
     created  with the ServiceAccount that the Kubernetes Operator is using
     on the namespace where you install it.

2. Include the [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) and [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding)
   in the default configuration files that you apply during the
   installation.

3. Create local Kubernetes [ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/):

   For each namespace, create some or all of the following local Kubernetes 
   ServiceAccounts:

   - If you want to deploy a MongoDB instance in the namespace, use
     `mongodb-kubernetes-database-pods`. 

   - If you want to deploy Ops Manager in the namespace, use 
     `mongodb-kubernetes-appdb` and `mongodb-kubernetes-ops-manager`. 

The following example illustrates how the [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) and [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) work
together in the cluster.

Suppose you create a ServiceAccount in the `mongodb` namespace, and
then install the Kubernetes Operator in this namespace. The Kubernetes Operator
uses this ServiceAccount.

To set the Kubernetes Operator scope to watch namespaces `ns1` and `ns2`:

1. Obtain `cluster-admin privileges`.
2. Using these privileges, create a cluster-wide, non-namespaced [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole).
3. Create a [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) in three namespaces: `mongodb`, `ns1`
   and `ns2`. This [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) will bind the
   [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) to the ServiceAccount in the `mongodb` namespace.
   The `clusterRoleBinding` will allow the Kubernetes Operator deployed in
   the `mongodb` namespace to access the resources described in the
   `clusterRole` of the target namespace, that is, in `mongodb`,
   `ns1` and `ns2`.

See also helm-watch-namespace.

### Operator Uses Cluster-Wide Scope

You can set the scope for the Kubernetes Operator to the Kubernetes cluster.
In this case, the Kubernetes Operator watches Ops Manager and `MongoDB` resources
in all [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes cluster.

**Important:**

You can deploy only one instance of the Kubernetes Operator with a
cluster-wide scope per Kubernetes cluster.

To set a cluster-wide scope for the Kubernetes Operator, follow the
instructions for your preferred installation method.

**cwidek8s:**

**k8s-no-helm:**

1. Use the mongodb-kubernetes.yaml
   sample YAML (Yet Another Markup Language) file from the MongoDB Controllers for Kubernetes Operator GitHub repository.
#. Set the `spec.template.spec.containers.name.env.name:WATCH_NAMESPACE`
   in mongodb-kubernetes.yaml
   to `"*"`. You must include the double quotation marks
   (`"`) around the asterisk (`*`) in the YAML (Yet Another Markup Language) file.

   ```sh
   WATCH_NAMESPACE: "*"
   ```

#. In mongodb-kubernetes.yaml,
   change:

   ```sh
   kind:  Role 
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: mongodb-kubernetes-operator
   ```

   to:

   ```sh
   kind: ClusterRole
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: mongodb-kubernetes-operator
   ```

#. Add the following code to the `ClusterRole` that you
   have just modified:

   ```sh
   - apiGroups:
     - ""
     resources:
     - namespaces
     verbs:
     - list
     - watch
   ```

#. In mongodb-kubernetes.yaml,
   change:

   ```sh
   kind:  RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: mongodb-kubernetes-operator
    namespace: mongodb
   roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: Role
    name: mongodb-kubernetes-operator
   subjects:
    - kind: ServiceAccount
    name: mongodb-kubernetes-operator
    namespace: mongodb
   ```

   to:

   ```sh
   kind:  ClusterRoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: mongodb-kubernetes-operator
    namespace: mongodb
   roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: mongodb-kubernetes-operator
   subjects:
    - kind: ServiceAccount
    name: mongodb-kubernetes-operator
    namespace: mongodb
   ```

#. In the `mongodb-kubernetes.yaml` file, change the
   `<namespace>` value to the namespace where you want
   the Kubernetes Operator to deploy resources and apply the
   YAML (Yet Another Markup Language) fle.

   ```yaml
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-database-pods
     namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-ops-manager
     namespace: <namespace>
   ---
   kind: Role
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   rules:
     - apiGroups:
         - ""
       resources:
         - secrets
       verbs:
         - get
     - apiGroups:
         - ""
       resources:
         - pods
       verbs:
         - patch
   ---
   kind: RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: mongodb-kubernetes-appdb
   subjects:
     - kind: ServiceAccount
       name: mongodb-kubernetes-appdb
       namespace: <namespace>
   ...
   ```

#. Create local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   For each namespace, create some or all of the following
   local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   - If you want to deploy a MongoDB instance in the
     namespace, use `mongodb-kubernetes-database-pods`.

   - If you want to deploy Ops Manager in the namespace, use
     `mongodb-kubernetes-appdb` and `mongodb-kubernetes-ops-manager`.

   Copy and paste the applicable examples and replace the `<namespace>`
   value with the label that identifies the namespace.

   ```sh
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
    name: mongodb-kubernetes-database-pods
    namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
    name: mongodb-kubernetes-appdb
    namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
    name: mongodb-kubernetes-ops-manager
    namespace: <namespace>
   ```

**k8s-with-helm:**

Before you deploy the Kubernetes Operator, configure the following
items:

1. Configure the Kubernetes Operator to watch all namespaces:

   ```sh
   helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
     --set operator.watchNamespace="*"
   ```

#. Create local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   For each namespace, create some or all of the following
   local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   - If you want to deploy a MongoDB instance in the
     namespace, use `mongodb-kubernetes-database-pods`.

   - If you want to deploy Ops Manager in the namespace, use
     `mongodb-kubernetes-appdb` and `mongodb-kubernetes-ops-manager`.

   Copy and paste the applicable examples and replace the `<namespace>`
   value with the label that identifies the namespace.

   ```sh
   helm template mongodb/mongodb-kubernetes \
     --set operator.namespace=<metadata.namespace> \
     --show-only templates/database-roles.yaml | kubectl apply -f -
   ```

**os:**

**openshift-no-helm:**

Before you deploy the Kubernetes Operator, configure the following
items:

1. Use the mongodb-kubernetes-openshift.yaml
   sample YAML (Yet Another Markup Language) file from the MongoDB Controllers for Kubernetes Operator GitHub repository.

#. Set the `spec.template.spec.containers.name.env.name:WATCH_NAMESPACE` in
   mongodb-kubernetes-openshift.yaml
   to `"*"`. You must include the double quotation marks
   (`"`) around the asterisk (`*`) in the YAML (Yet Another Markup Language) file.

   ```sh
   WATCH_NAMESPACE: "*"
   ```

#. Create the corresponding roles for these accounts. In
   mongodb-kubernetes-openshift.yaml,
   change:

   ```sh
   kind: Role
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: enterprise-operator
   ```

   to:

   ```sh
   kind: ClusterRole
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: enterprise-operator
   ```

#. Add the following code to the `ClusterRole` that you
   have just modified:

   ```sh
   - apiGroups:
     - ""
     resources:
     - namespaces
     verbs:
     - list
     - watch
   ```

#. In mongodb-kubernetes-openshift.yaml,
   change:

   ```sh
   kind:  RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: enterprise-operator
    namespace: mongodb
   roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: Role
    name: enterprise-operator
   subjects:
    - kind: ServiceAccount
    name: enterprise-operator
    namespace: mongodb
   ```

   to:

   ```sh
   kind:  ClusterRoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
    name: enterprise-operator
    namespace: mongodb
   roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: enterprise-operator
   subjects:
    - kind: ServiceAccount
    name: enterprise-operator
    namespace: mongodb
   ```

#. Create the secret only in the namespace where you will
   deploy the Kubernetes Operator.
   If you deploy MongoDB resources in multiple namespaces or with a cluster-wide
   scope, the Kubernetes Operator
   synchronizes the secret across all watched namespaces.
   To learn more, see the `registry.imagePullSecrets`
   setting in the Helm installation settings.

   In the `mongodb-kubernetes.yaml` file, replace
   `<namespace>` with the namespace in which you want to
   install the Kubernetes Operator. Use [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) or the OpenShift
   Container Platform UI to apply the resulting YAML (Yet Another Markup Language) file.

   ```yaml
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-database-pods
     namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-ops-manager
     namespace: <namespace>
   ---
   kind: Role
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   rules:
     - apiGroups:
         - ""
       resources:
         - secrets
       verbs:
         - get
     - apiGroups:
         - ""
       resources:
         - pods
       verbs:
         - patch
   ---
   kind: RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: mongodb-kubernetes-appdb
   subjects:
     - kind: ServiceAccount
       name: mongodb-kubernetes-appdb
       namespace: <namespace>
   ...
   ```

#. Create local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   For each namespace, create some or all of the following
   local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   - If you want to deploy a MongoDB instance in the
     namespace, use `mongodb-kubernetes-database-pods`.

   - If you want to deploy Ops Manager in the namespace, use
     `mongodb-kubernetes-appdb` and `mongodb-kubernetes-ops-manager`.

   Copy and paste the applicable examples and replace the `<namespace>`
   value with the label that identifies the namespace.

**openshift-helm:**

Before you deploy the Kubernetes Operator, configure the following
items:

1. Configure the Kubernetes Operator to watch all namespaces:

   ```sh
   helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
     --set operator.watchNamespace="*" \
   ```

#. Create the secret only in the namespace where you will
   deploy the Kubernetes Operator.
   If you deploy MongoDB resources in multiple namespaces or with a cluster-wide
   scope, the Kubernetes Operator
   synchronizes the secret across all watched namespaces.
   To learn more, see the `registry.imagePullSecrets`
   setting in the Helm installation settings.

   In the `mongodb-kubernetes.yaml` file, replace `<namespace>`
   with the namespace in which you want to install the
   Kubernetes Operator. Use [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) or the OpenShift Container
   Platform UI to apply the resulting YAML (Yet Another Markup Language) file.

   ```yaml
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-database-pods
     namespace: <namespace>
   ---
   kind: ServiceAccount
   apiVersion: v1
   metadata:
     name: mongodb-kubernetes-ops-manager
     namespace: <namespace>
   ---
   kind: Role
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   rules:
     - apiGroups:
         - ""
       resources:
         - secrets
       verbs:
         - get
     - apiGroups:
         - ""
       resources:
         - pods
       verbs:
         - patch
   ---
   kind: RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: mongodb-kubernetes-appdb
     namespace: <namespace>
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: mongodb-kubernetes-appdb
   subjects:
     - kind: ServiceAccount
       name: mongodb-kubernetes-appdb
       namespace: <namespace>
   ...
   ```

#. Create local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   For each namespace, create some or all of the following
   local Kubernetes [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/):

   - If you want to deploy a MongoDB instance in the
     namespace, use `mongodb-kubernetes-database-pods`.

   - If you want to deploy Ops Manager in the namespace, use
     `mongodb-kubernetes-appdb` and `mongodb-kubernetes-ops-manager`.

   Copy and paste the applicable examples and replace the `<namespace>`
   value with the label that identifies the namespace.

   ```sh
   helm template mongodb/mongodb-kubernetes \
     --set operator.namespace=<metadata.namespace> \
     --show-only templates/database-roles.yaml | oc apply -f -
   ```

## Next Steps

After setting up the scope for the MongoDB Controllers for Kubernetes Operator, you can:

- Read the Considerations.
- Complete the Prerequisites.
- Install the Kubernetes Operator.
