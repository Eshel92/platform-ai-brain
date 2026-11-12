<!-- Part 1 of 4 of reference/config-api/kubeadm-config.v1beta3.md (split because the page is big). -->

<h2>Overview</h2>
<p>Package v1beta3 defines the v1beta3 version of the kubeadm configuration file format.
This version improves on the v1beta2 format by fixing some minor issues and adding a few new fields.</p>
<p>A list of changes since v1beta2:</p>
<ul>
<li>The deprecated &quot;ClusterConfiguration.useHyperKubeImage&quot; field has been removed.
Kubeadm no longer supports the hyperkube image.</li>
<li>The &quot;ClusterConfiguration.dns.type&quot; field has been removed since CoreDNS is the only supported
DNS server type by kubeadm.</li>
<li>Include &quot;datapolicy&quot; tags on the fields that hold secrets.
This would result in the field values to be omitted when API structures are printed with klog.</li>
<li>Add &quot;InitConfiguration.skipPhases&quot;, &quot;JoinConfiguration.skipPhases&quot; to allow skipping
a list of phases during kubeadm init/join command execution.</li>
<li>Add &quot;InitConfiguration.nodeRegistration.imagePullPolicy&quot; and &quot;JoinConfiguration.nodeRegistration.imagePullPolicy&quot;
to allow specifying the images pull policy during kubeadm &quot;init&quot; and &quot;join&quot;.
The value must be one of &quot;Always&quot;, &quot;Never&quot; or &quot;IfNotPresent&quot;.
&quot;IfNotPresent&quot; is the default, which has been the existing behavior prior to this addition.</li>
<li>Add &quot;InitConfiguration.patches.directory&quot;, &quot;JoinConfiguration.patches.directory&quot; to allow
the user to configure a directory from which to take patches for components deployed by kubeadm.</li>
<li>Move the BootstrapToken* API and related utilities out of the &quot;kubeadm&quot; API group to a new group
&quot;bootstraptoken&quot;. The kubeadm API version v1beta3 no longer contains the BootstrapToken* structures.</li>
</ul>
<p>Migration from old kubeadm config versions</p>
<ul>
<li>kubeadm v1.15.x and newer can be used to migrate from v1beta1 to v1beta2.</li>
<li>kubeadm v1.22.x and newer no longer support v1beta1 and older APIs, but can be used to migrate v1beta2 to v1beta3.</li>
<li>kubeadm v1.27.x and newer no longer support v1beta2 and older APIs,</li>
</ul>

<h2>Basics</h2>
<p>The preferred way to configure kubeadm is to pass an YAML configuration file with the <code>--config</code> option. Some of the
configuration options defined in the kubeadm config file are also available as command line flags, but only
the most common/simple use case are supported with this approach.</p>
<p>A kubeadm config file could contain multiple configuration types separated using three dashes (<code>---</code>).</p>
<p>kubeadm supports the following configuration types:</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ClusterConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>JoinConfiguration<span style="color:#bbb">
</span></pre><p>To print the defaults for &quot;init&quot; and &quot;join&quot; actions use the following commands:</p>
<pre style="background-color:#fff">kubeadm config print init-defaults
kubeadm config print join-defaults
</pre><p>The list of configuration types that must be included in a configuration file depends by the action you are
performing (<code>init</code> or <code>join</code>) and by the configuration options you are going to use (defaults or advanced
customization).</p>
<p>If some configuration types are not provided, or provided only partially, kubeadm will use default values; defaults
provided by kubeadm includes also enforcing consistency of values across components when required (e.g.
<code>--cluster-cidr</code> flag on controller manager and <code>clusterCIDR</code> on kube-proxy).</p>
<p>Users are always allowed to override default values, with the only exception of a small subset of setting with
relevance for security (e.g. enforce authorization-mode Node and RBAC on api server).</p>
<p>If the user provides a configuration types that is not expected for the action you are performing, kubeadm will
ignore those types and print a warning.</p>
