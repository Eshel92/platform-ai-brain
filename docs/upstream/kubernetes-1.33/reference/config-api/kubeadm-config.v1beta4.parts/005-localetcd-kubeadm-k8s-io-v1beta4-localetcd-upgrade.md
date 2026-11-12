<!-- Part 5 of 6 of reference/config-api/kubeadm-config.v1beta4.md (split because the page is big). -->

## `LocalEtcd`     {#kubeadm-k8s-io-v1beta4-LocalEtcd}
    

**Appears in:**

- [Etcd](#kubeadm-k8s-io-v1beta4-Etcd)


<p>LocalEtcd describes that kubeadm should run an etcd cluster locally.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(Members of <code>ImageMeta</code> are embedded into this type.)
   <p>ImageMeta allows to customize the container used for etcd</p>
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
<tr><td><code>extraArgs</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-Arg"><code>[]Arg</code></a>
</td>
<td>
   <p><code>extraArgs</code> are extra arguments provided to the etcd binary when run
inside a static Pod. An argument name in this list is the flag name as
it appears on the command line except without leading dash(es).
Extra arguments will override existing default arguments.
Duplicate extra arguments are allowed.</p>
</td>
</tr>
<tr><td><code>extraEnvs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-EnvVar"><code>[]EnvVar</code></a>
</td>
<td>
   <p><code>extraEnvs</code> is an extra set of environment variables to pass to the
control plane component. Environment variables passed using <code>extraEnvs</code>
will override any existing environment variables, or <code>*_proxy</code> environment
variables that kubeadm adds by default.</p>
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


## `Networking`     {#kubeadm-k8s-io-v1beta4-Networking}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


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
   <p><code>dnsDomain</code> is the dns domain used by Kubernetes Services. Defaults to &quot;cluster.local&quot;.</p>
</td>
</tr>
</tbody>
</table>


## `NodeRegistrationOptions`     {#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)


<p>NodeRegistrationOptions holds fields that relate to registering a new control-plane or
node to the cluster, either via <code>kubeadm init</code> or <code>kubeadm join</code>.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <p><code>name</code> is the <code>.Metadata.Name</code> field of the Node API object that will be created in this
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
<a href="#kubeadm-k8s-io-v1beta4-Arg"><code>[]Arg</code></a>
</td>
<td>
   <p><code>kubeletExtraArgs</code> passes through extra arguments to the kubelet.
The arguments here are passed to the kubelet command line via the environment file
kubeadm writes at runtime for the kubelet to source.
This overrides the generic base-level configuration in the <code>kubelet-config</code> ConfigMap.
Flags have higher priority when parsing. These values are local and specific to the node
kubeadm is executing on. An argument name in this list is the flag name as it appears on the
command line except without leading dash(es). Extra arguments will override existing
default arguments. Duplicate extra arguments are allowed.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> provides a slice of pre-flight errors to be ignored when
the current node is registered, e.g. 'IsPrivilegedUser,Swap'.
Value 'all' ignores errors from all checks.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> specifies the policy for image pulling during kubeadm <code>init</code> and
<code>join</code> operations.
The value of this field must be one of &quot;Always&quot;, &quot;IfNotPresent&quot; or &quot;Never&quot;.
If this field is unset kubeadm will default it to &quot;IfNotPresent&quot;, or pull the required
images if not present on the host.</p>
</td>
</tr>
<tr><td><code>imagePullSerial</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>imagePullSerial</code> specifies if image pulling performed by kubeadm must be done serially or in parallel.
Default: true</p>
</td>
</tr>
</tbody>
</table>


## `Patches`     {#kubeadm-k8s-io-v1beta4-Patches}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)

- [UpgradeApplyConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeApplyConfiguration)

- [UpgradeNodeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeNodeConfiguration)


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
&quot;kube-apiserver&quot;, &quot;kube-controller-manager&quot;, &quot;kube-scheduler&quot;, &quot;etcd&quot;, &quot;kubeletconfiguration&quot;,
&quot;corednsdeployment&quot;.
&quot;patchtype&quot; can be one of &quot;strategic&quot;, &quot;merge&quot; or &quot;json&quot; and they match the patch formats
supported by kubectl.
The default &quot;patchtype&quot; is &quot;strategic&quot;. &quot;extension&quot; must be either &quot;json&quot; or &quot;yaml&quot;.
&quot;suffix&quot; is an optional string that can be used to determine which patches are applied
first alpha-numerically.</p>
</td>
</tr>
</tbody>
</table>


## `Proxy`     {#kubeadm-k8s-io-v1beta4-Proxy}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>Proxy defines the proxy addon that should be used in the cluster.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>disabled</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p><code>disabled</code> specifies whether to disable this addon in the cluster.</p>
</td>
</tr>
</tbody>
</table>


## `Timeouts`     {#kubeadm-k8s-io-v1beta4-Timeouts}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)

- [ResetConfiguration](#kubeadm-k8s-io-v1beta4-ResetConfiguration)

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>Timeouts holds various timeouts that apply to kubeadm commands.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>controlPlaneComponentHealthCheck</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>controlPlaneComponentHealthCheck</code> is the amount of time to wait for a control plane
component, such as the API server, to be healthy during <code>kubeadm init</code> and <code>kubeadm join</code>.
Default: 4m</p>
</td>
</tr>
<tr><td><code>kubeletHealthCheck</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>kubeletHealthCheck</code> is the amount of time to wait for the kubelet to be healthy
during <code>kubeadm init</code> and <code>kubeadm join</code>.
Default: 4m</p>
</td>
</tr>
<tr><td><code>kubernetesAPICall</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>kubernetesAPICall</code> is the amount of time to wait for the kubeadm client to complete a request to
the API server. This applies to all types of methods (GET, POST, etc).
Default: 1m</p>
</td>
</tr>
<tr><td><code>etcdAPICall</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>etcdAPICall</code> is the amount of time to wait for the kubeadm etcd client to complete a request to
the etcd cluster.
Default: 2m</p>
</td>
</tr>
<tr><td><code>tlsBootstrap</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>tlsBootstrap</code> is the amount of time to wait for the kubelet to complete TLS bootstrap
for a joining node.
Default: 5m</p>
</td>
</tr>
<tr><td><code>discovery</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>discovery</code> is the amount of time to wait for kubeadm to validate the API server identity
for a joining node.
Default: 5m</p>
</td>
</tr>
<tr><td><code>upgradeManifests</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>upgradeManifests</code> is the timeout for upgrading static Pod manifests
Default: 5m</p>
</td>
</tr>
</tbody>
</table>


## `UpgradeApplyConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeApplyConfiguration}
    

**Appears in:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradeApplyConfiguration contains a list of configurable options which are specific to the  &quot;kubeadm upgrade apply&quot; command.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesVersion</code><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> is the target version of the control plane.</p>
</td>
</tr>
<tr><td><code>allowExperimentalUpgrades</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>allowExperimentalUpgrades</code> instructs kubeadm to show unstable versions of Kubernetes as an upgrade
alternative and allows upgrading to an alpha/beta/release candidate version of Kubernetes.
Default: false</p>
</td>
</tr>
<tr><td><code>allowRCUpgrades</code><br/>
<code>bool</code>
</td>
<td>
   <p>Enable <code>allowRCUpgrades</code> will show release candidate versions of Kubernetes as an upgrade alternative and
allows upgrading to a release candidate version of Kubernetes.</p>
</td>
</tr>
<tr><td><code>certificateRenewal</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>certificateRenewal</code> instructs kubeadm to execute certificate renewal during upgrades.
Defaults to true.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> tells if the dry run mode is enabled, don't apply any change if it is and just output
what would be done.</p>
</td>
</tr>
<tr><td><code>etcdUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>etcdUpgrade</code> instructs kubeadm to execute etcd upgrade during upgrades.
Defaults to true.</p>
</td>
</tr>
<tr><td><code>forceUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>forceUpgrade</code> flag instructs kubeadm to upgrade the cluster without prompting for confirmation.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> provides a slice of pre-flight errors to be ignored during the upgrade process,
e.g. <code>IsPrivilegedUser,Swap</code>. Value <code>all</code> ignores errors from all checks.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> contains options related to applying patches to components deployed by kubeadm during <code>kubeadm upgrade</code>.</p>
</td>
</tr>
<tr><td><code>printConfig</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>printConfig</code> specifies whether the configuration file that will be used in the upgrade should be printed or not.</p>
</td>
</tr>
<tr><td><code>skipPhases</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> is a list of phases to skip during command execution.
NOTE: This field is currently ignored for <code>kubeadm upgrade apply</code>, but in the future it will be supported.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> specifies the policy for image pulling during <code>kubeadm upgrade apply</code> operations.
The value of this field must be one of &quot;Always&quot;, &quot;IfNotPresent&quot; or &quot;Never&quot;.
If this field is unset kubeadm will default it to &quot;IfNotPresent&quot;, or pull the required images if not present on the host.</p>
</td>
</tr>
<tr><td><code>imagePullSerial</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>imagePullSerial</code> specifies if image pulling performed by kubeadm must be done serially or in parallel.
Default: true</p>
</td>
</tr>
</tbody>
</table>


## `UpgradeDiffConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeDiffConfiguration}
    

**Appears in:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradeDiffConfiguration contains a list of configurable options which are specific to the <code>kubeadm upgrade diff</code> command.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesVersion</code><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> is the target version of the control plane.</p>
</td>
</tr>
<tr><td><code>contextLines</code><br/>
<code>int</code>
</td>
<td>
   <p><code>diffContextLines</code> is the number of lines of context in the diff.</p>
</td>
</tr>
</tbody>
</table>


## `UpgradeNodeConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeNodeConfiguration}
    

**Appears in:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradeNodeConfiguration contains a list of configurable options which are specific to the &quot;kubeadm upgrade node&quot; command.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>certificateRenewal</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>certificateRenewal</code> instructs kubeadm to execute certificate renewal during upgrades.
Defaults to true.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> tells if the dry run mode is enabled, don't apply any change if it is and just output what would be done.</p>
</td>
</tr>
<tr><td><code>etcdUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>etcdUpgrade</code> instructs kubeadm to execute etcd upgrade during upgrades.
Defaults to true.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> provides a slice of pre-flight errors to be ignored during the upgrade process,
e.g. 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> is a list of phases to skip during command execution.
The list of phases can be obtained with the <code>kubeadm upgrade node phase --help</code> command.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> contains options related to applying patches to components deployed by kubeadm during <code>kubeadm upgrade</code>.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> specifies the policy for image pulling during <code>kubeadm upgrade node</code> operations.
The value of this field must be one of &quot;Always&quot;, &quot;IfNotPresent&quot; or &quot;Never&quot;.
If this field is unset kubeadm will default it to &quot;IfNotPresent&quot;, or pull the required images if not present on the host.</p>
</td>
</tr>
<tr><td><code>imagePullSerial</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>imagePullSerial</code> specifies if image pulling performed by kubeadm must be done serially or in parallel.
Default: true</p>
</td>
</tr>
</tbody>
</table>
