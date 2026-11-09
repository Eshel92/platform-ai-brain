<!-- Converted from tutorial/om-arch.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Architecture in Kubernetes

`MongoDB Ops Manager`, or its cloud-based counterpart, Cloud Manager, is a required
component for any Enterprise MongoDB deployment. Ops Manager automates, monitors,
and performs backups of MongoDB databases. As shown in the following
diagram, the MongoDB Ops Manager consists of:

- The Ops Manager Application, which is the
  main Ops Manager component and the front-end UI application.
- The Application Database, which is the backing
  MongoDB database for Ops Manager.
- The Backup Daemon, which is the component supporting
  the Ops Manager Application in backup and restore processes.

The Kubernetes Operator supports deploying Ops Manager and its underlying Application Database
on a single or multiple Kubernetes clusters.

A multi-cluster deployment of the Ops Manager Application and the Application Database in
different zones, regions, or cloud providers increases availability and improves
resilience in case of disaster situations. To learn more, see om-multi-k8s.

Use the following resources to help you learn about and deploy the Ops Manager Application
and the Application Database using their [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) in the Kubernetes Operator:

- om-resource-crd-parts
- om-arch-reconciliation
- om-multi-k8s
