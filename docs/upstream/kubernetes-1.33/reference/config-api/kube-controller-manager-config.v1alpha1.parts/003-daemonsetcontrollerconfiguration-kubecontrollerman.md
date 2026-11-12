<!-- Part 3 of 4 of reference/config-api/kube-controller-manager-config.v1alpha1.md (split because the page is big). -->

## `DaemonSetControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DaemonSetControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DaemonSetControllerConfiguration contains elements describing DaemonSetController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentDaemonSetSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentDaemonSetSyncs is the number of daemonset objects that are
allowed to sync concurrently. Larger number = more responsive daemonset,
but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `DeploymentControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DeploymentControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DeploymentControllerConfiguration contains elements describing DeploymentController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentDeploymentSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentDeploymentSyncs is the number of deployment objects that are
allowed to sync concurrently. Larger number = more responsive deployments,
but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `DeprecatedControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DeprecatedControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DeprecatedControllerConfiguration contains elements be deprecated.</p>





## `EndpointControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EndpointControllerConfiguration contains elements describing EndpointController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentEndpointSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentEndpointSyncs is the number of endpoint syncing operations
that will be done concurrently. Larger number = faster endpoint updating,
but more CPU (and network) load.</p>
</td>
</tr>
<tr><td><code>EndpointUpdatesBatchPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>EndpointUpdatesBatchPeriod describes the length of endpoint updates batching period.
Processing of pod changes will be delayed by this duration to join them with potential
upcoming updates and reduce the overall number of endpoints updates.</p>
</td>
</tr>
</tbody>
</table>


## `EndpointSliceControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EndpointSliceControllerConfiguration contains elements describing
EndpointSliceController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentServiceEndpointSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentServiceEndpointSyncs is the number of service endpoint syncing
operations that will be done concurrently. Larger number = faster
endpoint slice updating, but more CPU (and network) load.</p>
</td>
</tr>
<tr><td><code>MaxEndpointsPerSlice</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>maxEndpointsPerSlice is the maximum number of endpoints that will be
added to an EndpointSlice. More endpoints per slice will result in fewer
and larger endpoint slices, but larger resources.</p>
</td>
</tr>
<tr><td><code>EndpointUpdatesBatchPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>EndpointUpdatesBatchPeriod describes the length of endpoint updates batching period.
Processing of pod changes will be delayed by this duration to join them with potential
upcoming updates and reduce the overall number of endpoints updates.</p>
</td>
</tr>
</tbody>
</table>


## `EndpointSliceMirroringControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceMirroringControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EndpointSliceMirroringControllerConfiguration contains elements describing
EndpointSliceMirroringController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>MirroringConcurrentServiceEndpointSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>mirroringConcurrentServiceEndpointSyncs is the number of service endpoint
syncing operations that will be done concurrently. Larger number = faster
endpoint slice updating, but more CPU (and network) load.</p>
</td>
</tr>
<tr><td><code>MirroringMaxEndpointsPerSubset</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>mirroringMaxEndpointsPerSubset is the maximum number of endpoints that
will be mirrored to an EndpointSlice for an EndpointSubset.</p>
</td>
</tr>
<tr><td><code>MirroringEndpointUpdatesBatchPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>mirroringEndpointUpdatesBatchPeriod can be used to batch EndpointSlice
updates. All updates triggered by EndpointSlice changes will be delayed
by up to 'mirroringEndpointUpdatesBatchPeriod'. If other addresses in the
same Endpoints resource change in that period, they will be batched to a
single EndpointSlice update. Default 0 value means that each Endpoints
update triggers an EndpointSlice update.</p>
</td>
</tr>
</tbody>
</table>


## `EphemeralVolumeControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EphemeralVolumeControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EphemeralVolumeControllerConfiguration contains elements describing EphemeralVolumeController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentEphemeralVolumeSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentEphemeralVolumeSyncseSyncs is the number of ephemeral volume syncing operations
that will be done concurrently. Larger number = faster ephemeral volume updating,
but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `GarbageCollectorControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-GarbageCollectorControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>GarbageCollectorControllerConfiguration contains elements describing GarbageCollectorController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>EnableGarbageCollector</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enables the generic garbage collector. MUST be synced with the
corresponding flag of the kube-apiserver. WARNING: the generic garbage
collector is an alpha feature.</p>
</td>
</tr>
<tr><td><code>ConcurrentGCSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentGCSyncs is the number of garbage collector workers that are
allowed to sync concurrently.</p>
</td>
</tr>
<tr><td><code>GCIgnoredResources</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-GroupResource"><code>[]GroupResource</code></a>
</td>
<td>
   <p>gcIgnoredResources is the list of GroupResources that garbage collection should ignore.</p>
</td>
</tr>
</tbody>
</table>


## `GroupResource`     {#kubecontrollermanager-config-k8s-io-v1alpha1-GroupResource}
    

**Appears in:**

- [GarbageCollectorControllerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-GarbageCollectorControllerConfiguration)


<p>GroupResource describes an group resource.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>Group</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>group is the group portion of the GroupResource.</p>
</td>
</tr>
<tr><td><code>Resource</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>resource is the resource portion of the GroupResource.</p>
</td>
</tr>
</tbody>
</table>


## `HPAControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-HPAControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>HPAControllerConfiguration contains elements describing HPAController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentHorizontalPodAutoscalerSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentHorizontalPodAutoscalerSyncs is the number of HPA objects that are allowed to sync concurrently.
Larger number = more responsive HPA processing, but more CPU (and network) load.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerSyncPeriod is the period for syncing the number of
pods in horizontal pod autoscaler.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerDownscaleStabilizationWindow</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerDowncaleStabilizationWindow is a period for which autoscaler will look
backwards and not scale down below any recommendation it made during that period.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerTolerance</code> <B>[Required]</B><br/>
<code>float64</code>
</td>
<td>
   <p>HorizontalPodAutoscalerTolerance is the tolerance for when
resource usage suggests upscaling/downscaling</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerCPUInitializationPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerCPUInitializationPeriod is the period after pod start when CPU samples
might be skipped.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerInitialReadinessDelay</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerInitialReadinessDelay is period after pod start during which readiness
changes are treated as readiness being set for the first time. The only effect of this is that
HPA will disregard CPU samples from unready pods that had last readiness change during that
period.</p>
</td>
</tr>
</tbody>
</table>


## `JobControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-JobControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>JobControllerConfiguration contains elements describing JobController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentJobSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentJobSyncs is the number of job objects that are
allowed to sync concurrently. Larger number = more responsive jobs,
but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `LegacySATokenCleanerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-LegacySATokenCleanerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>LegacySATokenCleanerConfiguration contains elements describing LegacySATokenCleaner</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>CleanUpPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>CleanUpPeriod is the period of time since the last usage of an
auto-generated service account token before it can be deleted.</p>
</td>
</tr>
</tbody>
</table>


## `NamespaceControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-NamespaceControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>NamespaceControllerConfiguration contains elements describing NamespaceController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>NamespaceSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>namespaceSyncPeriod is the period for syncing namespace life-cycle
updates.</p>
</td>
</tr>
<tr><td><code>ConcurrentNamespaceSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentNamespaceSyncs is the number of namespace objects that are
allowed to sync concurrently.</p>
</td>
</tr>
</tbody>
</table>


## `NodeIPAMControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-NodeIPAMControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>NodeIPAMControllerConfiguration contains elements describing NodeIpamController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ServiceCIDR</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>serviceCIDR is CIDR Range for Services in cluster.</p>
</td>
</tr>
<tr><td><code>SecondaryServiceCIDR</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>secondaryServiceCIDR is CIDR Range for Services in cluster. This is used in dual stack clusters. SecondaryServiceCIDR must be of different IP family than ServiceCIDR</p>
</td>
</tr>
<tr><td><code>NodeCIDRMaskSize</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>NodeCIDRMaskSize is the mask size for node cidr in cluster.</p>
</td>
</tr>
<tr><td><code>NodeCIDRMaskSizeIPv4</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>NodeCIDRMaskSizeIPv4 is the mask size for node cidr in dual-stack cluster.</p>
</td>
</tr>
<tr><td><code>NodeCIDRMaskSizeIPv6</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>NodeCIDRMaskSizeIPv6 is the mask size for node cidr in dual-stack cluster.</p>
</td>
</tr>
</tbody>
</table>


## `NodeLifecycleControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-NodeLifecycleControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>NodeLifecycleControllerConfiguration contains elements describing NodeLifecycleController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>NodeEvictionRate</code> <B>[Required]</B><br/>
<code>float32</code>
</td>
<td>
   <p>nodeEvictionRate is the number of nodes per second on which pods are deleted in case of node failure when a zone is healthy</p>
</td>
</tr>
<tr><td><code>SecondaryNodeEvictionRate</code> <B>[Required]</B><br/>
<code>float32</code>
</td>
<td>
   <p>secondaryNodeEvictionRate is the number of nodes per second on which pods are deleted in case of node failure when a zone is unhealthy</p>
</td>
</tr>
<tr><td><code>NodeStartupGracePeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeStartupGracePeriod is the amount of time which we allow starting a node to
be unresponsive before marking it unhealthy.</p>
</td>
</tr>
<tr><td><code>NodeMonitorGracePeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeMontiorGracePeriod is the amount of time which we allow a running node to be
unresponsive before marking it unhealthy. Must be N times more than kubelet's
nodeStatusUpdateFrequency, where N means number of retries allowed for kubelet
to post node status. This value should also be greater than the sum of
HTTP2_PING_TIMEOUT_SECONDS and HTTP2_READ_IDLE_TIMEOUT_SECONDS.</p>
</td>
</tr>
<tr><td><code>PodEvictionTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>podEvictionTimeout is the grace period for deleting pods on failed nodes.</p>
</td>
</tr>
<tr><td><code>LargeClusterSizeThreshold</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>secondaryNodeEvictionRate is implicitly overridden to 0 for clusters smaller than or equal to largeClusterSizeThreshold</p>
</td>
</tr>
<tr><td><code>UnhealthyZoneThreshold</code> <B>[Required]</B><br/>
<code>float32</code>
</td>
<td>
   <p>Zone is treated as unhealthy in nodeEvictionRate and secondaryNodeEvictionRate when at least
unhealthyZoneThreshold (no less than 3) of Nodes in the zone are NotReady</p>
</td>
</tr>
</tbody>
</table>


## `PersistentVolumeBinderControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeBinderControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>PersistentVolumeBinderControllerConfiguration contains elements describing
PersistentVolumeBinderController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>PVClaimBinderSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>pvClaimBinderSyncPeriod is the period for syncing persistent volumes
and persistent volume claims.</p>
</td>
</tr>
<tr><td><code>VolumeConfiguration</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-VolumeConfiguration"><code>VolumeConfiguration</code></a>
</td>
<td>
   <p>volumeConfiguration holds configuration for volume related features.</p>
</td>
</tr>
</tbody>
</table>
