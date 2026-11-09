<!-- Converted from tutorial/plan-k8s-op-considerations.txt (reStructuredText). Includes are inlined. -->

# Considerations

This page details best practices and system configuration
recommendations for the MongoDB Controllers for Kubernetes Operator when running in production.

## Deploy Multiple MongoDB Replica Sets

We recommend that you use a single instance of the Kubernetes Operator
to deploy and manage your MongoDB replica sets.

To deploy more than 10 MongoDB replica sets in parallel,
you can increase the thread count of your Kubernetes Operator instance. 

## Specify CPU and Memory Resource Requirements

**Note:**

The following considerations apply:

- All sizing and performance recommendations for common MongoDB deployments
  through the Kubernetes Operator in this section are subject to change. Do
  not treat these recommendations as guarantees or limitations of any kind.

- These recommendations reflect performance testing findings and represent
  our suggestions for production deployments. We ran the tests on a cluster
  comprised of seven AWS EC2 instances of type `t2.2xlarge` and a
  master node of type `t2.medium`.

- The recommendations in this section don't discuss characteristics of
  any specific deployment. Your deployment's characteristics may differ
  from the assumptions made to create these recommendations. Contact
  [MongoDB Support](https://support.mongodb.com/welcome) for further help with sizings.

In Kubernetes, each Pod includes parameters that allow you
to specify `CPU resources`
and `memory resources` for each
container in the Pod.

To indicate resource bounds, Kubernetes uses the `requests and limits`
parameters, where:
  
- *request* indicates a lower bound of a resource.
- *limit* indicates an upper bound of a resource.

The following sections illustrate how to:

- set CPU and Memory for the Operator Pod.
- set CPU and Memory for MongoDB Pods.

For the Pods hosting Ops Manager, use the
default resource limits configurations.

## Consider Recommended Practices for Storage

The following recommendations are applicable to MongoDB deployments and Ops Manager Application database 
deployments managed by the Kubernetes Operator.

**Note:**

- Redundancy in the storage class is not required because MongoDB automatically replicates data between 
  the members of a replica set or shard.

- You can't share storage across members of a replica set or shard.

- Use the storage class that provides the best performance given your constraints. See 
  scale a deployment to learn more.
- Provision [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that support `ReadWriteOnce` for your storage class.
- On a worker node level, apply the best practices from MongoDB on Linux.
- Ensure that you use a storage class that supports [volume expansion](https://kubernetes.io/docs/concepts/storage/storage-classes/#allow-volume-expansion) 
  to enable database volume resizing.

## Use Static Containers (Public Preview)

Static containers are simpler and more secure than non-static
containers. Static containers are immutable at runtime, which means that
they don't change from the image used to create the container. In
addition: 

- While running, static containers don't download binaries or run
  scripts or other utilities over network connections. Static containers
  only download runtime configuration files.  
- While running, static containers don't modify any file except storage
  volume mounts. 
- You can run security scans on the container images to determine what is
  actually run as a live container, and the container that runs won't
  run binaries other than what was defined in the
  image.  
- Static containers don't require that you host the MongoDB binary on
  either Ops Manager or another HTTPS (Hypertext Transfer Protocol Secure) server, which is especially useful
  if you have an air-gapped environment.
- You can't run extensive `CMD` scripts for the static container.
- You can't copy files between static containers using `initContainer`. 

**Note:**

When deployed as static containers, a Kubernetes Operator deployment consists of
two containers with distinct roles:

- The `mongodb-agent` container runs the MongoDB Agent, which then runs the
  `mongod` process. This container handles the actual database workload.
- The `mongodb-enterprise-server` container provides the MongoDB binaries but does not run any active processes.

The MongoDB database inherits resource limit definitions from
the `mongodb-agent` container that runs the actual workload. Resource
limits set on the `mongodb-enterprise-server` container have no functional
impact on performance, though they still count toward node resource
allocation. To modify the resource limits for the MongoDB database resource,
you must specify your desired resource limits on the `mongodb-agent` container.

To learn more, see static-containers.

## Co-locate `mongos` Pods with Your Applications

You can run the lightweight `mongos` instance on the same [node](https://kubernetes.io/docs/concepts/architecture/nodes/)
as your apps using MongoDB. The Kubernetes Operator supports standard Kubernetes
`node affinity and anti-affinity`
features. Using these features, you can force install the `mongos`
on the same node as your application.

The following abbreviated example shows affinity and multiple
availability zones configuration.

The `podAffinity` key determines whether to install an application
on the same Pod, node, or data center as another application.

To specify Pod affinity:

1. Add a label and value in the `spec.podSpec.podTemplate.metadata.labels`
   YAML (Yet Another Markup Language) collection to tag the deployment. See
   `spec.podSpec.podTemplate.metadata`,
   and the
   `Kubernetes PodSpec v1 core API`.

#. Specify which label the `mongos` uses in the
   `spec.mongosPodSpec.podAffinity`
   `.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`
   YAML (Yet Another Markup Language) collection. The `matchExpressions` collection defines the
   `label` that the Kubernetes Operator uses to identify the Pod for hosting
   the `mongos`.

**Example:**

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-replica-set
spec:
  members: 3
  version: 8.0.0
  service: my-service

  ...
    podTemplate:
      spec:
        affinity:
          podAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                    - key: security
                      operator: In
                      values:
                        - S1
                topologyKey: failure-domain.beta.kubernetes.io/zone
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
                - matchExpressions:
                    - key: kubernetes.io/e2e-az-name
                      operator: In
                      values:
                        - e2e-az1
                        - e2e-az2
          podAntiAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                topologyKey: nodeId
```

See the full example of multiple availability zones and node affinity
configuration in
replica-set-affinity.yaml
in the Affinity Samples
directory.

This directory also contains sample affinity and multiple
zones configurations for sharded clusters and standalone
MongoDB deployments.

**See also:**

- `Assigning Pods to Nodes`
- `Node affinity and anti-affinity`
- `Kubernetes PodSpec v1 core API`

## Name Your MongoDB Service with its Purpose

Set the `spec.service` parameter to a value that identifies
this deployment's purpose, as illustrated in the following example.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-replica-set
spec:
  members: 3
  version: "8.0.0"
  service: drilling-pumps-geosensors
  featureCompatibilityVersion: "8.0"
```

**See also:**

`spec.service`

## Use Labels to Differentiate Between Deployments

Use the `Pod affinity`
Kubernetes feature to:

- Separate different MongoDB resources, such as `test`, `staging`,
  and `production` environments.

- Place [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) on some specific nodes to take advantage of
  features such as SSD (Solid State Disk) support.

```yaml
mongosPodSpec:
  podAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
        matchExpressions:
        - key: security
          operator: In
          values:
          - S1
        topologyKey: failure-domain.beta.kubernetes.io/zone
```

**See also:**

`Pod affinity`

## Customize the CustomResourceDefinitions that the Kubernetes Operator Watches

You can specify which custom resources you want the Kubernetes Operator
to watch. This allows you to install the CustomResourceDefinition for
only the resources that you want the Kubernetes Operator to manage.

You must use `helm` to configure the Kubernetes Operator to watch only the
custom resources you specify. Follow the relevant `helm`
installation instructions,
but make the following adjustments:

1. Decide which CustomResourceDefinitions you want to install. You can
   install any number of the following:

   | Value | Description |
   |---|---|
   | `mongodb` | Install the CustomResourceDefinitions for database resources and watch those resources. |
   | `mongodbusers` | Install the CustomResourceDefinitions for MongoDB user resources and watch those resources. |
   | `opsmanagers` | Install the CustomResourceDefinitions for Ops Manager resources and watch those resources. |

#. Install the Helm Chart and specify which 
   CustomResourceDefinitions you want the 
   Kubernetes Operator to watch.
   
   Separate each custom resource with a comma:

   ```sh
   helm install <deployment-name> mongodb/mongodb-kubernetes \
     --set operator.watchedResources="{mongodb,mongodbusers}" \
        --skip-crds
   ```

## Ensure Proper Persistence Configuration

The Kubernetes deployments orchestrated by the Kubernetes Operator are
stateful. The Kubernetes container uses [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to maintain the
cluster state between restarts.

To satisfy the statefulness requirement, the Kubernetes Operator performs
the following actions:

- Creates [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for your MongoDB deployment.
- Mounts storage devices to one or more directories
  called mount points.
- Creates one persistent volume for each MongoDB mount point.
- Sets the default path in each Kubernetes container to `/data`.

To meet your MongoDB cluster's storage needs, make the following
changes in your configuration for each replica set deployed with
the Kubernetes Operator:

- Verify that persistent volumes are enabled in
  `spec.persistent`. This setting defaults to `true`.
- Specify a sufficient amount of storage for the Kubernetes Operator
  to allocate for each of the volumes. The volumes store the data
  and the logs.

  - To set multiple volumes, each for data, logs, and the `oplog`, use
    `spec.podSpec.persistence.multiple.data`.
  - To set a single volume to store data, logs, and the `oplog`,
    use `spec.podSpec.persistence.single`.

The following abbreviated example shows recommended persistent storage
sizes.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-replica-cluster
spec:

  ...
  persistent: true

  shardPodSpec:
  ...
    persistence:
      multiple:
        data:
          storage: "20Gi"
        logs:
          storage: "4Gi"
          storageClass: standard
```

For a full example of persistent volumes configuration, see
replica-set-persistent-volumes.yaml
in the Persistent Volumes Samples directory. This
directory also contains sample persistent volumes configurations for
sharded clusters and standalone deployments.

**See also:**

- `spec.persistent`
- `spec.podSpec.persistence.single`
- `spec.podSpec.persistence.multiple.data`

## Set CPU and Memory Utilization Bounds for the Kubernetes Operator Pod

When you deploy MongoDB replica sets with the Kubernetes Operator, the initial 
reconcilliation process increases CPU usage for the Pod running the 
Kubernetes Operator. However, when the replica set deployment process completes, 
the CPU usage by the Kubernetes Operator reduces considerably. 

**Note:**

The severity of CPU usage spikes in the Kubernetes Operator is directly impacted
by the thread count of the 
Kubernetes Operator, as the thread count (defined by the MDB_MAX_CONCURRENT_RECONCILES value) 
is equal to the number of reconcilliation processes that can be running in 
parallel at any given time.

For production deployments, to satisfy deploying up to 50 MongoDB
replica sets or sharded clusters in parallel with the Kubernetes Operator,
set the CPU and memory resources and limits for the Kubernetes Operator Pod
as follows:

- `spec.template.spec.containers.resources.requests.cpu` to 500m
- `spec.template.spec.containers.resources.limits.cpu` to 1100m
- `spec.template.spec.containers.resources.requests.memory` to 200Mi
- `spec.template.spec.containers.resources.limits.memory` to 1Gi

If you use Helm to deploy resources, define these values in 
the values.yaml file. 
  
The following abbreviated example shows the configuration with
recommended CPU and memory bounds for the Kubernetes Operator Pod in your
deployment of 50 replica sets or sharded clusters. If you are
deploying fewer than 50 MongoDB clusters, you may use lower
numbers in the configuration file for the Kubernetes Operator Pod.

**Example:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
 name: mongodb-kubernetes-operator
 namespace: mongodb
spec:
 replicas: 1
 selector:
  matchLabels:
     app.kubernetes.io/component: controller
     app.kubernetes.io/name: mongodb-kubernetes-operator
     app.kubernetes.io/instance: mongodb-kubernetes-operator
 template:
  metadata:
   labels:
     app.kubernetes.io/component: controller
     app.kubernetes.io/name: mongodb-kubernetes-operator
     app.kubernetes.io/instance: mongodb-kubernetes-operator
   spec:
     serviceAccountName: mongodb-kubernetes-operator
     securityContext:
       runAsNonRoot: true
       runAsUser: 2000
     containers:
     - name: mongodb-kubernetes-operator
       image: quay.io/mongodb/mongodb-kubernetes-operator:1.9.2
       imagePullPolicy: Always
       args:
        - "-watch-resource=mongodb"
        - "-watch-resource=opsmanagers"
        - "-watch-resource=mongodbusers"
       command:
        - "/usr/local/bin/mongodb-kubernetes-operator"
       resources:
         limits:
           cpu: 1100m
           memory: 1Gi
         requests:
           cpu: 500m
           memory: 200Mi
```

For a full example of CPU and memory utilization resources and limits
for the Kubernetes Operator Pod that satisfy parallel deployment of up to
50 MongoDB replica sets, see the mongodb-kubernetes.yaml
file.

**See also:**

- `Requests and Limits`
- `Assign CPU Resources to Containers and Pods`

## Set CPU and Memory Utilization Bounds for MongoDB Pods

The values for Pods hosting replica sets or sharded clusters map
to the `requests field`
for CPU and memory for the created Pod. These values are consistent
with considerations
stated for MongoDB hosts.

The Kubernetes Operator uses its allocated memory for processing, for the
WiredTiger cache, and for storing packages during the deployments.

For production deployments, set the CPU and memory resources and limits
for the MongoDB Pod as follows:

- `spec.podSpec.podTemplate.spec.containers.resources.requests.cpu` to 0.25
- `spec.podSpec.podTemplate.spec.containers.resources.limits.cpu` to 0.25
- `spec.podSpec.podTemplate.spec.containers.resources.requests.memory` to 512M
- `spec.podSpec.podTemplate.spec.containers.resources.limits.memory` to 512M

If you use Helm to deploy resources, define these values in 
the values.yaml file. 

The following abbreviated example shows the configuration with
recommended CPU and memory bounds for each Pod hosting a MongoDB
replica set member in your deployment.

**Example:**

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
name: my-replica-set
spec:
  members: 3
  version: 8.0.0
  service: my-service
  ...

  persistent: true
  podSpec:
    podTemplate:
      spec:
        containers:
        - name: mongodb-enterprise-database
          resources:
            limits:
              cpu: "0.25"
              memory: 512M
```

For a full example of CPU and memory utilization resources and limits
for Pods hosting MongoDB replica set members, see the
replica-set-podspec.yaml
file in the MongoDB Podspec Samples directory.

This directory also contains sample CPU and memory limits
configurations for Pods used for:

- A sharded cluster, in the sharded-cluster-podspec.yaml.
- Standalone MongoDB deployments, in the standalone-podspec.yaml.

**See also:**

- `spec.podSpec.podTemplate.spec`
- `Requests and Limits`
- `Assign CPU Resources to Containers and Pods`

## Use Multiple Availability Zones

Set the Kubernetes Operator and [statefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) to distribute all members
of one replica set to different [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) to ensure high
availability.

The following abbreviated example shows affinity and multiple
availability zones configuration.

**Example:**

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-replica-set
spec:
  members: 3
  version: 8.0.0
  service: my-service
  ...
    podAntiAffinityTopologyKey: nodeId
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
        matchExpressions:
        - key: security
          operator: In
          values:
          - S1
        topologyKey: failure-domain.beta.kubernetes.io/zone

    nodeAffinity:
       requiredDuringSchedulingIgnoredDuringExecution:
         nodeSelectorTerms:
         - matchExpressions:
           - key: kubernetes.io/e2e-az-name
           operator: In
           values:
           - e2e-az1
           - e2e-az2
```

In this example, the Kubernetes Operator schedules the Pods deployment to
the nodes which have the label `kubernetes.io/e2e-az-name` in `e2e-az1` or
`e2e-az2` availability zones. Change `nodeAffinity` to
schedule the deployment of Pods to the desired availability zones.

See the full example of multiple availability zones configuration in
replica-set-affinity.yaml
in the Affinity Samples
directory.

This directory also contains sample affinity and multiple zones
configurations for sharded clusters and standalone MongoDB deployments.

**See also:**

- `Running in Multiple Zones`
- `Node affinity`

## Increase Thread Count to Run multiple Reconciliation Processes in Parallel

If you plan to deploy more than 10 MongoDB replica sets in parallel, 
you can configure the Kubernetes Operator to run multiple reconciliation processes 
in parallel by setting MDB_MAX_CONCURRENT_RECONCILES environment variable in your Kubernetes Operator 
deployment or or through the operator.maxConcurrentReconciles field in your Helm 
`values.yaml` file to configure a higher thread count. 

Increasing the thread count of the Kubernetes Operator allows you to vertically scale your Kubernetes Operator 
deployment to hundreds of `MongoDB` resources running within your Kubernetes cluster  
and optimize CPU utilization.

Please monitor Kubernetes API server and Kubernetes Operator resource usage and adjust their respective 
resource allocation if necessary.

**Note:**

- Proceed with caution when increasing the MDB_MAX_CONCURRENT_RECONCILES beyond 10.
  In particular, you must monitor the Kubernetes Operator, and the Kubernetes API 
  closely to avoid downtime resulting from increased load on those components. 

  To determine the thread count that suits your deployment's needs, 
  use the following guidelines:

  - Your requirements for how responsive the Kubernetes Operator must be when 
    reconciling many resources

  - The compute resources available within your Kubernetes environment and 
    the total processing load your Kubernetes compute resources are under, including 
    resources that may be unrelated to MongoDB

- An alternative to increasing the thread count of a single Kubernetes Operator 
  instance, while still increasing the number of `MongoDB` resources you can support 
  in your Kubernetes cluster, is to deploy multiple Kubernetes Operator instances within 
  your Kubernetes cluster. However, deploying multiple Kubernetes Operator 
  instances requires that you ensure that no two Kubernetes Operator instances
  are monitoring the same `MongoDB` resources.

  Running more than one instance of the Kubernetes Operator should be done with care, 
  as more Kubernetes Operator instances (especially with parallel reconciliation enabled) 
  put the API server at greater risk of being overwhelmed. 

- Scaling of the Kubernetes API server is not a valid reason to run 
  more than one instance of the Kubernetes Operator. If you observe that performance of 
  the API server is affected, adding more instances of the Kubernetes Operator is 
  likely to compound the problem.
