<!-- Part 9 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.APIServerConfig">APIServerConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
<p>APIServerConfig defines how the Prometheus server connects to the Kubernetes API server.</p>
<p>More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config</a></p>
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
<p>host defines the Kubernetes API address consisting of a hostname or IP address followed
by an optional port number.</p>
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
<p>basicAuth configuration for the API server.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>bearerToken</code>, or
<code>bearerTokenFile</code>.</p>
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
<p>bearerTokenFile defines the file to read bearer token for accessing apiserver.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>authorization</code>, or <code>bearerToken</code>.</p>
<p>Deprecated: this will be removed in a future release. Prefer using <code>authorization</code>.</p>
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
<p>tlsConfig to use for the API server.</p>
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
<p>authorization section for the API server.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>bearerToken</code>, or
<code>bearerTokenFile</code>.</p>
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

<h3 id="monitoring.coreos.com/v1.AdditionalLabelSelectors">AdditionalLabelSelectors
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.TopologySpreadConstraint">TopologySpreadConstraint</a>)
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
<tbody><tr><td><p>&#34;OnResource&#34;</p></td>
<td><p>Automatically add a label selector that will select all pods matching the same Prometheus/PrometheusAgent resource (irrespective of their shards).</p>
</td>
</tr><tr><td><p>&#34;OnShard&#34;</p></td>
<td><p>Automatically add a label selector that will select all pods matching the same shard.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertingSpec">AlertingSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>)
</p>
<div>
<p>AlertingSpec defines parameters for alerting configuration of Prometheus servers.</p>
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
<code>alertmanagers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">
[]AlertmanagerEndpoints
</a>
</em>
</td>
<td>
<p>alertmanagers endpoints where Prometheus should send alerts to.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerAPIVersion">AlertmanagerAPIVersion
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>)
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
<tbody><tr><td><p>&#34;V1&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;V2&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerConfigFileSystemMode">AlertmanagerConfigFileSystemMode
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
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
<tbody><tr><td><p>&#34;AllowAll&#34;</p></td>
<td><p>AllowAllAlertmanagerConfigFileSystemMode (&ldquo;AllowAll&rdquo;) allows any
AlertmanagerConfig resource to reference files from the Alertmanager
container&rsquo;s filesystem.</p>
</td>
</tr><tr><td><p>&#34;DenyAll&#34;</p></td>
<td><p>DenyAllAlertmanagerConfigFileSystemMode (&ldquo;DenyAll&rdquo;) denies any
AlertmanagerConfig resource which references files from the Alertmanager
container&rsquo;s filesystem.</p>
</td>
</tr><tr><td><p>&#34;FromAlertmanagerConfigMatcherStrategy&#34;</p></td>
<td><p>FromAlertmanagerConfigMatcherStrategyAlertmanagerConfigFileSystemMode
(&ldquo;FromAlertmanagerConfigMatcherStrategy&rdquo;) uses the
<code>alertmanagerConfigNamespaceSelector</code> field to make a decision on
denying/allowing AlertmanagerConfig resources which reference files from
the Alertmanager container&rsquo;s filesystem.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerConfigMatcherStrategy">AlertmanagerConfigMatcherStrategy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
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
<code>type</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerConfigMatcherStrategyType">
AlertmanagerConfigMatcherStrategyType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>type defines the strategy used by
AlertmanagerConfig objects to match alerts in the routes and inhibition
rules.</p>
<p>The default value is <code>OnNamespace</code>.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerConfigMatcherStrategyType">AlertmanagerConfigMatcherStrategyType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerConfigMatcherStrategy">AlertmanagerConfigMatcherStrategy</a>)
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
<tbody><tr><td><p>&#34;None&#34;</p></td>
<td><p>With <code>None</code>, the route and inhibition rules of an AlertmanagerConfig
object process all incoming alerts.</p>
</td>
</tr><tr><td><p>&#34;OnNamespace&#34;</p></td>
<td><p>With <code>OnNamespace</code>, the route and inhibition rules of an
AlertmanagerConfig object only process alerts that have a <code>namespace</code>
label equal to the namespace of the object.</p>
</td>
</tr><tr><td><p>&#34;OnNamespaceExceptForAlertmanagerNamespace&#34;</p></td>
<td><p>With <code>OnNamespaceExceptForAlertmanagerNamespace</code>, the route and inhibition rules of an
AlertmanagerConfig object only process alerts that have a <code>namespace</code>
label equal to the namespace of the object, unless the AlertmanagerConfig object
is in the same namespace as the Alertmanager object, where it will process all alerts.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerConfiguration">AlertmanagerConfiguration
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
</p>
<div>
<p>AlertmanagerConfiguration defines the Alertmanager configuration.</p>
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
<em>(Optional)</em>
<p>name defines the name of the AlertmanagerConfig custom resource which is used to generate the Alertmanager configuration.
It must be defined in the same namespace as the Alertmanager object.
The operator will not enforce a <code>namespace</code> label for routes and inhibition rules.</p>
</td>
</tr>
<tr>
<td>
<code>global</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">
AlertmanagerGlobalConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>global defines the global parameters of the Alertmanager configuration.</p>
</td>
</tr>
<tr>
<td>
<code>templates</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
[]SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>templates defines the custom notification templates.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertingSpec">AlertingSpec</a>)
</p>
<div>
<p>AlertmanagerEndpoints defines a selection of a single Endpoints object
containing Alertmanager IPs to fire alerts against.</p>
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
<code>namespace</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>namespace of the Endpoints object.</p>
<p>If not set, the object will be discovered in the namespace of the
Prometheus object.</p>
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
<p>name of the Endpoints object in the namespace.</p>
</td>
</tr>
<tr>
<td>
<code>port</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/util/intstr#IntOrString">
k8s.io/apimachinery/pkg/util/intstr.IntOrString
</a>
</em>
</td>
<td>
<p>port on which the Alertmanager API is exposed.</p>
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
<p>scheme defines the HTTP scheme to use when sending alerts.</p>
</td>
</tr>
<tr>
<td>
<code>pathPrefix</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>pathPrefix defines the prefix for the HTTP path alerts are pushed to.</p>
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
<p>tlsConfig to use for Alertmanager.</p>
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
<p>basicAuth configuration for Alertmanager.</p>
<p>Cannot be set at the same time as <code>bearerTokenFile</code>, <code>authorization</code> or <code>sigv4</code>.</p>
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
<p>bearerTokenFile defines the file to read bearer token for Alertmanager.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>authorization</code>, or <code>sigv4</code>.</p>
<p>Deprecated: this will be removed in a future release. Prefer using <code>authorization</code>.</p>
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
<p>authorization section for Alertmanager.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>bearerTokenFile</code> or <code>sigv4</code>.</p>
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
<p>sigv4 defines AWS&rsquo;s Signature Verification 4 for the URL.</p>
<p>It requires Prometheus &gt;= v2.48.0.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>bearerTokenFile</code> or <code>authorization</code>.</p>
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
<code>apiVersion</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerAPIVersion">
AlertmanagerAPIVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiVersion defines the version of the Alertmanager API that Prometheus uses to send alerts.
It can be &ldquo;V1&rdquo; or &ldquo;V2&rdquo;.
The field has no effect for Prometheus &gt;= v3.0.0 because only the v2 API is supported.</p>
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
<p>timeout defines a per-target Alertmanager timeout when pushing alerts.</p>
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
<p>enableHttp2 defines whether to enable HTTP2.</p>
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
<p>relabelings defines the relabel configuration applied to the discovered Alertmanagers.</p>
</td>
</tr>
<tr>
<td>
<code>alertRelabelings</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertRelabelings defines the relabeling configs applied before sending alerts to a specific Alertmanager.
It requires Prometheus &gt;= v2.51.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerConfiguration">AlertmanagerConfiguration</a>)
</p>
<div>
<p>AlertmanagerGlobalConfig configures parameters that are valid in all other configuration contexts.
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
<code>smtp</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalSMTPConfig">
GlobalSMTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>smtp defines global SMTP parameters.</p>
</td>
</tr>
<tr>
<td>
<code>resolveTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>resolveTimeout defines the default value used by alertmanager if the alert does
not include EndsAt, after this time passes it can declare the alert as resolved if it has not been updated.
This has no impact on alerts from Prometheus, as they always include EndsAt.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.HTTPConfigWithProxy">
HTTPConfigWithProxy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines the default HTTP configuration.</p>
</td>
</tr>
<tr>
<td>
<code>slackApiUrl</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>slackApiUrl defines the default Slack API URL.</p>
</td>
</tr>
<tr>
<td>
<code>opsGenieApiUrl</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>opsGenieApiUrl defines the default OpsGenie API URL.</p>
</td>
</tr>
<tr>
<td>
<code>opsGenieApiKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>opsGenieApiKey defines the default OpsGenie API Key.</p>
</td>
</tr>
<tr>
<td>
<code>pagerdutyUrl</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>pagerdutyUrl defines the default Pagerduty URL.</p>
</td>
</tr>
<tr>
<td>
<code>telegram</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalTelegramConfig">
GlobalTelegramConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>telegram defines the default Telegram config</p>
</td>
</tr>
<tr>
<td>
<code>jira</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalJiraConfig">
GlobalJiraConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>jira defines the default configuration for Jira.</p>
</td>
</tr>
<tr>
<td>
<code>victorops</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalVictorOpsConfig">
GlobalVictorOpsConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>victorops defines the default configuration for VictorOps.</p>
</td>
</tr>
<tr>
<td>
<code>rocketChat</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalRocketChatConfig">
GlobalRocketChatConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>rocketChat defines the default configuration for Rocket Chat.</p>
</td>
</tr>
<tr>
<td>
<code>webex</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalWebexConfig">
GlobalWebexConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>webex defines the default configuration for Webex.</p>
</td>
</tr>
<tr>
<td>
<code>wechat</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalWeChatConfig">
GlobalWeChatConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>wechat defines the default WeChat Config</p>
</td>
</tr>
<tr>
<td>
<code>mattermost</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GlobalMattermostConfig">
GlobalMattermostConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>mattermost defines the default Mattermost Config</p>
</td>
</tr>
</tbody>
</table>
