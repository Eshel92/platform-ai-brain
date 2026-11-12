<!-- Part 2 of 4 of reference/kubernetes-api/workload-resources/resource-claim-v1beta2.md (split because the page is big). -->

## ResourceClaimSpec {#ResourceClaimSpec}

ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

<hr>

- **devices** (DeviceClaim)

  Devices defines how to request devices.

  <a name="DeviceClaim"></a>
  *DeviceClaim defines how to request devices with a ResourceClaim.*

  - **devices.config** ([]DeviceClaimConfiguration)

    *Atomic: will be replaced during a merge*
    
    This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim.

    <a name="DeviceClaimConfiguration"></a>
    *DeviceClaimConfiguration is used for configuration parameters in DeviceClaim.*

    - **devices.config.opaque** (OpaqueDeviceConfiguration)

      Opaque provides driver-specific configuration parameters.

      <a name="OpaqueDeviceConfiguration"></a>
      *OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.*

      - **devices.config.opaque.driver** (string), required

        Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.
        
        An admission policy provided by the driver developer could use this to decide whether it needs to validate them.
        
        Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.

      - **devices.config.opaque.parameters** (RawExtension), required

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

    - **devices.config.requests** ([]string)

      *Atomic: will be replaced during a merge*
      
      Requests lists the names of requests where the configuration applies. If empty, it applies to all requests.
      
      References to subrequests must include the name of the main request and may include the subrequest using the format \<main request>[/\<subrequest>]. If just the main request is given, the configuration applies to all subrequests.

  - **devices.constraints** ([]DeviceConstraint)

    *Atomic: will be replaced during a merge*
    
    These constraints must be satisfied by the set of devices that get allocated for the claim.

    <a name="DeviceConstraint"></a>
    *DeviceConstraint must have exactly one field set besides Requests.*

    - **devices.constraints.matchAttribute** (string)

      MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.
      
      For example, if you specified "dra.example.com/numa" (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn't, then it also will not be chosen.
      
      Must include the domain qualifier.

    - **devices.constraints.requests** ([]string)

      *Atomic: will be replaced during a merge*
      
      Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.
      
      References to subrequests must include the name of the main request and may include the subrequest using the format \<main request>[/\<subrequest>]. If just the main request is given, the constraint applies to all subrequests.

  - **devices.requests** ([]DeviceRequest)

    *Atomic: will be replaced during a merge*
    
    Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated.

    <a name="DeviceRequest"></a>
    *DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests.*

    - **devices.requests.name** (string), required

      Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.
      
      References using the name in the DeviceRequest will uniquely identify a request when the Exactly field is set. When the FirstAvailable field is set, a reference to the name of the DeviceRequest will match whatever subrequest is chosen by the scheduler.
      
      Must be a DNS label.

    - **devices.requests.exactly** (ExactDeviceRequest)

      Exactly specifies the details for a single request that must be met exactly for the request to be satisfied.
      
      One of Exactly or FirstAvailable must be set.

      <a name="ExactDeviceRequest"></a>
      *ExactDeviceRequest is a request for one or more identical devices.*

      - **devices.requests.exactly.deviceClassName** (string), required

        DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.
        
        A DeviceClassName is required.
        
        Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference.

      - **devices.requests.exactly.adminAccess** (boolean)

        AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device.  They ignore all ordinary claims to the device with respect to access modes and any resource allocations.
        
        This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.

      - **devices.requests.exactly.allocationMode** (string)

        AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:
        
        - ExactCount: This request is for a specific number of devices.
          This is the default. The exact number is provided in the
          count field.
        
        - All: This request is for all of the matching devices in a pool.
          At least one device must exist on the node for the allocation to succeed.
          Allocation will fail if some devices are already allocated,
          unless adminAccess is requested.
        
        If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.
        
        More modes may get added in the future. Clients must refuse to handle requests with unknown modes.

      - **devices.requests.exactly.count** (int64)

        Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one.

      - **devices.requests.exactly.selectors** ([]DeviceSelector)

        *Atomic: will be replaced during a merge*
        
        Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.

        <a name="DeviceSelector"></a>
        *DeviceSelector must have exactly one field set.*

        - **devices.requests.exactly.selectors.cel** (CELDeviceSelector)

          CEL contains a CEL expression for selecting a device.

          <a name="CELDeviceSelector"></a>
          *CELDeviceSelector contains a CEL expression for selecting a device.*

          - **devices.requests.exactly.selectors.cel.expression** (string), required

            Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.
            
            The expression's input is an object named "device", which carries the following properties:
             - driver (string): the name of the driver which defines this device.
             - attributes (map[string]object): the device's attributes, grouped by prefix
               (e.g. device.attributes["dra.example.com"] evaluates to an object with all
               of the attributes which were prefixed by "dra.example.com".
             - capacity (map[string]object): the device's capacities, grouped by prefix.
            
            Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:
            
                device.driver
                device.attributes["dra.example.com"].model
                device.attributes["ext.example.com"].family
                device.capacity["dra.example.com"].modules
            
            The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.
            
            The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.
            
            If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.
            
            A robust expression should check for the existence of attributes before referencing them.
            
            For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:
            
                cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)
            
            The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.

      - **devices.requests.exactly.tolerations** ([]DeviceToleration)

        *Atomic: will be replaced during a merge*
        
        If specified, the request's tolerations.
        
        Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.
        
        In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.
        
        The maximum number of tolerations is 16.
        
        This is an alpha field and requires enabling the DRADeviceTaints feature gate.

        <a name="DeviceToleration"></a>
        *The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.*

        - **devices.requests.exactly.tolerations.effect** (string)

          Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.

        - **devices.requests.exactly.tolerations.key** (string)

          Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.

        - **devices.requests.exactly.tolerations.operator** (string)

          Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.

        - **devices.requests.exactly.tolerations.tolerationSeconds** (int64)

          TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as \<time when taint was adedd> + \<toleration seconds>.

        - **devices.requests.exactly.tolerations.value** (string)

          Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.

    - **devices.requests.firstAvailable** ([]DeviceSubRequest)

      *Atomic: will be replaced during a merge*
      
      FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.
      
      DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.

      <a name="DeviceSubRequest"></a>
      *DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.
      
      DeviceSubRequest is similar to ExactDeviceRequest, but doesn't expose the AdminAccess field as that one is only supported when requesting a specific device.*

      - **devices.requests.firstAvailable.deviceClassName** (string), required

        DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this subrequest.
        
        A class is required. Which classes are available depends on the cluster.
        
        Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference.

      - **devices.requests.firstAvailable.name** (string), required

        Name can be used to reference this subrequest in the list of constraints or the list of configurations for the claim. References must use the format \<main request>/\<subrequest>.
        
        Must be a DNS label.

      - **devices.requests.firstAvailable.allocationMode** (string)

        AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:
        
        - ExactCount: This request is for a specific number of devices.
          This is the default. The exact number is provided in the
          count field.
        
        - All: This subrequest is for all of the matching devices in a pool.
          Allocation will fail if some devices are already allocated,
          unless adminAccess is requested.
        
        If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.
        
        More modes may get added in the future. Clients must refuse to handle requests with unknown modes.

      - **devices.requests.firstAvailable.count** (int64)

        Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one.

      - **devices.requests.firstAvailable.selectors** ([]DeviceSelector)

        *Atomic: will be replaced during a merge*
        
        Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.

        <a name="DeviceSelector"></a>
        *DeviceSelector must have exactly one field set.*

        - **devices.requests.firstAvailable.selectors.cel** (CELDeviceSelector)

          CEL contains a CEL expression for selecting a device.

          <a name="CELDeviceSelector"></a>
          *CELDeviceSelector contains a CEL expression for selecting a device.*

          - **devices.requests.firstAvailable.selectors.cel.expression** (string), required

            Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.
            
            The expression's input is an object named "device", which carries the following properties:
             - driver (string): the name of the driver which defines this device.
             - attributes (map[string]object): the device's attributes, grouped by prefix
               (e.g. device.attributes["dra.example.com"] evaluates to an object with all
               of the attributes which were prefixed by "dra.example.com".
             - capacity (map[string]object): the device's capacities, grouped by prefix.
            
            Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:
            
                device.driver
                device.attributes["dra.example.com"].model
                device.attributes["ext.example.com"].family
                device.capacity["dra.example.com"].modules
            
            The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.
            
            The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.
            
            If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.
            
            A robust expression should check for the existence of attributes before referencing them.
            
            For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:
            
                cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)
            
            The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.

      - **devices.requests.firstAvailable.tolerations** ([]DeviceToleration)

        *Atomic: will be replaced during a merge*
        
        If specified, the request's tolerations.
        
        Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.
        
        In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.
        
        The maximum number of tolerations is 16.
        
        This is an alpha field and requires enabling the DRADeviceTaints feature gate.

        <a name="DeviceToleration"></a>
        *The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.*

        - **devices.requests.firstAvailable.tolerations.effect** (string)

          Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.

        - **devices.requests.firstAvailable.tolerations.key** (string)

          Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name.

        - **devices.requests.firstAvailable.tolerations.operator** (string)

          Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.

        - **devices.requests.firstAvailable.tolerations.tolerationSeconds** (int64)

          TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as \<time when taint was adedd> + \<toleration seconds>.

        - **devices.requests.firstAvailable.tolerations.value** (string)

          Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value.
