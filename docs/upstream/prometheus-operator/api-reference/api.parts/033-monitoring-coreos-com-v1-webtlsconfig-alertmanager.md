<!-- Part 33 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.WebTLSConfig">WebTLSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ClusterTLSConfig">ClusterTLSConfig</a>, <a href="#monitoring.coreos.com/v1.WebConfigFileFields">WebConfigFileFields</a>)
</p>
<div>
<p>WebTLSConfig defines the TLS parameters for HTTPS.</p>
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
<code>cert</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>cert defines the Secret or ConfigMap containing the TLS certificate for the web server.</p>
<p>Either <code>keySecret</code> or <code>keyFile</code> must be defined.</p>
<p>It is mutually exclusive with <code>certFile</code>.</p>
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
<p>certFile defines the path to the TLS certificate file in the container for the web server.</p>
<p>Either <code>keySecret</code> or <code>keyFile</code> must be defined.</p>
<p>It is mutually exclusive with <code>cert</code>.</p>
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
<p>keySecret defines the secret containing the TLS private key for the web server.</p>
<p>Either <code>cert</code> or <code>certFile</code> must be defined.</p>
<p>It is mutually exclusive with <code>keyFile</code>.</p>
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
<p>keyFile defines the path to the TLS private key file in the container for the web server.</p>
<p>If defined, either <code>cert</code> or <code>certFile</code> must be defined.</p>
<p>It is mutually exclusive with <code>keySecret</code>.</p>
</td>
</tr>
<tr>
<td>
<code>client_ca</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SecretOrConfigMap">
SecretOrConfigMap
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>client_ca defines the Secret or ConfigMap containing the CA certificate for client certificate
authentication to the server.</p>
<p>It is mutually exclusive with <code>clientCAFile</code>.</p>
</td>
</tr>
<tr>
<td>
<code>clientCAFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientCAFile defines the path to the CA certificate file for client certificate authentication to
the server.</p>
<p>It is mutually exclusive with <code>client_ca</code>.</p>
</td>
</tr>
<tr>
<td>
<code>clientAuthType</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ClientAuthType">
ClientAuthType
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientAuthType defines the server policy for client TLS authentication.</p>
<p>For more detail on clientAuth options:
<a href="https://golang.org/pkg/crypto/tls/#ClientAuthType">https://golang.org/pkg/crypto/tls/#ClientAuthType</a></p>
</td>
</tr>
<tr>
<td>
<code>minVersion</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>minVersion defines the minimum TLS version that is acceptable.</p>
</td>
</tr>
<tr>
<td>
<code>maxVersion</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxVersion defines the Maximum TLS version that is acceptable.</p>
</td>
</tr>
<tr>
<td>
<code>cipherSuites</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>cipherSuites defines the list of supported cipher suites for TLS versions up to TLS 1.2.</p>
<p>If not defined, the Go default cipher suites are used.
Available cipher suites are documented in the Go documentation:
<a href="https://golang.org/pkg/crypto/tls/#pkg-constants">https://golang.org/pkg/crypto/tls/#pkg-constants</a></p>
</td>
</tr>
<tr>
<td>
<code>preferServerCipherSuites</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>preferServerCipherSuites defines whether the server selects the client&rsquo;s most preferred cipher
suite, or the server&rsquo;s most preferred cipher suite.</p>
<p>If true then the server&rsquo;s preference, as expressed in
the order of elements in cipherSuites, is used.</p>
</td>
</tr>
<tr>
<td>
<code>curvePreferences</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>curvePreferences defines elliptic curves that will be used in an ECDHE handshake, in preference
order.</p>
<p>Available curves are documented in the Go documentation:
<a href="https://golang.org/pkg/crypto/tls/#CurveID">https://golang.org/pkg/crypto/tls/#CurveID</a></p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.WhenScaledRetentionType">WhenScaledRetentionType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ShardRetentionPolicy">ShardRetentionPolicy</a>)
</p>
<div>
</div>

<h3 id="monitoring.coreos.com/v1.WorkloadBinding">WorkloadBinding
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.ConfigResourceStatus">ConfigResourceStatus</a>)
</p>
<div>
<p>WorkloadBinding is a link between a configuration resource and a workload resource.</p>
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
<code>group</code><br/>
<em>
string
</em>
</td>
<td>
<p>group defines the group of the referenced resource.</p>
</td>
</tr>
<tr>
<td>
<code>resource</code><br/>
<em>
string
</em>
</td>
<td>
<p>resource defines the type of resource being referenced (e.g. Prometheus, PrometheusAgent, ThanosRuler or Alertmanager).</p>
</td>
</tr>
<tr>
<td>
<code>name</code><br/>
<em>
string
</em>
</td>
<td>
<p>name defines the name of the referenced object.</p>
</td>
</tr>
<tr>
<td>
<code>namespace</code><br/>
<em>
string
</em>
</td>
<td>
<p>namespace defines the namespace of the referenced object.</p>
</td>
</tr>
<tr>
<td>
<code>conditions</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ConfigResourceCondition">
[]ConfigResourceCondition
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>conditions defines the current state of the configuration resource when bound to the referenced Workload object.</p>
</td>
</tr>
</tbody>
</table>
<hr/>

<h2 id="monitoring.coreos.com/v1alpha1">monitoring.coreos.com/v1alpha1</h2>
Resource Types:
<ul><li>
<a href="#monitoring.coreos.com/v1alpha1.AlertmanagerConfig">AlertmanagerConfig</a>
</li><li>
<a href="#monitoring.coreos.com/v1alpha1.PrometheusAgent">PrometheusAgent</a>
</li><li>
<a href="#monitoring.coreos.com/v1alpha1.ScrapeConfig">ScrapeConfig</a>
</li></ul>

<h3 id="monitoring.coreos.com/v1alpha1.AlertmanagerConfig">AlertmanagerConfig
</h3>
<div>
<p>AlertmanagerConfig configures the Prometheus Alertmanager,
specifying how alerts should be grouped, inhibited and notified to external systems.</p>
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
<td><code>AlertmanagerConfig</code></td>
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
<a href="#monitoring.coreos.com/v1alpha1.AlertmanagerConfigSpec">
AlertmanagerConfigSpec
</a>
</em>
</td>
<td>
<p>spec defines the specification of AlertmanagerConfigSpec</p>
<br/>
<br/>
<table>
<tr>
<td>
<code>route</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.Route">
Route
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>route defines the Alertmanager route definition for alerts matching the resource&rsquo;s
namespace. If present, it will be added to the generated Alertmanager
configuration as a first-level route.</p>
</td>
</tr>
<tr>
<td>
<code>receivers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.Receiver">
[]Receiver
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>receivers defines the list of receivers.</p>
</td>
</tr>
<tr>
<td>
<code>inhibitRules</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.InhibitRule">
[]InhibitRule
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>inhibitRules defines the list of inhibition rules. The rules will only apply to alerts matching
the resource&rsquo;s namespace.</p>
</td>
</tr>
<tr>
<td>
<code>muteTimeIntervals</code><br/>
<em>
<a href="#monitoring.coreos.com/v1alpha1.MuteTimeInterval">
[]MuteTimeInterval
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>muteTimeIntervals defines the list of MuteTimeInterval specifying when the routes should be muted.</p>
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
