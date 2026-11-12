<!-- Part 52 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1beta1.PushoverConfig">PushoverConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
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
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
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
<a href="#monitoring.coreos.com/v1beta1.HTTPConfig">
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

<h3 id="monitoring.coreos.com/v1beta1.Receiver">Receiver
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfigSpec">AlertmanagerConfigSpec</a>)
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
<a href="#monitoring.coreos.com/v1beta1.OpsGenieConfig">
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
<a href="#monitoring.coreos.com/v1beta1.PagerDutyConfig">
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
<a href="#monitoring.coreos.com/v1beta1.DiscordConfig">
[]DiscordConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>discordConfigs defines the list of Discord configurations.</p>
</td>
</tr>
<tr>
<td>
<code>slackConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SlackConfig">
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
<a href="#monitoring.coreos.com/v1beta1.WebhookConfig">
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
<a href="#monitoring.coreos.com/v1beta1.WeChatConfig">
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
<a href="#monitoring.coreos.com/v1beta1.EmailConfig">
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
<a href="#monitoring.coreos.com/v1beta1.VictorOpsConfig">
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
<a href="#monitoring.coreos.com/v1beta1.PushoverConfig">
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
<a href="#monitoring.coreos.com/v1beta1.SNSConfig">
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
<a href="#monitoring.coreos.com/v1beta1.TelegramConfig">
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
<a href="#monitoring.coreos.com/v1beta1.WebexConfig">
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
<a href="#monitoring.coreos.com/v1beta1.MSTeamsConfig">
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
<a href="#monitoring.coreos.com/v1beta1.MSTeamsV2Config">
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
<a href="#monitoring.coreos.com/v1beta1.RocketChatConfig">
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

<h3 id="monitoring.coreos.com/v1beta1.RocketChatActionConfig">RocketChatActionConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.RocketChatConfig">RocketChatConfig</a>)
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

<h3 id="monitoring.coreos.com/v1beta1.RocketChatConfig">RocketChatConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>RocketChatConfig configures notifications via RocketChat.
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
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the API URL for RocketChat.
Defaults to <a href="https://open.rocket.chat/">https://open.rocket.chat/</a> if not specified.</p>
</td>
</tr>
<tr>
<td>
<code>channel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>channel defines the channel to send alerts to.
This can be a channel name (e.g., &ldquo;#alerts&rdquo;) or a direct message recipient.</p>
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
<p>token defines the sender token for RocketChat authentication.
This is the personal access token or bot token used to authenticate API requests.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
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
<p>tokenID defines the sender token ID for RocketChat authentication.
This is the user ID associated with the token used for API requests.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
<tr>
<td>
<code>color</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>color defines the message color displayed in RocketChat.
This appears as a colored bar alongside the message.</p>
</td>
</tr>
<tr>
<td>
<code>emoji</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>emoji defines the emoji to be displayed as an avatar.
If provided, this emoji will be used instead of the default avatar or iconURL.</p>
</td>
</tr>
<tr>
<td>
<code>iconURL</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>iconURL defines the icon URL for the message avatar.
This displays a custom image as the message sender&rsquo;s avatar.</p>
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
<p>text defines the message text to send.
This is optional because attachments can be used instead of or alongside text.</p>
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
<p>title defines the message title displayed prominently in the message.
This appears as bold text at the top of the message attachment.</p>
</td>
</tr>
<tr>
<td>
<code>titleLink</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>titleLink defines the URL that the title will link to when clicked.
This makes the message title clickable in the RocketChat interface.</p>
</td>
</tr>
<tr>
<td>
<code>fields</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.RocketChatFieldConfig">
[]RocketChatFieldConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>fields defines additional fields for the message attachment.
These appear as structured key-value pairs within the message.</p>
</td>
</tr>
<tr>
<td>
<code>shortFields</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>shortFields defines whether to use short fields in the message layout.
When true, fields may be displayed side by side to save space.</p>
</td>
</tr>
<tr>
<td>
<code>imageURL</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>imageURL defines the image URL to display within the message.
This embeds an image directly in the message attachment.</p>
</td>
</tr>
<tr>
<td>
<code>thumbURL</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>thumbURL defines the thumbnail URL for the message.
This displays a small thumbnail image alongside the message content.</p>
</td>
</tr>
<tr>
<td>
<code>linkNames</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>linkNames defines whether to enable automatic linking of usernames and channels.
When true, @username and #channel references become clickable links.</p>
</td>
</tr>
<tr>
<td>
<code>actions</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.RocketChatActionConfig">
[]RocketChatActionConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>actions defines interactive actions to include in the message.
These appear as buttons that users can click to trigger responses.</p>
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
<p>httpConfig defines the HTTP client configuration for RocketChat API requests.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.RocketChatFieldConfig">RocketChatFieldConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.RocketChatConfig">RocketChatConfig</a>)
</p>
<div>
<p>RocketChatFieldConfig defines a field for RocketChat messages.</p>
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
<em>(Optional)</em>
<p>title defines the title of this field.
This appears as bold text labeling the field content.</p>
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
<p>value defines the value of this field, displayed underneath the title.
This contains the actual data or content for the field.</p>
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
<p>short defines whether this field should be a short field.
When true, the field may be displayed inline with other short fields to save space.</p>
</td>
</tr>
</tbody>
</table>
