<!-- Converted from tutorial/modify-resource-image.txt (reStructuredText). Includes are inlined. -->

# Modify Ops Manager or MongoDB Kubernetes Resource Containers

You can modify the containers in the [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) in which Ops Manager and
MongoDB database resources run using the `template` or
`podTemplate` setting that applies to your deployment:

- MongoDB database: `spec.podSpec.podTemplate`
- Ops Manager: `spec.statefulSet.spec.template`
- backup-daemon: `spec.backup.statefulSet.spec.template`

To review which fields you can add to a `template` or a
`podTemplate`, see the `Kubernetes documentation`.

When you create containers with a `template` or `podTemplate`, the
Kubernetes Operator handles container creation differently based on the
`name` you provide for each container in the `containers` array:

- If the `name` field *matches* the name of the applicable resource
  image, the Kubernetes Operator updates the Ops Manager or MongoDB database
  container in the [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) to which the `template` or
  `podTemplate` applies:

  - Ops Manager: `mongodb-kubernetes-ops-manager`
  - backup-daemon: `mongodb-backup-daemon`
  - MongoDB database: `mongodb-enterprise-database`
  - Application Database: `mongodb-kubernetes-appdb`

- If the `name` field *does not match* the name of the applicable
  resource image, the Kubernetes Operator creates a new container in each
  [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) to which the `template` or `podTemplate` applies.

## Define a Volume Mount for a MongoDB Kubernetes Resource

On-disk files in containers in [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) don't survive container
crashes or restarts. Using the `spec.podSpec.podTemplate`
setting, you can add a `volume mount`
to persist data in a MongoDB database resource for the life of the
[Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/).

To create a volume mount for a MongoDB database resource:

1. Update the MongoDB database resource definition to include a volume
   mount for containers in the database pods that the Kubernetes Operator
   creates.

   **Example:**

   Use `spec.podSpec.podTemplate` to define a volume mount:

   ```yaml
   podSpec:
     podTemplate:
       spec:
         containers:
         - name: mongodb-enterprise-database
           volumeMounts:
           - mountPath: </new/mount/path>
             name: survives-restart
         volumes:
         - name: survives-restart
           emptyDir: {}
   ```

#. Apply the updated resource definition:

   ```sh
   kubectl apply -f <database-resource-conf>.yaml -n <metadata.namespace>
   ```

## Tune MongoDB Kubernetes Resource Docker Images with an InitContainer

`MongoDB` resource Docker images run on RHEL and use RHEL's default
system configuration. To tune the underlying RHEL system
configuration in the `MongoDB` resource containers, add a privileged
InitContainer
`init container`
using one of the following settings:

- `spec.podSpec.podTemplate`: add a privileged InitContainer
  to a MongoDB database resource container.

- `spec.statefulSet.spec.template`: add a privileged
  InitContainer to an Ops Manager resource container.

**Example:**

MongoDB database resource Docker images use the RHEL default
`keepalive` time of `7200`. MongoDB recommends a shorter
`keepalive` time of `120` for database deployments.

You can tune the `keepalive` time in the database resource Docker
images if you experience network timeouts or socket errors in
communication between clients and the database resources.

**See also:**

Does TCP keepalive time affect MongoDB Deployments? in the
MongoDB Manual

To tune Docker images for a MongoDB database resource container:

1. Update the MongoDB database resource definition to append a
   privileged InitContainer to the database pods that the
   Kubernetes Operator creates.

   **Example:**

   Change `spec.podSpec.podTemplate` the `keepalive`
   value to the recommended value of `120`:

   ```yaml
   spec:
     podSpec:
       podTemplate:
         spec:
           initContainers:
           - name: "adjust-tcp-keepalive"
             image: "busybox:latest"
             securityContext:
               privileged: true
             command: ["sysctl", "-w", "net.ipv4.tcp_keepalive_time=120"]
   ```

#. Apply the updated resource definition:

   ```sh
   kubectl apply -f <database-resource-conf>.yaml -n <metadata.namespace>
   ```

Kubernetes adds a privileged InitContainer to each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) that the
Kubernetes Operator creates using the `MongoDB` resource definition.

Open a shell session to a running container in your database resource
[Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) and verify your changes.

**Example:**

To follow the previous `keepalive` example, invoke the following
command to get the current `keepalive` value:

```sh
> kubectl exec -n <metadata.namespace> -it <pod-name> -- cat /proc/sys/net/ipv4/tcp_keepalive_time

> 120
```

**See also:**

Operating System Configuration in the
MongoDB Manual.

## Build Custom Images with Dockerfile Templates

You can modify MongoDB Dockerfile templates to create custom 
Kubernetes Operator images that suit your use case. To build a 
custom image, you need:

- Your custom Dockerfile, modified from a MongoDB template.

- The MongoDB-provided context image for your template.

### MongoDB Dockerfile Templates

The Dockerfiles used to build container images are publicly 
available from the 
[MongoDB Kubernetes GitHub repository](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/public/dockerfiles).

The Dockerfile directory is organized by resource name, version and 
distribution:

```sh
├── <resource name>
│   └── <image version>
│       └── <base distribution>
│           └── Dockerfile template
```

Copy the template you want to use to your own Dockerfile and modify as 
desired.

### Context Images

To build an image from any MongoDB Dockerfile template, you must supply 
its context image. 

Each Dockerfile template has one associated context image, retrievable 
from the same [Quay](https://quay.io/) registry as the original images. Context image are
always tagged in the format `quay.io/mongodb/<resource-name>:<image-version>-context`.

To supply a context image to `docker build`, include the 
`--build-arg` option with the `imagebase` variable set to a 
Quay.io tag, where `<resource-name>` and `<image-version>` match 
your Dockerfile template.

**Example:**

If you want to build the `mongodb-enterprise-database` version 
2.0.0 image for any distribution, include:

```sh
--build-arg imagebase=quay.io/mongodb/mongodb-kubernetes-database:2.0.0-context
```

### `docker build` Example

The Ubuntu distribution for `mongodb-kubernetes-operator` version 
1.9.1 is based on `ubuntu:1604` by default. In this example, that 
base Dockerfile template is modified to use `ubuntu:1804` and 
saved as `myDockerfile`.

The following command builds the custom image and gives it the tag 
`1.9.1-ubuntu-1804`:
 

```sh
cat myDockerfile | docker build --build-arg imagebase=quay.io/mongodb/mongodb-kubernetes-operator:1.9.1-context \
--tag mongodb-kubernetes-operator:1.9.1-ubuntu-1804 -
```

**Note:**

Include a hyphen (`-`) at the end of `docker build` to read 
the output of `cat myDockerfile` instead of providing a 
local directory as build context.

      

**See also:**

To learn more about `docker build`, see the 
[Docker documentation](https://docs.docker.com/engine/reference/commandline/build/).
