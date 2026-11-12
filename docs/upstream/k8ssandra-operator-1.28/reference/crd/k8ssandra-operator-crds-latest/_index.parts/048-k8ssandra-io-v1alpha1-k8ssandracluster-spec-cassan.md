<!-- Part 48 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.metadata
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargate)</sup></sup>



labels and annotations for Stargate resources

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotations</b></td>
        <td>map[string]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commonAnnotations</b></td>
        <td>map[string]string</td>
        <td>
          annotations that will be applied to all components
created by the CRD<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commonLabels</b></td>
        <td>map[string]string</td>
        <td>
          labels/annotations that will be applied to all components
created by the CRD<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargatemetadatapods">pods</a></b></td>
        <td>object</td>
        <td>
          labels/annotations for the pod components<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargatemetadataservice">service</a></b></td>
        <td>object</td>
        <td>
          labels/annotations for the service component<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.metadata.pods
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargatemetadata)</sup></sup>



labels/annotations for the pod components

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotations</b></td>
        <td>map[string]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.metadata.service
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargatemetadata)</sup></sup>



labels/annotations for the service component

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotations</b></td>
        <td>map[string]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargate)</sup></sup>



StargateRackTemplate defines custom rules for Stargate pods in a given rack.
These rules will be merged with rules defined at datacenter level in a StargateDatacenterTemplate; rack-level rules
have precedence over datacenter-level ones.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the rack name. It must correspond to an existing rack name in the CassandraDatacenter resource where
Stargate is being deployed, otherwise it will be ignored.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinity">affinity</a></b></td>
        <td>object</td>
        <td>
          Affinity is the affinity to apply to all the Stargate pods.
Leave nil to let the controller reuse the same affinity rules used for data pods in this datacenter, if any.
See https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>allowStargateOnDataNodes</b></td>
        <td>boolean</td>
        <td>
          AllowStargateOnDataNodes allows Stargate pods to be scheduled on a worker node already hosting data pods for this
datacenter. The default is false, which means that Stargate pods will be scheduled on separate worker nodes.
Note: if the datacenter pods have HostNetwork:true, then the Stargate pods will inherit of it, in which case it
is possible that Stargate nodes won't be allowed to sit on data nodes even if this property is set to true,
because of port conflicts on the same IP address.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexauthoptions">authOptions</a></b></td>
        <td>object</td>
        <td>
          Authentication options.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexcassandraconfigmapref">cassandraConfigMapRef</a></b></td>
        <td>object</td>
        <td>
          CassandraConfigMapRef is a reference to a ConfigMap that holds Cassandra configuration.
The map should have a key named cassandra_yaml.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexcontainerimage">containerImage</a></b></td>
        <td>object</td>
        <td>
          ContainerImage is the image characteristics to use for Stargate containers. Leave nil
to use a default image.<br/>
          <br/>
            <i>Default</i>: map[repository:stargateio tag:v1.0.77]<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>heapSize</b></td>
        <td>int or string</td>
        <td>
          HeapSize sets the JVM heap size to use for Stargate. If no Resources are specified, this
value will also be used to set a default memory request and limit for the Stargate pods:
these will be set to HeapSize x2 and x4, respectively.<br/>
          <br/>
            <i>Default</i>: 256Mi<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexlivenessprobe">livenessProbe</a></b></td>
        <td>object</td>
        <td>
          LivenessProbe sets the Stargate liveness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexmetadata">metadata</a></b></td>
        <td>object</td>
        <td>
          labels and annotations for Stargate resources<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nodeSelector</b></td>
        <td>map[string]string</td>
        <td>
          NodeSelector is an optional map of label keys and values to restrict the scheduling of Stargate nodes to workers
with matching labels.
Leave nil to let the controller reuse the same node selectors used for data pods in this datacenter, if any.
See https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexreadinessprobe">readinessProbe</a></b></td>
        <td>object</td>
        <td>
          ReadinessProbe sets the Stargate readiness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexresources">resources</a></b></td>
        <td>object</td>
        <td>
          Resources is the Kubernetes resource requests and limits to apply, per Stargate pod. Leave
nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretsProvider</b></td>
        <td>enum</td>
        <td>
          SecretsProvider defines whether the secrets used for credentials and certs will be backed
by an external secret backend. This moves the responsibility of generating and storing
secrets from the operators to the user and will rely on a mutating webhook to inject
the secrets into the necessary resources<br/>
          <br/>
            <i>Enum</i>: internal, external<br/>
            <i>Default</i>: internal<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccount</b></td>
        <td>string</td>
        <td>
          ServiceAccount is the service account name to use for Stargate pods.<br/>
          <br/>
            <i>Default</i>: default<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetry">telemetry</a></b></td>
        <td>object</td>
        <td>
          Telemetry defines the desired telemetry integrations to deploy targeting the Stargate pods for all DCs in this cluster
(unless overridden by DC specific settings)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations are tolerations to apply to the Stargate pods.
Leave nil to let the controller reuse the same tolerations used for data pods in this datacenter, if any.
See https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].affinity
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindex)</sup></sup>



Affinity is the affinity to apply to all the Stargate pods.
Leave nil to let the controller reuse the same affinity rules used for data pods in this datacenter, if any.
See https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinity">nodeAffinity</a></b></td>
        <td>object</td>
        <td>
          Describes node affinity scheduling rules for the pod.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitypodaffinity">podAffinity</a></b></td>
        <td>object</td>
        <td>
          Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitypodantiaffinity">podAntiAffinity</a></b></td>
        <td>object</td>
        <td>
          Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].affinity.nodeAffinity
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinity)</sup></sup>



Describes node affinity scheduling rules for the pod.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindex">preferredDuringSchedulingIgnoredDuringExecution</a></b></td>
        <td>[]object</td>
        <td>
          The scheduler will prefer to schedule pods to nodes that satisfy
the affinity expressions specified by this field, but it may choose
a node that violates one or more of the expressions. The node that is
most preferred is the one with the greatest sum of weights, i.e.
for each node that meets all of the scheduling requirements (resource
request, requiredDuringScheduling affinity expressions, etc.),
compute a sum by iterating through the elements of this field and adding
"weight" to the sum if the node matches the corresponding matchExpressions; the
node(s) with the highest sum are the most preferred.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinityrequiredduringschedulingignoredduringexecution">requiredDuringSchedulingIgnoredDuringExecution</a></b></td>
        <td>object</td>
        <td>
          If the affinity requirements specified by this field are not met at
scheduling time, the pod will not be scheduled onto the node.
If the affinity requirements specified by this field cease to be met
at some point during pod execution (e.g. due to an update), the system
may or may not try to eventually evict the pod from its node.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinity)</sup></sup>



An empty preferred scheduling term matches all objects with implicit weight 0
(i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindexpreference">preference</a></b></td>
        <td>object</td>
        <td>
          A node selector term, associated with the corresponding weight.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>weight</b></td>
        <td>integer</td>
        <td>
          Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[index].preference
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindex)</sup></sup>



A node selector term, associated with the corresponding weight.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindexpreferencematchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          A list of node selector requirements by node's labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindexpreferencematchfieldsindex">matchFields</a></b></td>
        <td>[]object</td>
        <td>
          A list of node selector requirements by node's fields.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[index].preference.matchExpressions[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindexpreference)</sup></sup>



A node selector requirement is a selector that contains values, a key, and an operator
that relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          The label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          Represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          An array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. If the operator is Gt or Lt, the values
array must have a single element, which will be interpreted as an integer.
This array is replaced during a strategic merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[index].preference.matchFields[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindexaffinitynodeaffinitypreferredduringschedulingignoredduringexecutionindexpreference)</sup></sup>



A node selector requirement is a selector that contains values, a key, and an operator
that relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          The label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          Represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          An array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. If the operator is Gt or Lt, the values
array must have a single element, which will be interpreted as an integer.
This array is replaced during a strategic merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
