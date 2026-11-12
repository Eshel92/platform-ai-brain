<!-- Part 11 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.Alertmanager">Alertmanager</a>)
</p>
<div>
<p>AlertmanagerSpec is a specification of the desired behavior of the Alertmanager cluster. More info:
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
<p>podMetadata defines labels and annotations which are propagated to the Alertmanager pods.</p>
<p>The following items are reserved and cannot be overridden:
* &ldquo;alertmanager&rdquo; label, set to the name of the Alertmanager instance.
* &ldquo;app.kubernetes.io/instance&rdquo; label, set to the name of the Alertmanager instance.
* &ldquo;app.kubernetes.io/managed-by&rdquo; label, set to &ldquo;prometheus-operator&rdquo;.
* &ldquo;app.kubernetes.io/name&rdquo; label, set to &ldquo;alertmanager&rdquo;.
* &ldquo;app.kubernetes.io/version&rdquo; label, set to the Alertmanager version.
* &ldquo;kubectl.kubernetes.io/default-container&rdquo; annotation, set to &ldquo;alertmanager&rdquo;.</p>
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
<p>image if specified has precedence over baseImage, tag and sha
combinations. Specifying the version is still necessary to ensure the
Prometheus Operator knows what version of Alertmanager is being
configured.</p>
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
<p>imagePullPolicy for the &lsquo;alertmanager&rsquo;, &lsquo;init-config-reloader&rsquo; and &lsquo;config-reloader&rsquo; containers.
See <a href="https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy">https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy</a> for more details.</p>
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
<p>version the cluster should be on.</p>
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
<p>tag of Alertmanager container image to be deployed. Defaults to the value of <code>version</code>.
Version is ignored if Tag is set.
Deprecated: use &lsquo;image&rsquo; instead. The image tag can be specified as part of the image URL.</p>
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
<p>sha of Alertmanager container image to be deployed. Defaults to the value of <code>version</code>.
Similar to a tag, but the SHA explicitly deploys an immutable container image.
Version and Tag are ignored if SHA is set.
Deprecated: use &lsquo;image&rsquo; instead. The image digest can be specified as part of the image URL.</p>
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
<p>baseImage that is used to deploy pods, without tag.
Deprecated: use &lsquo;image&rsquo; instead.</p>
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
<p>imagePullSecrets An optional list of references to secrets in the same namespace
to use for pulling prometheus and alertmanager images from registries
see <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/">https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/</a></p>
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
<p>secrets is a list of Secrets in the same namespace as the Alertmanager
object, which shall be mounted into the Alertmanager Pods.
Each Secret is added to the StatefulSet definition as a volume named <code>secret-&lt;secret-name&gt;</code>.
The Secrets are mounted into <code>/etc/alertmanager/secrets/&lt;secret-name&gt;</code> in the &lsquo;alertmanager&rsquo; container.</p>
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
<p>configMaps defines a list of ConfigMaps in the same namespace as the Alertmanager
object, which shall be mounted into the Alertmanager Pods.
Each ConfigMap is added to the StatefulSet definition as a volume named <code>configmap-&lt;configmap-name&gt;</code>.
The ConfigMaps are mounted into <code>/etc/alertmanager/configmaps/&lt;configmap-name&gt;</code> in the &lsquo;alertmanager&rsquo; container.</p>
</td>
</tr>
<tr>
<td>
<code>configSecret</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>configSecret defines the name of a Kubernetes Secret in the same namespace as the
Alertmanager object, which contains the configuration for this Alertmanager
instance. If empty, it defaults to <code>alertmanager-&lt;alertmanager-name&gt;</code>.</p>
<p>The Alertmanager configuration should be available under the
<code>alertmanager.yaml</code> key. Additional keys from the original secret are
copied to the generated secret and mounted into the
<code>/etc/alertmanager/config</code> directory in the <code>alertmanager</code> container.</p>
<p>If either the secret or the <code>alertmanager.yaml</code> key is missing, the
operator provisions a minimal Alertmanager configuration with one empty
receiver (effectively dropping alert notifications).</p>
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
<p>logLevel for Alertmanager to be configured with.</p>
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
<p>logFormat for Alertmanager to be configured with.</p>
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
<p>replicas defines the expected size of the alertmanager cluster. The controller will
eventually make the size of the running cluster equal to the expected
size.</p>
</td>
</tr>
<tr>
<td>
<code>retention</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GoDuration">
GoDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>retention defines the time duration Alertmanager shall retain data for. Default is &lsquo;120h&rsquo;,
and must match the regular expression <code>[0-9]+(ms|s|m|h)</code> (milliseconds seconds minutes hours).</p>
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
<p>storage defines the definition of how storage will be used by the Alertmanager
instances.</p>
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
<p>volumes allows configuration of additional volumes on the output StatefulSet definition.
Volumes specified will be appended to other volumes that are generated as a result of
StorageSpec objects.</p>
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
<p>volumeMounts allows configuration of additional VolumeMounts on the output StatefulSet definition.
VolumeMounts specified will be appended to other VolumeMounts in the alertmanager container,
that are generated as a result of StorageSpec objects.</p>
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
<p>persistentVolumeClaimRetentionPolicy controls if and how PVCs are deleted during the lifecycle of a StatefulSet.
The default behavior is all PVCs are retained.
This is an alpha field from kubernetes 1.23 until 1.26 and a beta field from 1.26.
It requires enabling the StatefulSetAutoDeletePVC feature gate.</p>
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
<p>externalUrl defines the URL used to access the Alertmanager web service. This is
necessary to generate correct URLs. This is necessary if Alertmanager is not
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
<p>routePrefix Alertmanager registers HTTP handlers for. This is useful,
if using ExternalURL and a proxy is rewriting HTTP routes of a request,
and the actual ExternalURL is still true, but the server serves requests
under a different route prefix. For example for use with <code>kubectl proxy</code>.</p>
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
<p>paused if set to true all actions on the underlying managed objects are not
going to be performed, except for delete actions.</p>
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
<p>resources defines the resource requests and limits of the Pods.</p>
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
<p>affinity defines the pod&rsquo;s scheduling constraints.</p>
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
<p>tolerations defines the pod&rsquo;s tolerations.</p>
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
<p>topologySpreadConstraints defines the Pod&rsquo;s topology spread constraints.</p>
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
<code>serviceName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>serviceName defines the service name used by the underlying StatefulSet(s) as the governing service.
If defined, the Service  must be created before the Alertmanager resource in the same namespace and it must define a selector that matches the pod labels.
If empty, the operator will create and manage a headless service named <code>alertmanager-operated</code> for Alertmanager resources.
When deploying multiple Alertmanager resources in the same namespace, it is recommended to specify a different value for each.
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
<p>serviceAccountName is the name of the ServiceAccount to use to run the
Prometheus Pods.</p>
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
<p>listenLocal defines the Alertmanager server listen on loopback, so that it
does not bind against the Pod IP. Note this is only for the Alertmanager
UI, not the gossip communication.</p>
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
* <code>alertmanager</code>
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
can be used to e.g.  fetch secrets for injection into the Prometheus
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
<code>priorityClassName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>priorityClassName assigned to the Pods</p>
</td>
</tr>
<tr>
<td>
<code>additionalPeers</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>additionalPeers allows injecting a set of additional Alertmanagers to peer with to form a highly available cluster.</p>
</td>
</tr>
<tr>
<td>
<code>clusterAdvertiseAddress</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterAdvertiseAddress defines the explicit address to advertise in cluster.
Needs to be provided for non RFC1918 <a href="public">1</a> addresses.
[1] RFC1918: <a href="https://tools.ietf.org/html/rfc1918">https://tools.ietf.org/html/rfc1918</a></p>
</td>
</tr>
<tr>
<td>
<code>clusterGossipInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GoDuration">
GoDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterGossipInterval defines the interval between gossip attempts.</p>
</td>
</tr>
<tr>
<td>
<code>clusterLabel</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterLabel defines the identifier that uniquely identifies the Alertmanager cluster.
You should only set it when the Alertmanager cluster includes Alertmanager instances which are external to this Alertmanager resource. In practice, the addresses of the external instances are provided via the <code>.spec.additionalPeers</code> field.</p>
</td>
</tr>
<tr>
<td>
<code>clusterPushpullInterval</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GoDuration">
GoDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterPushpullInterval defines the interval between pushpull attempts.</p>
</td>
</tr>
<tr>
<td>
<code>clusterPeerTimeout</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.GoDuration">
GoDuration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterPeerTimeout defines the timeout for cluster peering.</p>
</td>
</tr>
<tr>
<td>
<code>clusterPeerName</code><br/>
<em>
string
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterPeerName defines the name that this Alertmanager instance uses to
advertise itself to other cluster peers (the <code>--cluster.peer-name</code> flag,
available since Alertmanager v0.30.0).</p>
<p>If not set, the operator defaults to the pod&rsquo;s name (<code>$(POD_NAME)</code>),
which is injected via the Kubernetes downward API. Setting this field
lets you override that default with either a literal value or a string
referencing environment variables that are already available in the
Alertmanager container (for example <code>$(POD_NAME).$(NAMESPACE)</code>).</p>
<p>/ It requires Alertmanager &gt;= 0.30.0.</p>
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
<p>portName defines the port&rsquo;s name for the pods and governing service.
Defaults to <code>web</code>.</p>
</td>
</tr>
<tr>
<td>
<code>forceEnableClusterMode</code><br/>
<em>
bool
</em>
</td>
<td>
<em>(Optional)</em>
<p>forceEnableClusterMode ensures Alertmanager does not deactivate the cluster mode when running with a single replica.
Use case is e.g. spanning an Alertmanager cluster across Kubernetes clusters with a single replica in each.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagerConfigSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagerConfigSelector defines the selector to be used for to merge and configure Alertmanager with.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagerConfigNamespaceSelector</code><br/>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#labelselector-v1-meta">
Kubernetes meta/v1.LabelSelector
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagerConfigNamespaceSelector defines the namespaces to be selected for AlertmanagerConfig discovery. If nil, only
check own namespace.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagerConfigMatcherStrategy</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerConfigMatcherStrategy">
AlertmanagerConfigMatcherStrategy
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagerConfigMatcherStrategy defines how AlertmanagerConfig objects
process incoming alerts.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagerConfigFileSystemMode</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerConfigFileSystemMode">
AlertmanagerConfigFileSystemMode
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagerConfigFileSystemMode defines how the operator handles
AlertmanagerConfig resources which have references to the Alertmanager
container&rsquo;s filesystem (as opposed to secret key references). Users
controlling the receiver&rsquo;s service may create an AlertmanagerConfig
resource with a reference to a container&rsquo;s file (for instance using
<code>botTokenFile</code> for the Telegram receiver) and exfiltrate sensitive
content from files located in the Alertmanager container.</p>
<p>Supported values are:
- &ldquo;DenyAll&rdquo; denies any AlertmanagerConfig resource referencing files from the container&rsquo;s filesystem, non-compliant resources are rejected.
- &ldquo;FromAlertmanagerConfigMatcherStrategy&rdquo; uses the <code>alertmanagerConfigNamespaceSelector</code> field to make a decision
- When <code>alertmanagerConfigNamespaceSelector</code> is &ldquo;None&rdquo;, it is equivalent to &ldquo;AllowAll&rdquo;
- When <code>alertmanagerConfigNamespaceSelector</code> is &ldquo;OnNamespaceExceptForAlertmanagerNamespace&rdquo;, it is equivalent to &ldquo;AllowAll&rdquo; for the AlertmanagerConfig resources located in the Alertmanager&rsquo;s namespace and &ldquo;DenyAll&rdquo; for all other resources.
- When <code>alertmanagerConfigNamespaceSelector</code> is &ldquo;OnNamespace&rdquo;, it is equivalent to &ldquo;AllowAll&rdquo; for the main AlertmanagerConfig resource (defined in <code>.spec.alertmanagerConfig.name</code>) and &ldquo;DenyAll&rdquo; for all other resources.
- &ldquo;AllowAll&rdquo; allows any AlertmanagerConfig resource to reference files from the container&rsquo;s filesystem (use with caution).</p>
<p>By default, the operator uses the &ldquo;FromAlertmanagerConfigMatcherStrategy&rdquo; mode.</p>
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
<p>minReadySeconds defines the minimum number of seconds for which a newly
created pod should be ready without any of its container crashing for it
to be considered available.</p>
<p>If unset, pods will be considered available as soon as they are ready.</p>
<p>When the Alertmanager version is greater than or equal to v0.30.0, the
duration is also used to delay the first flush of the aggregation
groups. This delay helps ensuring that all alerts have been resent by
the Prometheus instances to Alertmanager after a roll-out. It is
possible to override this behavior passing a custom value via
<code>.spec.additionalArgs</code>.</p>
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
<p>hostAliases Pods configuration</p>
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
<p>hostNetwork controls whether the pod may use the node network namespace.</p>
<p>Make sure to understand the security implications if you want to enable
it (<a href="https://kubernetes.io/docs/concepts/configuration/overview/">https://kubernetes.io/docs/concepts/configuration/overview/</a>).</p>
<p>When hostNetwork is enabled, this will set the DNS policy to
<code>ClusterFirstWithHostNet</code> automatically (unless <code>.spec.dnsPolicy</code> is set
to a different value).</p>
</td>
</tr>
<tr>
<td>
<code>web</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerWebSpec">
AlertmanagerWebSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>web defines the web command line flags when starting Alertmanager.</p>
</td>
</tr>
<tr>
<td>
<code>limits</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerLimitsSpec">
AlertmanagerLimitsSpec
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>limits defines the limits command line flags when starting Alertmanager.</p>
</td>
</tr>
<tr>
<td>
<code>clusterTLS</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ClusterTLSConfig">
ClusterTLSConfig
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>clusterTLS defines the mutual TLS configuration for the Alertmanager cluster&rsquo;s gossip protocol.</p>
<p>It requires Alertmanager &gt;= 0.24.0.</p>
</td>
</tr>
<tr>
<td>
<code>alertmanagerConfiguration</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.AlertmanagerConfiguration">
AlertmanagerConfiguration
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>alertmanagerConfiguration defines the configuration of Alertmanager.</p>
<p>If defined, it takes precedence over the <code>configSecret</code> field.</p>
<p>This is an <em>experimental feature</em>, it may change in any upcoming release
in a breaking way.</p>
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
If the service account has <code>automountServiceAccountToken: true</code>, set the field to <code>false</code> to opt out of automounting API credentials.</p>
</td>
</tr>
<tr>
<td>
<code>enableFeatures</code><br/>
<em>
[]string
</em>
</td>
<td>
<em>(Optional)</em>
<p>enableFeatures defines the Alertmanager&rsquo;s feature flags. By default, no features are enabled.
Enabling features which are disabled by default is entirely outside the
scope of what the maintainers will support and by doing so, you accept
that this behaviour may break at any time without notice.</p>
<p>It requires Alertmanager &gt;= 0.27.0.</p>
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
<p>additionalArgs allows setting additional arguments for the &lsquo;Alertmanager&rsquo; container.
It is intended for e.g. activating hidden flags which are not supported by
the dedicated configuration options yet. The arguments are passed as-is to the
Alertmanager container which may cause issues if they are invalid or not supported
by the given Alertmanager version.</p>
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
<p>terminationGracePeriodSeconds defines the Optional duration in seconds the pod needs to terminate gracefully.
Value must be non-negative integer. The value zero indicates stop immediately via
the kill signal (no opportunity to shut down) which may lead to data corruption.</p>
<p>Defaults to 120 seconds.</p>
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
</tbody>
</table>
