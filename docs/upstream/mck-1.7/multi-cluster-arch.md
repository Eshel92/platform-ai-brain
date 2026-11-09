<!-- Converted from multi-cluster-arch.txt (reStructuredText). Includes are inlined. -->

# Architecture, Capabilities, and Limitations

## Limitations

The following limitations exist for multi-Kubernetes cluster MongoDB deployments:

- Use Ops Manager versions later than 5.0.7.
- Use only Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) for your secret storage tool. The [HashiCorp Vault](https://www.vaultproject.io/) 
  secret storage tool isn't supported.
- For deployments where the same Kubernetes Operator instance is not managing both the
  MongoDBOpsManager and 
  MongoDB custom resources, 
  you must manually configure KMIP (Key Management Interoperability Protocol) backup encryption client settings in Ops Manager. 
  To learn more, see kmip-manual-procedure.   
- Don't add a ServiceMonitor
  to your `MongoDBMultiCluster` resources. The Kubernetes Operator doesn't support integration with Prometheus.

- .. include:: /includes/facts/fact-migrating-to-multi-clusters.rst

## Multi-Cluster Deployment Capabilities

This section describes the multi-Kubernetes cluster MongoDB deployment capabilities that you can
configure using the same procedures as the procedures for single clusters
of MongoDB resources deployed with the Kubernetes Operator. Other multi-Kubernetes cluster MongoDB deployment
capabilities have their own documentation in this guide.

- multi-cluster-connection-string
- multi-cluster-security-db-users
- multi-cluster-queryable-backups-for-om

### Connect with DNS (Domain Name System) SRV (Service) Records

To connect to the multi-Kubernetes cluster MongoDB deployment database as a user, you can use
the `connectionString.standardSrv`: DNS seed list connection string.
This string is included in the secret that the Kubernetes Operator creates for your multi-Kubernetes cluster MongoDB deployment.
Use the same procedure for connecting to the multi-Kubernetes cluster MongoDB deployment as for single
clusters deployed with Kubernetes Operator. See Connect to a MongoDB Database Resource from Inside Kubernetes
and select the tab Using the Kubernetes Secret.

### Manage Security for Database Users

Use these methods to manage security for database users:

- LDAP authentication
- SCRAM authentication
- TLS and X.509 for internal cluster authentication
- OIDC authentication

These procedures are the same as the procedures for single clusters deployed
with the Kubernetes Operator, with the following exceptions:

- The procedures apply to replica sets only. Multi-Kubernetes cluster MongoDB deployments don't support creating sharded clusters.
- In the `mongodbResourceRef`, specify the name of the multi-Kubernetes cluster MongoDB deployment
  replica set: `name: "<my-multi-cluster-replica-set>"`.

### Set up Queryable Backups for Single-Cluster Ops Manager Resources

If you deploy an Ops Manager instance on a single Kubernetes cluster with the Kubernetes Operator,
the operator-hosting cluster may also host Ops Manager. In this case, you can
configure queryable backups
for Ops Manager resources. Queryable backups aren't supported in deployments
of Ops Manager resources on multiple Kubernetes clusters.

## Deployment Architecture and Diagrams

You can create multi-Kubernetes cluster MongoDB deployments with or without relying on a service mesh.
To learn more, see mc_plan_external_connectivity

In both the following diagrams, the MongoDB Controllers for Kubernetes Operator performs these actions:

- Watches for the `MongoDBMultiCluster` resource spec creation in the
  central cluster.
- Uses the mounted `kubeconfig` file to communicate with
  member clusters.
- Creates the necessary resources, such as ConfigMaps, Secrets, Services
  and StatefulSet Kubernetes objects in each member cluster corresponding to
  the number of replica set members in the MongoDB cluster.
- Identifies the cluster for deploying each MongoDB replica set using
  the corresponding `MongoDBMultiCluster` resource spec, and deploys the MongoDB replica sets.
- Watches for the `CentralCluster` and `MemberCluster` events.
- Reconciles the resources it created to confirm that the multi-Kubernetes cluster MongoDB deployment
  is in the desired state.

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

Note that if the central cluster fails,
you can't use the Kubernetes Operator
to change your deployment until you restore access to this cluster or
until you redeploy the Kubernetes Operator to another available Kubernetes cluster.
To learn more, see disaster-recovery-ref.

### Diagram: Multi-Kubernetes Cluster Deployment with a Service Mesh

The following diagram shows the high-level architecture of a multi-Kubernetes cluster MongoDB deployment
across regions and availability zones. This deployment uses a service mesh,
such as Istio. The service mesh:

- Manages the discovery of MongoDB nodes deployed in different Kubernetes member clusters.
- Handles communication between replica set members.

You can host your application on any of the member clusters inside the
service mesh, such as:

- On Kubernetes clusters outside of the ones that you deploy with the Kubernetes Operator, or
- On the member clusters in a multi-Kubernetes cluster MongoDB deployment.

(Figure: /images/multi-cluster-arch-with-service-mesh.svg)
      deployment across regions and availability zones using the
      MongoDB Controllers for Kubernetes Operator, with a service mesh
:figwidth: 600px

### Diagram: Multi-Kubernetes Cluster Deployment without a Service Mesh

The following diagram shows the high-level architecture of a multi-Kubernetes cluster MongoDB deployment
across regions and availability zones. This deployment doesn't rely on a
service mesh for connectivity between the Kubernetes clusters hosting Pods
with MongoDB instances.

To handle external communication between MongoDB replica set members hosted
on Pods in distinct Kubernetes clusters, use external domains and DNS zones.

(Figure: /images/multi-cluster-arch-no-service-mesh.svg)
      deployment across regions and availability zones using the
      MongoDB Controllers for Kubernetes Operator, and without a service mesh
:figwidth: 600px

You can host your application on any of the member clusters.
