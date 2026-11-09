<!-- Converted from multi-cluster-overview.txt (reStructuredText). Includes are inlined. -->

# Overview

Multi-Kubernetes cluster MongoDB deployments enable different levels of resilience, depending on the
needs of your enterprise application:

- **Single Region, Multi AZ**. One or more Kubernetes clusters where you deploy
  each cluster's nodes in different zones in the same region. Such deployments
  protect MongoDB instances backing your enterprise applications against
  zone and Kubernetes cluster failures and offer increased availability,
  disaster recovery, and data distribution within one cloud region.

- **Multi Region**. One or more Kubernetes clusters where you deploy each cluster
  in a different region, and within each region, deploy cluster nodes in
  different availability zones. This gives your database resilience against
  the loss of a Kubernetes cluster, a zone, or an entire cloud region.

Multi-Kubernetes cluster MongoDB deployments allow you to add MongoDB instances in global clusters
that span multiple geographic regions for increased availability and
global distribution of data.

## Central and Member Clusters

Identify one Kubernetes cluster that should act as a **central cluster**
in your multi-Kubernetes cluster MongoDB deployment.

A multi-Kubernetes cluster MongoDB deployment that uses the MongoDB Controllers for Kubernetes Operator consists of one
**central cluster** and one or more **member clusters** in Kubernetes:

- The **central cluster** has the following role:

  - Hosts the MongoDB Controllers for Kubernetes Operator
  - Acts as the control plane for the multi-Kubernetes cluster MongoDB deployment
  - Hosts the `MongoDBMultiCluster` resource spec for the MongoDB replica set
  - Hosts Ops Manager, if you deploy Ops Manager with the Kubernetes Operator
  - Can also host members of the MongoDB replica set

  **Note:**

  The central cluster is also known as the operator cluster.

- **Member clusters** host the MongoDB replica sets.

The following diagram shows the high-level architecture of a multi-Kubernetes cluster MongoDB deployment
across regions and availability zones.
To learn more, see multi-cluster-arch-ref.

(Figure: /images/multi-cluster-arch-with-service-mesh.svg)
      deployment across regions and availability zones using the
      MongoDB Controllers for Kubernetes Operator, with a service mesh
:figwidth: 600px

**Note:**

This deployment uses a service mesh. This simplifies configuring multi-Kubernetes cluster MongoDB deployments.
A service mesh enables inter-cluster communication between the replica set
members deployed in different Kubernetes clusters. MongoDB development has
tested these deployments with [Istio](https://istio.io/), but any service mesh that provides FQDN (fully qualified domain name)
hostname resolution between Pods across clusters should work. To learn more,
see Plan for External Connectivity.

## Migrating to Multi-Kubernetes-Cluster Deployments

You can create a new multi-Kubernetes cluster MongoDB deployment and contact [MongoDB Support](https://support.mongodb.com/welcome) to help you
migrate data from your existing Kubernetes deployment to a multi-Kubernetes cluster MongoDB deployment.
You can't extend an existing single-Kubernetes cluster deployment to
new Kubernetes clusters.
