<!-- Converted from multi-cluster.txt (reStructuredText). Includes are inlined. -->

# Deploy MongoDB Resources on Multiple Kubernetes Clusters

**Important:**

You can deploy MongoDB Controllers for Kubernetes Operator to manage MongoDB deployments that span two
or more Kubernetes clusters. The Kubernetes Operator supports deploying both
replica sets and sharded clusters across two or more Kubernetes clusters. 

multi-cluster-overview-ref
  Learn about multi-Kubernetes cluster MongoDB deployments.

multi-cluster-arch-ref
  Learn about the multi-Kubernetes cluster MongoDB deployment architecture, capabilities, and
  limitations, and view the deployment's diagram.

multi-cluster-services-tools-ref
  Review the list of services and tools used in this quick start.

multi-cluster-prereqs
  Set up [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters, install tools, set the deployment's scope,
  install the `kubectl mongodb` plugin and check connectivity across
  member clusters.

multi-cluster-quick-start-ref
  Deploy a MongoDB replica set across three Kubernetes member clusters, using
  [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) and a service mesh.

multi-cluster-deploy-replica-set
  Deploy a `MongoDBMultiCluster` resource as a replica set with a service mesh.

multi-cluster-no-service-mesh-deploy-rs
  Deploy a `MongoDBMultiCluster` resource as a replica set without a service mesh.

multi-cluster-sharded-cluster
  Deploy a `MongoDBMultiCluster` resource as Sharded Clusters.

multi-cluster-edit-replica-set
  Modify the configuration of a `MongoDBMultiCluster` resource.

multi-cluster-secure-ref
  Secure client connections in multi-Kubernetes cluster MongoDB deployments.

multi-cluster-connect-ref
  Connect to a `MongoDBMultiCluster` resource.

disaster-recovery-ref
  Set a disaster recovery mode for your multi-Kubernetes cluster MongoDB deployment.

multi-cluster-troubleshooting
  Troubleshoot your multi-Kubernetes cluster MongoDB deployments.

kubectl-plugin-ref
  Review the `kubectl mongodb` plugin options.
