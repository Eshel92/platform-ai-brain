<!-- Converted from tutorial/plan-k8s-op-container-images.txt (reStructuredText). Includes are inlined. -->

# Container Images

When you install the Kubernetes Operator, it pulls the images from the Quay.io
container registry. The Kubernetes Operator images are based on the
[Red Hat UBI 8 and 9](https://www.redhat.com/en/topics/containers)
operating systems. MongoDB rebuilds Kubernetes Operator images daily for the
latest operating system and supporting library updates.

**Note:**

MongoDB Agent images pulled by static containers are always on Red Hat UBI 9.

Official images provide the following advantages:

- They are rebuilt daily for the latest upstream vulnerability fixes.
- MongoDB tests, maintains, and supports them.

To view all available versions for each image, see the following links.

| Image Name | Description | Supported Architecture |
|---|---|---|
| `mongodb-agent` | MongoDB Agent image built on Red Hat UBI 9 and used for static containers, the Application Database, and MongoDB Community Edition deployments. | Supports x86-64, ARM64, s390x, and ppc64le. Supports static and non-static containers for all versions of MongoDB Controllers for Kubernetes Operator. |
| `mongodb-agent-ubi` | Legacy MongoDB Agent image. | Supports x86-64 and ARM64. Supports non-static containers for all versions of MongoDB Controllers for Kubernetes Operator. Supports static containers for MongoDB Controllers for Kubernetes Operator 1.2.0 and earlier only. |
| `mongodb-enterprise-server` | The Enterprise MongoDB image used for static containers and the Application Database. For IBM ZSeries (s390x) and Power (ppc64le) architectures, images run on Red Hat UBI 9 only and support is limited to MongoDB 8.0.12+. | x86-64, ARM64, s390x, ppc64le |
| `mongodb-kubernetes-init-appdb` | `initContainer` image that contains the Application Database start-up scripts and the readiness probe. | x86-64, ARM64, s390x, ppc64le |
| `mongodb-kubernetes-database` | MongoDB Database environment image used for non-static containers. | x86-64, ARM64, s390x, ppc64le |
| `mongodb-kubernetes-init-database` | `initContainer` image that contains the MongoDB Agent start-up scripts and the readiness probe. | x86-64, ARM64, s390x, ppc64le |
| `mongodb-enterprise-ops-manager-ubi` | Ops Manager image. | x86-64 only |
| `mongodb-kubernetes-init-ops-manager` | `initContainer` image that contains the Ops Manager start-up scripts and the readiness probe. | x86-64 only |

## Static Containers (Public Preview)

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

You can use the Public Preview of
static containers instead of the existing non-static containers, which 
downloads the MongoDB binary from Cloud Manager or Ops Manager or the Internet at runtime.
You can use the procedures on this page to enable or disable static
containers for all or individual MongoDB deployments. 

Static containers use the image from the `mongodb-enterprise-server` Quay.io repository by
default, but you can use your own registry if you configured it for your
Kubernetes [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/). 

### Architecture

The architecture of static and non-static containers differs significantly and
requires several steps to migrate from one to the other. To learn more, see migrate-to-static-containers and migrate-to-non-static-containers.  

#### Non-Static Container Architecture

The default non-static container architecture assumes you bootstrap an empty-shell 
container, download and start the MongoDB Agent, which then downloads the binaries 
for `mongod` and `mongosh` from Cloud Manager or Ops Manager. 

(Figure: /images/mdb-deployment.svg)
      non-static containers configured using the MongoDB Controllers for Kubernetes Operator.
:figwidth: 600px

#### Static Container Architecture

The static container architecture uses Kubernetes' `shared namespace feature`
to run the MongoDB Agent as a separate process so it can control the full `mongod` lifecycle and avoid downloading files over a network.

(Figure: /images/mdb-deployment-static.svg)
      static containers configured using the MongoDB Controllers for Kubernetes Operator.
:figwidth: 600px

### Compatibility With Local or Remote Mode

If you use static containers, you don't need to configure Ops Manager to
run in Local Mode or
Remote Mode, unless you use
queryable backups. In static container architecture, the binaries
for the agent and `mongod` have their own container images and these
are not downloaded from Ops Manager. 

Queryable backups are the exception because in the non-static container
architecture, by default, the Backup Daemon downloads and runs the
MongoDB Server binaries for all versions that are backed-up. This
default MongoDB behavior undermines the fully static nature of the
containers used to run the Backup Daemon. If you use queryable backups,
you must still host the relevant MongoDB Server binaries using local or
remote mode. To learn more, see deploy-om-container-local-mode or
deploy-om-container-remote-mode.  

If you used Remote or Local mode before and don't want to use queryable
backups, do the following to ensure that `mongodb-enterprise-server`
[images](https://quay.io/repository/mongodb/mongodb-enterprise-server?tab=tags&tag=latest)  
can be downloaded on the [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) used by the pods: 

1. Configure an internal container registry for your Kubernetes nodes. 

   The [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) will download the images from [Quay.io](https://quay.io/repository/mongodb/mongodb-enterprise-server?tab=tags&tag=latest) 
   unless you use a local container registry.

2. Download and add the `mongodb-enterprise-server` [images](https://quay.io/repository/mongodb/mongodb-enterprise-server?tab=tags&tag=latest). 

### Limitations

If you enable static containers:

- Deployments on IBM ZSeries (s390x) or IBM Power (ppc64le) hardware architectures 
  support static containers only for MongoDB 8.0.12 and later.

- You must disable-queryable-backups so the backup-daemon
  doesn't attempt to download the MongoDB binaries from Ops Manager, which
  undermines the immutable nature of static containers.

- With Ops Manager, only versions 6.0.27+, 7.0.12+, and 8.0.0+ are compatible.
  The Kubernetes Operator automatically uses the correct version of the
  MongoDB Agent container based on the Ops Manager version 
  you select to manage a specific deployment. 

- With MongoDB Cloud Manager, your MongoDB Agent version could fall behind compatibility with the latest 
  version of MongoDB Cloud Manager because the Kubernetes Operator can't call the `agentVersion` endpoint 
  in MongoDB Cloud Manager. To ensure your MongoDB Agent is up to date with MongoDB Cloud Manager, you can perform one 
  of the following actions:

  - Specify a compatible MongoDB Agent version in the 
    MongoDB resource specification by
    overriding the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) container image for the MongoDB Agent. 
    For example:

    ```yaml
    podSpec:
      podTemplate:
        spec:
          containers:
            - name: mongodb-agent
              image: quay.io/mongodb/mongodb-agent:13.49.1.10399-1
    ```

  - Upgrade the Kubernetes Operator to the latest version, 
    which automatically updates the MongoDB Agent.

- Upgrading a MongoDB version triggers a rolling restart
  of all Pods, in order of last to first, and could cause more elections, up to the number of Pods. This is true of
  any updates that trigger a rolling restart. 

- You won't be able to determine whether a MongoDB database upgrade happened from 
  the MongoDB Agent's status. 
  When Kubernetes rotates Pods following an upgrade, the MongoDB Agent replaces the 
  health status file so you can't tell from the health status that a version change 
  happened, only the current health status.

### FAQs

#### Do static containers support local or remote mode?

No, if you use static containers, you don't need to configure Ops Manager
to run in Local Mode or
Remote Mode unless you use
queryable backups. To learn more, see Local and Remote Modes. 

#### What are the changes for static containers?

Static containers don't download the MongoDB binary at runtime.
Instead, it uses the images from the `mongodb-enterprise-server` Quay.io repository. To
learn more about the changes, see step 6. 

#### How can I verify if my deployment is running in static?

There are many ways to determine if your deployment is using static
container. To learn more, see step 7. 

### Migrate to Static Containers

To migrate from non-static to static containers, set the MongoDB Agent environment
variables and enable static containers by following the steps below.
You can also enable static containers during 
installation or upgrade. 

**Step 1: Review the limitations.**

**Step 2: Disable queryable backups.**

Follow the procedure in disable-queryable-backups.

If you want to use queryable backups, you must configure Ops Manager
resource to use Local Mode
or Remote Mode so that
the binaries for all versions in-use can be pulled from Ops Manager.

**Step 3: Remove [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) overrides for init containers, if any.**

There are no init containers used with the static container architecture.
If an override for an init container is present, the migration from non-static to static containers fails.

Remove any [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) overrides for init containers from your 
MongoDB resource specification or 
Ops Manager resource specification. 
For example, ensure none of the following settings have been configured for `initContainers`:

-  **Ops Manager:** `spec.statefulSet.spec`
-  **Application Database**: `spec.applicationDatabase.podSpec`
-  **Database:** statefulset-settings
-  **Multi-cluster:** spec.statefulSet.spec

**Step 4: Set environment variables for the MongoDB Agent image.**

**kubectl:**

In your Kubernetes Operator 
configuration file, define the MDB_AGENT_IMAGE_REPOSITORY environment variable to 
specify the repository from which the Kubernetes Operator downloads the MongoDB Agent 
image for static containers.

**helm:**

In your Kubernetes Operator Helm chart,
define agentRepo and agent-name-helm to specify the repository from which 
the Kubernetes Operator downloads the MongoDB Agent image for static containers.

**Step 5: Save and apply the file.**

After saving the changes, reapply your configuration.

**kubectl:**

If you use Kubernetes without OpenShift, run: 

```sh
kubectl apply -f mongodb-kubernetes.yaml
```

If you use Kubernetes with OpenShift:

```sh
oc apply -f mongodb-kubernetes-openshift.yaml
```

**helm:**

```sh
helm upgrade mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
  --set registry.pullPolicy='IfNotPresent'
```

This initiates a rolling restart of all Pods in your deployment.

**Step 6: Enable static containers.**

Select the appropriate tab below to enable static containers for all your MongoDB 
deployments at once, including existing deployments, or one deployment at a time.

**enable-static-all:**

In your Kubernetes Operator configuration file, 
set MDB_DEFAULT_ARCHITECTURE 
or operator.mdbDefaultArchitecture to `static`.

**enable-static-one:**

In the MongoDB resource specification for 
a specific deployment,
set the `metadata.annotations.mongodb.com/v1.architecture` 
annotation to `static`.

**Step 7: Save and apply the file.**

After saving the changes, reapply your configuration.

**kubectl:**

If you use Kubernetes without OpenShift, run: 

```sh
kubectl apply -f <my-config-file>.yaml
```

If you use Kubernetes with OpenShift:

```sh
oc apply -f <my-config-file>.yaml
```

**helm:**

```sh
helm upgrade mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
 --set <setting_1> --set <setting_2> --set operator.mdbDefaultArchitecture="static"
```

The Kubernetes Operator updates the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) images for your MongoDB deployment, 
transitioning from a single container that previously managed both the MongoDB Agent 
and MongoDB database, to a new configuration with two separate containers: one for 
the MongoDB Agent and another for the MongoDB database. This update initiates a 
rolling restart.

When you migrate to static containers, the following changes apply:

- Kubernetes [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) use their configured container registry
  to perform the downloads. 
- Monitoring agent and automation agent versions are aligned. 
- Kubernetes Operator, instead of the agent, handles MongoDB upgrades.  
- Kubernetes Operator replaces the existing images, which will cause a
  rolling restart. 

**Step 8: Verify that deployment is running in static.**

- Check the value for one of the following variables, which you
  must've set to `static`:   

  |  |  |
  |---|---|
  | `MDB_DEFAULT_ARCHITECTURE` | Variable for all deployments. |
  | `metadata.annotations[mongodb.com/v1.architecture]` | Per-deployment variable. |

- Check the database deployment to verify the usage of two separate
  images, one for the agent and one for MongoDB, and ensure that no
  init containers are deployed.

### Migrate to Non-Static Containers

To migrate from static to non-static containers, disable static containers by 
following the steps below.
You can also disable static containers during 
installation or upgrade.

**Step 1: Disable static containers.**

Select the appropriate tab below to disable static containers for all your MongoDB 
deployments at once, including existing deployments, or one deployment at a time.

**enable-static-all:**

In your Kubernetes Operator configuration file, 
set MDB_DEFAULT_ARCHITECTURE 
or operator.mdbDefaultArchitecture to `non-static`.

**enable-static-one:**

In the MongoDB resource specification for 
a specific deployment,
set the `metadata.annotations.mongodb.com/v1.architecture` 
annotation to `non-static`.

**Step 2: Save and apply the file.**

After saving the changes, reapply your configuration.

**kubectl:**

If you use Kubernetes without OpenShift, run: 

```sh
kubectl apply -f <my-config-file>.yaml
```

If you use Kubernetes with OpenShift:

```sh
oc apply -f <my-config-file>.yaml
```

**helm:**

```sh
helm upgrade mongodb-kubernetes-operator mongodb/mongodb-kubernetes \
 --set <setting_1> --set <setting_2> --set operator.mdbDefaultArchitecture="non-static"
```

The Kubernetes Operator replaces the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) images of your MongoDB 
deployment and initiates a rolling restart of all Pods in your deployment.
