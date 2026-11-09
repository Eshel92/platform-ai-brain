<!-- Converted from configure-k8s-operator-for-mdb-resources.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure the Kubernetes Operator for MongoDB Database Resources

create-k8s-credentials
  Create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) so the Kubernetes Operator can create and update
  [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in your Cloud Manager or Ops Manager Project.

create-k8s-project
  Create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to link the Kubernetes Operator to your Cloud Manager or Ops Manager
  Project.

create-x509-certs
  Create an X.509 certificate to connect to an X.509-enabled
  MongoDB deployment.
