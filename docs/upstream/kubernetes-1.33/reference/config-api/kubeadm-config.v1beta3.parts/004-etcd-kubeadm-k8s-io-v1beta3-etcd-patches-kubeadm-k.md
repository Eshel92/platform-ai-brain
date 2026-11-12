<!-- Part 4 of 4 of reference/config-api/kubeadm-config.v1beta3.md (split because the page is big). -->

## `Etcd`     {#kubeadm-k8s-io-v1beta3-Etcd}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>Etcd contains elements describing Etcd configuration.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>local</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-LocalEtcd"><code>LocalEtcd</code></a>
</td>
<td>
   <p><code>local</code> provides configuration knobs for configuring the local etcd instance.
<code>local</code> and <code>external</code> are mutually exclusive.</p>
</td>
</tr>
<tr><td><code>external</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-ExternalEtcd"><code>ExternalEtcd</code></a>
</td>
<td>
   <p><code>external</code> describes how to connect to an external etcd cluster.
<code>local</code> and <code>external</code> are mutually exclusive.</p>
</td>
</tr>
</tbody>
</table>


## `ExternalEtcd`     {#kubeadm-k8s-io-v1beta3-ExternalEtcd}
    

**Appears in:**

- [Etcd](#kubeadm-k8s-io-v1beta3-Etcd)


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


## `FileDiscovery`     {#kubeadm-k8s-io-v1beta3-FileDiscovery}
    

**Appears in:**

- [Discovery](#kubeadm-k8s-io-v1beta3-Discovery)


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


## `HostPathMount`     {#kubeadm-k8s-io-v1beta3-HostPathMount}
    

**Appears in:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta3-ControlPlaneComponent)


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


## `ImageMeta`     {#kubeadm-k8s-io-v1beta3-ImageMeta}
    

**Appears in:**

- [DNS](#kubeadm-k8s-io-v1beta3-DNS)

- [LocalEtcd](#kubeadm-k8s-io-v1beta3-LocalEtcd)


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
If not set, the <code>imageRepository</code> defined in ClusterConfiguration will be used instead.</p>
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


## `JoinControlPlane`     {#kubeadm-k8s-io-v1beta3-JoinControlPlane}
    

**Appears in:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>JoinControlPlane contains elements describing an additional control plane instance
to be deployed on the joining node.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-APIEndpoint"><code>APIEndpoint</code></a>
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
they are downloaded from the secret upon joining a new control plane node.
The corresponding encryption key is in the InitConfiguration.
The certificate key is a hex encoded string that is an AES key of size 32 bytes.</p>
</td>
</tr>
</tbody>
</table>


## `LocalEtcd`     {#kubeadm-k8s-io-v1beta3-LocalEtcd}
    

**Appears in:**

- [Etcd](#kubeadm-k8s-io-v1beta3-Etcd)


<p>LocalEtcd describes that kubeadm should run an etcd cluster locally.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(Members of <code>ImageMeta</code> are embedded into this type.)
   <p>ImageMeta allows to customize the container used for etcd.</p>
</td>
</tr>
<tr><td><code>dataDir</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>dataDir</code> is the directory etcd will place its data.
Defaults to &quot;/var/lib/etcd&quot;.</p>
</td>
</tr>
<tr><td><code>extraArgs</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p><code>extraArgs</code> are extra arguments provided to the etcd binary when run
inside a static Pod. A key in this map is the flag name as it appears on the
command line except without leading dash(es).</p>
</td>
</tr>
<tr><td><code>serverCertSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>serverCertSANs</code> sets extra Subject Alternative Names (SANs) for the etcd
server signing certificate.</p>
</td>
</tr>
<tr><td><code>peerCertSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>peerCertSANs</code> sets extra Subject Alternative Names (SANs) for the etcd peer
signing certificate.</p>
</td>
</tr>
</tbody>
</table>


## `Networking`     {#kubeadm-k8s-io-v1beta3-Networking}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>Networking contains elements describing cluster's networking configuration.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>serviceSubnet</code><br/>
<code>string</code>
</td>
<td>
   <p><code>serviceSubnet</code> is the subnet used by Kubernetes Services. Defaults to &quot;10.96.0.0/12&quot;.</p>
</td>
</tr>
<tr><td><code>podSubnet</code><br/>
<code>string</code>
</td>
<td>
   <p><code>podSubnet</code> is the subnet used by Pods.</p>
</td>
</tr>
<tr><td><code>dnsDomain</code><br/>
<code>string</code>
</td>
<td>
   <p><code>dnsDomain</code> is the DNS domain used by Kubernetes Services. Defaults to &quot;cluster.local&quot;.</p>
</td>
</tr>
</tbody>
</table>


## `NodeRegistrationOptions`     {#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>NodeRegistrationOptions holds fields that relate to registering a new control-plane or
node to the cluster, either via <code>kubeadm init</code> or <code>kubeadm join</code>.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <p><code>name</code> is the <code>.metadata.name</code> field of the Node API object that will be created in this
<code>kubeadm init</code> or <code>kubeadm join</code> operation.
This field is also used in the <code>CommonName</code> field of the kubelet's client certificate to
the API server.
Defaults to the hostname of the node if not provided.</p>
</td>
</tr>
<tr><td><code>criSocket</code><br/>
<code>string</code>
</td>
<td>
   <p><code>criSocket</code> is used to retrieve container runtime info.
This information will be annotated to the Node API object, for later re-use.</p>
</td>
</tr>
<tr><td><code>taints</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#taint-v1-core"><code>[]core/v1.Taint</code></a>
</td>
<td>
   <p><code>taints</code> specifies the taints the Node API object should be registered with.
If this field is unset, i.e. nil, it will be defaulted with a control-plane taint for control-plane nodes.
If you don't want to taint your control-plane node, set this field to an empty list,
i.e. <code>taints: []</code> in the YAML file. This field is solely used for Node registration.</p>
</td>
</tr>
<tr><td><code>kubeletExtraArgs</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p><code>kubeletExtraArgs</code> passes through extra arguments to the kubelet.
The arguments here are passed to the kubelet command line via the environment file
kubeadm writes at runtime for the kubelet to source.
This overrides the generic base-level configuration in the <code>kubelet-config</code> ConfigMap.
Flags have higher priority when parsing. These values are local and specific to the node
kubeadm is executing on. A key in this map is the flag name as it appears on the
command line except without leading dash(es).</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> provides a list of pre-flight errors to be ignored when
the current node is registered, e.g. <code>IsPrevilegedUser,Swap</code>.
Value <code>all</code> ignores errors from all checks.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> specifies the policy for image pulling during kubeadm &quot;init&quot; and
&quot;join&quot; operations.
The value of this field must be one of &quot;Always&quot;, &quot;IfNotPresent&quot; or &quot;Never&quot;.
If this field is not set, kubeadm will default it to &quot;IfNotPresent&quot;, or pull the required
images if not present on the host.</p>
</td>
</tr>
</tbody>
</table>


## `Patches`     {#kubeadm-k8s-io-v1beta3-Patches}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>Patches contains options related to applying patches to components deployed by kubeadm.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>directory</code><br/>
<code>string</code>
</td>
<td>
   <p><code>directory</code> is a path to a directory that contains files named
&quot;target[suffix][+patchtype].extension&quot;.
For example, &quot;kube-apiserver0+merge.yaml&quot; or just &quot;etcd.json&quot;. &quot;target&quot; can be one of
&quot;kube-apiserver&quot;, &quot;kube-controller-manager&quot;, &quot;kube-scheduler&quot;, &quot;etcd&quot;. &quot;patchtype&quot; can
be one of &quot;strategic&quot; &quot;merge&quot; or &quot;json&quot; and they match the patch formats supported by
kubectl.
The default &quot;patchtype&quot; is &quot;strategic&quot;. &quot;extension&quot; must be either &quot;json&quot; or &quot;yaml&quot;.
&quot;suffix&quot; is an optional string that can be used to determine which patches are applied
first alpha-numerically.</p>
</td>
</tr>
</tbody>
</table>
