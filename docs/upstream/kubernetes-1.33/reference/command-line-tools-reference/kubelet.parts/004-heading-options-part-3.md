<!-- Part 4 of 4 of reference/command-line-tools-reference/kubelet.md (split because the page is big). -->

<td></td><td style="line-height: 130%; word-wrap: break-word;">A set of &lt;key&gt;=&lt;value&gt; topology manager policy options to use, to fine tune their behaviour. If not supplied, keep the default behaviour. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--topology-manager-scope string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>container</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Scope to which topology hints are applied. Topology manager collects hints from hint providers and applies them to the defined scope to ensure the pod admission. Possible values: &quot;<code>container</code>&quot;, &quot;<code>pod</code>&quot;. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">-v, --v Level</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Number for the log level verbosity</td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Print version information and quit; <code>--version=vX.Y.Z...</code> sets the reported version.</td>
</tr>

<tr>
<td colspan="2">--vmodule &lt;A list of 'pattern=N' strings&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Comma-separated list of <code>pattern=N</code> settings for file-filtered logging (only works for text log format).</td>
</tr>

<tr>
<td colspan="2">--volume-plugin-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>/usr/libexec/kubernetes/kubelet-plugins/volume/exec/</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">The full path of the directory in which to search for additional third party volume plugins. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>

<tr>
<td colspan="2">--volume-stats-agg-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: <code>1m0s</code></td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">Specifies interval for kubelet to calculate and cache the volume disk usage for all pods and volumes. To disable volume calculations, set to a negative number. (DEPRECATED: This parameter should be set via the config file specified by the kubelet's <code>--config</code> flag. See <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/">kubelet-config-file</a> for more information.)</td>
</tr>
</tbody>
</table>
