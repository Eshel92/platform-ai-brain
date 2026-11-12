<!-- Part 7 of 9 of reference/kubernetes-api/workload-resources/pod-v1.md (split because the page is big). -->

## PodStatus {#PodStatus}

PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane.

<hr>

- **nominatedNodeName** (string)

  nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.

- **hostIP** (string)

  hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod

- **hostIPs** ([]HostIP)

  *Patch strategy: merge on key `ip`*
  
  *Atomic: will be replaced during a merge*
  
  hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod.

  <a name="HostIP"></a>
  *HostIP represents a single IP address allocated to the host.*

  - **hostIPs.ip** (string), required

    IP is the IP address assigned to the host

- **startTime** (Time)

  RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.

  <a name="Time"></a>
  *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

- **phase** (string)

  The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:
  
  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.
  
  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase

- **message** (string)

  A human readable message indicating details about why the pod is in this condition.

- **reason** (string)

  A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'

- **podIP** (string)

  podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.

- **podIPs** ([]PodIP)

  *Patch strategy: merge on key `ip`*
  
  *Map: unique values on key ip will be kept during a merge*
  
  podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.

  <a name="PodIP"></a>
  *PodIP represents a single IP address allocated to the pod.*

  - **podIPs.ip** (string), required

    IP is the IP address assigned to the pod

- **conditions** ([]PodCondition)

  *Patch strategy: merge on key `type`*
  
  *Map: unique values on key type will be kept during a merge*
  
  Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

  <a name="PodCondition"></a>
  *PodCondition contains details for the current condition of this pod.*

  - **conditions.status** (string), required

    Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

  - **conditions.type** (string), required

    Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

  - **conditions.lastProbeTime** (Time)

    Last time we probed the condition.

    <a name="Time"></a>
    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

  - **conditions.lastTransitionTime** (Time)

    Last time the condition transitioned from one status to another.

    <a name="Time"></a>
    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

  - **conditions.message** (string)

    Human-readable message indicating details about last transition.

  - **conditions.observedGeneration** (int64)

    If set, this represents the .metadata.generation that the pod condition was set based upon. This is an alpha field. Enable PodObservedGenerationTracking to be able to use this field.

  - **conditions.reason** (string)

    Unique, one-word, CamelCase reason for the condition's last transition.

- **qosClass** (string)

  The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes

- **initContainerStatuses** ([]ContainerStatus)

  *Atomic: will be replaced during a merge*
  
  Statuses of init containers in this pod. The most recent successful non-restartable init container will have ready = true, the most recently started container will have startTime set. Each init container in the pod should have at most one status in this list, and all statuses should be for containers in the pod. However this is not enforced. If a status for a non-existent container is present in the list, or the list has duplicate names, the behavior of various Kubernetes components is not defined and those statuses might be ignored. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-and-container-status

  <a name="ContainerStatus"></a>
  *ContainerStatus contains details for the current status of this container.*

  - **initContainerStatuses.allocatedResources** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

    AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.

  - **initContainerStatuses.allocatedResourcesStatus** ([]ResourceStatus)

    *Patch strategy: merge on key `name`*
    
    *Map: unique values on key name will be kept during a merge*
    
    AllocatedResourcesStatus represents the status of various resources allocated for this Pod.

    <a name="ResourceStatus"></a>
    *ResourceStatus represents the status of a single resource allocated to a Pod.*

    - **initContainerStatuses.allocatedResourcesStatus.name** (string), required

      Name of the resource. Must be unique within the pod and in case of non-DRA resource, match one of the resources from the pod spec. For DRA resources, the value must be "claim:\<claim_name>/\<request>". When this status is reported about a container, the "claim_name" and "request" must match one of the claims of this container.

    - **initContainerStatuses.allocatedResourcesStatus.resources** ([]ResourceHealth)

      *Map: unique values on key resourceID will be kept during a merge*
      
      List of unique resources health. Each element in the list contains an unique resource ID and its health. At a minimum, for the lifetime of a Pod, resource ID must uniquely identify the resource allocated to the Pod on the Node. If other Pod on the same Node reports the status with the same resource ID, it must be the same resource they share. See ResourceID type definition for a specific format it has in various use cases.

      <a name="ResourceHealth"></a>
      *ResourceHealth represents the health of a resource. It has the latest device health information. This is a part of KEP https://kep.k8s.io/4680.*

      - **initContainerStatuses.allocatedResourcesStatus.resources.resourceID** (string), required

        ResourceID is the unique identifier of the resource. See the ResourceID type for more information.

      - **initContainerStatuses.allocatedResourcesStatus.resources.health** (string)

        Health of the resource. can be one of:
         - Healthy: operates as normal
         - Unhealthy: reported unhealthy. We consider this a temporary health issue
                      since we do not have a mechanism today to distinguish
                      temporary and permanent issues.
         - Unknown: The status cannot be determined.
                    For example, Device Plugin got unregistered and hasn't been re-registered since.
        
        In future we may want to introduce the PermanentlyUnhealthy Status.

  - **initContainerStatuses.containerID** (string)

    ContainerID is the ID of the container in the format '\<type>://\<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd").

  - **initContainerStatuses.image** (string), required

    Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.

  - **initContainerStatuses.imageID** (string), required

    ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.

  - **initContainerStatuses.lastState** (ContainerState)

    LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0.

    <a name="ContainerState"></a>
    *ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.*

    - **initContainerStatuses.lastState.running** (ContainerStateRunning)

      Details about a running container

      <a name="ContainerStateRunning"></a>
      *ContainerStateRunning is a running state of a container.*

      - **initContainerStatuses.lastState.running.startedAt** (Time)

        Time at which the container was last (re-)started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **initContainerStatuses.lastState.terminated** (ContainerStateTerminated)

      Details about a terminated container

      <a name="ContainerStateTerminated"></a>
      *ContainerStateTerminated is a terminated state of a container.*

      - **initContainerStatuses.lastState.terminated.containerID** (string)

        Container's ID in the format '\<type>://\<container_id>'

      - **initContainerStatuses.lastState.terminated.exitCode** (int32), required

        Exit status from the last termination of the container

      - **initContainerStatuses.lastState.terminated.startedAt** (Time)

        Time at which previous execution of the container started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **initContainerStatuses.lastState.terminated.finishedAt** (Time)

        Time at which the container last terminated

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **initContainerStatuses.lastState.terminated.message** (string)

        Message regarding the last termination of the container

      - **initContainerStatuses.lastState.terminated.reason** (string)

        (brief) reason from the last termination of the container

      - **initContainerStatuses.lastState.terminated.signal** (int32)

        Signal from the last termination of the container

    - **initContainerStatuses.lastState.waiting** (ContainerStateWaiting)

      Details about a waiting container

      <a name="ContainerStateWaiting"></a>
      *ContainerStateWaiting is a waiting state of a container.*

      - **initContainerStatuses.lastState.waiting.message** (string)

        Message regarding why the container is not yet running.

      - **initContainerStatuses.lastState.waiting.reason** (string)

        (brief) reason the container is not yet running.

  - **initContainerStatuses.name** (string), required

    Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.

  - **initContainerStatuses.ready** (boolean), required

    Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).
    
    The value is typically used to determine whether a container is ready to accept traffic.

  - **initContainerStatuses.resources** (ResourceRequirements)

    Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized.

    <a name="ResourceRequirements"></a>
    *ResourceRequirements describes the compute resource requirements.*

    - **initContainerStatuses.resources.claims** ([]ResourceClaim)

      *Map: unique values on key name will be kept during a merge*
      
      Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.
      
      This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.
      
      This field is immutable. It can only be set for containers.

      <a name="ResourceClaim"></a>
      *ResourceClaim references one entry in PodSpec.ResourceClaims.*

      - **initContainerStatuses.resources.claims.name** (string), required

        Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.

      - **initContainerStatuses.resources.claims.request** (string)

        Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.

    - **initContainerStatuses.resources.limits** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

      Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

    - **initContainerStatuses.resources.requests** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

      Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

  - **initContainerStatuses.restartCount** (int32), required

    RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.

  - **initContainerStatuses.started** (boolean)

    Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.

  - **initContainerStatuses.state** (ContainerState)

    State holds details about the container's current condition.

    <a name="ContainerState"></a>
    *ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.*

    - **initContainerStatuses.state.running** (ContainerStateRunning)

      Details about a running container

      <a name="ContainerStateRunning"></a>
      *ContainerStateRunning is a running state of a container.*

      - **initContainerStatuses.state.running.startedAt** (Time)

        Time at which the container was last (re-)started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **initContainerStatuses.state.terminated** (ContainerStateTerminated)

      Details about a terminated container

      <a name="ContainerStateTerminated"></a>
      *ContainerStateTerminated is a terminated state of a container.*

      - **initContainerStatuses.state.terminated.containerID** (string)

        Container's ID in the format '\<type>://\<container_id>'

      - **initContainerStatuses.state.terminated.exitCode** (int32), required

        Exit status from the last termination of the container

      - **initContainerStatuses.state.terminated.startedAt** (Time)

        Time at which previous execution of the container started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **initContainerStatuses.state.terminated.finishedAt** (Time)

        Time at which the container last terminated

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **initContainerStatuses.state.terminated.message** (string)

        Message regarding the last termination of the container

      - **initContainerStatuses.state.terminated.reason** (string)

        (brief) reason from the last termination of the container

      - **initContainerStatuses.state.terminated.signal** (int32)

        Signal from the last termination of the container

    - **initContainerStatuses.state.waiting** (ContainerStateWaiting)

      Details about a waiting container

      <a name="ContainerStateWaiting"></a>
      *ContainerStateWaiting is a waiting state of a container.*

      - **initContainerStatuses.state.waiting.message** (string)

        Message regarding why the container is not yet running.

      - **initContainerStatuses.state.waiting.reason** (string)

        (brief) reason the container is not yet running.

  - **initContainerStatuses.stopSignal** (string)

    StopSignal reports the effective stop signal for this container

  - **initContainerStatuses.user** (ContainerUser)

    User represents user identity information initially attached to the first process of the container

    <a name="ContainerUser"></a>
    *ContainerUser represents user identity information*

    - **initContainerStatuses.user.linux** (LinuxContainerUser)

      Linux holds user identity information initially attached to the first process of the containers in Linux. Note that the actual running identity can be changed if the process has enough privilege to do so.

      <a name="LinuxContainerUser"></a>
      *LinuxContainerUser represents user identity information in Linux containers*

      - **initContainerStatuses.user.linux.gid** (int64), required

        GID is the primary gid initially attached to the first process in the container

      - **initContainerStatuses.user.linux.uid** (int64), required

        UID is the primary uid initially attached to the first process in the container

      - **initContainerStatuses.user.linux.supplementalGroups** ([]int64)

        *Atomic: will be replaced during a merge*
        
        SupplementalGroups are the supplemental groups initially attached to the first process in the container

  - **initContainerStatuses.volumeMounts** ([]VolumeMountStatus)

    *Patch strategy: merge on key `mountPath`*
    
    *Map: unique values on key mountPath will be kept during a merge*
    
    Status of volume mounts.

    <a name="VolumeMountStatus"></a>
    *VolumeMountStatus shows status of volume mounts.*

    - **initContainerStatuses.volumeMounts.mountPath** (string), required

      MountPath corresponds to the original VolumeMount.

    - **initContainerStatuses.volumeMounts.name** (string), required

      Name corresponds to the name of the original VolumeMount.

    - **initContainerStatuses.volumeMounts.readOnly** (boolean)

      ReadOnly corresponds to the original VolumeMount.

    - **initContainerStatuses.volumeMounts.recursiveReadOnly** (string)

      RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result.

- **containerStatuses** ([]ContainerStatus)

  *Atomic: will be replaced during a merge*
  
  Statuses of containers in this pod. Each container in the pod should have at most one status in this list, and all statuses should be for containers in the pod. However this is not enforced. If a status for a non-existent container is present in the list, or the list has duplicate names, the behavior of various Kubernetes components is not defined and those statuses might be ignored. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

  <a name="ContainerStatus"></a>
  *ContainerStatus contains details for the current status of this container.*

  - **containerStatuses.allocatedResources** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

    AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.

  - **containerStatuses.allocatedResourcesStatus** ([]ResourceStatus)

    *Patch strategy: merge on key `name`*
    
    *Map: unique values on key name will be kept during a merge*
    
    AllocatedResourcesStatus represents the status of various resources allocated for this Pod.

    <a name="ResourceStatus"></a>
    *ResourceStatus represents the status of a single resource allocated to a Pod.*

    - **containerStatuses.allocatedResourcesStatus.name** (string), required

      Name of the resource. Must be unique within the pod and in case of non-DRA resource, match one of the resources from the pod spec. For DRA resources, the value must be "claim:\<claim_name>/\<request>". When this status is reported about a container, the "claim_name" and "request" must match one of the claims of this container.

    - **containerStatuses.allocatedResourcesStatus.resources** ([]ResourceHealth)

      *Map: unique values on key resourceID will be kept during a merge*
      
      List of unique resources health. Each element in the list contains an unique resource ID and its health. At a minimum, for the lifetime of a Pod, resource ID must uniquely identify the resource allocated to the Pod on the Node. If other Pod on the same Node reports the status with the same resource ID, it must be the same resource they share. See ResourceID type definition for a specific format it has in various use cases.

      <a name="ResourceHealth"></a>
      *ResourceHealth represents the health of a resource. It has the latest device health information. This is a part of KEP https://kep.k8s.io/4680.*

      - **containerStatuses.allocatedResourcesStatus.resources.resourceID** (string), required

        ResourceID is the unique identifier of the resource. See the ResourceID type for more information.

      - **containerStatuses.allocatedResourcesStatus.resources.health** (string)

        Health of the resource. can be one of:
         - Healthy: operates as normal
         - Unhealthy: reported unhealthy. We consider this a temporary health issue
                      since we do not have a mechanism today to distinguish
                      temporary and permanent issues.
         - Unknown: The status cannot be determined.
                    For example, Device Plugin got unregistered and hasn't been re-registered since.
        
        In future we may want to introduce the PermanentlyUnhealthy Status.

  - **containerStatuses.containerID** (string)

    ContainerID is the ID of the container in the format '\<type>://\<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd").

  - **containerStatuses.image** (string), required

    Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.

  - **containerStatuses.imageID** (string), required

    ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.

  - **containerStatuses.lastState** (ContainerState)

    LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0.

    <a name="ContainerState"></a>
    *ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.*

    - **containerStatuses.lastState.running** (ContainerStateRunning)

      Details about a running container

      <a name="ContainerStateRunning"></a>
      *ContainerStateRunning is a running state of a container.*

      - **containerStatuses.lastState.running.startedAt** (Time)

        Time at which the container was last (re-)started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **containerStatuses.lastState.terminated** (ContainerStateTerminated)

      Details about a terminated container

      <a name="ContainerStateTerminated"></a>
      *ContainerStateTerminated is a terminated state of a container.*

      - **containerStatuses.lastState.terminated.containerID** (string)

        Container's ID in the format '\<type>://\<container_id>'

      - **containerStatuses.lastState.terminated.exitCode** (int32), required

        Exit status from the last termination of the container

      - **containerStatuses.lastState.terminated.startedAt** (Time)

        Time at which previous execution of the container started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **containerStatuses.lastState.terminated.finishedAt** (Time)

        Time at which the container last terminated

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **containerStatuses.lastState.terminated.message** (string)

        Message regarding the last termination of the container

      - **containerStatuses.lastState.terminated.reason** (string)

        (brief) reason from the last termination of the container

      - **containerStatuses.lastState.terminated.signal** (int32)

        Signal from the last termination of the container

    - **containerStatuses.lastState.waiting** (ContainerStateWaiting)

      Details about a waiting container

      <a name="ContainerStateWaiting"></a>
      *ContainerStateWaiting is a waiting state of a container.*

      - **containerStatuses.lastState.waiting.message** (string)

        Message regarding why the container is not yet running.

      - **containerStatuses.lastState.waiting.reason** (string)

        (brief) reason the container is not yet running.

  - **containerStatuses.name** (string), required

    Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.

  - **containerStatuses.ready** (boolean), required

    Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).
    
    The value is typically used to determine whether a container is ready to accept traffic.

  - **containerStatuses.resources** (ResourceRequirements)

    Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized.

    <a name="ResourceRequirements"></a>
    *ResourceRequirements describes the compute resource requirements.*

    - **containerStatuses.resources.claims** ([]ResourceClaim)

      *Map: unique values on key name will be kept during a merge*
      
      Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.
      
      This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.
      
      This field is immutable. It can only be set for containers.

      <a name="ResourceClaim"></a>
      *ResourceClaim references one entry in PodSpec.ResourceClaims.*

      - **containerStatuses.resources.claims.name** (string), required

        Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.

      - **containerStatuses.resources.claims.request** (string)

        Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.

    - **containerStatuses.resources.limits** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

      Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

    - **containerStatuses.resources.requests** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

      Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

  - **containerStatuses.restartCount** (int32), required

    RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.

  - **containerStatuses.started** (boolean)

    Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.

  - **containerStatuses.state** (ContainerState)

    State holds details about the container's current condition.

    <a name="ContainerState"></a>
    *ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.*

    - **containerStatuses.state.running** (ContainerStateRunning)

      Details about a running container

      <a name="ContainerStateRunning"></a>
      *ContainerStateRunning is a running state of a container.*

      - **containerStatuses.state.running.startedAt** (Time)

        Time at which the container was last (re-)started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **containerStatuses.state.terminated** (ContainerStateTerminated)

      Details about a terminated container

      <a name="ContainerStateTerminated"></a>
      *ContainerStateTerminated is a terminated state of a container.*

      - **containerStatuses.state.terminated.containerID** (string)

        Container's ID in the format '\<type>://\<container_id>'

      - **containerStatuses.state.terminated.exitCode** (int32), required

        Exit status from the last termination of the container

      - **containerStatuses.state.terminated.startedAt** (Time)

        Time at which previous execution of the container started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **containerStatuses.state.terminated.finishedAt** (Time)

        Time at which the container last terminated

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **containerStatuses.state.terminated.message** (string)

        Message regarding the last termination of the container

      - **containerStatuses.state.terminated.reason** (string)

        (brief) reason from the last termination of the container

      - **containerStatuses.state.terminated.signal** (int32)

        Signal from the last termination of the container

    - **containerStatuses.state.waiting** (ContainerStateWaiting)

      Details about a waiting container

      <a name="ContainerStateWaiting"></a>
      *ContainerStateWaiting is a waiting state of a container.*

      - **containerStatuses.state.waiting.message** (string)

        Message regarding why the container is not yet running.

      - **containerStatuses.state.waiting.reason** (string)

        (brief) reason the container is not yet running.

  - **containerStatuses.stopSignal** (string)

    StopSignal reports the effective stop signal for this container

  - **containerStatuses.user** (ContainerUser)

    User represents user identity information initially attached to the first process of the container

    <a name="ContainerUser"></a>
    *ContainerUser represents user identity information*

    - **containerStatuses.user.linux** (LinuxContainerUser)

      Linux holds user identity information initially attached to the first process of the containers in Linux. Note that the actual running identity can be changed if the process has enough privilege to do so.

      <a name="LinuxContainerUser"></a>
      *LinuxContainerUser represents user identity information in Linux containers*

      - **containerStatuses.user.linux.gid** (int64), required

        GID is the primary gid initially attached to the first process in the container

      - **containerStatuses.user.linux.uid** (int64), required

        UID is the primary uid initially attached to the first process in the container

      - **containerStatuses.user.linux.supplementalGroups** ([]int64)

        *Atomic: will be replaced during a merge*
        
        SupplementalGroups are the supplemental groups initially attached to the first process in the container

  - **containerStatuses.volumeMounts** ([]VolumeMountStatus)

    *Patch strategy: merge on key `mountPath`*
    
    *Map: unique values on key mountPath will be kept during a merge*
    
    Status of volume mounts.

    <a name="VolumeMountStatus"></a>
    *VolumeMountStatus shows status of volume mounts.*

    - **containerStatuses.volumeMounts.mountPath** (string), required

      MountPath corresponds to the original VolumeMount.

    - **containerStatuses.volumeMounts.name** (string), required

      Name corresponds to the name of the original VolumeMount.

    - **containerStatuses.volumeMounts.readOnly** (boolean)

      ReadOnly corresponds to the original VolumeMount.

    - **containerStatuses.volumeMounts.recursiveReadOnly** (string)

      RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result.

- **ephemeralContainerStatuses** ([]ContainerStatus)

  *Atomic: will be replaced during a merge*
  
  Statuses for any ephemeral containers that have run in this pod. Each ephemeral container in the pod should have at most one status in this list, and all statuses should be for containers in the pod. However this is not enforced. If a status for a non-existent container is present in the list, or the list has duplicate names, the behavior of various Kubernetes components is not defined and those statuses might be ignored. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

  <a name="ContainerStatus"></a>
  *ContainerStatus contains details for the current status of this container.*

  - **ephemeralContainerStatuses.allocatedResources** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

    AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.

  - **ephemeralContainerStatuses.allocatedResourcesStatus** ([]ResourceStatus)

    *Patch strategy: merge on key `name`*
    
    *Map: unique values on key name will be kept during a merge*
    
    AllocatedResourcesStatus represents the status of various resources allocated for this Pod.

    <a name="ResourceStatus"></a>
    *ResourceStatus represents the status of a single resource allocated to a Pod.*

    - **ephemeralContainerStatuses.allocatedResourcesStatus.name** (string), required

      Name of the resource. Must be unique within the pod and in case of non-DRA resource, match one of the resources from the pod spec. For DRA resources, the value must be "claim:\<claim_name>/\<request>". When this status is reported about a container, the "claim_name" and "request" must match one of the claims of this container.

    - **ephemeralContainerStatuses.allocatedResourcesStatus.resources** ([]ResourceHealth)

      *Map: unique values on key resourceID will be kept during a merge*
      
      List of unique resources health. Each element in the list contains an unique resource ID and its health. At a minimum, for the lifetime of a Pod, resource ID must uniquely identify the resource allocated to the Pod on the Node. If other Pod on the same Node reports the status with the same resource ID, it must be the same resource they share. See ResourceID type definition for a specific format it has in various use cases.

      <a name="ResourceHealth"></a>
      *ResourceHealth represents the health of a resource. It has the latest device health information. This is a part of KEP https://kep.k8s.io/4680.*

      - **ephemeralContainerStatuses.allocatedResourcesStatus.resources.resourceID** (string), required

        ResourceID is the unique identifier of the resource. See the ResourceID type for more information.

      - **ephemeralContainerStatuses.allocatedResourcesStatus.resources.health** (string)

        Health of the resource. can be one of:
         - Healthy: operates as normal
         - Unhealthy: reported unhealthy. We consider this a temporary health issue
                      since we do not have a mechanism today to distinguish
                      temporary and permanent issues.
         - Unknown: The status cannot be determined.
                    For example, Device Plugin got unregistered and hasn't been re-registered since.
        
        In future we may want to introduce the PermanentlyUnhealthy Status.

  - **ephemeralContainerStatuses.containerID** (string)

    ContainerID is the ID of the container in the format '\<type>://\<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd").

  - **ephemeralContainerStatuses.image** (string), required

    Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.

  - **ephemeralContainerStatuses.imageID** (string), required

    ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.

  - **ephemeralContainerStatuses.lastState** (ContainerState)

    LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0.

    <a name="ContainerState"></a>
    *ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.*

    - **ephemeralContainerStatuses.lastState.running** (ContainerStateRunning)

      Details about a running container

      <a name="ContainerStateRunning"></a>
      *ContainerStateRunning is a running state of a container.*

      - **ephemeralContainerStatuses.lastState.running.startedAt** (Time)

        Time at which the container was last (re-)started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **ephemeralContainerStatuses.lastState.terminated** (ContainerStateTerminated)

      Details about a terminated container

      <a name="ContainerStateTerminated"></a>
      *ContainerStateTerminated is a terminated state of a container.*

      - **ephemeralContainerStatuses.lastState.terminated.containerID** (string)

        Container's ID in the format '\<type>://\<container_id>'

      - **ephemeralContainerStatuses.lastState.terminated.exitCode** (int32), required

        Exit status from the last termination of the container

      - **ephemeralContainerStatuses.lastState.terminated.startedAt** (Time)

        Time at which previous execution of the container started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **ephemeralContainerStatuses.lastState.terminated.finishedAt** (Time)

        Time at which the container last terminated

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **ephemeralContainerStatuses.lastState.terminated.message** (string)

        Message regarding the last termination of the container

      - **ephemeralContainerStatuses.lastState.terminated.reason** (string)

        (brief) reason from the last termination of the container

      - **ephemeralContainerStatuses.lastState.terminated.signal** (int32)

        Signal from the last termination of the container

    - **ephemeralContainerStatuses.lastState.waiting** (ContainerStateWaiting)

      Details about a waiting container

      <a name="ContainerStateWaiting"></a>
      *ContainerStateWaiting is a waiting state of a container.*

      - **ephemeralContainerStatuses.lastState.waiting.message** (string)

        Message regarding why the container is not yet running.

      - **ephemeralContainerStatuses.lastState.waiting.reason** (string)

        (brief) reason the container is not yet running.

  - **ephemeralContainerStatuses.name** (string), required

    Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.

  - **ephemeralContainerStatuses.ready** (boolean), required

    Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).
    
    The value is typically used to determine whether a container is ready to accept traffic.

  - **ephemeralContainerStatuses.resources** (ResourceRequirements)

    Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized.

    <a name="ResourceRequirements"></a>
    *ResourceRequirements describes the compute resource requirements.*

    - **ephemeralContainerStatuses.resources.claims** ([]ResourceClaim)

      *Map: unique values on key name will be kept during a merge*
      
      Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.
      
      This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.
      
      This field is immutable. It can only be set for containers.

      <a name="ResourceClaim"></a>
      *ResourceClaim references one entry in PodSpec.ResourceClaims.*

      - **ephemeralContainerStatuses.resources.claims.name** (string), required

        Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.

      - **ephemeralContainerStatuses.resources.claims.request** (string)

        Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.

    - **ephemeralContainerStatuses.resources.limits** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

      Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

    - **ephemeralContainerStatuses.resources.requests** (map[string]<a href="{{< ref "../common-definitions/quantity#Quantity" >}}">Quantity</a>)

      Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

  - **ephemeralContainerStatuses.restartCount** (int32), required

    RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.

  - **ephemeralContainerStatuses.started** (boolean)

    Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.

  - **ephemeralContainerStatuses.state** (ContainerState)

    State holds details about the container's current condition.

    <a name="ContainerState"></a>
    *ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.*

    - **ephemeralContainerStatuses.state.running** (ContainerStateRunning)

      Details about a running container

      <a name="ContainerStateRunning"></a>
      *ContainerStateRunning is a running state of a container.*

      - **ephemeralContainerStatuses.state.running.startedAt** (Time)

        Time at which the container was last (re-)started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **ephemeralContainerStatuses.state.terminated** (ContainerStateTerminated)

      Details about a terminated container

      <a name="ContainerStateTerminated"></a>
      *ContainerStateTerminated is a terminated state of a container.*

      - **ephemeralContainerStatuses.state.terminated.containerID** (string)

        Container's ID in the format '\<type>://\<container_id>'

      - **ephemeralContainerStatuses.state.terminated.exitCode** (int32), required

        Exit status from the last termination of the container

      - **ephemeralContainerStatuses.state.terminated.startedAt** (Time)

        Time at which previous execution of the container started

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **ephemeralContainerStatuses.state.terminated.finishedAt** (Time)

        Time at which the container last terminated

        <a name="Time"></a>
        *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

      - **ephemeralContainerStatuses.state.terminated.message** (string)

        Message regarding the last termination of the container

      - **ephemeralContainerStatuses.state.terminated.reason** (string)

        (brief) reason from the last termination of the container

      - **ephemeralContainerStatuses.state.terminated.signal** (int32)

        Signal from the last termination of the container

    - **ephemeralContainerStatuses.state.waiting** (ContainerStateWaiting)

      Details about a waiting container

      <a name="ContainerStateWaiting"></a>
      *ContainerStateWaiting is a waiting state of a container.*

      - **ephemeralContainerStatuses.state.waiting.message** (string)

        Message regarding why the container is not yet running.

      - **ephemeralContainerStatuses.state.waiting.reason** (string)

        (brief) reason the container is not yet running.

  - **ephemeralContainerStatuses.stopSignal** (string)

    StopSignal reports the effective stop signal for this container

  - **ephemeralContainerStatuses.user** (ContainerUser)

    User represents user identity information initially attached to the first process of the container

    <a name="ContainerUser"></a>
    *ContainerUser represents user identity information*

    - **ephemeralContainerStatuses.user.linux** (LinuxContainerUser)

      Linux holds user identity information initially attached to the first process of the containers in Linux. Note that the actual running identity can be changed if the process has enough privilege to do so.

      <a name="LinuxContainerUser"></a>
      *LinuxContainerUser represents user identity information in Linux containers*

      - **ephemeralContainerStatuses.user.linux.gid** (int64), required

        GID is the primary gid initially attached to the first process in the container

      - **ephemeralContainerStatuses.user.linux.uid** (int64), required

        UID is the primary uid initially attached to the first process in the container

      - **ephemeralContainerStatuses.user.linux.supplementalGroups** ([]int64)

        *Atomic: will be replaced during a merge*
        
        SupplementalGroups are the supplemental groups initially attached to the first process in the container

  - **ephemeralContainerStatuses.volumeMounts** ([]VolumeMountStatus)

    *Patch strategy: merge on key `mountPath`*
    
    *Map: unique values on key mountPath will be kept during a merge*
    
    Status of volume mounts.

    <a name="VolumeMountStatus"></a>
    *VolumeMountStatus shows status of volume mounts.*

    - **ephemeralContainerStatuses.volumeMounts.mountPath** (string), required

      MountPath corresponds to the original VolumeMount.

    - **ephemeralContainerStatuses.volumeMounts.name** (string), required

      Name corresponds to the name of the original VolumeMount.

    - **ephemeralContainerStatuses.volumeMounts.readOnly** (boolean)

      ReadOnly corresponds to the original VolumeMount.

    - **ephemeralContainerStatuses.volumeMounts.recursiveReadOnly** (string)

      RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result.

- **resourceClaimStatuses** ([]PodResourceClaimStatus)

  *Patch strategies: retainKeys, merge on key `name`*
  
  *Map: unique values on key name will be kept during a merge*
  
  Status of resource claims.

  <a name="PodResourceClaimStatus"></a>
  *PodResourceClaimStatus is stored in the PodStatus for each PodResourceClaim which references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim.*

  - **resourceClaimStatuses.name** (string), required

    Name uniquely identifies this resource claim inside the pod. This must match the name of an entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL.

  - **resourceClaimStatuses.resourceClaimName** (string)

    ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. If this is unset, then generating a ResourceClaim was not necessary. The pod.spec.resourceClaims entry can be ignored in this case.

- **resize** (string)

  Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to "Proposed" Deprecated: Resize status is moved to two pod conditions PodResizePending and PodResizeInProgress. PodResizePending will track states where the spec has been resized, but the Kubelet has not yet allocated the resources. PodResizeInProgress will track in-progress resizes, and should be present whenever allocated resources != acknowledged resources.

- **observedGeneration** (int64)

  If set, this represents the .metadata.generation that the pod status was set based upon. This is an alpha field. Enable PodObservedGenerationTracking to be able to use this field.
