<!-- Part 2 of 3 of reference/config-api/kubelet-config.v1beta1.md (split because the page is big). -->

## `KubeletConfiguration`     {#kubelet-config-k8s-io-v1beta1-KubeletConfiguration}
    


<p>KubeletConfiguration contains the configuration for the Kubelet</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>KubeletConfiguration</code></td></tr>
    
  
<tr><td><code>enableServer</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableServer enables Kubelet's secured server.
Note: Kubelet's insecure port is controlled by the readOnlyPort option.
Default: true</p>
</td>
</tr>
<tr><td><code>staticPodPath</code><br/>
<code>string</code>
</td>
<td>
   <p>staticPodPath is the path to the directory containing local (static) pods to
run, or the path to a single static pod file.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>podLogsDir</code><br/>
<code>string</code>
</td>
<td>
   <p>podLogsDir is a custom root directory path kubelet will use to place pod's log files.
Default: &quot;/var/log/pods/&quot;
Note: it is not recommended to use the temp folder as a log directory as it may cause
unexpected behavior in many places.</p>
</td>
</tr>
<tr><td><code>syncFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>syncFrequency is the max period between synchronizing running
containers and config.
Default: &quot;1m&quot;</p>
</td>
</tr>
<tr><td><code>fileCheckFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>fileCheckFrequency is the duration between checking config files for
new data.
Default: &quot;20s&quot;</p>
</td>
</tr>
<tr><td><code>httpCheckFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>httpCheckFrequency is the duration between checking http for new data.
Default: &quot;20s&quot;</p>
</td>
</tr>
<tr><td><code>staticPodURL</code><br/>
<code>string</code>
</td>
<td>
   <p>staticPodURL is the URL for accessing static pods to run.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>staticPodURLHeader</code><br/>
<code>map[string][]string</code>
</td>
<td>
   <p>staticPodURLHeader is a map of slices with HTTP headers to use when accessing the podURL.
Default: nil</p>
</td>
</tr>
<tr><td><code>address</code><br/>
<code>string</code>
</td>
<td>
   <p>address is the IP address for the Kubelet to serve on (set to 0.0.0.0
for all interfaces).
Default: &quot;0.0.0.0&quot;</p>
</td>
</tr>
<tr><td><code>port</code><br/>
<code>int32</code>
</td>
<td>
   <p>port is the port for the Kubelet to serve on.
The port number must be between 1 and 65535, inclusive.
Default: 10250</p>
</td>
</tr>
<tr><td><code>readOnlyPort</code><br/>
<code>int32</code>
</td>
<td>
   <p>readOnlyPort is the read-only port for the Kubelet to serve on with
no authentication/authorization.
The port number must be between 1 and 65535, inclusive.
Setting this field to 0 disables the read-only service.
Default: 0 (disabled)</p>
</td>
</tr>
<tr><td><code>tlsCertFile</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsCertFile is the file containing x509 Certificate for HTTPS. (CA cert,
if any, concatenated after server cert). If tlsCertFile and
tlsPrivateKeyFile are not provided, a self-signed certificate
and key are generated for the public address and saved to the directory
passed to the Kubelet's --cert-dir flag.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>tlsPrivateKeyFile</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsPrivateKeyFile is the file containing x509 private key matching tlsCertFile.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>tlsCipherSuites</code><br/>
<code>[]string</code>
</td>
<td>
   <p>tlsCipherSuites is the list of allowed cipher suites for the server.
Note that TLS 1.3 ciphersuites are not configurable.
Values are from tls package constants (https://golang.org/pkg/crypto/tls/#pkg-constants).
Default: nil</p>
</td>
</tr>
<tr><td><code>tlsMinVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsMinVersion is the minimum TLS version supported.
Values are from tls package constants (https://golang.org/pkg/crypto/tls/#pkg-constants).
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>rotateCertificates</code><br/>
<code>bool</code>
</td>
<td>
   <p>rotateCertificates enables client certificate rotation. The Kubelet will request a
new certificate from the certificates.k8s.io API. This requires an approver to approve the
certificate signing requests.
Default: false</p>
</td>
</tr>
<tr><td><code>serverTLSBootstrap</code><br/>
<code>bool</code>
</td>
<td>
   <p>serverTLSBootstrap enables server certificate bootstrap. Instead of self
signing a serving certificate, the Kubelet will request a certificate from
the 'certificates.k8s.io' API. This requires an approver to approve the
certificate signing requests (CSR). The RotateKubeletServerCertificate feature
must be enabled when setting this field.
Default: false</p>
</td>
</tr>
<tr><td><code>authentication</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletAuthentication"><code>KubeletAuthentication</code></a>
</td>
<td>
   <p>authentication specifies how requests to the Kubelet's server are authenticated.
Defaults:
anonymous:
enabled: false
webhook:
enabled: true
cacheTTL: &quot;2m&quot;</p>
</td>
</tr>
<tr><td><code>authorization</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletAuthorization"><code>KubeletAuthorization</code></a>
</td>
<td>
   <p>authorization specifies how requests to the Kubelet's server are authorized.
Defaults:
mode: Webhook
webhook:
cacheAuthorizedTTL: &quot;5m&quot;
cacheUnauthorizedTTL: &quot;30s&quot;</p>
</td>
</tr>
<tr><td><code>registryPullQPS</code><br/>
<code>int32</code>
</td>
<td>
   <p>registryPullQPS is the limit of registry pulls per second.
The value must not be a negative number.
Setting it to 0 means no limit.
Default: 5</p>
</td>
</tr>
<tr><td><code>registryBurst</code><br/>
<code>int32</code>
</td>
<td>
   <p>registryBurst is the maximum size of bursty pulls, temporarily allows
pulls to burst to this number, while still not exceeding registryPullQPS.
The value must not be a negative number.
Only used if registryPullQPS is greater than 0.
Default: 10</p>
</td>
</tr>
<tr><td><code>imagePullCredentialsVerificationPolicy</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ImagePullCredentialsVerificationPolicy"><code>ImagePullCredentialsVerificationPolicy</code></a>
</td>
<td>
   <p>imagePullCredentialsVerificationPolicy determines how credentials should be
verified when pod requests an image that is already present on the node:</p>
<ul>
<li>NeverVerify
<ul>
<li>anyone on a node can use any image present on the node</li>
</ul>
</li>
<li>NeverVerifyPreloadedImages
<ul>
<li>images that were pulled to the node by something else than the kubelet
can be used without reverifying pull credentials</li>
</ul>
</li>
<li>NeverVerifyAllowlistedImages
<ul>
<li>like &quot;NeverVerifyPreloadedImages&quot; but only node images from
<code>preloadedImagesVerificationAllowlist</code> don't require reverification</li>
</ul>
</li>
<li>AlwaysVerify
<ul>
<li>all images require credential reverification</li>
</ul>
</li>
</ul>
</td>
</tr>
<tr><td><code>preloadedImagesVerificationAllowlist</code><br/>
<code>[]string</code>
</td>
<td>
   <p>preloadedImagesVerificationAllowlist specifies a list of images that are
exempted from credential reverification for the &quot;NeverVerifyAllowlistedImages&quot;
<code>imagePullCredentialsVerificationPolicy</code>.
The list accepts a full path segment wildcard suffix &quot;/&ast;&quot;.
Only use image specs without an image tag or digest.</p>
</td>
</tr>
<tr><td><code>eventRecordQPS</code><br/>
<code>int32</code>
</td>
<td>
   <p>eventRecordQPS is the maximum event creations per second. If 0, there
is no limit enforced. The value cannot be a negative number.
Default: 50</p>
</td>
</tr>
<tr><td><code>eventBurst</code><br/>
<code>int32</code>
</td>
<td>
   <p>eventBurst is the maximum size of a burst of event creations, temporarily
allows event creations to burst to this number, while still not exceeding
eventRecordQPS. This field canot be a negative number and it is only used
when eventRecordQPS &gt; 0.
Default: 100</p>
</td>
</tr>
<tr><td><code>enableDebuggingHandlers</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableDebuggingHandlers enables server endpoints for log access
and local running of containers and commands, including the exec,
attach, logs, and portforward features.
Default: true</p>
</td>
</tr>
<tr><td><code>enableContentionProfiling</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableContentionProfiling enables block profiling, if enableDebuggingHandlers is true.
Default: false</p>
</td>
</tr>
<tr><td><code>healthzPort</code><br/>
<code>int32</code>
</td>
<td>
   <p>healthzPort is the port of the localhost healthz endpoint (set to 0 to disable).
A valid number is between 1 and 65535.
Default: 10248</p>
</td>
</tr>
<tr><td><code>healthzBindAddress</code><br/>
<code>string</code>
</td>
<td>
   <p>healthzBindAddress is the IP address for the healthz server to serve on.
Default: &quot;127.0.0.1&quot;</p>
</td>
</tr>
<tr><td><code>oomScoreAdj</code><br/>
<code>int32</code>
</td>
<td>
   <p>oomScoreAdj is The oom-score-adj value for kubelet process. Values
must be within the range [-1000, 1000].
Default: -999</p>
</td>
</tr>
<tr><td><code>clusterDomain</code><br/>
<code>string</code>
</td>
<td>
   <p>clusterDomain is the DNS domain for this cluster. If set, kubelet will
configure all containers to search this domain in addition to the
host's search domains.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>clusterDNS</code><br/>
<code>[]string</code>
</td>
<td>
   <p>clusterDNS is a list of IP addresses for the cluster DNS server. If set,
kubelet will configure all containers to use this for DNS resolution
instead of the host's DNS servers.
Default: nil</p>
</td>
</tr>
<tr><td><code>streamingConnectionIdleTimeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>streamingConnectionIdleTimeout is the maximum time a streaming connection
can be idle before the connection is automatically closed.
Default: &quot;4h&quot;</p>
</td>
</tr>
<tr><td><code>nodeStatusUpdateFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeStatusUpdateFrequency is the frequency that kubelet computes node
status. If node lease feature is not enabled, it is also the frequency that
kubelet posts node status to master.
Note: When node lease feature is not enabled, be cautious when changing the
constant, it must work with nodeMonitorGracePeriod in nodecontroller.
Default: &quot;10s&quot;</p>
</td>
</tr>
<tr><td><code>nodeStatusReportFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeStatusReportFrequency is the frequency that kubelet posts node
status to master if node status does not change. Kubelet will ignore this
frequency and post node status immediately if any change is detected. It is
only used when node lease feature is enabled. nodeStatusReportFrequency's
default value is 5m. But if nodeStatusUpdateFrequency is set explicitly,
nodeStatusReportFrequency's default value will be set to
nodeStatusUpdateFrequency for backward compatibility.
Default: &quot;5m&quot;</p>
</td>
</tr>
<tr><td><code>nodeLeaseDurationSeconds</code><br/>
<code>int32</code>
</td>
<td>
   <p>nodeLeaseDurationSeconds is the duration the Kubelet will set on its corresponding Lease.
NodeLease provides an indicator of node health by having the Kubelet create and
periodically renew a lease, named after the node, in the kube-node-lease namespace.
If the lease expires, the node can be considered unhealthy.
The lease is currently renewed every 10s, per KEP-0009. In the future, the lease renewal
interval may be set based on the lease duration.
The field value must be greater than 0.
Default: 40</p>
</td>
</tr>
<tr><td><code>imageMinimumGCAge</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>imageMinimumGCAge is the minimum age for an unused image before it is
garbage collected.
Default: &quot;2m&quot;</p>
</td>
</tr>
<tr><td><code>imageMaximumGCAge</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>imageMaximumGCAge is the maximum age an image can be unused before it is garbage collected.
The default of this field is &quot;0s&quot;, which disables this field--meaning images won't be garbage
collected based on being unused for too long.
Default: &quot;0s&quot; (disabled)</p>
</td>
</tr>
<tr><td><code>imageGCHighThresholdPercent</code><br/>
<code>int32</code>
</td>
<td>
   <p>imageGCHighThresholdPercent is the percent of disk usage after which
image garbage collection is always run. The percent is calculated by
dividing this field value by 100, so this field must be between 0 and
100, inclusive. When specified, the value must be greater than
imageGCLowThresholdPercent.
Default: 85</p>
</td>
</tr>
<tr><td><code>imageGCLowThresholdPercent</code><br/>
<code>int32</code>
</td>
<td>
   <p>imageGCLowThresholdPercent is the percent of disk usage before which
image garbage collection is never run. Lowest disk usage to garbage
collect to. The percent is calculated by dividing this field value by 100,
so the field value must be between 0 and 100, inclusive. When specified, the
value must be less than imageGCHighThresholdPercent.
Default: 80</p>
</td>
</tr>
<tr><td><code>volumeStatsAggPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>volumeStatsAggPeriod is the frequency for calculating and caching volume
disk usage for all pods.
Default: &quot;1m&quot;</p>
</td>
</tr>
<tr><td><code>kubeletCgroups</code><br/>
<code>string</code>
</td>
<td>
   <p>kubeletCgroups is the absolute name of cgroups to isolate the kubelet in
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>systemCgroups</code><br/>
<code>string</code>
</td>
<td>
   <p>systemCgroups is absolute name of cgroups in which to place
all non-kernel processes that are not already in a container. Empty
for no container. Rolling back the flag requires a reboot.
The cgroupRoot must be specified if this field is not empty.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>cgroupRoot</code><br/>
<code>string</code>
</td>
<td>
   <p>cgroupRoot is the root cgroup to use for pods. This is handled by the
container runtime on a best effort basis.</p>
</td>
</tr>
<tr><td><code>cgroupsPerQOS</code><br/>
<code>bool</code>
</td>
<td>
   <p>cgroupsPerQOS enable QoS based CGroup hierarchy: top level CGroups for QoS classes
and all Burstable and BestEffort Pods are brought up under their specific top level
QoS CGroup.
Default: true</p>
</td>
</tr>
<tr><td><code>cgroupDriver</code><br/>
<code>string</code>
</td>
<td>
   <p>cgroupDriver is the driver kubelet uses to manipulate CGroups on the host (cgroupfs
or systemd).
Default: &quot;cgroupfs&quot;</p>
</td>
</tr>
<tr><td><code>cpuManagerPolicy</code><br/>
<code>string</code>
</td>
<td>
   <p>cpuManagerPolicy is the name of the policy to use.
Default: &quot;None&quot;</p>
</td>
</tr>
<tr><td><code>singleProcessOOMKill</code><br/>
<code>bool</code>
</td>
<td>
   <p>singleProcessOOMKill, if true, will prevent the <code>memory.oom.group</code> flag from being set for container
cgroups in cgroups v2. This causes processes in the container to be OOM killed individually instead of as
a group. It means that if true, the behavior aligns with the behavior of cgroups v1.
The default value is determined automatically when you don't specify.
On non-linux such as windows, only null / absent is allowed.
On cgroup v1 linux, only null / absent and true are allowed.
On cgroup v2 linux, null / absent, true and false are allowed. The default value is false.</p>
</td>
</tr>
<tr><td><code>cpuManagerPolicyOptions</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>cpuManagerPolicyOptions is a set of key=value which 	allows to set extra options
to fine tune the behaviour of the cpu manager policies.
Default: nil</p>
</td>
</tr>
<tr><td><code>cpuManagerReconcilePeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cpuManagerReconcilePeriod is the reconciliation period for the CPU Manager.
Default: &quot;10s&quot;</p>
</td>
</tr>
<tr><td><code>memoryManagerPolicy</code><br/>
<code>string</code>
</td>
<td>
   <p>memoryManagerPolicy is the name of the policy to use by memory manager.
Requires the MemoryManager feature gate to be enabled.
Default: &quot;none&quot;</p>
</td>
</tr>
<tr><td><code>topologyManagerPolicy</code><br/>
<code>string</code>
</td>
<td>
   <p>topologyManagerPolicy is the name of the topology manager policy to use.
Valid values include:</p>
<ul>
<li><code>restricted</code>: kubelet only allows pods with optimal NUMA node alignment for
requested resources;</li>
<li><code>best-effort</code>: kubelet will favor pods with NUMA alignment of CPU and device
resources;</li>
<li><code>none</code>: kubelet has no knowledge of NUMA alignment of a pod's CPU and device resources.</li>
<li><code>single-numa-node</code>: kubelet only allows pods with a single NUMA alignment
of CPU and device resources.</li>
</ul>
<p>Default: &quot;none&quot;</p>
</td>
</tr>
<tr><td><code>topologyManagerScope</code><br/>
<code>string</code>
</td>
<td>
   <p>topologyManagerScope represents the scope of topology hint generation
that topology manager requests and hint providers generate. Valid values include:</p>
<ul>
<li><code>container</code>: topology policy is applied on a per-container basis.</li>
<li><code>pod</code>: topology policy is applied on a per-pod basis.</li>
</ul>
<p>Default: &quot;container&quot;</p>
</td>
</tr>
<tr><td><code>topologyManagerPolicyOptions</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>TopologyManagerPolicyOptions is a set of key=value which allows to set extra options
to fine tune the behaviour of the topology manager policies.
Requires  both the &quot;TopologyManager&quot; and &quot;TopologyManagerPolicyOptions&quot; feature gates to be enabled.
Default: nil</p>
</td>
</tr>
<tr><td><code>qosReserved</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>qosReserved is a set of resource name to percentage pairs that specify
the minimum percentage of a resource reserved for exclusive use by the
guaranteed QoS tier.
Currently supported resources: &quot;memory&quot;
Requires the QOSReserved feature gate to be enabled.
Default: nil</p>
</td>
</tr>
<tr><td><code>runtimeRequestTimeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>runtimeRequestTimeout is the timeout for all runtime requests except long running
requests - pull, logs, exec and attach.
Default: &quot;2m&quot;</p>
</td>
</tr>
<tr><td><code>hairpinMode</code><br/>
<code>string</code>
</td>
<td>
   <p>hairpinMode specifies how the Kubelet should configure the container
bridge for hairpin packets.
Setting this flag allows endpoints in a Service to loadbalance back to
themselves if they should try to access their own Service. Values:</p>
<ul>
<li>&quot;promiscuous-bridge&quot;: make the container bridge promiscuous.</li>
<li>&quot;hairpin-veth&quot;:       set the hairpin flag on container veth interfaces.</li>
<li>&quot;none&quot;:               do nothing.</li>
</ul>
<p>Generally, one must set <code>--hairpin-mode=hairpin-veth to</code> achieve hairpin NAT,
because promiscuous-bridge assumes the existence of a container bridge named cbr0.
Default: &quot;promiscuous-bridge&quot;</p>
</td>
</tr>
<tr><td><code>maxPods</code><br/>
<code>int32</code>
</td>
<td>
   <p>maxPods is the maximum number of Pods that can run on this Kubelet.
The value must be a non-negative integer.
Default: 110</p>
</td>
</tr>
<tr><td><code>podCIDR</code><br/>
<code>string</code>
</td>
<td>
   <p>podCIDR is the CIDR to use for pod IP addresses, only used in standalone mode.
In cluster mode, this is obtained from the control plane.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>podPidsLimit</code><br/>
<code>int64</code>
</td>
<td>
   <p>podPidsLimit is the maximum number of PIDs in any pod.
Default: -1</p>
</td>
</tr>
<tr><td><code>resolvConf</code><br/>
<code>string</code>
</td>
<td>
   <p>resolvConf is the resolver configuration file used as the basis
for the container DNS resolution configuration.
If set to the empty string, will override the default and effectively disable DNS lookups.
Default: &quot;/etc/resolv.conf&quot;</p>
</td>
</tr>
<tr><td><code>runOnce</code><br/>
<code>bool</code>
</td>
<td>
   <p>runOnce causes the Kubelet to check the API server once for pods,
run those in addition to the pods specified by static pod files, and exit.
Default: false</p>
</td>
</tr>
<tr><td><code>cpuCFSQuota</code><br/>
<code>bool</code>
</td>
<td>
   <p>cpuCFSQuota enables CPU CFS quota enforcement for containers that
specify CPU limits.
Default: true</p>
</td>
</tr>
<tr><td><code>cpuCFSQuotaPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cpuCFSQuotaPeriod is the CPU CFS quota period value, <code>cpu.cfs_period_us</code>.
The value must be between 1 ms and 1 second, inclusive.
Requires the CustomCPUCFSQuotaPeriod feature gate to be enabled.
Default: &quot;100ms&quot;</p>
</td>
</tr>
<tr><td><code>nodeStatusMaxImages</code><br/>
<code>int32</code>
</td>
<td>
   <p>nodeStatusMaxImages caps the number of images reported in Node.status.images.
The value must be greater than -2.
Note: If -1 is specified, no cap will be applied. If 0 is specified, no image is returned.
Default: 50</p>
</td>
</tr>
<tr><td><code>maxOpenFiles</code><br/>
<code>int64</code>
</td>
<td>
   <p>maxOpenFiles is Number of files that can be opened by Kubelet process.
The value must be a non-negative number.
Default: 1000000</p>
</td>
</tr>
<tr><td><code>contentType</code><br/>
<code>string</code>
</td>
<td>
   <p>contentType is contentType of requests sent to apiserver.
Default: &quot;application/vnd.kubernetes.protobuf&quot;</p>
</td>
</tr>
<tr><td><code>kubeAPIQPS</code><br/>
<code>int32</code>
</td>
<td>
   <p>kubeAPIQPS is the QPS to use while talking with kubernetes apiserver.
Default: 50</p>
</td>
</tr>
<tr><td><code>kubeAPIBurst</code><br/>
<code>int32</code>
</td>
<td>
   <p>kubeAPIBurst is the burst to allow while talking with kubernetes API server.
This field cannot be a negative number.
Default: 100</p>
</td>
</tr>
<tr><td><code>serializeImagePulls</code><br/>
<code>bool</code>
</td>
<td>
   <p>serializeImagePulls when enabled, tells the Kubelet to pull images one
at a time. We recommend <em>not</em> changing the default value on nodes that
run docker daemon with version  &lt; 1.9 or an Aufs storage backend.
Issue #10959 has more details.
Default: true</p>
</td>
</tr>
<tr><td><code>maxParallelImagePulls</code><br/>
<code>int32</code>
</td>
<td>
   <p>MaxParallelImagePulls sets the maximum number of image pulls in parallel.
This field cannot be set if SerializeImagePulls is true.
Setting it to nil means no limit.
Default: nil</p>
</td>
</tr>
<tr><td><code>evictionHard</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionHard is a map of signal names to quantities that defines hard eviction
thresholds. For example: <code>{&quot;memory.available&quot;: &quot;300Mi&quot;}</code>.
To explicitly disable, pass a 0% or 100% threshold on an arbitrary resource.
Default:
memory.available:  &quot;100Mi&quot;
nodefs.available:  &quot;10%&quot;
nodefs.inodesFree: &quot;5%&quot;
imagefs.available: &quot;15%&quot;</p>
</td>
</tr>
<tr><td><code>evictionSoft</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionSoft is a map of signal names to quantities that defines soft eviction thresholds.
For example: <code>{&quot;memory.available&quot;: &quot;300Mi&quot;}</code>.
Default: nil</p>
</td>
</tr>
<tr><td><code>evictionSoftGracePeriod</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionSoftGracePeriod is a map of signal names to quantities that defines grace
periods for each soft eviction signal. For example: <code>{&quot;memory.available&quot;: &quot;30s&quot;}</code>.
Default: nil</p>
</td>
</tr>
<tr><td><code>evictionPressureTransitionPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>evictionPressureTransitionPeriod is the duration for which the kubelet has to wait
before transitioning out of an eviction pressure condition.
A duration of 0s will be converted to the default value of 5m
Default: &quot;5m&quot;</p>
</td>
</tr>
<tr><td><code>evictionMaxPodGracePeriod</code><br/>
<code>int32</code>
</td>
<td>
   <p>evictionMaxPodGracePeriod is the maximum allowed grace period (in seconds) to use
when terminating pods in response to a soft eviction threshold being met. This value
effectively caps the Pod's terminationGracePeriodSeconds value during soft evictions.
Default: 0</p>
</td>
</tr>
<tr><td><code>evictionMinimumReclaim</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionMinimumReclaim is a map of signal names to quantities that defines minimum reclaims,
which describe the minimum amount of a given resource the kubelet will reclaim when
performing a pod eviction while that resource is under pressure.
For example: <code>{&quot;imagefs.available&quot;: &quot;2Gi&quot;}</code>.
Default: nil</p>
</td>
</tr>
<tr><td><code>mergeDefaultEvictionSettings</code><br/>
<code>bool</code>
</td>
<td>
   <p>mergeDefaultEvictionSettings indicates that defaults for the evictionHard, evictionSoft, evictionSoftGracePeriod, and evictionMinimumReclaim
fields should be merged into values specified for those fields in this configuration.
Signals specified in this configuration take precedence.
Signals not specified in this configuration inherit their defaults.
If false, and if any signal is specified in this configuration then other signals that
are not specified in this configuration will be set to 0.
It applies to merging the fields for which the default exists, and currently only evictionHard has default values.
Default: false</p>
</td>
</tr>
<tr><td><code>podsPerCore</code><br/>
<code>int32</code>
</td>
<td>
   <p>podsPerCore is the maximum number of pods per core. Cannot exceed maxPods.
The value must be a non-negative integer.
If 0, there is no limit on the number of Pods.
Default: 0</p>
</td>
</tr>
<tr><td><code>enableControllerAttachDetach</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableControllerAttachDetach enables the Attach/Detach controller to
manage attachment/detachment of volumes scheduled to this node, and
disables kubelet from executing any attach/detach operations.
Note: attaching/detaching CSI volumes is not supported by the kubelet,
so this option needs to be true for that use case.
Default: true</p>
</td>
</tr>
<tr><td><code>protectKernelDefaults</code><br/>
<code>bool</code>
</td>
<td>
   <p>protectKernelDefaults, if true, causes the Kubelet to error if kernel
flags are not as it expects. Otherwise the Kubelet will attempt to modify
kernel flags to match its expectation.
Default: false</p>
</td>
</tr>
<tr><td><code>makeIPTablesUtilChains</code><br/>
<code>bool</code>
</td>
<td>
   <p>makeIPTablesUtilChains, if true, causes the Kubelet to create the
KUBE-IPTABLES-HINT chain in iptables as a hint to other components about the
configuration of iptables on the system.
Default: true</p>
</td>
</tr>
<tr><td><code>iptablesMasqueradeBit</code><br/>
<code>int32</code>
</td>
<td>
   <p>iptablesMasqueradeBit formerly controlled the creation of the KUBE-MARK-MASQ
chain.
Deprecated: no longer has any effect.
Default: 14</p>
</td>
</tr>
<tr><td><code>iptablesDropBit</code><br/>
<code>int32</code>
</td>
<td>
   <p>iptablesDropBit formerly controlled the creation of the KUBE-MARK-DROP chain.
Deprecated: no longer has any effect.
Default: 15</p>
</td>
</tr>
<tr><td><code>featureGates</code><br/>
<code>map[string]bool</code>
</td>
<td>
   <p>featureGates is a map of feature names to bools that enable or disable experimental
features. This field modifies piecemeal the built-in default values from
&quot;k8s.io/kubernetes/pkg/features/kube_features.go&quot;.
Default: nil</p>
</td>
</tr>
<tr><td><code>failSwapOn</code><br/>
<code>bool</code>
</td>
<td>
   <p>failSwapOn tells the Kubelet to fail to start if swap is enabled on the node.
Default: true</p>
</td>
</tr>
<tr><td><code>memorySwap</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-MemorySwapConfiguration"><code>MemorySwapConfiguration</code></a>
</td>
<td>
   <p>memorySwap configures swap memory available to container workloads.</p>
</td>
</tr>
<tr><td><code>containerLogMaxSize</code><br/>
<code>string</code>
</td>
<td>
   <p>containerLogMaxSize is a quantity defining the maximum size of the container log
file before it is rotated. For example: &quot;5Mi&quot; or &quot;256Ki&quot;.
Default: &quot;10Mi&quot;</p>
</td>
</tr>
<tr><td><code>containerLogMaxFiles</code><br/>
<code>int32</code>
</td>
<td>
   <p>containerLogMaxFiles specifies the maximum number of container log files that can
be present for a container.
Default: 5</p>
</td>
</tr>
<tr><td><code>containerLogMaxWorkers</code><br/>
<code>int32</code>
</td>
<td>
   <p>ContainerLogMaxWorkers specifies the maximum number of concurrent workers to spawn
for performing the log rotate operations. Set this count to 1 for disabling the
concurrent log rotation workflows
Default: 1</p>
</td>
</tr>
<tr><td><code>containerLogMonitorInterval</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>ContainerLogMonitorInterval specifies the duration at which the container logs are monitored
for performing the log rotate operation. This defaults to 10 * time.Seconds. But can be
customized to a smaller value based on the log generation rate and the size required to be
rotated against
Default: 10s</p>
</td>
</tr>
<tr><td><code>configMapAndSecretChangeDetectionStrategy</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ResourceChangeDetectionStrategy"><code>ResourceChangeDetectionStrategy</code></a>
</td>
<td>
   <p>configMapAndSecretChangeDetectionStrategy is a mode in which ConfigMap and Secret
managers are running. Valid values include:</p>
<ul>
<li><code>Get</code>: kubelet fetches necessary objects directly from the API server;</li>
<li><code>Cache</code>: kubelet uses TTL cache for object fetched from the API server;</li>
<li><code>Watch</code>: kubelet uses watches to observe changes to objects that are in its interest.</li>
</ul>
<p>Default: &quot;Watch&quot;</p>
</td>
</tr>
<tr><td><code>systemReserved</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>systemReserved is a set of ResourceName=ResourceQuantity (e.g. cpu=200m,memory=150G)
pairs that describe resources reserved for non-kubernetes components.
Currently only cpu and memory are supported.
See https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources for more detail.
Default: nil</p>
</td>
</tr>
<tr><td><code>kubeReserved</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>kubeReserved is a set of ResourceName=ResourceQuantity (e.g. cpu=200m,memory=150G) pairs
that describe resources reserved for kubernetes system components.
Currently cpu, memory and local storage for root file system are supported.
See https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources
for more details.
Default: nil</p>
</td>
</tr>
<tr><td><code>reservedSystemCPUs</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>The reservedSystemCPUs option specifies the CPU list reserved for the host
level system threads and kubernetes related threads. This provide a &quot;static&quot;
CPU list rather than the &quot;dynamic&quot; list by systemReserved and kubeReserved.
This option does not support systemReservedCgroup or kubeReservedCgroup.</p>
</td>
</tr>
<tr><td><code>showHiddenMetricsForVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>showHiddenMetricsForVersion is the previous version for which you want to show
hidden metrics.
Only the previous minor version is meaningful, other values will not be allowed.
The format is <code>&lt;major&gt;.&lt;minor&gt;</code>, e.g.: <code>1.16</code>.
The purpose of this format is make sure you have the opportunity to notice
if the next release hides additional metrics, rather than being surprised
when they are permanently removed in the release after that.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>systemReservedCgroup</code><br/>
<code>string</code>
</td>
<td>
   <p>systemReservedCgroup helps the kubelet identify absolute name of top level CGroup used
to enforce <code>systemReserved</code> compute resource reservation for OS system daemons.
Refer to <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">Node Allocatable</a>
doc for more information.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>kubeReservedCgroup</code><br/>
<code>string</code>
</td>
<td>
   <p>kubeReservedCgroup helps the kubelet identify absolute name of top level CGroup used
to enforce <code>KubeReserved</code> compute resource reservation for Kubernetes node system daemons.
Refer to <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">Node Allocatable</a>
doc for more information.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>enforceNodeAllocatable</code><br/>
<code>[]string</code>
</td>
<td>
   <p>This flag specifies the various Node Allocatable enforcements that Kubelet needs to perform.
This flag accepts a list of options. Acceptable options are <code>none</code>, <code>pods</code>,
<code>system-reserved</code> and <code>kube-reserved</code>.
If <code>none</code> is specified, no other options may be specified.
When <code>system-reserved</code> is in the list, systemReservedCgroup must be specified.
When <code>kube-reserved</code> is in the list, kubeReservedCgroup must be specified.
This field is supported only when <code>cgroupsPerQOS</code> is set to true.
Refer to <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">Node Allocatable</a>
for more information.
Default: [&quot;pods&quot;]</p>
</td>
</tr>
<tr><td><code>allowedUnsafeSysctls</code><br/>
<code>[]string</code>
</td>
<td>
   <p>A comma separated whitelist of unsafe sysctls or sysctl patterns (ending in <code>*</code>).
Unsafe sysctl groups are <code>kernel.shm*</code>, <code>kernel.msg*</code>, <code>kernel.sem</code>, <code>fs.mqueue.*</code>,
and <code>net.*</code>. For example: &quot;<code>kernel.msg*,net.ipv4.route.min_pmtu</code>&quot;
Default: []</p>
</td>
</tr>
<tr><td><code>volumePluginDir</code><br/>
<code>string</code>
</td>
<td>
   <p>volumePluginDir is the full path of the directory in which to search
for additional third party volume plugins.
Default: &quot;/usr/libexec/kubernetes/kubelet-plugins/volume/exec/&quot;</p>
</td>
</tr>
<tr><td><code>providerID</code><br/>
<code>string</code>
</td>
<td>
   <p>providerID, if set, sets the unique ID of the instance that an external
provider (i.e. cloudprovider) can use to identify a specific node.
Default: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>kernelMemcgNotification</code><br/>
<code>bool</code>
</td>
<td>
   <p>kernelMemcgNotification, if set, instructs the kubelet to integrate with the
kernel memcg notification for determining if memory eviction thresholds are
exceeded rather than polling.
Default: false</p>
</td>
</tr>
<tr><td><code>logging</code> <B>[Required]</B><br/>
<a href="#LoggingConfiguration"><code>LoggingConfiguration</code></a>
</td>
<td>
   <p>logging specifies the options of logging.
Refer to <a href="https://github.com/kubernetes/component-base/blob/master/logs/options.go">Logs Options</a>
for more information.
Default:
Format: text</p>
</td>
</tr>
<tr><td><code>enableSystemLogHandler</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableSystemLogHandler enables system logs via web interface host:port/logs/
Default: true</p>
</td>
</tr>
<tr><td><code>enableSystemLogQuery</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableSystemLogQuery enables the node log query feature on the /logs endpoint.
EnableSystemLogHandler has to be enabled in addition for this feature to work.
Enabling this feature has security implications. The recommendation is to enable it on a need basis for debugging
purposes and disabling otherwise.
Default: false</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>shutdownGracePeriod specifies the total duration that the node should delay the
shutdown and total grace period for pod termination during a node shutdown.
Default: &quot;0s&quot;</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriodCriticalPods</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>shutdownGracePeriodCriticalPods specifies the duration used to terminate critical
pods during a node shutdown. This should be less than shutdownGracePeriod.
For example, if shutdownGracePeriod=30s, and shutdownGracePeriodCriticalPods=10s,
during a node shutdown the first 20 seconds would be reserved for gracefully
terminating normal pods, and the last 10 seconds would be reserved for terminating
critical pods.
Default: &quot;0s&quot;</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriodByPodPriority</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ShutdownGracePeriodByPodPriority"><code>[]ShutdownGracePeriodByPodPriority</code></a>
</td>
<td>
   <p>shutdownGracePeriodByPodPriority specifies the shutdown grace period for Pods based
on their associated priority class value.
When a shutdown request is received, the Kubelet will initiate shutdown on all pods
running on the node with a grace period that depends on the priority of the pod,
and then wait for all pods to exit.
Each entry in the array represents the graceful shutdown time a pod with a priority
class value that lies in the range of that value and the next higher entry in the
list when the node is shutting down.
For example, to allow critical pods 10s to shutdown, priority&gt;=10000 pods 20s to
shutdown, and all remaining pods 30s to shutdown.</p>
<p>shutdownGracePeriodByPodPriority:</p>
<ul>
<li>priority: 2000000000
shutdownGracePeriodSeconds: 10</li>
<li>priority: 10000
shutdownGracePeriodSeconds: 20</li>
<li>priority: 0
shutdownGracePeriodSeconds: 30</li>
</ul>
<p>The time the Kubelet will wait before exiting will at most be the maximum of all
shutdownGracePeriodSeconds for each priority class range represented on the node.
When all pods have exited or reached their grace periods, the Kubelet will release
the shutdown inhibit lock.
Requires the GracefulNodeShutdown feature gate to be enabled.
This configuration must be empty if either ShutdownGracePeriod or ShutdownGracePeriodCriticalPods is set.
Default: nil</p>
</td>
</tr>
<tr><td><code>crashLoopBackOff</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-CrashLoopBackOffConfig"><code>CrashLoopBackOffConfig</code></a>
</td>
<td>
   <p>CrashLoopBackOff contains config to modify node-level parameters for
container restart behavior</p>
</td>
</tr>
<tr><td><code>reservedMemory</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-MemoryReservation"><code>[]MemoryReservation</code></a>
</td>
<td>
   <p>reservedMemory specifies a comma-separated list of memory reservations for NUMA nodes.
The parameter makes sense only in the context of the memory manager feature.
The memory manager will not allocate reserved memory for container workloads.
For example, if you have a NUMA0 with 10Gi of memory and the reservedMemory was
specified to reserve 1Gi of memory at NUMA0, the memory manager will assume that
only 9Gi is available for allocation.
You can specify a different amount of NUMA node and memory types.
You can omit this parameter at all, but you should be aware that the amount of
reserved memory from all NUMA nodes should be equal to the amount of memory specified
by the <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">node allocatable</a>.
If at least one node allocatable parameter has a non-zero value, you will need
to specify at least one NUMA node.
Also, avoid specifying:</p>
<ol>
<li>Duplicates, the same NUMA node, and memory type, but with a different value.</li>
<li>zero limits for any memory type.</li>
<li>NUMAs nodes IDs that do not exist under the machine.</li>
<li>memory types except for memory and hugepages-<!-- raw HTML omitted --></li>
</ol>
<p>Default: nil</p>
</td>
</tr>
<tr><td><code>enableProfilingHandler</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableProfilingHandler enables profiling via web interface host:port/debug/pprof/
Default: true</p>
</td>
</tr>
<tr><td><code>enableDebugFlagsHandler</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableDebugFlagsHandler enables flags endpoint via web interface host:port/debug/flags/v
Default: true</p>
</td>
</tr>
<tr><td><code>seccompDefault</code><br/>
<code>bool</code>
</td>
<td>
   <p>SeccompDefault enables the use of <code>RuntimeDefault</code> as the default seccomp profile for all workloads.
Default: false</p>
</td>
</tr>
<tr><td><code>memoryThrottlingFactor</code><br/>
<code>float64</code>
</td>
<td>
   <p>MemoryThrottlingFactor specifies the factor multiplied by the memory limit or node allocatable memory
when setting the cgroupv2 memory.high value to enforce MemoryQoS.
Decreasing this factor will set lower high limit for container cgroups and put heavier reclaim pressure
while increasing will put less reclaim pressure.
See https://kep.k8s.io/2570 for more details.
Default: 0.9</p>
</td>
</tr>
<tr><td><code>registerWithTaints</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#taint-v1-core"><code>[]core/v1.Taint</code></a>
</td>
<td>
   <p>registerWithTaints are an array of taints to add to a node object when
the kubelet registers itself. This only takes effect when registerNode
is true and upon the initial registration of the node.
Default: nil</p>
</td>
</tr>
<tr><td><code>registerNode</code><br/>
<code>bool</code>
</td>
<td>
   <p>registerNode enables automatic registration with the apiserver.
Default: true</p>
</td>
</tr>
<tr><td><code>tracing</code><br/>
<a href="#TracingConfiguration"><code>TracingConfiguration</code></a>
</td>
<td>
   <p>Tracing specifies the versioned configuration for OpenTelemetry tracing clients.
See https://kep.k8s.io/2832 for more details.
Default: nil</p>
</td>
</tr>
<tr><td><code>localStorageCapacityIsolation</code><br/>
<code>bool</code>
</td>
<td>
   <p>LocalStorageCapacityIsolation enables local ephemeral storage isolation feature. The default setting is true.
This feature allows users to set request/limit for container's ephemeral storage and manage it in a similar way
as cpu and memory. It also allows setting sizeLimit for emptyDir volume, which will trigger pod eviction if disk
usage from the volume exceeds the limit.
This feature depends on the capability of detecting correct root file system disk usage. For certain systems,
such as kind rootless, if this capability cannot be supported, the feature LocalStorageCapacityIsolation should be
disabled. Once disabled, user should not set request/limit for container's ephemeral storage, or sizeLimit for emptyDir.
Default: true</p>
</td>
</tr>
<tr><td><code>containerRuntimeEndpoint</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>ContainerRuntimeEndpoint is the endpoint of container runtime.
Unix Domain Sockets are supported on Linux, while npipe and tcp endpoints are supported on Windows.
Examples:'unix:///path/to/runtime.sock', 'npipe:////./pipe/runtime'</p>
</td>
</tr>
<tr><td><code>imageServiceEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>ImageServiceEndpoint is the endpoint of container image service.
Unix Domain Socket are supported on Linux, while npipe and tcp endpoints are supported on Windows.
Examples:'unix:///path/to/runtime.sock', 'npipe:////./pipe/runtime'.
If not specified, the value in containerRuntimeEndpoint is used.</p>
</td>
</tr>
<tr><td><code>failCgroupV1</code><br/>
<code>bool</code>
</td>
<td>
   <p>FailCgroupV1 prevents the kubelet from starting on hosts
that use cgroup v1. By default, this is set to 'false', meaning
the kubelet is allowed to start on cgroup v1 hosts unless this
option is explicitly enabled.
Default: false</p>
</td>
</tr>
<tr><td><code>userNamespaces</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-UserNamespaces"><code>UserNamespaces</code></a>
</td>
<td>
   <p>UserNamespaces contains User Namespace configurations.</p>
</td>
</tr>
</tbody>
</table>
