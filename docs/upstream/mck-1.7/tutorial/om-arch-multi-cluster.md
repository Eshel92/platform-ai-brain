<!-- Converted from tutorial/om-arch-multi-cluster.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Ops Manager Architecture

This section describes specific considerations for deploying the Ops Manager Application
and the Application Database on multiple Kubernetes clusters, where you set
`spec.topology` and `spec.applicationDatabase.topology`
to `MultiCluster`.

This section addresses the following areas:

- Single- and Multi-Cluster Mode
- Limitations
- Differences between Single and Multi-cluster Deployments

**Note:**

For actual deployment steps, see deploy-om-multi-cluster.

## Single- and Multi-Cluster Mode

The following settings in the k8s-om-specification define the mode
in which you deploy the Ops Manager Application and the Application Database custom
resources:

- Multi-cluster mode. To deploy the Ops Manager Application and the Application Database
  on multiple Kubernetes clusters, set `spec.topology` and
  `spec.applicationDatabase.topology` to `MultiCluster`.

  If you define `spec.topology` and `spec.applicationDatabase.topology`
  as `MultiCluster`, this allows you to begin with a single-member Kubernetes cluster
  and scale your multi-cluster deployment as needed. In particular:

  - You can create a deployment in a multi-cluster mode that has only one
    member cluster.
  - You can have the replica set of a minimum 3 `mongod` processes for the
    Application Database deployed on a single member cluster in a multi-cluster
    mode. To increase resilience of the Application Database, you can expand
    the replica set to span across multiple Kubernetes clusters and redeploy
    the configuration.

  - You can have a single Ops Manager Application instance deployed on a single member
    cluster in a multi-cluster mode. To increase resilience of the Ops Manager Application,
    you can add more Kubernetes clusters, add the Ops Manager Application instances on them
    and redeploy the configuration.

- Single cluster mode. To deploy the Ops Manager Application and the Application Database
  on a single Kubernetes cluster, omit specifying the values for the following
  settings, or set `spec.topology` and
  `spec.applicationDatabase.topology` to `SingleCluster`.

## Limitations

Deploying the Ops Manager Application and the Application Database on multiple Kubernetes
clusters has the following limitations:

- You can't change the topology of an existing Ops Manager deployment from
  single to multi-cluster. You can set `spec.topology` and
  `spec.applicationDatabase.topology` to `MultiCluster`
  only for new deployments of the Ops Manager Application.

- You can't use [HashiCorp Vault](https://www.vaultproject.io/) in any multi-cluster Kubernetes deployments.
  This includes multi-cluster deployments of Ops Manager resources,
  the Application Database resources, and `MongoDBMultiCluster` resources.

## Differences between Single and Multi-Cluster Ops Manager Deployments

The following table lists the differences between single and multi-Kubernetes
cluster deployments of the Ops Manager Application and the Application Database.
All other features not listed in this table are equivalent for single and
multi-cluster deployments.

| Capability or Requirement | Single-Cluster Deployment | Multi-Cluster Deployment |
|---|---|---|
| You must install the Kubernetes Operator in the same cluster as the Ops Manager Application and the Application Database. | Yes | No. The central cluster can also host the Ops Manager Application, the Application Database and the Backup Daemon. To learn more, see om-multi-k8s-diagram. |
| You must configure the Kubernetes Operator for single or multi-cluster mode. | No. | Yes |
| Service mesh is required for Kubernetes clusters hosting the Ops Manager Application and the Application Database. | No | Yes |
| Alternative Secret Storage ([HashiCorp Vault](https://www.vaultproject.io/)) is supported. | Yes | No. To learn more, see om-multi-k8s-limitations. |
| All backup mechanisms are supported. | Yes | No. Only S3 (Simple Storage Service)-compatible Oplog and snapshot storage backups are supported. To learn more, see `spec.clusterSpecList[*].backup`.` |
| KMIP (Key Management Interoperability Protocol) encryption | Yes | With limitations. |

Use the following resources to help you learn about the architecture and
performance of a multi-Kubernetes cluster deployment, and to configure networking:

- Architecture Diagram
- Networking, Load Balancer, Service Mesh
- Performance
