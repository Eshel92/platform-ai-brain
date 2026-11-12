<!-- Part 17 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.Endpoint">Endpoint
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>)
</p>
<div>
<p>Endpoint defines an endpoint serving Prometheus metrics to be scraped by
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
<p>port defines the name of the Service port which this endpoint refers to
(e.g. <code>.spec.ports[].name</code>).</p>
<p>It takes precedence over <code>targetPort</code>.</p>
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
<p>targetPort defines the name or number of a container port on Pods selected
by the Service.
If a name, it matches against <code>.spec.containers[].ports[].name</code> of the Pods.
If a number, it matches against <code>.spec.containers[].ports[].containerPort</code> of the Pods.</p>
<p>Because it relies on Pod metadata, endpoints which aren&rsquo;t backed by Pods
are never scraped when <code>targetPort</code> is used.</p>
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
<p>scheme defines the HTTP scheme to use when scraping the metrics.</p>
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
<p>honorLabels defines when true the metric&rsquo;s labels when they collide
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
<code>bearerTokenFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>bearerTokenFile defines the file to read bearer token for scraping the target.</p>
<p>Deprecated: use <code>authorization</code> instead.</p>
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
<a href="#monitoring.coreos.com/v1.TLSConfig">
TLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines TLS configuration used by the client.</p>
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

<h3 id="monitoring.coreos.com/v1.Exemplars">Exemplars
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
<code>maxSize</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxSize defines the maximum number of exemplars stored in memory for all series.</p>
<p>exemplar-storage itself must be enabled using the <code>spec.enableFeature</code>
option for exemplars to be scraped in the first place.</p>
<p>If not set, Prometheus uses its default value. A value of zero or less
than zero disables the storage.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GRPCServerTLSConfig">GRPCServerTLSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>, <a href="#monitoring.coreos.com/v1.ThanosSpec">ThanosSpec</a>)
</p>
<div>
<p>GRPCServerTLSConfig defines TLS configuration for a gRPC server.</p>
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
<tr>
<td>
<code>caFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>caFile defines the path to the CA cert in the Prometheus container to use for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>certFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>certFile defines the path to the client cert file in the Prometheus container for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>keyFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>keyFile defines the path to the client key file in the Prometheus container for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>cipherSuites</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>cipherSuites defines the list of supported cipher suites for TLS
versions up to TLS 1.2.</p>
<p>If not defined, the Go default cipher suites are used.
Available cipher suites are documented in the Go documentation:
<a href="https://golang.org/pkg/crypto/tls/#pkg-constants">https://golang.org/pkg/crypto/tls/#pkg-constants</a></p>
<p>It requires Thanos &gt;= v0.42.0. Note that the operator doesn&rsquo;t verify if
the Thanos version supports the provided values.</p>
</td>
</tr>
<tr>
<td>
<code>curves</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>curves defines the list of preferred elliptic curves for
TLS handshakes.</p>
<p>If not defined, the Go default curves are used.
Available curves are documented in the Go documentation:
<a href="https://golang.org/pkg/crypto/tls/#CurveID">https://golang.org/pkg/crypto/tls/#CurveID</a></p>
<p>It requires Thanos &gt;= v0.42.0. Note that the operator doesn&rsquo;t verify if
the Thanos version supports the provided values.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalJiraConfig">GlobalJiraConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalJiraConfig configures global Jira parameters.</p>
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
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the default Jira API URL.</p>
<p>It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalMattermostConfig">GlobalMattermostConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalMattermostConfig configures global Mattermost parameters.</p>
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
<code>webhookURL</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>webhookURL defines the default Mattermost Webhook URL.</p>
<p>It requires Alertmanager &gt;= v0.32.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalRocketChatConfig">GlobalRocketChatConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalRocketChatConfig configures global Rocket Chat parameters.</p>
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
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the default Rocket Chat API URL.</p>
<p>It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>token</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>token defines the default Rocket Chat token.</p>
<p>It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>tokenID</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tokenID defines the default Rocket Chat Token ID.</p>
<p>It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalSMTPConfig">GlobalSMTPConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalSMTPConfig configures global SMTP parameters.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#configuration-file">https://prometheus.io/docs/alerting/latest/configuration/#configuration-file</a></p>
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
<code>from</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>from defines the default SMTP From header field.</p>
</td>
</tr>
<tr>
<td>
<code>smartHost</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.HostPort">
HostPort
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>smartHost defines the default SMTP smarthost used for sending emails.</p>
</td>
</tr>
<tr>
<td>
<code>hello</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>hello defines the default hostname to identify to the SMTP server.</p>
</td>
</tr>
<tr>
<td>
<code>authUsername</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>authUsername represents SMTP Auth using CRAM-MD5, LOGIN and PLAIN. If empty, Alertmanager doesn&rsquo;t authenticate to the SMTP server.</p>
</td>
</tr>
<tr>
<td>
<code>authPassword</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authPassword represents SMTP Auth using LOGIN and PLAIN.</p>
</td>
</tr>
<tr>
<td>
<code>authIdentity</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>authIdentity represents SMTP Auth using PLAIN</p>
</td>
</tr>
<tr>
<td>
<code>authSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authSecret represents SMTP Auth using CRAM-MD5.</p>
</td>
</tr>
<tr>
<td>
<code>requireTLS</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>requireTLS defines the default SMTP TLS requirement.
Note that Go does not support unencrypted connections to remote SMTP endpoints.</p>
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
<p>tlsConfig defines the default TLS configuration for SMTP receivers</p>
</td>
</tr>
<tr>
<td>
<code>forceImplicitTLS</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>forceImplicitTLS defines whether to force use of implicit TLS (direct TLS connection) for better security.
true: force use of implicit TLS (direct TLS connection on any port)
false: force disable implicit TLS (use explicit TLS/STARTTLS if required)
nil (default): auto-detect based on port (465=implicit, other=explicit) for backward compatibility
It requires Alertmanager &gt;= v0.31.0.</p>
</td>
</tr>
</tbody>
</table>
