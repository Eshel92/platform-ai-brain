<!-- Converted from tutorial/om-arch-reconciliation.txt (reStructuredText). Includes are inlined. -->

# Reconciling the `MongoDBOpsManager` Custom Resource

The following diagram describes how the Kubernetes Operator reconciles changes
to the `MongoDBOpsManager` [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) on each member Kubernetes cluster.

(Figure: /images/meko-reconciliation.svg)
      Operator reconciles changes to the MongoDBOpsManager 
      Custom Resource Definition on each member Kubernetes cluster.
:figwidth: 600px

1. The Kubernetes Operator creates or updates the
   `<om_resource_name>-db-config` secret. This secret contains
   the configurations that the MongoDB Agent uses to start the
   Application Database replica set.

2. The Kubernetes Operator creates or updates the `<om_resource_name>-db`
   Application Database StatefulSet. This StatefulSet contains at
   least three [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/).

   - Each Pod runs one MongoDB Agent instance. Each MongoDB Agent starts a
     `mongod` instance on its Pod.
   - The Kubernetes Operator mounts the `<om_resource_name>-db-config`
     secret to each Pod. The MongoDB Agent uses this secret to
     configure the Application Database replica set.

     In multi-cluster deployments, the Kubernetes Operator assigns the member
     cluster's index suffix to each Application Database\'s StatefulSet, in
     the form of `<om_resource_name>-db-<cluster-idx>`, for example: `om-db-1`.

3. The Kubernetes Operator creates or updates the `<om_resource_name>`
   StatefulSet. In multi-cluster deployments, the Kubernetes Operator assigns
   the member cluster's index suffix to each StatefulSet, in the form of
   `<om_resource_name>-<cluster-idx>`, for example: `om-1`.

   The StatefulSet contains one Pod for each Ops Manager replica. Each Ops Manager
   replica connects to the Application Database.

   Most changes to the `MongoDBOpsManager` [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
   trigger a rolling upgrade of the Pods in the `<om_resource_name>`
   StatefulSet. Enabling TLS for the Application Database
   also triggers a rolling restart because the connection string to the
   Application Database changes. Changes to `spec.backup`
   don't trigger a rolling upgrade.

4. The Kubernetes Operator invokes Ops Manager APIs to create an admin user.
   The Kubernetes Operator saves this admin user's credentials in the
   `<om_resource_name>-admin-key` secret. The Kubernetes Operator uses
   these credentials for all other Ops Manager API invocations.
   This reconciliation step happens only once when you use the Kubernetes Operator
   to deploy a new Ops Manager resource. The Kubernetes Operator skips this step
   when it updates the resource.

5. The Kubernetes Operator performs a rolling upgrade of the Pods in the `<om_resource_name>-db`
   Application Database StatefulSet to enable Ops Manager to monitor it.
   Monitoring is enabled by default. This reconciliation step happens
   only once, such as when you deploy a new Ops Manager resource.

6. If `spec.backup.enabled` is **true**, the Kubernetes Operator
   creates the `<om_resource_name>-backup-daemon` StatefulSet or
   verifies that it is running. The Backup Daemon connects to the same
   Application Database as the Ops Manager deployment.

   In multi-cluster deployments, the Kubernetes Operator assigns the member
   cluster's index suffix to each Backup Daemon's StatefulSet, in
   the form of `<om_resource_name>-backup-daemon-<cluster-idx>`, for
   example: `om-backup-daemon-1`.

7. If `spec.backup.enabled` is **true**, the Kubernetes Operator
   invokes Ops Manager APIs to ensure that the Ops Manager Application\'s backup
   configuration matches the one that you define in the custom resource
   definition.
