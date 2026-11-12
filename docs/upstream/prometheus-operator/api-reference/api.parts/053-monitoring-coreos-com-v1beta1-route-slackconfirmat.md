<!-- Part 53 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1beta1.Route">Route
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfigSpec">AlertmanagerConfigSpec</a>)
</p>
<div>
<p>Route defines a node in the routing tree.</p>
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
<code>receiver</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>receiver defines the name of the receiver for this route. If not empty, it should be listed in
the <code>receivers</code> field.</p>
</td>
</tr>
<tr>
<td>
<code>groupBy</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>groupBy defines the list of labels to group by.
Labels must not be repeated (unique list).
Special label &ldquo;&hellip;&rdquo; (aggregate by all possible labels), if provided, must be the only element in the list.</p>
</td>
</tr>
<tr>
<td>
<code>groupWait</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NonEmptyDuration">
NonEmptyDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>groupWait defines how long to wait before sending the initial notification.
Example: &ldquo;30s&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>groupInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NonEmptyDuration">
NonEmptyDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>groupInterval defines how long to wait before sending an updated notification.
Must be greater than 0.
Example: &ldquo;5m&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>repeatInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NonEmptyDuration">
NonEmptyDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>repeatInterval defines how long to wait before repeating the last notification.
Must be greater than 0.
Example: &ldquo;4h&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>matchers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.Matcher">
[]Matcher
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>matchers defines the list of matchers that the alert&rsquo;s labels should match. For the first
level route, the operator removes any existing equality and regexp
matcher on the <code>namespace</code> label and adds a <code>namespace: &lt;object namespace&gt;</code> matcher,
unless configured otherwise in Alertmanager&rsquo;s AlertmanagerConfigMatcherStrategyType.</p>
</td>
</tr>
<tr>
<td>
<code>continue</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>continue defines the boolean indicating whether an alert should continue matching subsequent
sibling nodes. It will always be overridden to true for the first-level
route by the Prometheus operator.</p>
</td>
</tr>
<tr>
<td>
<code>routes</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1#JSON">
[]k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1.JSON
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>routes defines the child routes.</p>
</td>
</tr>
<tr>
<td>
<code>muteTimeIntervals</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>muteTimeIntervals is a list of MuteTimeInterval names that will mute this route when matched,</p>
</td>
</tr>
<tr>
<td>
<code>activeTimeIntervals</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>activeTimeIntervals is a list of TimeInterval names when this route should be active.</p>
</td>
</tr>
<tr>
<td>
<code>labels</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.KeyValue">
[]KeyValue
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>labels defines the list of labels that will be attached to the alerts matching this route.
They can be inherited by child routes and can be overridden by child routes.
The values support template expressions.</p>
<p>It requires Alertmanager &gt;= 0.34.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.SNSConfig">SNSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>SNSConfig configures notifications via AWS SNS.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#sns_configs">https://prometheus.io/docs/alerting/latest/configuration/#sns_configs</a></p>
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
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the SNS API URL, e.g. <a href="https://sns.us-east-2.amazonaws.com">https://sns.us-east-2.amazonaws.com</a>.
If not specified, the SNS API URL from the SNS SDK will be used.</p>
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
<p>sigv4 configures AWS&rsquo;s Signature Verification 4 signing process to sign requests.
This includes AWS credentials and region configuration for authentication.</p>
</td>
</tr>
<tr>
<td>
<code>topicARN</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>topicARN defines the SNS topic ARN, e.g. arn:aws:sns:us-east-2:698519295917:My-Topic.
If you don&rsquo;t specify this value, you must specify a value for the PhoneNumber or TargetARN.</p>
</td>
</tr>
<tr>
<td>
<code>subject</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>subject defines the subject line when the message is delivered to email endpoints.
This field is only used when sending to email subscribers of an SNS topic.</p>
</td>
</tr>
<tr>
<td>
<code>phoneNumber</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>phoneNumber defines the phone number if message is delivered via SMS in E.164 format.
If you don&rsquo;t specify this value, you must specify a value for the TopicARN or TargetARN.</p>
</td>
</tr>
<tr>
<td>
<code>targetARN</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>targetARN defines the mobile platform endpoint ARN if message is delivered via mobile notifications.
If you don&rsquo;t specify this value, you must specify a value for the TopicARN or PhoneNumber.</p>
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
<p>message defines the message content of the SNS notification.
This is the actual notification text that will be sent to subscribers.</p>
</td>
</tr>
<tr>
<td>
<code>attributes</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>attributes defines SNS message attributes as key-value pairs.
These provide additional metadata that can be used for message filtering and routing.</p>
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
<p>httpConfig defines the HTTP client configuration for SNS API requests.</p>
</td>
</tr>
<tr>
<td>
<code>useAWSHTTPClient</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>useAWSHTTPClient forces the AWS SDK&rsquo;s BuildableClient instead of
alertmanager&rsquo;s tracing-wrapped HTTP client. Auto-enabled when AWS_CA_BUNDLE
is set; set explicitly when configuring ca_bundle via shared AWS config.</p>
<p>It requires Alertmanager &gt;= 0.33.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.SecretKeySelector">SecretKeySelector
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.EmailConfig">EmailConfig</a>, <a href="#monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1beta1.OpsGenieConfig">OpsGenieConfig</a>, <a href="#monitoring.coreos.com/v1beta1.PagerDutyConfig">PagerDutyConfig</a>, <a href="#monitoring.coreos.com/v1beta1.PushoverConfig">PushoverConfig</a>, <a href="#monitoring.coreos.com/v1beta1.SlackConfig">SlackConfig</a>, <a href="#monitoring.coreos.com/v1beta1.TelegramConfig">TelegramConfig</a>, <a href="#monitoring.coreos.com/v1beta1.VictorOpsConfig">VictorOpsConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WeChatConfig">WeChatConfig</a>, <a href="#monitoring.coreos.com/v1beta1.WebhookConfig">WebhookConfig</a>)
</p>
<div>
<p>SecretKeySelector selects a key of a Secret.</p>
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
<p>name defines the name of the secret in the object&rsquo;s namespace to select from.</p>
</td>
</tr>
<tr>
<td>
<code>key</code><br/>
<em>
string
</em>
</td>
<td>
<p>key defines the key of the secret to select from.  Must be a valid secret key.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.SlackAction">SlackAction
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.SlackConfig">SlackConfig</a>)
</p>
<div>
<p>SlackAction configures a single Slack action that is sent with each
notification.
See <a href="https://api.slack.com/docs/message-attachments#action_fields">https://api.slack.com/docs/message-attachments#action_fields</a> and
<a href="https://api.slack.com/docs/message-buttons">https://api.slack.com/docs/message-buttons</a> for more information.</p>
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
string
</em>
</td>
<td>
<p>type defines the type of interactive component.
Common values include &ldquo;button&rdquo; for clickable buttons and &ldquo;select&rdquo; for dropdown menus.</p>
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
<p>text defines the user-visible label displayed on the action element.
For buttons, this is the button text. For select menus, this is the placeholder text.</p>
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
<p>url defines the URL to open when the action is triggered.
Only applicable for button-type actions. When set, clicking the button opens this URL.</p>
</td>
</tr>
<tr>
<td>
<code>style</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>style defines the visual appearance of the action element.
Valid values include &ldquo;default&rdquo;, &ldquo;primary&rdquo; (green), and &ldquo;danger&rdquo; (red).</p>
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
<p>name defines a unique identifier for the action within the message.
This value is sent back to your application when the action is triggered.</p>
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
<p>value defines the payload sent when the action is triggered.
This data is included in the callback sent to your application.</p>
</td>
</tr>
<tr>
<td>
<code>confirm</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SlackConfirmationField">
SlackConfirmationField
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>confirm defines an optional confirmation dialog that appears before the action is executed.
When set, users must confirm their intent before the action proceeds.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.SlackConfig">SlackConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.Receiver">Receiver</a>)
</p>
<div>
<p>SlackConfig configures notifications via Slack.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#slack_config">https://prometheus.io/docs/alerting/latest/configuration/#slack_config</a></p>
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
<a href="#monitoring.coreos.com/v1beta1.SecretKeySelector">
SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the secret&rsquo;s key that contains the Slack webhook URL.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
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
<p>channel defines the channel or user to send notifications to.</p>
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
<p>username defines the slack bot user name.</p>
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
<p>color defines the color of the left border of the Slack message attachment.
Can be a hex color code (e.g., &ldquo;#ff0000&rdquo;) or a predefined color name.</p>
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
<p>title defines the title text displayed in the Slack message attachment.</p>
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
<p>titleLink defines the URL that the title will link to when clicked.</p>
</td>
</tr>
<tr>
<td>
<code>pretext</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>pretext defines optional text that appears above the message attachment block.</p>
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
<p>text defines the main text content of the Slack message attachment.</p>
</td>
</tr>
<tr>
<td>
<code>fields</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SlackField">
[]SlackField
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>fields defines a list of Slack fields that are sent with each notification.</p>
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
<p>shortFields determines whether fields are displayed in a compact format.
When true, fields are shown side by side when possible.</p>
</td>
</tr>
<tr>
<td>
<code>footer</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>footer defines small text displayed at the bottom of the message attachment.</p>
</td>
</tr>
<tr>
<td>
<code>fallback</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>fallback defines a plain-text summary of the attachment for clients that don&rsquo;t support attachments.</p>
</td>
</tr>
<tr>
<td>
<code>callbackId</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>callbackId defines an identifier for the message used in interactive components.</p>
</td>
</tr>
<tr>
<td>
<code>iconEmoji</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>iconEmoji defines the emoji to use as the bot&rsquo;s avatar (e.g., &ldquo;:ghost:&rdquo;).</p>
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
<p>iconURL defines the URL to an image to use as the bot&rsquo;s avatar.</p>
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
<p>imageURL defines the URL to an image file that will be displayed inside the message attachment.</p>
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
<p>thumbURL defines the URL to an image file that will be displayed as a thumbnail
on the right side of the message attachment.</p>
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
<p>linkNames enables automatic linking of channel names and usernames in the message.
When true, @channel and @username will be converted to clickable links.</p>
</td>
</tr>
<tr>
<td>
<code>mrkdwnIn</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>mrkdwnIn defines which fields should be parsed as Slack markdown.
Valid values include &ldquo;pretext&rdquo;, &ldquo;text&rdquo;, and &ldquo;fields&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>actions</code><br/>
<em>
<a href="#monitoring.coreos.com/v1beta1.SlackAction">
[]SlackAction
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>actions defines a list of Slack actions that are sent with each notification.</p>
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
<p>httpConfig defines the HTTP client configuration.</p>
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
It requires Alertmanager &gt;= v0.30.0.</p>
</td>
</tr>
<tr>
<td>
<code>messageText</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>messageText defines text content of the Slack message.
If set, this is sent as the top-level &lsquo;text&rsquo; field in the Slack payload.
It requires Alertmanager &gt;= v0.31.0.</p>
</td>
</tr>
<tr>
<td>
<code>updateMessage</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>updateMessage enables updating existing Slack messages instead of creating new ones
when alert state changes. Please note that Webhook URLs do not support updates.
It requires Alertmanager &gt;= v0.32.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1beta1.SlackConfirmationField">SlackConfirmationField
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1beta1.SlackAction">SlackAction</a>)
</p>
<div>
<p>SlackConfirmationField protect users from destructive actions or
particularly distinguished decisions by asking them to confirm their button
click one more time.
See <a href="https://api.slack.com/docs/interactive-message-field-guide#confirmation_fields">https://api.slack.com/docs/interactive-message-field-guide#confirmation_fields</a>
for more information.</p>
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
<p>text defines the main message displayed in the confirmation dialog.
This should be a clear question or statement asking the user to confirm their action.</p>
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
<p>title defines the title text displayed at the top of the confirmation dialog.
When not specified, a default title will be used.</p>
</td>
</tr>
<tr>
<td>
<code>okText</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>okText defines the label for the confirmation button in the dialog.
When not specified, defaults to &ldquo;Okay&rdquo;. This button proceeds with the action.</p>
</td>
</tr>
<tr>
<td>
<code>dismissText</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>dismissText defines the label for the cancel button in the dialog.
When not specified, defaults to &ldquo;Cancel&rdquo;. This button cancels the action.</p>
</td>
</tr>
</tbody>
</table>
