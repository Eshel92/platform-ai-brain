<!-- Converted from tutorial/plan-k8s-op-architecture.txt (reStructuredText). Includes are inlined. -->

# Kubernetes Operator Architecture

**Important:**

This section is for single Kubernetes cluster deployments only. For
multi-Kubernetes cluster MongoDB deployments, see multi-cluster-arch-ref.

The MongoDB Controllers for Kubernetes Operator provides a container image for the MongoDB Agent in Ops Manager. This
allows you to manage and deploy MongoDB database clusters with full monitoring,
backups, and automation provided by Ops Manager.

The Kubernetes container serves as a host on which Ops Manager orchestrates the
installation of `mongod` processes and deploys the cluster configuration.

As part of deployment, the Kubernetes Operator creates [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for
the Ops Manager StatefulSets. The Kubernetes container uses [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to maintain the cluster state
between restarts.

The Kubernetes Operator architecture consists of:

- **An Ops Manager custom resource**. Through this resource, the Kubernetes Operator
  deploys Ops Manager components: the application database, the Ops Manager
  application, and the Backup Daemon in the Kubernetes containers. After the deployment
  is operational, the Ops Manager components reconcile updates that you make to
  the MongoDB cluster configuration. To learn more, see meko-om-arch.
  
- **MongoDB database custom resources**. The Kubernetes Operator deploys the `MongoDB`
  database and the mongodbuser-specification. After the deployment is
  operational, these resources reconcile updates that you make to the
  user or the MongoDB cluster configuration. To learn more, see mdb-resources-arch.
