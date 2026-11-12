<!-- Part 31 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.ThanosRulerStatus">ThanosRulerStatus
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ThanosRuler">ThanosRuler</a>)
</p>
<div>
<p>ThanosRulerStatus is the most recent observed status of the ThanosRuler. Read-only.
More info:
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
<code>paused</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>paused defines whether any actions on the underlying managed objects are
being performed. Only delete actions will be performed.</p>
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
<p>replicas defines the total number of non-terminated pods targeted by this ThanosRuler deployment
(their labels match the selector).</p>
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
<em>(Optional)</em>
<p>updatedReplicas defines the total number of non-terminated pods targeted by this ThanosRuler deployment
that have the desired version spec.</p>
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
<em>(Optional)</em>
<p>availableReplicas defines the total number of available pods (ready for at least minReadySeconds)
targeted by this ThanosRuler deployment.</p>
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
<em>(Optional)</em>
<p>unavailableReplicas defines the total number of unavailable pods targeted by this ThanosRuler deployment.</p>
</td>
</tr>
<tr>
<td>
<code>conditions</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Condition">
[]Condition
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>conditions defines the current state of the ThanosRuler object.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ThanosRulerWebSpec">ThanosRulerWebSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>ThanosRulerWebSpec defines the configuration of the ThanosRuler web server.</p>
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
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WebTLSConfig">
WebTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig defines the TLS parameters for HTTPS.</p>
</td>
</tr>
<tr>
<td>
<code>httpConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WebHTTPConfig">
WebHTTPConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpConfig defines HTTP parameters for web server.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ThanosSpec">ThanosSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>)
</p>
<div>
<p>ThanosSpec defines the configuration of the Thanos sidecar.</p>
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
<code>image</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>image defines the container image name for Thanos. If specified, it takes precedence over
the <code>spec.thanos.baseImage</code>, <code>spec.thanos.tag</code> and <code>spec.thanos.sha</code>
fields.</p>
<p>Specifying <code>spec.thanos.version</code> is still necessary to ensure the
Prometheus Operator knows which version of Thanos is being configured.</p>
<p>If neither <code>spec.thanos.image</code> nor <code>spec.thanos.baseImage</code> are defined,
the operator will use the latest upstream version of Thanos available at
the time when the operator was released.</p>
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
<p>version of Thanos being deployed. The operator uses this information
to generate the Prometheus StatefulSet + configuration files.</p>
<p>If not specified, the operator assumes the latest upstream release of
Thanos available at the time when the version of the operator was
released.</p>
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
<p>tag is deprecated: use &lsquo;image&rsquo; instead. The image&rsquo;s tag can be specified as as part of the image name.</p>
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
<p>sha is deprecated: use &lsquo;image&rsquo; instead.  The image digest can be specified as part of the image name.</p>
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
<p>baseImage is deprecated: use &lsquo;image&rsquo; instead.</p>
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
<p>resources defines the resources requests and limits of the Thanos sidecar.</p>
</td>
</tr>
<tr>
<td>
<code>objectStorageConfig</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>objectStorageConfig defines the Thanos sidecar&rsquo;s configuration to upload TSDB blocks to object storage.</p>
<p>More info: <a href="https://thanos.io/tip/thanos/storage.md/">https://thanos.io/tip/thanos/storage.md/</a></p>
<p>objectStorageConfigFile takes precedence over this field.</p>
</td>
</tr>
<tr>
<td>
<code>objectStorageConfigFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>objectStorageConfigFile defines the Thanos sidecar&rsquo;s configuration file to upload TSDB blocks to object storage.</p>
<p>More info: <a href="https://thanos.io/tip/thanos/storage.md/">https://thanos.io/tip/thanos/storage.md/</a></p>
<p>This field takes precedence over objectStorageConfig.</p>
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
<p>listenLocal is deprecated: use <code>grpcListenLocal</code> and <code>httpListenLocal</code> instead.</p>
</td>
</tr>
<tr>
<td>
<code>grpcListenLocal</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>grpcListenLocal defines when true, the Thanos sidecar listens on the loopback interface instead
of the Pod IP&rsquo;s address for the gRPC endpoints.</p>
<p>It has no effect if <code>listenLocal</code> is true.</p>
</td>
</tr>
<tr>
<td>
<code>httpListenLocal</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>httpListenLocal when true, the Thanos sidecar listens on the loopback interface instead
of the Pod IP&rsquo;s address for the HTTP endpoints.</p>
<p>It has no effect if <code>listenLocal</code> is true.</p>
</td>
</tr>
<tr>
<td>
<code>tracingConfig</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tracingConfig defines the tracing configuration for the Thanos sidecar.</p>
<p><code>tracingConfigFile</code> takes precedence over this field.</p>
<p>More info: <a href="https://thanos.io/tip/thanos/tracing.md/">https://thanos.io/tip/thanos/tracing.md/</a></p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
</td>
</tr>
<tr>
<td>
<code>tracingConfigFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tracingConfigFile defines the tracing configuration file for the Thanos sidecar.</p>
<p>This field takes precedence over <code>tracingConfig</code>.</p>
<p>More info: <a href="https://thanos.io/tip/thanos/tracing.md/">https://thanos.io/tip/thanos/tracing.md/</a></p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
</td>
</tr>
<tr>
<td>
<code>grpcServerTlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GRPCServerTLSConfig">
GRPCServerTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>grpcServerTlsConfig defines the TLS parameters for the gRPC server providing the StoreAPI.</p>
<p>Note: Currently only the <code>minVersion</code>, <code>caFile</code>, <code>certFile</code>, <code>keyFile</code>, <code>cipherSuites</code> and <code>curves</code> fields are supported.</p>
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
<p>logLevel for the Thanos sidecar.</p>
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
<p>logFormat for the Thanos sidecar.</p>
</td>
</tr>
<tr>
<td>
<code>minTime</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>minTime defines the start of time range limit served by the Thanos sidecar&rsquo;s StoreAPI.
The field&rsquo;s value should be a constant time in RFC3339 format or a time
duration relative to current time, such as -1d or 2h45m. Valid duration
units are ms, s, m, h, d, w, y.</p>
</td>
</tr>
<tr>
<td>
<code>blockSize</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>blockSize controls the size of TSDB blocks produced by Prometheus.
The default value is 2h to match the upstream Prometheus defaults.</p>
<p>WARNING: Changing the block duration can impact the performance and
efficiency of the entire Prometheus/Thanos stack due to how it interacts
with memory and Thanos compactors. It is recommended to keep this value
set to a multiple of 120 times your longest scrape or rule interval. For
example, 30s * 120 = 1h.</p>
</td>
</tr>
<tr>
<td>
<code>readyTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>readyTimeout defines the maximum time that the Thanos sidecar will wait for
Prometheus to start.</p>
</td>
</tr>
<tr>
<td>
<code>getConfigInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>getConfigInterval defines how often to retrieve the Prometheus configuration.</p>
</td>
</tr>
<tr>
<td>
<code>getConfigTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>getConfigTimeout defines the maximum time to wait when retrieving the Prometheus configuration.</p>
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
<p>volumeMounts allows configuration of additional VolumeMounts for Thanos.
VolumeMounts specified will be appended to other VolumeMounts in the
&lsquo;thanos-sidecar&rsquo; container.</p>
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
<p>additionalArgs allows setting additional arguments for the Thanos container.
The arguments are passed as-is to the Thanos container which may cause issues
if they are invalid or not supported the given Thanos version.
In case of an argument conflict (e.g. an argument which is already set by the
operator itself) or when providing an invalid argument, the reconciliation will
fail and an error will be logged.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TopologyShardingStrategy">TopologyShardingStrategy
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ShardingStrategy">ShardingStrategy</a>)
</p>
<div>
<p>TopologyShardingStrategy defines the configuration for topology-aware sharding.</p>
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
<code>externalLabelName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>externalLabelName defines the name of the Prometheus external label used
to communicate the topology zone assigned to the Prometheus instance.
If not defined, it defaults to &ldquo;zone&rdquo;.
If set to the empty string, no external label is added to the Prometheus configuration.</p>
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
<p>values defines the list of topology values (e.g. zone names) to be used
for sharding. The configured number of shards must be greater than or
equal to the number of values.</p>
</td>
</tr>
</tbody>
</table>
