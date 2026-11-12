<!-- Part 2 of 4 of reference/command-line-tools-reference/kubelet.md (split because the page is big). -->

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0 </td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The IP address for the kubelet to serve on (set to <code>0.0.0.0</code> or <code>::</code> for listening on all interfaces and IP address families)  (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--allowed-unsafe-sysctls strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Comma-separated whitelist of unsafe sysctls or unsafe sysctl patterns (ending in <code>&ast;</code>). Use these at your own risk. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--anonymous-auth&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enables anonymous requests to the kubelet server. Requests that are not rejected by another authentication method are treated as anonymous requests. Anonymous requests have a username of <code>system:anonymous</code>, and a group name of <code>system:unauthenticated</code>. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Use the <code>TokenReview</code> API to determine authentication for bearer tokens. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-cache-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>2m0s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The duration to cache responses from the webhook token authenticator. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--authorization-mode string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>AlwaysAllow</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Authorization mode for kubelet server. Valid options are &quot;<code>AlwaysAllow</code>&quot; or &quot;<code>Webhook</code>&quot;. Webhook mode uses the <code>SubjectAccessReview</code> API to determine authorization. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-authorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>5m0s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The duration to cache 'authorized' responses from the webhook authorizer. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-unauthorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>30s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The duration to cache 'unauthorized' responses from the webhook authorizer. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--bootstrap-kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Path to a kubeconfig file that will be used to get client certificate for kubelet. If the file specified by <code>--kubeconfig</code> does not exist, the bootstrap kubeconfig is used to request a client certificate from the API server. On success, a kubeconfig file referencing the generated client certificate and key is written to the path specified by <code>--kubeconfig</code>. The client certificate and key file will be stored in the directory pointed by <code>--cert-dir</code>.</td>
</tr>

<tr>
<td colspan="2">--cert-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>/var/lib/kubelet/pki</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The directory where the TLS certs are located. If <code>--tls-cert-file</code> and <code>--tls-private-key-file</code> are provided, this flag will be ignored.</td>
</tr>

<tr>
<td colspan="2">--cgroup-driver string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>cgroupfs</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Driver that the kubelet uses to manipulate cgroups on the host.  Possible values: &quot;<code>cgroupfs</code>&quot;, &quot;<code>systemd</code>&quot;. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cgroup-root string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>''</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Optional root cgroup to use for pods. This is handled by the container runtime on a best effort basis. Default: '', which means use the container runtime default. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cgroups-per-qos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enable creation of QoS cgroup hierarchy, if true, top level QoS and pod cgroups are created. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">If set, any request presenting a client certificate signed by one of the authorities in the client-ca-file is authenticated with an identity corresponding to the <code>CommonName</code> of the client certificate. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cloud-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The path to the cloud provider configuration file. Empty string for no configuration file. (DEPRECATED: will be removed in 1.25 or later, in favor of removing cloud providers code from kubelet.)</td>
</tr>

<tr>
<td colspan="2">--cloud-provider string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The provider for cloud services. Set to empty string for running with no cloud provider. Set to 'external' for running with an external cloud provider. If set, the cloud provider determines the name of the node (consult cloud provider documentation to determine if and how the hostname is used).</td>
</tr>

<tr>
<td colspan="2">--cluster-dns strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Comma-separated list of DNS server IP address. This value is used for containers DNS server in case of Pods with "<code>dnsPolicy: ClusterFirst</code>".<br/><B>Note:</B> all DNS servers appearing in the list MUST serve the same set of records otherwise name resolution within the cluster may not work correctly. There is no guarantee as to which DNS server may be contacted for name resolution. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cluster-domain string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Domain for this cluster. If set, kubelet will configure all containers to search this domain in addition to the host's search domains. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The kubelet will load its initial configuration from this file. The path may be absolute or relative; relative paths start at the kubelet's current working directory. Omit this flag to use the built-in default configuration values. Command-line flags override configuration from this file.</td>
</tr>

<tr>
<td colspan="2">--config-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: ''</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Path to a directory to specify drop-ins, allows the user to optionally specify additional configs to overwrite what is provided by default and in the `--config` flag.<br/><B>Note</B>: Set the '<code>KUBELET_CONFIG_DROPIN_DIR_ALPHA</code>' environment variable to specify the directory.</td>
</tr>

<tr>
<td colspan="2">--container-log-max-files int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">&lt;Warning: Beta feature&gt; Set the maximum number of container log files that can be present for a container. The number must be &gt;= 2. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--container-log-max-size string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>10Mi</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">&lt;Warning: Beta feature&gt; Set the maximum size (e.g. <code>10Mi</code>) of container log file before it is rotated.  (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--container-runtime-endpoint string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>"unix:///run/containerd/containerd.sock"</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The endpoint of remote runtime service. UNIX domain sockets are supported on Linux, while 'npipe' and 'tcp' endpoints are supported on windows. Examples: <code>'unix:///path/to/runtime.sock'</code>, <code>'npipe:////./pipe/runtime'</code>. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--contention-profiling</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enable block profiling, if profiling is enabled. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cpu-cfs-quota&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enable CPU CFS quota enforcement for containers that specify CPU limits. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cpu-cfs-quota-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>100ms</code></td>
   </tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Sets CPU CFS quota period value, <code>cpu.cfs_period_us</code>, defaults to Linux Kernel default. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cpu-manager-policy string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>none</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The CPU manager policy to use. Possible values: &quot;<code>none</code>&quot;, &quot;<code>static</code>&quot;. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cpu-manager-policy-options string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of 'key=value' CPU manager policy options to use, to fine tune their behaviour. If not supplied, keep the default behaviour. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--cpu-manager-reconcile-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>10s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">&lt;Warning: Alpha feature&gt; CPU manager reconciliation period. Examples: &quot;<code>10s</code>&quot;, or &quot;<code>1m</code>&quot;. If not supplied, defaults to node status update frequency. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--enable-controller-attach-detach&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enables the Attach/Detach controller to manage attachment/detachment of volumes scheduled to this node, and disables kubelet from executing any attach/detach operations. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--enable-debugging-handlers&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enables server endpoints for log collection and local running of containers and commands. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--enable-server&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Enable the kubelet's server. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--enforce-node-allocatable strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>pods</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A comma separated list of levels of node allocatable enforcement to be enforced by kubelet. Acceptable options are &quot;<code>none</code>&quot;, &quot;<code>pods</code>&quot;, &quot;<code>system-reserved</code>&quot;, and &quot;<code>kube-reserved</code>&quot;. If the latter two options are specified, <code>--system-reserved-cgroup</code> and <code>--kube-reserved-cgroup</code> must also be set, respectively. If &quot;<code>none</code>&quot; is specified, no additional options should be set. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/">official documentation</a> for more details. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--event-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Maximum size of a bursty event records, temporarily allows event records to burst to this number, while still not exceeding <code>--event-qps</code>. The number must be &gt;= 0. If 0 will use default burst (100). (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--event-qps int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">QPS to limit event creations. The number must be &gt;= 0. If 0 will use default QPS (50). (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--eviction-hard strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>imagefs.available<15%,memory.available<100Mi,nodefs.available<10%</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of eviction thresholds (e.g. &quot;<code>memory.available<1Gi</code>&quot;) that if met would trigger a pod eviction. On a Linux node, the default value also includes &quot;<code>nodefs.inodesFree<5%</code>&quot;. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--eviction-max-pod-grace-period int32</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"> Maximum allowed grace period (in seconds) to use when terminating pods in response to a soft eviction threshold being met. If negative, defer to pod specified value. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--eviction-minimum-reclaim strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of minimum reclaims (e.g. &quot;<code>imagefs.available=2Gi</code>&quot;) that describes the minimum amount of resource the kubelet will reclaim when performing a pod eviction if that resource is under pressure. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--eviction-pressure-transition-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>5m0s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Duration for which the kubelet has to wait before transitioning out of an eviction pressure condition. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--eviction-soft strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of eviction thresholds (e.g. &quot;<code>memory.available<1.5Gi</code>&quot;) that if met over a corresponding grace period would trigger a pod eviction. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--eviction-soft-grace-period strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of eviction grace periods (e.g. &quot;<code>memory.available=1m30s</code>&quot;) that correspond to how long a soft eviction threshold must hold before triggering a pod eviction. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--exit-on-lock-contention</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Whether kubelet should exit upon lock-file contention.</td>
</tr>

<tr>
<td colspan="2">--experimental-allocatable-ignore-eviction&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>false</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">When set to <code>true</code>, hard eviction thresholds will be ignored while calculating node allocatable. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/">here</a> for more details. (DEPRECATED: will be removed in 1.25 or later)</td>
</tr>

<tr>
<td colspan="2">--experimental-mounter-path string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>mount</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">[Experimental] Path of mounter binary. Leave empty to use the default <code>mount</code>. (DEPRECATED: will be removed in 1.24 or later, in favor of using CSI.)</td>
</tr>

<tr>
<td colspan="2">--fail-cgroupv1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Prevent the kubelet from starting on the host using cgroup v1.</td>
</tr>

<tr>
<td colspan="2">--fail-swap-on&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>true</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Makes the kubelet fail to start if swap is enabled on the node. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--feature-gates &lt;A list of 'key=true/false' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of <code>key=value</code> pairs that describe feature gates for alpha/experimental features. Options are:<br/>

APIResponseCompression=true|false (BETA - default=true)<br/>
APIServerIdentity=true|false (BETA - default=true)<br/>
APIServerTracing=true|false (BETA - default=true)<br/>
APIServingWithRoutine=true|false (BETA - default=true)<br/>
AllAlpha=true|false (ALPHA - default=false)<br/>
AllBeta=true|false (BETA - default=false)<br/>
AllowUnsafeMalformedObjectDeletion=true|false (ALPHA - default=false)<br/>
AnonymousAuthConfigurableEndpoints=true|false (BETA - default=true)<br/>
AnyVolumeDataSource=true|false (BETA - default=true)<br/>
AuthorizeNodeWithSelectors=true|false (BETA - default=true)<br/>
AuthorizeWithSelectors=true|false (BETA - default=true)<br/>
BtreeWatchCache=true|false (BETA - default=true)<br/>
CBORServingAndStorage=true|false (ALPHA - default=false)<br/>
CPUManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>
CPUManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>
CPUManagerPolicyOptions=true|false (BETA - default=true)<br/>
CRDValidationRatcheting=true|false (BETA - default=true)<br/>
CSIMigrationPortworx=true|false (BETA - default=false)<br/>
CSIVolumeHealth=true|false (ALPHA - default=false)<br/>
ClientsAllowCBOR=true|false (ALPHA - default=false)<br/>
ClientsPreferCBOR=true|false (ALPHA - default=false)<br/>
CloudControllerManagerWebhook=true|false (ALPHA - default=false)<br/>
ClusterTrustBundle=true|false (ALPHA - default=false)<br/>
ClusterTrustBundleProjection=true|false (ALPHA - default=false)<br/>
ComponentFlagz=true|false (ALPHA - default=false)<br/>
ComponentStatusz=true|false (ALPHA - default=false)<br/>
ConcurrentWatchObjectDecode=true|false (BETA - default=false)<br/>
ConsistentListFromCache=true|false (BETA - default=true)<br/>
ContainerCheckpoint=true|false (BETA - default=true)<br/>
ContextualLogging=true|false (BETA - default=true)<br/>
CoordinatedLeaderElection=true|false (ALPHA - default=false)<br/>
CrossNamespaceVolumeDataSource=true|false (ALPHA - default=false)<br/>
CustomCPUCFSQuotaPeriod=true|false (ALPHA - default=false)<br/>
DRAAdminAccess=true|false (ALPHA - default=false)<br/>
DRAResourceClaimDeviceStatus=true|false (ALPHA - default=false)<br/>
DisableAllocatorDualWrite=true|false (ALPHA - default=false)
DynamicResourceAllocation=true|false (BETA - default=false)<br/>
EventedPLEG=true|false (ALPHA - default=false)<br/>
ExternalServiceAccountTokenSigner=true|false (ALPHA - default=false)<br/>
GracefulNodeShutdown=true|false (BETA - default=true)<br/>
GracefulNodeShutdownBasedOnPodPriority=true|false (BETA - default=true)<br/>
HPAScaleToZero=true|false (ALPHA - default=false)<br/>
HonorPVReclaimPolicy=true|false (BETA - default=true)<br/>
ImageMaximumGCAge=true|false (BETA - default=true)<br/>
ImageVolume=true|false (ALPHA - default=false)<br/>
InPlacePodVerticalScaling=true|false (ALPHA - default=false)<br/>
InPlacePodVerticalScalingAllocatedStatus=true|false (ALPHA - default=false)<br/>
InPlacePodVerticalScalingExclusiveCPUs=true|false (ALPHA - default=false)<br/>
InTreePluginPortworxUnregister=true|false (ALPHA - default=false)<br/>
InformerResourceVersion=true|false (ALPHA - default=false)<br/>
JobBackoffLimitPerIndex=true|false (BETA - default=true)<br/>
JobManagedBy=true|false (ALPHA - default=false)<br/>
JobPodReplacementPolicy=true|false (BETA - default=true)<br/>
JobSuccessPolicy=true|false (BETA - default=true)<br/>
KubeletCgroupDriverFromCRI=true|false (BETA - default=true)<br/>
KubeletCrashLoopBackOffMax=true|false (ALPHA - default=false)<br/>
KubeletFineGrainedAuthz=true|false (ALPHA - default=false)<br/>
KubeletInUserNamespace=true|false (ALPHA - default=false)<br/>
KubeletPodResourcesDynamicResources=true|false (ALPHA - default=false)<br/>
KubeletPodResourcesGet=true|false (ALPHA - default=false)<br/>
KubeletSeparateDiskGC=true|false (BETA - default=true)<br/>
KubeletTracing=true|false (BETA - default=true)<br/>
LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (BETA - default=true)<br/>
LoggingAlphaOptions=true|false (ALPHA - default=false)<br/>
LoggingBetaOptions=true|false (BETA - default=true)<br/>
MatchLabelKeysInPodAffinity=true|false (BETA - default=true)<br/>
MatchLabelKeysInPodTopologySpread=true|false (BETA - default=true)<br/>
MaxUnavailableStatefulSet=true|false (ALPHA - default=false)<br/>
MemoryQoS=true|false (ALPHA - default=false)<br/>
MultiCIDRServiceAllocator=true|false (BETA - default=false)<br/>
MutatingAdmissionPolicy=true|false (ALPHA - default=false)<br/>
NFTablesProxyMode=true|false (BETA - default=true)<br/>
NodeInclusionPolicyInPodTopologySpread=true|false (BETA - default=true)<br/>
NodeLogQuery=true|false (BETA - default=false)<br/>
NodeSwap=true|false (BETA - default=true)<br/>
OpenAPIEnums=true|false (BETA - default=true)<br/>
PodAndContainerStatsFromCRI=true|false (ALPHA - default=false)<br/>
PodDeletionCost=true|false (BETA - default=true)<br/>
PodLevelResources=true|false (ALPHA - default=false)<br/>
PodLifecycleSleepAction=true|false (BETA - default=true)<br/>
PodLifecycleSleepActionAllowZero=true|false (ALPHA - default=false)<br/>
PodLogsQuerySplitStreams=true|false (ALPHA - default=false)<br/>
PodReadyToStartContainersCondition=true|false (BETA - default=true)<br/>
PodObservedGenerationTracking=true|false (ALPHA - default=false)<br/>
PortForwardWebsockets=true|false (BETA - default=true)<br/>
ProcMountType=true|false (BETA - default=true)<br/>
QOSReserved=true|false (ALPHA - default=false)<br/>
RecoverVolumeExpansionFailure=true|false (BETA - default=true)<br/>
RecursiveReadOnlyMounts=true|false (BETA - default=true)<br/>
RelaxedDNSSearchValidation=true|false (ALPHA - default=false)<br/>
RelaxedEnvironmentVariableValidation=true|false (BETA - default=true)<br/>
ReloadKubeletServerCertificateFile=true|false (BETA - default=true)<br/>
RemoteRequestHeaderUID=true|false (ALPHA - default=false)<br/>
ResilientWatchCacheInitialization=true|false (BETA - default=true)<br/>
ResourceHealthStatus=true|false (ALPHA - default=false)<br/>
RotateKubeletServerCertificate=true|false (BETA - default=true)<br/>
RuntimeClassInImageCriApi=true|false (ALPHA - default=false)<br/>
SELinuxChangePolicy=true|false (ALPHA - default=false)<br/>
SELinuxMount=true|false (ALPHA - default=false)<br/>
SELinuxMountReadWriteOncePod=true|false (BETA - default=true)<br/>
SchedulerAsyncPreemption=true|false (ALPHA - default=false)<br/>
SchedulerQueueingHints=true|false (BETA - default=true)<br/>
SeparateCacheWatchRPC=true|false (BETA - default=true)<br/>
SeparateTaintEvictionController=true|false (BETA - default=true)<br/>
ServiceAccountNodeAudienceRestriction=true|false (BETA - default=true)<br/>
ServiceAccountTokenNodeBinding=true|false (BETA - default=true)<br/>
ServiceTrafficDistribution=true|false (BETA - default=true)<br/>
SidecarContainers=true|false (BETA - default=true)<br/>
StorageNamespaceIndex=true|false (BETA - default=true)<br/>
StorageVersionAPI=true|false (ALPHA - default=false)<br/>
StorageVersionHash=true|false (BETA - default=true)<br/>
StorageVersionMigrator=true|false (ALPHA - default=false)<br/>
StructuredAuthenticationConfiguration=true|false (BETA - default=true)<br/>
SupplementalGroupsPolicy=true|false (ALPHA - default=false)<br/>
SystemdWatchdog=true|false (BETA - default=true)<br/>
TopologyAwareHints=true|false (BETA - default=true)<br/>
TopologyManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>
TopologyManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>
TranslateStreamCloseWebsocketRequests=true|false (BETA - default=true)<br/>
UnauthenticatedHTTP2DOSMitigation=true|false (BETA - default=true)<br/>
UnknownVersionInteroperabilityProxy=true|false (ALPHA - default=false)<br/>
UserNamespacesPodSecurityStandards=true|false (ALPHA - default=false)<br/>
UserNamespacesSupport=true|false (BETA - default=false)<br/>
VolumeAttributesClass=true|false (BETA - default=false)<br/>
VolumeCapacityPriority=true|false (ALPHA - default=false)<br/>
WatchCacheInitializationPostStartHook=true|false (BETA - default=false)<br/>
WatchFromStorageWithoutResourceVersion=true|false (BETA - default=false)<br/>
WatchList=true|false (BETA - default=true)<br/>
WatchListClient=true|false (BETA - default=false)<br/>
WinDSR=true|false (ALPHA - default=false)<br/>
WinOverlay=true|false (BETA - default=true)<br/>
WindowsCPUAndMemoryAffinity=true|false (ALPHA - default=false)<br/>
WindowsGracefulNodeShutdown=true|false (ALPHA - default=false)<br/>
WindowsHostNetwork=true|false (ALPHA - default=true)<br/>
(DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--file-check-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>20s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Duration between checking config files for new data. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--hairpin-mode string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>promiscuous-bridge</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">How should the kubelet setup hairpin NAT. This allows endpoints of a Service to load balance back to themselves if they should try to access their own Service. Valid values are &quot;<code>promiscuous-bridge</code>&quot;, &quot;<code>hairpin-veth</code>&quot; and &quot;<code>none</code>&quot;. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--healthz-bind-address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>127.0.0.1</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The IP address for the healthz server to serve on (set to &quot;<code>0.0.0.0</code>&quot; or &quot;<code>::</code>&quot; for listening in all interfaces and IP families). (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--healthz-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10248</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The port of the localhost healthz endpoint (set to <code>0</code> to disable). (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">help for kubelet</td>
</tr>

<tr>
<td colspan="2">--hostname-override string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">If non-empty, will use this string as identification instead of the actual hostname. If <code>--cloud-provider</code> is set, the cloud provider determines the name of the node (consult cloud provider documentation to determine if and how the hostname is used).</td>
</tr>

<tr>
<td colspan="2">--http-check-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>20s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Duration between checking HTTP for new data. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--image-credential-provider-bin-dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The path to the directory where credential provider plugin binaries are located.</td>
</tr>

<tr>
<td colspan="2">--image-credential-provider-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The path to the credential provider plugin config file.</td>
</tr>

<tr>
<td colspan="2">--image-gc-high-threshold int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 85</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The percent of disk usage after which image garbage collection is always run. Values must be within the range [0, 100], To disable image garbage collection, set to 100.   (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--image-gc-low-threshold int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 80</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to. Values must be within the range [0, 100] and should not be larger than that of <code>--image-gc-high-threshold</code>. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--image-service-endpoint string</td>
</tr>
<tr>
