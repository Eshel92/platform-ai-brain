<!-- Part 8 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.ThanosRuler">ThanosRuler
</h3>
<div>
<p>The <code>ThanosRuler</code> custom resource definition (CRD) defines a desired <a href="https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md">Thanos Ruler</a> setup to run in a Kubernetes cluster.</p>
<p>A <code>ThanosRuler</code> instance requires at least one compatible Prometheus API endpoint (either Thanos Querier or Prometheus services).</p>
<p>The resource defines via label and namespace selectors which <code>PrometheusRule</code> objects should be associated to the deployed Thanos Ruler instances.</p>
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
<td><code>ThanosRuler</code></td>
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
<a href="#monitoring.coreos.com/v1.ThanosRulerSpec">
ThanosRulerSpec
</a>
</em>
</td>
<td>
<p>spec defines the specification of the desired behavior of the ThanosRuler cluster. More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
<br/>
<br/>
<table>
<tr>
<td>
<code>version</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>version of Thanos to be deployed.</p>
</td>
</tr>
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
<p>podMetadata defines labels and annotations which are propagated to the ThanosRuler pods.</p>
<p>The following items are reserved and cannot be overridden:
* &ldquo;app.kubernetes.io/name&rdquo; label, set to &ldquo;thanos-ruler&rdquo;.
* &ldquo;app.kubernetes.io/managed-by&rdquo; label, set to &ldquo;prometheus-operator&rdquo;.
* &ldquo;app.kubernetes.io/instance&rdquo; label, set to the name of the ThanosRuler instance.
* &ldquo;thanos-ruler&rdquo; label, set to the name of the ThanosRuler instance.
* &ldquo;kubectl.kubernetes.io/default-container&rdquo; annotation, set to &ldquo;thanos-ruler&rdquo;.</p>
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
<p>image defines Thanos container image URL.</p>
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
<p>imagePullPolicy defines for the &lsquo;thanos&rsquo;, &lsquo;init-config-reloader&rsquo; and &lsquo;config-reloader&rsquo; containers.
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
<p>imagePullSecrets defines an optional list of references to secrets in the same namespace
to use for pulling thanos images from registries
see <a href="http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod">http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod</a></p>
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
<p>paused defines when a ThanosRuler deployment is paused, no actions except for deletion
will be performed on the underlying objects.</p>
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
<p>replicas defines the number of thanos ruler instances to deploy.</p>
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
<p>nodeSelector defines which Nodes the Pods are scheduled on.</p>
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
<code>resources</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core">
Kubernetes core/v1.ResourceRequirements
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>resources defines the resource requirements for single Pods.
If not provided, no requests/limits will be set</p>
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
<p>affinity defines when specified, the pod&rsquo;s scheduling constraints.</p>
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
<p>tolerations defines when specified, the pod&rsquo;s tolerations.</p>
</td>
</tr>
<tr>
<td>
<code>topologySpreadConstraints</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#topologyspreadconstraint-v1-core">
[]Kubernetes core/v1.TopologySpreadConstraint
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>topologySpreadConstraints defines the pod&rsquo;s topology spread constraints.</p>
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
<p>securityContext defines the pod-level security attributes and common container settings.
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
<p>dnsConfig defines Defines the DNS configuration for the pods.</p>
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
<code>priorityClassName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>priorityClassName defines the priority class assigned to the Pods</p>
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
If defined, the Service  must be created before the ThanosRuler resource in the same namespace and it must define a selector that matches the pod labels.
If empty, the operator will create and manage a headless service named <code>thanos-ruler-operated</code> for ThanosRuler resources.
When deploying multiple ThanosRuler resources in the same namespace, it is recommended to specify a different value for each.
See <a href="https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-id">https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-id</a> for more details.</p>
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
<p>serviceAccountName defines the name of the ServiceAccount to use to run the
Thanos Ruler Pods.</p>
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
<p>storage defines the specification of how storage shall be used.</p>
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
<p>volumes defines how configuration of additional volumes on the output StatefulSet definition. Volumes specified will
be appended to other volumes that are generated as a result of StorageSpec objects.</p>
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
<p>volumeMounts defines how the configuration of additional VolumeMounts on the output StatefulSet definition.
VolumeMounts specified will be appended to other VolumeMounts in the ruler container,
that are generated as a result of StorageSpec objects.</p>
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
<p>objectStorageConfig defines the configuration format is defined at <a href="https://thanos.io/tip/thanos/storage.md/#configuring-access-to-object-storage">https://thanos.io/tip/thanos/storage.md/#configuring-access-to-object-storage</a></p>
<p>The operator performs no validation of the configuration.</p>
<p><code>objectStorageConfigFile</code> takes precedence over this field.</p>
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
<p>objectStorageConfigFile defines the path of the object storage configuration file.</p>
<p>The configuration format is defined at <a href="https://thanos.io/tip/thanos/storage.md/#configuring-access-to-object-storage">https://thanos.io/tip/thanos/storage.md/#configuring-access-to-object-storage</a></p>
<p>The operator performs no validation of the configuration file.</p>
<p>This field takes precedence over <code>objectStorageConfig</code>.</p>
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
<p>listenLocal defines the Thanos ruler listen on loopback, so that it
does not bind against the Pod IP.</p>
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
<code>queryEndpoints</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>queryEndpoints defines the list of Thanos Query endpoints from which to query metrics.</p>
<p>For Thanos &gt;= v0.11.0, it is recommended to use <code>queryConfig</code> instead.</p>
<p><code>queryConfig</code> takes precedence over this field.</p>
</td>
</tr>
<tr>
<td>
<code>queryConfig</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>queryConfig defines the list of Thanos Query endpoints from which to query metrics.</p>
<p>The configuration format is defined at <a href="https://thanos.io/tip/components/rule.md/#query-api">https://thanos.io/tip/components/rule.md/#query-api</a></p>
<p>It requires Thanos &gt;= v0.11.0.</p>
<p>The operator performs no validation of the configuration.</p>
<p>This field takes precedence over <code>queryEndpoints</code>.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagersUrl</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagersUrl defines the list of Alertmanager endpoints to send alerts to.</p>
<p>For Thanos &gt;= v0.10.0, it is recommended to use <code>alertmanagersConfig</code> instead.</p>
<p><code>alertmanagersConfig</code> takes precedence over this field.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagersConfig</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagersConfig defines the list of Alertmanager endpoints to send alerts to.</p>
<p>The configuration format is defined at <a href="https://thanos.io/tip/components/rule.md/#alertmanager">https://thanos.io/tip/components/rule.md/#alertmanager</a>.</p>
<p>It requires Thanos &gt;= v0.10.0.</p>
<p>The operator performs no validation of the configuration.</p>
<p>This field takes precedence over <code>alertmanagersUrl</code>.</p>
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
<p>ruleSelector defines the PrometheusRule objects to be selected for rule evaluation. An empty
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
<p>ruleNamespaceSelector defines the namespaces to be selected for Rules discovery. If unspecified, only
the same namespace as the ThanosRuler object is in is used.</p>
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
<p>enforcedNamespaceLabel enforces adding a namespace label of origin for each alert
and metric that is user created. The label value will always be the namespace of the object that is
being created.</p>
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
<p>excludedFromEnforcement defines the list of references to PrometheusRule objects
to be excluded from enforcing a namespace label of origin.
Applies only if enforcedNamespaceLabel set to true.</p>
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
<p>prometheusRulesExcludedFromEnforce defines a list of Prometheus rules to be excluded from enforcing
of adding namespace labels. Works only if enforcedNamespaceLabel set to true.
Make sure both ruleNamespace and ruleName are set for each pair
Deprecated: use excludedFromEnforcement instead.</p>
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
<p>logLevel for ThanosRuler to be configured with.</p>
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
<p>logFormat for ThanosRuler to be configured with.</p>
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
<p>portName defines the port name used for the pods and governing service.
Defaults to <code>web</code>.</p>
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
<p>evaluationInterval defines the interval between consecutive evaluations.</p>
</td>
</tr>
<tr>
<td>
<code>resendDelay</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>resendDelay defines the minimum amount of time to wait before resending an alert to Alertmanager.</p>
</td>
</tr>
<tr>
<td>
<code>ruleOutageTolerance</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ruleOutageTolerance defines the max time to tolerate prometheus outage for restoring &ldquo;for&rdquo; state of alert.
It requires Thanos &gt;= v0.30.0.</p>
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
<p>ruleQueryOffset defines the default rule group&rsquo;s query offset duration to use.
It requires Thanos &gt;= v0.38.0.</p>
</td>
</tr>
<tr>
<td>
<code>ruleConcurrentEval</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>ruleConcurrentEval defines how many rules can be evaluated concurrently.
It requires Thanos &gt;= v0.37.0.</p>
</td>
</tr>
<tr>
<td>
<code>ruleGracePeriod</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.Duration">
Duration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>ruleGracePeriod defines the minimum duration between alert and restored &ldquo;for&rdquo; state.
This is maintained only for alerts with configured &ldquo;for&rdquo; time greater than grace period.
It requires Thanos &gt;= v0.30.0.</p>
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
<p>retention defines the time duration ThanosRuler shall retain data for. Default is &lsquo;24h&rsquo;, and
must match the regular expression <code>[0-9]+(ms|s|m|h|d|w|y)</code> (milliseconds
seconds minutes hours days weeks years).</p>
<p>The field has no effect when remote-write is configured since the Ruler
operates in stateless mode.</p>
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
* <code>thanos-ruler</code>
* <code>config-reloader</code></p>
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
<p>initContainers allows injecting initContainers to the Pod definition.
Those can be used to e.g. fetch secrets for injection into the
configuration from external sources. Any errors during the execution of
an initContainer will lead to a restart of the Pod. More info:
<a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/">https://kubernetes.io/docs/concepts/workloads/pods/init-containers/</a></p>
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
<p>tracingConfig defines the tracing configuration.</p>
<p>The configuration format is defined at <a href="https://thanos.io/tip/thanos/tracing.md/#configuration">https://thanos.io/tip/thanos/tracing.md/#configuration</a></p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
<p>The operator performs no validation of the configuration.</p>
<p><code>tracingConfigFile</code> takes precedence over this field.</p>
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
<p>tracingConfigFile defines the path of the tracing configuration file.</p>
<p>The configuration format is defined at <a href="https://thanos.io/tip/thanos/tracing.md/#configuration">https://thanos.io/tip/thanos/tracing.md/#configuration</a></p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
<p>The operator performs no validation of the configuration file.</p>
<p>This field takes precedence over <code>tracingConfig</code>.</p>
</td>
</tr>
<tr>
<td>
<code>labels</code><br/>
<em>
map[string]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>labels defines the external label pairs of the ThanosRuler resource.</p>
<p>A default replica label <code>thanos_ruler_replica</code> will be always added as a
label with the value of the pod&rsquo;s name.</p>
</td>
</tr>
<tr>
<td>
<code>alertDropLabels</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertDropLabels defines the label names which should be dropped in Thanos Ruler
alerts.</p>
<p>The replica label <code>thanos_ruler_replica</code> will always be dropped from the alerts.</p>
</td>
</tr>
<tr>
<td>
<code>externalPrefix</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>externalPrefix defines the Thanos Ruler instances will be available under. This is
necessary to generate correct URLs. This is necessary if Thanos Ruler is not
served from root of a DNS name.</p>
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
<p>routePrefix defines the route prefix ThanosRuler registers HTTP handlers for. This allows thanos UI to be served on a sub-path.</p>
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
<p>grpcServerTlsConfig defines the gRPC server from which Thanos Querier reads
recorded rule data.</p>
<p>Note: Currently only the <code>minVersion</code>, <code>caFile</code>, <code>certFile</code>, <code>keyFile</code>, <code>cipherSuites</code> and <code>curves</code> fields are supported.</p>
</td>
</tr>
<tr>
<td>
<code>alertQueryUrl</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertQueryUrl defines how Thanos Ruler will set in the &lsquo;Source&rsquo; field
of all alerts.
Maps to the &lsquo;&ndash;alert.query-url&rsquo; CLI arg.</p>
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
<p>minReadySeconds defines the minimum number of seconds for which a newly created pod should be ready
without any of its container crashing for it to be considered available.</p>
<p>If unset, pods will be considered available as soon as they are ready.</p>
</td>
</tr>
<tr>
<td>
<code>alertRelabelConfigs</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#secretkeyselector-v1-core">
Kubernetes core/v1.SecretKeySelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertRelabelConfigs defines the alert relabeling in Thanos Ruler.</p>
<p>Alert relabel configuration must have the form as specified in the
official Prometheus documentation:
<a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs</a></p>
<p>The operator performs no validation of the configuration.</p>
<p><code>alertRelabelConfigFile</code> takes precedence over this field.</p>
</td>
</tr>
<tr>
<td>
<code>alertRelabelConfigFile</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertRelabelConfigFile defines the path to the alert relabeling configuration file.</p>
<p>Alert relabel configuration must have the form as specified in the
official Prometheus documentation:
<a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs">https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs</a></p>
<p>The operator performs no validation of the configuration file.</p>
<p>This field takes precedence over <code>alertRelabelConfig</code>.</p>
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
<p>hostAliases defines pods&rsquo; hostAliases configuration</p>
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
<p>additionalArgs defines how to add additional arguments for the ThanosRuler container.
It is intended for e.g. activating hidden flags which are not supported by
the dedicated configuration options yet. The arguments are passed as-is to the
ThanosRuler container which may cause issues if they are invalid or not supported
by the given ThanosRuler version.
In case of an argument conflict (e.g. an argument which is already set by the
operator itself) or when providing an invalid argument the reconciliation will
fail and an error will be logged.</p>
</td>
</tr>
<tr>
<td>
<code>web</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ThanosRulerWebSpec">
ThanosRulerWebSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>web defines the configuration of the ThanosRuler web server.</p>
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
<p>When the list isn&rsquo;t empty, the ruler is configured with stateless mode.</p>
<p>It requires Thanos &gt;= 0.24.0.</p>
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
<p>Defaults to 120 seconds.</p>
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
<p>enableFeatures defines how to setup Thanos Ruler feature flags. By default, no features are enabled.</p>
<p>Enabling features which are disabled by default is entirely outside the
scope of what the maintainers will support and by doing so, you accept
that this behaviour may break at any time without notice.</p>
<p>For more information see <a href="https://thanos.io/tip/components/rule.md/">https://thanos.io/tip/components/rule.md/</a></p>
<p>It requires Thanos &gt;= 0.39.0.</p>
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
</table>
</td>
</tr>
<tr>
<td>
<code>status</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ThanosRulerStatus">
ThanosRulerStatus
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>status defines the most recent observed status of the ThanosRuler cluster. Read-only.
More info:
<a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status">https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</a></p>
</td>
</tr>
</tbody>
</table>
