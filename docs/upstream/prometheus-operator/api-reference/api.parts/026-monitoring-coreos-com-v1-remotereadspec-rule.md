<!-- Part 26 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>)
</p>
<div>
<p>RemoteReadSpec defines the configuration for Prometheus to read back samples
from a remote endpoint.</p>
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
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<p>url defines the URL of the endpoint to query from.</p>
<p>It must use the HTTP or HTTPS scheme.</p>
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
<p>name of the remote read queue, it must be unique if specified. The
name is used in metrics and logging in order to differentiate read
configurations.</p>
<p>It requires Prometheus &gt;= v2.15.0.</p>
</td>
</tr>
<tr>
<td>
<code>requiredMatchers</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>requiredMatchers defines an optional list of equality matchers which have to be present
in a selector to query the remote read endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>remoteTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>remoteTimeout defines the timeout for requests to the remote read endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>headers</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>headers defines the custom HTTP headers to be sent along with each remote read request.
Be aware that headers that are set by Prometheus itself can&rsquo;t be overwritten.
Only valid in Prometheus versions 2.26.0 and newer.</p>
</td>
</tr>
<tr>
<td>
<code>readRecent</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>readRecent defines whether reads should be made for queries for time ranges that
the local storage should have complete data for.</p>
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
<p>oauth2 configuration for the URL.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, or <code>basicAuth</code>.</p>
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
<p>basicAuth configuration for the URL.</p>
<p>Cannot be set at the same time as <code>authorization</code>, or <code>oauth2</code>.</p>
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
<p>bearerTokenFile defines the file from which to read the bearer token for the URL.</p>
<p>Deprecated: this will be removed in a future release. Prefer using <code>authorization</code>.</p>
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
<p>authorization section for the URL.</p>
<p>It requires Prometheus &gt;= v2.26.0.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, or <code>oauth2</code>.</p>
</td>
</tr>
<tr>
<td>
<code>bearerToken</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>bearerToken is deprecated: this will be removed in a future release.
<em>Warning: this field shouldn&rsquo;t be used because the token value appears
in clear-text. Prefer using <code>authorization</code>.</em></p>
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
<p>tlsConfig to use for the URL.</p>
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
<tr>
<td>
<code>followRedirects</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>followRedirects defines whether HTTP requests follow HTTP 3xx redirects.</p>
<p>It requires Prometheus &gt;= v2.26.0.</p>
</td>
</tr>
<tr>
<td>
<code>filterExternalLabels</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>filterExternalLabels defines whether to use the external labels as selectors for the remote read endpoint.</p>
<p>It requires Prometheus &gt;= v2.34.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RemoteWriteMessageVersion">RemoteWriteMessageVersion
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>)
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
<tbody><tr><td><p>&#34;V1.0&#34;</p></td>
<td><p>Remote Write message&rsquo;s version 1.0.</p>
</td>
</tr><tr><td><p>&#34;V2.0&#34;</p></td>
<td><p>Remote Write message&rsquo;s version 2.0.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>RemoteWriteSpec defines the configuration to write samples from Prometheus
to a remote endpoint.</p>
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
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<p>url defines the URL of the endpoint to send samples to.</p>
<p>It must use the HTTP or HTTPS scheme.</p>
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
<p>name of the remote write queue, it must be unique if specified. The
name is used in metrics and logging in order to differentiate queues.</p>
<p>It requires Prometheus &gt;= v2.15.0 or Thanos &gt;= 0.24.0.</p>
</td>
</tr>
<tr>
<td>
<code>messageVersion</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RemoteWriteMessageVersion">
RemoteWriteMessageVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>messageVersion defines the Remote Write message&rsquo;s version to use when writing to the endpoint.</p>
<p><code>Version1.0</code> corresponds to the <code>prometheus.WriteRequest</code> protobuf message introduced in Remote Write 1.0.
<code>Version2.0</code> corresponds to the <code>io.prometheus.write.v2.Request</code> protobuf message introduced in Remote Write 2.0.</p>
<p>When <code>Version2.0</code> is selected, Prometheus will automatically be
configured to append the metadata of scraped metrics to the WAL.</p>
<p>Before setting this field, consult with your remote storage provider
what message version it supports.</p>
<p>It requires Prometheus &gt;= v2.54.0 or Thanos &gt;= v0.37.0.</p>
</td>
</tr>
<tr>
<td>
<code>sendExemplars</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendExemplars enables sending of exemplars over remote write. Note that
exemplar-storage itself must be enabled using the <code>spec.enableFeatures</code>
option for exemplars to be scraped in the first place.</p>
<p>It requires Prometheus &gt;= v2.27.0 or Thanos &gt;= v0.24.0.</p>
</td>
</tr>
<tr>
<td>
<code>sendNativeHistograms</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendNativeHistograms enables sending of native histograms, also known as sparse histograms
over remote write.</p>
<p>It requires Prometheus &gt;= v2.40.0 or Thanos &gt;= v0.30.0.</p>
</td>
</tr>
<tr>
<td>
<code>remoteTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>remoteTimeout defines the timeout for requests to the remote write endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>headers</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>headers defines the custom HTTP headers to be sent along with each remote write request.
Be aware that headers that are set by Prometheus itself can&rsquo;t be overwritten.</p>
<p>It requires Prometheus &gt;= v2.25.0 or Thanos &gt;= v0.24.0.</p>
</td>
</tr>
<tr>
<td>
<code>writeRelabelConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>writeRelabelConfigs defines the list of remote write relabel configurations.</p>
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
<p>oauth2 configuration for the URL.</p>
<p>It requires Prometheus &gt;= v2.27.0 or Thanos &gt;= v0.24.0.</p>
<p>Cannot be set at the same time as <code>sigv4</code>, <code>authorization</code>, <code>basicAuth</code>, or <code>azureAd</code>.</p>
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
<p>basicAuth configuration for the URL.</p>
<p>Cannot be set at the same time as <code>sigv4</code>, <code>authorization</code>, <code>oauth2</code>, or <code>azureAd</code>.</p>
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
<p>bearerTokenFile defines the file from which to read bearer token for the URL.</p>
<p>Deprecated: this will be removed in a future release. Prefer using <code>authorization</code>.</p>
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
<p>authorization section for the URL.</p>
<p>It requires Prometheus &gt;= v2.26.0 or Thanos &gt;= v0.24.0.</p>
<p>Cannot be set at the same time as <code>sigv4</code>, <code>basicAuth</code>, <code>oauth2</code>, or <code>azureAd</code>.</p>
</td>
</tr>
<tr>
<td>
<code>sigv4</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Sigv4">
Sigv4
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>sigv4 defines the AWS&rsquo;s Signature Verification 4 for the URL.</p>
<p>It requires Prometheus &gt;= v2.26.0 or Thanos &gt;= v0.24.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code>, <code>oauth2</code>, or <code>azureAd</code>.</p>
</td>
</tr>
<tr>
<td>
<code>azureAd</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AzureAD">
AzureAD
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>azureAd for the URL.</p>
<p>It requires Prometheus &gt;= v2.45.0 or Thanos &gt;= v0.31.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code>, <code>oauth2</code>, or <code>sigv4</code>.</p>
</td>
</tr>
<tr>
<td>
<code>bearerToken</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>bearerToken is deprecated: this will be removed in a future release.
<em>Warning: this field shouldn&rsquo;t be used because the token value appears
in clear-text. Prefer using <code>authorization</code>.</em></p>
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
<p>tlsConfig to use for the URL.</p>
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
<tr>
<td>
<code>followRedirects</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>followRedirects defines whether HTTP requests follow HTTP 3xx redirects.</p>
<p>It requires Prometheus &gt;= v2.26.0 or Thanos &gt;= v0.24.0.</p>
</td>
</tr>
<tr>
<td>
<code>queueConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.QueueConfig">
QueueConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>queueConfig allows tuning of the remote write queue parameters.</p>
</td>
</tr>
<tr>
<td>
<code>metadataConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.MetadataConfig">
MetadataConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>metadataConfig defines how to send a series metadata to the remote storage.</p>
<p>When the field is empty, <strong>no metadata</strong> is sent. But when the field is
null, metadata is sent.</p>
</td>
</tr>
<tr>
<td>
<code>enableHTTP2</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableHTTP2 defines whether to enable HTTP2.</p>
</td>
</tr>
<tr>
<td>
<code>roundRobinDNS</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>roundRobinDNS controls the DNS resolution behavior for remote-write connections.
When enabled:
- The remote-write mechanism will resolve the hostname via DNS.
- It will randomly select one of the resolved IP addresses and connect to it.</p>
<p>When disabled (default behavior):
- The Go standard library will handle hostname resolution.
- It will attempt connections to each resolved IP address sequentially.</p>
<p>Note: The connection timeout applies to the entire resolution and connection process.</p>
<pre><code>If disabled, the timeout is distributed across all connection attempts.
</code></pre>
<p>It requires Prometheus &gt;= v3.1.0 or Thanos &gt;= v0.38.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RetainConfig">RetainConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ShardRetentionPolicy">ShardRetentionPolicy</a>)
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
<code>retentionPeriod</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<p>retentionPeriod defines how long the scaled-down shard(s) need to be
kept before being deleted.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.RollingUpdateStatefulSetStrategy">RollingUpdateStatefulSetStrategy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.StatefulSetUpdateStrategy">StatefulSetUpdateStrategy</a>)
</p>
<div>
<p>RollingUpdateStatefulSetStrategy is used to communicate parameter for the RollingUpdate strategy.</p>
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
<code>maxUnavailable</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/util/intstr#IntOrString">
k8s.io/apimachinery/pkg/util/intstr.IntOrString
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxUnavailable is the maximum number of pods that can be unavailable
during the update. The value can be an absolute number (ex: 5) or a
percentage of desired pods (ex: 10%). Absolute number is calculated from
percentage by rounding up. This can not be 0.  Defaults to 1. This field
is alpha-level and is only honored by servers that enable the
MaxUnavailableStatefulSet feature. The field applies to all pods in the
range 0 to Replicas-1.  That means if there is any unavailable pod in
the range 0 to Replicas-1, it will be counted towards MaxUnavailable.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.Rule">Rule
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.RuleGroup">RuleGroup</a>)
</p>
<div>
<p>Rule describes an alerting or recording rule
See Prometheus documentation: <a href="https://www.prometheus.io/docs/prometheus/latest/configuration/alerting_rules/">alerting</a> or <a href="https://www.prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules">recording</a> rule</p>
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
<code>record</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>record defines the name of the time series to output to. Must be a valid metric name.
Only one of <code>record</code> and <code>alert</code> must be set.</p>
</td>
</tr>
<tr>
<td>
<code>alert</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alert defines the name of the alert. Must be a valid label value.
Only one of <code>record</code> and <code>alert</code> must be set.</p>
</td>
</tr>
<tr>
<td>
<code>expr</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/util/intstr#IntOrString">
k8s.io/apimachinery/pkg/util/intstr.IntOrString
</a>
</em>
</td>
<td>
<p>expr defines the PromQL expression to evaluate.</p>
</td>
</tr>
<tr>
<td>
<code>for</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>for defines how alerts are considered firing once they have been returned for this long.</p>
</td>
</tr>
<tr>
<td>
<code>keep_firing_for</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NonEmptyDuration">
NonEmptyDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>keep_firing_for defines how long an alert will continue firing after the condition that triggered it has cleared.</p>
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
<p>labels defines labels to add or overwrite.</p>
</td>
</tr>
<tr>
<td>
<code>annotations</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>annotations defines annotations to add to each alert.
Only valid for alerting rules.</p>
</td>
</tr>
</tbody>
</table>
