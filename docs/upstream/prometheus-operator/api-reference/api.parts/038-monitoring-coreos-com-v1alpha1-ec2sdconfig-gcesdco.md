<!-- Part 38 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.EC2SDConfig">EC2SDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>EC2SDConfig allow retrieving scrape targets from AWS EC2 instances.
The private IP address is used by default, but may be changed to the public IP address with relabeling.
The IAM credentials used must have the ec2:DescribeInstances permission to discover scrape targets
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#ec2_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#ec2_sd_config</a></p>
<p>The EC2 service discovery requires AWS API keys or role ARN for authentication.
BasicAuth, Authorization and OAuth2 fields are not present on purpose.</p>
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
<code>region</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>region defines the AWS region.</p>
</td>
</tr>
<tr>
<td>
<code>accessKey</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>accessKey defines the AWS API key.</p>
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
<em>(Optional)</em>
<p>secretKey defines the AWS API secret.</p>
</td>
</tr>
<tr>
<td>
<code>roleARN</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>roleARN defines an alternative to using AWS API keys.</p>
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
<code>filters</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.Filters">
Filters
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>filters can be used optionally to filter the instance list by other criteria.
Available filter criteria can be found here:
<a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html">https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html</a>
Filter API documentation: <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Filter.html">https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Filter.html</a>
It requires Prometheus &gt;= v2.3.0</p>
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
<p>tlsConfig defines the TLS configuration to connect to the EC2 API.
It requires Prometheus &gt;= v2.41.0</p>
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
It requires Prometheus &gt;= v2.41.0</p>
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
<p>enableHTTP2 defines whether to enable HTTP2.
It requires Prometheus &gt;= v2.41.0</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.EmailConfig">EmailConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.Receiver">Receiver</a>)
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
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
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
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
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
<a href="#monitoring.coreos.com/v1alpha1.KeyValue">
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
<a href="#monitoring.coreos.com/v1alpha1.EmailThreadingConfig">
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

<h3 id="monitoring.coreos.com/v1alpha1.EmailThreadingConfig">EmailThreadingConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.EmailConfig">EmailConfig</a>)
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
<a href="#monitoring.coreos.com/v1alpha1.ThreadByDateType">
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

<h3 id="monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>Eureka SD configurations allow retrieving scrape targets using the Eureka REST API.
Prometheus will periodically check the REST endpoint and create a target for every app instance.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#eureka_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#eureka_sd_config</a></p>
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
<a href="#monitoring.coreos.com/v1alpha1.URL">
URL
</a>
</em>
</td>
<td>
<p>server defines the URL to connect to the Eureka server.</p>
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
<p>basicAuth defines the BasicAuth information to use on every scrape request.</p>
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
<p>authorization defines the header configuration to authenticate against the Eureka server.
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
<p>oauth2 defines the configuration to use on every scrape request.</p>
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
<p>tlsConfig defines the TLS configuration to connect to the Eureka server.</p>
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

<h3 id="monitoring.coreos.com/v1alpha1.FileSDConfig">FileSDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>FileSDConfig defines a Prometheus file service discovery configuration
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#file_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#file_sd_config</a></p>
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
<code>files</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.SDFile">
[]SDFile
</a>
</em>
</td>
<td>
<p>files defines the list of files to be used for file discovery. Recommendation: use absolute paths. While relative paths work, the
prometheus-operator project makes no guarantees about the working directory where the configuration file is
stored.
Files must be mounted using Prometheus.ConfigMaps or Prometheus.Secrets.</p>
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

<h3 id="monitoring.coreos.com/v1alpha1.Filter">Filter
</h3>
<div>
<p>Filter name and value pairs to limit the discovery process to a subset of available resources.</p>
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
<p>name of the Filter.</p>
</td>
</tr>
<tr>
<td>
<code>values</code><br/>
<em>
[]string
</em>
</td>
<td>
<p>values defines values to filter on.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1alpha1.Filters">Filters
(<code>[]github.com/prometheus-operator/prometheus-operator/pkg/apis/monitoring/v1alpha1.Filter</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">DockerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">DockerSwarmSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EC2SDConfig">EC2SDConfig</a>)
</p>
<div>
</div>

<h3 id="monitoring.coreos.com/v1alpha1.GCESDConfig">GCESDConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>GCESDConfig configures scrape targets from GCP GCE instances.
The private IP address is used by default, but may be changed to
the public IP address with relabeling.
See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#gce_sd_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#gce_sd_config</a></p>
<p>The GCE service discovery will load the Google Cloud credentials
from the file specified by the GOOGLE_APPLICATION_CREDENTIALS environment variable.
See <a href="https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform">https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform</a></p>
<p>A pre-requisite for using GCESDConfig is that a Secret containing valid
Google Cloud credentials is mounted into the Prometheus or PrometheusAgent
pod via the <code>.spec.secrets</code> field and that the GOOGLE_APPLICATION_CREDENTIALS
environment variable is set to /etc/prometheus/secrets/<secret-name>/<credentials-filename.json>.</p>
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
<code>project</code><br/>
<em>
string
</em>
</td>
<td>
<p>project defines the Google Cloud Project ID</p>
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
<p>zone defines the zone of the scrape targets. If you need multiple zones use multiple GCESDConfigs.</p>
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
<p>filter defines the filter that can be used optionally to filter the instance list by other criteria
Syntax of this filter is described in the filter query parameter section:
<a href="https://cloud.google.com/compute/docs/reference/latest/instances/list">https://cloud.google.com/compute/docs/reference/latest/instances/list</a></p>
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
<code>tagSeparator</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tagSeparator defines the tag separator is used to separate the tags on concatenation</p>
</td>
</tr>
</tbody>
</table>
