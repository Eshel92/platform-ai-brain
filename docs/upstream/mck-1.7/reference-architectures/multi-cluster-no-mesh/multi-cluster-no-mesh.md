<!-- Converted from reference-architectures/multi-cluster-no-mesh/multi-cluster-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Reference Architecture Without a Service Mesh

The multi-cluster reference architecture includes multiple deployment strategies, 
each with the common foundation of MongoDB custom resources being deployed across 
multiple Kubernetes clusters without a service mesh.

Standard multi-cluster deployments consist of one or more elements from each of 
the following categories, including but not limited to Kubernetes clusters and a 
means of securely networking between them. 

You can access all of the code examples included in the following guides from 
the `architectures` directory of the Kubernetes Operator [official GitHub repository](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0), 
or you can simply copy and paste the same examples directly from the guides 
included in this reference architecture.

Follow the procedures within the following categories to deploy a tested, 
working multiple-Kubernetes cluster implementation of the MongoDB Controllers for Kubernetes Operator. 

**Note:**

The examples included in this reference architecture are opinionated and 
include specific, third-party tools and platforms for illustration's sake. 
You can substitute any equivalent tool or platform. MongoDB does not support 
third-party tooling.

## Kubernetes Infrastruture

To deploy any variety of Multi-Cluster MongoDB implementation, you must have 
multiple Kubernetes clusters. You can deploy your Kubernetes clusters in any way you like. 
To deploy them on [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine), you can follow the steps in this guide:

- Deploy multiple Kubernetes clusters on GKE.

## Cluster-to-Cluster Networking

All implementations of multiple Kubernetes cluster Kubernetes Operator deployments require 
each cluster to expose FQDN (fully qualified domain name). To achieve this without deploying a service mesh 
you can follow the guides within this section of the reference architectures.

- Configure External DNS.

## MongoDB Kubernetes Operator

The MongoDB Controllers for Kubernetes Operator handles the deployment of MongoDB custom resources, 
such as the Ops Manager and MongoDB database intances in Kubernetes.
For general information about the Kubernetes Operator for multi-cluster deployments, 
see Multi-Cluster Replics Sets. 
To deploy the Kubernetes Operator to your Kubernetes cluster, see:

- Deploy the Operator.

## Ops Manager

MongoDB Controllers for Kubernetes Operator deployments require either a Cloud Manager or an Ops Manager instance. 
These required resources facilitate workloads such as backing up data and 
monitoring database performance. To deploy Ops Manager across multiple Kubernetes 
clusters, see:

- Deploy multi-cluster Ops Manager.

## MongoDB Deployments

MongoDB Controllers for Kubernetes Operator facilitates the deployment of MongoDB and related resources in one or 
more Kubernetes clusters. To learn more, see Multi Cluster Replicasets
and see Multi-Cluster Sharded Clusters.
