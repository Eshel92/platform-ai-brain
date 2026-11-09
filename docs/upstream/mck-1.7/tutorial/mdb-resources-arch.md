<!-- Converted from tutorial/mdb-resources-arch.txt (reStructuredText). Includes are inlined. -->

# MongoDB Database Architecture in Kubernetes

**Important:**

This section is for single Kubernetes cluster deployments only. For
multi-Kubernetes cluster MongoDB deployments, see multi-cluster-arch-ref.

  
You can use the Kubernetes Operator and Cloud Manager or Ops Manager to deploy MongoDB database
resources to a Kubernetes cluster. You can use an existing Cloud Manager or Ops Manager, or deploy
Ops Manager in Kubernetes to manage your databases.

The Kubernetes Operator uses Cloud Manager or Ops Manager to manage the following MongoDB database custom resources:

- `MongoDB`
- `MongoDBUser`

Your [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) specifications define these resources in the Kubernetes Operator.
The Kubernetes Operator monitors these resources. When you update the
resource's specification, the Kubernetes Operator pushes these changes to
Cloud Manager or Ops Manager, which make changes to the MongoDB deployment's configuration.

## The `MongoDB` Custom Resource Definition

The Kubernetes Operator manages MongoDB database deployments
which are defined by MongoDB custom resources.

The MongoDB database [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) specification defines the
following types of the MongoDB database custom resources:

- `Standalone`
- `ReplicaSet`
- `ShardedCluster`

The following diagram illustrates the composition of each type of the MongoDB
resource in the Kubernetes Operator.

(Figure: /images/mdb-resources-arch.svg)
      the MongoDB Controllers for Kubernetes Operator
:figwidth: 600px

**Warning:**

Kubernetes Operator doesn't support arbiter nodes.

### Standalone

For the `Standalone` type of the MongoDB database resource, the Kubernetes Operator
deploys a replica set with a single member to the Kubernetes cluster as a
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

The Kubernetes Operator creates the StatefulSet, which contains the Pod
specification with the number of Pods to create. The Kubernetes Operator
relies on the Kubernetes StatefulSet Controller to create a Pod for this
standalone MongoDB database instance.

**Important:**

In Kubernetes, a `Standalone` resource is equivalent to a `ReplicaSet`
resource with only one member. We recommend that you deploy
a `ReplicaSet` with one member instead of a `Standalone`
because a replica set allows you to add members to it in
the future.

### Replica Set

For the `ReplicaSet` type of the MongoDB resource, the Kubernetes Operator
deploys a replica set to the Kubernetes cluster as a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), with
a number of members equal to the value of `spec.members`.

The Kubernetes Operator relies on the Kubernetes StatefulSet Controller to create
one Pod in the StatefulSet for each member of the replica set.

Each Pod in the StatefulSet runs a MongoDB Agent instance.

### Sharded Cluster

The `ShardedCluster` type of the MongoDB resource consists of one or more
Config Servers, `mongos` instances, and shard members.

For the `ShardedCluster` resource, the Kubernetes Operator deploys:

- One StatefulSet for all Config Servers
- One StatefulSet for all `mongos` instances
- One StatefulSet for each Shard Member

The Kubernetes Operator relies on the Kubernetes StatefulSet Controller to
create one Pod in each of the StatefulSets created for the sharded cluster.

## Reconciling the `MongoDB` Custom Resource

When you apply a MongoDB custom resource specification,
the Kubernetes Operator deploys each resource as a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
to the Kubernetes cluster.

The Kubernetes Operator:

- Watches the custom resource's specification and associated
  [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) or secrets stored in your 
  secret storage tool.
- Validates the changes when the specification file, the ConfigMap,
  or the secret change.
- Makes the appropriate updates to the MongoDB database resources
  in the Kubernetes cluster.
- Pushes the changes to Cloud Manager or Ops Manager, which make changes to the MongoDB
  deployment's configuration.

### Diagram of a Replica Set Reconciliation

The following diagram describes how the Kubernetes Operator behaves
if you make changes to a replica set's:

- `MongoDB` custom resource specifications
- Associated [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
- Associated secrets stored in your 
  secret storage tool

(Figure: /images/mdb-resources-replica-set-reconciliation.svg)
      Operator makes changes to the MongoDB Custom Resource Definition
      for a replica set
:figwidth: 600px

### Diagram of a Sharded Cluster Reconciliation

The following diagram describes how the Kubernetes Operator behaves if
you make changes to a sharded cluster's:

- `MongoDB` custom resource specifications
- Associated [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
- Associated secrets stored in your 
  secret storage tool

(Figure: /images/mdb-resources-sharded-reconciliation.svg)
      Operator makes changes to the MongoDB Custom Resource Definition
      for a sharded cluster
:figwidth: 600px

### Reconciliation Workflow

When you create or change a MongoDB resource specification, or when you make
changes to an associated [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) or secret, the Kubernetes Operator
performs the following actions to reconcile the changes:

1. Reads the required organization and project configuration
   from the ConfigMap
   that you used to create or connect to a project in the Kubernetes Operator.

   If you change your resource specification, the Kubernetes Operator identifies
   that the change took place, and checks the specification for the ConfigMap
   specified in `spec.opsManager.configMapRef.name`.

   **Note:**

   When you configure the Kubernetes Operator for MongoDB resources,
   you create a ConfigMap to connect
   or create your Cloud Manager or Ops Manager project. The MongoDB Agent uses this ConfigMap
   to start or make changes to the deployment for the MongoDB resource.

2. Reads the authentication configuration for Cloud Manager or Ops Manager from
   the secret specified in either: 
   
   - `spec.credentials` in the resource specification
   - Your secret storage tool
   
   This secret stores the
   `Cloud Manager API keys`
   or the `Ops Manager API Keys`
   required for the Kubernetes Operator to authenticate to Cloud Manager or Ops Manager.
   

   **Note:**

   When you configure the Kubernetes Operator for MongoDB resources,
   you either create this secret in Kubernetes or store this
   secret in your secret storage tool.

3. The Kubernetes Operator connects to Cloud Manager or Ops Manager and performs the following actions:

   - Reads the organization from the `orgId` field in the ConfigMap.
     You must provide a value in the `orgId` field.

   - Reads a project name specified in the `projectName` field in the
     ConfigMap, or, if you didn't specify a value for this optional field,
     creates this project in Cloud Manager or Ops Manager if it doesn't exist.

   - Checks that the `<project-id>-group-secret` secret
     created by the Kubernetes Operator for the MongoDB Agent exists.
     The Kubernetes Operator reads the secret from your secret storage tool,
     or creates it with
     `Ops Manager API keys`
     or `Cloud Manager API keys`.
     
   - Registers itself as a watcher of the ConfigMap and this secret.
     This enables the Kubernetes Operator to react to changes that you make
     to the ConfigMap or the secret.

4. The Kubernetes Operator verifies any TLS and X.509 certificates.
      
   - If TLS is enabled for a replica set, the
     Kubernetes Operator looks for certificates provided in the
     `<prefix>-<resource-name>-cert` secret or your 
     secret storage tool.
     
   - If TLS is enabled for a sharded cluster, the
     Kubernetes Operator looks for certificates in these secrets:
      
     - `<prefix>-<resource-name>-x-cert` for each shard member.
     - `<prefix>-<resource-name>-config-cert` for all config servers.
     - `<prefix>-<resource-name>-mongos-cert` for all `mongos` instances.
     - Your secret storage tool.

   - If X.509 or
     internal authentication with X.509 and  TLS
     are enabled, the Kubernetes Operator checks that their certificates
     contain the required configuration.

5. The Kubernetes Operator locates and updates the necessary StatefulSets,
   or creates new StatefulSets if they don't exist. The number of
   StatefulSets depends on the type of the MongoDB resource.

   - For `ReplicaSet` or `Standalone` resources,
     the Kubernetes Operator creates a single StatefulSet.

   - For a `ShardedCluster` resource, the Kubernetes Operator creates:
    
     - One StatefulSet for all config servers.
     - One StatefulSet for all `mongos` instances.
     - One StatefulSet for each shard member.
   
     At this point, each Pod runs at least one MongoDB Agent instance,
     but does not yet contain `mongod` instances.
        
   - Each MongoDB Agent instance starts polling Cloud Manager or Ops Manager to receive the
     MongoDB automation configuration.
     

     **Note:**

     **Non-static containers:** When the MongoDB Agent receives the configuration for 
     the first time, it downloads the MongoDB binaries with the version
     specified in `spec.version` from the Internet, or
     from Ops Manager if the MongoDB Agent is configured in local mode. 

     **Static containers:** Static containers do not download binaries at runtime. 
     To learn more, see static-containers. 

     
   - After the MongoDB Agent receives the automation configuration, it starts a
     `mongod` instance on the corresponding Pod.

   - For each Pod of each StatefulSet that the MongoDB custom resource creates,
     except for `mongos` StatefulSets, the Kubernetes Operator generates a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).
     You can override this behavior by setting `spec.persistent` to
     `false` in the resource specification.

6. The Kubernetes Operator updates the automation configuration it received from the
   MongoDB Agent with changes from the specifications and sends it to Cloud Manager or Ops Manager.

   - Each MongoDB Agent for each Pod polls Cloud Manager or Ops Manager again and receives the
     updated automation configuration.

   - If you change any field in the specification, the Kubernetes Operator
     performs a [rolling update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) of the StatefulSets to start new Pods
     matching the new specification.
     
   - The Kubernetes Operator waits for each MongoDB Agent to report that it reached
     the ready state.

   **Note:**

   If you change the security configuration
   of a database resource, or `scale down`
   an existing StatefulSet, the Kubernetes Operator runs step 6 before it
   runs  step 5.

7. The Kubernetes Operator updates the Kubernetes services, or for a new MongoDB
   resource, creates the services required for each new StatefulSet.

   For the [ServiceType](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) `ClusterIP`, the Kubernetes Operator sets
   `ClusterIP` to `None`, and performs these actions:

   - Creates this service if it doesn't exist.
  
   - For `ReplicaSet` or `Standalone` resources, the Kubernetes Operator
     names the service with the custom resource's name  with `-svc`
     appended to it.
   - For a `ShardedCluster` resource, the Kubernetes Operator uses these
     naming conventions:
  
     - For `mongos` instances, the Kubernetes Operator uses the name specified in
       `spec.service`, or the resource's name  with `-svc`
       appended to it.
     - For the config servers, the Kubernetes Operator uses the resource's name
       with `-cs` appended to it.
     - For each shard, the Kubernetes Operator uses the resource's name
       with `-sh` appended to it.

   - For the port, the Kubernetes Operator uses the default port 27017, or
     the .net.port
     specified in `spec.additionalMongodConfig`.

## Reconciling the `MongoDBUser` Custom Resource

If the user authentication method is set to SCRAM,
the mongodbuser-specification depends
on the secret storage tool that stores the
user credentials.  If you are using a Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/), you specify the
secret in the `spec.passwordSecretKeyRef` settings in the `MongoDBUser`
resource specification.

The Kubernetes Operator watches the secret for changes. If you make changes
to the secret's configuration, the Kubernetes Operator reconciles the
changes. It takes the following actions:

1. Determines the MongoDB user's resource based on the value
   specified in the `spec.MongoDBResourceRef.name` setting in the
   mongodbuser-specification.

2. Connects to Cloud Manager or Ops Manager:

   - Reads the organization from the `orgId` in the ConfigMap.
   - Reads a project's name from `projectName` in the ConfigMap,
     or creates this project in Cloud Manager or Ops Manager if it doesn't exist.
   - Checks that the `<project-id>-group-secret` created by the
     Kubernetes Operator for the MongoDB Agent exists.
     The Kubernetes Operator reads the secret from your secret storage tool,
     or creates it with
     `Ops Manager API keys`
     or `Cloud Manager API keys`.
     
3. Updates the user's credentials in Cloud Manager or Ops Manager, or creates a new user if it doesn't exist.
   
   - If the user authentication method is SCRAM,
     reads the password from the secret.
   - Reads the user name. If the user name has changed, the Kubernetes Operator
     removes the old name and adds a new one.
   - Ensures that the user exists in Cloud Manager or Ops Manager.

The following diagram describes how the Kubernetes Operator behaves if you make
changes to the user secret or the mongodbuser-specification.

(Figure: /images/mdb-user-resource-reconciliation.svg)
      Operator reconciles changes to the MongoDBUser
      Custom Resource Definition
:figwidth: 600px
