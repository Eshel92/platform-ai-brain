<!-- Part 36 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.AlertmanagerConfigSpec">AlertmanagerConfigSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.AlertmanagerConfig">AlertmanagerConfig</a>)
</p>
<div>
<p>AlertmanagerConfigSpec is a specification of the desired behavior of the
Alertmanager configuration.
By default, the Alertmanager configuration only applies to alerts for which
the <code>namespace</code> label is equal to the namespace of the AlertmanagerConfig
resource (see the <code>.spec.alertmanagerConfigMatcherStrategy</code> field of the
Alertmanager CRD).</p>
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
<a href="#monitoring.coreos.com/v1alpha1.Route">
Route
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>route defines the Alertmanager route definition for alerts matching the resource&rsquo;s
namespace. If present, it will be added to the generated Alertmanager
configuration as a first-level route.</p>
</td>
</tr>
<tr>
<td>
<code>receivers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.Receiver">
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
<a href="#monitoring.coreos.com/v1alpha1.InhibitRule">
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
<code>muteTimeIntervals</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.MuteTimeInterval">
[]MuteTimeInterval
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>muteTimeIntervals defines the list of MuteTimeInterval specifying when the routes should be muted.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.AttachMetadata">AttachMetadata
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">KubernetesSDConfig</a>)
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
<code>node</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>node attaches node metadata to discovered targets.
When set to true, Prometheus must have the <code>get</code> permission on the
<code>Nodes</code> objects.
Only valid for Pod, Endpoint and Endpointslice roles.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.AuthenticationMethodType">AuthenticationMethodType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig</a>)
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
<tbody><tr><td><p>&#34;ManagedIdentity&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;OAuth&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;SDK&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;WorkloadIdentity&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>AzureSDConfig allow retrieving scrape targets from Azure VMs.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#azure_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#azure_sd_config</a></p>
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
<code>environment</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>environment defines the Azure environment.</p>
</td>
</tr>
<tr>
<td>
<code>authenticationMethod</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.AuthenticationMethodType">
AuthenticationMethodType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>authenticationMethod defines the authentication method, either <code>OAuth</code> or <code>ManagedIdentity</code> or <code>SDK</code>.
See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview</a>
SDK authentication method uses environment variables by default.
See <a href="https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication">https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication</a></p>
</td>
</tr>
<tr>
<td>
<code>subscriptionID</code><br/>
<em>
string
</em>
</td>
<td>
<p>subscriptionID defines subscription ID. Always required.</p>
</td>
</tr>
<tr>
<td>
<code>tenantID</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tenantID defines tenant ID. Only required with the OAuth authentication method.</p>
</td>
</tr>
<tr>
<td>
<code>clientID</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientID defines client ID. Only required with the OAuth authentication method.</p>
</td>
</tr>
<tr>
<td>
<code>clientSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientSecret defines client secret. Only required with the OAuth authentication method.</p>
</td>
</tr>
<tr>
<td>
<code>resourceGroup</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>resourceGroup defines resource group name. Limits discovery to this resource group.
Requires  Prometheus v2.35.0 and above</p>
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
<code>basicAuth</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.BasicAuth">
BasicAuth
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>basicAuth defines the information to authenticate against the target HTTP endpoint.
More info: <a href="https://prometheus.io/docs/operating/configuration/#endpoints">https://prometheus.io/docs/operating/configuration/#endpoints</a>
Cannot be set at the same time as <code>authorization</code>, or <code>oAuth2</code>.</p>
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
<p>authorization defines the authorization header configuration to authenticate against the target HTTP endpoint.
Cannot be set at the same time as <code>oAuth2</code>, or <code>basicAuth</code>.</p>
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
<p>oauth2 defines the configuration to use on every scrape request.</p>
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
<p>tlsConfig defines the TLS configuration applying to the target HTTP endpoint.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>ConsulSDConfig defines a Consul service discovery configuration
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#consul_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#consul_sd_config</a></p>
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
<code>server</code><br/>
<em>
string
</em>
</td>
<td>
<p>server defines the consul server address. A valid string consisting of a hostname or IP followed by an optional port number.</p>
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
<p>pathPrefix defines the prefix for URIs for when consul is behind an API gateway (reverse proxy).</p>
<p>It requires Prometheus &gt;= 2.45.0.</p>
</td>
</tr>
<tr>
<td>
<code>tokenRef</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tokenRef defines the consul ACL TokenRef, if not provided it will use the ACL from the local Consul Agent.</p>
</td>
</tr>
<tr>
<td>
<code>datacenter</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>datacenter defines the consul Datacenter name, if not provided it will use the local Consul Agent Datacenter.</p>
</td>
</tr>
<tr>
<td>
<code>namespace</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>namespace are only supported in Consul Enterprise.</p>
<p>It requires Prometheus &gt;= 2.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>partition</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>partition defines the admin Partitions are only supported in Consul Enterprise.</p>
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
<p>scheme defines the HTTP Scheme.</p>
</td>
</tr>
<tr>
<td>
<code>services</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>services defines a list of services for which targets are retrieved. If omitted, all services are scraped.</p>
</td>
</tr>
<tr>
<td>
<code>tags</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tags defines an optional list of tags used to filter nodes for a given service. Services must contain all tags in the list.
Starting with Consul 1.14, it is recommended to use <code>filter</code> with the <code>ServiceTags</code> selector instead.</p>
</td>
</tr>
<tr>
<td>
<code>tagSeparator</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tagSeparator defines the string by which Consul tags are joined into the tag label.
If unset, Prometheus uses its default value.</p>
</td>
</tr>
<tr>
<td>
<code>nodeMeta</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>nodeMeta defines the node metadata key/value pairs to filter nodes for a given service.
Starting with Consul 1.14, it is recommended to use <code>filter</code> with the <code>NodeMeta</code> selector instead.</p>
</td>
</tr>
<tr>
<td>
<code>filter</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>filter defines the filter expression used to filter the catalog results.
See <a href="https://developer.hashicorp.com/consul/api-docs/catalog#filtering">https://developer.hashicorp.com/consul/api-docs/catalog#filtering</a>
It requires Prometheus &gt;= 3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>healthFilter</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>healthFilter defines the filter expression used to filter the health results.
See <a href="https://developer.hashicorp.com/consul/api-docs/health#filtering">https://developer.hashicorp.com/consul/api-docs/health#filtering</a>
It requires Prometheus &gt;= 3.11.2.</p>
</td>
</tr>
<tr>
<td>
<code>allowStale</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>allowStale Consul results (see <a href="https://www.consul.io/api/features/consistency.html">https://www.consul.io/api/features/consistency.html</a>). Will reduce load on Consul.
If unset, Prometheus uses its default value.</p>
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
<code>basicAuth</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.BasicAuth">
BasicAuth
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>basicAuth defines the information to authenticate against the Consul Server.
More info: <a href="https://prometheus.io/docs/operating/configuration/#endpoints">https://prometheus.io/docs/operating/configuration/#endpoints</a>
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
<p>authorization defines the header configuration to authenticate against the Consul Server.
Cannot be set at the same time as <code>basicAuth</code>, or <code>oauth2</code>.</p>
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
<p>tlsConfig defines the TLS configuration to connect to the Consul API.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.DNSRecordType">DNSRecordType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.DNSSDConfig">DNSSDConfig</a>)
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
<tbody><tr><td><p>&#34;A&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;AAAA&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;MX&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;NS&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;SRV&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.DNSSDConfig">DNSSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>DNSSDConfig allows specifying a set of DNS domain names which are periodically queried to discover a list of targets.
The DNS servers to be contacted are read from /etc/resolv.conf.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#dns_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#dns_sd_config</a></p>
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
<code>names</code><br/>
<em>
[]string
</em>
</td>
<td>
<p>names defines a list of DNS domain names to be queried.</p>
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
<code>type</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.DNSRecordType">
DNSRecordType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>type defines the type of DNS query to perform. One of SRV, A, AAAA, MX or NS.
If not set, Prometheus uses its default value.</p>
<p>When set to NS, it requires Prometheus &gt;= v2.49.0.
When set to MX, it requires Prometheus &gt;= v2.38.0</p>
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
Ignored for SRV records</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.DayOfMonthRange">DayOfMonthRange
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.TimeInterval">TimeInterval</a>)
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
