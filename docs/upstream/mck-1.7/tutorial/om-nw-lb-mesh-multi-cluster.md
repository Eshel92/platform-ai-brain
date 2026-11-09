<!-- Converted from tutorial/om-nw-lb-mesh-multi-cluster.txt (reStructuredText). Includes are inlined. -->

# Networking, Load Balancing, Service Mesh

Consider the following additional requirements when deploying the Ops Manager Application
in multiple Kubernetes clusters:

- om-networking-overview
- om-service-mesh
- om-networking-and-load-balancing
- diagram-om-mc-ext-lb
- diagram-om-mc-mesh-lb-proxy

## Networking Overview

The following table describes:

- Origins of connections to the Ops Manager Application instances
- The tasks that the Ops Manager Application performs after it connects
- The URL to Ops Manager that each type of connection uses and how to configure it.

| Connection's origin | Purpose or action | URL to Ops Manager |
|---|---|---|
| The Kubernetes Operator | Configures the Ops Manager instance and enables monitoring after the Application Database is in the running state | Through a default Ops Manager FQDN (fully qualified domain name) in the form: `<om_resource_name>-svc.<namespace>.svc.cluster.local` or the value of `spec.opsManagerURL` |
| The Kubernetes Operator | Configures a specific `MongoDB` resource or `MongoDBMultiCluster` resource deployment | Through the project's ConfigMap, configured when you create a project |
| MongoDB Agent in the Application Database Pods | Receives the Automation configuration | Without having to connect to an Ops Manager instance. The MongoDB Agent is running in a headless mode. |
| Monitoring Agent in the Application Database Pods | Sends monitoring data | Through a default Ops Manager FQDN (fully qualified domain name) in the form: `<om_resource_name>-svc.<namespace>.svc.cluster.local` or the value of `spec.opsManagerURL` |
| MongoDB Agent in the `MongoDB` or `MongoDBMultiCluster` resources Pods | Receives the Automation configuration, backup and restore processes | Through the project's ConfigMap, configured when you create a project |
| Monitoring Agent in the `MongoDB` or `MongoDBMultiCluster` resources Pods | Sends monitoring data | Through the project's ConfigMap, configured when you create a project |
| User | Uses the Ops Manager UI or API | Through a public, external domain of the externally exposed Ops Manager instance, configured with `spec.externalConnectivity` |

## Service Mesh

Add the nodes hosting the Application Database instances  and the Ops Manager Application
instances to the same service mesh to allow for:

- Network connectivity between deployed components.
- Cross-cluster DNS resolution.

To simplify the networking configuration between the Kubernetes Operator and
Ops Manager instances, add the central cluster, which is the Kubernetes cluster where you
install the Kubernetes Operator, to the same service mesh. This isn't a
strict requirement. If you include the central cluster into the same
service mesh, you can use it as a host for the
Ops Manager Application and the Application Database instances.

Configure a service mesh for the following Kubernetes clusters and include them into the mesh configuration:

- The central cluster on which you
  deploy the Kubernetes Operator itself.
- The "member Kubernetes clusters" that will host the Ops Manager Application instances.
- Additional member Kubernetes clusters, or the same member clusters used for Ops Manager,
  that will host the Application Database instances.

Having the same service mesh configured for all Kubernetes clusters ensures that each
Ops Manager instance can establish a secure connection to any of the
Application Database instances deployed in multiple Kubernetes clusters.

After you deploy the Application Database instances on member Kubernetes clusters,
the API endpoint for each Ops Manager instance that you deploy on member Kubernetes
clusters must be able to directly connect to each of the Application Database
instances. This allows the Kubernetes Operator to complete the stages needed
to deploy Ops Manager instances on member clusters, such as creating admin
users, and configuring backups.

## Load Balancing

In most cases, you must provide an external access to the Ops Manager Application
to enable user access to the Ops Manager UI.

For multi-cluster deployments of the Ops Manager Application, each cluster can
expose its Pods hosting the Ops Manager Application individually using a [service](https://kubernetes.io/docs/concepts/services-networking/service/)
of type `LoadBalancer` .

Create a `LoadBalancer` service using `spec.externalConnectivity`
and point an external domain to that service's external IP address.
Even if you configure more than one instance of the Ops Manager Application, the
Kubernetes service sends traffic in a round-robin fashion to all available Pods
hosting the Ops Manager Application.

Since the Kubernetes Operator doesn't support load balancing of the traffic to
all Pods across all Kubernetes clusters, you must configure load balancing
outside of the Kubernetes Operator configuration.

The following examples and diagrams illustrate a few of the many ways in which
you can configure load balancing across multiple Kubernetes clusters.

- diagram-om-mc-ext-lb
- diagram-om-mc-mesh-lb-proxy

### Diagram Example 1: External Load Balancer

Configure an external network load balancer (a passthrough proxy) for all
Kubernetes clusters hosting the Ops Manager Application and the Application Database.
The Ops Manager Application is stateless. The load balancer can forward traffic to
each cluster's `LoadBalancer` service in a round-robin fashion, or to
one cluster at a time, if you configure the load balancer in a way where
while one cluster is active, the other cluster is passive. The following
diagram illustrates this approach.

(Figure: /images/om-multicluster-external-lb.svg)
      deployment on multiple Kubernetes clusters where the traffic
      is distributed by an external load balancer.
:figwidth: 600px

In this diagram:

1. The Kubernetes Operator creates an external service of type `LoadBalancer`,
   named `<om_resource_name>-svc-ext`, with an assigned external IP address,
   on each member cluster. You can configure this service globally for all
   member clusters using `spec.externalConnectivity`. Or, if
   this service is specific to each member cluster, you can configure it
   using `spec.clusterSpecList.externalConnectivity`.

   Each service that the Kubernetes Operator creates for the Ops Manager Application always
   contains all Pods hosting the Ops Manager Application from the current cluster.

### Diagram Example 2: Load Balancing by a Service Mesh, with a Proxy

Use cross-cluster load balancing capabilities provided by a service mesh.

In each Kubernetes cluster, the Kubernetes Operator creates a [service](https://kubernetes.io/docs/concepts/services-networking/service/), named
`<om_resource_name>-svc`, which you can use to distribute traffic across
all available Pods hosting the Ops Manager Application instances in all member clusters.

You can deploy a proxy component, such as Nginx or HAProxy, in one of the
clusters, expose it externally over the Internet through your public FQDN (fully qualified domain name),
and configure the proxy to forward all network traffic through the TCP
passthrough to the service named `<om_resource_name>-svc.<namespace>.svc.cluster.local`.

The following diagram illustrates this approach.

(Figure: /images/om-multicluster-lb-from-mesh-with-proxy.svg)
      deployment on multiple Kubernetes clusters where the traffic
      is distributed by a load balancer within a service mesh, and a
      proxy service is used.
:figwidth: 600px

In this diagram:

1. On each member cluster the Kubernetes Operator creates a [service](https://kubernetes.io/docs/concepts/services-networking/service/) of
   type `ClusterIP` that you can access using
   `<om_resource_name>-svc.<namespace>.svc.cluster.local`.
   It's a service that contains in its endpoints all Pods deployed in this
   member cluster.
2. The traffic between Kubernetes clusters is handled by the service mesh.
   When the Kubernetes Operator creates services on each member cluster for the
   Ops Manager Application, the Kubernetes Operator doesn't assign a cluster index suffix
   to the names of these services. Therefore, the service mesh can perform
   traffic load balancing  to all Pods hosting the Ops Manager Application in all
   clusters.
3. In each member cluster, the Kubernetes Operator deploys a StatefulSet named
   `<om_resource_name>-<cluster-index>`. For example, `om-0` is the
   name of the StatefulSet for the member cluster with the index 0.
4. Even though each cluster has an `<om_resource_name>-svc` `ClusterIP`
   service deployed, this service doesn't handle the user traffic. When
   the user accesses the service in `Member Cluster 1`, the service mesh
   handles the traffic.
5. Each Pod hosting the Ops Manager Application is named after its StatefulSet name.
   For example, `om-1-2` is the name of the Pod number 2 in the cluster with
   the index 1.
