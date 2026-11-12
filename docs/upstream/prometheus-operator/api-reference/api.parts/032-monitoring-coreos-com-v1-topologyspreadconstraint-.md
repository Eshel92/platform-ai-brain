<!-- Part 32 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.TopologySpreadConstraint">TopologySpreadConstraint
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
<code>maxSkew</code><br/>
<em>
int32
</em>
</td>
<td>
<p>MaxSkew describes the degree to which pods may be unevenly distributed.
When <code>whenUnsatisfiable=DoNotSchedule</code>, it is the maximum permitted difference
between the number of matching pods in the target topology and the global minimum.
The global minimum is the minimum number of matching pods in an eligible domain
or zero if the number of eligible domains is less than MinDomains.
For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same
labelSelector spread as 2/2/1:
In this case, the global minimum is 1.
| zone1 | zone2 | zone3 |
|  P P  |  P P  |   P   |
- if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2;
scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2)
violate MaxSkew(1).
- if MaxSkew is 2, incoming pod can be scheduled onto any zone.
When <code>whenUnsatisfiable=ScheduleAnyway</code>, it is used to give higher precedence
to topologies that satisfy it.
It&rsquo;s a required field. Default value is 1 and 0 is not allowed.</p>
</td>
</tr>
<tr>
<td>
<code>topologyKey</code><br/>
<em>
string
</em>
</td>
<td>
<p>TopologyKey is the key of node labels. Nodes that have a label with this key
and identical values are considered to be in the same topology.
We consider each <key, value> as a &ldquo;bucket&rdquo;, and try to put balanced number
of pods into each bucket.
We define a domain as a particular instance of a topology.
Also, we define an eligible domain as a domain whose nodes meet the requirements of
nodeAffinityPolicy and nodeTaintsPolicy.
e.g. If TopologyKey is &ldquo;kubernetes.io/hostname&rdquo;, each Node is a domain of that topology.
And, if TopologyKey is &ldquo;topology.kubernetes.io/zone&rdquo;, each zone is a domain of that topology.
It&rsquo;s a required field.</p>
</td>
</tr>
<tr>
<td>
<code>whenUnsatisfiable</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#unsatisfiableconstraintaction-v1-core">
Kubernetes core/v1.UnsatisfiableConstraintAction
</a>
</em>
</td>
<td>
<p>WhenUnsatisfiable indicates how to deal with a pod if it doesn&rsquo;t satisfy
the spread constraint.
- DoNotSchedule (default) tells the scheduler not to schedule it.
- ScheduleAnyway tells the scheduler to schedule the pod in any location,
but giving higher precedence to topologies that would help reduce the
skew.
A constraint is considered &ldquo;Unsatisfiable&rdquo; for an incoming pod
if and only if every possible node assignment for that pod would violate
&ldquo;MaxSkew&rdquo; on some topology.
For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same
labelSelector spread as 3/1/1:
| zone1 | zone2 | zone3 |
| P P P |   P   |   P   |
If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled
to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies
MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler
won&rsquo;t make it <em>more</em> imbalanced.
It&rsquo;s a required field.</p>
</td>
</tr>
<tr>
<td>
<code>labelSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>LabelSelector is used to find matching pods.
Pods that match this label selector are counted to determine the number of pods
in their corresponding topology domain.</p>
</td>
</tr>
<tr>
<td>
<code>minDomains</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>MinDomains indicates a minimum number of eligible domains.
When the number of eligible domains with matching topology keys is less than minDomains,
Pod Topology Spread treats &ldquo;global minimum&rdquo; as 0, and then the calculation of Skew is performed.
And when the number of eligible domains with matching topology keys equals or greater than minDomains,
this value has no effect on scheduling.
As a result, when the number of eligible domains is less than minDomains,
scheduler won&rsquo;t schedule more than maxSkew Pods to those domains.
If value is nil, the constraint behaves as if MinDomains is equal to 1.
Valid values are integers greater than 0.
When value is not nil, WhenUnsatisfiable must be DoNotSchedule.</p>
<p>For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same
labelSelector spread as 2/2/2:
| zone1 | zone2 | zone3 |
|  P P  |  P P  |  P P  |
The number of domains is less than 5(MinDomains), so &ldquo;global minimum&rdquo; is treated as 0.
In this situation, new pod with the same labelSelector cannot be scheduled,
because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones,
it will violate MaxSkew.</p>
</td>
</tr>
<tr>
<td>
<code>nodeAffinityPolicy</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#nodeinclusionpolicy-v1-core">
Kubernetes core/v1.NodeInclusionPolicy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>NodeAffinityPolicy indicates how we will treat Pod&rsquo;s nodeAffinity/nodeSelector
when calculating pod topology spread skew. Options are:
- Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations.
- Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.</p>
<p>If this value is nil, the behavior is equivalent to the Honor policy.</p>
</td>
</tr>
<tr>
<td>
<code>nodeTaintsPolicy</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#nodeinclusionpolicy-v1-core">
Kubernetes core/v1.NodeInclusionPolicy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>NodeTaintsPolicy indicates how we will treat node taints when calculating
pod topology spread skew. Options are:
- Honor: nodes without taints, along with tainted nodes for which the incoming pod
has a toleration, are included.
- Ignore: node taints are ignored. All nodes are included.</p>
<p>If this value is nil, the behavior is equivalent to the Ignore policy.</p>
</td>
</tr>
<tr>
<td>
<code>matchLabelKeys</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>MatchLabelKeys is a set of pod label keys to select the pods over which
spreading will be calculated. The keys are used to lookup values from the
incoming pod labels, those key-value labels are ANDed with labelSelector
to select the group of existing pods over which spreading will be calculated
for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector.
MatchLabelKeys cannot be set when LabelSelector isn&rsquo;t set.
Keys that don&rsquo;t exist in the incoming pod labels will
be ignored. A null or empty list means only match against labelSelector.</p>
<p>This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).</p>
</td>
</tr>
<tr>
<td>
<code>additionalLabelSelectors</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AdditionalLabelSelectors">
AdditionalLabelSelectors
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>additionalLabelSelectors Defines what Prometheus Operator managed labels should be added to labelSelector on the topologySpreadConstraint.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TracingConfig">TracingConfig
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
<code>clientType</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clientType defines the client used to export the traces. Supported values are <code>HTTP</code> and <code>GRPC</code>.</p>
</td>
</tr>
<tr>
<td>
<code>endpoint</code><br/>
<em>
string
</em>
</td>
<td>
<p>endpoint to send the traces to. Should be provided in format <host>:<port>.</p>
</td>
</tr>
<tr>
<td>
<code>samplingFraction</code><br/>
<em>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity">
k8s.io/apimachinery/pkg/api/resource.Quantity
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>samplingFraction defines the probability a given trace will be sampled. Must be a float from 0 through 1.</p>
</td>
</tr>
<tr>
<td>
<code>insecure</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>insecure if disabled, the client will use a secure connection.</p>
</td>
</tr>
<tr>
<td>
<code>headers</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>headers defines the key-value pairs to be used as headers associated with gRPC or HTTP requests.</p>
</td>
</tr>
<tr>
<td>
<code>compression</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>compression key for supported compression types. The only supported value is <code>Gzip</code>.</p>
</td>
</tr>
<tr>
<td>
<code>timeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>timeout defines the maximum time the exporter will wait for each batch export.</p>
</td>
</tr>
<tr>
<td>
<code>tlsConfig</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.TLSConfig">
TLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>tlsConfig to use when sending traces.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.TranslationStrategyOption">TranslationStrategyOption
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.OTLPConfig">OTLPConfig</a>)
</p>
<div>
<p>TranslationStrategyOption represents a translation strategy option for the OTLP endpoint.
Supported values are:
* <code>NoUTF8EscapingWithSuffixes</code>
* <code>UnderscoreEscapingWithSuffixes</code>
* <code>UnderscoreEscapingWithoutSuffixes</code>
* <code>NoTranslation</code></p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;NoTranslation&#34;</p></td>
<td><p>It requires Prometheus &gt;= v3.4.0.</p>
</td>
</tr><tr><td><p>&#34;NoUTF8EscapingWithSuffixes&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;UnderscoreEscapingWithSuffixes&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;UnderscoreEscapingWithoutSuffixes&#34;</p></td>
<td><p>It requires Prometheus &gt;= v3.6.0.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.URL">URL
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerGlobalConfig">AlertmanagerGlobalConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalJiraConfig">GlobalJiraConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalRocketChatConfig">GlobalRocketChatConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalTelegramConfig">GlobalTelegramConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalVictorOpsConfig">GlobalVictorOpsConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalWeChatConfig">GlobalWeChatConfig</a>, <a href="#monitoring.coreos.com/v1.GlobalWebexConfig">GlobalWebexConfig</a>, <a href="#monitoring.coreos.com/v1.OAuth2">OAuth2</a>, <a href="#monitoring.coreos.com/v1.RemoteReadSpec">RemoteReadSpec</a>, <a href="#monitoring.coreos.com/v1.RemoteWriteSpec">RemoteWriteSpec</a>)
</p>
<div>
<p>URL represents a valid URL</p>
</div>

<h3 id="monitoring.coreos.com/v1.WebConfigFileFields">WebConfigFileFields
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerWebSpec">AlertmanagerWebSpec</a>, <a href="#monitoring.coreos.com/v1.PrometheusWebSpec">PrometheusWebSpec</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerWebSpec">ThanosRulerWebSpec</a>)
</p>
<div>
<p>WebConfigFileFields defines the file content for &ndash;web.config.file flag.</p>
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

<h3 id="monitoring.coreos.com/v1.WebHTTPConfig">WebHTTPConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.WebConfigFileFields">WebConfigFileFields</a>)
</p>
<div>
<p>WebHTTPConfig defines HTTP parameters for web server.</p>
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
<code>http2</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>http2 enable HTTP/2 support. Note that HTTP/2 is only supported with TLS.
When TLSConfig is not configured, HTTP/2 will be disabled.
Whenever the value of the field changes, a rolling update will be triggered.</p>
</td>
</tr>
<tr>
<td>
<code>headers</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WebHTTPHeaders">
WebHTTPHeaders
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>headers defines a list of headers that can be added to HTTP responses.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.WebHTTPHeaders">WebHTTPHeaders
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.WebHTTPConfig">WebHTTPConfig</a>)
</p>
<div>
<p>WebHTTPHeaders defines the list of headers that can be added to HTTP responses.</p>
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
<code>contentSecurityPolicy</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>contentSecurityPolicy defines the Content-Security-Policy header to HTTP responses.
Unset if blank.</p>
</td>
</tr>
<tr>
<td>
<code>xFrameOptions</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>xFrameOptions defines the X-Frame-Options header to HTTP responses.
Unset if blank. Accepted values are deny and sameorigin.
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options</a></p>
</td>
</tr>
<tr>
<td>
<code>xContentTypeOptions</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>xContentTypeOptions defines the X-Content-Type-Options header to HTTP responses.
Unset if blank. Accepted value is nosniff.
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options</a></p>
</td>
</tr>
<tr>
<td>
<code>xXSSProtection</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>xXSSProtection defines the X-XSS-Protection header to all responses.
Unset if blank.
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection</a></p>
</td>
</tr>
<tr>
<td>
<code>strictTransportSecurity</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>strictTransportSecurity defines the Strict-Transport-Security header to HTTP responses.
Unset if blank.
Please make sure that you use this with care as this header might force
browsers to load Prometheus and the other applications hosted on the same
domain and subdomains over HTTPS.
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security</a></p>
</td>
</tr>
</tbody>
</table>
