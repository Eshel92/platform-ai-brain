<!-- Converted from index.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# MongoDB Controllers for Kubernetes Operator

**Important:**

Kubernetes Operator deploys MongoDB Enterprise, `Ops Manager`, and MongoDB Community to Kubernetes. Due to the breadth of 
configuration options available for MongoDB Enterprise and `Ops Manager`, this guide focuses on these deployment options.

To deploy MongoDB Community in Kubernetes, see [the documentation on GitHub](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/docs/mongodbcommunity).

The MongoDB Controllers for Kubernetes Operator translates the human knowledge of creating a MongoDB
instance into a scalable, repeatable, and standardized method.
Kubernetes needs help creating and managing stateful applications like
databases. It needs to configure the network, persist storage, and
dedicate computing capacity without additional human effort on each
container.

The Kubernetes Operator manages the typical lifecycle events for a MongoDB
cluster: provisioning storage and computing power, configuring network
connections, setting up users, and changing these settings as needed.
It accomplishes this using the Kubernetes API and tools.

You provide the MongoDB Controllers for Kubernetes Operator with the specifications for your MongoDB
cluster. The MongoDB Controllers for Kubernetes Operator uses this information to specify to Kubernetes how to
configure that cluster including provisioning storage, setting up the
network connections, and configuring other resources.

(Figure: /images/kubernetes-operator.bakedsvg.svg)

For MongoDB Enterprise deployments, MongoDB Controllers for Kubernetes Operator works together with MongoDB Cloud Manager or Ops Manager, which further
configures to MongoDB clusters. When MongoDB is deployed and running in
Kubernetes, you can manage MongoDB tasks using Cloud Manager or Ops Manager.

You can then deploy MongoDB databases as you deploy them now after the
cluster is created. You can use the Cloud Manager or Ops Manager console to run MongoDB at
optimal performance.

The MongoDB Controllers for Kubernetes Operator is an operator that replaces the previous MongoDB
Enterprise Kubernetes Operator and MongoDB Community Operator. For more information
about the first version of Kubernetes Operator, see the release notes.

**See also:**

- faq-k8s-advanced
- k8s-faq
