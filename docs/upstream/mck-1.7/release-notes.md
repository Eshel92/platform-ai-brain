<!-- Converted from release-notes.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Release Notes for MongoDB Controllers for Kubernetes Operator (MCK)

## MCK v1.7.0

*Released 10 February 2026*

- To view the changelog for Kubernetes Operator version 1.7.0, see the 
  official [MongoDB Controllers for Kubernetes Release Notes](https://github.com/mongodb/mongodb-kubernetes/releases/tag/1.7.0).

## MCK v1.6.1

*Released 16 December 2025*

- To view the changelog for Kubernetes Operator version 1.6.1, see the 
  official [MongoDB Controllers for Kubernetes Release Notes](https://github.com/mongodb/mongodb-kubernetes/releases/tag/1.6.1).

## MCK v1.6.0

*Released 17 November 2025*

- To view the changelog for Kubernetes Operator version 1.6.0, see the 
  official [MongoDB Controllers for Kubernetes Release Notes](https://github.com/mongodb/mongodb-kubernetes/releases/tag/1.6.0).

## MCK v1.5.0

### New Features

- **Improved Automation Agent Certificate Rotation** 

  - The agent now restarts automatically when its certificate is renewed, 
    ensuring smooth operation and seamless certificate updates without manual 
    intervention. 

### Bug Fixes

- MongoDBMultiCluster: Fixed resource stuck in Pending state if any 
  `clusterSpecList` item has 0 members. After the fix, a value of 0 members 
  is handled correctly, as in the MongoDB resource.
  
- MultiClusterSharded: Blocked removing non-zero member clusters from MongoDB 
  resource. This prevents scaling down member clusters without current 
  configuration available, which could lead to unexpected issues.

## MCK v1.4.0

*Released 17 September 2025*

### New features

- **MongoDB Search and Vector Search (Public Preview) Support**

  - Launches Public Preview of MongoDB Search and Vector Search for self-managed MongoDB
    Enterprise Server deployments, which makes it easier to build AI-powered apps on your own infrastructure and eliminates the need for a separate vector database.
  - This Public Preview is compatible with MongoDB Enterprise Server version 8.0.10+ 
    and is intended for testing, evaluation, and feedback.
  - The search process (`mongot`) must run in Kubernetes, but your database cluster 
    (`mongod`) can run on your existing infrastructure, either inside the same 
    Kubernetes cluster or on external VMs and bare-metal servers. This allows you to adopt
    powerful search features without needing to migrate your current database workloads.
  - Supports deployments running as replica sets.
  - Supports TLS (Transport Layer Security) encryption for all communication between the `mongod` and `mongot`
    processes.

## MCK v1.3.0

*Released 04 September 2025*

### New features

- **Multi-Architecture Support**

  - Adds comprehensive multi-architecture support for the Kubernetes Operator.
  - Supports deployment on IBM Power (ppc64le) and IBM Z (s390x) architectures alongside existing x86_64 support. 
  - Core images (operator, agent, init containers, database, readiness
    probe) now support multiple architectures. But, this release doesn't add IBM and ARM
    support for Ops Manager and the `mongodb-kubernetes-init-ops-manager`
    images. 

    **Note:**

    This release migrates MongoDB Agent images to a new container
    repository, `quay.io/mongodb/mongodb-agent`. 

    - The agents in the new repository support the x86-64, ARM64,
      s390x, and ppc64le architectures. To learn more, see
      k8s-container-images. 
    - Kubernetes Operator running version greater than or equal to 1.3.0
      and static can't use the agent images from the old container
      repository, `quay.io/mongodb/mongodb-agent-ubi`. 

    Don't use `quay.io/mongodb/mongodb-agent-ubi` as it is
    made available only for backwards compatibility.

### Bug Fixes

* Fixes the current architecture for stateful set containers, which
  relies on an "agent matrix" to map operator and agent versions. The
  new design eliminates the `operator-version/agent-version` matrix,
  but adds one additional container containing all required binaries.
  This architecture maps to the `mongodb-database` container.
* Fixes an issue where the readiness probe reported the node as ready
  even when its authentication mechanism was not in sync with the other
  nodes, sometimes resulting in premature restarts. 
* Fixes an issue where the MongoDB Agents didn't adhere to the
  `NO_PROXY` environment variable configured on the operator. 
* Changes webhook `ClusterRole` and `ClusterRoleBinding` default
  names to include the namespace so that multiple operator installations
  in different namespaces don't conflict with each other. 

### Other Changes

* Moves optional permissions for `PersistentVolumeClaim` to a separate
  role. 

  When you manage the operator with [Helm](https://helm.sh/), you could disable permissions
  for `PersistentVolumeClaim` resources by setting
  `operator.enablePVCResize` value to `false`, which is `true` by
  default. If enabled, these permissions were part of the primary
  operator role. With this change, permissions have a separate role.

* Removes `subresourceEnabled` [Helm](https://helm.sh/) value.
 
  This setting was `true` by default. You could exclude subresource
  permissions from the operator role by specifying `false` as the
  value. This setting was introduced as a temporary solution for the
  OpenShift issue (Bug 1803171). The issue has since been resolved and
  the setting is no longer needed. Therefore, this change removes this
  configuration option, making the operator roles always have
  subresource permissions. 

* Doesn't include container images for Ops Manager versions 7.0.16, 8.0.8,
  8.0.9 and 8.0.10 due to a bug in Ops Manager that prevents Kubernetes Operator
  users from upgrading their Ops Manager deployments of these versions.

## MCK v1.2.0

*Released 10 July 2025*

### New features

- **OpenID Connect (OIDC) user authentication**
   - Adds support for OpenID Connect (OIDC) user authentication.
   - You can configure OIDC authentication with the 
     `spec.security.authentication.modes` and 
     `spec.security.authentication.oidcProviderConfigs` 
     settings.
   - Requires MongoDB Enterprise Server 7.0.11+ or 8.0.0+.
   - For more information, see:
      - Enable Authentication
      - Manage Database Users Using OIDC Authentication

- **New ClusterMongoDBRole CRD**
   - Adds new ClusterMongoDBRole CRD 
     to support reusable roles across multiple MongoDB clusters. This 
     allows users to define roles once and reuse them in multiple 
     MongoDB or MongoDBMultiCluster resources.
   - You can reference this role using the 
     `spec.security.roleRefs` 
     field. Note that only one of 
     `spec.security.roles` and 
     `spec.security.roleRefs` 
     can be used at a time.
   - The operator treats ClusterMongoDBRole resources as custom role 
     templates that are only used when referenced by the database 
     resources.
   - The operator watches the new resource by default. This means 
     that the operator requires you to create a new ClusterRole and 
     ClusterRoleBinding. The helm chart or the kubectl mongodb plugin 
     create these ClusterRole and ClusterRoleBinding by default. You 
     must create them manually if you use a different installation 
     method.
   - To disable this behavior in the helm chart, set the 
     `operator.enableClusterMongoDBRoles` value to `false`. This 
     disables the creation of the necessary RBAC resources for the 
     ClusterMongoDBRole resource, and disables the watch for 
     this resource.
   - To skip installing necessary ClusterRole and ClusterRoleBinding 
     with the kubectl mongodb plugin, set the 
     `--create-mongodb-roles-cluster-role` to `false`.
   - The new ClusterMongoDBRole resource is designed to be read-only, 
     meaning it can be used by MongoDB deployments managed by 
     different operators.
   - You can delete the ClusterMongoDBRole resource at any time, but 
     the operator does not delete any roles that were created using 
     this resource. To properly remove access, you must manually 
     remove the reference to the ClusterMongoDBRole in the MongoDB or 
     MongoDBMultiCluster resources.
   - The reference documentation for this resource can be found in 
     the ClusterMongoDBRole Resource Specification.

### Bug Fixes

* Fixes an issue where moving a MongoDBMultiCluster resource to a new project (or a new `Ops Manager` instance) would leave the deployment in a failed state.

## MCK v1.1.0

*Released 23 May 2025*

### New features

- **MongoDBSearch (Community Private Preview)**
   - Adds support for deploying MongoDB Search (Community Private Preview Edition).
   - Enables full-text and vector search capabilities for MongoDBCommunity deployments.
   - Adds new MongoDB CRD which is watched by default by the Kubernetes Operator. For more information see the [Quick Start](https://github.com/mongodb/mongodb-kubernetes/blob/1.1.0/docs/community-search/quick-start/README.md).
   - MongoDBSearch Private Preview phase comes with the following limitations
      - Minimum MongoDB Community version: 8.0.
      - TLS must be disabled in MongoDB (communication between `mongot` and `mongod` is in plaintext for now).

## MCK v1.0.1

*Released 13 May 2025*

### Bug Fixes

* Adds missing MongoDB Agent images in the Kubernetes Operator bundle in the OpenShift catalog and the [operatorhub.io](https://operatorhub.io/) catalog.
* Adds the missing `mongodbcommunity` CRD from the watched list in the [Helm chart](https://github.com/mongodb/helm-charts/tree/main/charts/mongodb-kubernetes).  

## MCK v1.0.0

*Released 9 May 2025*

MongoDB is unifying its Kubernetes offerings with the introduction of Kubernetes Operator. 
This new operator is an open-source project and represents a merge of the previous 
[MongoDB Community Operator](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/docs/mongodbcommunity) 
and the MongoDB Enterprise Kubernetes Operator. This makes it 
easier to manage, scale, and upgrade your deployments. Future changes build on this 
to more closely align how Community and Enterprise are managed 
in Kubernetes, to offer an even more seamless and streamlined experience. 

As an open-source project, it now allows for community contributions, helping drive quicker bug 
fixes and ongoing innovation.

## License

Users with contracts that allowed use of the Enterprise Operator can still leverage the new replacement, 
allowing customers to adopt it without contract changes. Kubernetes Operator itself is licensed under the 
Apache 2.0 license, and a [license file](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0) 
included in the repository provides further detail. 

License entitlements for all other MongoDB products and tools, such as 
MongoDB Enterprise Server and Ops Manager, remain unchanged. If you have
licensing questions regarding these products or tools, please contact your 
MongoDB account team.

## Migration

Migration from the Community Kubernetes Operator and the Enterprise Kubernetes Operator to 
Kubernetes Operator is seamless: your MongoDB deployments are not impacted by the upgrade and 
require no changes. Follow the instructions in the migration guide.

## Legacy Operator Deprecation and EOL

We continue best-effort support of the Community Kubernetes Operator for 6 months,
until November, 2025. Each Enterprise Kubernetes Operator release remains supported 
according to the guidance in place at the time of that release.

All future bug fixes and improvements are released in new versions of Kubernetes Operator. 
We encourage all users to plan their migration to Kubernetes Operator within these timelines.

## Older Release Notes

To view older release notes for the Kubernetes Operator, see the [Legacy Documentation](https://www.mongodb.com/docs/legacy/).
