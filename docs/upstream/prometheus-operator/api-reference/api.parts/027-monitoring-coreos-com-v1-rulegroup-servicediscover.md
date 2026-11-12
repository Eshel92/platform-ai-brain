<!-- Part 27 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.RuleGroup">RuleGroup
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusRuleSpec">PrometheusRuleSpec</a>)
</p>
<div>
<p>RuleGroup is a list of sequentially evaluated recording and alerting rules.</p>
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
<code>name</code><br/>
<em>
string
</em>
</td>
<td>
<p>name defines the name of the rule group.</p>
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
<p>labels define the labels to add or overwrite before storing the result for its rules.
The labels defined at the rule level take precedence.</p>
<p>It requires Prometheus &gt;= 3.0.0.
The field is ignored for Thanos Ruler.</p>
</td>
</tr>
<tr>
<td>
<code>interval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>interval defines how often rules in the group are evaluated.</p>
</td>
</tr>
<tr>
<td>
<code>query_offset</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>query_offset defines the offset the rule evaluation timestamp of this particular group by the specified duration into the past.</p>
<p>It requires Prometheus &gt;= v2.53.0.
It is not supported for ThanosRuler.</p>
</td>
</tr>
<tr>
<td>
<code>rules</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Rule">
[]Rule
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>rules defines the list of alerting and recording rules.</p>
</td>
</tr>
<tr>
<td>
<code>partial_response_strategy</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>partial_response_strategy is only used by ThanosRuler and will
be ignored by Prometheus instances.
More info: <a href="https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md#partial-response">https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md#partial-response</a></p>
</td>
</tr>
<tr>
<td>
<code>limit</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>limit defines the number of alerts an alerting rule and series a recording
rule can produce.
Limit is supported starting with Prometheus &gt;= 2.31 and Thanos Ruler &gt;= 0.24.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.Rules">Rules
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>)
</p>
<div>
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
<code>alert</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RulesAlert">
RulesAlert
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alert defines the parameters of the Prometheus rules&rsquo; engine.</p>
<p>Any update to these parameters trigger a restart of the pods.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RulesAlert">RulesAlert
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Rules">Rules</a>)
</p>
<div>
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
<code>forOutageTolerance</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>forOutageTolerance defines the max time to tolerate prometheus outage for restoring &lsquo;for&rsquo; state of
alert.</p>
</td>
</tr>
<tr>
<td>
<code>forGracePeriod</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>forGracePeriod defines the minimum duration between alert and restored &lsquo;for&rsquo; state.</p>
<p>This is maintained only for alerts with a configured &lsquo;for&rsquo; time greater
than the grace period.</p>
</td>
</tr>
<tr>
<td>
<code>resendDelay</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>resendDelay defines the minimum amount of time to wait before resending an alert to
Alertmanager.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RuntimeConfig">RuntimeConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
<p>RuntimeConfig configures the values for the process behavior.</p>
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
<code>goGC</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>goGC defines the Go garbage collection target percentage. Lowering this number may increase the CPU usage.
See: <a href="https://tip.golang.org/doc/gc-guide#GOGC">https://tip.golang.org/doc/gc-guide#GOGC</a></p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.SafeAuthorization">SafeAuthorization
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.Authorization">Authorization</a>, <a href="#monitoring.coreos.com/v1.HTTPConfigWithoutTLS">HTTPConfigWithoutTLS</a>, <a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DigitalOceanSDConfig">DigitalOceanSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">DockerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">DockerSwarmSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">HTTPSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HetznerSDConfig">HetznerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.IonosSDConfig">IonosSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">KubernetesSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">KumaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LightSailSDConfig">LightSailSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LinodeSDConfig">LinodeSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">NomadSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>, <a href="#monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig</a>)
</p>
<div>
<p>SafeAuthorization specifies a subset of the Authorization struct, that is
safe for use because it doesn&rsquo;t provide access to the Prometheus container&rsquo;s
filesystem.</p>
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
<code>type</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>type defines the authentication type. The value is case-insensitive.</p>
<p>&ldquo;Basic&rdquo; is not a supported value.</p>
<p>Default: &ldquo;Bearer&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>credentials</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>credentials defines a key of a Secret in the namespace that contains the credentials for authentication.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.SafeTLSConfig">SafeTLSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ClusterTLSConfig">ClusterTLSConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalSMTPConfig">GlobalSMTPConfig</a>, <a href="#monitoring.coreos.com/v1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1.OAuth2">OAuth2</a>, <a href="#monitoring.coreos.com/v1.TLSConfig">TLSConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DigitalOceanSDConfig">DigitalOceanSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">DockerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">DockerSwarmSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EC2SDConfig">EC2SDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EmailConfig">EmailConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">HTTPSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HetznerSDConfig">HetznerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.IonosSDConfig">IonosSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">KubernetesSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">KumaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LightSailSDConfig">LightSailSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LinodeSDConfig">LinodeSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">NomadSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.OpenStackSDConfig">OpenStackSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScalewaySDConfig">ScalewaySDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>, <a href="#monitoring.coreos.com/v1beta1.EmailConfig">EmailConfig</a>, <a href="#monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig</a>)
</p>
<div>
<p>SafeTLSConfig defines safe TLS configurations.</p>
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
<code>ca</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ca defines the Certificate authority used when verifying server certificates.</p>
</td>
</tr>
<tr>
<td>
<code>cert</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>cert defines the Client certificate to present when doing client-authentication.</p>
</td>
</tr>
<tr>
<td>
<code>keySecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>keySecret defines the Secret containing the client key file for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>serverName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>serverName is used to verify the hostname for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>insecureSkipVerify</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>insecureSkipVerify defines how to disable target certificate validation.</p>
</td>
</tr>
<tr>
<td>
<code>minVersion</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TLSVersion">
TLSVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>minVersion defines the minimum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.35.0 or Thanos &gt;= v0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>maxVersion</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TLSVersion">
TLSVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxVersion defines the maximum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.41.0 or Thanos &gt;= v0.31.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.Scheme">Scheme
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.Endpoint">Endpoint</a>, <a href="#monitoring.coreos.com/v1.PodMetricsEndpoint">PodMetricsEndpoint</a>, <a href="#monitoring.coreos.com/v1.ProberSpec">ProberSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>Supported values are <code>HTTP</code> and <code>HTTPS</code>. You can also rewrite the
<code>__scheme__</code> label via relabeling configuration.</p>
<p>If empty, the value defaults to <code>HTTP</code>.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;HTTP&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;HTTPS&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ScrapeClass">ScrapeClass
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
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
<code>name</code><br/>
<em>
string
</em>
</td>
<td>
<p>name of the scrape class.</p>
</td>
</tr>
<tr>
<td>
<code>default</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>default defines that the scrape applies to all scrape objects that
don&rsquo;t configure an explicit scrape class name.</p>
<p>Only one scrape class can be set as the default.</p>
</td>
</tr>
<tr>
<td>
<code>fallbackScrapeProtocol</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ScrapeProtocol">
ScrapeProtocol
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>fallbackScrapeProtocol defines the protocol to use if a scrape returns blank, unparseable, or otherwise invalid Content-Type.
It will only apply if the scrape resource doesn&rsquo;t specify any FallbackScrapeProtocol</p>
<p>It requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TLSConfig">
TLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines the TLS settings to use for the scrape. When the
scrape objects define their own CA, certificate and/or key, they take
precedence over the corresponding scrape class fields.</p>
<p>For now only the <code>caFile</code>, <code>certFile</code> and <code>keyFile</code> fields are supported.</p>
</td>
</tr>
<tr>
<td>
<code>authorization</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Authorization">
Authorization
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authorization section for the ScrapeClass.
It will only apply if the scrape resource doesn&rsquo;t specify any Authorization.</p>
</td>
</tr>
<tr>
<td>
<code>relabelings</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>relabelings defines the relabeling rules to apply to all scrape targets.</p>
<p>The Operator automatically adds relabelings for a few standard Kubernetes fields
like <code>__meta_kubernetes_namespace</code> and <code>__meta_kubernetes_service_name</code>.
Then the Operator adds the scrape class relabelings defined here.
Then the Operator adds the target-specific relabelings defined in the scrape object.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p>
</td>
</tr>
<tr>
<td>
<code>metricRelabelings</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>metricRelabelings defines the relabeling rules to apply to all samples before ingestion.</p>
<p>The Operator adds the scrape class metric relabelings defined here.
Then the Operator adds the target-specific metric relabelings defined in ServiceMonitors, PodMonitors, Probes and ScrapeConfigs.
Then the Operator adds namespace enforcement relabeling rule, specified in &lsquo;.spec.enforcedNamespaceLabel&rsquo;.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs</a></p>
</td>
</tr>
<tr>
<td>
<code>attachMetadata</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AttachMetadata">
AttachMetadata
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>attachMetadata defines additional metadata to the discovered targets.
When the scrape object defines its own configuration, it takes
precedence over the scrape class configuration.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ScrapeProtocol">ScrapeProtocol
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>, <a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>, <a href="#monitoring.coreos.com/v1.ScrapeClass">ScrapeClass</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>ScrapeProtocol represents a protocol used by Prometheus for scraping metrics.
Supported values are:
* <code>OpenMetricsText0.0.1</code>
* <code>OpenMetricsText1.0.0</code>
* <code>PrometheusProto</code>
* <code>PrometheusText0.0.4</code>
* <code>PrometheusText1.0.0</code></p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;OpenMetricsText0.0.1&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;OpenMetricsText1.0.0&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;PrometheusProto&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;PrometheusText0.0.4&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;PrometheusText1.0.0&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.SecretOrConfigMap">SecretOrConfigMap
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerConfiguration">AlertmanagerConfiguration</a>, <a href="#monitoring.coreos.com/v1.OAuth2">OAuth2</a>, <a href="#monitoring.coreos.com/v1.SafeTLSConfig">SafeTLSConfig</a>, <a href="#monitoring.coreos.com/v1.WebTLSConfig">WebTLSConfig</a>)
</p>
<div>
<p>SecretOrConfigMap allows to specify data as a Secret or ConfigMap. Fields are mutually exclusive.</p>
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
<code>secret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>secret defines the Secret containing data to use for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>configMap</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#configmapkeyselector-v1-core">
Kubernetes core/v1.ConfigMapKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>configMap defines the ConfigMap containing data to use for the targets.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.SelectorMechanism">SelectorMechanism
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>)
</p>
<div>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;RelabelConfig&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;RoleSelector&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ServiceDiscoveryRole">ServiceDiscoveryRole
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>)
</p>
<div>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;EndpointSlice&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Endpoints&#34;</p></td>
<td></td>
</tr></tbody>
</table>
