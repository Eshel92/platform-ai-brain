<!-- Part 29 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.StorageSpec">StorageSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>StorageSpec defines the configured storage for a group Prometheus servers.
If no storage option is specified, then by default an <a href="https://kubernetes.io/docs/concepts/storage/volumes/#emptydir">EmptyDir</a> will be used.</p>
<p>If multiple storage options are specified, priority will be given as follows:
1. emptyDir
2. ephemeral
3. volumeClaimTemplate</p>
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
<code>disableMountSubPath</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>disableMountSubPath deprecated: subPath usage will be removed in a future release.</p>
</td>
</tr>
<tr>
<td>
<code>emptyDir</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#emptydirvolumesource-v1-core">
Kubernetes core/v1.EmptyDirVolumeSource
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>emptyDir to be used by the StatefulSet.
If specified, it takes precedence over <code>ephemeral</code> and <code>volumeClaimTemplate</code>.
More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes/#emptydir">https://kubernetes.io/docs/concepts/storage/volumes/#emptydir</a></p>
</td>
</tr>
<tr>
<td>
<code>ephemeral</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#ephemeralvolumesource-v1-core">
Kubernetes core/v1.EphemeralVolumeSource
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ephemeral to be used by the StatefulSet.
This is a beta field in k8s 1.21 and GA in 1.15.
For lower versions, starting with k8s 1.19, it requires enabling the GenericEphemeralVolume feature gate.
More info: <a href="https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes">https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes</a></p>
</td>
</tr>
<tr>
<td>
<code>volumeClaimTemplate</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.EmbeddedPersistentVolumeClaim">
EmbeddedPersistentVolumeClaim
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>volumeClaimTemplate defines the PVC spec to be used by the Prometheus StatefulSets.
The easiest way to use a volume that cannot be automatically provisioned
is to use a label selector alongside manually created PersistentVolumes.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TLSConfig">TLSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.APIServerConfig">APIServerConfig</a>, <a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.GRPCServerTLSConfig">GRPCServerTLSConfig</a>, <a href="#monitoring.coreos.com/v1.HTTPConfigWithTLSFiles">HTTPConfigWithTLSFiles</a>, <a href="#monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1.ScrapeClass">ScrapeClass</a>, <a href="#monitoring.coreos.com/v1.TracingConfig">TracingConfig</a>)
</p>
<div>
<p>TLSConfig defines full TLS configuration.</p>
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
<code>ca</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ca defines the Certificate authority used when verifying server certificates.</p>
</td>
</tr>
<tr>
<td>
<code>cert</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>cert defines the Client certificate to present when doing client-authentication.</p>
</td>
</tr>
<tr>
<td>
<code>keySecret</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>keySecret defines the Secret containing the client key file for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>serverName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>serverName is used to verify the hostname for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>insecureSkipVerify</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>insecureSkipVerify defines how to disable target certificate validation.</p>
</td>
</tr>
<tr>
<td>
<code>minVersion</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TLSVersion">
TLSVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>minVersion defines the minimum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.35.0 or Thanos &gt;= v0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>maxVersion</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TLSVersion">
TLSVersion
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxVersion defines the maximum acceptable TLS version.</p>
<p>It requires Prometheus &gt;= v2.41.0 or Thanos &gt;= v0.31.0.</p>
</td>
</tr>
<tr>
<td>
<code>caFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>caFile defines the path to the CA cert in the Prometheus container to use for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>certFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>certFile defines the path to the client cert file in the Prometheus container for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>keyFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>keyFile defines the path to the client key file in the Prometheus container for the targets.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TLSFilesConfig">TLSFilesConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.TLSConfig">TLSConfig</a>)
</p>
<div>
<p>TLSFilesConfig extends the TLS configuration with file parameters.</p>
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
<code>caFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>caFile defines the path to the CA cert in the Prometheus container to use for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>certFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>certFile defines the path to the client cert file in the Prometheus container for the targets.</p>
</td>
</tr>
<tr>
<td>
<code>keyFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>keyFile defines the path to the client key file in the Prometheus container for the targets.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TLSVersion">TLSVersion
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.SafeTLSConfig">SafeTLSConfig</a>)
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
<tbody><tr><td><p>&#34;TLS10&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;TLS11&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;TLS12&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;TLS13&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TSDBSpec">TSDBSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
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
<code>outOfOrderTimeWindow</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>outOfOrderTimeWindow defines how old an out-of-order/out-of-bounds sample can be with
respect to the TSDB max time.</p>
<p>An out-of-order/out-of-bounds sample is ingested into the TSDB as long as
the timestamp of the sample is &gt;= (TSDB.MaxTime - outOfOrderTimeWindow).</p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
<p>It requires Prometheus &gt;= v2.39.0 or PrometheusAgent &gt;= v2.54.0.</p>
</td>
</tr>
<tr>
<td>
<code>staleSeriesCompactionThreshold</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity">
k8s.io/apimachinery/pkg/api/resource.Quantity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>staleSeriesCompactionThreshold configures the trigger point for compacting
stale series from memory into persistent blocks and removing those stale
series from memory.</p>
<p>The threshold is a number between 0.0 and 1.0. It represents the ratio of
stale series in memory to the total series in memory. The stale series
compaction is triggered when this ratio crosses the configured threshold.
It may not trigger the stale series compaction if the usual head compaction
is about to happen soon.</p>
<p>If set to 0, stale series compaction is disabled.</p>
<p>It requires Prometheus &gt;= v3.10.0.</p>
</td>
</tr>
<tr>
<td>
<code>chunkEncoding</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ChunkEncodingSpec">
ChunkEncodingSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>chunkEncoding configures per-chunk-type encoding overrides.</p>
<p>It requires Prometheus &gt;= v3.13.0.</p>
<p>Notice: Setting &ldquo;Xor&rdquo; is incompatible with &ndash;enable-feature=st-storage
(XOR chunks do not store start timestamps).</p>
</td>
</tr>
</tbody>
</table>
