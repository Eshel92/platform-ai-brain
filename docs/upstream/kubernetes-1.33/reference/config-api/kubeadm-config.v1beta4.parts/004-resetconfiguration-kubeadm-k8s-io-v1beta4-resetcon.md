<!-- Part 4 of 6 of reference/config-api/kubeadm-config.v1beta4.md (split because the page is big). -->

## `ResetConfiguration`     {#kubeadm-k8s-io-v1beta4-ResetConfiguration}
    


<p>ResetConfiguration contains a list of fields that are specifically <code>kubeadm reset</code>-only
runtime information.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ResetConfiguration</code></td></tr>
    
  
<tr><td><code>cleanupTmpDir</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>cleanupTmpDir</code> specifies whether the &quot;/etc/kubernetes/tmp&quot; directory should be cleaned
during the reset process.</p>
</td>
</tr>
<tr><td><code>certificatesDir</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificatesDir</code> specifies the directory where the certificates are stored.
If specified, it will be cleaned during the reset process.</p>
</td>
</tr>
<tr><td><code>criSocket</code><br/>
<code>string</code>
</td>
<td>
   <p><code>criSocket</code> is used to retrieve container runtime inforomation and used for the
removal of the containers.
If <code>criSocket</code> is not specified by flag or config file, kubeadm will try to detect
one valid CRI socket instead.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> tells if the dry run mode is enabled, don't apply any change if it is set
and just output what would be done.</p>
</td>
</tr>
<tr><td><code>force</code><br/>
<code>bool</code>
</td>
<td>
   <p>The <code>force</code> flag instructs kubeadm to reset the node without prompting for confirmation.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> provides a list of pre-flight errors to be ignored during
the reset process, e.g. <code>IsPrivilegedUser,Swap</code>.
Value <code>all</code> ignores errors from all checks.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> is a list of phases to skip during command execution.
The list of phases can be obtained with the <code>kubeadm reset phase --help</code> command.</p>
</td>
</tr>
<tr><td><code>unmountFlags</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>unmountFlags</code> is a list of <code>unmount2()</code> syscall flags that kubeadm can use when unmounting
directories during &quot;reset&quot;. This flag can be one of: <code>&quot;MNT_FORCE&quot;</code>, <code>&quot;MNT_DETACH&quot;</code>,
<code>&quot;MNT_EXPIRE&quot;</code>, <code>&quot;UMOUNT_NOFOLLOW&quot;</code>.  By default this list is empty.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p>Timeouts holds various timeouts that apply to kubeadm commands.</p>
</td>
</tr>
</tbody>
</table>


## `UpgradeConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeConfiguration}
    


<p>UpgradeConfiguration contains a list of options that are specific to <code>kubeadm upgrade</code> subcommands.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>UpgradeConfiguration</code></td></tr>
    
  
<tr><td><code>apply</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradeApplyConfiguration"><code>UpgradeApplyConfiguration</code></a>
</td>
<td>
   <p><code>apply</code> holds a list of options that are specific to the <code>kubeadm upgrade apply</code> command.</p>
</td>
</tr>
<tr><td><code>diff</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradeDiffConfiguration"><code>UpgradeDiffConfiguration</code></a>
</td>
<td>
   <p><code>diff</code> holds a list of options that are specific to the <code>kubeadm upgrade diff</code> command.</p>
</td>
</tr>
<tr><td><code>node</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradeNodeConfiguration"><code>UpgradeNodeConfiguration</code></a>
</td>
<td>
   <p><code>node</code> holds a list of options that are specific to the <code>kubeadm upgrade node</code> command.</p>
</td>
</tr>
<tr><td><code>plan</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradePlanConfiguration"><code>UpgradePlanConfiguration</code></a>
</td>
<td>
   <p><code>plan</code> holds a list of options that are specific to the <code>kubeadm upgrade plan</code> command.</p>
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


## `APIEndpoint`     {#kubeadm-k8s-io-v1beta4-APIEndpoint}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinControlPlane](#kubeadm-k8s-io-v1beta4-JoinControlPlane)


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


## `APIServer`     {#kubeadm-k8s-io-v1beta4-APIServer}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>APIServer holds settings necessary for API server deployments in the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ControlPlaneComponent</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
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
</tbody>
</table>


## `Arg`     {#kubeadm-k8s-io-v1beta4-Arg}
    

**Appears in:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta4-ControlPlaneComponent)

- [LocalEtcd](#kubeadm-k8s-io-v1beta4-LocalEtcd)

- [NodeRegistrationOptions](#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions)


<p>Arg represents an argument with a name and a value.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>The name of the argument.</p>
</td>
</tr>
<tr><td><code>value</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>The value of the argument.</p>
</td>
</tr>
</tbody>
</table>


## `BootstrapTokenDiscovery`     {#kubeadm-k8s-io-v1beta4-BootstrapTokenDiscovery}
    

**Appears in:**

- [Discovery](#kubeadm-k8s-io-v1beta4-Discovery)


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
object in DER-encoded ASN.1. These hashes can be // calculated using, for example, OpenSSL.</p>
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


## `ControlPlaneComponent`     {#kubeadm-k8s-io-v1beta4-ControlPlaneComponent}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)

- [APIServer](#kubeadm-k8s-io-v1beta4-APIServer)


<p>ControlPlaneComponent holds settings common to control plane component of the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>extraArgs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Arg"><code>[]Arg</code></a>
</td>
<td>
   <p><code>extraArgs</code> is an extra set of flags to pass to the control plane component.
An argument name in this list is the flag name as it appears on the
command line except without leading dash(es). Extra arguments will override existing
default arguments. Duplicate extra arguments are allowed.</p>
</td>
</tr>
<tr><td><code>extraVolumes</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-HostPathMount"><code>[]HostPathMount</code></a>
</td>
<td>
   <p><code>extraVolumes</code> is an extra set of host volumes, mounted to the control plane component.</p>
</td>
</tr>
<tr><td><code>extraEnvs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-EnvVar"><code>[]EnvVar</code></a>
</td>
<td>
   <p><code>extraEnvs</code> is an extra set of environment variables to pass to the control plane component.
Environment variables passed using <code>extraEnvs</code> will override any existing environment variables,
or <code>*_proxy</code> environment variables that kubeadm adds by default.</p>
</td>
</tr>
</tbody>
</table>


## `DNS`     {#kubeadm-k8s-io-v1beta4-DNS}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>DNS defines the DNS addon that should be used in the cluster</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(Members of <code>ImageMeta</code> are embedded into this type.)
   <p><code>imageMeta</code> allows to customize the image used for the DNS addon.</p>
</td>
</tr>
<tr><td><code>disabled</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p><code>disabled</code> specifies whether to disable this addon in the cluster.</p>
</td>
</tr>
</tbody>
</table>


## `Discovery`     {#kubeadm-k8s-io-v1beta4-Discovery}
    

**Appears in:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)


<p>Discovery specifies the options for the kubelet to use during the TLS Bootstrap process</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>bootstrapToken</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-BootstrapTokenDiscovery"><code>BootstrapTokenDiscovery</code></a>
</td>
<td>
   <p><code>bootstrapToken</code> is used to set the options for bootstrap token based discovery.
<code>bootstrapToken</code> and <code>file</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>file</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-FileDiscovery"><code>FileDiscovery</code></a>
</td>
<td>
   <p><code>file</code> is used to specify a file or URL to a kubeconfig file from which to load
cluster information. <code>bootstrapToken</code> and <code>file</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>tlsBootstrapToken</code><br/>
<code>string</code>
</td>
<td>
   <p><code>tlsBootstrapToken</code> is a token used for TLS bootstrapping.
If <code>bootstrapToken</code> is set, this field is defaulted to <code>bootstrapToken.token</code>, but
can be overridden. If <code>file</code> is set, this field <strong>must be set</strong> in case the KubeConfigFile
does not contain any other authentication information.</p>
</td>
</tr>
</tbody>
</table>


## `EncryptionAlgorithmType`     {#kubeadm-k8s-io-v1beta4-EncryptionAlgorithmType}
    
(Alias of `string`)

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>EncryptionAlgorithmType can define an asymmetric encryption algorithm type.</p>





## `EnvVar`     {#kubeadm-k8s-io-v1beta4-EnvVar}
    

**Appears in:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta4-ControlPlaneComponent)

- [LocalEtcd](#kubeadm-k8s-io-v1beta4-LocalEtcd)


<p>EnvVar represents an environment variable present in a Container.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>EnvVar</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#envvar-v1-core"><code>core/v1.EnvVar</code></a>
</td>
<td>(Members of <code>EnvVar</code> are embedded into this type.)
   <span class="text-muted">No description provided.</span></td>
</tr>
</tbody>
</table>


## `Etcd`     {#kubeadm-k8s-io-v1beta4-Etcd}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>Etcd contains elements describing Etcd configuration.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>local</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-LocalEtcd"><code>LocalEtcd</code></a>
</td>
<td>
   <p><code>local</code> provides configuration knobs for configuring the local etcd instance.
<code>local</code> and <code>external</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>external</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-ExternalEtcd"><code>ExternalEtcd</code></a>
</td>
<td>
   <p><code>external</code> describes how to connect to an external etcd cluster.
<code>local</code> and <code>external</code> are mutually exclusive.</p>
</td>
</tr>
</tbody>
</table>


## `ExternalEtcd`     {#kubeadm-k8s-io-v1beta4-ExternalEtcd}
    

**Appears in:**

- [Etcd](#kubeadm-k8s-io-v1beta4-Etcd)


<p>ExternalEtcd describes an external etcd cluster.
Kubeadm has no knowledge of where certificate files live and they must be supplied.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoints</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p><code>endpoints</code> contains the list of etcd members.</p>
</td>
</tr>
<tr><td><code>caFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>caFile</code> is an SSL Certificate Authority (CA) file used to secure etcd communication.
Required if using a TLS connection.</p>
</td>
</tr>
<tr><td><code>certFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>certFile</code> is an SSL certification file used to secure etcd communication.
Required if using a TLS connection.</p>
</td>
</tr>
<tr><td><code>keyFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>keyFile</code> is an SSL key file used to secure etcd communication.
Required if using a TLS connection.</p>
</td>
</tr>
</tbody>
</table>


## `FileDiscovery`     {#kubeadm-k8s-io-v1beta4-FileDiscovery}
    

**Appears in:**

- [Discovery](#kubeadm-k8s-io-v1beta4-Discovery)


<p>FileDiscovery is used to specify a file or URL to a kubeconfig file from which to load
cluster information.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubeConfigPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>kubeConfigPath</code> is used to specify the actual file path or URL to the kubeconfig
file from which to load cluster information.</p>
</td>
</tr>
</tbody>
</table>


## `HostPathMount`     {#kubeadm-k8s-io-v1beta4-HostPathMount}
    

**Appears in:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta4-ControlPlaneComponent)


<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>name</code> is the name of the volume inside the Pod template.</p>
</td>
</tr>
<tr><td><code>hostPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>hostPath</code> is the path in the host that will be mounted inside the Pod.</p>
</td>
</tr>
<tr><td><code>mountPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>mountPath</code> is the path inside the Pod where <code>hostPath</code> will be mounted.</p>
</td>
</tr>
<tr><td><code>readOnly</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>readOnly</code> controls write access to the volume.</p>
</td>
</tr>
<tr><td><code>pathType</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#hostpathtype-v1-core"><code>core/v1.HostPathType</code></a>
</td>
<td>
   <p><code>pathType</code> is the type of the <code>hostPath</code>.</p>
</td>
</tr>
</tbody>
</table>


## `ImageMeta`     {#kubeadm-k8s-io-v1beta4-ImageMeta}
    

**Appears in:**

- [DNS](#kubeadm-k8s-io-v1beta4-DNS)

- [LocalEtcd](#kubeadm-k8s-io-v1beta4-LocalEtcd)


<p>ImageMeta allows to customize the image used for components that are not
originated from the Kubernetes/Kubernetes release process</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>imageRepository</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageRepository</code> sets the container registry to pull images from.
if not set, the <code>imageRepository</code> defined in ClusterConfiguration will be used instead.</p>
</td>
</tr>
<tr><td><code>imageTag</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageTag</code> allows to specify a tag for the image.
In case this value is set, kubeadm does not change automatically the version of
the above components during upgrades.</p>
</td>
</tr>
</tbody>
</table>


## `JoinControlPlane`     {#kubeadm-k8s-io-v1beta4-JoinControlPlane}
    

**Appears in:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)


<p>JoinControlPlane contains elements describing an additional control plane instance to be deployed on the joining node.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p><code>localAPIEndpoint</code> represents the endpoint of the API server instance to be
deployed on this node.</p>
</td>
</tr>
<tr><td><code>certificateKey</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificateKey</code> is the key that is used for decryption of certificates after
they are downloaded from the Secret upon joining a new control plane node.
The corresponding encryption key is in the InitConfiguration.
The certificate key is a hex encoded string that is an AES key of size 32 bytes.</p>
</td>
</tr>
</tbody>
</table>
