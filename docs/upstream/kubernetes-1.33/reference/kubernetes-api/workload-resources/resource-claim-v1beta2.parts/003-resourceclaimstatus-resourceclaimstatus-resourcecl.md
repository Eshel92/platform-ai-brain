<!-- Part 3 of 4 of reference/kubernetes-api/workload-resources/resource-claim-v1beta2.md (split because the page is big). -->

## ResourceClaimStatus {#ResourceClaimStatus}

ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was.

<hr>

- **allocation** (AllocationResult)

  Allocation is set once the claim has been allocated successfully.

  <a name="AllocationResult"></a>
  *AllocationResult contains attributes of an allocated resource.*

  - **allocation.devices** (DeviceAllocationResult)

    Devices is the result of allocating devices.

    <a name="DeviceAllocationResult"></a>
    *DeviceAllocationResult is the result of allocating devices.*

    - **allocation.devices.config** ([]DeviceAllocationConfiguration)

      *Atomic: will be replaced during a merge*
      
      This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.
      
      This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.

      <a name="DeviceAllocationConfiguration"></a>
      *DeviceAllocationConfiguration gets embedded in an AllocationResult.*

      - **allocation.devices.config.source** (string), required

        Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim.

      - **allocation.devices.config.opaque** (OpaqueDeviceConfiguration)

        Opaque provides driver-specific configuration parameters.

        <a name="OpaqueDeviceConfiguration"></a>
        *OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.*

        - **allocation.devices.config.opaque.driver** (string), required

          Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.
          
          An admission policy provided by the driver developer could use this to decide whether it needs to validate them.
          
          Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.

        - **allocation.devices.config.opaque.parameters** (RawExtension), required

          Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.
          
          The length of the raw data must be smaller or equal to 10 Ki.

          <a name="RawExtension"></a>
          *RawExtension is used to hold extensions in external versions.
          
          To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.
          
          // Internal package:
          
          	type MyAPIObject struct {
          		runtime.TypeMeta `json:",inline"`
          		MyPlugin runtime.Object `json:"myPlugin"`
          	}
          
          	type PluginA struct {
          		AOption string `json:"aOption"`
          	}
          
          // External package:
          
          	type MyAPIObject struct {
          		runtime.TypeMeta `json:",inline"`
          		MyPlugin runtime.RawExtension `json:"myPlugin"`
          	}
          
          	type PluginA struct {
          		AOption string `json:"aOption"`
          	}
          
          // On the wire, the JSON will look something like this:
          
          	{
          		"kind":"MyAPIObject",
          		"apiVersion":"v1",
          		"myPlugin": {
          			"kind":"PluginA",
          			"aOption":"foo",
          		},
          	}
          
          So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package's DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)*

      - **allocation.devices.config.requests** ([]string)

        *Atomic: will be replaced during a merge*
        
        Requests lists the names of requests where the configuration applies. If empty, its applies to all requests.
        
        References to subrequests must include the name of the main request and may include the subrequest using the format \<main request>[/\<subrequest>]. If just the main request is given, the configuration applies to all subrequests.

    - **allocation.devices.results** ([]DeviceRequestAllocationResult)

      *Atomic: will be replaced during a merge*
      
      Results lists all allocated devices.

      <a name="DeviceRequestAllocationResult"></a>
      *DeviceRequestAllocationResult contains the allocation result for one request.*

      - **allocation.devices.results.device** (string), required

        Device references one device instance via its name in the driver's resource pool. It must be a DNS label.

      - **allocation.devices.results.driver** (string), required

        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.
        
        Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.

      - **allocation.devices.results.pool** (string), required

        This name together with the driver name and the device name field identify which device was allocated (`\<driver name>/\<pool name>/\<device name>`).
        
        Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.

      - **allocation.devices.results.request** (string), required

        Request is the name of the request in the claim which caused this device to be allocated. If it references a subrequest in the firstAvailable list on a DeviceRequest, this field must include both the name of the main request and the subrequest using the format \<main request>/\<subrequest>.
        
        Multiple devices may have been allocated per request.

      - **allocation.devices.results.adminAccess** (boolean)

        AdminAccess indicates that this device was allocated for administrative access. See the corresponding request field for a definition of mode.
        
        This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.

      - **allocation.devices.results.tolerations** ([]DeviceToleration)

        *Atomic: will be replaced during a merge*
        
        A copy of all tolerations specified in the request at the time when the device got allocated.
        
        The maximum number of tolerations is 16.
        
        This is an alpha field and requires enabling the DRADeviceTaints feature gate.

        <a name="DeviceToleration"></a>
        *The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.*

        - **allocation.devices.results.tolerations.effect** (string)

          Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.

        - **allocation.devices.results.tolerations.key** (string)

          Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.

        - **allocation.devices.results.tolerations.operator** (string)

          Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.

        - **allocation.devices.results.tolerations.tolerationSeconds** (int64)

          TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as \<time when taint was adedd> + \<toleration seconds>.

        - **allocation.devices.results.tolerations.value** (string)

          Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.

  - **allocation.nodeSelector** (NodeSelector)

    NodeSelector defines where the allocated resources are available. If unset, they are available everywhere.

    <a name="NodeSelector"></a>
    *A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.*

    - **allocation.nodeSelector.nodeSelectorTerms** ([]NodeSelectorTerm), required

      *Atomic: will be replaced during a merge*
      
      Required. A list of node selector terms. The terms are ORed.

      <a name="NodeSelectorTerm"></a>
      *A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.*

      - **allocation.nodeSelector.nodeSelectorTerms.matchExpressions** ([]<a href="{{< ref "../common-definitions/node-selector-requirement#NodeSelectorRequirement" >}}">NodeSelectorRequirement</a>)

        *Atomic: will be replaced during a merge*
        
        A list of node selector requirements by node's labels.

      - **allocation.nodeSelector.nodeSelectorTerms.matchFields** ([]<a href="{{< ref "../common-definitions/node-selector-requirement#NodeSelectorRequirement" >}}">NodeSelectorRequirement</a>)

        *Atomic: will be replaced during a merge*
        
        A list of node selector requirements by node's fields.

- **devices** ([]AllocatedDeviceStatus)

  *Map: unique values on keys `driver, device, pool` will be kept during a merge*
  
  Devices contains the status of each device allocated for this claim, as reported by the driver. This can include driver-specific information. Entries are owned by their respective drivers.

  <a name="AllocatedDeviceStatus"></a>
  *AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.*

  - **devices.device** (string), required

    Device references one device instance via its name in the driver's resource pool. It must be a DNS label.

  - **devices.driver** (string), required

    Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.
    
    Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.

  - **devices.pool** (string), required

    This name together with the driver name and the device name field identify which device was allocated (`\<driver name>/\<pool name>/\<device name>`).
    
    Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.

  - **devices.conditions** ([]Condition)

    *Map: unique values on key type will be kept during a merge*
    
    Conditions contains the latest observation of the device's state. If the device has been configured according to the class and claim config references, the `Ready` condition should be True.
    
    Must not contain more than 8 entries.

    <a name="Condition"></a>
    *Condition contains details for one aspect of the current state of this API Resource.*

    - **devices.conditions.lastTransitionTime** (Time), required

      lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.

      <a name="Time"></a>
      *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.*

    - **devices.conditions.message** (string), required

      message is a human readable message indicating details about the transition. This may be an empty string.

    - **devices.conditions.reason** (string), required

      reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.

    - **devices.conditions.status** (string), required

      status of the condition, one of True, False, Unknown.

    - **devices.conditions.type** (string), required

      type of condition in CamelCase or in foo.example.com/CamelCase.

    - **devices.conditions.observedGeneration** (int64)

      observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.

  - **devices.data** (RawExtension)

    Data contains arbitrary driver-specific data.
    
    The length of the raw data must be smaller or equal to 10 Ki.

    <a name="RawExtension"></a>
    *RawExtension is used to hold extensions in external versions.
    
    To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.
    
    // Internal package:
    
    	type MyAPIObject struct {
    		runtime.TypeMeta `json:",inline"`
    		MyPlugin runtime.Object `json:"myPlugin"`
    	}
    
    	type PluginA struct {
    		AOption string `json:"aOption"`
    	}
    
    // External package:
    
    	type MyAPIObject struct {
    		runtime.TypeMeta `json:",inline"`
    		MyPlugin runtime.RawExtension `json:"myPlugin"`
    	}
    
    	type PluginA struct {
    		AOption string `json:"aOption"`
    	}
    
    // On the wire, the JSON will look something like this:
    
    	{
    		"kind":"MyAPIObject",
    		"apiVersion":"v1",
    		"myPlugin": {
    			"kind":"PluginA",
    			"aOption":"foo",
    		},
    	}
    
    So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package's DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)*

  - **devices.networkData** (NetworkDeviceData)

    NetworkData contains network-related information specific to the device.

    <a name="NetworkDeviceData"></a>
    *NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context.*

    - **devices.networkData.hardwareAddress** (string)

      HardwareAddress represents the hardware address (e.g. MAC Address) of the device's network interface.
      
      Must not be longer than 128 characters.

    - **devices.networkData.interfaceName** (string)

      InterfaceName specifies the name of the network interface associated with the allocated device. This might be the name of a physical or virtual network interface being configured in the pod.
      
      Must not be longer than 256 characters.

    - **devices.networkData.ips** ([]string)

      *Atomic: will be replaced during a merge*
      
      IPs lists the network addresses assigned to the device's network interface. This can include both IPv4 and IPv6 addresses. The IPs are in the CIDR notation, which includes both the address and the associated subnet mask. e.g.: "192.0.2.5/24" for IPv4 and "2001:db8::5/64" for IPv6.

- **reservedFor** ([]ResourceClaimConsumerReference)

  *Patch strategy: merge on key `uid`*
  
  *Map: unique values on key uid will be kept during a merge*
  
  ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.
  
  In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.
  
  Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.
  
  There can be at most 256 such reservations. This may get increased in the future, but not reduced.

  <a name="ResourceClaimConsumerReference"></a>
  *ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.*

  - **reservedFor.name** (string), required

    Name is the name of resource being referenced.

  - **reservedFor.resource** (string), required

    Resource is the type of resource being referenced, for example "pods".

  - **reservedFor.uid** (string), required

    UID identifies exactly one incarnation of the resource.

  - **reservedFor.apiGroup** (string)

    APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources.






## ResourceClaimList {#ResourceClaimList}

ResourceClaimList is a collection of claims.

<hr>

- **apiVersion**: resource.k8s.io/v1beta2


- **kind**: ResourceClaimList


- **metadata** (<a href="{{< ref "../common-definitions/list-meta#ListMeta" >}}">ListMeta</a>)

  Standard list metadata

- **items** ([]<a href="{{< ref "../workload-resources/resource-claim-v1beta2#ResourceClaim" >}}">ResourceClaim</a>), required

  Items is the list of resource claims.
