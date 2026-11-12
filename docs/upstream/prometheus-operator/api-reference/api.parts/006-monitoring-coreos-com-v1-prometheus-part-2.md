<!-- Part 6 of 55 of api-reference/api.md (split because the page is big). -->

* Scrape objects with a labelNameLengthLimit value less than or equal to enforcedLabelNameLengthLimit keep their specific value.
* Scrape objects with a labelNameLengthLimit value greater than enforcedLabelNameLengthLimit are set to enforcedLabelNameLengthLimit.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedLabelValueLengthLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedLabelValueLengthLimit when not null defines a global limit on the length
of labels value per sample. The value overrides any <code>spec.labelValueLengthLimit</code> set by
ServiceMonitor, PodMonitor, Probe objects unless <code>spec.labelValueLengthLimit</code> is
greater than zero and less than <code>spec.enforcedLabelValueLengthLimit</code>.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
<p>When both <code>enforcedLabelValueLengthLimit</code> and <code>labelValueLengthLimit</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined labelValueLengthLimit value will inherit the global labelValueLengthLimit value (Prometheus &gt;= 2.45.0) or the enforcedLabelValueLengthLimit value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedLabelValueLengthLimit</code> is greater than the <code>labelValueLengthLimit</code>, the <code>labelValueLengthLimit</code> will be set to <code>enforcedLabelValueLengthLimit</code>.
* Scrape objects with a labelValueLengthLimit value less than or equal to enforcedLabelValueLengthLimit keep their specific value.
* Scrape objects with a labelValueLengthLimit value greater than enforcedLabelValueLengthLimit are set to enforcedLabelValueLengthLimit.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedKeepDroppedTargets</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedKeepDroppedTargets when defined specifies a global limit on the number of targets
dropped by relabeling that will be kept in memory. The value overrides
any <code>spec.keepDroppedTargets</code> set by
ServiceMonitor, PodMonitor, Probe objects unless <code>spec.keepDroppedTargets</code> is
greater than zero and less than <code>spec.enforcedKeepDroppedTargets</code>.</p>
<p>It requires Prometheus &gt;= v2.47.0.</p>
<p>When both <code>enforcedKeepDroppedTargets</code> and <code>keepDroppedTargets</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined keepDroppedTargets value will inherit the global keepDroppedTargets value (Prometheus &gt;= 2.45.0) or the enforcedKeepDroppedTargets value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedKeepDroppedTargets</code> is greater than the <code>keepDroppedTargets</code>, the <code>keepDroppedTargets</code> will be set to <code>enforcedKeepDroppedTargets</code>.
* Scrape objects with a keepDroppedTargets value less than or equal to enforcedKeepDroppedTargets keep their specific value.
* Scrape objects with a keepDroppedTargets value greater than enforcedKeepDroppedTargets are set to enforcedKeepDroppedTargets.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedBodySizeLimit</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ByteSize">
ByteSize
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedBodySizeLimit when defined specifies a global limit on the size
of uncompressed response body that will be accepted by Prometheus.
Targets responding with a body larger than this many bytes will cause
the scrape to fail.</p>
<p>It requires Prometheus &gt;= v2.28.0.</p>
<p>When both <code>enforcedBodySizeLimit</code> and <code>bodySizeLimit</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined bodySizeLimit value will inherit the global bodySizeLimit value (Prometheus &gt;= 2.45.0) or the enforcedBodySizeLimit value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedBodySizeLimit</code> is greater than the <code>bodySizeLimit</code>, the <code>bodySizeLimit</code> will be set to <code>enforcedBodySizeLimit</code>.
* Scrape objects with a bodySizeLimit value less than or equal to enforcedBodySizeLimit keep their specific value.
* Scrape objects with a bodySizeLimit value greater than enforcedBodySizeLimit are set to enforcedBodySizeLimit.</p>
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
<p>It requires Prometheus &gt;= v2.55.0.</p>
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
<p>nameEscapingScheme defines the character escaping scheme that will be requested when scraping
for metric and label names that do not conform to the legacy Prometheus
character set.</p>
<p>It requires Prometheus &gt;= v3.4.0.</p>
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
<p>convertClassicHistogramsToNHCB defines whether to convert all scraped classic histograms into a native
histogram with custom buckets.</p>
<p>It requires Prometheus &gt;= v3.4.0.</p>
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
<p>scrapeClassicHistograms defines whether to scrape a classic histogram that is also exposed as a native histogram.</p>
<p>Notice: <code>scrapeClassicHistograms</code> corresponds to the <code>always_scrape_classic_histograms</code> field in the Prometheus configuration.</p>
<p>It requires Prometheus &gt;= v3.5.0.</p>
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
<p>It requires Prometheus &gt;= v2.32.0.</p>
</td>
</tr>
<tr>
<td>
<code>minReadySeconds</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>minReadySeconds defines the minimum number of seconds for which a newly created Pod should be ready
without any of its container crashing for it to be considered available.</p>
<p>If unset, pods will be considered available as soon as they are ready.</p>
</td>
</tr>
<tr>
<td>
<code>hostAliases</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.HostAlias">
[]HostAlias
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>hostAliases defines the optional list of hosts and IPs that will be injected into the Pod&rsquo;s
hosts file if specified.</p>
</td>
</tr>
<tr>
<td>
<code>additionalArgs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Argument">
[]Argument
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>additionalArgs allows setting additional arguments for the &lsquo;prometheus&rsquo; container.</p>
<p>It is intended for e.g. activating hidden flags which are not supported by
the dedicated configuration options yet. The arguments are passed as-is to the
Prometheus container which may cause issues if they are invalid or not supported
by the given Prometheus version.</p>
<p>In case of an argument conflict (e.g. an argument which is already set by the
operator itself) or when providing an invalid argument, the reconciliation will
fail and an error will be logged.</p>
</td>
</tr>
<tr>
<td>
<code>walCompression</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>walCompression defines the compression of the write-ahead log (WAL) using Snappy.</p>
<p>WAL compression is enabled by default for Prometheus &gt;= 2.20.0</p>
<p>Requires Prometheus v2.11.0 and above.</p>
</td>
</tr>
<tr>
<td>
<code>excludedFromEnforcement</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ObjectReference">
[]ObjectReference
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>excludedFromEnforcement defines the list of references to PodMonitor, ServiceMonitor, Probe and PrometheusRule objects
to be excluded from enforcing a namespace label of origin.</p>
<p>It is only applicable if <code>spec.enforcedNamespaceLabel</code> set to true.</p>
</td>
</tr>
<tr>
<td>
<code>hostNetwork</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>hostNetwork defines the host&rsquo;s network namespace if true.</p>
<p>Make sure to understand the security implications if you want to enable
it (<a href="https://kubernetes.io/docs/concepts/configuration/overview/">https://kubernetes.io/docs/concepts/configuration/overview/</a> ).</p>
<p>When hostNetwork is enabled, this will set the DNS policy to
<code>ClusterFirstWithHostNet</code> automatically (unless <code>.spec.DNSPolicy</code> is set
to a different value).</p>
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
<p>podTargetLabels are appended to the <code>spec.podTargetLabels</code> field of all
PodMonitor and ServiceMonitor objects.</p>
</td>
</tr>
<tr>
<td>
<code>tracingConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TracingConfig">
TracingConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tracingConfig defines tracing in Prometheus.</p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
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
<p>bodySizeLimit defines per-scrape on response body size.
Only valid in Prometheus versions 2.45.0 and newer.</p>
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedBodySizeLimit.</p>
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
<p>sampleLimit defines per-scrape limit on number of scraped samples that will be accepted.
Only valid in Prometheus versions 2.45.0 and newer.</p>
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedSampleLimit.</p>
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
<p>targetLimit defines a limit on the number of scraped targets that will be accepted.
Only valid in Prometheus versions 2.45.0 and newer.</p>
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedTargetLimit.</p>
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
<p>labelLimit defines per-scrape limit on number of labels that will be accepted for a sample.
Only valid in Prometheus versions 2.45.0 and newer.</p>
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedLabelLimit.</p>
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
Only valid in Prometheus versions 2.45.0 and newer.</p>
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedLabelNameLengthLimit.</p>
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
Only valid in Prometheus versions 2.45.0 and newer.</p>
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedLabelValueLengthLimit.</p>
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
<p>Note that the global limit only applies to scrape objects that don&rsquo;t specify an explicit limit value.
If you want to enforce a maximum limit for all scrape objects, refer to enforcedKeepDroppedTargets.</p>
</td>
</tr>
<tr>
<td>
<code>reloadStrategy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ReloadStrategyType">
ReloadStrategyType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>reloadStrategy defines the strategy used to reload the Prometheus configuration.
If not specified, the configuration is reloaded using the /-/reload HTTP endpoint.</p>
</td>
</tr>
<tr>
<td>
<code>maximumStartupDurationSeconds</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maximumStartupDurationSeconds defines the maximum time that the <code>prometheus</code> container&rsquo;s startup probe will wait before being considered failed. The startup probe will return success after the WAL replay is complete.
If set, the value should be greater than 60 (seconds). Otherwise it will be equal to 900 seconds (15 minutes).</p>
</td>
</tr>
<tr>
<td>
<code>scrapeClasses</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ScrapeClass">
[]ScrapeClass
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeClasses defines the list of scrape classes to expose to scraping objects such as
PodMonitors, ServiceMonitors, Probes and ScrapeConfigs.</p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
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
<p>serviceDiscoveryRole defines the service discovery role used to discover targets from
<code>ServiceMonitor</code> objects and Alertmanager endpoints.</p>
<p>If set, the value should be either &ldquo;Endpoints&rdquo; or &ldquo;EndpointSlice&rdquo;.
If unset, the operator assumes the &ldquo;Endpoints&rdquo; role.</p>
</td>
</tr>
<tr>
<td>
<code>tsdb</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TSDBSpec">
TSDBSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tsdb defines the runtime reloadable configuration of the timeseries database(TSDB).
It requires Prometheus &gt;= v2.39.0 or PrometheusAgent &gt;= v2.54.0.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeFailureLogFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeFailureLogFile defines the file to which scrape failures are logged.
Reloading the configuration will reopen the file.</p>
<p>If the filename has an empty path, e.g. &lsquo;file.log&rsquo;, The Prometheus Pods
will mount the file into an emptyDir volume at <code>/var/log/prometheus</code>.
If a full path is provided, e.g. &lsquo;/var/log/prometheus/file.log&rsquo;, you
must mount a volume in the specified directory and it must be writable.
It requires Prometheus &gt;= v2.55.0.</p>
</td>
</tr>
<tr>
<td>
<code>serviceName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceName defines the name of the service name used by the underlying StatefulSet(s) as the governing service.
If defined, the Service  must be created before the Prometheus/PrometheusAgent resource in the same namespace and it must define a selector that matches the pod labels.
If empty, the operator will create and manage a headless service named <code>prometheus-operated</code> for Prometheus resources,
or <code>prometheus-agent-operated</code> for PrometheusAgent resources.
When deploying multiple Prometheus/PrometheusAgent resources in the same namespace, it is recommended to specify a different value for each.
See <a href="https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-id">https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-id</a> for more details.</p>
</td>
</tr>
<tr>
<td>
<code>runtime</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RuntimeConfig">
RuntimeConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>runtime defines the values for the Prometheus process behavior</p>
</td>
</tr>
<tr>
<td>
<code>terminationGracePeriodSeconds</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>terminationGracePeriodSeconds defines the optional duration in seconds the pod needs to terminate gracefully.
Value must be non-negative integer. The value zero indicates stop immediately via
the kill signal (no opportunity to shut down) which may lead to data corruption.</p>
<p>Defaults to 600 seconds.</p>
</td>
</tr>
<tr>
<td>
<code>hostUsers</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>hostUsers supports the user space in Kubernetes.</p>
<p>More info: <a href="https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/">https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/</a></p>
<p>The feature requires at least Kubernetes 1.28 with the <code>UserNamespacesSupport</code> feature gate enabled.
Starting Kubernetes 1.33, the feature is enabled by default.</p>
</td>
</tr>
<tr>
<td>
<code>baseImage</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>baseImage is deprecated: use &lsquo;spec.image&rsquo; instead.</p>
</td>
</tr>
<tr>
<td>
<code>tag</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tag is deprecated: use &lsquo;spec.image&rsquo; instead. The image&rsquo;s tag can be specified as part of the image name.</p>
</td>
</tr>
<tr>
<td>
<code>sha</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>sha is deprecated: use &lsquo;spec.image&rsquo; instead. The image&rsquo;s digest can be specified as part of the image name.</p>
</td>
</tr>
<tr>
<td>
<code>retention</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>retention defines how long to retain the Prometheus data.</p>
<p>Default: &ldquo;24h&rdquo; if <code>spec.retention</code>, <code>spec.retentionSize</code> and
<code>spec.retentionPercentage</code> are empty.</p>
</td>
</tr>
<tr>
<td>
<code>retentionSize</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ByteSize">
ByteSize
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>retentionSize defines the maximum number of bytes used by the Prometheus data.</p>
</td>
</tr>
<tr>
<td>
<code>retentionPercentage</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity">
k8s.io/apimachinery/pkg/api/resource.Quantity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>retentionPercentage defines the maximum percentage of the data volume&rsquo;s
capacity used by the Prometheus data.</p>
<p>The value is a number between 0 and 100. If set to 0, percentage-based
retention is disabled.</p>
<p>It requires Prometheus &gt;= v3.11.0 and is ignored by older versions.</p>
</td>
</tr>
<tr>
<td>
<code>shardRetentionPolicy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ShardRetentionPolicy">
ShardRetentionPolicy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>shardRetentionPolicy defines the retention policy for the Prometheus shards.</p>
<p>(Beta) Using this mode requires the <code>PrometheusShardRetentionPolicy</code> feature gate (enabled by default).</p>
</td>
</tr>
<tr>
<td>
<code>disableCompaction</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>disableCompaction when true, the Prometheus compaction is disabled.</p>
<p>When <code>spec.thanos.objectStorageConfig</code> or <code>spec.thanos.objectStorageConfigFile</code> are defined, the operator&rsquo;s
default handling depends on the Prometheus and Thanos sidecar versions:
- With Prometheus &lt; v3.9.0 or a Thanos sidecar &lt; v0.42.0, block compaction is disabled to avoid race
conditions during block uploads (as the Thanos documentation recommends).
- With Prometheus &gt;= v3.9.0 and a Thanos sidecar &gt;= v0.42.0, local compaction is kept enabled and coordinated
with the sidecar through the shipper meta file (<code>--storage.tsdb.delay-compact-file.path</code>), so blocks are only
compacted after they have been uploaded.
Setting this field to true always disables local compaction regardless of the versions.</p>
</td>
</tr>
<tr>
<td>
<code>rules</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Rules">
Rules
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>rules defines the configuration of the Prometheus rules&rsquo; engine.</p>
</td>
</tr>
<tr>
<td>
<code>prometheusRulesExcludedFromEnforce</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PrometheusRuleExcludeConfig">
[]PrometheusRuleExcludeConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>prometheusRulesExcludedFromEnforce defines the list of PrometheusRule objects to which the namespace label
enforcement doesn&rsquo;t apply.
This is only relevant when <code>spec.enforcedNamespaceLabel</code> is set to true.
Deprecated: use <code>spec.excludedFromEnforcement</code> instead.</p>
</td>
</tr>
<tr>
<td>
<code>ruleSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ruleSelector defines the prometheusRule objects to be selected for rule evaluation. An empty
label selector matches all objects. A null label selector matches no
objects.</p>
</td>
</tr>
<tr>
<td>
<code>ruleNamespaceSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ruleNamespaceSelector defines the namespaces to match for PrometheusRule discovery. An empty label selector
matches all namespaces. A null label selector matches the current
namespace only.</p>
</td>
</tr>
<tr>
<td>
<code>query</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.QuerySpec">
QuerySpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>query defines the configuration of the Prometheus query service.</p>
</td>
</tr>
<tr>
<td>
<code>alerting</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertingSpec">
AlertingSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alerting defines the settings related to Alertmanager.</p>
</td>
</tr>
<tr>
<td>
<code>additionalAlertRelabelConfigs</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>additionalAlertRelabelConfigs defines a key of a Secret containing
additional Prometheus alert relabel configurations. The alert relabel
configurations are appended to the configuration generated by the
Prometheus Operator. They must be formatted according to the official
Prometheus documentation:</p>
<p><a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs</a></p>
<p>The user is responsible for making sure that the configurations are valid</p>
<p>Note that using this feature may expose the possibility to break
upgrades of Prometheus. It is advised to review Prometheus release notes
to ensure that no incompatible alert relabel configs are going to break
Prometheus after the upgrade.</p>
</td>
</tr>
<tr>
<td>
<code>additionalAlertManagerConfigs</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>additionalAlertManagerConfigs defines a key of a Secret containing
additional Prometheus Alertmanager configurations. The Alertmanager
configurations are appended to the configuration generated by the
Prometheus Operator. They must be formatted according to the official
Prometheus documentation:</p>
<p><a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config</a></p>
<p>The user is responsible for making sure that the configurations are valid</p>
<p>Note that using this feature may expose the possibility to break
upgrades of Prometheus. It is advised to review Prometheus release notes
to ensure that no incompatible AlertManager configs are going to break
Prometheus after the upgrade.</p>
</td>
</tr>
<tr>
<td>
<code>remoteRead</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RemoteReadSpec">
[]RemoteReadSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>remoteRead defines the list of remote read configurations.</p>
</td>
</tr>
<tr>
<td>
<code>thanos</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ThanosSpec">
ThanosSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>thanos defines the configuration of the optional Thanos sidecar.</p>
</td>
</tr>
<tr>
<td>
<code>queryLogFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>queryLogFile specifies where the file to which PromQL queries are logged.</p>
<p>If the filename has an empty path, e.g. &lsquo;query.log&rsquo;, The Prometheus Pods
will mount the file into an emptyDir volume at <code>/var/log/prometheus</code>.
If a full path is provided, e.g. &lsquo;/var/log/prometheus/query.log&rsquo;, you
must mount a volume in the specified directory and it must be writable.
This is because the prometheus container runs with a read-only root
filesystem for security reasons.
Alternatively, the location can be set to a standard I/O stream, e.g.
<code>/dev/stdout</code>, to log query information to the default Prometheus log
stream.</p>
</td>
</tr>
<tr>
<td>
<code>allowOverlappingBlocks</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>allowOverlappingBlocks enables vertical compaction and vertical query
merge in Prometheus.</p>
<p>Deprecated: this flag has no effect for Prometheus &gt;= 2.39.0 where overlapping blocks are enabled by default.</p>
</td>
</tr>
<tr>
<td>
<code>exemplars</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Exemplars">
Exemplars
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>exemplars related settings that are runtime reloadable.
It requires to enable the <code>exemplar-storage</code> feature flag to be effective.</p>
</td>
</tr>
<tr>
<td>
<code>evaluationInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>evaluationInterval defines the interval between rule evaluations.
Default: &ldquo;30s&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>ruleQueryOffset</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ruleQueryOffset defines the offset the rule evaluation timestamp of this particular group by the specified duration into the past.
It requires Prometheus &gt;= v2.53.0.</p>
</td>
</tr>
<tr>
<td>
<code>enableAdminAPI</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableAdminAPI defines access to the Prometheus web admin API.</p>
<p>WARNING: Enabling the admin APIs enables mutating endpoints, to delete data,
shutdown Prometheus, and more. Enabling this should be done with care and the
user is advised to add additional authentication authorization via a proxy to
ensure only clients authorized to perform these actions can do so.</p>
<p>For more information:
<a href="https://prometheus.io/docs/prometheus/latest/querying/api/#tsdb-admin-apis">https://prometheus.io/docs/prometheus/latest/querying/api/#tsdb-admin-apis</a></p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PrometheusStatus">
PrometheusStatus
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>status defines the most recent observed status of the Prometheus cluster. Read-only.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
</td>
</tr>
</tbody>
</table>
