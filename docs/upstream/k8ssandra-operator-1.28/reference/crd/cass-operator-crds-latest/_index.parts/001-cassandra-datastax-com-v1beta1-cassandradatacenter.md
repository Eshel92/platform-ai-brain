<!-- Part 1 of 46 of reference/crd/cass-operator-crds-latest/_index.md (split because the page is big). -->

## cassandra.datastax.com/v1beta1

Resource Types:

- [CassandraDatacenter](#cassandradatacenter)




### CassandraDatacenter
<sup><sup>[↩ Parent](#cassandradatastaxcomv1beta1 )</sup></sup>






CassandraDatacenter is the Schema for the cassandradatacenters API

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
      <td>cassandra.datastax.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>CassandraDatacenter</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspec">spec</a></b></td>
        <td>object</td>
        <td>
          CassandraDatacenterSpec defines the desired state of a CassandraDatacenter<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterstatus">status</a></b></td>
        <td>object</td>
        <td>
          CassandraDatacenterStatus defines the observed state of CassandraDatacenter<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraDatacenter.spec
<sup><sup>[↩ Parent](#cassandradatacenter)</sup></sup>



CassandraDatacenterSpec defines the desired state of a CassandraDatacenter

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
        <td><b>clusterName</b></td>
        <td>string</td>
        <td>
          The name by which CQL clients and instances will know the cluster. If the same
cluster name is shared by multiple Datacenters in the same Kubernetes namespace,
they will join together in a multi-datacenter cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>serverType</b></td>
        <td>enum</td>
        <td>
          Server type: "cassandra", "dse" or "hcd"<br/>
          <br/>
            <i>Enum</i>: cassandra, dse, hcd<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>serverVersion</b></td>
        <td>string</td>
        <td>
          Version string for config builder,
used to generate Cassandra server configuration<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>size</b></td>
        <td>integer</td>
        <td>
          Desired number of Cassandra server nodes<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Minimum</i>: 1<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecstorageconfig">storageConfig</a></b></td>
        <td>object</td>
        <td>
          StorageConfig describes the persistent storage request of each server node<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>additionalAnnotations</b></td>
        <td>map[string]string</td>
        <td>
          Additional Annotations allows to define additional labels that will be included in all objects created by the operator. Note, user can override values set by default from the cass-operator and doing so could break cass-operator functionality.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>additionalLabels</b></td>
        <td>map[string]string</td>
        <td>
          Additional Labels allows to define additional labels that will be included in all objects created by the operator. Note, user can override values set by default from the cass-operator and doing so could break cass-operator functionality.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>additionalSeeds</b></td>
        <td>[]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecadditionalserviceconfig">additionalServiceConfig</a></b></td>
        <td>object</td>
        <td>
          AdditionalServiceConfig allows to define additional parameters that are included in the created Services. Note, user can override values set by cass-operator and doing so could break cass-operator functionality.
Avoid label "cass-operator" and anything that starts with "cassandra.datastax.com/"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>allowMultipleNodesPerWorker</b></td>
        <td>boolean</td>
        <td>
          Turning this option on allows multiple server pods to be created on a k8s worker node, by removing the default pod anti affinity rules.
By default the operator creates just one server pod per k8s worker node. Using custom affinity rules might require turning this
option on in which case the defaults are not set.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>canaryUpgrade</b></td>
        <td>boolean</td>
        <td>
          Indicates that configuration and container image changes should only be pushed to
the first rack of the datacenter<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>canaryUpgradeCount</b></td>
        <td>integer</td>
        <td>
          The number of nodes that will be updated when CanaryUpgrade is true. Note that the value is
either 0 or greater than the rack size, then all nodes in the rack will get updated.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspeccdc">cdc</a></b></td>
        <td>object</td>
        <td>
          CDC allows configuration of the change data capture agent which can run within the Management API container. Use it to send data to Pulsar.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>string</td>
        <td>
          Config for the server, in YAML format<br/>
          <br/>
            <i>Format</i>: byte<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>configBuilderImage</b></td>
        <td>string</td>
        <td>
          Container image for the config builder init container. Overrides value from ImageConfig ConfigBuilderImage<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecconfigbuilderresources">configBuilderResources</a></b></td>
        <td>object</td>
        <td>
          Kubernetes resource requests and limits per server config initialization container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>configSecret</b></td>
        <td>string</td>
        <td>
          ConfigSecret is the name of a secret that contains configuration for Cassandra. The
secret is expected to have a property named config whose value should be a JSON
formatted string that should look like this:

   config: |-
     {
       "cassandra-yaml": {
         "read_request_timeout_in_ms": 10000
       },
       "jmv-options": {
         "max_heap_size": 1024M
       }
     }

ConfigSecret is mutually exclusive with Config. ConfigSecret takes precedence and
will be used exclusively if both properties are set. The operator sets a watch such
that an update to the secret will trigger an update of the StatefulSets.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>datacenterName</b></td>
        <td>string</td>
        <td>
          DatacenterName allows to override the name of the Cassandra datacenter. In Cassandra the DC name will be overridden by this value.
This setting can create conflicts if multiple DCs coexist in the same namespace if metadata.name for a DC with no override is set to the same value as the override name of another DC.
Use cautiously.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableSystemLoggerSidecar</b></td>
        <td>boolean</td>
        <td>
          Configuration for disabling the simple log tailing sidecar container. Our default is to have it enabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dockerImageRunsAsCassandra</b></td>
        <td>boolean</td>
        <td>
          DEPRECATED This setting does nothing and defaults to true. Use SecurityContext instead.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecdseworkloads">dseWorkloads</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>forceUpgradeRacks</b></td>
        <td>[]string</td>
        <td>
          Rack names in this list are set to the latest StatefulSet configuration
even if Cassandra nodes are down. Use this to recover from an upgrade that couldn't
roll out.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecmanagementapiauth">managementApiAuth</a></b></td>
        <td>object</td>
        <td>
          Config for the Management API certificates<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>minReadySeconds</b></td>
        <td>integer</td>
        <td>
          MinReadySeconds sets the minimum number of seconds for which a newly created pod should be ready without any of its containers crashing, for it to be considered available. Defaults to 5 seconds and is set in the StatefulSet spec.
Setting to 0 might cause multiple Cassandra pods to restart at the same time despite PodDisruptionBudget settings.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecnetworking">networking</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nodeAffinityLabels</b></td>
        <td>map[string]string</td>
        <td>
          NodeAffinityLabels to pin the Datacenter, using node affinity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nodeSelector</b></td>
        <td>map[string]string</td>
        <td>
          A map of label keys and values to restrict Cassandra node scheduling to k8s workers
with matchiing labels.
More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespec">podTemplateSpec</a></b></td>
        <td>object</td>
        <td>
          PodTemplate provides customisation options (labels, annotations, affinity rules, resource requests, and so on) for the cassandra pods<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecracksindex">racks</a></b></td>
        <td>[]object</td>
        <td>
          A list of the named racks in the datacenter, representing independent failure domains. The
number of racks should match the replication factor in the keyspaces you plan to create, and
the number of racks cannot easily be changed once a datacenter is deployed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>readOnlyRootFilesystem</b></td>
        <td>boolean</td>
        <td>
          ReadOnlyRootFilesystem makes the cassandra container to be run with a read-only root filesystem. This is enabled by default when using OSS Cassandra 4.1.0 and or newer, DSE 6.8 and newer (from datastax/dse-mgmtapi-6_8 repository) or HCD.
If serverImage override is used, this setting defaults to false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>replaceNodes</b></td>
        <td>[]string</td>
        <td>
          Deprecated Use CassandraTask replacenode to achieve correct node replacement. A list of pod names that need to be replaced.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecresources">resources</a></b></td>
        <td>object</td>
        <td>
          Kubernetes resource requests and limits, per pod<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>rollingRestartRequested</b></td>
        <td>boolean</td>
        <td>
          Deprecated. Use CassandraTask for rolling restarts. Whether to do a rolling restart at the next opportunity. The operator will set this back
to false once the restart is in progress.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serverImage</b></td>
        <td>string</td>
        <td>
          Cassandra server image name. Use of ImageConfig to match ServerVersion is recommended instead of this value.
This value will override anything set in the ImageConfig matching the ServerVersion
More info: https://kubernetes.io/docs/concepts/containers/images<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccount</b></td>
        <td>string</td>
        <td>
          Deprecated DeprecatedServiceAccount Use ServiceAccountName instead, which takes precedence. The k8s service account to use for the server pods<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the Kubernetes service account to use for the server pods. This takes presedence over DeprecatedServiceAccount and both take precedence over
setting it in the PodTemplateSpec.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stopped</b></td>
        <td>boolean</td>
        <td>
          A stopped CassandraDatacenter will have no running server pods, like using "stop" with
traditional System V init scripts. Other Kubernetes resources will be left intact, and volumes
will re-attach when the CassandraDatacenter workload is resumed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>superuserSecretName</b></td>
        <td>string</td>
        <td>
          This secret defines the username and password for the Cassandra server superuser.
If it is omitted, we will generate a secret instead.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>systemLoggerImage</b></td>
        <td>string</td>
        <td>
          Container image for the log tailing sidecar container. Overrides value from ImageConfig SystemLoggerImage<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecsystemloggerresources">systemLoggerResources</a></b></td>
        <td>object</td>
        <td>
          Kubernetes resource requests and limits per system logger container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspectolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations applied to the Cassandra pod. Note that these cannot be overridden with PodTemplateSpec.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecusersindex">users</a></b></td>
        <td>[]object</td>
        <td>
          Cassandra users to bootstrap<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraDatacenter.spec.storageConfig
<sup><sup>[↩ Parent](#cassandradatacenterspec)</sup></sup>



StorageConfig describes the persistent storage request of each server node

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
        <td><b><a href="#cassandradatacenterspecstorageconfigadditionalvolumesindex">additionalVolumes</a></b></td>
        <td>[]object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecstorageconfigcassandradatavolumeclaimspec">cassandraDataVolumeClaimSpec</a></b></td>
        <td>object</td>
        <td>
          PersistentVolumeClaimSpec describes the common attributes of storage devices
and allows a Source for provider-specific attributes<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraDatacenter.spec.storageConfig.additionalVolumes[index]
<sup><sup>[↩ Parent](#cassandradatacenterspecstorageconfig)</sup></sup>



AdditionalVolumes defines additional storage configurations

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
        <td><b>mountPath</b></td>
        <td>string</td>
        <td>
          Mount path into cassandra container<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the pvc / volume<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecstorageconfigadditionalvolumesindexpvcspec">pvcSpec</a></b></td>
        <td>object</td>
        <td>
          PVCSpec is a persistent volume claim spec. Either this or VolumeSource is required.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecstorageconfigadditionalvolumesindexvolumesource">volumeSource</a></b></td>
        <td>object</td>
        <td>
          VolumeSource to mount the volume from (such as ConfigMap / Secret). This or PVCSpec is required.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
