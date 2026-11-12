<!-- Part 3 of 4 of reference/config-api/kubeadm-config.v1beta3.md (split because the page is big). -->

## Resource Types 


- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)
- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)
- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)
  
    
    


## `BootstrapToken`     {#BootstrapToken}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)


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
  


## `ClusterConfiguration`     {#kubeadm-k8s-io-v1beta3-ClusterConfiguration}
    


<p>ClusterConfiguration contains cluster-wide configuration for a kubeadm cluster.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta3</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ClusterConfiguration</code></td></tr>
    
  
<tr><td><code>etcd</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Etcd"><code>Etcd</code></a>
</td>
<td>
   <p><code>etcd</code> holds the configuration for etcd.</p>
</td>
</tr>
<tr><td><code>networking</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Networking"><code>Networking</code></a>
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
   <p><code>controlPlaneEndpoint</code> sets a stable IP address or DNS name for the control plane.
It can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port.
In case the <code>controlPlaneEndpoint</code> is not specified, the <code>advertiseAddress</code> + <code>bindPort</code>
are used; in case the <code>controlPlaneEndpoint</code> is specified but without a TCP port,
the <code>bindPort</code> is used.
Possible usages are:</p>
<ul>
<li>In a cluster with more than one control plane instances, this field should be
assigned the address of the external load balancer in front of the
control plane instances.</li>
<li>In environments with enforced node recycling, the <code>controlPlaneEndpoint</code> could
be used for assigning a stable DNS to the control plane.</li>
</ul>
</td>
</tr>
<tr><td><code>apiServer</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-APIServer"><code>APIServer</code></a>
</td>
<td>
   <p><code>apiServer</code> contains extra settings for the API server.</p>
</td>
</tr>
<tr><td><code>controllerManager</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>controllerManager</code> contains extra settings for the controller manager.</p>
</td>
</tr>
<tr><td><code>scheduler</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>scheduler</code> contains extra settings for the scheduler.</p>
</td>
</tr>
<tr><td><code>dns</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-DNS"><code>DNS</code></a>
</td>
<td>
   <p><code>dns</code> defines the options for the DNS add-on installed in the cluster.</p>
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
</tbody>
</table>


## `InitConfiguration`     {#kubeadm-k8s-io-v1beta3-InitConfiguration}
    


<p>InitConfiguration contains a list of elements that is specific &quot;kubeadm init&quot;-only runtime
information.
<code>kubeadm init</code>-only information. These fields are solely used the first time <code>kubeadm init</code> runs.
After that, the information in the fields IS NOT uploaded to the <code>kubeadm-config</code> ConfigMap
that is used by <code>kubeadm upgrade</code> for instance. These fields must be omitempty.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta3</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>InitConfiguration</code></td></tr>
    
  
<tr><td><code>bootstrapTokens</code><br/>
<a href="#BootstrapToken"><code>[]BootstrapToken</code></a>
</td>
<td>
   <p><code>bootstrapTokens</code> is respected at <code>kubeadm init</code> time and describes a set of Bootstrap Tokens to create.
This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature</p>
</td>
</tr>
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> holds fields that relate to registering the new control-plane node
to the cluster.</p>
</td>
</tr>
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p><code>localAPIEndpoint</code> represents the endpoint of the API server instance that's deployed on this
control plane node. In HA setups, this differs from <code>ClusterConfiguration.controlPlaneEndpoint</code>
in the sense that <code>controlPlaneEndpoint</code> is the global endpoint for the cluster, which then
load-balances the requests to each individual API server.
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
The flag &quot;--skip-phases&quot; takes precedence over this field.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> contains options related to applying patches to components deployed by kubeadm during
<code>kubeadm init</code>.</p>
</td>
</tr>
</tbody>
</table>


## `JoinConfiguration`     {#kubeadm-k8s-io-v1beta3-JoinConfiguration}
    


<p>JoinConfiguration contains elements describing a particular node.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta3</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>JoinConfiguration</code></td></tr>
    
  
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> holds fields that relate to registering the new
control-plane node to the cluster.</p>
</td>
</tr>
<tr><td><code>caCertPath</code><br/>
<code>string</code>
</td>
<td>
   <p><code>caCertPath</code> is the path to the SSL certificate authority used to secure
comunications between a node and the control-plane.
Defaults to &quot;/etc/kubernetes/pki/ca.crt&quot;.</p>
</td>
</tr>
<tr><td><code>discovery</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-Discovery"><code>Discovery</code></a>
</td>
<td>
   <p><code>discovery</code> specifies the options for the kubelet to use during the TLS
bootstrap process.</p>
</td>
</tr>
<tr><td><code>controlPlane</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-JoinControlPlane"><code>JoinControlPlane</code></a>
</td>
<td>
   <p><code>controlPlane</code> defines the additional control plane instance to be deployed
on the joining node. If nil, no additional control plane instance will be deployed.</p>
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
<a href="#kubeadm-k8s-io-v1beta3-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> contains options related to applying patches to components deployed
by kubeadm during <code>kubeadm join</code>.</p>
</td>
</tr>
</tbody>
</table>


## `APIEndpoint`     {#kubeadm-k8s-io-v1beta3-APIEndpoint}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [JoinControlPlane](#kubeadm-k8s-io-v1beta3-JoinControlPlane)


<p>APIEndpoint struct contains elements of API server instance deployed on a node.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>advertiseAddress</code><br/>
<code>string</code>
</td>
<td>
   <p><code>advertiseAddress</code> sets the IP address for the API server to advertise.</p>
</td>
</tr>
<tr><td><code>bindPort</code><br/>
<code>int32</code>
</td>
<td>
   <p><code>bindPort</code> sets the secure port for the API Server to bind to.
Defaults to 6443.</p>
</td>
</tr>
</tbody>
</table>


## `APIServer`     {#kubeadm-k8s-io-v1beta3-APIServer}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>APIServer holds settings necessary for API server deployments in the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ControlPlaneComponent</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>(Members of <code>ControlPlaneComponent</code> are embedded into this type.)
   <span class="text-muted">No description provided.</span></td>
</tr>
<tr><td><code>certSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>certSANs</code> sets extra Subject Alternative Names (SANs) for the API Server signing
certificate.</p>
</td>
</tr>
<tr><td><code>timeoutForControlPlane</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>timeoutForControlPlane</code> controls the timeout that we wait for API server to appear.</p>
</td>
</tr>
</tbody>
</table>


## `BootstrapTokenDiscovery`     {#kubeadm-k8s-io-v1beta3-BootstrapTokenDiscovery}
    

**Appears in:**

- [Discovery](#kubeadm-k8s-io-v1beta3-Discovery)


<p>BootstrapTokenDiscovery is used to set the options for bootstrap token based discovery.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>token</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>token</code> is a token used to validate cluster information fetched from the
control-plane.</p>
</td>
</tr>
<tr><td><code>apiServerEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p><code>apiServerEndpoint</code> is an IP or domain name to the API server from which
information will be fetched.</p>
</td>
</tr>
<tr><td><code>caCertHashes</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>caCertHashes</code> specifies a set of public key pins to verify when token-based discovery
is used. The root CA found during discovery must match one of these values.
Specifying an empty set disables root CA pinning, which can be unsafe.
Each hash is specified as <code>&lt;type&gt;:&lt;value&gt;</code>, where the only currently supported type is
&quot;sha256&quot;. This is a hex-encoded SHA-256 hash of the Subject Public Key Info (SPKI)
object in DER-encoded ASN.1. These hashes can be calculated using, for example, OpenSSL.</p>
</td>
</tr>
<tr><td><code>unsafeSkipCAVerification</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>unsafeSkipCAVerification</code> allows token-based discovery without CA verification
via <code>caCertHashes</code>. This can weaken the security of kubeadm since other nodes can
impersonate the control-plane.</p>
</td>
</tr>
</tbody>
</table>


## `ControlPlaneComponent`     {#kubeadm-k8s-io-v1beta3-ControlPlaneComponent}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)

- [APIServer](#kubeadm-k8s-io-v1beta3-APIServer)


<p>ControlPlaneComponent holds settings common to control plane component of the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>extraArgs</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p><code>extraArgs</code> is an extra set of flags to pass to the control plane component.
A key in this map is the flag name as it appears on the command line except
without leading dash(es).</p>
</td>
</tr>
<tr><td><code>extraVolumes</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-HostPathMount"><code>[]HostPathMount</code></a>
</td>
<td>
   <p><code>extraVolumes</code> is an extra set of host volumes, mounted to the control plane component.</p>
</td>
</tr>
</tbody>
</table>


## `DNS`     {#kubeadm-k8s-io-v1beta3-DNS}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>DNS defines the DNS addon that should be used in the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(Members of <code>ImageMeta</code> are embedded into this type.)
   <p><code>imageMeta</code> allows to customize the image used for the DNS component.</p>
</td>
</tr>
</tbody>
</table>


## `Discovery`     {#kubeadm-k8s-io-v1beta3-Discovery}
    

**Appears in:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>Discovery specifies the options for the kubelet to use during the TLS Bootstrap process.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>bootstrapToken</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-BootstrapTokenDiscovery"><code>BootstrapTokenDiscovery</code></a>
</td>
<td>
   <p><code>bootstrapToken</code> is used to set the options for bootstrap token based discovery.
<code>bootstrapToken</code> and <code>file</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>file</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-FileDiscovery"><code>FileDiscovery</code></a>
</td>
<td>
   <p><code>file</code> is used to specify a file or URL to a kubeconfig file from which to load
cluster information.
<code>bootstrapToken</code> and <code>file</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>tlsBootstrapToken</code><br/>
<code>string</code>
</td>
<td>
   <p><code>tlsBootstrapToken</code> is a token used for TLS bootstrapping.
If <code>bootstrapToken</code> is set, this field is defaulted to <code>.bootstrapToken.token</code>, but
can be overridden. If <code>file</code> is set, this field <strong>must be set</strong> in case the KubeConfigFile
does not contain any other authentication information</p>
</td>
</tr>
<tr><td><code>timeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>timeout</code> modifies the discovery timeout.</p>
</td>
</tr>
</tbody>
</table>
