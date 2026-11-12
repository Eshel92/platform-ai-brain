<!-- Part 6 of 6 of reference/config-api/kubeadm-config.v1beta4.md (split because the page is big). -->

## `UpgradePlanConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradePlanConfiguration}
    

**Appears in:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradePlanConfiguration contains a list of configurable options which are specific to the &quot;kubeadm upgrade plan&quot; command.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesVersion</code> <B>[Required]</B><br/>
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
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> tells if the dry run mode is enabled, don't apply any change if it is and just output what would be done.</p>
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
<tr><td><code>printConfig</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>printConfig</code> specifies whether the configuration file that will be used in the upgrade should be printed or not.</p>
</td>
</tr>
</tbody>
</table>
