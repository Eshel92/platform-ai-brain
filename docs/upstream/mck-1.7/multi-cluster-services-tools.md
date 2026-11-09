<!-- Converted from multi-cluster-services-tools.txt (reStructuredText). Includes are inlined. -->

# Services and Tools

To create a multi-Kubernetes cluster MongoDB deployment, you can:

- Use the Quick Start, to deploy a
  MongoDB replica set across three Kubernetes member clusters, using [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) and a service mesh.

- Deploy a MongoDBMultiCluster Resource
  on each of the member clusters. This allows you to set different settings
  for the replica set resource, such as overrides for statefulSet configuration.

Both methods of creating a multi-Kubernetes cluster MongoDB deployment rely on the following services,
tools, and their documentation:

- Kubernetes clusters. The procedures use [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) to provision multiple Kubernetes
  clusters. Each Kubernetes member cluster hosts a MongoDB replica set deployment
  and represents a data center that serves your application.

- MongoDB Controllers for Kubernetes Operator repository with configuration files that
  the Kubernetes Operator needs to deploy a Kubernetes cluster.

- [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) with
  charts for multi-Kubernetes cluster MongoDB deployments.

- [Istio](https://istio.io/) service mesh. The quick start procedure uses [Istio](https://istio.io/) to facilitate
  [DNS resolution](https://istio.io/latest/docs/ops/configuration/traffic-management/dns-proxy/)
  for MongoDB replica sets deployed in different Kubernetes clusters.
  You can use another service mesh solution as long as you ensure that
  cross-cluster service FQDNs are resolvable.

  In addition, we offer the install_istio_separate_network example script. This script is based on Istio documentation and provides an example installation
  that uses the [multi-primary mode on different networks](https://istio.io/latest/docs/setup/install/multicluster/multi-primary_multi-network/). We don't guarantee the script's maintenance with future Istio releases. If you choose to use the script, review the latest Istio documentation for
  [installing a multicluster](https://istio.io/latest/docs/setup/install/multicluster/),
  and, if necessary, adjust the script to match the documentation and your deployment.
  If you use another service mesh solution, create your own script for
  configuring separate networks to facilitate DNS resolution.

- MongoDB kubectl plugin that sets up
  multi-Kubernetes cluster MongoDB deployments and allows you to run automatic and manual
  disaster recovery. To learn more,
  see the kubectl-plugin-ref.
