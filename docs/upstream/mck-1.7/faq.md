<!-- Converted from faq.txt (reStructuredText). Includes are inlined. -->

# Frequently Asked Questions

## What is an Operator?

An operator is a standard mechanism that extends the control plane of
Kubernetes to managing custom Kubernetes resources. Because each operator is
built for its own Custom Resources (CRs), it can contain logic that
addresses the type of service that the operator is built for. For the
Kubernetes Operator, the operator includes the logic for the deployment of
MongoDB Server and Ops Manager instances.

Each CR used by the Kubernetes Operator represents an element of a MongoDB 
Server deployment in Kubernetes, and has options for customizing that part
of the deployment. Once you configure these objects in the Kubernetes 
deployment, the operator builds native Kubernetes objects, such as Stateful 
Sets that are necessary to create Pods according to your specified 
requirements for MongoDB Servers. The Kubernetes Operator also facilitates
configuration of MongoDB Server features, such as database backups, 
through interaction with MongoDB Cloud Manager or Ops Manager.

## Why run MongoDB Enterprise Advanced on Kubernetes?

Running MongoDB on Kubernetes simplifies the setup and management of self-hosting MongoDB. 

The Kubernetes Operator works with MongoDB and `Ops Manager` to automate configuration using 
custom resource files that you create to define your setup. This allows you to 
manage the configuration using whatever tools you already have for managing 
applications in Kubernetes, including tools that enable a GitOps workflow where 
configuration is managed in a Git repository. The high level of automation and 
abstraction from complexity makes Kubernetes and the Kubernetes Operator especially well 
suited to running MongoDB as a service, either for internal users or external customers.

Kubernetes allows MongoDB to take advantage of the scalability and automated resilience 
that Kubernetes offers, like the automated replacement of a lost Pod making up 
a replica set or sharded cluster. This allows MongoDB to be highly scalable and 
resilient when running in Kubernetes.

## How scalable is MongoDB in Kubernetes?

MongoDB within Kubernetes is as scalable as MongoDB on bare metal or VMs. For many 
customers, scalability is easier to achieve within Kubernetes. The Kubernetes Operator and Kubernetes 
work seamlessly together to enable easy horizontal scaling, including the ability 
to span MongoDB deployments across multiple Kubernetes clusters for multi-cluster and 
multi-site resilience. 

Vertical scaling is as easy as changing the resources for a deployment in the 
custom resource that defines it.

All of this allows MongoDB to scale to meet any demands.

## Are there any downsides to running MongoDB within Kubernetes?

There are no downsides from a technical perspective. MongoDB within Kubernetes is as 
performant and scalable as MongoDB running on any hardware or infrastructure. 

But, as with any infrastructure, there is an inherent requirement for customers 
to have familiarity and expertise with the technology, in this case Kubernetes. 
While the Kubernetes Operator simplifies and automates the setup of MongoDB within Kubernetes, 
there is still a dependency on the underlying resources and capabilities that are 
part of the Kubernetes cluster, things like stateful storage, networking, security, 
and compute. This means that customers still need to ensure that those 
services and resources are available and configured correctly to support MongoDB, 
much as this would be needed if running on bare metal or virtual machines.

## Which Kubernetes platforms are supported for MongoDB Server deployments?

MongoDB Server supports any platform that builds upon native Kubernetes without
changing the default logic or behavior. In practice, this means that
MongoDB Server supports any Kubernetes platform
[certified by the Cloud Native Computing Foundation](https://www.cncf.io/certification/software-conformance/).
To learn more, see MongoDB Kubernetes Operator Compatibility.

## How many deployments can MongoDB Controllers for Kubernetes Operator support?

Kubernetes Operator can support hundreds of deployments. 
To facilitate parallel reconciliation operations and avoid prolonged 
reconciliation times, increase thread count of your Kubernetes Operator instance.

## Should I run MongoDB Server in Kubernetes in the same cluster as the application using it?

To help minimize latency, consider colocating your database and applications on
the same Kubernetes cluster if your deployment architecture allows this.

## Can I deploy MongoDB Server across multiple Kubernetes clusters?

Yes. To learn more, see Deploy MongoDB Resources on Multiple Kubernetes Clusters.
For help, contact [MongoDB Support](https://support.mongodb.com/welcome).

## What is the difference between using the Kubernetes Operator for managing multi-Kubernetes cluster MongoDB deployments and  managing a single Kubernetes cluster?

To use the Kubernetes Operator for managing a multi-Kubernetes cluster MongoDB deployment, you must set up a specific set of 
Kubernetes `Roles, ClusterRoles`, 
`RoleBindings, ClusterRoleBindings`,
and `ServiceAccounts`.

The Kubernetes Operator used for a multi-Kubernetes cluster MongoDB deployment can also reconcile a single Kubernetes cluster resource.
To learn more, see faq-many-operators.

## Does MongoDB support running more than one Kubernetes Operator instance?

If possible, we recommend that you set up a single Kubernetes Operator instance to
watch one, many, or all namespaces within your Kubernetes cluster. By default,
the Kubernetes Operator watches all [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) types that you choose
to deploy, and you don't need to configure it to watch specific resource types.

However, once you reach a performance limit
for the number of deployments a single Kubernetes Operator instance can support,
you can set up an additional Kubernetes Operator instance. At this point,
consider how you want to divide up management of resources in the Kubernetes cluster.
Use the following recommendations listed in the order of priority:

- Ensure that each Kubernetes Operator instance is watching different and non-overlapping
  namespaces within the Kubernetes cluster.
- Alternatively, configure different instances of the Kubernetes Operator to watch
  different resource types, either in different namespaces or overlapping namespaces.
  
  If you choose to use overlapping namespaces, ensure that each Kubernetes Operator
  instance watches different types of resources to avoid conflict that would
  result in two instances of the Kubernetes Operator attempting to manage
  the same resources.

**Note:**

Before you configure another Kubernetes Operator instance, verify that none of its
namespaces are included in the subset of namespaces for the existing Kubernetes Operator instance.
