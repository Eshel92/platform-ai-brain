<!-- Part 1 of 4 of reference/kubernetes-api/workload-resources/resource-claim-v1beta2.md (split because the page is big). -->

## ResourceClaim {#ResourceClaim}

ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.

This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

<hr>

- **apiVersion**: resource.k8s.io/v1beta2


- **kind**: ResourceClaim


- **metadata** (<a href="{{< ref "../common-definitions/object-meta#ObjectMeta" >}}">ObjectMeta</a>)

  Standard object metadata

- **spec** (<a href="{{< ref "../workload-resources/resource-claim-v1beta2#ResourceClaimSpec" >}}">ResourceClaimSpec</a>), required

  Spec describes what is being requested and how to configure it. The spec is immutable.

- **status** (<a href="{{< ref "../workload-resources/resource-claim-v1beta2#ResourceClaimStatus" >}}">ResourceClaimStatus</a>)

  Status describes whether the claim is ready to use and what has been allocated.
