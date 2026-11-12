<!-- Part 180 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

## replication.k8ssandra.io/v1alpha1

Resource Types:

- [ReplicatedSecret](#replicatedsecret)




### ReplicatedSecret
<sup><sup>[↩ Parent](#replicationk8ssandraiov1alpha1 )</sup></sup>






ReplicatedSecret is the Schema for the replicatedsecrets API

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
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>replication.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ReplicatedSecret</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#replicatedsecretspec">spec</a></b></td>
        <td>object</td>
        <td>
          ReplicatedSecretSpec defines the desired state of ReplicatedSecret<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#replicatedsecretstatus">status</a></b></td>
        <td>object</td>
        <td>
          ReplicatedSecretStatus defines the observed state of ReplicatedSecret<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ReplicatedSecret.spec
<sup><sup>[↩ Parent](#replicatedsecret)</sup></sup>



ReplicatedSecretSpec defines the desired state of ReplicatedSecret

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
        <td><b><a href="#replicatedsecretspecreplicationtargetsindex">replicationTargets</a></b></td>
        <td>[]object</td>
        <td>
          TargetContexts indicates the target clusters to which the secrets are replicated to. If empty, no clusters are targeted<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#replicatedsecretspecselector">selector</a></b></td>
        <td>object</td>
        <td>
          Selector defines which secrets are replicated. If left empty, all the secrets are replicated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ReplicatedSecret.spec.replicationTargets[index]
<sup><sup>[↩ Parent](#replicatedsecretspec)</sup></sup>





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
        <td><b>addLabels</b></td>
        <td>map[string]string</td>
        <td>
          AddLabels adds labels to the target secret.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dropLabels</b></td>
        <td>[]string</td>
        <td>
          DropLabels defines the labels to be dropped from the secret before replication, this is sometimes neccessary to avoid infinite replication.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sContextName</b></td>
        <td>string</td>
        <td>
          K8sContextName defines the target cluster name as set in the ClientConfig. If left empty, current cluster is assumed<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to replicate the data to in the target cluster. If left empty, current namespace is used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>targetPrefix</b></td>
        <td>string</td>
        <td>
          TargetPrefix is the prefix to be used for the replicated secret in the target cluster. If left empty, the same name is used
as the original secret.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ReplicatedSecret.spec.selector
<sup><sup>[↩ Parent](#replicatedsecretspec)</sup></sup>



Selector defines which secrets are replicated. If left empty, all the secrets are replicated

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
        <td><b><a href="#replicatedsecretspecselectormatchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ReplicatedSecret.spec.selector.matchExpressions[index]
<sup><sup>[↩ Parent](#replicatedsecretspecselector)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

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
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ReplicatedSecret.status
<sup><sup>[↩ Parent](#replicatedsecret)</sup></sup>



ReplicatedSecretStatus defines the observed state of ReplicatedSecret

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
        <td><b><a href="#replicatedsecretstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ReplicatedSecret.status.conditions[index]
<sup><sup>[↩ Parent](#replicatedsecretstatus)</sup></sup>





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
        <td><b>cluster</b></td>
        <td>string</td>
        <td>
          Cluster<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>string</td>
        <td>
          Status of the replication to target cluster<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          Type of condition<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          LastTransitionTime is the last time the condition transited from one status to another.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


## stargate.k8ssandra.io/v1alpha1

Resource Types:

- [Stargate](#stargate)




### Stargate
<sup><sup>[↩ Parent](#stargatek8ssandraiov1alpha1 )</sup></sup>






Stargate is the Schema for the stargates API

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
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>stargate.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Stargate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#stargatespec">spec</a></b></td>
        <td>object</td>
        <td>
          Specification of the desired behavior of this Stargate resource.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatestatus">status</a></b></td>
        <td>object</td>
        <td>
          Most recently observed status of this Stargate resource.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec
<sup><sup>[↩ Parent](#stargate)</sup></sup>



Specification of the desired behavior of this Stargate resource.

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
        <td><b><a href="#stargatespecdatacenterref">datacenterRef</a></b></td>
        <td>object</td>
        <td>
          DatacenterRef is the namespace-local reference of a CassandraDatacenter resource where
Stargate should be deployed.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>size</b></td>
        <td>integer</td>
        <td>
          Size is the number of Stargate instances to deploy in each datacenter. They will be spread evenly across racks.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 1<br/>
            <i>Minimum</i>: 1<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#stargatespecaffinity">affinity</a></b></td>
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
        <td><b>auth</b></td>
        <td>boolean</td>
        <td>
          Whether to enable authentication for Stargate. The default is true; it is highly recommended to always leave
authentication turned on, not only on Stargate nodes, but also on data nodes as well. Note that Stargate REST
APIs are currently only accessible if authentication is enabled, and if the authenticator in use in the whole
cluster is PasswordAuthenticator. The usage of any other authenticator will cause the REST API to become
inaccessible, see https://github.com/stargate/stargate/issues/792 for more. Stargate CQL API however remains
accessible even if authentication is disabled in the cluster, or when a custom authenticator is being used.<br/>
          <br/>
            <i>Default</i>: true<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespecauthoptions">authOptions</a></b></td>
        <td>object</td>
        <td>
          Authentication options.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraconfigmapref">cassandraConfigMapRef</a></b></td>
        <td>object</td>
        <td>
          CassandraConfigMapRef is a reference to a ConfigMap that holds Cassandra configuration.
The map should have a key named cassandra_yaml.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryption">cassandraEncryption</a></b></td>
        <td>object</td>
        <td>
          CassandraEncryption groups together encryption stores that are passed to the Stargate pods, so
that they can be mounted as volumes.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespeccontainerimage">containerImage</a></b></td>
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
        <td><b><a href="#stargatespeclivenessprobe">livenessProbe</a></b></td>
        <td>object</td>
        <td>
          LivenessProbe sets the Stargate liveness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespecmetadata">metadata</a></b></td>
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
        <td><b><a href="#stargatespecracksindex">racks</a></b></td>
        <td>[]object</td>
        <td>
          Racks allow customizing Stargate characteristics for specific racks in the datacenter.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespecreadinessprobe">readinessProbe</a></b></td>
        <td>object</td>
        <td>
          ReadinessProbe sets the Stargate readiness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespecresources">resources</a></b></td>
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
        <td><b><a href="#stargatespectelemetry">telemetry</a></b></td>
        <td>object</td>
        <td>
          Telemetry defines the desired telemetry integrations to deploy targeting the Stargate pods for all DCs in this cluster
(unless overridden by DC specific settings)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespectolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations are tolerations to apply to the Stargate pods.
Leave nil to let the controller reuse the same tolerations used for data pods in this datacenter, if any.
See https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec.datacenterRef
<sup><sup>[↩ Parent](#stargatespec)</sup></sup>



DatacenterRef is the namespace-local reference of a CassandraDatacenter resource where
Stargate should be deployed.

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
          Name of the referent.
This field is effectively required, but due to backwards compatibility is
allowed to be empty. Instances of this type with an empty value here are
almost certainly wrong.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
          <br/>
            <i>Default</i>: <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec.affinity
<sup><sup>[↩ Parent](#stargatespec)</sup></sup>



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
        <td><b><a href="#stargatespecaffinitynodeaffinity">nodeAffinity</a></b></td>
        <td>object</td>
        <td>
          Describes node affinity scheduling rules for the pod.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespecaffinitypodaffinity">podAffinity</a></b></td>
        <td>object</td>
        <td>
          Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespecaffinitypodantiaffinity">podAntiAffinity</a></b></td>
        <td>object</td>
        <td>
          Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
