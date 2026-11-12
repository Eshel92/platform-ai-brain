<!-- Part 35 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1alpha1.ScrapeConfig">ScrapeConfig
</h3>
<div>
<p>ScrapeConfig defines a namespaced Prometheus scrape_config to be aggregated across
multiple namespaces into the Prometheus configuration.</p>
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
monitoring.coreos.com/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code><br/>
string
</td>
<td><code>ScrapeConfig</code></td>
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
<a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">
ScrapeConfigSpec
</a>
</em>
</td>
<td>
<p>spec defines the specification of ScrapeConfigSpec.</p>
<br/>
<br/>
<table>
<tr>
<td>
<code>jobName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>jobName defines the value of the <code>job</code> label assigned to the scraped metrics by default.</p>
<p>The <code>job_name</code> field in the rendered scrape configuration is always controlled by the
operator to prevent duplicate job names, which Prometheus does not allow. Instead the
<code>job</code> label is set by means of relabeling configs.</p>
</td>
</tr>
<tr>
<td>
<code>staticConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.StaticConfig">
[]StaticConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>staticConfigs defines a list of static targets with a common label set.</p>
</td>
</tr>
<tr>
<td>
<code>fileSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.FileSDConfig">
[]FileSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>fileSDConfigs defines a list of file service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>httpSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">
[]HTTPSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpSDConfigs defines a list of HTTP service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>kubernetesSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">
[]KubernetesSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>kubernetesSDConfigs defines a list of Kubernetes service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>consulSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">
[]ConsulSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>consulSDConfigs defines a list of Consul service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>dnsSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.DNSSDConfig">
[]DNSSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>dnsSDConfigs defines a list of DNS service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>ec2SDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.EC2SDConfig">
[]EC2SDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ec2SDConfigs defines a list of EC2 service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>azureSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">
[]AzureSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>azureSDConfigs defines a list of Azure service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>gceSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.GCESDConfig">
[]GCESDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>gceSDConfigs defines a list of GCE service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>openstackSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OpenStackSDConfig">
[]OpenStackSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>openstackSDConfigs defines a list of OpenStack service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>digitalOceanSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.DigitalOceanSDConfig">
[]DigitalOceanSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>digitalOceanSDConfigs defines a list of DigitalOcean service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>kumaSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">
[]KumaSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>kumaSDConfigs defines a list of Kuma service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>eurekaSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">
[]EurekaSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>eurekaSDConfigs defines a list of Eureka service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>dockerSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">
[]DockerSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>dockerSDConfigs defines a list of Docker service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>linodeSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.LinodeSDConfig">
[]LinodeSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>linodeSDConfigs defines a list of Linode service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>hetznerSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.HetznerSDConfig">
[]HetznerSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>hetznerSDConfigs defines a list of Hetzner service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>nomadSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">
[]NomadSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>nomadSDConfigs defines a list of Nomad service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>dockerSwarmSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">
[]DockerSwarmSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>dockerSwarmSDConfigs defines a list of Dockerswarm service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>puppetDBSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">
[]PuppetDBSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>puppetDBSDConfigs defines a list of PuppetDB service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>lightSailSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.LightSailSDConfig">
[]LightSailSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>lightSailSDConfigs defines a list of Lightsail service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>ovhcloudSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.OVHCloudSDConfig">
[]OVHCloudSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ovhcloudSDConfigs defines a list of OVHcloud service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>scalewaySDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.ScalewaySDConfig">
[]ScalewaySDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scalewaySDConfigs defines a list of Scaleway instances and baremetal service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>ionosSDConfigs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.IonosSDConfig">
[]IonosSDConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ionosSDConfigs defines a list of IONOS service discovery configurations.</p>
</td>
</tr>
<tr>
<td>
<code>relabelings</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>relabelings defines how to rewrite the target&rsquo;s labels before scraping.
Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields.
The original scrape job&rsquo;s name is available via the <code>__tmp_prometheus_job_name</code> label.
More info: <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config</a></p>
</td>
</tr>
<tr>
<td>
<code>metricsPath</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>metricsPath defines the HTTP path to scrape for metrics. If empty, Prometheus uses the default value (e.g. /metrics).</p>
</td>
</tr>
<tr>
<td>
<code>scrapeInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeInterval defines the interval between consecutive scrapes.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeTimeout defines the number of seconds to wait until a scrape request times out.
The value cannot be greater than the scrape interval otherwise the operator will reject the resource.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeProtocols</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ScrapeProtocol">
[]ScrapeProtocol
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeProtocols defines the protocols to negotiate during a scrape. It tells clients the
protocols supported by Prometheus in order of preference (from most to least preferred).</p>
<p>If unset, Prometheus uses its default value.</p>
<p>It requires Prometheus &gt;= v2.49.0.</p>
</td>
</tr>
<tr>
<td>
<code>fallbackScrapeProtocol</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ScrapeProtocol">
ScrapeProtocol
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>fallbackScrapeProtocol defines the protocol to use if a scrape returns blank, unparseable, or otherwise invalid Content-Type.</p>
<p>It requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>extraScrapeMetrics</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>extraScrapeMetrics defines whether to store additional time series for each scrape:
<code>scrape_timeout_seconds</code>, <code>scrape_sample_limit</code> and <code>scrape_body_size_bytes</code>.
These metrics help monitor how close targets are to their configured limits.</p>
<p>It requires Prometheus &gt;= v3.10.0.</p>
</td>
</tr>
<tr>
<td>
<code>honorTimestamps</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>honorTimestamps defines whether Prometheus preserves the timestamps
when exposed by the target.</p>
</td>
</tr>
<tr>
<td>
<code>trackTimestampsStaleness</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>trackTimestampsStaleness defines whether Prometheus tracks staleness of
the metrics that have an explicit timestamp present in scraped data.
Has no effect if <code>honorTimestamps</code> is false.
It requires Prometheus &gt;= v2.48.0.</p>
</td>
</tr>
<tr>
<td>
<code>honorLabels</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>honorLabels defines when true the metric&rsquo;s labels when they collide
with the target&rsquo;s labels.</p>
</td>
</tr>
<tr>
<td>
<code>params</code><br/>
<em>
map[string][]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>params defines optional HTTP URL parameters</p>
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
<p>scheme defines the protocol scheme used for requests.</p>
</td>
</tr>
<tr>
<td>
<code>enableCompression</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableCompression when false, Prometheus will request uncompressed response from the scraped target.</p>
<p>It requires Prometheus &gt;= v2.49.0.</p>
<p>If unset, Prometheus uses true by default.</p>
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
<code>basicAuth</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.BasicAuth">
BasicAuth
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>basicAuth defines information to use on every scrape request.</p>
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
<p>authorization defines the header to use on every scrape request.</p>
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
<p>tlsConfig defines the TLS configuration to use on every scrape request</p>
</td>
</tr>
<tr>
<td>
<code>sampleLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>sampleLimit defines per-scrape limit on number of scraped samples that will be accepted.</p>
</td>
</tr>
<tr>
<td>
<code>targetLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>targetLimit defines a limit on the number of scraped targets that will be accepted.</p>
</td>
</tr>
<tr>
<td>
<code>labelLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>labelLimit defines the per-scrape limit on number of labels that will be accepted for a sample.
Only valid in Prometheus versions 2.27.0 and newer.</p>
</td>
</tr>
<tr>
<td>
<code>labelNameLengthLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>labelNameLengthLimit defines the per-scrape limit on length of labels name that will be accepted for a sample.
Only valid in Prometheus versions 2.27.0 and newer.</p>
</td>
</tr>
<tr>
<td>
<code>labelValueLengthLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>labelValueLengthLimit defines the per-scrape limit on length of labels value that will be accepted for a sample.
Only valid in Prometheus versions 2.27.0 and newer.</p>
</td>
</tr>
<tr>
<td>
<code>bodySizeLimit</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ByteSize">
ByteSize
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>bodySizeLimit defines a per-scrape limit on the size of the uncompressed
response body that will be accepted by Prometheus. Targets responding with
a body larger than this many bytes will cause the scrape to fail.</p>
<p>It requires Prometheus &gt;= v2.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeNativeHistograms</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeNativeHistograms defines whether to enable scraping of native histograms.
It requires Prometheus &gt;= v3.8.0.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeClassicHistograms</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeClassicHistograms defines whether to scrape a classic histogram that is also exposed as a native histogram.
It requires Prometheus &gt;= v2.45.0.</p>
<p>Notice: <code>scrapeClassicHistograms</code> corresponds to the <code>always_scrape_classic_histograms</code> field in the Prometheus configuration.</p>
</td>
</tr>
<tr>
<td>
<code>nativeHistogramBucketLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>nativeHistogramBucketLimit defines ff there are more than this many buckets in a native histogram,
buckets will be merged to stay within the limit.
It requires Prometheus &gt;= v2.45.0.</p>
</td>
</tr>
<tr>
<td>
<code>nativeHistogramMinBucketFactor</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity">
k8s.io/apimachinery/pkg/api/resource.Quantity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>nativeHistogramMinBucketFactor defines if the growth factor of one bucket to the next is smaller than this,
buckets will be merged to increase the factor sufficiently.
It requires Prometheus &gt;= v2.50.0.</p>
</td>
</tr>
<tr>
<td>
<code>convertClassicHistogramsToNHCB</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>convertClassicHistogramsToNHCB defines whether to convert all scraped classic histograms into a native histogram with custom buckets.
It requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>keepDroppedTargets</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>keepDroppedTargets defines the per-scrape limit on the number of targets dropped by relabeling
that will be kept in memory. 0 means no limit.</p>
<p>It requires Prometheus &gt;= v2.47.0.</p>
</td>
</tr>
<tr>
<td>
<code>metricRelabelings</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RelabelConfig">
[]RelabelConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>metricRelabelings defines the metricRelabelings to apply to samples before ingestion.</p>
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
<code>nameValidationScheme</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NameValidationSchemeOptions">
NameValidationSchemeOptions
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>nameValidationScheme defines the validation scheme for metric and label names.</p>
<p>It requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>nameEscapingScheme</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NameEscapingSchemeOptions">
NameEscapingSchemeOptions
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>nameEscapingScheme defines the metric name escaping mode to request through content negotiation.</p>
<p>It requires Prometheus &gt;= v3.4.0.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeClass</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeClass defines the scrape class to apply.</p>
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
<p>Most recent observed status of the ScrapeConfig. Read-only.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
</td>
</tr>
</tbody>
</table>
