<!-- Converted from tutorial/plan-k8s-operator-install.txt (reStructuredText). Includes are inlined. -->

# Plan your MongoDB Controllers for Kubernetes Operator Installation

**Important:**

This section is for single Kubernetes cluster deployments only. For
multi-Kubernetes cluster MongoDB deployments, see multi-cluster-overview-ref.

Use the MongoDB Controllers for Kubernetes Operator to deploy:

- Ops Manager resources
- MongoDB standalone, replica set, and sharded cluster resources

To deploy MongoDB resources with the Kubernetes Operator, you need an
Ops Manager instance. Deploy this instance to Kubernetes using the Operator or
outside Kubernetes using
`traditional installation methods`. The
Operator uses Ops Manager API (Application Programming Interface) methods to deploy and then manage MongoDB
resources.

Architecture
  Review the architecture of the custom resources in the Kubernetes Operator:
  the Ops Manager and the MongoDB database.

Compatibility
  Review compatible versions of Kubernetes, OpenShift, MongoDB, and Ops Manager.

Container Images
  Review container image details.

Single- or Multi-Kubernetes Clusters
  Decide whether to set up single or multiple Kubernetes clusters for your custom
  MongoDB resources.

Set Deployment Scope
  Set the scope for the Kubernetes Operator deployment by configuring which
  type of namespace the Kubernetes Operator should use.

k8s-considerations
  Review Kubernetes Operator deployment scopes and other preparation 
  information.

k8s-prerequisites
  Review the prerequisites before you install the Kubernetes Operator.
