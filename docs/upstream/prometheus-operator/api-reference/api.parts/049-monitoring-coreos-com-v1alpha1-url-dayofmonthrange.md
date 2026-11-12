<!-- Part 49 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.URL">URL
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.DiscordConfig">DiscordConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">HTTPSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">KumaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">NomadSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.OpenStackSDConfig">OpenStackSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.OpsGenieConfig">OpsGenieConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PagerDutyConfig">PagerDutyConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.RocketChatConfig">RocketChatConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScalewaySDConfig">ScalewaySDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.TelegramConfig">TelegramConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.VictorOpsConfig">VictorOpsConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.WeChatConfig">WeChatConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.WebexConfig">WebexConfig</a>)
</p>
<div>
<p>URL represents a valid URL</p>
</div>

<h3 id="monitoring.coreos.com/v1alpha1.VictorOpsConfig">VictorOpsConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>VictorOpsConfig configures notifications via VictorOps.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#victorops_config">https://prometheus.io/docs/alerting/latest/configuration/#victorops_config</a></p>
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
<code>apiKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiKey defines the secret&rsquo;s key that contains the API key to use when talking to the VictorOps API.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
<tr>
<td>
<code>apiUrl</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiUrl defines the VictorOps API URL.
When not specified, defaults to the standard VictorOps API endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>routingKey</code><br/>
<em>
string
</em>
</td>
<td>
<p>routingKey defines a key used to map the alert to a team.
This determines which VictorOps team will receive the alert notification.</p>
</td>
</tr>
<tr>
<td>
<code>messageType</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>messageType describes the behavior of the alert.
Valid values are &ldquo;CRITICAL&rdquo;, &ldquo;WARNING&rdquo;, and &ldquo;INFO&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>entityDisplayName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>entityDisplayName contains a summary of the alerted problem.
This appears as the main title or identifier for the incident.</p>
</td>
</tr>
<tr>
<td>
<code>stateMessage</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>stateMessage contains a long explanation of the alerted problem.
This provides detailed context about the incident.</p>
</td>
</tr>
<tr>
<td>
<code>monitoringTool</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>monitoringTool defines the monitoring tool the state message is from.
This helps identify the source system that generated the alert.</p>
</td>
</tr>
<tr>
<td>
<code>customFields</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.KeyValue">
[]KeyValue
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>customFields defines additional custom fields for notification.
These provide extra metadata that will be included with the VictorOps incident.</p>
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
<p>httpConfig defines the HTTP client&rsquo;s configuration for VictorOps API requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.WeChatConfig">WeChatConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>WeChatConfig configures notifications via WeChat.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#wechat_config">https://prometheus.io/docs/alerting/latest/configuration/#wechat_config</a></p>
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
<code>apiSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiSecret defines the secret&rsquo;s key that contains the WeChat API key.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
<tr>
<td>
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the WeChat API URL.
When not specified, defaults to the standard WeChat Work API endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>corpID</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>corpID defines the corp id for authentication.
This is the unique identifier for your WeChat Work organization.</p>
</td>
</tr>
<tr>
<td>
<code>agentID</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>agentID defines the application agent ID within WeChat Work.
This identifies which WeChat Work application will send the notifications.</p>
</td>
</tr>
<tr>
<td>
<code>toUser</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>toUser defines the target user(s) to receive the notification.
Can be a single user ID or multiple user IDs separated by &lsquo;|&rsquo;.</p>
</td>
</tr>
<tr>
<td>
<code>toParty</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>toParty defines the target department(s) to receive the notification.
Can be a single department ID or multiple department IDs separated by &lsquo;|&rsquo;.</p>
</td>
</tr>
<tr>
<td>
<code>toTag</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>toTag defines the target tag(s) to receive the notification.
Can be a single tag ID or multiple tag IDs separated by &lsquo;|&rsquo;.</p>
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
<p>message defines the API request data as defined by the WeChat API.
This contains the actual notification content to be sent.</p>
</td>
</tr>
<tr>
<td>
<code>messageType</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>messageType defines the type of message to send.
Valid values include &ldquo;text&rdquo;, &ldquo;markdown&rdquo;, and other WeChat Work supported message types.</p>
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
<p>httpConfig defines the HTTP client configuration for WeChat API requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.WebexConfig">WebexConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>WebexConfig configures notification via Cisco Webex
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#webex_config">https://prometheus.io/docs/alerting/latest/configuration/#webex_config</a></p>
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
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the Webex Teams API URL i.e. <a href="https://webexapis.com/v1/messages">https://webexapis.com/v1/messages</a></p>
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
<p>httpConfig defines the HTTP client&rsquo;s configuration.</p>
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
<p>message defines the message template</p>
</td>
</tr>
<tr>
<td>
<code>roomID</code><br/>
<em>
string
</em>
</td>
<td>
<p>roomID defines the ID of the Webex Teams room where to send the messages.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.WebhookConfig">WebhookConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>WebhookConfig configures notifications via a generic receiver supporting the webhook payload.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#webhook_config">https://prometheus.io/docs/alerting/latest/configuration/#webhook_config</a></p>
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
<code>url</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>url defines the URL to send HTTP POST requests to.
urlSecret takes precedence over url. One of urlSecret and url should be defined.</p>
</td>
</tr>
<tr>
<td>
<code>urlSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>urlSecret defines the secret&rsquo;s key that contains the webhook URL to send HTTP requests to.
urlSecret takes precedence over url. One of urlSecret and url should be defined.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
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
<p>httpConfig defines the HTTP client configuration for webhook requests.</p>
</td>
</tr>
<tr>
<td>
<code>maxAlerts</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxAlerts defines the maximum number of alerts to be sent per webhook message.
When 0, all alerts are included in the webhook payload.</p>
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
<p>timeout defines the maximum time to wait for a webhook request to complete,
before failing the request and allowing it to be retried.
It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>payload</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>payload define custom payload to be sent to the webhook endpoint.
This is an advanced configuration option that allows you
to define a custom payload using Go templates.
It requires Alertmanager &gt;= v0.32.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.Weekday">Weekday
(<code>string</code> alias)</h3>
<div>
<p>Weekday is day of the week</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;friday&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;monday&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;saturday&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;sunday&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;thursday&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;tuesday&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;wednesday&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.WeekdayRange">WeekdayRange
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.TimeInterval">TimeInterval</a>)
</p>
<div>
<p>WeekdayRange is an inclusive range of days of the week beginning on Sunday
Days can be specified by name (e.g &lsquo;Sunday&rsquo;) or as an inclusive range (e.g &lsquo;Monday:Friday&rsquo;)</p>
</div>

<h3 id="monitoring.coreos.com/v1alpha1.YearRange">YearRange
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.TimeInterval">TimeInterval</a>)
</p>
<div>
<p>YearRange is an inclusive range of years</p>
</div>
<hr/>

<h2 id="monitoring.coreos.com/v1beta1">monitoring.coreos.com/v1beta1</h2>
Resource Types:
<ul><li>
<a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfig">AlertmanagerConfig</a>
</li></ul>

<h3 id="monitoring.coreos.com/v1beta1.AlertmanagerConfig">AlertmanagerConfig
</h3>
<div>
<p>The <code>AlertmanagerConfig</code> custom resource definition (CRD) defines how <code>Alertmanager</code> objects process Prometheus alerts. It allows to specify alert grouping and routing, notification receivers and inhibition rules.</p>
<p><code>Alertmanager</code> objects select <code>AlertmanagerConfig</code> objects using label and namespace selectors.</p>
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
<code>apiVersion</code><br/>
string</td>
<td>
<code>
monitoring.coreos.com/v1beta1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code><br/>
string
</td>
<td><code>AlertmanagerConfig</code></td>
</tr>
<tr>
<td>
<code>metadata</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta">
Kubernetes meta/v1.ObjectMeta
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>metadata defines ObjectMeta as the metadata that all persisted resources.</p>
Refer to the Kubernetes API documentation for the fields of the
<code>metadata</code> field.
</td>
</tr>
<tr>
<td>
<code>spec</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfigSpec">
AlertmanagerConfigSpec
</a>
</em>
</td>
<td>
<p>spec defines the specification of AlertmanagerConfigSpec</p>
<br/>
<br/>
<table>
<tr>
<td>
<code>route</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Route">
Route
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>route defines the Alertmanager route definition for incoming alerts. It will be added to the
generated Alertmanager configuration as a first-level route. The matching behavior of the
route depends on the Alertmanager&rsquo;s AlertmanagerConfigMatcherStrategyType.</p>
</td>
</tr>
<tr>
<td>
<code>receivers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Receiver">
[]Receiver
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>receivers defines the list of receivers.</p>
</td>
</tr>
<tr>
<td>
<code>inhibitRules</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.InhibitRule">
[]InhibitRule
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>inhibitRules defines the list of inhibition rules. The rules will only apply to alerts matching
the resource&rsquo;s namespace.</p>
</td>
</tr>
<tr>
<td>
<code>timeIntervals</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.TimeInterval">
[]TimeInterval
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>timeIntervals defines the list of timeIntervals specifying when the routes should be muted.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ConfigResourceStatus">
ConfigResourceStatus
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>status defines the status subresource. It is under active development and is updated only when the
&ldquo;StatusForConfigurationResources&rdquo; feature gate is enabled.</p>
<p>Most recent observed status of the ServiceMonitor. Read-only.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.AlertmanagerConfigSpec">AlertmanagerConfigSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfig">AlertmanagerConfig</a>)
</p>
<div>
<p>AlertmanagerConfigSpec is a specification of the desired behavior of the Alertmanager configuration.
By definition, the Alertmanager configuration only applies to alerts for which
the <code>namespace</code> label is equal to the namespace of the AlertmanagerConfig resource.</p>
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
<code>route</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Route">
Route
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>route defines the Alertmanager route definition for incoming alerts. It will be added to the
generated Alertmanager configuration as a first-level route. The matching behavior of the
route depends on the Alertmanager&rsquo;s AlertmanagerConfigMatcherStrategyType.</p>
</td>
</tr>
<tr>
<td>
<code>receivers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Receiver">
[]Receiver
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>receivers defines the list of receivers.</p>
</td>
</tr>
<tr>
<td>
<code>inhibitRules</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.InhibitRule">
[]InhibitRule
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>inhibitRules defines the list of inhibition rules. The rules will only apply to alerts matching
the resource&rsquo;s namespace.</p>
</td>
</tr>
<tr>
<td>
<code>timeIntervals</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.TimeInterval">
[]TimeInterval
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>timeIntervals defines the list of timeIntervals specifying when the routes should be muted.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.DayOfMonthRange">DayOfMonthRange
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.TimePeriod">TimePeriod</a>)
</p>
<div>
<p>DayOfMonthRange is an inclusive range of days of the month beginning at 1</p>
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
<code>start</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>start of the inclusive range</p>
</td>
</tr>
<tr>
<td>
<code>end</code><br/>
<em>
int
</em>
</td>
<td>
<em>(Optional)</em>
<p>end of the inclusive range</p>
</td>
</tr>
</tbody>
</table>
