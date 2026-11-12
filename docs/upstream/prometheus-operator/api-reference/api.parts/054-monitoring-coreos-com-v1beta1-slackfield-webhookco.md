<!-- Part 54 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1beta1.SlackField">SlackField
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.SlackConfig">SlackConfig</a>)
</p>
<div>
<p>SlackField configures a single Slack field that is sent with each notification.
Each field must contain a title, value, and optionally, a boolean value to indicate if the field
is short enough to be displayed next to other fields designated as short.
See <a href="https://api.slack.com/docs/message-attachments#fields">https://api.slack.com/docs/message-attachments#fields</a> for more information.</p>
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
<code>title</code><br/>
<em>
string
</em>
</td>
<td>
<p>title defines the label or header text displayed for this field.
This appears as bold text above the field value in the Slack message.</p>
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
<p>value defines the content or data displayed for this field.
This appears below the title and can contain plain text or Slack markdown.</p>
</td>
</tr>
<tr>
<td>
<code>short</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>short determines whether this field can be displayed alongside other short fields.
When true, Slack may display this field side by side with other short fields.
When false or not specified, the field takes the full width of the message.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.TelegramConfig">TelegramConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>TelegramConfig configures notifications via Telegram.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#telegram_config">https://prometheus.io/docs/alerting/latest/configuration/#telegram_config</a></p>
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
<a href="#monitoring.coreos.com/v1beta1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the Telegram API URL, e.g. <a href="https://api.telegram.org">https://api.telegram.org</a>.
If not specified, the default Telegram API URL will be used.</p>
</td>
</tr>
<tr>
<td>
<code>botToken</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>botToken defines the Telegram bot token. It is mutually exclusive with <code>botTokenFile</code>.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.
Either <code>botToken</code> or <code>botTokenFile</code> is required.</p>
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
Either <code>botToken</code> or <code>botTokenFile</code> is required.
It requires Alertmanager &gt;= v0.26.0.</p>
</td>
</tr>
<tr>
<td>
<code>chatID</code><br/>
<em>
int64
</em>
</td>
<td>
<p>chatID defines the Telegram chat ID where messages will be sent.
This can be a user ID, group ID, or channel ID (with @ prefix for public channels).</p>
</td>
</tr>
<tr>
<td>
<code>messageThreadID</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>messageThreadID defines the Telegram Group Topic ID for threaded messages.
This allows sending messages to specific topics within Telegram groups.
It requires Alertmanager &gt;= 0.26.0.</p>
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
<p>message defines the message template for the Telegram notification.
This is the content that will be sent to the specified chat.</p>
</td>
</tr>
<tr>
<td>
<code>disableNotifications</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>disableNotifications controls whether Telegram notifications are sent silently.
When true, users will receive the message without notification sounds.</p>
</td>
</tr>
<tr>
<td>
<code>parseMode</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>parseMode defines the parse mode for telegram message formatting.
Valid values are &ldquo;MarkdownV2&rdquo;, &ldquo;Markdown&rdquo;, and &ldquo;HTML&rdquo;.
This determines how text formatting is interpreted in the message.</p>
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
<p>httpConfig defines the HTTP client configuration for Telegram API requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.ThreadByDateType">ThreadByDateType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.EmailThreadingConfig">EmailThreadingConfig</a>)
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
<tbody><tr><td><p>&#34;Daily&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;None&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.Time">Time
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.TimeRange">TimeRange</a>)
</p>
<div>
<p>Time defines a time in 24hr format</p>
</div>

<h3 id="monitoring.coreos.com/v1beta1.TimeInterval">TimeInterval
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfigSpec">AlertmanagerConfigSpec</a>)
</p>
<div>
<p>TimeInterval specifies the periods in time when notifications will be muted or active.</p>
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
<p>name of the time interval.</p>
</td>
</tr>
<tr>
<td>
<code>timeIntervals</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.TimePeriod">
[]TimePeriod
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>timeIntervals defines a list of TimePeriod.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.TimePeriod">TimePeriod
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.TimeInterval">TimeInterval</a>)
</p>
<div>
<p>TimePeriod describes periods of time.</p>
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
<code>times</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.TimeRange">
[]TimeRange
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>times defines a list of TimeRange</p>
</td>
</tr>
<tr>
<td>
<code>weekdays</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.WeekdayRange">
[]WeekdayRange
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>weekdays defines a list of WeekdayRange</p>
</td>
</tr>
<tr>
<td>
<code>daysOfMonth</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.DayOfMonthRange">
[]DayOfMonthRange
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>daysOfMonth defines a list of DayOfMonthRange</p>
</td>
</tr>
<tr>
<td>
<code>months</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.MonthRange">
[]MonthRange
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>months defines a list of MonthRange</p>
</td>
</tr>
<tr>
<td>
<code>years</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.YearRange">
[]YearRange
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>years defines a list of YearRange</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.TimeRange">TimeRange
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.TimePeriod">TimePeriod</a>)
</p>
<div>
<p>TimeRange defines a start and end time in 24hr format</p>
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
<code>startTime</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Time">
Time
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>startTime defines the start time in 24hr format.</p>
</td>
</tr>
<tr>
<td>
<code>endTime</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Time">
Time
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>endTime defines the end time in 24hr format.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.URL">URL
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.DiscordConfig">DiscordConfig</a>, <a href="#monitoring.coreos.com/v1beta1.OpsGenieConfig">OpsGenieConfig</a>, <a href="#monitoring.coreos.com/v1beta1.PagerDutyConfig">PagerDutyConfig</a>, <a href="#monitoring.coreos.com/v1beta1.RocketChatConfig">RocketChatConfig</a>, <a href="#monitoring.coreos.com/v1beta1.TelegramConfig">TelegramConfig</a>, <a href="#monitoring.coreos.com/v1beta1.VictorOpsConfig">VictorOpsConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WeChatConfig">WeChatConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WebexConfig">WebexConfig</a>)
</p>
<div>
<p>URL represents a valid URL</p>
</div>

<h3 id="monitoring.coreos.com/v1beta1.VictorOpsConfig">VictorOpsConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
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
<a href="#monitoring.coreos.com/v1beta1.URL">
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
<a href="#monitoring.coreos.com/v1beta1.KeyValue">
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
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
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

<h3 id="monitoring.coreos.com/v1beta1.WeChatConfig">WeChatConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
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
<a href="#monitoring.coreos.com/v1beta1.URL">
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
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
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

<h3 id="monitoring.coreos.com/v1beta1.WebexConfig">WebexConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1beta1.URL">
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
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
HTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines the HTTP client&rsquo;s configuration.
You must use this configuration to supply the bot token as part of the HTTP <code>Authorization</code> header.</p>
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

<h3 id="monitoring.coreos.com/v1beta1.WebhookConfig">WebhookConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
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
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
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
