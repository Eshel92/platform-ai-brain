<!-- Part 25 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.PrometheusStatus">PrometheusStatus
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Prometheus">Prometheus</a>, <a href="#monitoring.coreos.com/v1alpha1.PrometheusAgent">PrometheusAgent</a>)
</p>
<div>
<p>PrometheusStatus is the most recent observed status of the Prometheus cluster.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
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
<code>paused</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>paused defines whether any actions on the underlying managed objects are
being performed. Only delete actions will be performed.</p>
</td>
</tr>
<tr>
<td>
<code>replicas</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>replicas defines the total number of non-terminated pods targeted by this Prometheus deployment
(their labels match the selector).</p>
</td>
</tr>
<tr>
<td>
<code>updatedReplicas</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>updatedReplicas defines the total number of non-terminated pods targeted by this Prometheus deployment
that have the desired version spec.</p>
</td>
</tr>
<tr>
<td>
<code>availableReplicas</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>availableReplicas defines the total number of available pods (ready for at least minReadySeconds)
targeted by this Prometheus deployment.</p>
</td>
</tr>
<tr>
<td>
<code>unavailableReplicas</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>unavailableReplicas defines the total number of unavailable pods targeted by this Prometheus deployment.</p>
</td>
</tr>
<tr>
<td>
<code>conditions</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Condition">
[]Condition
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>conditions defines the current state of the Prometheus deployment.</p>
</td>
</tr>
<tr>
<td>
<code>shardStatuses</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ShardStatus">
[]ShardStatus
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>shardStatuses defines the list has one entry per shard. Each entry provides a summary of the shard status.</p>
</td>
</tr>
<tr>
<td>
<code>shards</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>shards defines the most recently observed number of shards.</p>
</td>
</tr>
<tr>
<td>
<code>selector</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>selector used to match the pods targeted by this Prometheus resource.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PrometheusWebSpec">PrometheusWebSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
<p>PrometheusWebSpec defines the configuration of the Prometheus web server.</p>
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
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WebTLSConfig">
WebTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines the TLS parameters for HTTPS.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WebHTTPConfig">
WebHTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines HTTP parameters for web server.</p>
</td>
</tr>
<tr>
<td>
<code>pageTitle</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>pageTitle defines the prometheus web page title.</p>
</td>
</tr>
<tr>
<td>
<code>maxConnections</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxConnections defines the maximum number of simultaneous connections
A zero value means that Prometheus doesn&rsquo;t accept any incoming connection.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ProxyConfig">ProxyConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.APIServerConfig">APIServerConfig</a>, <a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.HTTPConfigWithProxy">HTTPConfigWithProxy</a>, <a href="#monitoring.coreos.com/v1.HTTPConfigWithProxyAndTLSFiles">HTTPConfigWithProxyAndTLSFiles</a>, <a href="#monitoring.coreos.com/v1.OAuth2">OAuth2</a>, <a href="#monitoring.coreos.com/v1.ProberSpec">ProberSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DigitalOceanSDConfig">DigitalOceanSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">DockerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">DockerSwarmSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EC2SDConfig">EC2SDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">HTTPSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HetznerSDConfig">HetznerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.IonosSDConfig">IonosSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">KubernetesSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">KumaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LightSailSDConfig">LightSailSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LinodeSDConfig">LinodeSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">NomadSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScalewaySDConfig">ScalewaySDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>, <a href="#monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig</a>)
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

<h3 id="monitoring.coreos.com/v1.QuerySpec">QuerySpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>)
</p>
<div>
<p>QuerySpec defines the query command line flags when starting Prometheus.</p>
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
<code>lookbackDelta</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>lookbackDelta defines the delta difference allowed for retrieving metrics during expression evaluations.</p>
</td>
</tr>
<tr>
<td>
<code>maxConcurrency</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxConcurrency defines the number of concurrent queries that can be run at once.</p>
</td>
</tr>
<tr>
<td>
<code>maxSamples</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxSamples defines the maximum number of samples a single query can load into memory. Note that
queries will fail if they would load more samples than this into memory,
so this also limits the number of samples a query can return.</p>
</td>
</tr>
<tr>
<td>
<code>timeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>timeout defines the maximum time a query may take before being aborted.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.QueueConfig">QueueConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>)
</p>
<div>
<p>QueueConfig allows the tuning of remote write&rsquo;s queue_config parameters.
This object is referenced in the RemoteWriteSpec object.</p>
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
<code>capacity</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>capacity defines the number of samples to buffer per shard before we start
dropping them.</p>
</td>
</tr>
<tr>
<td>
<code>minShards</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>minShards defines the minimum number of shards, i.e. amount of concurrency.</p>
</td>
</tr>
<tr>
<td>
<code>maxShards</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxShards defines the maximum number of shards, i.e. amount of concurrency.</p>
</td>
</tr>
<tr>
<td>
<code>maxSamplesPerSend</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxSamplesPerSend defines the maximum number of samples per send.</p>
</td>
</tr>
<tr>
<td>
<code>batchSendDeadline</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>batchSendDeadline defines the maximum time a sample will wait in buffer.</p>
</td>
</tr>
<tr>
<td>
<code>maxRetries</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxRetries defines the maximum number of times to retry a batch on recoverable errors.</p>
</td>
</tr>
<tr>
<td>
<code>minBackoff</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>minBackoff defines the initial retry delay. Gets doubled for every retry.</p>
</td>
</tr>
<tr>
<td>
<code>maxBackoff</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxBackoff defines the maximum retry delay.</p>
</td>
</tr>
<tr>
<td>
<code>retryOnRateLimit</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>retryOnRateLimit defines the retry upon receiving a 429 status code from the remote-write storage.</p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
</td>
</tr>
<tr>
<td>
<code>sampleAgeLimit</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>sampleAgeLimit drops samples older than the limit.
It requires Prometheus &gt;= v2.50.0 or Thanos &gt;= v0.32.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RelabelConfig">RelabelConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.Endpoint">Endpoint</a>, <a href="#monitoring.coreos.com/v1.PodMetricsEndpoint">PodMetricsEndpoint</a>, <a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>, <a href="#monitoring.coreos.com/v1.ProbeTargetIngress">ProbeTargetIngress</a>, <a href="#monitoring.coreos.com/v1.ProbeTargetStaticConfig">ProbeTargetStaticConfig</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1.ScrapeClass">ScrapeClass</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>RelabelConfig allows dynamic rewriting of the label set for targets, alerts,
scraped samples and remote write samples.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p>
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
<code>sourceLabels</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.LabelName">
[]LabelName
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>sourceLabels defines the source labels select values from existing labels. Their content is
concatenated using the configured Separator and matched against the
configured regular expression.</p>
</td>
</tr>
<tr>
<td>
<code>separator</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>separator defines the string between concatenated SourceLabels.</p>
</td>
</tr>
<tr>
<td>
<code>targetLabel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>targetLabel defines the label to which the resulting string is written in a replacement.</p>
<p>It is mandatory for <code>Replace</code>, <code>HashMod</code>, <code>Lowercase</code>, <code>Uppercase</code>,
<code>KeepEqual</code> and <code>DropEqual</code> actions.</p>
<p>Regex capture groups are available.</p>
</td>
</tr>
<tr>
<td>
<code>regex</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>regex defines the regular expression against which the extracted value is matched.</p>
</td>
</tr>
<tr>
<td>
<code>modulus</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>modulus to take of the hash of the source label values.</p>
<p>Only applicable when the action is <code>HashMod</code>.</p>
</td>
</tr>
<tr>
<td>
<code>replacement</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>replacement value against which a Replace action is performed if the
regular expression matches.</p>
<p>Regex capture groups are available.</p>
</td>
</tr>
<tr>
<td>
<code>action</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>action to perform based on the regex matching.</p>
<p><code>Uppercase</code> and <code>Lowercase</code> actions require Prometheus &gt;= v2.36.0.
<code>DropEqual</code> and <code>KeepEqual</code> actions require Prometheus &gt;= v2.41.0.</p>
<p>Default: &ldquo;Replace&rdquo;</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ReloadStrategyType">ReloadStrategyType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
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
<tbody><tr><td><p>&#34;HTTP&#34;</p></td>
<td><p>HTTPReloadStrategyType reloads the configuration using the /-/reload HTTP endpoint.</p>
</td>
</tr><tr><td><p>&#34;ProcessSignal&#34;</p></td>
<td><p>ProcessSignalReloadStrategyType reloads the configuration by sending a SIGHUP signal to the process.</p>
</td>
</tr></tbody>
</table>
