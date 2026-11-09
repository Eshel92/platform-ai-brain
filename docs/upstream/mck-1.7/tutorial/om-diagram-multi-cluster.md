<!-- Converted from tutorial/om-diagram-multi-cluster.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Architecture Diagram: Ops Manager and the Application Database

The following diagram shows the Ops Manager Application, the Application Database,
the Backup Daemon, and the corresponding [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) deployed on multiple
Kubernetes clusters.

(Figure: /images/om-multicluster-arch.svg)
      its UI application, the Application Database, and the Backup Daemon
      on multiple Kubernetes clusters. The diagram also shows network
      connections between the components.
:figwidth: 100%

In this diagram:

1. The `Member Cluster 0` is also the central cluster because you install
   the Kubernetes Operator on it. It is also a member cluster and can host
   any multi-cluster custom resource.

2. The `Member Cluster 0` stores the [kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/), which describe the
   [Kubernetes configuration](https://kubernetes.io/docs/concepts/configuration/) for member clusters, users, and contexts. When you
   configure the Kubernetes Operator for multi-cluster deployments using the
   `kubectl mongodb` plugin, it creates the following resource:

   - The `mongodb-enterprise-operator-multi-cluster-kubeconfig` secret,
     which contains the credentials to all Kubernetes clusters that the Kubernetes Operator
     is going to manage. If you plan to use the central cluster as a member
     cluster, this secret might contain the credentials to the same cluster
     where you install the Kubernetes Operator.

   When the Kubernetes Operator runs in the multi-cluster mode,
   it stores the resources it needs, such as ConfigMaps and secrets about
   the clusters that it is going to manage. These resources belong to the
   same namespace as the Kubernetes Operator. The Kubernetes Operator uses these
   resources to deploy the Ops Manager Application and the Application Database on
   multiple Kubernetes clusters.

3. The Kubernetes Operator also creates and maintains some additional multi-cluster
   deployment state ConfigMaps for each Ops Manager Application and Application Database
   deployment it manages. The `Member Cluster 0` stores this configuration,
   which includes the following ConfigMaps:

   - The `<om_resource_name>-cluster-mapping` ConfigMap contains the
     mapping of member cluster names listed in the `spec.clusterSpecList`
     to cluster indexes, referenced in this documentation as `cluster_index`, such
     as `Cluster 0`, or `Cluster 1`. The Kubernetes Operator assigns these indexes to
     each cluster name.
   - The `<om_resource_name>-db-cluster-mapping` ConfigMap contains the
     mapping of member cluster names listed in the `spec.applicationDatabase.clusterSpecList`
     to cluster indexes.
   - The `<om_resource_name>-db-member-spec` ConfigMap contains the number
     of Application Database replicas configured for each member cluster.
     Having this information allows the Kubernetes Operator to correctly scale
     or reconfigure the replica set as part of disaster recovery, such as
     after losing the entire member cluster.

4. The `MongoDBOpsManager` resource's configuration is a file that you
   create that describes a multi-cluster Ops Manager deployment.
   The Kubernetes Operator uses this file to deploy the Ops Manager components.
   
   The following example shows the configuration that leads to the Kubernetes Operator
   deploying the Ops Manager components described in this diagram. This example
   omits some settings that aren't relevant for this diagram, such as TLS (Transport Layer Security) configuration.

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
     name: om
     namespace: om-ns
   spec:
     replicas: 1 # You can set this value and use it as a global or default
                 # setting for all clusters. The spec.clusterSpecList.members
                 # setting overrides this setting.
     topology: MultiCluster
     version: 8.0.0
     adminCredentials: om-admin-secret
     clusterSpecList:
       - clusterName: "Member Cluster 1" # Ops Manager settings for "Member Cluster 1"
         members: 2
         backup: # Backup settings for "Member Cluster 1"
           members: 2 # Overrides spec.backup.members
       - clusterName: "Member Cluster 2" # Ops Manager settings for "Member Cluster 2"
         members: 1
         backup: # Backup settings for "Member Cluster 2"
           members: 2 # Overrides spec.backup.members
     applicationDatabase: # Global Application Database settings
       topology: MultiCluster
       version: 8.0.0
       members: 3 # In multi-cluster mode, the Operator ignores this field.
                  # The Operator sets the number of members for the Application
                  # Database in spec.applicationDatabase.clusterSpecList.members.
       clusterSpecList:
         - clusterName: "Member Cluster 1"
           members: 3
         - clusterName: "Member Cluster 2"
           members: 2
     backup: # Global settings for the Backup Daemon
       enabled: true
       members: 1 # Set this value and use it as a global or default setting.
                  # To override this value, set the value for
                  # spec.clusterSpecList.backup.members.
                  # The Backup Daemon's configuration for each cluster isn't
                  # stored here. Use the Ops Manager's spec.clusterSpecList.backup to
                  # specify the Backup Daemon configuration for each member cluster.
   ```

5. The Kubernetes Operator connects to the Ops Manager instances referencing either:

   - The default FQDN (fully qualified domain name) of the service it creates for the Ops Manager resource,
     `<om_resource_name>-svc.<namespace>.svc.cluster.local`, or
   - The URL that you specify in `spec.opsManagerURL`.
     In some deployments, such as when the cluster where you installed the
     Kubernetes Operator isn't attached to the service mesh, the default service
     FQDN (fully qualified domain name) might be unreachable. In this case, the Kubernetes Operator reports
     the `MongoDBOpsManager` resource status as `Failed` indicating a
     connection error. To account for such cases, provide the URL to Ops Manager
     in the `spec.opsManagerURL`. This URL might be a hostname of
     an externally exposed Ops Manager instance. To learn more, see om-networking-overview.

6. Two member clusters host the Ops Manager Application.
   In each cluster, the Kubernetes Operator deploys a StatefulSet named `<om_resource_name>-<cluster_index>`.

   - The StatefulSet deploys two instances of the Ops Manager Application in `Member Cluster 1`
     and one instance in `Member Cluster 2`.

   - You define the number of instances in `spec.clusterSpecList.members`.
     You might set the number of instances to zero so that this cluster doesn't
     deploy any Ops Manager Application instances. This is useful, if, for example,
     you would like to use this cluster for hosting only Backup Daemon instances.

     If you remove a cluster from `spec.clusterSpecList`, this is
     equivalent to specifying zero members in `spec.clusterSpecList.members`
     and `spec.clusterSpecList[*].backup.members`.

   - For each StatefulSet in each cluster, the Kubernetes Operator configures a
     [service](https://kubernetes.io/docs/concepts/services-networking/service/) of type `ClusterIP`, named `<om_resource_name>-svc`,
     that contains all Pods on the cluster's endpoints list. This service's
     FQDN, `<om_resource_name>-svc.<namespace>.svc.cluster.local`, is a
     default hostname that the Kubernetes Operator uses to access the deployed
     endpoint for the Ops Manager Application.

   - If you specify `spec.externalConnectivity`, the Kubernetes Operator
     also creates an external Kubernetes `LoadBalancer`-type service, named
     `<om_resource_name>-svc-ext`, for each cluster. In each cluster,
     you can specify its own configuration for this external service using
     `spec.clusterSpecList.externalConnectivity`. For example,
     you can change the service's type or define annotations.

7. Application Database. The Kubernetes Operator deploys the Application Database on two clusters.

   - The `Member Cluster 1` contains three `mongod` processes for the
     Application Database, and the `Member Cluster 2` contains two `mongod`
     processes..

   - You define the Application Database configuration using the
     `spec.applicationDatabase` settings. On each member cluster,
     the Kubernetes Operator creates a StatefulSet named `<om_resource_name>-db-<cluster_index>`
     with the number of member clusters defined in `spec.applicationDatabase.clusterSpecList.members`.
     In multi-cluster mode, the Kubernetes Operator ignores values that you set
     for the `spec.applicationDatabase.members` field.
     The Kubernetes Operator configures one replica set formed from `mongod`
     processes deployed across all member clusters.

   - For each Pod in `<statefulset_name>-<pod_index>` hosting a MongoDB
     process named `<om_resource_name>-db-<cluster_index>-<pod_index>`,
     the Kubernetes Operator creates a Kubernetes `ClusterIP`-type service for accessing
     the individual `mongod` processes by its FQDN (fully qualified domain name),
     `<om_resource_name>-db-<cluster_index>-<pod_index>-svc`. Each `mongod`
     process in the replica set must be uniquely addressable.

     The processes in the replica set configuration must have their process hostnames
     configured to that Pod service's FQDN (fully qualified domain name): `<om_resource_name>-db-<cluster_index>-<pod_index>-svc.<namespace>.svc.cluster.local`.

   - Each Pod has its persistent volume attached via a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) that the
     Kubernetes Operator creates.

   - To form a replica set from all `mongod` processes, each process must
     connect to each other process for replication purposes. To achieve this,
     include all member clusters on which you deploy the Application Database
     into the same service mesh configuration.

     The service mesh handles cross-cluster DNS queries and routes the traffic accordingly.
     The service mesh assists in resolving each Pod service's FQDN (fully qualified domain name)
     `<om_resource_name>-db-<cluster_index>-<pod-index>-svc.<namespace>.svc.cluster.local`
     across all clusters and allows connectivity on the exposed `mongod` port
     (27017 by default).

     For example, when a `mongod` process running in the `om-db-1-0` Pod
     in `Member Cluster 1` connects to a `mongod` running in the
     `om-db-2-1` Pod in `Member Cluster 2`, the first `mongod` process
     uses its hostname from the Automation Configuration, `om-db-2-1-svc.om-ns.svc.cluster.local:27017`,
     and the service mesh routes this request to `Member Cluster 2` to
     the `om-db-2-1-svc` service.
     Without the service mesh, the Kubernetes `Member Cluster 1` has no information
     about the `om-db-2-1-svc` service deployed in the `Member Cluster 2`
     and the DNS resolution of `om-db-2-1-svc.om-ns.svc.cluster.local`
     would fail.

   - When the Application Database and the Ops Manager Application instances are in a
     `Running` state, the Kubernetes Operator adds an additional monitoring
     container to the Application Database StatefulSets. This results in
     a rolling restart of all Application Database Pods in all clusters.
     The Kubernetes Operator updates the StatefulSets across all clusters
     sequentially, so that during the rolling restart process, in each
     cluster, only one replica set's member becomes temporarily unavailable.

   - The Monitoring Agent connects to the Ops Manager Application instances using
     the Ops Manager service's FQDN (fully qualified domain name), `<om_resource_name>-svc.<namespace>.svc.cluster.local`,
     or the value in `spec.opsManagerURL` if you specify it.

     The Ops Manager Application and the Backup Daemon always use the connection string
     to the Application Database that contains all replica set members in it.
     The connection string is always constructed using the service-per-pod
     FQDNs.

8. The Kubernetes Operator deploys the Backup Daemon StatefulSets if you set
   the `spec.backup.enabled` to `true`. 
   
   - On each member cluster listed in the `spec.clusterSpecList`, the Kubernetes Operator
     creates one Backup Daemon StatefulSet, named `<om_resource_name>-backup-daemon-<cluster_index>`
     with the number of Backup Daemon instances set to `spec.backup.members`.
   
     Alternatively, you can configure the number of Backup Daemon instances
     for each cluster in `spec.clusterSpecList[*].backup.members`.

   - The Backup Daemon instances connect only to the Application Database
     replica set using the same connection string as the Ops Manager Application
     instances.

In addition, in this diagram, you can observe the service mesh and the
networking connections between the components:

- The dotted lines surrounding the diagram show the single service mesh that
  includes the networking configuration for all clusters.
- The dotted lines surrounding the Ops Manager Application across member clusters
  indicate that these instances are stateless and the traffic can be
  equally distributed to all instances, for example by using using a
  round-robin load balancer.

- The dotted lines surrounding the Application Database across member
  clusters indicate that these instances communicate with each other and
  form a single MongoDB replica set.
