<!-- Part 43 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.PagerDutyConfig">PagerDutyConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>PagerDutyConfig configures notifications via PagerDuty.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#pagerduty_config">https://prometheus.io/docs/alerting/latest/configuration/#pagerduty_config</a></p>
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
<code>routingKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>routingKey defines the secret&rsquo;s key that contains the PagerDuty integration key (when using
Events API v2). Either this field or <code>serviceKey</code> needs to be defined.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
<tr>
<td>
<code>serviceKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceKey defines the secret&rsquo;s key that contains the PagerDuty service key (when using
integration type &ldquo;Prometheus&rdquo;). Either this field or <code>routingKey</code> needs to
be defined.
The secret needs to be in the same namespace as the AlertmanagerConfig
object and accessible by the Prometheus Operator.</p>
</td>
</tr>
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
<em>(Optional)</em>
<p>url defines the URL to send requests to.</p>
</td>
</tr>
<tr>
<td>
<code>client</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>client defines the client identification.</p>
</td>
</tr>
<tr>
<td>
<code>clientURL</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientURL defines the backlink to the sender of notification.</p>
</td>
</tr>
<tr>
<td>
<code>description</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>description of the incident.</p>
</td>
</tr>
<tr>
<td>
<code>severity</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>severity of the incident.</p>
</td>
</tr>
<tr>
<td>
<code>class</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>class defines the class/type of the event.</p>
</td>
</tr>
<tr>
<td>
<code>group</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>group defines a cluster or grouping of sources.</p>
</td>
</tr>
<tr>
<td>
<code>component</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>component defines the part or component of the affected system that is broken.</p>
</td>
</tr>
<tr>
<td>
<code>details</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.KeyValue">
[]KeyValue
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>details defines the arbitrary key/value pairs that provide further detail about the incident.</p>
</td>
</tr>
<tr>
<td>
<code>pagerDutyImageConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.PagerDutyImageConfig">
[]PagerDutyImageConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>pagerDutyImageConfigs defines a list of image details to attach that provide further detail about an incident.</p>
</td>
</tr>
<tr>
<td>
<code>pagerDutyLinkConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.PagerDutyLinkConfig">
[]PagerDutyLinkConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>pagerDutyLinkConfigs defines a list of link details to attach that provide further detail about an incident.</p>
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
<p>httpConfig defines the HTTP client configuration.</p>
</td>
</tr>
<tr>
<td>
<code>source</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>source defines the unique location of the affected system.</p>
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
<p>timeout is the maximum time allowed to invoke the pagerduty
It requires Alertmanager &gt;= v0.30.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.PagerDutyImageConfig">PagerDutyImageConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.PagerDutyConfig">PagerDutyConfig</a>)
</p>
<div>
<p>PagerDutyImageConfig attaches images to an incident</p>
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
<code>src</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>src of the image being attached to the incident</p>
</td>
</tr>
<tr>
<td>
<code>href</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>href defines the optional URL; makes the image a clickable link.</p>
</td>
</tr>
<tr>
<td>
<code>alt</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alt is the optional alternative text for the image.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.PagerDutyLinkConfig">PagerDutyLinkConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.PagerDutyConfig">PagerDutyConfig</a>)
</p>
<div>
<p>PagerDutyLinkConfig attaches text links to an incident</p>
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
<code>href</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>href defines the URL of the link to be attached</p>
</td>
</tr>
<tr>
<td>
<code>alt</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alt defines the text that describes the purpose of the link, and can be used as the link&rsquo;s text.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.ParsedRange">ParsedRange
</h3>
<div>
<p>ParsedRange is an integer representation of a range</p>
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
<p>start defines the beginning of the range</p>
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
<p>end defines the end of the range</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.PrometheusAgentMode">PrometheusAgentMode
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.PrometheusAgentSpec">PrometheusAgentSpec</a>)
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
<tbody><tr><td><p>&#34;DaemonSet&#34;</p></td>
<td><p>Deploys PrometheusAgent as DaemonSet.</p>
</td>
</tr><tr><td><p>&#34;StatefulSet&#34;</p></td>
<td><p>Deploys PrometheusAgent as StatefulSet.</p>
</td>
</tr></tbody>
</table>
