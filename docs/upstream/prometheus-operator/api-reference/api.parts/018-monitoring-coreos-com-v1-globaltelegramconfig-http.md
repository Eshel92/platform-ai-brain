<!-- Part 18 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.GlobalTelegramConfig">GlobalTelegramConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalTelegramConfig configures global Telegram parameters.</p>
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
<p>apiURL defines he default Telegram API URL.</p>
<p>It requires Alertmanager &gt;= v0.24.0.</p>
</td>
</tr>
<tr>
<td>
<code>botToken</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>botToken represents the bot token configuration for Telegram.
It is mutually exclusive with <code>botTokenFile</code>.
It requires Alertmanager &gt;= v0.31.0.</p>
</td>
</tr>
<tr>
<td>
<code>botTokenFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>botTokenFile defines the file to read the Telegram bot token from.
It is mutually exclusive with <code>botToken</code>.
It requires Alertmanager &gt;= v0.31.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalVictorOpsConfig">GlobalVictorOpsConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalVictorOpsConfig configures global VictorOps parameters.</p>
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
<p>apiURL defines the default VictorOps API URL.</p>
</td>
</tr>
<tr>
<td>
<code>apiKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiKey defines the default VictorOps API Key.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalWeChatConfig">GlobalWeChatConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
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
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines he default WeChat API URL.
The default value is &ldquo;<a href="https://qyapi.weixin.qq.com/cgi-bin/&quot;">https://qyapi.weixin.qq.com/cgi-bin/&rdquo;</a></p>
</td>
</tr>
<tr>
<td>
<code>apiSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiSecret defines the default WeChat API Secret.</p>
</td>
</tr>
<tr>
<td>
<code>apiCorpID</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiCorpID defines the default WeChat API Corporate ID.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GlobalWebexConfig">GlobalWebexConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>)
</p>
<div>
<p>GlobalWebexConfig configures global Webex parameters.
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
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the is the default Webex API URL.</p>
<p>It requires Alertmanager &gt;= v0.25.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.GoDuration">GoDuration
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
</p>
<div>
<p>GoDuration is a valid time duration that can be parsed by Go&rsquo;s time.ParseDuration() function.
Supported units: h, m, s, ms
Examples: <code>45ms</code>, <code>30s</code>, <code>1m</code>, <code>1h20m15s</code></p>
</div>

<h3 id="monitoring.coreos.com/v1.HTTPConfig">HTTPConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.HTTPConfigWithProxy">HTTPConfigWithProxy</a>, <a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>)
</p>
<div>
<p>HTTPConfig defines the HTTP configuration + TLS configuration (only from
secret/configmap references).</p>
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
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.HTTPConfigWithProxy">HTTPConfigWithProxy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>, <a href="#monitoring.coreos.com/v1.PodMetricsEndpoint">PodMetricsEndpoint</a>)
</p>
<div>
<p>HTTPConfigWithProxy defines the configuration for the HTTP client with proxy
configuration. It is used for PodMonitor endpoints and Probes.</p>
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

<h3 id="monitoring.coreos.com/v1.HTTPConfigWithProxyAndTLSFiles">HTTPConfigWithProxyAndTLSFiles
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Endpoint">Endpoint</a>)
</p>
<div>
<p>HTTPConfigWithProxyAndTLSFiles defines the configuration for the HTTP client
with proxy configuration and TLS configuration. It is used for
ServiceMonitor endpoints.</p>
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

<h3 id="monitoring.coreos.com/v1.HTTPConfigWithTLSFiles">HTTPConfigWithTLSFiles
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.HTTPConfigWithProxyAndTLSFiles">HTTPConfigWithProxyAndTLSFiles</a>)
</p>
<div>
<p>HTTPConfigWithTLSFiles defines HTTP configuration + TLS configuration
(from secret/configmap references as well as files).</p>
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
</tbody>
</table>
