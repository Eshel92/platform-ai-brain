<!-- Converted from tutorial/recover-mcsc-no-k8sop-cluster.txt (reStructuredText). Includes are inlined. -->

# Recover the Sharded Cluster if the Central Cluster Fails

If the Kubernetes cluster on which your Kubernetes Operator is deployed fails, 
you first need to recover the Kubernetes Operator. To do so, deploy and configure the 
Kubernetes Operator on a separate, healthy Kubernetes cluster as described in the 
steps below. Then, once you've redeployed the Kubernetes Operator to a healthy Kubernetes 
cluster, you can follow these recovery steps. 

If your Ops Manager instance is also deployed to your central cluster, 
follow these steps to redeploy to a healthy 
Kubernetes cluster.

## Procedure

**Step 1: Redeploy the Kubernetes Operator.**

You can follow this guide to install the 
Kubernetes Operator on a separate, healthy Kubernetes cluster as you did originally. 

**Step 2: Configure the Kubernetes Operator and the Kubernetes cluster for multi-cluster deployments.**

Use the `kubectl mongodb multicluster setup` command to set up credentials, roles 
and permissions and create mongodb-kubernetes-operator-member-list config 
map for the operator. 

See Understand Kubernetes Roles and Role Bindings to learn more.

**Step 3: Restore the Kubernetes Operator deployment state.**

MongoDB resources: apply yaml files from backup or Git repository if 
following GitOps. 

1. Restore the following config maps and secrets referenced by 
   the MongoDB resource: 

   - `spec.credentials` (secret)
   - `spec.opsManager.configMapRef.name`

2. Restore the deployment state config map named `<resource-name>-state`. 

   This config map is required for the Kubernetes Operator to 
   correctly reconcile your MongoDB database. It is created 
   dynamically at runtime by the Kubernetes Operator. In order to restore it, 
   you must have previously set up a separate process that periodically 
   backs this config map up.

   If this config map cannot be restored from backup, please contact 
   MongoDB Support before proceeding with the recovery steps.

3. Recreate TLS certificates, and related TLS secrets. You can either 
   create them manually or with Cert-Manager. Note that if the restored 
   TLS certificates are changed (re-issued) then the replicaset automation 
   might perform the TLS certificate rotation procedure. 

**Step 4: Continue the restoration process with a working Kubernetes Operator deployment.**

After performing the above steps, continue the restoration process
by following the steps in this guide.
