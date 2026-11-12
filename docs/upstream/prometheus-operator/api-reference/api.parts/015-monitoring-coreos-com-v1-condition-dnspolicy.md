<!-- Part 15 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.Condition">Condition
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerStatus">AlertmanagerStatus</a>, <a href="#monitoring.coreos.com/v1.PrometheusStatus">PrometheusStatus</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerStatus">ThanosRulerStatus</a>)
</p>
<div>
<p>Condition represents the state of the resources associated with the
Prometheus, Alertmanager or ThanosRuler resource.</p>
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
<a href="#monitoring.coreos.com/v1.ConditionType">
ConditionType
</a>
</em>
</td>
<td>
<p>type of the condition being reported.</p>
</td>
</tr>
<tr>
<td>
<code>status</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ConditionStatus">
ConditionStatus
</a>
</em>
</td>
<td>
<p>status of the condition.</p>
</td>
</tr>
<tr>
<td>
<code>lastTransitionTime</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#time-v1-meta">
Kubernetes meta/v1.Time
</a>
</em>
</td>
<td>
<p>lastTransitionTime is the time of the last update to the current status property.</p>
</td>
</tr>
<tr>
<td>
<code>reason</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>reason for the condition&rsquo;s last transition.</p>
</td>
</tr>
<tr>
<td>
<code>message</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>message defines human-readable message indicating details for the condition&rsquo;s last transition.</p>
</td>
</tr>
<tr>
<td>
<code>observedGeneration</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>observedGeneration defines the .metadata.generation that the
condition was set based upon. For instance, if <code>.metadata.generation</code> is
currently 12, but the <code>.status.conditions[].observedGeneration</code> is 9, the
condition is out of date with respect to the current state of the
instance.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ConditionStatus">ConditionStatus
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Condition">Condition</a>, <a href="#monitoring.coreos.com/v1.ConfigResourceCondition">ConfigResourceCondition</a>)
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
<tbody><tr><td><p>&#34;Degraded&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;False&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;True&#34;</p></td>
<td></td>
</tr><tr><td><p>&#34;Unknown&#34;</p></td>
<td></td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ConditionType">ConditionType
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Condition">Condition</a>, <a href="#monitoring.coreos.com/v1.ConfigResourceCondition">ConfigResourceCondition</a>)
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
<tbody><tr><td><p>&#34;Accepted&#34;</p></td>
<td><p>Accepted indicates whether the workload controller has successfully accepted
the configuration resource and updated the configuration of the workload accordingly.
The possible status values for this condition type are:
- True: the configuration resource was successfully accepted by the controller and written to the configuration secret.
- False: the controller rejected the configuration due to an error.
- Unknown: the operator couldn&rsquo;t determine the condition status.</p>
</td>
</tr><tr><td><p>&#34;Available&#34;</p></td>
<td><p>Available indicates whether enough pods are ready to provide the
service.
The possible status values for this condition type are:
- True: all pods are running and ready, the service is fully available.
- Degraded: some pods aren&rsquo;t ready, the service is partially available.
- False: no pods are running, the service is totally unavailable.
- Unknown: the operator couldn&rsquo;t determine the condition status.</p>
</td>
</tr><tr><td><p>&#34;Reconciled&#34;</p></td>
<td><p>Reconciled indicates whether the operator has reconciled the state of
the underlying resources with the object&rsquo;s spec.
The possible status values for this condition type are:
- True: the reconciliation was successful.
- False: the reconciliation failed.
- Unknown: the operator couldn&rsquo;t determine the condition status.</p>
</td>
</tr></tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ConfigResourceCondition">ConfigResourceCondition
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.WorkloadBinding">WorkloadBinding</a>)
</p>
<div>
<p>ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler.</p>
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
<a href="#monitoring.coreos.com/v1.ConditionType">
ConditionType
</a>
</em>
</td>
<td>
<p>type of the condition being reported.
Currently, only &ldquo;Accepted&rdquo; is supported.</p>
</td>
</tr>
<tr>
<td>
<code>status</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ConditionStatus">
ConditionStatus
</a>
</em>
</td>
<td>
<p>status of the condition.</p>
</td>
</tr>
<tr>
<td>
<code>lastTransitionTime</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#time-v1-meta">
Kubernetes meta/v1.Time
</a>
</em>
</td>
<td>
<p>lastTransitionTime defines the time of the last update to the current status property.</p>
</td>
</tr>
<tr>
<td>
<code>reason</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>reason for the condition&rsquo;s last transition.</p>
</td>
</tr>
<tr>
<td>
<code>message</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>message defines the human-readable message indicating details for the condition&rsquo;s last transition.</p>
</td>
</tr>
<tr>
<td>
<code>observedGeneration</code><br/>
<em>
int64
</em>
</td>
<td>
<em>(Optional)</em>
<p>observedGeneration defines the .metadata.generation that the
condition was set based upon. For instance, if <code>.metadata.generation</code> is
currently 12, but the <code>.status.conditions[].observedGeneration</code> is 9, the
condition is out of date with respect to the current state of the object.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.ConfigResourceStatus">ConfigResourceStatus
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.PodMonitor">PodMonitor</a>, <a href="#monitoring.coreos.com/v1.Probe">Probe</a>, <a href="#monitoring.coreos.com/v1.PrometheusRule">PrometheusRule</a>, <a href="#monitoring.coreos.com/v1.ServiceMonitor">ServiceMonitor</a>, <a href="#monitoring.coreos.com/v1alpha1.AlertmanagerConfig">AlertmanagerConfig</a>, <a href="#monitoring.coreos.com/v1alpha1.ScrapeConfig">ScrapeConfig</a>, <a href="#monitoring.coreos.com/v1beta1.AlertmanagerConfig">AlertmanagerConfig</a>)
</p>
<div>
<p>ConfigResourceStatus is the most recent observed status of the Configuration Resource (ServiceMonitor, PodMonitor, Probes, ScrapeConfig, PrometheusRule or AlertmanagerConfig). Read-only.
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
<code>bindings</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WorkloadBinding">
[]WorkloadBinding
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource.</p>
</td>
</tr>
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.CoreV1TopologySpreadConstraint">CoreV1TopologySpreadConstraint
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.TopologySpreadConstraint">TopologySpreadConstraint</a>)
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
</tbody>
</table>

<h3 id="monitoring.coreos.com/v1.DNSPolicy">DNSPolicy
(<code>string</code> alias)</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>, <a href="#monitoring.coreos.com/v1.CommonPrometheusFields">CommonPrometheusFields</a>, <a href="#monitoring.coreos.com/v1.ThanosRulerSpec">ThanosRulerSpec</a>)
</p>
<div>
<p>DNSPolicy specifies the DNS policy for the pod.</p>
</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr><td><p>&#34;ClusterFirst&#34;</p></td>
<td><p>DNSClusterFirst defines that the pod should use cluster DNS
first unless hostNetwork is true, if it is available, then
fall back on the default (as determined by kubelet) DNS settings.</p>
</td>
</tr><tr><td><p>&#34;ClusterFirstWithHostNet&#34;</p></td>
<td><p>DNSClusterFirstWithHostNet defines that the pod should use cluster DNS
first, if it is available, then fall back on the default
(as determined by kubelet) DNS settings.</p>
</td>
</tr><tr><td><p>&#34;Default&#34;</p></td>
<td><p>DNSDefault defines that the pod should use the default (as
determined by kubelet) DNS settings.</p>
</td>
</tr><tr><td><p>&#34;None&#34;</p></td>
<td><p>DNSNone defines that the pod should use empty DNS settings. DNS
parameters such as nameservers and search paths should be defined via
DNSConfig.</p>
</td>
</tr></tbody>
</table>
