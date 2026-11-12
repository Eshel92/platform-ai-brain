<!-- Part 1 of 4 of reference/config-api/kube-controller-manager-config.v1alpha1.md (split because the page is big). -->

## Resource Types 


- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)
- [LeaderMigrationConfiguration](#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration)
- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)
  
    
    


## `ClientConnectionConfiguration`     {#ClientConnectionConfiguration}
    

**Appears in:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>ClientConnectionConfiguration contains details for constructing a client.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubeconfig</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>kubeconfig is the path to a KubeConfig file.</p>
</td>
</tr>
<tr><td><code>acceptContentTypes</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>acceptContentTypes defines the Accept header sent by clients when connecting to a server, overriding the
default value of 'application/json'. This field will control all connections to the server used by a particular
client.</p>
</td>
</tr>
<tr><td><code>contentType</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>contentType is the content type used when sending data to the server from this client.</p>
</td>
</tr>
<tr><td><code>qps</code> <B>[Required]</B><br/>
<code>float32</code>
</td>
<td>
   <p>qps controls the number of queries per second allowed for this connection.</p>
</td>
</tr>
<tr><td><code>burst</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>burst allows extra queries to accumulate when a client is exceeding its rate.</p>
</td>
</tr>
</tbody>
</table>


## `DebuggingConfiguration`     {#DebuggingConfiguration}
    

**Appears in:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>DebuggingConfiguration holds configuration for Debugging related features.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>enableProfiling</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableProfiling enables profiling via web interface host:port/debug/pprof/</p>
</td>
</tr>
<tr><td><code>enableContentionProfiling</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableContentionProfiling enables block profiling, if
enableProfiling is true.</p>
</td>
</tr>
</tbody>
</table>


## `LeaderElectionConfiguration`     {#LeaderElectionConfiguration}
    

**Appears in:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>LeaderElectionConfiguration defines the configuration of leader election
clients for components that can run with leader election enabled.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>leaderElect</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>leaderElect enables a leader election client to gain leadership
before executing the main loop. Enable this when running replicated
components for high availability.</p>
</td>
</tr>
<tr><td><code>leaseDuration</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>leaseDuration is the duration that non-leader candidates will wait
after observing a leadership renewal until attempting to acquire
leadership of a led but unrenewed leader slot. This is effectively the
maximum duration that a leader can be stopped before it is replaced
by another candidate. This is only applicable if leader election is
enabled.</p>
</td>
</tr>
<tr><td><code>renewDeadline</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>renewDeadline is the interval between attempts by the acting master to
renew a leadership slot before it stops leading. This must be less
than or equal to the lease duration. This is only applicable if leader
election is enabled.</p>
</td>
</tr>
<tr><td><code>retryPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>retryPeriod is the duration the clients should wait between attempting
acquisition and renewal of a leadership. This is only applicable if
leader election is enabled.</p>
</td>
</tr>
<tr><td><code>resourceLock</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceLock indicates the resource object type that will be used to lock
during leader election cycles.</p>
</td>
</tr>
<tr><td><code>resourceName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName indicates the name of resource object that will be used to lock
during leader election cycles.</p>
</td>
</tr>
<tr><td><code>resourceNamespace</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName indicates the namespace of resource object that will be used to lock
during leader election cycles.</p>
</td>
</tr>
</tbody>
</table>


## `NodeControllerConfiguration`     {#NodeControllerConfiguration}
    

**Appears in:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)


<p>NodeControllerConfiguration contains elements describing NodeController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentNodeSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentNodeSyncs is the number of workers
concurrently synchronizing nodes</p>
</td>
</tr>
</tbody>
</table>


## `ServiceControllerConfiguration`     {#ServiceControllerConfiguration}
    

**Appears in:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ServiceControllerConfiguration contains elements describing ServiceController.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentServiceSyncs</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentServiceSyncs is the number of services that are
allowed to sync concurrently. Larger number = more responsive service
management, but more CPU (and network) load.</p>
</td>
</tr>
</tbody>
</table>
  


## `CloudControllerManagerConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration}
    


<p>CloudControllerManagerConfiguration contains elements describing cloud-controller manager.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>cloudcontrollermanager.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CloudControllerManagerConfiguration</code></td></tr>
    
  
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
<tr><td><code>NodeController</code> <B>[Required]</B><br/>
<a href="#NodeControllerConfiguration"><code>NodeControllerConfiguration</code></a>
</td>
<td>
   <p>NodeController holds configuration for node controller
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
<tr><td><code>NodeStatusUpdateFrequency</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>NodeStatusUpdateFrequency is the frequency at which the controller updates nodes' status</p>
</td>
</tr>
<tr><td><code>Webhook</code> <B>[Required]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-WebhookConfiguration"><code>WebhookConfiguration</code></a>
</td>
<td>
   <p>Webhook is the configuration for cloud-controller-manager hosted webhooks</p>
</td>
</tr>
</tbody>
</table>


## `CloudProviderConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudProviderConfiguration}
    

**Appears in:**

- [KubeCloudSharedConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration)


<p>CloudProviderConfiguration contains basically elements about cloud provider.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>Name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name is the provider for cloud services.</p>
</td>
</tr>
<tr><td><code>CloudConfigFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>cloudConfigFile is the path to the cloud provider configuration file.</p>
</td>
</tr>
</tbody>
</table>


## `KubeCloudSharedConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration}
    

**Appears in:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>KubeCloudSharedConfiguration contains elements shared by both kube-controller manager
and cloud-controller manager, but not genericconfig.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>CloudProvider</code> <B>[Required]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudProviderConfiguration"><code>CloudProviderConfiguration</code></a>
</td>
<td>
   <p>CloudProviderConfiguration holds configuration for CloudProvider related features.</p>
</td>
</tr>
<tr><td><code>ExternalCloudVolumePlugin</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>externalCloudVolumePlugin specifies the plugin to use when cloudProvider is &quot;external&quot;.
It is currently used by the in repo cloud providers to handle node and volume control in the KCM.</p>
</td>
</tr>
<tr><td><code>UseServiceAccountCredentials</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>useServiceAccountCredentials indicates whether controllers should be run with
individual service account credentials.</p>
</td>
</tr>
<tr><td><code>AllowUntaggedCloud</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>run with untagged cloud instances</p>
</td>
</tr>
<tr><td><code>RouteReconciliationPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>routeReconciliationPeriod is the period for reconciling routes created for Nodes by cloud provider..</p>
</td>
</tr>
<tr><td><code>NodeMonitorPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeMonitorPeriod is the period for syncing NodeStatus in NodeController.</p>
</td>
</tr>
<tr><td><code>ClusterName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterName is the instance prefix for the cluster.</p>
</td>
</tr>
<tr><td><code>ClusterCIDR</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterCIDR is CIDR Range for Pods in cluster.</p>
</td>
</tr>
<tr><td><code>AllocateNodeCIDRs</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>AllocateNodeCIDRs enables CIDRs for Pods to be allocated and, if
ConfigureCloudRoutes is true, to be set on the cloud provider.</p>
</td>
</tr>
<tr><td><code>CIDRAllocatorType</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>CIDRAllocatorType determines what kind of pod CIDR allocator will be used.</p>
</td>
</tr>
<tr><td><code>ConfigureCloudRoutes</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>configureCloudRoutes enables CIDRs allocated with allocateNodeCIDRs
to be configured on the cloud provider.</p>
</td>
</tr>
<tr><td><code>NodeSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeSyncPeriod is the period for syncing nodes from cloudprovider. Longer
periods will result in fewer calls to cloud provider, but may delay addition
of new nodes to cluster.</p>
</td>
</tr>
</tbody>
</table>


## `WebhookConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-WebhookConfiguration}
    

**Appears in:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)


<p>WebhookConfiguration contains configuration related to
cloud-controller-manager hosted webhooks</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>Webhooks</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>Webhooks is the list of webhooks to enable or disable
'*' means &quot;all enabled by default webhooks&quot;
'foo' means &quot;enable 'foo'&quot;
'-foo' means &quot;disable 'foo'&quot;
first item for a particular name wins</p>
</td>
</tr>
</tbody>
</table>
  
  


## `LeaderMigrationConfiguration`     {#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration}
    

**Appears in:**

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>LeaderMigrationConfiguration provides versioned configuration for all migrating leader locks.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>controllermanager.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>LeaderMigrationConfiguration</code></td></tr>
    
  
<tr><td><code>leaderName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>LeaderName is the name of the leader election resource that protects the migration
E.g. 1-20-KCM-to-1-21-CCM</p>
</td>
</tr>
<tr><td><code>resourceLock</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>ResourceLock indicates the resource object type that will be used to lock
Should be &quot;leases&quot; or &quot;endpoints&quot;</p>
</td>
</tr>
<tr><td><code>controllerLeaders</code> <B>[Required]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-ControllerLeaderConfiguration"><code>[]ControllerLeaderConfiguration</code></a>
</td>
<td>
   <p>ControllerLeaders contains a list of migrating leader lock configurations</p>
</td>
</tr>
</tbody>
</table>


## `ControllerLeaderConfiguration`     {#controllermanager-config-k8s-io-v1alpha1-ControllerLeaderConfiguration}
    

**Appears in:**

- [LeaderMigrationConfiguration](#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration)


<p>ControllerLeaderConfiguration provides the configuration for a migrating leader lock.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name is the name of the controller being migrated
E.g. service-controller, route-controller, cloud-node-controller, etc</p>
</td>
</tr>
<tr><td><code>component</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Component is the name of the component in which the controller should be running.
E.g. kube-controller-manager, cloud-controller-manager, etc
Or '*' meaning the controller can be run under any component that participates in the migration</p>
</td>
</tr>
</tbody>
</table>
