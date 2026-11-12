<!-- Part 3 of 6 of reference/config-api/kubeadm-config.v1beta4.md (split because the page is big). -->

<h2>Kubeadm reset configuration types</h2>
<p>When executing <code>kubeadm reset</code> with the <code>--config</code> option, the <code>ResetConfiguration</code> type should be provided.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ResetConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span></pre><h2>Kubeadm upgrade configuration types</h2>
<p>When executing <code>kubeadm upgrade</code> with the <code>--config</code> option, the <code>UpgradeConfiguration</code> type should be provided.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>UpgradeConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apply</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">diff</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">node</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">plan</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span></pre><p>The <code>UpgradeConfiguration</code> structure includes a few substructures that only apply to different subcommands of
<code>kubeadm upgrade</code>. For example, the <code>apply</code> substructure will be used with the <code>kubeadm upgrade apply</code> subcommand
and all other substructures will be ignored in such a case.</p>



## Resource Types 


- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)
- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)
- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)
- [ResetConfiguration](#kubeadm-k8s-io-v1beta4-ResetConfiguration)
- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)
  
    
    


## `BootstrapToken`     {#BootstrapToken}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)


<p>BootstrapToken describes one bootstrap token, stored as a Secret in the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>token</code> <B>[Required]</B><br/>
<a href="#BootstrapTokenString"><code>BootstrapTokenString</code></a>
</td>
<td>
   <p><code>token</code> is used for establishing bidirectional trust between nodes and control-planes.
Used for joining nodes in the cluster.</p>
</td>
</tr>
<tr><td><code>description</code><br/>
<code>string</code>
</td>
<td>
   <p><code>description</code> sets a human-friendly message why this token exists and what it's used
for, so other administrators can know its purpose.</p>
</td>
</tr>
<tr><td><code>ttl</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>ttl</code> defines the time to live for this token. Defaults to <code>24h</code>.
<code>expires</code> and <code>ttl</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>expires</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p><code>expires</code> specifies the timestamp when this token expires. Defaults to being set
dynamically at runtime based on the <code>ttl</code>. <code>expires</code> and <code>ttl</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>usages</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>usages</code> describes the ways in which this token can be used. Can by default be used
for establishing bidirectional trust, but that can be changed here.</p>
</td>
</tr>
<tr><td><code>groups</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>groups</code> specifies the extra groups that this token will authenticate as when/if
used for authentication</p>
</td>
</tr>
</tbody>
</table>


## `BootstrapTokenString`     {#BootstrapTokenString}
    

**Appears in:**

- [BootstrapToken](#BootstrapToken)


<p>BootstrapTokenString is a token of the format <code>abcdef.abcdef0123456789</code> that is used
for both validation of the practically of the API server from a joining node's point
of view and as an authentication method for the node in the bootstrap phase of
&quot;kubeadm join&quot;. This token is and should be short-lived.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>-</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">No description provided.</span></td>
</tr>
<tr><td><code>-</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">No description provided.</span></td>
</tr>
</tbody>
</table>
  


## `ClusterConfiguration`     {#kubeadm-k8s-io-v1beta4-ClusterConfiguration}
    


<p>ClusterConfiguration contains cluster-wide configuration for a kubeadm cluster.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ClusterConfiguration</code></td></tr>
    
  
<tr><td><code>etcd</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Etcd"><code>Etcd</code></a>
</td>
<td>
   <p><code>etcd</code> holds the configuration for etcd.</p>
</td>
</tr>
<tr><td><code>networking</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Networking"><code>Networking</code></a>
</td>
<td>
   <p><code>networking</code> holds configuration for the networking topology of the cluster.</p>
</td>
</tr>
<tr><td><code>kubernetesVersion</code><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> is the target version of the control plane.</p>
</td>
</tr>
<tr><td><code>controlPlaneEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p><code>controlPlaneEndpoint</code> sets a stable IP address or DNS name for the control plane;
It can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port.
In case the <code>controlPlaneEndpoint</code> is not specified, the <code>advertiseAddress</code> + <code>bindPort</code>
are used; in case the <code>controlPlaneEndpoint</code> is specified but without a TCP port,
the <code>bindPort</code> is used.
Possible usages are:</p>
<ul>
<li>In a cluster with more than one control plane instances, this field should be
assigned the address of the external load balancer in front of the
control plane instances.</li>
<li>In environments with enforced node recycling, the <code>controlPlaneEndpoint</code>
could be used for assigning a stable DNS to the control plane.</li>
</ul>
</td>
</tr>
<tr><td><code>apiServer</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-APIServer"><code>APIServer</code></a>
</td>
<td>
   <p><code>apiServer</code> contains extra settings for the API server.</p>
</td>
</tr>
<tr><td><code>controllerManager</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>controllerManager</code> contains extra settings for the controller manager.</p>
</td>
</tr>
<tr><td><code>scheduler</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>scheduler</code> contains extra settings for the scheduler.</p>
</td>
</tr>
<tr><td><code>dns</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-DNS"><code>DNS</code></a>
</td>
<td>
   <p><code>dns</code> defines the options for the DNS add-on installed in the cluster.</p>
</td>
</tr>
<tr><td><code>proxy</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-Proxy"><code>Proxy</code></a>
</td>
<td>
   <p><code>proxy</code> defines the options for the proxy add-on installed in the cluster.</p>
</td>
</tr>
<tr><td><code>certificatesDir</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificatesDir</code> specifies where to store or look for all required certificates.</p>
</td>
</tr>
<tr><td><code>imageRepository</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageRepository</code> sets the container registry to pull images from.
If empty, <code>registry.k8s.io</code> will be used by default.
In case of kubernetes version is a CI build (kubernetes version starts with <code>ci/</code>)
<code>gcr.io/k8s-staging-ci-images</code> will be used as a default for control plane components
and for kube-proxy, while <code>registry.k8s.io</code> will be used for all the other images.</p>
</td>
</tr>
<tr><td><code>featureGates</code><br/>
<code>map[string]bool</code>
</td>
<td>
   <p><code>featureGates</code> contains the feature gates enabled by the user.</p>
</td>
</tr>
<tr><td><code>clusterName</code><br/>
<code>string</code>
</td>
<td>
   <p>The cluster name.</p>
</td>
</tr>
<tr><td><code>encryptionAlgorithm</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-EncryptionAlgorithmType"><code>EncryptionAlgorithmType</code></a>
</td>
<td>
   <p><code>encryptionAlgorithm</code> holds the type of asymmetric encryption algorithm used for keys and
certificates. Can be one of <code>&quot;RSA-2048&quot;</code> (default), <code>&quot;RSA-3072&quot;</code>, <code>&quot;RSA-4096&quot;</code> or <code>&quot;ECDSA-P256&quot;</code>.</p>
</td>
</tr>
<tr><td><code>certificateValidityPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>certificateValidityPeriod</code> specifies the validity period for a non-CA certificate generated by kubeadm.
Default value: `8760h`` (365 days * 24 hours = 1 year)</p>
</td>
</tr>
<tr><td><code>caCertificateValidityPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>caCertificateValidityPeriod</code> specifies the validity period for a CA certificate generated by kubeadm.
Default value: <code>87600h</code> (365 days * 24 hours * 10 = 10 years)</p>
</td>
</tr>
</tbody>
</table>


## `InitConfiguration`     {#kubeadm-k8s-io-v1beta4-InitConfiguration}
    


<p>InitConfiguration contains a list of elements that is specific &quot;kubeadm init&quot;-only runtime
information.
<code>kubeadm init</code>-only information. These fields are solely used the first time <code>kubeadm init</code> runs.
After that, the information in the fields IS NOT uploaded to the <code>kubeadm-config</code> ConfigMap
that is used by <code>kubeadm upgrade</code> for instance. These fields must be omitempty.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>InitConfiguration</code></td></tr>
    
  
<tr><td><code>bootstrapTokens</code><br/>
<a href="#BootstrapToken"><code>[]BootstrapToken</code></a>
</td>
<td>
   <p><code>bootstrapTokens</code> is respected at <code>kubeadm init</code> time and describes a set of Bootstrap Tokens to create.
This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature</p>
</td>
</tr>
<tr><td><code>dryRun</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> tells if the dry run mode is enabled, don't apply any change in dry run mode,
just out put what would be done.</p>
</td>
</tr>
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> holds fields that relate to registering the new control-plane node
to the cluster.</p>
</td>
</tr>
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p><code>localAPIEndpoint</code> represents the endpoint of the API server instance that's deployed on this
control plane node. In HA setups, this differs from <code>ClusterConfiguration.controlPlaneEndpoint</code>
in the sense that <code>controlPlaneEndpoint</code> is the global endpoint for the cluster, which then
loadbalances the requests to each individual API server.
This configuration object lets you customize what IP/DNS name and port the local API server
advertises it's accessible on. By default, kubeadm tries to auto-detect the IP of the default
interface and use that, but in case that process fails you may set the desired value here.</p>
</td>
</tr>
<tr><td><code>certificateKey</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificateKey</code> sets the key with which certificates and keys are encrypted prior to being
uploaded in a Secret in the cluster during the <code>uploadcerts init</code> phase.
The certificate key is a hex encoded string that is an AES key of size 32 bytes.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> is a list of phases to skip during command execution.
The list of phases can be obtained with the <code>kubeadm init --help</code> command.
The flag <code>--skip-phases</code> takes precedence over this field.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> contains options related to applying patches to components deployed by kubeadm during
<code>kubeadm init</code>.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p><code>timeouts</code> holds various timeouts that apply to kubeadm commands.</p>
</td>
</tr>
</tbody>
</table>


## `JoinConfiguration`     {#kubeadm-k8s-io-v1beta4-JoinConfiguration}
    


<p>JoinConfiguration contains elements describing a particular node.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>JoinConfiguration</code></td></tr>
    
  
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> tells if the dry run mode is enabled, don't apply any change if it is set,
just output what would be done.</p>
</td>
</tr>
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> holds fields that relate to registering the new control-plane
node to the cluster</p>
</td>
</tr>
<tr><td><code>caCertPath</code><br/>
<code>string</code>
</td>
<td>
   <p><code>caCertPath</code> is the path to the SSL certificate authority used to secure communications
between node and control-plane.
Defaults to &quot;/etc/kubernetes/pki/ca.crt&quot;.</p>
</td>
</tr>
<tr><td><code>discovery</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-Discovery"><code>Discovery</code></a>
</td>
<td>
   <p><code>discovery</code> specifies the options for the kubelet to use during the TLS bootstrap process.</p>
</td>
</tr>
<tr><td><code>controlPlane</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-JoinControlPlane"><code>JoinControlPlane</code></a>
</td>
<td>
   <p><code>controlPlane</code> defines the additional control plane instance to be deployed on the
joining node. If nil, no additional control plane instance will be deployed.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> is a list of phases to skip during command execution.
The list of phases can be obtained with the <code>kubeadm join --help</code> command.
The flag <code>--skip-phases</code> takes precedence over this field.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> contains options related to applying patches to components deployed
by kubeadm during <code>kubeadm join</code>.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p><code>timeouts</code> holds various timeouts that apply to kubeadm commands.</p>
</td>
</tr>
</tbody>
</table>
