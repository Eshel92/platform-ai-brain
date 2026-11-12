<!-- Part 22 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.ProbeTargetIngress">ProbeTargetIngress
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ProbeTargets">ProbeTargets</a>)
</p>
<div>
<p>ProbeTargetIngress defines the set of Ingress objects considered for probing.
The operator configures a target for each host/path combination of each ingress object.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>selector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>selector to select the Ingress objects.</p>
</td>
</tr>
<tr>
<td>
<code>namespaceSelector</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NamespaceSelector">
NamespaceSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>namespaceSelector defines from which namespaces to select Ingress objects.</p>
</td>
</tr>
<tr>
<td>
<code>relabelingConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>relabelingConfigs to apply to the label set of the target before it gets
scraped.
The original ingress address is available via the
<code>__tmp_prometheus_ingress_address</code> label. It can be used to customize the
probed URL.
The original scrape job&rsquo;s name is available via the <code>__tmp_prometheus_job_name</code> label.
More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ProbeTargetStaticConfig">ProbeTargetStaticConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ProbeTargets">ProbeTargets</a>)
</p>
<div>
<p>ProbeTargetStaticConfig defines the set of static targets considered for probing.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>static</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>static defines the list of hosts to probe.</p>
</td>
</tr>
<tr>
<td>
<code>labels</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>labels defines all labels assigned to all metrics scraped from the targets.</p>
</td>
</tr>
<tr>
<td>
<code>relabelingConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>relabelingConfigs defines relabelings to be apply to the label set of the targets before it gets
scraped.
More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ProbeTargets">ProbeTargets
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>)
</p>
<div>
<p>ProbeTargets defines how to discover the probed targets.
One of the <code>staticConfig</code> or <code>ingress</code> must be defined.
If both are defined, <code>staticConfig</code> takes precedence.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>staticConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ProbeTargetStaticConfig">
ProbeTargetStaticConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>staticConfig defines the static list of targets to probe and the
relabeling configuration.
If <code>ingress</code> is also defined, <code>staticConfig</code> takes precedence.
More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config</a>.</p>
</td>
</tr>
<tr>
<td>
<code>ingress</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ProbeTargetIngress">
ProbeTargetIngress
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ingress defines the Ingress objects to probe and the relabeling
configuration.
If <code>staticConfig</code> is also defined, <code>staticConfig</code> takes precedence.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ProberSpec">ProberSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>)
</p>
<div>
<p>ProberSpec contains specification parameters for the Prober used for probing.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>url</code><br/>
<em>
string
</em>
</td>
<td>
<p>url defines the address of the prober.</p>
<p>Unlike what the name indicates, the value should be in the form of
<code>address:port</code> without any scheme which should be specified in the
<code>scheme</code> field.</p>
</td>
</tr>
<tr>
<td>
<code>scheme</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Scheme">
Scheme
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scheme defines the HTTP scheme to use when scraping the prober.</p>
</td>
</tr>
<tr>
<td>
<code>path</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>path to collect metrics from.
Defaults to <code>/probe</code>.</p>
</td>
</tr>
<tr>
<td>
<code>proxyUrl</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>proxyUrl defines the HTTP proxy server to use.</p>
</td>
</tr>
<tr>
<td>
<code>noProxy</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names
that should be excluded from proxying. IP and domain names can
contain port numbers.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p>
</td>
</tr>
<tr>
<td>
<code>proxyFromEnvironment</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p>
</td>
</tr>
<tr>
<td>
<code>proxyConnectHeader</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
map[string][]Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>proxyConnectHeader optionally specifies headers to send to
proxies during CONNECT requests.</p>
<p>It requires Prometheus &gt;= v2.43.0, Alertmanager &gt;= v0.25.0 or Thanos &gt;= v0.32.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PrometheusRuleExcludeConfig">PrometheusRuleExcludeConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>PrometheusRuleExcludeConfig enables users to configure excluded
PrometheusRule names and their namespaces to be ignored while enforcing
namespace label for alerts and metrics.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>ruleNamespace</code><br/>
<em>
string
</em>
</td>
<td>
<p>ruleNamespace defines the namespace of the excluded PrometheusRule object.</p>
</td>
</tr>
<tr>
<td>
<code>ruleName</code><br/>
<em>
string
</em>
</td>
<td>
<p>ruleName defines the name of the excluded PrometheusRule object.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PrometheusRuleSpec">PrometheusRuleSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusRule">PrometheusRule</a>)
</p>
<div>
<p>PrometheusRuleSpec contains specification parameters for a Rule.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>groups</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RuleGroup">
[]RuleGroup
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>groups defines the content of Prometheus rule file</p>
</td>
</tr>
</tbody>
</table>
