<!-- Part 21 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitor">PodMonitor</a>)
</p>
<div>
<p>PodMonitorSpec contains specification parameters for a PodMonitor.</p>
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
<code>jobLabel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>jobLabel defines the label to use to retrieve the job name from.
<code>jobLabel</code> selects the label from the associated Kubernetes <code>Pod</code>
object which will be used as the <code>job</code> label for all metrics.</p>
<p>For example if <code>jobLabel</code> is set to <code>foo</code> and the Kubernetes <code>Pod</code>
object is labeled with <code>foo: bar</code>, then Prometheus adds the <code>job=&quot;bar&quot;</code>
label to all ingested metrics.</p>
<p>If the value of this field is empty, the <code>job</code> label of the metrics
defaults to the namespace and name of the PodMonitor object (e.g. <code>&lt;namespace&gt;/&lt;name&gt;</code>).</p>
</td>
</tr>
<tr>
<td>
<code>podTargetLabels</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>podTargetLabels defines the labels which are transferred from the
associated Kubernetes <code>Pod</code> object onto the ingested metrics.</p>
</td>
</tr>
<tr>
<td>
<code>podMetricsEndpoints</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PodMetricsEndpoint">
[]PodMetricsEndpoint
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>podMetricsEndpoints defines how to scrape metrics from the selected pods.</p>
</td>
</tr>
<tr>
<td>
<code>selector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<p>selector defines the label selector to select the Kubernetes <code>Pod</code> objects to scrape metrics from.</p>
</td>
</tr>
<tr>
<td>
<code>selectorMechanism</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SelectorMechanism">
SelectorMechanism
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>selectorMechanism defines the mechanism used to select the endpoints to scrape.
By default, the selection process relies on relabel configurations to filter the discovered targets.
Alternatively, you can opt in for role selectors, which may offer better efficiency in large clusters.
Which strategy is best for your use case needs to be carefully evaluated.</p>
<p>It requires Prometheus &gt;= v2.17.0.</p>
</td>
</tr>
<tr>
<td>
<code>namespaceSelector</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.NamespaceSelector">
NamespaceSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>namespaceSelector defines in which namespace(s) Prometheus should discover the pods.
By default, the pods are discovered in the same namespace as the <code>PodMonitor</code> object but it is possible to select pods across different/all namespaces.</p>
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
<p>sampleLimit defines a per-scrape limit on the number of scraped samples
that will be accepted.</p>
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
<p>targetLimit defines a limit on the number of scraped targets that will
be accepted.</p>
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
<code>labelLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>labelLimit defines the per-scrape limit on number of labels that will be accepted for a sample.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
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
<p>labelNameLengthLimit defines the per-scrape limit on length of labels name that will be accepted for a sample.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
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
<p>labelValueLengthLimit defines the per-scrape limit on length of labels value that will be accepted for a sample.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
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
<code>attachMetadata</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AttachMetadata">
AttachMetadata
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>attachMetadata defines additional metadata which is added to the
discovered targets.</p>
<p>It requires Prometheus &gt;= v2.35.0.</p>
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
<p>bodySizeLimit when defined specifies a job level limit on the size
of uncompressed response body that will be accepted by Prometheus.</p>
<p>It requires Prometheus &gt;= v2.28.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ProbeParam">ProbeParam
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ProbeSpec">ProbeSpec</a>)
</p>
<div>
<p>ProbeParam defines specification of extra parameters for a Probe.</p>
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
<p>name defines the parameter name</p>
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
<em>(Optional)</em>
<p>values defines the parameter values</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ProbeSpec">ProbeSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Probe">Probe</a>)
</p>
<div>
<p>ProbeSpec contains specification parameters for a Probe.</p>
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
<code>jobName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>jobName assigned to scraped metrics by default.</p>
</td>
</tr>
<tr>
<td>
<code>prober</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ProberSpec">
ProberSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>prober defines the specification for the prober to use for probing targets.
The prober.URL parameter is required. Targets cannot be probed if left empty.</p>
</td>
</tr>
<tr>
<td>
<code>module</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>module to use for probing specifying how to probe the target.
Example module configuring in the blackbox exporter:
<a href="https://github.com/prometheus/blackbox_exporter/blob/master/example.yml">https://github.com/prometheus/blackbox_exporter/blob/master/example.yml</a></p>
</td>
</tr>
<tr>
<td>
<code>targets</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ProbeTargets">
ProbeTargets
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>targets defines a set of static or dynamically discovered targets to probe.</p>
</td>
</tr>
<tr>
<td>
<code>interval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>interval at which targets are probed using the configured prober.
If not specified Prometheus&rsquo; global scrape interval is used.</p>
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
<p>scrapeTimeout defines the timeout for scraping metrics from the Prometheus exporter.
If not specified, the Prometheus global scrape timeout is used.
The value cannot be greater than the scrape interval otherwise the operator will reject the resource.</p>
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
<p>metricRelabelings defines the RelabelConfig to apply to samples before ingestion.</p>
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
<p>authorization section for this endpoint</p>
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
<tr>
<td>
<code>params</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ProbeParam">
[]ProbeParam
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>params defines the list of HTTP query parameters for the scrape.
Please note that the <code>.spec.module</code> field takes precedence over the <code>module</code> parameter from this list when both are defined.
The module name must be added using Module under ProbeSpec.</p>
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
<p>authorization configures the Authorization header credentials used by
the client.</p>
<p>Cannot be set at the same time as <code>basicAuth</code>, <code>bearerTokenSecret</code> or <code>oauth2</code>.</p>
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
<p>basicAuth defines the Basic Authentication credentials used by the
client.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>bearerTokenSecret</code> or <code>oauth2</code>.</p>
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
<p>oauth2 defines the OAuth2 settings used by the client.</p>
<p>It requires Prometheus &gt;= 2.27.0.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code> or <code>bearerTokenSecret</code>.</p>
</td>
</tr>
<tr>
<td>
<code>bearerTokenSecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>bearerTokenSecret defines a key of a Secret containing the bearer token
used by the client for authentication. The secret needs to be in the
same namespace as the custom resource and readable by the Prometheus
Operator.</p>
<p>Cannot be set at the same time as <code>authorization</code>, <code>basicAuth</code> or <code>oauth2</code>.</p>
<p>Deprecated: use <code>authorization</code> instead.</p>
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
<p>followRedirects defines whether the client should follow HTTP 3xx
redirects.</p>
</td>
</tr>
<tr>
<td>
<code>enableHttp2</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableHttp2 can be used to disable HTTP2.</p>
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
<p>tlsConfig defines the TLS configuration used by the client.</p>
</td>
</tr>
</tbody>
</table>
