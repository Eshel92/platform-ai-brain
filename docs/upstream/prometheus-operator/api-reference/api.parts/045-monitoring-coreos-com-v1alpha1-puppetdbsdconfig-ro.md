<!-- Part 45 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>PuppetDBSDConfig configurations allow retrieving scrape targets from PuppetDB resources.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#puppetdb_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#puppetdb_sd_config</a></p>
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
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<p>url defines the URL of the PuppetDB root query endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>query</code><br/>
<em>
string
</em>
</td>
<td>
<p>query defines the Puppet Query Language (PQL) query. Only resources are supported.
<a href="https://puppet.com/docs/puppetdb/latest/api/query/v4/pql.html">https://puppet.com/docs/puppetdb/latest/api/query/v4/pql.html</a></p>
</td>
</tr>
<tr>
<td>
<code>includeParameters</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>includeParameters defines whether to include the parameters as meta labels.
Note: Enabling this exposes parameters in the Prometheus UI and API. Make sure
that you don&rsquo;t have secrets exposed as parameters if you enable this.</p>
</td>
</tr>
<tr>
<td>
<code>refreshInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>refreshInterval defines the time after which the provided names are refreshed.
If not set, Prometheus uses its default value.</p>
</td>
</tr>
<tr>
<td>
<code>port</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>port defines the port to scrape metrics from. If using the public IP address, this must</p>
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
<p>basicAuth defines information to use on every scrape request.
Cannot be set at the same time as <code>authorization</code>, or <code>oauth2</code>.</p>
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
<p>authorization defines the header configuration to authenticate against the PuppetDB API.
Cannot be set at the same time as <code>oauth2</code>.</p>
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
<p>oauth2 defines the optional OAuth 2.0 configuration to authenticate against the target HTTP endpoint.
Cannot be set at the same time as <code>authorization</code>, or <code>basicAuth</code>.</p>
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
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SafeTLSConfig">
SafeTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines the TLS configuration to connect to the PuppetDB server.</p>
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
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.PushoverConfig">PushoverConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>PushoverConfig configures notifications via Pushover.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#pushover_config">https://prometheus.io/docs/alerting/latest/configuration/#pushover_config</a></p>
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
<code>userKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>userKey defines the secret&rsquo;s key that contains the recipient user&rsquo;s user key.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.
Either <code>userKey</code> or <code>userKeyFile</code> is required.</p>
</td>
</tr>
<tr>
<td>
<code>userKeyFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>userKeyFile defines the user key file that contains the recipient user&rsquo;s user key.
Either <code>userKey</code> or <code>userKeyFile</code> is required.
It requires Alertmanager &gt;= v0.26.0.</p>
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
<p>token defines the secret&rsquo;s key that contains the registered application&rsquo;s API token.
See <a href="https://pushover.net/apps">https://pushover.net/apps</a> for application registration.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.
Either <code>token</code> or <code>tokenFile</code> is required.</p>
</td>
</tr>
<tr>
<td>
<code>tokenFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tokenFile defines the token file that contains the registered application&rsquo;s API token.
See <a href="https://pushover.net/apps">https://pushover.net/apps</a> for application registration.
Either <code>token</code> or <code>tokenFile</code> is required.
It requires Alertmanager &gt;= v0.26.0.</p>
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
<p>title defines the notification title displayed in the Pushover message.
This appears as the bold header text in the notification.</p>
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
<p>message defines the notification message content.
This is the main body text of the Pushover notification.</p>
</td>
</tr>
<tr>
<td>
<code>url</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>url defines a supplementary URL shown alongside the message.
This creates a clickable link within the Pushover notification.</p>
</td>
</tr>
<tr>
<td>
<code>urlTitle</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>urlTitle defines a title for the supplementary URL.
If not specified, the raw URL is shown instead.</p>
</td>
</tr>
<tr>
<td>
<code>ttl</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ttl defines the time to live for the alert notification.
This determines how long the notification remains active before expiring.</p>
</td>
</tr>
<tr>
<td>
<code>device</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>device defines the name of a specific device to send the notification to.
If not specified, the notification is sent to all user&rsquo;s devices.</p>
</td>
</tr>
<tr>
<td>
<code>sound</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>sound defines the name of one of the sounds supported by device clients.
This overrides the user&rsquo;s default sound choice for this notification.</p>
</td>
</tr>
<tr>
<td>
<code>priority</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>priority defines the notification priority level.
See <a href="https://pushover.net/api#priority">https://pushover.net/api#priority</a> for valid values and behavior.</p>
</td>
</tr>
<tr>
<td>
<code>retry</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>retry defines how often the Pushover servers will send the same notification to the user.
Must be at least 30 seconds. Only applies to priority 2 notifications.</p>
</td>
</tr>
<tr>
<td>
<code>expire</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>expire defines how long your notification will continue to be retried for,
unless the user acknowledges the notification. Only applies to priority 2 notifications.</p>
</td>
</tr>
<tr>
<td>
<code>html</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>html defines whether notification message is HTML or plain text.
When true, the message can include HTML formatting tags.
html and monospace formatting are mutually exclusive.</p>
</td>
</tr>
<tr>
<td>
<code>monospace</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>monospace optional HTML/monospace formatting for the message, see <a href="https://pushover.net/api#html">https://pushover.net/api#html</a>
html and monospace formatting are mutually exclusive.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">
HTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines the HTTP client configuration for Pushover API requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.Receiver">Receiver
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.AlertmanagerConfigSpec">AlertmanagerConfigSpec</a>)
</p>
<div>
<p>Receiver defines one or more notification integrations.</p>
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
<p>name defines the name of the receiver. Must be unique across all items from the list.</p>
</td>
</tr>
<tr>
<td>
<code>opsgenieConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OpsGenieConfig">
[]OpsGenieConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>opsgenieConfigs defines the list of OpsGenie configurations.</p>
</td>
</tr>
<tr>
<td>
<code>pagerdutyConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.PagerDutyConfig">
[]PagerDutyConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>pagerdutyConfigs defines the List of PagerDuty configurations.</p>
</td>
</tr>
<tr>
<td>
<code>discordConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.DiscordConfig">
[]DiscordConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>discordConfigs defines the list of Slack configurations.</p>
</td>
</tr>
<tr>
<td>
<code>slackConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.SlackConfig">
[]SlackConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>slackConfigs defines the list of Slack configurations.</p>
</td>
</tr>
<tr>
<td>
<code>webhookConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.WebhookConfig">
[]WebhookConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>webhookConfigs defines the List of webhook configurations.</p>
</td>
</tr>
<tr>
<td>
<code>wechatConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.WeChatConfig">
[]WeChatConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>wechatConfigs defines the list of WeChat configurations.</p>
</td>
</tr>
<tr>
<td>
<code>emailConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.EmailConfig">
[]EmailConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>emailConfigs defines the list of Email configurations.</p>
</td>
</tr>
<tr>
<td>
<code>victoropsConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.VictorOpsConfig">
[]VictorOpsConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>victoropsConfigs defines the list of VictorOps configurations.</p>
</td>
</tr>
<tr>
<td>
<code>pushoverConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.PushoverConfig">
[]PushoverConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>pushoverConfigs defines the list of Pushover configurations.</p>
</td>
</tr>
<tr>
<td>
<code>snsConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.SNSConfig">
[]SNSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>snsConfigs defines the list of SNS configurations</p>
</td>
</tr>
<tr>
<td>
<code>telegramConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.TelegramConfig">
[]TelegramConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>telegramConfigs defines the list of Telegram configurations.</p>
</td>
</tr>
<tr>
<td>
<code>webexConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.WebexConfig">
[]WebexConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>webexConfigs defines the list of Webex configurations.</p>
</td>
</tr>
<tr>
<td>
<code>msteamsConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.MSTeamsConfig">
[]MSTeamsConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>msteamsConfigs defines the list of MSTeams configurations.
It requires Alertmanager &gt;= 0.26.0.</p>
</td>
</tr>
<tr>
<td>
<code>msteamsv2Configs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.MSTeamsV2Config">
[]MSTeamsV2Config
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>msteamsv2Configs defines the list of MSTeamsV2 configurations.
It requires Alertmanager &gt;= 0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>rocketchatConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.RocketChatConfig">
[]RocketChatConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>rocketchatConfigs defines the list of RocketChat configurations.
It requires Alertmanager &gt;= 0.28.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.RocketChatActionConfig">RocketChatActionConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.RocketChatConfig">RocketChatConfig</a>)
</p>
<div>
<p>RocketChatActionConfig defines actions for RocketChat messages.</p>
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
<code>text</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>text defines the button text displayed to users.
This is the label that appears on the interactive button.</p>
</td>
</tr>
<tr>
<td>
<code>url</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>url defines the URL the button links to when clicked.
This creates a clickable button that opens the specified URL.</p>
</td>
</tr>
<tr>
<td>
<code>msg</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>msg defines the message to send when the button is clicked.
This allows the button to post a predefined message to the channel.</p>
</td>
</tr>
</tbody>
</table>
