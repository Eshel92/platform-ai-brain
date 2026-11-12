<!-- Part 2 of 4 of reference/config-api/kube-controller-manager-config.v1alpha1.md (split because the page is big). -->

## `GenericControllerManagerConfiguration`     {#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration}
    

**Appears in:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>GenericControllerManagerConfiguration holds configuration for a generic controller-manager.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>Port</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>port is the port that the controller-manager's http service runs on.</p>
</td>
</tr>
<tr><td><code>Address</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>address is the IP address to serve on (set to 0.0.0.0 for all interfaces).</p>
</td>
</tr>
<tr><td><code>MinResyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>minResyncPeriod is the resync period in reflectors; will be random between
minResyncPeriod and 2*minResyncPeriod.</p>
</td>
</tr>
<tr><td><code>ClientConnection</code> <B>[Required]</B><br/>
<a href="#ClientConnectionConfiguration"><code>ClientConnectionConfiguration</code></a>
</td>
<td>
   <p>ClientConnection specifies the kubeconfig file and client connection
settings for the proxy server to use when communicating with the apiserver.</p>
</td>
</tr>
<tr><td><code>ControllerStartInterval</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>How long to wait between starting controller managers</p>
</td>
</tr>
<tr><td><code>LeaderElection</code> <B>[Required]</B><br/>
<a href="#LeaderElectionConfiguration"><code>LeaderElectionConfiguration</code></a>
</td>
<td>
   <p>leaderElection defines the configuration of leader election client.</p>
</td>
</tr>
<tr><td><code>Controllers</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>Controllers is the list of controllers to enable or disable
'*' means &quot;all enabled by default controllers&quot;
'foo' means &quot;enable 'foo'&quot;
'-foo' means &quot;disable 'foo'&quot;
first item for a particular name wins</p>
</td>
</tr>
<tr><td><code>Debugging</code> <B>[Required]</B><br/>
<a href="#DebuggingConfiguration"><code>DebuggingConfiguration</code></a>
</td>
<td>
   <p>DebuggingConfiguration holds configuration for Debugging related features.</p>
</td>
</tr>
<tr><td><code>LeaderMigrationEnabled</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>LeaderMigrationEnabled indicates whether Leader Migration should be enabled for the controller manager.</p>
</td>
</tr>
<tr><td><code>LeaderMigration</code> <B>[Required]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration"><code>LeaderMigrationConfiguration</code></a>
</td>
<td>
   <p>LeaderMigration holds the configuration for Leader Migration.</p>
</td>
</tr>
</tbody>
</table>
  
  


## `KubeControllerManagerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration}
    


<p>KubeControllerManagerConfiguration contains elements describing kube-controller manager.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubecontrollermanager.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>KubeControllerManagerConfiguration</code></td></tr>
    
  
<tr><td><code>Generic</code> <B>[Required]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration"><code>GenericControllerManagerConfiguration</code></a>
</td>
<td>
   <p>Generic holds configuration for a generic controller-manager</p>
</td>
</tr>
<tr><td><code>KubeCloudShared</code> <B>[Required]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration"><code>KubeCloudSharedConfiguration</code></a>
</td>
<td>
   <p>KubeCloudSharedConfiguration holds configuration for shared related features
both in cloud controller manager and kube-controller manager.</p>
</td>
</tr>
<tr><td><code>AttachDetachController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-AttachDetachControllerConfiguration"><code>AttachDetachControllerConfiguration</code></a>
</td>
<td>
   <p>AttachDetachControllerConfiguration holds configuration for
AttachDetachController related features.</p>
</td>
</tr>
<tr><td><code>CSRSigningController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningControllerConfiguration"><code>CSRSigningControllerConfiguration</code></a>
</td>
<td>
   <p>CSRSigningControllerConfiguration holds configuration for
CSRSigningController related features.</p>
</td>
</tr>
<tr><td><code>DaemonSetController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DaemonSetControllerConfiguration"><code>DaemonSetControllerConfiguration</code></a>
</td>
<td>
   <p>DaemonSetControllerConfiguration holds configuration for DaemonSetController
related features.</p>
</td>
</tr>
<tr><td><code>DeploymentController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DeploymentControllerConfiguration"><code>DeploymentControllerConfiguration</code></a>
</td>
<td>
   <p>DeploymentControllerConfiguration holds configuration for
DeploymentController related features.</p>
</td>
</tr>
<tr><td><code>StatefulSetController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-StatefulSetControllerConfiguration"><code>StatefulSetControllerConfiguration</code></a>
</td>
<td>
   <p>StatefulSetControllerConfiguration holds configuration for
StatefulSetController related features.</p>
</td>
</tr>
<tr><td><code>DeprecatedController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DeprecatedControllerConfiguration"><code>DeprecatedControllerConfiguration</code></a>
</td>
<td>
   <p>DeprecatedControllerConfiguration holds configuration for some deprecated
features.</p>
</td>
</tr>
<tr><td><code>EndpointController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointControllerConfiguration"><code>EndpointControllerConfiguration</code></a>
</td>
<td>
   <p>EndpointControllerConfiguration holds configuration for EndpointController
related features.</p>
</td>
</tr>
<tr><td><code>EndpointSliceController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceControllerConfiguration"><code>EndpointSliceControllerConfiguration</code></a>
</td>
<td>
   <p>EndpointSliceControllerConfiguration holds configuration for
EndpointSliceController related features.</p>
</td>
</tr>
<tr><td><code>EndpointSliceMirroringController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceMirroringControllerConfiguration"><code>EndpointSliceMirroringControllerConfiguration</code></a>
</td>
<td>
   <p>EndpointSliceMirroringControllerConfiguration holds configuration for
EndpointSliceMirroringController related features.</p>
</td>
</tr>
<tr><td><code>EphemeralVolumeController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EphemeralVolumeControllerConfiguration"><code>EphemeralVolumeControllerConfiguration</code></a>
</td>
<td>
   <p>EphemeralVolumeControllerConfiguration holds configuration for EphemeralVolumeController
related features.</p>
</td>
</tr>
<tr><td><code>GarbageCollectorController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-GarbageCollectorControllerConfiguration"><code>GarbageCollectorControllerConfiguration</code></a>
</td>
<td>
   <p>GarbageCollectorControllerConfiguration holds configuration for
GarbageCollectorController related features.</p>
</td>
</tr>
<tr><td><code>HPAController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-HPAControllerConfiguration"><code>HPAControllerConfiguration</code></a>
</td>
<td>
   <p>HPAControllerConfiguration holds configuration for HPAController related features.</p>
</td>
</tr>
<tr><td><code>JobController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-JobControllerConfiguration"><code>JobControllerConfiguration</code></a>
</td>
<td>
   <p>JobControllerConfiguration holds configuration for JobController related features.</p>
</td>
</tr>
<tr><td><code>CronJobController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CronJobControllerConfiguration"><code>CronJobControllerConfiguration</code></a>
</td>
<td>
   <p>CronJobControllerConfiguration holds configuration for CronJobController related features.</p>
</td>
</tr>
<tr><td><code>LegacySATokenCleaner</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-LegacySATokenCleanerConfiguration"><code>LegacySATokenCleanerConfiguration</code></a>
</td>
<td>
   <p>LegacySATokenCleanerConfiguration holds configuration for LegacySATokenCleaner related features.</p>
</td>
</tr>
<tr><td><code>NamespaceController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-NamespaceControllerConfiguration"><code>NamespaceControllerConfiguration</code></a>
</td>
<td>
   <p>NamespaceControllerConfiguration holds configuration for NamespaceController
related features.</p>
</td>
</tr>
<tr><td><code>NodeIPAMController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-NodeIPAMControllerConfiguration"><code>NodeIPAMControllerConfiguration</code></a>
</td>
<td>
   <p>NodeIPAMControllerConfiguration holds configuration for NodeIPAMController
related features.</p>
</td>
</tr>
<tr><td><code>NodeLifecycleController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-NodeLifecycleControllerConfiguration"><code>NodeLifecycleControllerConfiguration</code></a>
</td>
<td>
   <p>NodeLifecycleControllerConfiguration holds configuration for
NodeLifecycleController related features.</p>
</td>
</tr>
<tr><td><code>PersistentVolumeBinderController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeBinderControllerConfiguration"><code>PersistentVolumeBinderControllerConfiguration</code></a>
</td>
<td>
   <p>PersistentVolumeBinderControllerConfiguration holds configuration for
PersistentVolumeBinderController related features.</p>
</td>
</tr>
<tr><td><code>PodGCController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-PodGCControllerConfiguration"><code>PodGCControllerConfiguration</code></a>
</td>
<td>
   <p>PodGCControllerConfiguration holds configuration for PodGCController
related features.</p>
</td>
</tr>
<tr><td><code>ReplicaSetController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicaSetControllerConfiguration"><code>ReplicaSetControllerConfiguration</code></a>
</td>
<td>
   <p>ReplicaSetControllerConfiguration holds configuration for ReplicaSet related features.</p>
</td>
</tr>
<tr><td><code>ReplicationController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicationControllerConfiguration"><code>ReplicationControllerConfiguration</code></a>
</td>
<td>
   <p>ReplicationControllerConfiguration holds configuration for
ReplicationController related features.</p>
</td>
</tr>
<tr><td><code>ResourceQuotaController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ResourceQuotaControllerConfiguration"><code>ResourceQuotaControllerConfiguration</code></a>
</td>
<td>
   <p>ResourceQuotaControllerConfiguration holds configuration for
ResourceQuotaController related features.</p>
</td>
</tr>
<tr><td><code>SAController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-SAControllerConfiguration"><code>SAControllerConfiguration</code></a>
</td>
<td>
   <p>SAControllerConfiguration holds configuration for ServiceAccountController
related features.</p>
</td>
</tr>
<tr><td><code>ServiceController</code> <B>[Required]</B><br/>
<a href="#ServiceControllerConfiguration"><code>ServiceControllerConfiguration</code></a>
</td>
<td>
   <p>ServiceControllerConfiguration holds configuration for ServiceController
related features.</p>
</td>
</tr>
<tr><td><code>TTLAfterFinishedController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-TTLAfterFinishedControllerConfiguration"><code>TTLAfterFinishedControllerConfiguration</code></a>
</td>
<td>
   <p>TTLAfterFinishedControllerConfiguration holds configuration for
TTLAfterFinishedController related features.</p>
</td>
</tr>
<tr><td><code>ValidatingAdmissionPolicyStatusController</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ValidatingAdmissionPolicyStatusControllerConfiguration"><code>ValidatingAdmissionPolicyStatusControllerConfiguration</code></a>
</td>
<td>
   <p>ValidatingAdmissionPolicyStatusControllerConfiguration holds configuration for
ValidatingAdmissionPolicyStatusController related features.</p>
</td>
</tr>
</tbody>
</table>


## `AttachDetachControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-AttachDetachControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>AttachDetachControllerConfiguration contains elements describing AttachDetachController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>DisableAttachDetachReconcilerSync</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>Reconciler runs a periodic loop to reconcile the desired state of the with
the actual state of the world by triggering attach detach operations.
This flag enables or disables reconcile.  Is false by default, and thus enabled.</p>
</td>
</tr>
<tr><td><code>ReconcilerSyncLoopPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>ReconcilerSyncLoopPeriod is the amount of time the reconciler sync states loop
wait between successive executions. Is set to 60 sec by default.</p>
</td>
</tr>
<tr><td><code>disableForceDetachOnTimeout</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>DisableForceDetachOnTimeout disables force detach when the maximum unmount
time is exceeded. Is false by default, and thus force detach on unmount is
enabled.</p>
</td>
</tr>
</tbody>
</table>


## `CSRSigningConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration}
    

**Appears in:**

- [CSRSigningControllerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningControllerConfiguration)


<p>CSRSigningConfiguration holds information about a particular CSR signer</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>CertFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>certFile is the filename containing a PEM-encoded
X509 CA certificate used to issue certificates</p>
</td>
</tr>
<tr><td><code>KeyFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>keyFile is the filename containing a PEM-encoded
RSA or ECDSA private key used to issue certificates</p>
</td>
</tr>
</tbody>
</table>


## `CSRSigningControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>CSRSigningControllerConfiguration contains elements describing CSRSigningController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ClusterSigningCertFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterSigningCertFile is the filename containing a PEM-encoded
X509 CA certificate used to issue cluster-scoped certificates</p>
</td>
</tr>
<tr><td><code>ClusterSigningKeyFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterSigningCertFile is the filename containing a PEM-encoded
RSA or ECDSA private key used to issue cluster-scoped certificates</p>
</td>
</tr>
<tr><td><code>KubeletServingSignerConfiguration</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>kubeletServingSignerConfiguration holds the certificate and key used to issue certificates for the kubernetes.io/kubelet-serving signer</p>
</td>
</tr>
<tr><td><code>KubeletClientSignerConfiguration</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>kubeletClientSignerConfiguration holds the certificate and key used to issue certificates for the kubernetes.io/kube-apiserver-client-kubelet</p>
</td>
</tr>
<tr><td><code>KubeAPIServerClientSignerConfiguration</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>kubeAPIServerClientSignerConfiguration holds the certificate and key used to issue certificates for the kubernetes.io/kube-apiserver-client</p>
</td>
</tr>
<tr><td><code>LegacyUnknownSignerConfiguration</code> <B>[Required]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>legacyUnknownSignerConfiguration holds the certificate and key used to issue certificates for the kubernetes.io/legacy-unknown</p>
</td>
</tr>
<tr><td><code>ClusterSigningDuration</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>clusterSigningDuration is the max length of duration signed certificates will be given.
Individual CSRs may request shorter certs by setting spec.expirationSeconds.</p>
</td>
</tr>
</tbody>
</table>


## `CronJobControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-CronJobControllerConfiguration}
    

**Appears in:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>CronJobControllerConfiguration contains elements describing CrongJob2Controller.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentCronJobSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentCronJobSyncs is the number of job objects that are
allowed to sync concurrently. Larger number = more responsive jobs,
but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>
