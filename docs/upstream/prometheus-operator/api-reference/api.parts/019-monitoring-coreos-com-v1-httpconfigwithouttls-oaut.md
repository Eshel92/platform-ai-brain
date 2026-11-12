<!-- Part 19 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.HTTPConfigWithoutTLS">HTTPConfigWithoutTLS
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1.HTTPConfigWithTLSFiles">HTTPConfigWithTLSFiles</a>)
</p>
<div>
<p>HTTPConfigWithoutTLS defines the configuration for the HTTP client.</p>
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
<code>authorization</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SafeAuthorization">
SafeAuthorization
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authorization configures the Authorization header credentials used by
the client.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>bearerTokenSecret</code> or <code>oauth2</code>.</p>
</td>
</tr>
<tr>
<td>
<code>basicAuth</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.BasicAuth">
BasicAuth
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>basicAuth defines the Basic Authentication credentials used by the
client.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>bearerTokenSecret</code> or <code>oauth2</code>.</p>
</td>
</tr>
<tr>
<td>
<code>oauth2</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.OAuth2">
OAuth2
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>oauth2 defines the OAuth2 settings used by the client.</p>
<p>It requires Prometheus &gt;= 2.27.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code> or <code>bearerTokenSecret</code>.</p>
</td>
</tr>
<tr>
<td>
<code>bearerTokenSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>bearerTokenSecret defines a key of a Secret containing the bearer token
used by the client for authentication. The secret needs to be in the
same namespace as the custom resource and readable by the Prometheus
Operator.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code> or <code>oauth2</code>.</p>
<p>Deprecated: use <code>authorization</code> instead.</p>
</td>
</tr>
<tr>
<td>
<code>followRedirects</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>followRedirects defines whether the client should follow HTTP 3xx
redirects.</p>
</td>
</tr>
<tr>
<td>
<code>enableHttp2</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableHttp2 can be used to disable HTTP2.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.HostAlias">HostAlias
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the
pod&rsquo;s hosts file.</p>
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
<code>ip</code><br/>
<em>
string
</em>
</td>
<td>
<p>ip defines the IP address of the host file entry.</p>
</td>
</tr>
<tr>
<td>
<code>hostnames</code><br/>
<em>
[]string
</em>
</td>
<td>
<p>hostnames defines hostnames for the above IP address.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.HostPort">HostPort
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.GlobalSMTPConfig">GlobalSMTPConfig</a>)
</p>
<div>
<p>HostPort represents a &ldquo;host:port&rdquo; network address.</p>
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
<code>host</code><br/>
<em>
string
</em>
</td>
<td>
<p>host defines the host&rsquo;s address, it can be a DNS name or a literal IP address.</p>
</td>
</tr>
<tr>
<td>
<code>port</code><br/>
<em>
string
</em>
</td>
<td>
<p>port defines the host&rsquo;s port, it can be a literal port number or a port name.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.LabelName">LabelName
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.RelabelConfig">RelabelConfig</a>)
</p>
<div>
<p>LabelName is a valid Prometheus label name.
For Prometheus 3.x, a label name is valid if it contains UTF-8 characters.
For Prometheus 2.x, a label name is only valid if it contains ASCII characters, letters, numbers, as well as underscores.</p>
</div>

<h3 id="monitoring.coreos.com/v1.ManagedIdentity">ManagedIdentity
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AzureAD">AzureAD</a>)
</p>
<div>
<p>ManagedIdentity defines the Azure User-assigned Managed identity.</p>
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
<code>clientId</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientId defines the Azure User-assigned Managed identity.</p>
<p>For Prometheus &gt;= 3.5.0 and Thanos &gt;= 0.40.0, this field is allowed to be empty to support system-assigned managed identities.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.MetadataConfig">MetadataConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>)
</p>
<div>
<p>MetadataConfig configures the sending of series metadata to the remote storage.</p>
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
<code>send</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>send defines whether metric metadata is sent to the remote storage or not.</p>
<p>The setting is ignored when Remote Write message&rsquo;s version 2.0 is used.</p>
</td>
</tr>
<tr>
<td>
<code>sendInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendInterval defines how frequently metric metadata is sent to the remote storage.</p>
</td>
</tr>
<tr>
<td>
<code>maxSamplesPerSend</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxSamplesPerSend defines the maximum number of metadata samples per send.</p>
<p>It requires Prometheus &gt;= v2.29.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.NameEscapingSchemeOptions">NameEscapingSchemeOptions
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>Specifies the character escaping scheme that will be applied when scraping
for metric and label names that do not conform to the legacy Prometheus
character set.</p>
<p>Supported values are:</p>
<ul>
<li><code>AllowUTF8</code>, full UTF-8 support, no escaping needed.</li>
<li><code>Underscores</code>, legacy-invalid characters are escaped to underscores.</li>
<li><code>Dots</code>, dot characters are escaped to <code>_dot_</code>, underscores to <code>__</code>, and
all other legacy-invalid characters to underscores.</li>
<li><code>Values</code>, the string is prefixed by <code>U__</code> and all invalid characters are
escaped to their unicode value, surrounded by underscores.</li>
</ul>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;AllowUTF8&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Dots&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Underscores&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Values&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.NameValidationSchemeOptions">NameValidationSchemeOptions
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>Specifies the validation scheme for metric and label names.</p>
<p>Supported values are:
- <code>UTF8NameValidationScheme</code> for UTF-8 support.
- <code>LegacyNameValidationScheme</code> for letters, numbers, colons, and underscores.</p>
<p>Note that <code>LegacyNameValidationScheme</code> cannot be used along with the
OpenTelemetry <code>NoUTF8EscapingWithSuffixes</code> translation strategy (if
enabled).</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;Legacy&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;UTF8&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.NamespaceSelector">NamespaceSelector
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>, <a href="#monitoring.coreos.com/v1.ProbeTargetIngress">ProbeTargetIngress</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>)
</p>
<div>
<p>NamespaceSelector is a selector for selecting either all namespaces or a
list of namespaces.
If <code>any</code> is true, it takes precedence over <code>matchNames</code>.
If <code>matchNames</code> is empty and <code>any</code> is false, it means that the objects are
selected from the current namespace.</p>
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
<code>any</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>any defines the boolean describing whether all namespaces are selected in contrast to a
list restricting them.</p>
</td>
</tr>
<tr>
<td>
<code>matchNames</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>matchNames defines the list of namespace names to select from.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.NativeHistogramConfig">NativeHistogramConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>, <a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>NativeHistogramConfig extends the native histogram configuration settings.</p>
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
<code>scrapeNativeHistograms</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeNativeHistograms defines whether to enable scraping of native histograms.
It requires Prometheus &gt;= v3.8.0.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeClassicHistograms</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeClassicHistograms defines whether to scrape a classic histogram that is also exposed as a native histogram.
It requires Prometheus &gt;= v2.45.0.</p>
<p>Notice: <code>scrapeClassicHistograms</code> corresponds to the <code>always_scrape_classic_histograms</code> field in the Prometheus configuration.</p>
</td>
</tr>
<tr>
<td>
<code>nativeHistogramBucketLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>nativeHistogramBucketLimit defines ff there are more than this many buckets in a native histogram,
buckets will be merged to stay within the limit.
It requires Prometheus &gt;= v2.45.0.</p>
</td>
</tr>
<tr>
<td>
<code>nativeHistogramMinBucketFactor</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity">
k8s.io/apimachinery/pkg/api/resource.Quantity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>nativeHistogramMinBucketFactor defines if the growth factor of one bucket to the next is smaller than this,
buckets will be merged to increase the factor sufficiently.
It requires Prometheus &gt;= v2.50.0.</p>
</td>
</tr>
<tr>
<td>
<code>convertClassicHistogramsToNHCB</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>convertClassicHistogramsToNHCB defines whether to convert all scraped classic histograms into a native histogram with custom buckets.
It requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.NonEmptyDuration">NonEmptyDuration
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Rule">Rule</a>, <a href="#monitoring.coreos.com/v1alpha1.Route">Route</a>, <a href="#monitoring.coreos.com/v1beta1.Route">Route</a>)
</p>
<div>
<p>NonEmptyDuration is a valid time duration that can be parsed by Prometheus model.ParseDuration() function.
Compared to Duration,  NonEmptyDuration enforces a minimum length of 1.
Supported units: y, w, d, h, m, s, ms
Examples: <code>30s</code>, <code>1m</code>, <code>1h20m15s</code>, <code>15d</code></p>
</div>

<h3 id="monitoring.coreos.com/v1.OAuth2">OAuth2
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.HTTPConfigWithoutTLS">HTTPConfigWithoutTLS</a>, <a href="#monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DigitalOceanSDConfig">DigitalOceanSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">DockerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">DockerSwarmSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">HTTPSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HetznerSDConfig">HetznerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.IonosSDConfig">IonosSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">KubernetesSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">KumaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LightSailSDConfig">LightSailSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LinodeSDConfig">LinodeSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">NomadSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>, <a href="#monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig</a>)
</p>
<div>
<p>OAuth2 configures OAuth2 settings.</p>
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
<code>clientId</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<p>clientId defines a key of a Secret or ConfigMap containing the
OAuth2 client&rsquo;s ID.</p>
</td>
</tr>
<tr>
<td>
<code>clientSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<p>clientSecret defines a key of a Secret containing the OAuth2
client&rsquo;s secret.</p>
</td>
</tr>
<tr>
<td>
<code>tokenUrl</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<p>tokenUrl defines the URL to fetch the token from.</p>
</td>
</tr>
<tr>
<td>
<code>scopes</code><br/>
<em>
[]string
</em>
</td>
<td>
<p>scopes defines the OAuth2 scopes used for the token request.</p>
</td>
</tr>
<tr>
<td>
<code>endpointParams</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>endpointParams configures the HTTP parameters to append to the token
URL.</p>
</td>
</tr>
<tr>
<td>
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SafeTLSConfig">
SafeTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines the TLS configuration to use when connecting to the OAuth2 server.
It requires Prometheus &gt;= v2.43.0.</p>
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
