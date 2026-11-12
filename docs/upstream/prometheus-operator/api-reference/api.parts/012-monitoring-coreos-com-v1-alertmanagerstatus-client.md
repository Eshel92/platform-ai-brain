<!-- Part 12 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.AlertmanagerStatus">AlertmanagerStatus
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Alertmanager">Alertmanager</a>)
</p>
<div>
<p>AlertmanagerStatus is the most recent observed status of the Alertmanager cluster. Read-only.
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
<p>replicas defines the total number of non-terminated pods targeted by this Alertmanager
object (their labels match the selector).</p>
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
<p>updatedReplicas defines the total number of non-terminated pods targeted by this Alertmanager
object that have the desired version spec.</p>
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
targeted by this Alertmanager cluster.</p>
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
<p>unavailableReplicas defines the total number of unavailable pods targeted by this Alertmanager object.</p>
</td>
</tr>
<tr>
<td>
<code>selector</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>selector used to match the pods targeted by this Alertmanager object.</p>
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
<p>conditions defines the current state of the Alertmanager object.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AlertmanagerWebSpec">AlertmanagerWebSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
</p>
<div>
<p>AlertmanagerWebSpec defines the web command line flags when starting Alertmanager.</p>
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
<tr>
<td>
<code>getConcurrency</code><br/>
<em>
uint32
</em>
</td>
<td>
<em>(Optional)</em>
<p>getConcurrency defines the maximum number of GET requests processed concurrently. This corresponds to the
Alertmanager&rsquo;s <code>--web.get-concurrency</code> flag.</p>
</td>
</tr>
<tr>
<td>
<code>timeout</code><br/>
<em>
uint32
</em>
</td>
<td>
<em>(Optional)</em>
<p>timeout for HTTP requests. This corresponds to the Alertmanager&rsquo;s
<code>--web.timeout</code> flag.</p>
</td>
</tr>
<tr>
<td>
<code>corsOrigin</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>corsOrigin is a fully anchored regular expression matching the origins
allowed to call the API from a browser. This corresponds to the
Alertmanager&rsquo;s <code>--web.cors.origin</code> flag.
It requires Alertmanager &gt;= v0.34.2.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ArbitraryFSAccessThroughSMsConfig">ArbitraryFSAccessThroughSMsConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>)
</p>
<div>
<p>ArbitraryFSAccessThroughSMsConfig enables users to configure, whether
a service monitor selected by the Prometheus instance is allowed to use
arbitrary files on the file system of the Prometheus container. This is the case
when e.g. a service monitor specifies a BearerTokenFile in an endpoint. A
malicious user could create a service monitor selecting arbitrary secret files
in the Prometheus container. Those secrets would then be sent with a scrape
request by Prometheus to a malicious target. Denying the above would prevent the
attack, users can instead use the BearerTokenSecret field.</p>
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
<code>deny</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>deny prevents service monitors from accessing arbitrary files on the file system.
When true, service monitors cannot use file-based configurations like BearerTokenFile
that could potentially access sensitive files. When false (default), such access is allowed.
Setting this to true enhances security by preventing potential credential theft attacks.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.Argument">Argument
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>, <a href="#monitoring.coreos.com/v1.ThanosSpec">ThanosSpec</a>)
</p>
<div>
<p>Argument as part of the AdditionalArgs list.</p>
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
<p>name of the argument, e.g. &ldquo;scrape.discovery-reload-interval&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>value</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>value defines the argument value, e.g. 30s. Can be empty for name-only arguments (e.g. &ndash;storage.tsdb.no-lockfile)</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AttachMetadata">AttachMetadata
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>, <a href="#monitoring.coreos.com/v1.ScrapeClass">ScrapeClass</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>)
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
<p>node when set to true, Prometheus attaches node metadata to the discovered
targets.</p>
<p>The Prometheus service account must have the <code>list</code> and <code>watch</code>
permissions on the <code>Nodes</code> objects.</p>
<p>Node metadata labels are not automatically added to scraped metrics. They are
exposed as <code>__meta_kubernetes_node_*</code> labels and can be copied to timeseries
with relabeling configuration.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.Authorization">Authorization
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.APIServerConfig">APIServerConfig</a>, <a href="#monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1.ScrapeClass">ScrapeClass</a>)
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
<code>type</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>type defines the authentication type. The value is case-insensitive.</p>
<p>&ldquo;Basic&rdquo; is not a supported value.</p>
<p>Default: &ldquo;Bearer&rdquo;</p>
</td>
</tr>
<tr>
<td>
<code>credentials</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>credentials defines a key of a Secret in the namespace that contains the credentials for authentication.</p>
</td>
</tr>
<tr>
<td>
<code>credentialsFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>credentialsFile defines the file to read a secret from, mutually exclusive with <code>credentials</code>.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AzureAD">AzureAD
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>)
</p>
<div>
<p>AzureAD defines the configuration for remote write&rsquo;s azuread parameters.</p>
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
<code>cloud</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>cloud defines the Azure Cloud. Options are &lsquo;AzurePublic&rsquo;, &lsquo;AzureChina&rsquo;, or &lsquo;AzureGovernment&rsquo;.</p>
</td>
</tr>
<tr>
<td>
<code>managedIdentity</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ManagedIdentity">
ManagedIdentity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>managedIdentity defines the Azure User-assigned Managed identity.
Cannot be set at the same time as <code>oauth</code>, <code>sdk</code> or <code>workloadIdentity</code>.</p>
</td>
</tr>
<tr>
<td>
<code>oauth</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AzureOAuth">
AzureOAuth
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>oauth defines the oauth config that is being used to authenticate.
Cannot be set at the same time as <code>managedIdentity</code>, <code>sdk</code> or <code>workloadIdentity</code>.</p>
<p>It requires Prometheus &gt;= v2.48.0 or Thanos &gt;= v0.31.0.</p>
</td>
</tr>
<tr>
<td>
<code>sdk</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AzureSDK">
AzureSDK
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>sdk defines the Azure SDK config that is being used to authenticate.
See <a href="https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication">https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication</a>
Cannot be set at the same time as <code>oauth</code>, <code>managedIdentity</code> or <code>workloadIdentity</code>.</p>
<p>It requires Prometheus &gt;= v2.52.0 or Thanos &gt;= v0.36.0.</p>
</td>
</tr>
<tr>
<td>
<code>workloadIdentity</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AzureWorkloadIdentity">
AzureWorkloadIdentity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>workloadIdentity defines the Azure Workload Identity authentication.
Cannot be set at the same time as <code>oauth</code>, <code>managedIdentity</code>, or <code>sdk</code>.</p>
<p>It requires Prometheus &gt;= 3.7.0. Currently not supported by Thanos.</p>
</td>
</tr>
<tr>
<td>
<code>scope</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>scope is the custom OAuth 2.0 scope to request when acquiring tokens.
It requires Prometheus &gt;= 3.9.0. Currently not supported by Thanos.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AzureOAuth">AzureOAuth
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AzureAD">AzureAD</a>)
</p>
<div>
<p>AzureOAuth defines the Azure OAuth settings.</p>
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
<code>clientId</code><br/>
<em>
string
</em>
</td>
<td>
<p>clientId defines the clientId of the Azure Active Directory application that is being used to authenticate.</p>
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
<p>clientSecret specifies a key of a Secret containing the client secret of the Azure Active Directory application that is being used to authenticate.</p>
</td>
</tr>
<tr>
<td>
<code>tenantId</code><br/>
<em>
string
</em>
</td>
<td>
<p>tenantId is the tenant ID of the Azure Active Directory application that is being used to authenticate.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AzureSDK">AzureSDK
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AzureAD">AzureAD</a>)
</p>
<div>
<p>AzureSDK is used to store azure SDK config values.</p>
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
<code>tenantId</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>tenantId defines the tenant ID of the azure active directory application that is being used to authenticate.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.AzureWorkloadIdentity">AzureWorkloadIdentity
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AzureAD">AzureAD</a>)
</p>
<div>
<p>AzureWorkloadIdentity defines the Azure Workload Identity authentication configuration.</p>
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
<code>clientId</code><br/>
<em>
string
</em>
</td>
<td>
<p>clientId is the clientID of the Azure Active Directory application.</p>
</td>
</tr>
<tr>
<td>
<code>tenantId</code><br/>
<em>
string
</em>
</td>
<td>
<p>tenantId is the tenant ID of the Azure Active Directory application.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.BasicAuth">BasicAuth
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.APIServerConfig">APIServerConfig</a>, <a href="#monitoring.coreos.com/v1.AlertmanagerEndpoints">AlertmanagerEndpoints</a>, <a href="#monitoring.coreos.com/v1.HTTPConfigWithoutTLS">HTTPConfigWithoutTLS</a>, <a href="#monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.AzureSDConfig">AzureSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ConsulSDConfig">ConsulSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSDConfig">DockerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.DockerSwarmSDConfig">DockerSwarmSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.EurekaSDConfig">EurekaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPConfig">HTTPConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HTTPSDConfig">HTTPSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.HetznerSDConfig">HetznerSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KubernetesSDConfig">KubernetesSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.KumaSDConfig">KumaSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.LightSailSDConfig">LightSailSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.NomadSDConfig">NomadSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.PuppetDBSDConfig">PuppetDBSDConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>, <a href="#monitoring.coreos.com/v1beta1.HTTPConfig">HTTPConfig</a>)
</p>
<div>
<p>BasicAuth configures HTTP Basic Authentication settings.</p>
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
<code>username</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>username defines a key of a Secret containing the username for
authentication.</p>
</td>
</tr>
<tr>
<td>
<code>password</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>password defines a key of a Secret containing the password for
authentication.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ByteSize">ByteSize
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerLimitsSpec">AlertmanagerLimitsSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.PodMonitorSpec">PodMonitorSpec</a>, <a href="#monitoring.coreos.com/v1.PrometheusSpec">PrometheusSpec</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitorSpec">ServiceMonitorSpec</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfigSpec">ScrapeConfigSpec</a>)
</p>
<div>
<p>ByteSize is a valid memory size type based on powers-of-2, so 1KB is 1024B.
Supported units: B, KB, KiB, MB, MiB, GB, GiB, TB, TiB, PB, PiB, EB, EiB Ex: <code>512MB</code>.</p>
</div>

<h3 id="monitoring.coreos.com/v1.ChunkEncodingFloats">ChunkEncodingFloats
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ChunkEncodingSpec">ChunkEncodingSpec</a>)
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
<tbody><tr><td><p>&#34;Xor&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Xor2&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ChunkEncodingSpec">ChunkEncodingSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.TSDBSpec">TSDBSpec</a>)
</p>
<div>
<p>ChunkEncodingSpec configures per-chunk-type encoding overrides.</p>
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
<code>floats</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ChunkEncodingFloats">
ChunkEncodingFloats
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>floats selects the encoding used for float chunks.
Valid values are &ldquo;Xor&rdquo; and &ldquo;Xor2&rdquo;.</p>
<p>Notice:
* Setting &ldquo;Xor&rdquo; is incompatible with &ndash;enable-feature=st-storage
(XOR chunks do not store start timestamps).
* Setting &ldquo;Xor2&rdquo; automatically adds the <code>xor2-encoding</code> feature flag.</p>
<p>It requires Prometheus &gt;= v3.13.0.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ClientAuthType">ClientAuthType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.WebTLSConfig">WebTLSConfig</a>)
</p>
<div>
<p>Taken from <a href="https://golang.org/pkg/crypto/tls/#ClientAuthType">https://golang.org/pkg/crypto/tls/#ClientAuthType</a>.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;NoClientCert&#34;</p></td>
<td><p>NoClientCert indicates that no client certificate should be requested
during the handshake, and if any certificates are sent they will not
be verified.</p>
</td>
</tr><tr><td><p>&#34;RequestClientCert&#34;</p></td>
<td><p>RequestClientCert indicates that a client certificate should be requested
during the handshake, but does not require that the client send any
certificates.</p>
</td>
</tr><tr><td><p>&#34;RequireAndVerifyClientCert&#34;</p></td>
<td><p>RequireAndVerifyClientCert indicates that a client certificate should be requested
during the handshake, and that at least one valid certificate is required
to be sent by the client.</p>
</td>
</tr><tr><td><p>&#34;RequireAnyClientCert&#34;</p></td>
<td><p>RequireAnyClientCert indicates that a client certificate should be requested
during the handshake, and that at least one certificate is required to be
sent by the client, but that certificate is not required to be valid.</p>
</td>
</tr><tr><td><p>&#34;VerifyClientCertIfGiven&#34;</p></td>
<td><p>VerifyClientCertIfGiven indicates that a client certificate should be requested
during the handshake, but does not require that the client sends a
certificate. If the client does send a certificate it is required to be
valid.</p>
</td>
</tr></tbody>
</table>
