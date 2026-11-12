<!-- Part 42 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.OVHCloudSDConfig">OVHCloudSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>OVHCloudSDConfig configurations allow retrieving scrape targets from OVHcloud&rsquo;s dedicated servers and VPS using their API.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#ovhcloud_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#ovhcloud_sd_config</a></p>
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
<code>applicationKey</code><br/>
<em>
string
</em>
</td>
<td>
<p>applicationKey defines the access key to use for OVHCloud API authentication.
This is obtained from the OVHCloud API credentials at <a href="https://api.ovh.com">https://api.ovh.com</a>.</p>
</td>
</tr>
<tr>
<td>
<code>applicationSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<p>applicationSecret defines the secret key for OVHCloud API authentication.
This contains the application secret obtained during OVHCloud API credential creation.</p>
</td>
</tr>
<tr>
<td>
<code>consumerKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<p>consumerKey defines the consumer key for OVHCloud API authentication.
This is the third component of OVHCloud&rsquo;s three-key authentication system.</p>
</td>
</tr>
<tr>
<td>
<code>service</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OVHService">
OVHService
</a>
</em>
</td>
<td>
<p>service defines the service type of the targets to retrieve.
Must be either <code>VPS</code> or <code>DedicatedServer</code> to specify which OVHCloud resources to discover.</p>
</td>
</tr>
<tr>
<td>
<code>endpoint</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>endpoint defines a custom API endpoint to be used.
When not specified, defaults to the standard OVHCloud API endpoint for the region.</p>
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
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.OVHService">OVHService
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.OVHCloudSDConfig">OVHCloudSDConfig</a>)
</p>
<div>
<p>Service of the targets to retrieve. Must be <code>VPS</code> or <code>DedicatedServer</code>.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;DedicatedServer&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;VPS&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.OpenStackAvailability">OpenStackAvailability
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.OpenStackSDConfig">OpenStackSDConfig</a>)
</p>
<div>
<p>OpenStackAvailability defines the availability of the endpoint to connect to.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;Admin&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Internal&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Public&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.OpenStackRole">OpenStackRole
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.OpenStackSDConfig">OpenStackSDConfig</a>)
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
<tbody><tr><td><p>&#34;Hypervisor&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Instance&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;LoadBalancer&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.OpenStackSDConfig">OpenStackSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>OpenStackSDConfig allow retrieving scrape targets from OpenStack Nova instances.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#openstack_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#openstack_sd_config</a></p>
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
<code>role</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OpenStackRole">
OpenStackRole
</a>
</em>
</td>
<td>
<p>role defines the OpenStack role of entities that should be discovered.</p>
<p>Note: The <code>LoadBalancer</code> role requires Prometheus &gt;= v3.2.0.</p>
</td>
</tr>
<tr>
<td>
<code>region</code><br/>
<em>
string
</em>
</td>
<td>
<p>region defines the OpenStack Region.</p>
</td>
</tr>
<tr>
<td>
<code>identityEndpoint</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>identityEndpoint defines the HTTP endpoint that is required to work with
the Identity API of the appropriate version.</p>
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
<p>username defines the username required if using Identity V2 API. Consult with your provider&rsquo;s
control panel to discover your account&rsquo;s username.
In Identity V3, either userid or a combination of username
and domainId or domainName are needed</p>
</td>
</tr>
<tr>
<td>
<code>userid</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>userid defines the OpenStack userid.</p>
</td>
</tr>
<tr>
<td>
<code>password</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>password defines the password for the Identity V2 and V3 APIs. Consult with your provider&rsquo;s
control panel to discover your account&rsquo;s preferred method of authentication.</p>
</td>
</tr>
<tr>
<td>
<code>domainName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>domainName defines at most one of domainId and domainName that must be provided if using username
with Identity V3. Otherwise, either are optional.</p>
</td>
</tr>
<tr>
<td>
<code>domainID</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>domainID defines The OpenStack domainID.</p>
</td>
</tr>
<tr>
<td>
<code>projectName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>projectName defines an optional field for the Identity V2 API.
Some providers allow you to specify a ProjectName instead of the ProjectId.
Some require both. Your provider&rsquo;s authentication policies will determine
how these fields influence authentication.</p>
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
<em>(Optional)</em>
<p>projectID defines the OpenStack projectID.</p>
</td>
</tr>
<tr>
<td>
<code>applicationCredentialName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>applicationCredentialName defines the ApplicationCredentialID or ApplicationCredentialName fields are
required if using an application credential to authenticate. Some providers
allow you to create an application credential to authenticate rather than a
password.</p>
</td>
</tr>
<tr>
<td>
<code>applicationCredentialId</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>applicationCredentialId defines the OpenStack applicationCredentialId.</p>
</td>
</tr>
<tr>
<td>
<code>applicationCredentialSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>applicationCredentialSecret defines the required field if using an application
credential to authenticate.</p>
</td>
</tr>
<tr>
<td>
<code>allTenants</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>allTenants defines whether the service discovery should list all instances for all projects.
It is only relevant for the &lsquo;instance&rsquo; role and usually requires admin permissions.</p>
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
<p>port defines the port to scrape metrics from. If using the public IP address, this must
instead be specified in the relabeling rule.</p>
</td>
</tr>
<tr>
<td>
<code>availability</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OpenStackAvailability">
OpenStackAvailability
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>availability defines the availability of the endpoint to connect to.</p>
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
<p>tlsConfig defines the TLS configuration applying to the target HTTP endpoint.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.OpsGenieConfig">OpsGenieConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
</p>
<div>
<p>OpsGenieConfig configures notifications via OpsGenie.
See <a href="https://prometheus.io/docs/alerting/latest/configuration/#opsgenie_config">https://prometheus.io/docs/alerting/latest/configuration/#opsgenie_config</a></p>
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
<p>apiKey defines the secret&rsquo;s key that contains the OpsGenie API key.
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
<p>apiURL defines the URL to send OpsGenie API requests to.
When not specified, defaults to the standard OpsGenie API endpoint.</p>
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
<p>message defines the alert text limited to 130 characters.
This appears as the main alert title in OpsGenie.</p>
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
<p>description defines the detailed description of the incident.
This provides additional context beyond the message field.</p>
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
<p>source defines the backlink to the sender of the notification.
This helps identify where the alert originated from.</p>
</td>
</tr>
<tr>
<td>
<code>tags</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tags defines a comma separated list of tags attached to the notifications.
These help categorize and filter alerts within OpsGenie.</p>
</td>
</tr>
<tr>
<td>
<code>note</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>note defines an additional alert note.
This provides supplementary information about the alert.</p>
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
<p>priority defines the priority level of alert.
Possible values are P1, P2, P3, P4, and P5, where P1 is highest priority.</p>
</td>
</tr>
<tr>
<td>
<code>updateAlerts</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>updateAlerts defines Whether to update message and description of the alert in OpsGenie if it already exists
By default, the alert is never updated in OpsGenie, the new message only appears in activity log.</p>
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
<p>details defines a set of arbitrary key/value pairs that provide further detail about the incident.
These appear as additional fields in the OpsGenie alert.</p>
</td>
</tr>
<tr>
<td>
<code>responders</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OpsGenieConfigResponder">
[]OpsGenieConfigResponder
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>responders defines the list of responders responsible for notifications.
These determine who gets notified when the alert is created.</p>
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
<p>httpConfig defines the HTTP client configuration for OpsGenie API requests.</p>
</td>
</tr>
<tr>
<td>
<code>entity</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>entity defines an optional field that can be used to specify which domain alert is related to.
This helps group related alerts together in OpsGenie.</p>
</td>
</tr>
<tr>
<td>
<code>actions</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>actions defines a comma separated list of actions that will be available for the alert.
These appear as action buttons in the OpsGenie interface.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.OpsGenieConfigResponder">OpsGenieConfigResponder
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.OpsGenieConfig">OpsGenieConfig</a>)
</p>
<div>
<p>OpsGenieConfigResponder defines a responder to an incident.
One of <code>id</code>, <code>name</code> or <code>username</code> has to be defined.</p>
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
<code>id</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>id defines the unique identifier of the responder.
This corresponds to the responder&rsquo;s ID within OpsGenie.</p>
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
<p>name defines the display name of the responder.
This is used when the responder is identified by name rather than ID.</p>
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
<p>username defines the username of the responder.
This is typically used for user-type responders when identifying by username.</p>
</td>
</tr>
<tr>
<td>
<code>type</code><br/>
<em>
string
</em>
</td>
<td>
<p>type defines the type of responder.
Valid values include &ldquo;user&rdquo;, &ldquo;team&rdquo;, &ldquo;schedule&rdquo;, and &ldquo;escalation&rdquo;.
This determines how OpsGenie interprets the other identifier fields.</p>
</td>
</tr>
</tbody>
</table>
