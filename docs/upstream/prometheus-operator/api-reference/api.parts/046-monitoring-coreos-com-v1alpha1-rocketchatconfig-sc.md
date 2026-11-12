<!-- Part 46 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.RocketChatConfig">RocketChatConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1alpha1.URL">
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
<a href="#monitoring.coreos.com/v1alpha1.RocketChatFieldConfig">
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
<a href="#monitoring.coreos.com/v1alpha1.RocketChatActionConfig">
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
<a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">
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

<h3 id="monitoring.coreos.com/v1alpha1.RocketChatFieldConfig">RocketChatFieldConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.RocketChatConfig">RocketChatConfig</a>)
</p>
<div>
<p>RocketChatFieldConfig defines additional fields for RocketChat messages.</p>
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

<h3 id="monitoring.coreos.com/v1alpha1.Route">Route
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.AlertmanagerConfigSpec">AlertmanagerConfigSpec</a>)
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
<a href="#monitoring.coreos.com/v1alpha1.Matcher">
[]Matcher
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>matchers defines the list of matchers that the alert&rsquo;s labels should match. For the first
level route, the operator removes any existing equality and regexp
matcher on the <code>namespace</code> label and adds a <code>namespace: &lt;object
namespace&gt;</code> matcher.</p>
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
<p>activeTimeIntervals is a list of MuteTimeInterval names when this route should be active.</p>
</td>
</tr>
<tr>
<td>
<code>labels</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.KeyValue">
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

<h3 id="monitoring.coreos.com/v1alpha1.SDFile">SDFile
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.FileSDConfig">FileSDConfig</a>)
</p>
<div>
<p>SDFile represents a file used for service discovery</p>
</div>

<h3 id="monitoring.coreos.com/v1alpha1.SNSConfig">SNSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
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
<a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">
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

<h3 id="monitoring.coreos.com/v1alpha1.ScalewayRole">ScalewayRole
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScalewaySDConfig">ScalewaySDConfig</a>)
</p>
<div>
<p>Role of the targets to retrieve. Must be <code>Instance</code> or <code>Baremetal</code>.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;Baremetal&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Instance&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.ScalewaySDConfig">ScalewaySDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>ScalewaySDConfig configurations allow retrieving scrape targets from Scaleway instances and baremetal services.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scaleway_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scaleway_sd_config</a></p>
<p>Note: The <code>_file</code> variants of credential fields (e.g. <code>secret_key_file</code>)
from the Prometheus configuration are not supported. Use Kubernetes secrets via <code>secretKey</code> instead.</p>
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
<code>accessKey</code><br/>
<em>
string
</em>
</td>
<td>
<p>accessKey defines the access key to use. <a href="https://console.scaleway.com/project/credentials">https://console.scaleway.com/project/credentials</a></p>
</td>
</tr>
<tr>
<td>
<code>secretKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<p>secretKey defines the secret key to use when listing targets.</p>
</td>
</tr>
<tr>
<td>
<code>projectID</code><br/>
<em>
string
</em>
</td>
<td>
<p>projectID defines the Project ID of the targets.</p>
</td>
</tr>
<tr>
<td>
<code>role</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.ScalewayRole">
ScalewayRole
</a>
</em>
</td>
<td>
<p>role defines the service of the targets to retrieve. Must be <code>Instance</code> or <code>Baremetal</code>.</p>
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
<code>apiURL</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiURL defines the API URL to use when doing the server listing requests.</p>
</td>
</tr>
<tr>
<td>
<code>zone</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>zone defines the availability zone of your targets (e.g. fr-par-1).</p>
</td>
</tr>
<tr>
<td>
<code>nameFilter</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>nameFilter defines a name filter (works as a LIKE) to apply on the server listing request.</p>
</td>
</tr>
<tr>
<td>
<code>tagsFilter</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tagsFilter defines a tag filter (a server needs to have all defined tags to be listed) to apply on the server listing request.</p>
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
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SafeTLSConfig">
SafeTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines the TLS configuration to connect to the Scaleway API.</p>
</td>
</tr>
</tbody>
</table>
