<!-- Converted from tutorial/migrate-to-mck.txt (reStructuredText). Includes are inlined. -->

# Migrate to MongoDB Controllers for Kubernetes Operator

Follow the steps for your deployment type to begin managing your MongoDB Enterprise and `Ops Manager` deployments
with MongoDB Controllers for Kubernetes Operator instead of the MongoDB Enterprise Kubernetes Operator.

## Migrate from MongoDB Enterprise Operator to MongoDB Controllers for Kubernetes Operator for Most Deployments

Follow these steps to migrate in most deployment scenarios. If you are using
Operator Lifecycle Manager (OLM) to manage your operator deployments 
(typically on OpenShift clusters), see these steps instead.

**Step 1: Upgrade to v1.33 of the MongoDB Enterprise Kubernetes Operator.**

Upgrade your MongoDB Enterprise Kubernetes Operator deployment 
to v1.33 before you migrate. The upgrade process requires that 
you upgrade incrementally through each minor version. For 
example, if you are upgrading from version 1.31.x, you must 
first upgrade to 1.32.x before proceeding to 1.33.x.

**Step 2: Scale down the MongoDB Enterprise Kubernetes Operator to 0 replicas.**

This prevents both MongoDB Enterprise Kubernetes Operator and MongoDB Controllers for Kubernetes Operator from running in parallel.

**Step 3: Perform the following two tasks if you have deployed resources across multiple Kubernetes clusters:**

a. Back up the `kubectl` plug-in binary. This makes it easier 
   for you to reverse the migration to MongoDB Controllers for Kubernetes Operator if you encounter problems.

b. Configure the member clusters by either following the multi-cluster setup documentation
   (ensuring that you use the `kubectl` plugin from the MongoDB Controllers for Kubernetes Operator release) or 
   manually using Helm templating.

   **Important:**

   MongoDB Controllers for Kubernetes Operator\'s RBACs must be deployed to the member clusters before
   deploying MongoDB Controllers for Kubernetes Operator in step 5. The new RBAC resources begin with `mongodb-kubernetes-operator-`.
   You must also ensure that the `mongodb-kubernetes-operator-member-list` is present on your 
   central cluster after running the newest version of the `kubectl` plug-in binary.

**Step 4: Install the MongoDB Controllers for Kubernetes Operator CRDs manually.**

```sh
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.0.1/public/crds.yaml
```

After you migrate your deployment to 1.0.1, we recommend that 
you upgrade MongoDB Controllers for Kubernetes Operator directly to the latest available version, skipping any 
intermediate versions. You can use the regular upgrade procedure 
for this and all future upgrades.

To verify that the CRDs are installed on your Kubernetes cluster, search for the `mongodbcommunity` CRD:

**Tip:**

The custom resource names for Ops Manager and MongoDB Enterprise have not changed in 
MongoDB Controllers for Kubernetes Operator. Though you might not have MongoDB Community resources deployed,
searching for `mongodbcommunity` custom resources is the simplest way
to verify installation of the MongoDB Controllers for Kubernetes Operator.

```sh
kubectl get crds | grep mongodbcommunity
```

**Step 5: Install the new MongoDB Controllers for Kubernetes Operator.**

Choose one of the following installation methods:

**helm-migration:**

**Warning:**

If you have overridden the default Helm chart values for your Enterprise Kubernetes Operator deployment,
you should not use the same values for your MongoDB Controllers for Kubernetes Operator deployment as resource names could
collide and prevent the migration from succeeding.

```sh
helm repo add mongodb https://mongodb.github.io/helm-charts && \
helm repo update && \
helm upgrade --install mongodb-kubernetes-operator mongodb/mongodb-kubernetes --namespace <your-namespace>
```

**kubectl-migration:**

**Warning:**

If you customized the YAML configuration for your Enterprise Kubernetes Operator deployment,
ensure that your customizations are compatible with the MongoDB Controllers for Kubernetes Operator deployment to avoid
resource naming conflicts that could prevent the migration from succeeding.

Run the following `kubectl` command to deploy your chosen version of the Kubernetes Operator to your Kubernetes cluster:

```sh
kubectl apply -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/mongodb-kubernetes.yaml
```

**Step 6: The MongoDB Controllers for Kubernetes Operator reconciler runs and processes the existing custom resources.**

MongoDB Controllers for Kubernetes Operator applies updated images, `ServiceAccounts`, and other
resources.

If you have custom security configurations for init container images, update your YAML files to use the new `mongodb-kubernetes-` prefix instead of `mongodb-enterprise-`.

**Important:**

This step triggers a rolling restart of deployed Pods, as the RBAC
names have changed from the MongoDB Enterprise Kubernetes Operator to the
MongoDB Controllers for Kubernetes Operator.

**Step 7: Wait for the resources to reconcile (reach the `Running` phase) and become healthy.**

By default, MongoDB Controllers for Kubernetes Operator doesn't reconcile multiple resources in 
parralel. To change the default behavior, see `<https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/public/mongodb-kubernetes.yaml#L409>`__ and increase the 
`MDB_MAX_CONCURRENT_RECONCILES` environment variable.

**Step 8: Remove old assets.**

You can now remove the Helm chart for the MongoDB Enterprise Kubernetes Operator, 
as well as the RBACs on all Kubernetes clusters and any backed-up `kubectl` plug-in binaries.

If you have deployed resources across multiple Kubernetes clusters,
you can now safely remove the `mongodb-enterprise` from the member 
clusters and delete your backed-up `kubectl` plug-in binary.

## Migrate from MongoDB Enterprise Kubernetes Operator to MongoDB Controllers for Kubernetes Operator with the Operator Lifecycle Manager on OpenShift or Other Platforms

To migrate from the MongoDB Enterprise Kubernetes Operator to the MongoDB Controllers for Kubernetes Operator using OLM (Operator Lifecycle Manager)
(the typical deployment method on OpenShift clusters, but also possible on other Kubernetes platforms),
uninstall the old operator and then install the new one:

**Important:**

Removing the Enterprise Kubernetes Operator doesn't affect the database
and `Ops Manager` resources that you deploy to Kubernetes. The migration process
doesn't affect your workloads.

**Step 1: Upgrade to v1.33 of the MongoDB Enterprise Kubernetes Operator.**

Upgrade your MongoDB Enterprise Kubernetes Operator deployment 
to v1.33 before you migrate. The upgrade process requires that 
you upgrade incrementally through each minor version. For 
example, if you are upgrading from version 1.31.x, you must 
first upgrade to 1.32.x before proceeding to 1.33.x.

**Step 2: Scale down the MongoDB Enterprise Kubernetes Operator to 0 replicas.**

This prevents both MongoDB Enterprise Kubernetes Operator and MongoDB Controllers for Kubernetes Operator from running in parallel.

**Step 3: Delete the existing MongoDB Enterprise Kubernetes Operator Subscription.**

Replace `<subscription-namespace>` and `<subscription-name>` with the values that 
correspond to your resource.

```sh
kubectl -n <subscription-namespace> delete subscription <subscription-name>
```

**Step 4: Delete the `ClusterServiceVersion` (CSV) of the old MongoDB Enterprise Kubernetes Operator.**

You can usually find the CSV name by listing the CSVs in the operator's namespace. 
Replace `<operator-namespace>` and `<csv-name>` with the appropriate values.

```sh
kubectl -n <operator-namespace> delete csv <csv-name>
```

**Step 5: Install MongoDB Controllers for Kubernetes Operator from a catalog available on your cluster.**

MongoDB Controllers for Kubernetes Operator is available in Red Hat's certified operators catalog,
as well as the [operatorhub.io](https://operatorhub.io/) catalog.

```sh
kubectl create -f <path-to-bundle>
```

## Migrating from the Community Kubernetes Operator to the MongoDB Controllers for Kubernetes Operator

See the following resources to learn how to migrate to MongoDB Controllers for Kubernetes Operator:

- [Learn about the mongodbcommunity custom resource](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/docs/mongodbcommunity)
- [Migrate existing mongodbcommunity deployments to the new operator](https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/docs/migration/community-operator-migration.md)
