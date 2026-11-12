<!-- Part 7 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.PrometheusRule">PrometheusRule
</h3>
<div>
<p>The <code>PrometheusRule</code> custom resource definition (CRD) defines <a href="https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/">alerting</a> and <a href="https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/">recording</a> rules to be evaluated by <code>Prometheus</code> or <code>ThanosRuler</code> objects.</p>
<p><code>Prometheus</code> and <code>ThanosRuler</code> objects select <code>PrometheusRule</code> objects using label and namespace selectors.</p>
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
monitoring.coreos.com/v1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code><br/>
string
</td>
<td><code>PrometheusRule</code></td>
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
<a href="#monitoring.coreos.com/v1.PrometheusRuleSpec">
PrometheusRuleSpec
</a>
</em>
</td>
<td>
<p>spec defines the specification of desired alerting rule definitions for Prometheus.</p>
<br/>
<br/>
<table>
<tr>
<td>
<code>groups</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RuleGroup">
[]RuleGroup
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>groups defines the content of Prometheus rule file</p>
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
<p>Most recent observed status of the PrometheusRule. Read-only.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ServiceMonitor">ServiceMonitor
</h3>
<div>
<p>The <code>ServiceMonitor</code> custom resource definition (CRD) defines how <code>Prometheus</code> and <code>PrometheusAgent</code> can scrape metrics from a group of services.
Among other things, it allows to specify:
* The services to scrape via label selectors.
* The container ports to scrape.
* Authentication credentials to use.
* Target and metric relabeling.</p>
<p><code>Prometheus</code> and <code>PrometheusAgent</code> objects select <code>ServiceMonitor</code> objects using label and namespace selectors.</p>
<p>Service targets that aren&rsquo;t backed by Pods (for instance manually managed
Endpoints or EndpointSlices) can only be scraped when the endpoint selects
the service port with <code>port</code> instead of <code>targetPort</code> and <code>filterRunning</code> is
set to <code>false</code>. Manually created Pods have no such restriction.</p>
<p>For targets that aren&rsquo;t backed by Pods, you can also consider using the
<code>ScrapeConfig</code> CRD.</p>
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
monitoring.coreos.com/v1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code><br/>
string
</td>
<td><code>ServiceMonitor</code></td>
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
<a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">
ServiceMonitorSpec
</a>
</em>
</td>
<td>
<p>spec defines the specification of desired Service selection for target discovery by
Prometheus.</p>
<br/>
<br/>
<table>
<tr>
<td>
<code>jobLabel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>jobLabel selects the label from the associated Kubernetes <code>Service</code>
object which will be used as the <code>job</code> label for all metrics.</p>
<p>For example if <code>jobLabel</code> is set to <code>foo</code> and the Kubernetes <code>Service</code>
object is labeled with <code>foo: bar</code>, then Prometheus adds the <code>job=&quot;bar&quot;</code>
label to all ingested metrics.</p>
<p>If the value of this field is empty or if the label doesn&rsquo;t exist for
the given Service, the <code>job</code> label of the metrics defaults to the name
of the associated Kubernetes <code>Service</code>.</p>
</td>
</tr>
<tr>
<td>
<code>targetLabels</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>targetLabels defines the labels which are transferred from the
associated Kubernetes <code>Service</code> object onto the ingested metrics.</p>
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
<code>endpoints</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Endpoint">
[]Endpoint
</a>
</em>
</td>
<td>
<p>endpoints defines the list of endpoints part of this ServiceMonitor.
Defines how to scrape metrics from Kubernetes <a href="https://kubernetes.io/docs/concepts/services-networking/service/#endpoints">Endpoints</a> objects.
In most cases, an Endpoints object is backed by a Kubernetes <a href="https://kubernetes.io/docs/concepts/services-networking/service/">Service</a> object with the same name and labels.</p>
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
<p>selector defines the label selector to select the Kubernetes <code>Endpoints</code> objects to scrape metrics from.</p>
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
<p>namespaceSelector defines in which namespace(s) Prometheus should discover the services.
By default, the services are discovered in the same namespace as the <code>ServiceMonitor</code> object but it is possible to select pods across different/all namespaces.</p>
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
<p>It requires Prometheus &gt;= v2.37.0.</p>
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
<p>bodySizeLimit when defined, bodySizeLimit specifies a job level limit on the size
of uncompressed response body that will be accepted by Prometheus.</p>
<p>It requires Prometheus &gt;= v2.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>serviceDiscoveryRole</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ServiceDiscoveryRole">
ServiceDiscoveryRole
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceDiscoveryRole defines the service discovery role used to discover targets.</p>
<p>If set, the value should be either &ldquo;Endpoints&rdquo; or &ldquo;EndpointSlice&rdquo;.
Otherwise it defaults to the value defined in the
Prometheus/PrometheusAgent resource.</p>
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
<p>Most recent observed status of the ServiceMonitor. Read-only.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
</td>
</tr>
</tbody>
</table>
