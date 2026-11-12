<!-- Part 23 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Prometheus">Prometheus</a>)
</p>
<div>
<p>PrometheusSpec is a specification of the desired behavior of the Prometheus cluster. More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
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
<code>podMetadata</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.EmbeddedObjectMetadata">
EmbeddedObjectMetadata
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>podMetadata defines labels and annotations which are propagated to the Prometheus pods.</p>
<p>The following items are reserved and cannot be overridden:
* &ldquo;prometheus&rdquo; label, set to the name of the Prometheus object.
* &ldquo;app.kubernetes.io/instance&rdquo; label, set to the name of the Prometheus object.
* &ldquo;app.kubernetes.io/managed-by&rdquo; label, set to &ldquo;prometheus-operator&rdquo;.
* &ldquo;app.kubernetes.io/name&rdquo; label, set to &ldquo;prometheus&rdquo;.
* &ldquo;app.kubernetes.io/version&rdquo; label, set to the Prometheus version.
* &ldquo;operator.prometheus.io/name&rdquo; label, set to the name of the Prometheus object.
* &ldquo;operator.prometheus.io/shard&rdquo; label, set to the shard number of the Prometheus object.
* &ldquo;kubectl.kubernetes.io/default-container&rdquo; annotation, set to &ldquo;prometheus&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>serviceMonitorSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceMonitorSelector defines the serviceMonitors to be selected for target discovery. An empty label
selector matches all objects. A null label selector matches no objects.</p>
<p>If <code>spec.serviceMonitorSelector</code>, <code>spec.podMonitorSelector</code>, <code>spec.probeSelector</code>
and <code>spec.scrapeConfigSelector</code> are null, the Prometheus configuration is unmanaged.
The Prometheus operator will ensure that the Prometheus configuration&rsquo;s
Secret exists, but it is the responsibility of the user to provide the raw
gzipped Prometheus configuration under the <code>prometheus.yaml.gz</code> key.
This behavior is <em>deprecated</em> and will be removed in the next major version
of the custom resource definition. It is recommended to use
<code>spec.additionalScrapeConfigs</code> instead.</p>
</td>
</tr>
<tr>
<td>
<code>serviceMonitorNamespaceSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceMonitorNamespaceSelector defines the namespaces to match for ServicedMonitors discovery. An empty label selector
matches all namespaces. A null label selector (default value) matches the current
namespace only.</p>
</td>
</tr>
<tr>
<td>
<code>podMonitorSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>podMonitorSelector defines the podMonitors to be selected for target discovery. An empty label selector
matches all objects. A null label selector matches no objects.</p>
<p>If <code>spec.serviceMonitorSelector</code>, <code>spec.podMonitorSelector</code>, <code>spec.probeSelector</code>
and <code>spec.scrapeConfigSelector</code> are null, the Prometheus configuration is unmanaged.
The Prometheus operator will ensure that the Prometheus configuration&rsquo;s
Secret exists, but it is the responsibility of the user to provide the raw
gzipped Prometheus configuration under the <code>prometheus.yaml.gz</code> key.
This behavior is <em>deprecated</em> and will be removed in the next major version
of the custom resource definition. It is recommended to use
<code>spec.additionalScrapeConfigs</code> instead.</p>
</td>
</tr>
<tr>
<td>
<code>podMonitorNamespaceSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>podMonitorNamespaceSelector defines the namespaces to match for PodMonitors discovery. An empty label selector
matches all namespaces. A null label selector (default value) matches the current
namespace only.</p>
</td>
</tr>
<tr>
<td>
<code>probeSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>probeSelector defines the probes to be selected for target discovery. An empty label selector
matches all objects. A null label selector matches no objects.</p>
<p>If <code>spec.serviceMonitorSelector</code>, <code>spec.podMonitorSelector</code>, <code>spec.probeSelector</code>
and <code>spec.scrapeConfigSelector</code> are null, the Prometheus configuration is unmanaged.
The Prometheus operator will ensure that the Prometheus configuration&rsquo;s
Secret exists, but it is the responsibility of the user to provide the raw
gzipped Prometheus configuration under the <code>prometheus.yaml.gz</code> key.
This behavior is <em>deprecated</em> and will be removed in the next major version
of the custom resource definition. It is recommended to use
<code>spec.additionalScrapeConfigs</code> instead.</p>
</td>
</tr>
<tr>
<td>
<code>probeNamespaceSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>probeNamespaceSelector defines the namespaces to match for Probe discovery. An empty label
selector matches all namespaces. A null label selector matches the
current namespace only.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeConfigSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeConfigSelector defines the scrapeConfigs to be selected for target discovery. An empty label
selector matches all objects. A null label selector matches no objects.</p>
<p>If <code>spec.serviceMonitorSelector</code>, <code>spec.podMonitorSelector</code>, <code>spec.probeSelector</code>
and <code>spec.scrapeConfigSelector</code> are null, the Prometheus configuration is unmanaged.
The Prometheus operator will ensure that the Prometheus configuration&rsquo;s
Secret exists, but it is the responsibility of the user to provide the raw
gzipped Prometheus configuration under the <code>prometheus.yaml.gz</code> key.
This behavior is <em>deprecated</em> and will be removed in the next major version
of the custom resource definition. It is recommended to use
<code>spec.additionalScrapeConfigs</code> instead.</p>
<p>Note that the ScrapeConfig custom resource definition is currently at Alpha level
and will be graduated to Beta in a future release.</p>
</td>
</tr>
<tr>
<td>
<code>scrapeConfigNamespaceSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>scrapeConfigNamespaceSelector defines the namespaces to match for ScrapeConfig discovery. An empty label selector
matches all namespaces. A null label selector matches the current
namespace only.</p>
<p>Note that the ScrapeConfig custom resource definition is currently at Alpha level
and will be graduated to Beta in a future release.</p>
</td>
</tr>
<tr>
<td>
<code>version</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>version of Prometheus being deployed. The operator uses this information
to generate the Prometheus StatefulSet + configuration files.</p>
<p>If not specified, the operator assumes the latest upstream version of
Prometheus available at the time when the version of the operator was
released.</p>
</td>
</tr>
<tr>
<td>
<code>paused</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>paused defines when a Prometheus deployment is paused, no actions except for deletion
will be performed on the underlying objects.</p>
</td>
</tr>
<tr>
<td>
<code>image</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>image defines the container image name for Prometheus. If specified, it takes precedence
over the <code>spec.baseImage</code>, <code>spec.tag</code> and <code>spec.sha</code> fields.</p>
<p>Specifying <code>spec.version</code> is still necessary to ensure the Prometheus
Operator knows which version of Prometheus is being configured.</p>
<p>If neither <code>spec.image</code> nor <code>spec.baseImage</code> are defined, the operator
will use the latest upstream version of Prometheus available at the time
when the operator was released.</p>
</td>
</tr>
<tr>
<td>
<code>imagePullPolicy</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#pullpolicy-v1-core">
Kubernetes core/v1.PullPolicy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>imagePullPolicy defines the image pull policy for the &lsquo;prometheus&rsquo;, &lsquo;init-config-reloader&rsquo; and &lsquo;config-reloader&rsquo; containers.
See <a href="https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy">https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy</a> for more details.</p>
</td>
</tr>
<tr>
<td>
<code>imagePullSecrets</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#localobjectreference-v1-core">
[]Kubernetes core/v1.LocalObjectReference
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>imagePullSecrets defines an optional list of references to Secrets in the same namespace
to use for pulling images from registries.
See <a href="http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod">http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod</a></p>
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
<em>(Optional)</em>
<p>replicas defines the number of replicas of each shard to deploy for a Prometheus deployment.
<code>spec.replicas</code> multiplied by <code>spec.shards</code> is the total number of Pods
created.</p>
<p>Default: 1</p>
</td>
</tr>
<tr>
<td>
<code>shards</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>shards defines the number of shards to distribute the scraped targets onto.</p>
<p><code>spec.replicas</code> multiplied by <code>spec.shards</code> is the total number of Pods
being created.</p>
<p>When not defined, the operator assumes only one shard.</p>
<p>Note that scaling down shards will not reshard data onto the remaining
instances, it must be manually moved. Increasing shards will not reshard
data either but it will continue to be available from the same
instances. To query globally, use either
* Thanos sidecar + querier for query federation and Thanos Ruler for rules.
* Remote-write to send metrics to a central location.</p>
<p>By default, the sharding of targets is performed on:
* The <code>__address__</code> target&rsquo;s metadata label for PodMonitor,
ServiceMonitor and ScrapeConfig resources.
* The <code>__param_target__</code> label for Probe resources.</p>
<p>Users can define their own sharding implementation by setting the
<code>__tmp_hash</code> label during the target discovery with relabeling
configuration (either in the monitoring resources or via scrape class).</p>
<p>You can also disable sharding on a specific target by setting the
<code>__tmp_disable_sharding</code> label with relabeling configuration. When
the label value isn&rsquo;t empty, all Prometheus shards will scrape the target.</p>
<p>Default: 1</p>
</td>
</tr>
<tr>
<td>
<code>shardingStrategy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ShardingStrategy">
ShardingStrategy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>shardingStrategy defines the sharding strategy for distributing scraped targets across Prometheus shards.</p>
<p>When not defined, the operator defaults to the &lsquo;Address&rsquo; mode which distributes
targets based on a hash of the target address.</p>
</td>
</tr>
<tr>
<td>
<code>replicaExternalLabelName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>replicaExternalLabelName defines the name of Prometheus external label used to denote the replica name.
The external label will <em>not</em> be added when the field is set to the
empty string (<code>&quot;&quot;</code>).</p>
<p>Default: &ldquo;prometheus_replica&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>prometheusExternalLabelName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>prometheusExternalLabelName defines the name of Prometheus external label used to denote the Prometheus instance
name. The external label will <em>not</em> be added when the field is set to
the empty string (<code>&quot;&quot;</code>).</p>
<p>Default: &ldquo;prometheus&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>logLevel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>logLevel for Prometheus and the config-reloader sidecar.</p>
</td>
</tr>
<tr>
<td>
<code>logFormat</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>logFormat for Log level for Prometheus and the config-reloader sidecar.</p>
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
<p>scrapeInterval defines interval between consecutive scrapes.</p>
<p>Default: &ldquo;30s&rdquo;</p>
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
<p><code>PrometheusText1.0.0</code> requires Prometheus &gt;= v3.0.0.</p>
</td>
</tr>
<tr>
<td>
<code>externalLabels</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>externalLabels defines the labels to add to any time series or alerts when communicating with
external systems (federation, remote storage, Alertmanager).
Labels defined by <code>spec.replicaExternalLabelName</code> and
<code>spec.prometheusExternalLabelName</code> take precedence over this list.</p>
</td>
</tr>
<tr>
<td>
<code>enableRemoteWriteReceiver</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableRemoteWriteReceiver defines the Prometheus to be used as a receiver for the Prometheus remote
write protocol.</p>
<p>WARNING: This is not considered an efficient way of ingesting samples.
Use it with caution for specific low-volume use cases.
It is not suitable for replacing the ingestion via scraping and turning
Prometheus into a push-based metrics collection system.
For more information see <a href="https://prometheus.io/docs/prometheus/latest/querying/api/#remote-write-receiver">https://prometheus.io/docs/prometheus/latest/querying/api/#remote-write-receiver</a></p>
<p>It requires Prometheus &gt;= v2.33.0.</p>
</td>
</tr>
<tr>
<td>
<code>enableOTLPReceiver</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableOTLPReceiver defines the Prometheus to be used as a receiver for the OTLP Metrics protocol.</p>
<p>Note that the OTLP receiver endpoint is automatically enabled if <code>.spec.otlpConfig</code> is defined.</p>
<p>It requires Prometheus &gt;= v2.47.0.</p>
</td>
</tr>
<tr>
<td>
<code>remoteWriteReceiverMessageVersions</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RemoteWriteMessageVersion">
[]RemoteWriteMessageVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>remoteWriteReceiverMessageVersions list of the protobuf message versions to accept when receiving the
remote writes.</p>
<p>It requires Prometheus &gt;= v2.54.0.</p>
</td>
</tr>
<tr>
<td>
<code>enableFeatures</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.EnableFeature">
[]EnableFeature
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableFeatures enables access to Prometheus feature flags. By default, no features are enabled.</p>
<p>Enabling features which are disabled by default is entirely outside the
scope of what the maintainers will support and by doing so, you accept
that this behaviour may break at any time without notice.</p>
<p>For more information see <a href="https://prometheus.io/docs/prometheus/latest/feature_flags/">https://prometheus.io/docs/prometheus/latest/feature_flags/</a></p>
</td>
</tr>
<tr>
<td>
<code>externalUrl</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>externalUrl defines the external URL under which the Prometheus service is externally
available. This is necessary to generate correct URLs (for instance if
Prometheus is accessible behind an Ingress resource).</p>
</td>
</tr>
<tr>
<td>
<code>routePrefix</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>routePrefix defines the route prefix Prometheus registers HTTP handlers for.</p>
<p>This is useful when using <code>spec.externalURL</code>, and a proxy is rewriting
HTTP routes of a request, and the actual ExternalURL is still true, but
the server serves requests under a different route prefix. For example
for use with <code>kubectl proxy</code>.</p>
</td>
</tr>
<tr>
<td>
<code>storage</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.StorageSpec">
StorageSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>storage defines the storage used by Prometheus.</p>
</td>
</tr>
<tr>
<td>
<code>volumes</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#volume-v1-core">
[]Kubernetes core/v1.Volume
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>volumes allows the configuration of additional volumes on the output
StatefulSet definition. Volumes specified will be appended to other
volumes that are generated as a result of StorageSpec objects.</p>
</td>
</tr>
<tr>
<td>
<code>volumeMounts</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#volumemount-v1-core">
[]Kubernetes core/v1.VolumeMount
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>volumeMounts allows the configuration of additional VolumeMounts.</p>
<p>VolumeMounts will be appended to other VolumeMounts in the &lsquo;prometheus&rsquo;
container, that are generated as a result of StorageSpec objects.</p>
</td>
</tr>
<tr>
<td>
<code>persistentVolumeClaimRetentionPolicy</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#statefulsetpersistentvolumeclaimretentionpolicy-v1-apps">
Kubernetes apps/v1.StatefulSetPersistentVolumeClaimRetentionPolicy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>persistentVolumeClaimRetentionPolicy defines the field controls if and how PVCs are deleted during the lifecycle of a StatefulSet.
The default behavior is all PVCs are retained.
This is an alpha field from kubernetes 1.23 until 1.26 and a beta field from 1.26.
It requires enabling the StatefulSetAutoDeletePVC feature gate.</p>
</td>
</tr>
<tr>
<td>
<code>web</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PrometheusWebSpec">
PrometheusWebSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>web defines the configuration of the Prometheus web server.</p>
</td>
</tr>
<tr>
<td>
<code>resources</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core">
Kubernetes core/v1.ResourceRequirements
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>resources defines the resources requests and limits of the &lsquo;prometheus&rsquo; container.</p>
</td>
</tr>
<tr>
<td>
<code>nodeSelector</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>nodeSelector defines on which Nodes the Pods are scheduled.</p>
</td>
</tr>
<tr>
<td>
<code>schedulerName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>schedulerName defines the scheduler to use for Pod scheduling. If not specified, the default scheduler is used.</p>
</td>
</tr>
<tr>
<td>
<code>serviceAccountName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceAccountName is the name of the ServiceAccount to use to run the
Prometheus Pods.</p>
</td>
</tr>
<tr>
<td>
<code>automountServiceAccountToken</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>automountServiceAccountToken defines whether a service account token should be automatically mounted in the pod.
If the field isn&rsquo;t set, the operator mounts the service account token by default.</p>
<p><strong>Warning:</strong> be aware that by default, Prometheus requires the service account token for Kubernetes service discovery.
It is possible to use strategic merge patch to project the service account token into the &lsquo;prometheus&rsquo; container.</p>
</td>
</tr>
<tr>
<td>
<code>secrets</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>secrets defines a list of Secrets in the same namespace as the Prometheus
object, which shall be mounted into the Prometheus Pods.
Each Secret is added to the StatefulSet definition as a volume named <code>secret-&lt;secret-name&gt;</code>.
The Secrets are mounted into /etc/prometheus/secrets/<secret-name> in the &lsquo;prometheus&rsquo; container.</p>
</td>
</tr>
<tr>
<td>
<code>configMaps</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>configMaps defines a list of ConfigMaps in the same namespace as the Prometheus
object, which shall be mounted into the Prometheus Pods.
Each ConfigMap is added to the StatefulSet definition as a volume named <code>configmap-&lt;configmap-name&gt;</code>.
The ConfigMaps are mounted into /etc/prometheus/configmaps/<configmap-name> in the &lsquo;prometheus&rsquo; container.</p>
</td>
</tr>
<tr>
<td>
<code>affinity</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core">
Kubernetes core/v1.Affinity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>affinity defines the Pods&rsquo; affinity scheduling rules if specified.</p>
</td>
</tr>
<tr>
<td>
<code>tolerations</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core">
[]Kubernetes core/v1.Toleration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tolerations defines the Pods&rsquo; tolerations if specified.</p>
</td>
</tr>
<tr>
<td>
<code>topologySpreadConstraints</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TopologySpreadConstraint">
[]TopologySpreadConstraint
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>topologySpreadConstraints defines the pod&rsquo;s topology spread constraints if specified.</p>
</td>
</tr>
<tr>
<td>
<code>remoteWrite</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.RemoteWriteSpec">
[]RemoteWriteSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>remoteWrite defines the list of remote write configurations.</p>
</td>
</tr>
<tr>
<td>
<code>otlp</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.OTLPConfig">
OTLPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>otlp defines the settings related to the OTLP receiver feature.
It requires Prometheus &gt;= v2.55.0.</p>
</td>
</tr>
<tr>
<td>
<code>securityContext</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#podsecuritycontext-v1-core">
Kubernetes core/v1.PodSecurityContext
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>securityContext holds pod-level security attributes and common container settings.
This defaults to the default PodSecurityContext.</p>
</td>
</tr>
<tr>
<td>
<code>dnsPolicy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.DNSPolicy">
DNSPolicy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>dnsPolicy defines the DNS policy for the pods.</p>
</td>
</tr>
<tr>
<td>
<code>dnsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PodDNSConfig">
PodDNSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>dnsConfig defines the DNS configuration for the pods.</p>
</td>
</tr>
<tr>
<td>
<code>listenLocal</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>listenLocal when true, the Prometheus server listens on the loopback address
instead of the Pod IP&rsquo;s address.</p>
</td>
</tr>
<tr>
<td>
<code>podManagementPolicy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.PodManagementPolicyType">
PodManagementPolicyType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>podManagementPolicy defines the policy for creating/deleting pods when
scaling up and down.</p>
<p>Unlike the default StatefulSet behavior, the default policy is
<code>Parallel</code> to avoid manual intervention in case a pod gets stuck during
a rollout.</p>
<p>Note that updating this value implies the recreation of the StatefulSet
which incurs a service outage.</p>
</td>
</tr>
<tr>
<td>
<code>updateStrategy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.StatefulSetUpdateStrategy">
StatefulSetUpdateStrategy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>updateStrategy indicates the strategy that will be employed to update
Pods in the StatefulSet when a revision is made to statefulset&rsquo;s Pod
Template.</p>
<p>The default strategy is RollingUpdate.</p>
</td>
</tr>
<tr>
<td>
<code>enableServiceLinks</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableServiceLinks defines whether information about services should be injected into pod&rsquo;s environment variables</p>
</td>
</tr>
<tr>
<td>
<code>containers</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#container-v1-core">
[]Kubernetes core/v1.Container
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>containers allows injecting additional containers or modifying operator
generated containers. This can be used to allow adding an authentication
proxy to the Pods or to change the behavior of an operator generated
container. Containers described here modify an operator generated
container if they share the same name and modifications are done via a
strategic merge patch.</p>
<p>The names of containers managed by the operator are:
* <code>prometheus</code>
* <code>config-reloader</code>
* <code>thanos-sidecar</code></p>
<p>Overriding containers which are managed by the operator require careful
testing, especially when upgrading to a new version of the operator.</p>
</td>
</tr>
<tr>
<td>
<code>initContainers</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#container-v1-core">
[]Kubernetes core/v1.Container
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>initContainers allows injecting initContainers to the Pod definition. Those
can be used to e.g. fetch secrets for injection into the Prometheus
configuration from external sources. Any errors during the execution of
an initContainer will lead to a restart of the Pod. More info:
<a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/">https://kubernetes.io/docs/concepts/workloads/pods/init-containers/</a>
InitContainers described here modify an operator generated init
containers if they share the same name and modifications are done via a
strategic merge patch.</p>
<p>The names of init container name managed by the operator are:
* <code>init-config-reloader</code>.</p>
<p>Overriding init containers which are managed by the operator require
careful testing, especially when upgrading to a new version of the
operator.</p>
</td>
</tr>
<tr>
<td>
<code>additionalScrapeConfigs</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>additionalScrapeConfigs allows specifying a key of a Secret containing
additional Prometheus scrape configurations. Scrape configurations
specified are appended to the configurations generated by the Prometheus
Operator. Job configurations specified must have the form as specified
in the official Prometheus documentation:
<a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config</a>.
As scrape configs are appended, the user is responsible to make sure it
is valid. Note that using this feature may expose the possibility to
break upgrades of Prometheus. It is advised to review Prometheus release
notes to ensure that no incompatible scrape configs are going to break
Prometheus after the upgrade.</p>
</td>
</tr>
<tr>
<td>
<code>apiserverConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.APIServerConfig">
APIServerConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>apiserverConfig allows specifying a host and auth methods to access the
Kuberntees API server.
If null, Prometheus is assumed to run inside of the cluster: it will
discover the API servers automatically and use the Pod&rsquo;s CA certificate
and bearer token file at /var/run/secrets/kubernetes.io/serviceaccount/.</p>
</td>
</tr>
<tr>
<td>
<code>priorityClassName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>priorityClassName assigned to the Pods.</p>
</td>
</tr>
<tr>
<td>
<code>portName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>portName used for the pods and governing service.
Default: &ldquo;web&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>arbitraryFSAccessThroughSMs</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ArbitraryFSAccessThroughSMsConfig">
ArbitraryFSAccessThroughSMsConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>arbitraryFSAccessThroughSMs when true, ServiceMonitor, PodMonitor and Probe object are forbidden to
reference arbitrary files on the file system of the &lsquo;prometheus&rsquo;
container.
When a ServiceMonitor&rsquo;s endpoint specifies a <code>bearerTokenFile</code> value
(e.g.  &lsquo;/var/run/secrets/kubernetes.io/serviceaccount/token&rsquo;), a
malicious target can get access to the Prometheus service account&rsquo;s
token in the Prometheus&rsquo; scrape request. Setting
<code>spec.arbitraryFSAccessThroughSM</code> to &lsquo;true&rsquo; would prevent the attack.
Users should instead provide the credentials using the
<code>spec.bearerTokenSecret</code> field.</p>
</td>
</tr>
<tr>
<td>
<code>overrideHonorLabels</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>overrideHonorLabels when true, Prometheus resolves label conflicts by renaming the labels in the scraped data
to “exported_” for all targets created from ServiceMonitor, PodMonitor and
ScrapeConfig objects. Otherwise the HonorLabels field of the service or pod monitor applies.
In practice,<code>OverrideHonorLabels:true</code> enforces <code>honorLabels:false</code>
for all ServiceMonitor, PodMonitor and ScrapeConfig objects.</p>
</td>
</tr>
<tr>
<td>
<code>overrideHonorTimestamps</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>overrideHonorTimestamps when true, Prometheus ignores the timestamps for all the targets created
from service and pod monitors.
Otherwise the HonorTimestamps field of the service or pod monitor applies.</p>
</td>
</tr>
<tr>
<td>
<code>ignoreNamespaceSelectors</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>ignoreNamespaceSelectors when true, <code>spec.namespaceSelector</code> from all PodMonitor, ServiceMonitor
and Probe objects will be ignored. They will only discover targets
within the namespace of the PodMonitor, ServiceMonitor and Probe
object.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedNamespaceLabel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedNamespaceLabel when not empty, a label will be added to:</p>
<ol>
<li>All metrics scraped from <code>ServiceMonitor</code>, <code>PodMonitor</code>, <code>Probe</code> and <code>ScrapeConfig</code> objects.</li>
<li>All metrics generated from recording rules defined in <code>PrometheusRule</code> objects.</li>
<li>All alerts generated from alerting rules defined in <code>PrometheusRule</code> objects.</li>
<li>All vector selectors of PromQL expressions defined in <code>PrometheusRule</code> objects.</li>
</ol>
<p>The label will not added for objects referenced in <code>spec.excludedFromEnforcement</code>.</p>
<p>The label&rsquo;s name is this field&rsquo;s value.
The label&rsquo;s value is the namespace of the <code>ServiceMonitor</code>,
<code>PodMonitor</code>, <code>Probe</code>, <code>PrometheusRule</code> or <code>ScrapeConfig</code> object.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedSampleLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedSampleLimit when defined specifies a global limit on the number
of scraped samples that will be accepted. This overrides any
<code>spec.sampleLimit</code> set by ServiceMonitor, PodMonitor, Probe objects
unless <code>spec.sampleLimit</code> is greater than zero and less than
<code>spec.enforcedSampleLimit</code>.</p>
<p>It is meant to be used by admins to keep the overall number of
samples/series under a desired limit.</p>
<p>When both <code>enforcedSampleLimit</code> and <code>sampleLimit</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined sampleLimit value will inherit the global sampleLimit value (Prometheus &gt;= 2.45.0) or the enforcedSampleLimit value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedSampleLimit</code> is greater than the <code>sampleLimit</code>, the <code>sampleLimit</code> will be set to <code>enforcedSampleLimit</code>.
* Scrape objects with a sampleLimit value less than or equal to enforcedSampleLimit keep their specific value.
* Scrape objects with a sampleLimit value greater than enforcedSampleLimit are set to enforcedSampleLimit.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedTargetLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedTargetLimit when defined specifies a global limit on the number
of scraped targets. The value overrides any <code>spec.targetLimit</code> set by
ServiceMonitor, PodMonitor, Probe objects unless <code>spec.targetLimit</code> is
greater than zero and less than <code>spec.enforcedTargetLimit</code>.</p>
<p>It is meant to be used by admins to to keep the overall number of
targets under a desired limit.</p>
<p>When both <code>enforcedTargetLimit</code> and <code>targetLimit</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined targetLimit value will inherit the global targetLimit value (Prometheus &gt;= 2.45.0) or the enforcedTargetLimit value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedTargetLimit</code> is greater than the <code>targetLimit</code>, the <code>targetLimit</code> will be set to <code>enforcedTargetLimit</code>.
* Scrape objects with a targetLimit value less than or equal to enforcedTargetLimit keep their specific value.
* Scrape objects with a targetLimit value greater than enforcedTargetLimit are set to enforcedTargetLimit.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedLabelLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedLabelLimit when defined specifies a global limit on the number
of labels per sample. The value overrides any <code>spec.labelLimit</code> set by
ServiceMonitor, PodMonitor, Probe objects unless <code>spec.labelLimit</code> is
greater than zero and less than <code>spec.enforcedLabelLimit</code>.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
<p>When both <code>enforcedLabelLimit</code> and <code>labelLimit</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined labelLimit value will inherit the global labelLimit value (Prometheus &gt;= 2.45.0) or the enforcedLabelLimit value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedLabelLimit</code> is greater than the <code>labelLimit</code>, the <code>labelLimit</code> will be set to <code>enforcedLabelLimit</code>.
* Scrape objects with a labelLimit value less than or equal to enforcedLabelLimit keep their specific value.
* Scrape objects with a labelLimit value greater than enforcedLabelLimit are set to enforcedLabelLimit.</p>
</td>
</tr>
<tr>
<td>
<code>enforcedLabelNameLengthLimit</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>enforcedLabelNameLengthLimit when defined specifies a global limit on the length
of labels name per sample. The value overrides any <code>spec.labelNameLengthLimit</code> set by
ServiceMonitor, PodMonitor, Probe objects unless <code>spec.labelNameLengthLimit</code> is
greater than zero and less than <code>spec.enforcedLabelNameLengthLimit</code>.</p>
<p>It requires Prometheus &gt;= v2.27.0.</p>
<p>When both <code>enforcedLabelNameLengthLimit</code> and <code>labelNameLengthLimit</code> are defined and greater than zero, the following rules apply:
* Scrape objects without a defined labelNameLengthLimit value will inherit the global labelNameLengthLimit value (Prometheus &gt;= 2.45.0) or the enforcedLabelNameLengthLimit value (Prometheus &lt; v2.45.0).
If Prometheus version is &gt;= 2.45.0 and the <code>enforcedLabelNameLengthLimit</code> is greater than the <code>labelNameLengthLimit</code>, the <code>labelNameLengthLimit</code> will be set to <code>enforcedLabelNameLengthLimit</code>.
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
