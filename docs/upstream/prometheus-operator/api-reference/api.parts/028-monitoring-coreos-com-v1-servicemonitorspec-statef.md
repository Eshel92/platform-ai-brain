<!-- Part 28 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ServiceMonitor">ServiceMonitor</a>)
</p>
<div>
<p>ServiceMonitorSpec defines the specification parameters for a ServiceMonitor.</p>
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
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ShardRetentionPolicy">ShardRetentionPolicy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>)
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
<code>whenScaled</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WhenScaledRetentionType">
WhenScaledRetentionType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>whenScaled defines the retention policy when the Prometheus shards are scaled down.
* <code>Delete</code>, the operator will delete the pods from the scaled-down shard(s).
* <code>Retain</code>, the operator will keep the pods from the scaled-down shard(s), so the data can still be queried.</p>
<p>If not defined, the operator assumes the <code>Delete</code> value.</p>
</td>
</tr>
<tr>
<td>
<code>retain</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RetainConfig">
RetainConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>retain defines the config for retention when the retention policy is set
to <code>Retain</code>.</p>
<p>If not defined, the operator will use the retention duration configured
for the Prometheus data. If the resource uses size-based retention, the
shard(s) are kept forever (unless manually deleted).</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ShardStatus">ShardStatus
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusStatus">PrometheusStatus</a>)
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
<code>shardID</code><br/>
<em>
string
</em>
</td>
<td>
<p>shardID defines the identifier of the shard.</p>
</td>
</tr>
<tr>
<td>
<code>replicas</code><br/>
<em>
int32
</em>
</td>
<td>
<p>replicas defines the total number of pods targeted by this shard.</p>
</td>
</tr>
<tr>
<td>
<code>updatedReplicas</code><br/>
<em>
int32
</em>
</td>
<td>
<p>updatedReplicas defines the total number of non-terminated pods targeted by this shard
that have the desired spec.</p>
</td>
</tr>
<tr>
<td>
<code>availableReplicas</code><br/>
<em>
int32
</em>
</td>
<td>
<p>availableReplicas defines the total number of available pods (ready for at least minReadySeconds)
targeted by this shard.</p>
</td>
</tr>
<tr>
<td>
<code>unavailableReplicas</code><br/>
<em>
int32
</em>
</td>
<td>
<p>unavailableReplicas defines the Total number of unavailable pods targeted by this shard.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ShardingStrategy">ShardingStrategy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
<p>ShardingStrategy defines the sharding strategy for Prometheus.</p>
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
<code>mode</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ShardingStrategyMode">
ShardingStrategyMode
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>mode defines the sharding mode. Can be &lsquo;Address&rsquo; or &lsquo;Topology&rsquo;.</p>
<p>&lsquo;Address&rsquo; is the default mode and distributes targets across shards
based on a hash of the target address.</p>
<p>&lsquo;Topology&rsquo; enables zone-aware sharding where each shard is assigned to a
specific topology zone and only scrapes targets in that zone.
(Alpha) Using the &lsquo;Topology&rsquo; mode requires the <code>PrometheusTopologySharding</code>
feature gate to be enabled.</p>
</td>
</tr>
<tr>
<td>
<code>topology</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TopologyShardingStrategy">
TopologyShardingStrategy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>topology defines the configuration for topology-aware sharding.
This field is only valid when mode is set to &lsquo;Topology&rsquo;.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ShardingStrategyMode">ShardingStrategyMode
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ShardingStrategy">ShardingStrategy</a>)
</p>
<div>
<p>ShardingStrategyMode defines the sharding mode for Prometheus.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;Address&#34;</p></td>
<td><p>AddressShardingStrategyMode is the default sharding mode.
Targets are distributed across shards based on a hash of the target address.</p>
</td>
</tr><tr><td><p>&#34;Topology&#34;</p></td>
<td><p>TopologyShardingStrategyMode enables zone-aware sharding.
Each shard is assigned to a specific topology zone and only scrapes targets in that zone.</p>
<p>(Beta) Using this mode requires the <code>PrometheusTopologySharding</code> feature gate (enabled by default).</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.Sigv4">Sigv4
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.SNSConfig">SNSConfig</a>, <a href="#monitoring.coreos.com/v1beta1.SNSConfig">SNSConfig</a>)
</p>
<div>
<p>Sigv4 defines AWS&rsquo;s Signature Verification 4 signing process to
sign requests.</p>
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
<p>region defines the AWS region. If blank, the region from the default credentials chain used.</p>
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
<p>accessKey defines the AWS API key. If not specified, the environment variable
<code>AWS_ACCESS_KEY_ID</code> is used.</p>
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
<p>secretKey defines the AWS API secret. If not specified, the environment
variable <code>AWS_SECRET_ACCESS_KEY</code> is used.</p>
</td>
</tr>
<tr>
<td>
<code>profile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>profile defines the named AWS profile used to authenticate.</p>
</td>
</tr>
<tr>
<td>
<code>roleArn</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>roleArn defines the named AWS profile used to authenticate.</p>
</td>
</tr>
<tr>
<td>
<code>externalId</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>externalId defines the external ID used when assuming an AWS role. Can only be used with roleArn.
It requires Prometheus &gt;= v3.11.0 or Alertmanager &gt;= v0.34.0. Currently not supported by Thanos.</p>
</td>
</tr>
<tr>
<td>
<code>useFIPSSTSEndpoint</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>useFIPSSTSEndpoint defines the FIPS mode for the AWS STS endpoint.
It requires Prometheus &gt;= v2.54.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.StatefulSetUpdateStrategy">StatefulSetUpdateStrategy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>StatefulSetUpdateStrategy indicates the strategy used when updating the
StatefulSet. It includes any additional parameters necessary to perform the
update for the indicated strategy.</p>
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
<a href="#monitoring.coreos.com/v1.StatefulSetUpdateStrategyType">
StatefulSetUpdateStrategyType
</a>
</em>
</td>
<td>
<p>type indicates the type of the StatefulSetUpdateStrategy.</p>
<p>Default is RollingUpdate.</p>
</td>
</tr>
<tr>
<td>
<code>rollingUpdate</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RollingUpdateStatefulSetStrategy">
RollingUpdateStatefulSetStrategy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>rollingUpdate is used to communicate parameters when type is RollingUpdate.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.StatefulSetUpdateStrategyType">StatefulSetUpdateStrategyType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.StatefulSetUpdateStrategy">StatefulSetUpdateStrategy</a>)
</p>
<div>
<p>StatefulSetUpdateStrategyType is a string enumeration type that enumerates
all possible update strategies for the StatefulSet pods.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;OnDelete&#34;</p></td>
<td><p>OnDeleteStatefulSetStrategyType triggers the legacy behavior. Version
tracking and ordered rolling restarts are disabled. Pods are recreated
from the StatefulSetSpec when they are manually deleted. When a scale
operation is performed with this strategy, new Pods will be created from
the the specification version indicated by the StatefulSet&rsquo;s
currentRevision.</p>
</td>
</tr><tr><td><p>&#34;RollingUpdate&#34;</p></td>
<td><p>RollingUpdateStatefulSetStrategyType indicates that update will be
applied to all Pods in the StatefulSet with respect to the StatefulSet
ordering constraints. When a scale operation is performed with this
strategy, new Pods will be created from the specification version indicated
by the StatefulSet&rsquo;s updateRevision.</p>
</td>
</tr></tbody>
</table>
