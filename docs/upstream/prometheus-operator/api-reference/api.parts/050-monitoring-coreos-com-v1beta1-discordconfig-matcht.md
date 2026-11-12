<!-- Part 50 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1beta1.DiscordConfig">DiscordConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>DiscordConfig configures notifications via Discord.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#discord_config">https://prometheus.io/docs/alerting/latest/configuration/#discord_config</a></p>
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
<code>sendResolved</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendResolved defines whether or not to notify about resolved alerts.</p>
</td>
</tr>
<tr>
<td>
<code>apiURL</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<p>apiURL defines the secret&rsquo;s key that contains the Discord webhook URL.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
<tr>
<td>
<code>title</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>title defines the template of the message&rsquo;s title.</p>
</td>
</tr>
<tr>
<td>
<code>message</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>message defines the template of the message&rsquo;s body.</p>
</td>
</tr>
<tr>
<td>
<code>content</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>content defines the template of the content&rsquo;s body.</p>
</td>
</tr>
<tr>
<td>
<code>username</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>username defines the username of the message sender.</p>
</td>
</tr>
<tr>
<td>
<code>avatarURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>avatarURL defines the avatar url of the message sender.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
HTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines HTTP client configuration.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.EmailConfig">EmailConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>EmailConfig configures notifications via Email.</p>
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
<code>sendResolved</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendResolved defines whether or not to notify about resolved alerts.</p>
</td>
</tr>
<tr>
<td>
<code>to</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>to defines the email address to send notifications to.
This is the recipient address for alert notifications.</p>
</td>
</tr>
<tr>
<td>
<code>from</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>from defines the sender address for email notifications.
This appears as the &ldquo;From&rdquo; field in the email header.</p>
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
<p>hello defines the hostname to identify to the SMTP server.
This is used in the SMTP HELO/EHLO command during the connection handshake.</p>
</td>
</tr>
<tr>
<td>
<code>smarthost</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>smarthost defines the SMTP host and port through which emails are sent.
Format should be &ldquo;hostname:port&rdquo;, e.g. &ldquo;smtp.example.com:587&rdquo;.</p>
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
<p>authUsername defines the username to use for SMTP authentication.
This is used for SMTP AUTH when the server requires authentication.</p>
</td>
</tr>
<tr>
<td>
<code>authPassword</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authPassword defines the secret&rsquo;s key that contains the password to use for authentication.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
<tr>
<td>
<code>authSecret</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authSecret defines the secret&rsquo;s key that contains the CRAM-MD5 secret.
This is used for CRAM-MD5 authentication mechanism.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
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
<p>authIdentity defines the identity to use for SMTP authentication.
This is typically used with PLAIN authentication mechanism.</p>
</td>
</tr>
<tr>
<td>
<code>headers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.KeyValue">
[]KeyValue
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>headers defines additional email header key/value pairs.
These override any headers previously set by the notification implementation.</p>
</td>
</tr>
<tr>
<td>
<code>html</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>html defines the HTML body of the email notification.
This allows for rich formatting in the email content.</p>
</td>
</tr>
<tr>
<td>
<code>text</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>text defines the plain text body of the email notification.
This provides a fallback for email clients that don&rsquo;t support HTML.</p>
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
<p>requireTLS defines the SMTP TLS requirement.
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
<p>tlsConfig defines the TLS configuration for SMTP connections.
This includes settings for certificates, CA validation, and TLS protocol options.</p>
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
<tr>
<td>
<code>threading</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.EmailThreadingConfig">
EmailThreadingConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>threading defines the threading configuration for email receiver.
It requires Alertmanager &gt;= v0.30.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.EmailThreadingConfig">EmailThreadingConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.EmailConfig">EmailConfig</a>)
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
<code>threadByDate</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.ThreadByDateType">
ThreadByDateType
</a>
</em>
</td>
<td>
<p>threadByDate defines what granularity of current date to thread by. Accepted values: Daily, None.
(None means group by alert group key, no date).</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.DiscordConfig">DiscordConfig</a>, <a href="#monitoring.coreos.com/v1beta1.MSTeamsConfig">MSTeamsConfig</a>, <a href="#monitoring.coreos.com/v1beta1.MSTeamsV2Config">MSTeamsV2Config</a>, <a href="#monitoring.coreos.com/v1beta1.OpsGenieConfig">OpsGenieConfig</a>, <a href="#monitoring.coreos.com/v1beta1.PagerDutyConfig">PagerDutyConfig</a>, <a href="#monitoring.coreos.com/v1beta1.PushoverConfig">PushoverConfig</a>, <a href="#monitoring.coreos.com/v1beta1.RocketChatConfig">RocketChatConfig</a>, <a href="#monitoring.coreos.com/v1beta1.SNSConfig">SNSConfig</a>, <a href="#monitoring.coreos.com/v1beta1.SlackConfig">SlackConfig</a>, <a href="#monitoring.coreos.com/v1beta1.TelegramConfig">TelegramConfig</a>, <a href="#monitoring.coreos.com/v1beta1.VictorOpsConfig">VictorOpsConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WeChatConfig">WeChatConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WebexConfig">WebexConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WebhookConfig">WebhookConfig</a>)
</p>
<div>
<p>HTTPConfig defines a client HTTP configuration.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#http_config">https://prometheus.io/docs/alerting/latest/configuration/#http_config</a></p>
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
<p>authorization defines the authorization header configuration for the client.
This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.</p>
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
<p>basicAuth defines the basic authentication credentials for the client.
This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.</p>
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
<p>oauth2 defines the OAuth2 client credentials used to fetch a token for the targets.
This enables OAuth2 authentication flow for HTTP requests.</p>
</td>
</tr>
<tr>
<td>
<code>bearerTokenSecret</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>bearerTokenSecret defines the secret&rsquo;s key that contains the bearer token to be used by the client
for authentication.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
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
<p>tlsConfig defines the TLS configuration for the client.
This includes settings for certificates, CA validation, and TLS protocol options.</p>
</td>
</tr>
<tr>
<td>
<code>proxyURL</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>proxyURL defines an optional proxy URL for HTTP requests.
If defined, this field takes precedence over <code>proxyUrl</code>.</p>
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
<p>followRedirects defines whether HTTP requests follow HTTP 3xx redirects.
When true, the client will automatically follow redirect responses.</p>
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

<h3 id="monitoring.coreos.com/v1beta1.InhibitRule">InhibitRule
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfigSpec">AlertmanagerConfigSpec</a>)
</p>
<div>
<p>InhibitRule defines an inhibition rule that allows to mute alerts when other
alerts are already firing.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule">https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule</a></p>
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
<code>targetMatch</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Matcher">
[]Matcher
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>targetMatch defines matchers that have to be fulfilled in the alerts to be muted.
The operator enforces that the alert matches the resource&rsquo;s namespace.
When these conditions are met, matching alerts will be inhibited (silenced).</p>
</td>
</tr>
<tr>
<td>
<code>sourceMatch</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Matcher">
[]Matcher
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>sourceMatch defines matchers for which one or more alerts have to exist for the inhibition
to take effect. The operator enforces that the alert matches the resource&rsquo;s namespace.
These are the &ldquo;trigger&rdquo; alerts that cause other alerts to be inhibited.</p>
</td>
</tr>
<tr>
<td>
<code>equal</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>equal defines labels that must have an equal value in the source and target alert
for the inhibition to take effect. This ensures related alerts are properly grouped.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.KeyValue">KeyValue
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.EmailConfig">EmailConfig</a>, <a href="#monitoring.coreos.com/v1beta1.OpsGenieConfig">OpsGenieConfig</a>, <a href="#monitoring.coreos.com/v1beta1.PagerDutyConfig">PagerDutyConfig</a>, <a href="#monitoring.coreos.com/v1beta1.Route">Route</a>, <a href="#monitoring.coreos.com/v1beta1.VictorOpsConfig">VictorOpsConfig</a>)
</p>
<div>
<p>KeyValue defines a (key, value) tuple.</p>
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
<code>key</code><br/>
<em>
string
</em>
</td>
<td>
<p>key defines the key of the tuple.
This is the identifier or name part of the key-value pair.</p>
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
<p>value defines the value of the tuple.
This is the data or content associated with the key.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.MSTeamsConfig">MSTeamsConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>MSTeamsConfig configures notifications via Microsoft Teams.
It requires Alertmanager &gt;= 0.26.0.</p>
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
<code>sendResolved</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendResolved defines whether or not to notify about resolved alerts.</p>
</td>
</tr>
<tr>
<td>
<code>webhookUrl</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<p>webhookUrl defines the MSTeams webhook URL for sending notifications.
This is the incoming webhook URL configured in your Teams channel.</p>
</td>
</tr>
<tr>
<td>
<code>title</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>title defines the message title template for Teams notifications.
This appears as the main heading of the Teams message card.</p>
</td>
</tr>
<tr>
<td>
<code>summary</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>summary defines the message summary template for Teams notifications.
This provides a brief overview that appears in Teams notification previews.
It requires Alertmanager &gt;= 0.27.0.</p>
</td>
</tr>
<tr>
<td>
<code>text</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>text defines the message body template for Teams notifications.
This contains the detailed content of the Teams message.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
HTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines the HTTP client configuration for Teams webhook requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.MSTeamsV2Config">MSTeamsV2Config
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>MSTeamsV2Config configures notifications via Microsoft Teams using the new message format with adaptive cards as required by flows.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#msteamsv2_config">https://prometheus.io/docs/alerting/latest/configuration/#msteamsv2_config</a>
It requires Alertmanager &gt;= 0.28.0.</p>
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
<code>sendResolved</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>sendResolved defines whether or not to notify about resolved alerts.</p>
</td>
</tr>
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
<p>webhookURL defines the MSTeams incoming webhook URL for adaptive card notifications.
This webhook must support the newer adaptive cards format required by Teams flows.</p>
</td>
</tr>
<tr>
<td>
<code>title</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>title defines the message title template for adaptive card notifications.
This appears as the main heading in the Teams adaptive card.</p>
</td>
</tr>
<tr>
<td>
<code>text</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>text defines the message body template for adaptive card notifications.
This contains the detailed content displayed in the Teams adaptive card format.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
HTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines the HTTP client configuration for Teams webhook requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.MatchType">MatchType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Matcher">Matcher</a>)
</p>
<div>
<p>MatchType is a comparison operator on a Matcher</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;=&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;!=&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;!~&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;=~&#34;</p></td>
<td></td>
</tr></tbody>
</table>
