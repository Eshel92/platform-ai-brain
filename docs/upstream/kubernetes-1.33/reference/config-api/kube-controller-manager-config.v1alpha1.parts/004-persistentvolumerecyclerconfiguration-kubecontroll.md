<!-- Part 4 of 4 of reference/config-api/kube-controller-manager-config.v1alpha1.md (split because the page is big). -->

## `PersistentVolumeRecyclerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeRecyclerConfiguration}
    

**Appears in:**

- [VolumeConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-VolumeConfiguration)


<p>PersistentVolumeRecyclerConfiguration contains elements describing persistent volume plugins.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>MaximumRetry</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>maximumRetry is number of retries the PV recycler will execute on failure to recycle
PV.</p>
</td>
</tr>
<tr><td><code>MinimumTimeoutNFS</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>minimumTimeoutNFS is the minimum ActiveDeadlineSeconds to use for an NFS Recycler
pod.</p>
</td>
</tr>
<tr><td><code>PodTemplateFilePathNFS</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>podTemplateFilePathNFS is the file path to a pod definition used as a template for
NFS persistent volume recycling</p>
</td>
</tr>
<tr><td><code>IncrementTimeoutNFS</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>incrementTimeoutNFS is the increment of time added per Gi to ActiveDeadlineSeconds
for an NFS scrubber pod.</p>
</td>
</tr>
<tr><td><code>PodTemplateFilePathHostPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>podTemplateFilePathHostPath is the file path to a pod definition used as a template for
HostPath persistent volume recycling. This is for development and testing only and
will not work in a multi-node cluster.</p>
</td>
</tr>
<tr><td><code>MinimumTimeoutHostPath</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>minimumTimeoutHostPath is the minimum ActiveDeadlineSeconds to use for a HostPath
Recycler pod.  This is for development and testing only and will not work in a multi-node
cluster.</p>
</td>
</tr>
<tr><td><code>IncrementTimeoutHostPath</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>incrementTimeoutHostPath is the increment of time added per Gi to ActiveDeadlineSeconds
for a HostPath scrubber pod.  This is for development and testing only and will not work
in a multi-node cluster.</p>
</td>
</tr>
</tbody>
</table>


## `PodGCControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-PodGCControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>PodGCControllerConfiguration contains elements describing PodGCController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>TerminatedPodGCThreshold</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>terminatedPodGCThreshold is the number of terminated pods that can exist
before the terminated pod garbage collector starts deleting terminated pods.
If &lt;= 0, the terminated pod garbage collector is disabled.</p>
</td>
</tr>
</tbody>
</table>


## `ReplicaSetControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicaSetControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ReplicaSetControllerConfiguration contains elements describing ReplicaSetController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentRSSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentRSSyncs is the number of replica sets that are  allowed to sync
concurrently. Larger number = more responsive replica  management, but more
CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `ReplicationControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicationControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ReplicationControllerConfiguration contains elements describing ReplicationController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentRCSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentRCSyncs is the number of replication controllers that are
allowed to sync concurrently. Larger number = more responsive replica
management, but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `ResourceQuotaControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ResourceQuotaControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ResourceQuotaControllerConfiguration contains elements describing ResourceQuotaController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ResourceQuotaSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>resourceQuotaSyncPeriod is the period for syncing quota usage status
in the system.</p>
</td>
</tr>
<tr><td><code>ConcurrentResourceQuotaSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentResourceQuotaSyncs is the number of resource quotas that are
allowed to sync concurrently. Larger number = more responsive quota
management, but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `SAControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-SAControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>SAControllerConfiguration contains elements describing ServiceAccountController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ServiceAccountKeyFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>serviceAccountKeyFile is the filename containing a PEM-encoded private RSA key
used to sign service account tokens.</p>
</td>
</tr>
<tr><td><code>ConcurrentSATokenSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentSATokenSyncs is the number of service account token syncing operations
that will be done concurrently.</p>
</td>
</tr>
<tr><td><code>RootCAFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>rootCAFile is the root certificate authority will be included in service
account's token secret. This must be a valid PEM-encoded CA bundle.</p>
</td>
</tr>
</tbody>
</table>


## `StatefulSetControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-StatefulSetControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>StatefulSetControllerConfiguration contains elements describing StatefulSetController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentStatefulSetSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentStatefulSetSyncs is the number of statefulset objects that are
allowed to sync concurrently. Larger number = more responsive statefulsets,
but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>


## `TTLAfterFinishedControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-TTLAfterFinishedControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>TTLAfterFinishedControllerConfiguration contains elements describing TTLAfterFinishedController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentTTLSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentTTLSyncs is the number of TTL-after-finished collector workers that are
allowed to sync concurrently.</p>
</td>
</tr>
</tbody>
</table>


## `ValidatingAdmissionPolicyStatusControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ValidatingAdmissionPolicyStatusControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ValidatingAdmissionPolicyStatusControllerConfiguration contains elements describing ValidatingAdmissionPolicyStatusController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentPolicySyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentPolicySyncs is the number of policy objects that are
allowed to sync concurrently. Larger number = quicker type checking,
but more CPU (and network) load.
The default value is 5.</p>
</td>
</tr>
</tbody>
</table>


## `VolumeConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-VolumeConfiguration}
    

**Appears in:**

- [PersistentVolumeBinderControllerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeBinderControllerConfiguration)


<p>VolumeConfiguration contains <em>all</em> enumerated flags meant to configure all volume
plugins. From this config, the controller-manager binary will create many instances of
volume.VolumeConfig, each containing only the configuration needed for that plugin which
are then passed to the appropriate plugin. The ControllerManager binary is the only part
of the code which knows what plugins are supported and which flags correspond to each plugin.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>EnableHostPathProvisioning</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableHostPathProvisioning enables HostPath PV provisioning when running without a
cloud provider. This allows testing and development of provisioning features. HostPath
provisioning is not supported in any way, won't work in a multi-node cluster, and
should not be used for anything other than testing or development.</p>
</td>
</tr>
<tr><td><code>EnableDynamicProvisioning</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableDynamicProvisioning enables the provisioning of volumes when running within an environment
that supports dynamic provisioning. Defaults to true.</p>
</td>
</tr>
<tr><td><code>PersistentVolumeRecyclerConfiguration</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeRecyclerConfiguration"><code>PersistentVolumeRecyclerConfiguration</code></a>
</td>
<td>
   <p>persistentVolumeRecyclerConfiguration holds configuration for persistent volume plugins.</p>
</td>
</tr>
<tr><td><code>FlexVolumePluginDir</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>volumePluginDir is the full path of the directory in which the flex
volume plugin should search for additional third party volume plugins</p>
</td>
</tr>
</tbody>
</table>
