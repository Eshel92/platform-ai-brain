<!-- Part 3 of 9 of reference/kubernetes-api/workload-resources/pod-v1.md (split because the page is big). -->

## Container {#Container}

A single application container that you want to run within a pod.

<hr>

- **name** (string), required

  Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.



### Image


- **image** (string)

  Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.

- **imagePullPolicy** (string)

  Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images

### Entrypoint


- **command** ([]string)

  *Atomic: will be replaced during a merge*
  
  Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

- **args** ([]string)

  *Atomic: will be replaced during a merge*
  
  Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

- **workingDir** (string)

  Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

### Ports


- **ports** ([]ContainerPort)

  *Patch strategy: merge on key `containerPort`*
  
  *Map: unique values on keys `containerPort, protocol` will be kept during a merge*
  
  List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated.

  <a name="ContainerPort"></a>
  *ContainerPort represents a network port in a single container.*

  - **ports.containerPort** (int32), required

    Number of port to expose on the pod's IP address. This must be a valid port number, 0 \< x \< 65536.

  - **ports.hostIP** (string)

    What host IP to bind the external port to.

  - **ports.hostPort** (int32)

    Number of port to expose on the host. If specified, this must be a valid port number, 0 \< x \< 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.

  - **ports.name** (string)

    If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.

  - **ports.protocol** (string)

    Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".

### Environment variables


- **env** ([]EnvVar)

  *Patch strategy: merge on key `name`*
  
  *Map: unique values on key name will be kept during a merge*
  
  List of environment variables to set in the container. Cannot be updated.

  <a name="EnvVar"></a>
  *EnvVar represents an environment variable present in a Container.*

  - **env.name** (string), required

    Name of the environment variable. Must be a C_IDENTIFIER.

  - **env.value** (string)

    Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".

  - **env.valueFrom** (EnvVarSource)

    Source for the environment variable's value. Cannot be used if value is not empty.

    <a name="EnvVarSource"></a>
    *EnvVarSource represents a source for the value of an EnvVar.*

    - **env.valueFrom.configMapKeyRef** (ConfigMapKeySelector)

      Selects a key of a ConfigMap.

      <a name="ConfigMapKeySelector"></a>
      *Selects a key from a ConfigMap.*

      - **env.valueFrom.configMapKeyRef.key** (string), required

        The key to select.

      - **env.valueFrom.configMapKeyRef.name** (string)

        Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

      - **env.valueFrom.configMapKeyRef.optional** (boolean)

        Specify whether the ConfigMap or its key must be defined

    - **env.valueFrom.fieldRef** (<a href="{{< ref "../common-definitions/object-field-selector#ObjectFieldSelector" >}}">ObjectFieldSelector</a>)

      Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['\<KEY>']`, `metadata.annotations['\<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

    - **env.valueFrom.resourceFieldRef** (<a href="{{< ref "../common-definitions/resource-field-selector#ResourceFieldSelector" >}}">ResourceFieldSelector</a>)

      Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

    - **env.valueFrom.secretKeyRef** (SecretKeySelector)

      Selects a key of a secret in the pod's namespace

      <a name="SecretKeySelector"></a>
      *SecretKeySelector selects a key of a Secret.*

      - **env.valueFrom.secretKeyRef.key** (string), required

        The key of the secret to select from.  Must be a valid secret key.

      - **env.valueFrom.secretKeyRef.name** (string)

        Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

      - **env.valueFrom.secretKeyRef.optional** (boolean)

        Specify whether the Secret or its key must be defined

- **envFrom** ([]EnvFromSource)

  *Atomic: will be replaced during a merge*
  
  List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

  <a name="EnvFromSource"></a>
  *EnvFromSource represents the source of a set of ConfigMaps or Secrets*

  - **envFrom.configMapRef** (ConfigMapEnvSource)

    The ConfigMap to select from

    <a name="ConfigMapEnvSource"></a>
    *ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.
    
    The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.*

    - **envFrom.configMapRef.name** (string)

      Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

    - **envFrom.configMapRef.optional** (boolean)

      Specify whether the ConfigMap must be defined

  - **envFrom.prefix** (string)

    Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER.

  - **envFrom.secretRef** (SecretEnvSource)

    The Secret to select from

    <a name="SecretEnvSource"></a>
    *SecretEnvSource selects a Secret to populate the environment variables with.
    
    The contents of the target Secret's Data field will represent the key-value pairs as environment variables.*

    - **envFrom.secretRef.name** (string)

      Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

    - **envFrom.secretRef.optional** (boolean)

      Specify whether the Secret must be defined

### Volumes


- **volumeMounts** ([]VolumeMount)

  *Patch strategy: merge on key `mountPath`*
  
  *Map: unique values on key mountPath will be kept during a merge*
  
  Pod volumes to mount into the container's filesystem. Cannot be updated.

  <a name="VolumeMount"></a>
  *VolumeMount describes a mounting of a Volume within a container.*

  - **volumeMounts.mountPath** (string), required

    Path within the container at which the volume should be mounted.  Must not contain ':'.

  - **volumeMounts.name** (string), required

    This must match the Name of a Volume.

  - **volumeMounts.mountPropagation** (string)

    mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).

  - **volumeMounts.readOnly** (boolean)

    Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.

  - **volumeMounts.recursiveReadOnly** (string)

    RecursiveReadOnly specifies whether read-only mounts should be handled recursively.
    
    If ReadOnly is false, this field has no meaning and must be unspecified.
    
    If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only.  If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.
    
    If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).
    
    If this field is not specified, it is treated as an equivalent of Disabled.

  - **volumeMounts.subPath** (string)

    Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).

  - **volumeMounts.subPathExpr** (string)

    Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.

- **volumeDevices** ([]VolumeDevice)

  *Patch strategy: merge on key `devicePath`*
  
  *Map: unique values on key devicePath will be kept during a merge*
  
  volumeDevices is the list of block devices to be used by the container.

  <a name="VolumeDevice"></a>
  *volumeDevice describes a mapping of a raw block device within a container.*

  - **volumeDevices.devicePath** (string), required

    devicePath is the path inside of the container that the device will be mapped to.

  - **volumeDevices.name** (string), required

    name must match the name of a persistentVolumeClaim in the pod

### Resources


- **resources** (ResourceRequirements)

  Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

  <a name="ResourceRequirements"></a>
  *ResourceRequirements describes the compute resource requirements.*

  - **resources.claims** ([]ResourceClaim)

    *Map: unique values on key name will be kept during a merge*
    
    Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.
    
    This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.
    
    This field is immutable. It can only be set for containers.

    <a name="ResourceClaim"></a>
    *ResourceClaim references one entry in PodSpec.ResourceClaims.*

    - **resources.claims.name** (string), required

      Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.

    - **resources.claims.request** (string)

      Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.

  - **resources.limits** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

    Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

  - **resources.requests** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

    Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

- **resizePolicy** ([]ContainerResizePolicy)

  *Atomic: will be replaced during a merge*
  
  Resources resize policy for the container.

  <a name="ContainerResizePolicy"></a>
  *ContainerResizePolicy represents resource resize policy for the container.*

  - **resizePolicy.resourceName** (string), required

    Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.

  - **resizePolicy.restartPolicy** (string), required

    Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.

### Lifecycle


- **lifecycle** (Lifecycle)

  Actions that the management system should take in response to container lifecycle events. Cannot be updated.

  <a name="Lifecycle"></a>
  *Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.*

  - **lifecycle.postStart** (<a href="{{< ref "../workload-resources/pod-v1#LifecycleHandler" >}}">LifecycleHandler</a>)

    PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

  - **lifecycle.preStop** (<a href="{{< ref "../workload-resources/pod-v1#LifecycleHandler" >}}">LifecycleHandler</a>)

    PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

  - **lifecycle.stopSignal** (string)

    StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name

- **terminationMessagePath** (string)

  Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.

- **terminationMessagePolicy** (string)

  Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.

- **livenessProbe** (<a href="{{< ref "../workload-resources/pod-v1#Probe" >}}">Probe</a>)

  Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

- **readinessProbe** (<a href="{{< ref "../workload-resources/pod-v1#Probe" >}}">Probe</a>)

  Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

- **startupProbe** (<a href="{{< ref "../workload-resources/pod-v1#Probe" >}}">Probe</a>)

  StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

- **restartPolicy** (string)

  RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.

### Security Context


- **securityContext** (SecurityContext)

  SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

  <a name="SecurityContext"></a>
  *SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence.*

  - **securityContext.allowPrivilegeEscalation** (boolean)

    AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.

  - **securityContext.appArmorProfile** (AppArmorProfile)

    appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod's appArmorProfile. Note that this field cannot be set when spec.os.name is windows.

    <a name="AppArmorProfile"></a>
    *AppArmorProfile defines a pod or container's AppArmor settings.*

    - **securityContext.appArmorProfile.type** (string), required

      type indicates which kind of AppArmor profile will be applied. Valid options are:
        Localhost - a profile pre-loaded on the node.
        RuntimeDefault - the container runtime's default profile.
        Unconfined - no AppArmor enforcement.

    - **securityContext.appArmorProfile.localhostProfile** (string)

      localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".

  - **securityContext.capabilities** (Capabilities)

    The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.

    <a name="Capabilities"></a>
    *Adds and removes POSIX capabilities from running containers.*

    - **securityContext.capabilities.add** ([]string)

      *Atomic: will be replaced during a merge*
      
      Added capabilities

    - **securityContext.capabilities.drop** ([]string)

      *Atomic: will be replaced during a merge*
      
      Removed capabilities

  - **securityContext.procMount** (string)

    procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.

  - **securityContext.privileged** (boolean)

    Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.

  - **securityContext.readOnlyRootFilesystem** (boolean)

    Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.

  - **securityContext.runAsUser** (int64)

    The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

  - **securityContext.runAsNonRoot** (boolean)

    Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

  - **securityContext.runAsGroup** (int64)

    The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

  - **securityContext.seLinuxOptions** (SELinuxOptions)

    The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

    <a name="SELinuxOptions"></a>
    *SELinuxOptions are the labels to be applied to the container*

    - **securityContext.seLinuxOptions.level** (string)

      Level is SELinux level label that applies to the container.

    - **securityContext.seLinuxOptions.role** (string)

      Role is a SELinux role label that applies to the container.

    - **securityContext.seLinuxOptions.type** (string)

      Type is a SELinux type label that applies to the container.

    - **securityContext.seLinuxOptions.user** (string)

      User is a SELinux user label that applies to the container.

  - **securityContext.seccompProfile** (SeccompProfile)

    The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.

    <a name="SeccompProfile"></a>
    *SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set.*

    - **securityContext.seccompProfile.type** (string), required

      type indicates which kind of seccomp profile will be applied. Valid options are:
      
      Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.

    - **securityContext.seccompProfile.localhostProfile** (string)

      localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.

  - **securityContext.windowsOptions** (WindowsSecurityContextOptions)

    The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

    <a name="WindowsSecurityContextOptions"></a>
    *WindowsSecurityContextOptions contain Windows-specific options and credentials.*

    - **securityContext.windowsOptions.gmsaCredentialSpec** (string)

      GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.

    - **securityContext.windowsOptions.gmsaCredentialSpecName** (string)

      GMSACredentialSpecName is the name of the GMSA credential spec to use.

    - **securityContext.windowsOptions.hostProcess** (boolean)

      HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.

    - **securityContext.windowsOptions.runAsUserName** (string)

      The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

### Debugging


- **stdin** (boolean)

  Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.

- **stdinOnce** (boolean)

  Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false

- **tty** (boolean)

  Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
