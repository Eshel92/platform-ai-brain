<!-- Part 20 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.OTLPConfig">OTLPConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
<p>OTLPConfig is the configuration for writing to the OTLP endpoint.</p>
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
<code>promoteAllResourceAttributes</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>promoteAllResourceAttributes promotes all resource attributes to metric labels except the ones defined in <code>ignoreResourceAttributes</code>.</p>
<p>Cannot be true when <code>promoteResourceAttributes</code> is defined.
It requires Prometheus &gt;= v3.5.0.</p>
</td>
</tr>
<tr>
<td>
<code>ignoreResourceAttributes</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>ignoreResourceAttributes defines the list of OpenTelemetry resource attributes to ignore when <code>promoteAllResourceAttributes</code> is true.</p>
<p>It requires <code>promoteAllResourceAttributes</code> to be true.
It requires Prometheus &gt;= v3.5.0.</p>
</td>
</tr>
<tr>
<td>
<code>promoteResourceAttributes</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>promoteResourceAttributes defines the list of OpenTelemetry Attributes that should be promoted to metric labels, defaults to none.
Cannot be defined when <code>promoteAllResourceAttributes</code> is true.</p>
</td>
</tr>
<tr>
<td>
<code>translationStrategy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TranslationStrategyOption">
TranslationStrategyOption
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>translationStrategy defines how the OTLP receiver endpoint translates the incoming metrics.</p>
<p>It requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>keepIdentifyingResourceAttributes</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>keepIdentifyingResourceAttributes enables adding <code>service.name</code>, <code>service.namespace</code> and <code>service.instance.id</code>
resource attributes to the <code>target_info</code> metric, on top of converting them into the <code>instance</code> and <code>job</code> labels.</p>
<p>It requires Prometheus &gt;= v3.1.0.</p>
</td>
</tr>
<tr>
<td>
<code>convertHistogramsToNHCB</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>convertHistogramsToNHCB defines optional translation of OTLP explicit bucket histograms into native histograms with custom buckets.
It requires Prometheus &gt;= v3.4.0.</p>
</td>
</tr>
<tr>
<td>
<code>promoteScopeMetadata</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>promoteScopeMetadata controls whether to promote OpenTelemetry scope metadata (i.e. name, version, schema URL, and attributes) to metric labels.
As per the OpenTelemetry specification, the aforementioned scope metadata should be identifying, i.e. made into metric labels.
It requires Prometheus &gt;= v3.6.0.</p>
</td>
</tr>
<tr>
<td>
<code>labelNameUnderscoreSanitization</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>labelNameUnderscoreSanitization controls whether to enable prepending of &lsquo;key<em>&rsquo; to labels starting with &lsquo;</em>&rsquo;.
Reserved labels starting with &lsquo;__&rsquo; are not modified.
This is only relevant when translation_strategy uses underscore escaping (e.g., &ldquo;UnderscoreEscapingWithSuffixes&rdquo; or &ldquo;UnderscoreEscapingWithoutSuffixes&rdquo;).</p>
<p>Notice: This one has no impact if <code>nameEscapingScheme</code> is <code>AllowUTF8</code>.</p>
<p>It requires Prometheus &gt;= v3.8.0.</p>
</td>
</tr>
<tr>
<td>
<code>labelNamePreserveMultipleUnderscores</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>labelNamePreserveMultipleUnderscores enables preserving of multiple consecutive underscores in label names when translation_strategy uses
underscore escaping.
When true (default), multiple consecutive underscores are preserved during label name sanitization.</p>
<p>Notice: This one has no impact if <code>nameEscapingScheme</code> is <code>AllowUTF8</code>.</p>
<p>It requires Prometheus &gt;= v3.8.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ObjectReference">ObjectReference
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>ObjectReference references a PodMonitor, ServiceMonitor, Probe or PrometheusRule object.</p>
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
<code>group</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>group of the referent. When not specified, it defaults to <code>monitoring.coreos.com</code></p>
</td>
</tr>
<tr>
<td>
<code>resource</code><br/>
<em>
string
</em>
</td>
<td>
<p>resource of the referent.</p>
</td>
</tr>
<tr>
<td>
<code>namespace</code><br/>
<em>
string
</em>
</td>
<td>
<p>namespace of the referent.
More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/</a></p>
</td>
</tr>
<tr>
<td>
<code>name</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>name of the referent. When not set, all resources in the namespace are matched.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PodDNSConfig">PodDNSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>PodDNSConfig defines the DNS parameters of a pod in addition to
those generated from DNSPolicy.</p>
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
<code>nameservers</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>nameservers defines the list of DNS name server IP addresses.
This will be appended to the base nameservers generated from DNSPolicy.</p>
</td>
</tr>
<tr>
<td>
<code>searches</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>searches defines the list of DNS search domains for host-name lookup.
This will be appended to the base search paths generated from DNSPolicy.</p>
</td>
</tr>
<tr>
<td>
<code>options</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PodDNSConfigOption">
[]PodDNSConfigOption
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>options defines the list of DNS resolver options.
This will be merged with the base options generated from DNSPolicy.
Resolution options given in Options
will override those that appear in the base DNSPolicy.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PodDNSConfigOption">PodDNSConfigOption
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodDNSConfig">PodDNSConfig</a>)
</p>
<div>
<p>PodDNSConfigOption defines DNS resolver options of a pod.</p>
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
<p>name is required and must be unique.</p>
</td>
</tr>
<tr>
<td>
<code>value</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>value is optional.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PodManagementPolicyType">PodManagementPolicyType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
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
<tbody><tr><td><p>&#34;OrderedReady&#34;</p></td>
<td><p>OrderedReadyPodManagement will create pods in strictly increasing order on
scale up and strictly decreasing order on scale down, progressing only when
the previous pod is ready or terminated. At most one pod will be changed
at any time.</p>
</td>
</tr><tr><td><p>&#34;Parallel&#34;</p></td>
<td><p>ParallelPodManagement will create and delete pods as soon as the stateful set
replica count is changed, and will not wait for pods to be ready or complete
termination.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.PodMetricsEndpoint">PodMetricsEndpoint
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>)
</p>
<div>
<p>PodMetricsEndpoint defines an endpoint serving Prometheus metrics to be scraped by
Prometheus.</p>
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
<code>port</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>port defines the <code>Pod</code> port name which exposes the endpoint.</p>
<p>If the pod doesn&rsquo;t expose a port with the same name, it will result
in no targets being discovered.</p>
<p>If a <code>Pod</code> has multiple <code>Port</code>s with the same name (which is not
recommended), one target instance per unique port number will be
generated.</p>
<p>It takes precedence over the <code>portNumber</code> and <code>targetPort</code> fields.</p>
</td>
</tr>
<tr>
<td>
<code>portNumber</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>portNumber defines the <code>Pod</code> port number which exposes the endpoint.</p>
<p>The <code>Pod</code> must declare the specified <code>Port</code> in its spec or the
target will be dropped by Prometheus.</p>
<p>This cannot be used to enable scraping of an undeclared port.
To scrape targets on a port which isn&rsquo;t exposed, you need to use
relabeling to override the <code>__address__</code> label (but beware of
duplicate targets if the <code>Pod</code> has other declared ports).</p>
<p>In practice Prometheus will select targets for which the
matches the target&rsquo;s __meta_kubernetes_pod_container_port_number.</p>
</td>
</tr>
<tr>
<td>
<code>targetPort</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/util/intstr#IntOrString">
k8s.io/apimachinery/pkg/util/intstr.IntOrString
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>targetPort defines the name or number of the target port of the <code>Pod</code> object behind the Service, the
port must be specified with container port property.</p>
<p>Deprecated: use &lsquo;port&rsquo; or &lsquo;portNumber&rsquo; instead.</p>
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
<p>path defines the HTTP path from which to scrape for metrics.</p>
<p>If empty, Prometheus uses the default value (e.g. <code>/metrics</code>).</p>
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
<p>scheme defines the HTTP scheme to use for scraping.</p>
</td>
</tr>
<tr>
<td>
<code>params</code><br/>
<em>
map[string][]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>params define optional HTTP URL parameters.</p>
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
<p>interval at which Prometheus scrapes the metrics from the target.</p>
<p>If empty, Prometheus uses the global scrape interval.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeTimeout defines the timeout after which Prometheus considers the scrape to be failed.</p>
<p>If empty, Prometheus uses the global scrape timeout unless it is less
than the target&rsquo;s scrape interval value in which the latter is used.
The value cannot be greater than the scrape interval otherwise the operator will reject the resource.</p>
</td>
</tr>
<tr>
<td>
<code>honorLabels</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>honorLabels when true preserves the metric&rsquo;s labels when they collide
with the target&rsquo;s labels.</p>
</td>
</tr>
<tr>
<td>
<code>honorTimestamps</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>honorTimestamps defines whether Prometheus preserves the timestamps
when exposed by the target.</p>
</td>
</tr>
<tr>
<td>
<code>trackTimestampsStaleness</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>trackTimestampsStaleness defines whether Prometheus tracks staleness of
the metrics that have an explicit timestamp present in scraped data.
Has no effect if <code>honorTimestamps</code> is false.</p>
<p>It requires Prometheus &gt;= v2.48.0.</p>
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
<p>metricRelabelings defines the relabeling rules to apply to the
samples before ingestion.</p>
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
<p>relabelings defines the relabeling rules to apply the target&rsquo;s
metadata labels.</p>
<p>The Operator automatically adds relabelings for a few standard Kubernetes fields.</p>
<p>The original scrape job&rsquo;s name is available via the <code>__tmp_prometheus_job_name</code> label.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p>
</td>
</tr>
<tr>
<td>
<code>filterRunning</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>filterRunning when true, the pods which are not running (e.g. either in Failed or
Succeeded state) are dropped during the target discovery.</p>
<p>If unset, the filtering is enabled.</p>
<p>More info: <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase">https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase</a></p>
</td>
</tr>
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
<p>tlsConfig defines the TLS configuration used by the client.</p>
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
