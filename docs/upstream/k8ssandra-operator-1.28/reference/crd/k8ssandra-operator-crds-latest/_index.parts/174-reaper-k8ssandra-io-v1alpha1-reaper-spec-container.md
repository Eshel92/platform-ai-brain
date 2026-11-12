<!-- Part 174 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### Reaper.spec.containerImage
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



The image to use for the Reaper pod main container.
The default is "thelastpickle/cassandra-reaper:4.0.0-rc1".

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          The image name to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pullPolicy</b></td>
        <td>enum</td>
        <td>
          The image pull policy to use. Defaults to "Always" if the tag is "latest", otherwise to "IfNotPresent".<br/>
          <br/>
            <i>Enum</i>: Always, IfNotPresent, Never<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspeccontainerimagepullsecretref">pullSecretRef</a></b></td>
        <td>object</td>
        <td>
          The secret to use when pulling the image from private repositories. If specified, this secret will be passed to
individual puller implementations for them to use. For example, in the case of Docker, only DockerConfig type
secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>registry</b></td>
        <td>string</td>
        <td>
          The Docker registry to use. Defaults to "docker.io", the official Docker Hub.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>repository</b></td>
        <td>string</td>
        <td>
          The Docker repository to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          The image tag to use. Defaults to "latest".<br/>
          <br/>
            <i>Default</i>: latest<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.containerImage.pullSecretRef
<sup><sup>[↩ Parent](#reaperspeccontainerimage)</sup></sup>



The secret to use when pulling the image from private repositories. If specified, this secret will be passed to
individual puller implementations for them to use. For example, in the case of Docker, only DockerConfig type
secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
This field is effectively required, but due to backwards compatibility is
allowed to be empty. Instances of this type with an empty value here are
almost certainly wrong.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
          <br/>
            <i>Default</i>: <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.datacenterRef
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



DatacenterRef is the reference of a CassandraDatacenter resource that this Reaper instance should manage. It will
also be used as the backend for persisting Reaper's state. Reaper must be able to access the JMX port (7199 by
default) and the CQL port (9042 by default) on this DC.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          The datacenter name.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          The datacenter namespace. If empty, the datacenter will be assumed to reside in the same namespace as the Reaper
instance.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.httpManagement
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>enabled</b></td>
        <td>boolean</td>
        <td>
          Enable/disable the HTTP management connection between Reaper and Cassandra.
When enabled, HTTP will be used instead of JMX for management connectivity between Cassandra
and Reaper.<br/>
          <br/>
            <i>Default</i>: true<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspechttpmanagementkeystores">keystores</a></b></td>
        <td>object</td>
        <td>
          LocalObjectReference contains enough information to let you locate the
referenced object inside the same namespace.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.httpManagement.keystores
<sup><sup>[↩ Parent](#reaperspechttpmanagement)</sup></sup>



LocalObjectReference contains enough information to let you locate the
referenced object inside the same namespace.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
This field is effectively required, but due to backwards compatibility is
allowed to be empty. Instances of this type with an empty value here are
almost certainly wrong.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
          <br/>
            <i>Default</i>: <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerImage
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



Deprecated: The main container image will be used for the init container as well.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          The image name to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pullPolicy</b></td>
        <td>enum</td>
        <td>
          The image pull policy to use. Defaults to "Always" if the tag is "latest", otherwise to "IfNotPresent".<br/>
          <br/>
            <i>Enum</i>: Always, IfNotPresent, Never<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainerimagepullsecretref">pullSecretRef</a></b></td>
        <td>object</td>
        <td>
          The secret to use when pulling the image from private repositories. If specified, this secret will be passed to
individual puller implementations for them to use. For example, in the case of Docker, only DockerConfig type
secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>registry</b></td>
        <td>string</td>
        <td>
          The Docker registry to use. Defaults to "docker.io", the official Docker Hub.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>repository</b></td>
        <td>string</td>
        <td>
          The Docker repository to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          The image tag to use. Defaults to "latest".<br/>
          <br/>
            <i>Default</i>: latest<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerImage.pullSecretRef
<sup><sup>[↩ Parent](#reaperspecinitcontainerimage)</sup></sup>



The secret to use when pulling the image from private repositories. If specified, this secret will be passed to
individual puller implementations for them to use. For example, in the case of Docker, only DockerConfig type
secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
This field is effectively required, but due to backwards compatibility is
allowed to be empty. Instances of this type with an empty value here are
almost certainly wrong.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
          <br/>
            <i>Default</i>: <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerResources
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



Init Container resources.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#reaperspecinitcontainerresourcesclaimsindex">claims</a></b></td>
        <td>[]object</td>
        <td>
          Claims lists the names of resources, defined in spec.resourceClaims,
that are used by this container.

This is an alpha field and requires enabling the
DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>limits</b></td>
        <td>map[string]int or string</td>
        <td>
          Limits describes the maximum amount of compute resources allowed.
More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>requests</b></td>
        <td>map[string]int or string</td>
        <td>
          Requests describes the minimum amount of compute resources required.
If Requests is omitted for a container, it defaults to Limits if that is explicitly specified,
otherwise to an implementation-defined value. Requests cannot exceed Limits.
More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerResources.claims[index]
<sup><sup>[↩ Parent](#reaperspecinitcontainerresources)</sup></sup>



ResourceClaim references one entry in PodSpec.ResourceClaims.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name must match the name of one entry in pod.spec.resourceClaims of
the Pod where this field is used. It makes that resource available
inside a container.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>request</b></td>
        <td>string</td>
        <td>
          Request is the name chosen for a request in the referenced claim.
If empty, everything from the claim is made available, otherwise
only the result of this request.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerSecurityContext
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



InitContainerSecurityContext is the SecurityContext applied to the Reaper init container, used to perform schema
migrations.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>allowPrivilegeEscalation</b></td>
        <td>boolean</td>
        <td>
          AllowPrivilegeEscalation controls whether a process can gain more
privileges than its parent process. This bool directly controls if
the no_new_privs flag will be set on the container process.
AllowPrivilegeEscalation is true always when the container is:
1) run as Privileged
2) has CAP_SYS_ADMIN
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainersecuritycontextapparmorprofile">appArmorProfile</a></b></td>
        <td>object</td>
        <td>
          appArmorProfile is the AppArmor options to use by this container. If set, this profile
overrides the pod's appArmorProfile.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainersecuritycontextcapabilities">capabilities</a></b></td>
        <td>object</td>
        <td>
          The capabilities to add/drop when running containers.
Defaults to the default set of capabilities granted by the container runtime.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>privileged</b></td>
        <td>boolean</td>
        <td>
          Run container in privileged mode.
Processes in privileged containers are essentially equivalent to root on the host.
Defaults to false.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>procMount</b></td>
        <td>string</td>
        <td>
          procMount denotes the type of proc mount to use for the containers.
The default value is Default which uses the container runtime defaults for
readonly paths and masked paths.
This requires the ProcMountType feature flag to be enabled.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>readOnlyRootFilesystem</b></td>
        <td>boolean</td>
        <td>
          Whether this container has a read-only root filesystem.
Default is false.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsGroup</b></td>
        <td>integer</td>
        <td>
          The GID to run the entrypoint of the container process.
Uses runtime default if unset.
May also be set in PodSecurityContext.  If set in both SecurityContext and
PodSecurityContext, the value specified in SecurityContext takes precedence.
Note that this field cannot be set when spec.os.name is windows.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsNonRoot</b></td>
        <td>boolean</td>
        <td>
          Indicates that the container must run as a non-root user.
If true, the Kubelet will validate the image at runtime to ensure that it
does not run as UID 0 (root) and fail to start the container if it does.
If unset or false, no such validation will be performed.
May also be set in PodSecurityContext.  If set in both SecurityContext and
PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsUser</b></td>
        <td>integer</td>
        <td>
          The UID to run the entrypoint of the container process.
Defaults to user specified in image metadata if unspecified.
May also be set in PodSecurityContext.  If set in both SecurityContext and
PodSecurityContext, the value specified in SecurityContext takes precedence.
Note that this field cannot be set when spec.os.name is windows.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainersecuritycontextselinuxoptions">seLinuxOptions</a></b></td>
        <td>object</td>
        <td>
          The SELinux context to be applied to the container.
If unspecified, the container runtime will allocate a random SELinux context for each
container.  May also be set in PodSecurityContext.  If set in both SecurityContext and
PodSecurityContext, the value specified in SecurityContext takes precedence.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainersecuritycontextseccompprofile">seccompProfile</a></b></td>
        <td>object</td>
        <td>
          The seccomp options to use by this container. If seccomp options are
provided at both the pod & container level, the container options
override the pod options.
Note that this field cannot be set when spec.os.name is windows.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainersecuritycontextwindowsoptions">windowsOptions</a></b></td>
        <td>object</td>
        <td>
          The Windows specific settings applied to all containers.
If unspecified, the options from the PodSecurityContext will be used.
If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
Note that this field cannot be set when spec.os.name is linux.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerSecurityContext.appArmorProfile
<sup><sup>[↩ Parent](#reaperspecinitcontainersecuritycontext)</sup></sup>



appArmorProfile is the AppArmor options to use by this container. If set, this profile
overrides the pod's appArmorProfile.
Note that this field cannot be set when spec.os.name is windows.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type indicates which kind of AppArmor profile will be applied.
Valid options are:
  Localhost - a profile pre-loaded on the node.
  RuntimeDefault - the container runtime's default profile.
  Unconfined - no AppArmor enforcement.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>localhostProfile</b></td>
        <td>string</td>
        <td>
          localhostProfile indicates a profile loaded on the node that should be used.
The profile must be preconfigured on the node to work.
Must match the loaded name of the profile.
Must be set if and only if type is "Localhost".<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.initContainerSecurityContext.capabilities
<sup><sup>[↩ Parent](#reaperspecinitcontainersecuritycontext)</sup></sup>



The capabilities to add/drop when running containers.
Defaults to the default set of capabilities granted by the container runtime.
Note that this field cannot be set when spec.os.name is windows.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>add</b></td>
        <td>[]string</td>
        <td>
          Added capabilities<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>drop</b></td>
        <td>[]string</td>
        <td>
          Removed capabilities<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
