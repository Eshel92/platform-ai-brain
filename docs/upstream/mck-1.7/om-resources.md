<!-- Converted from om-resources.txt (reStructuredText). Includes are inlined. -->

# Deploy Ops Manager Resources on Kubernetes Clusters

meko-om-arch
  Review the Ops Manager resource architecture.

plan-om-resource
  Review the Ops Manager resource considerations and prerequisites.

deploy-om-multi-cluster
 Deploy the Ops Manager instances and the Application Database replica sets
 securely on multiple Kubernetes clusters.

deploy-om-container
  Use the Kubernetes Operator to deploy the Ops Manager resources securely on a
  single Kubernetes cluster.

deploy-om-container-remote-mode
  Use the Kubernetes Operator to configure Ops Manager to operate in **Remote** mode
  on a single Kubernetes cluster.
  In Remote mode, the Backup Daemons and managed MongoDB resources download
  installation archives from HTTP endpoints on a web server or S3-compatible
  file store deployed to your Kubernetes cluster instead of from the Internet.

deploy-om-container-local-mode
  Use the Kubernetes Operator to configure Ops Manager to operate in **Local** mode
  on a single Kubernetes cluster.
  In Local mode, the Backup Daemons and managed MongoDB resources download
  installation archives from a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that you create for the Ops Manager
  StatefulSet instead of from the Internet.

meko-upgrade-om-version
  Upgrade the versions of your Ops Manager instance and backing databases
  that the Kubernetes Operator uses to manage your deployment.

configure-om-queryable-backups
  Configure queryable backups for Ops Manager deployments created with the Kubernetes Operator.

configure-file-store
  Configure backup snapshot storage for Ops Manager resources created with the Kubernetes Operator.

configure-kmip-backup-encryption
  Configure KMIP (Key Management Interoperability Protocol) backup encryption.

cert-manager-integration
  Configure automated certificate renewal for Ops Manager deployments with `cert-manager`.

disaster-recovery-om-appdb
  Manually recover the Kubernetes Operator, the Ops Manager Application, and the Application Database
  in cases when the Kubernetes cluster hosting the Kubernetes Operator fails, or when
  the Application Database\'s replica set loses node majority to elect a primary.
