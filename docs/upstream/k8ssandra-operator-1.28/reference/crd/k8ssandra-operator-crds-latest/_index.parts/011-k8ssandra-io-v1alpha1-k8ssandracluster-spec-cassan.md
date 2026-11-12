<!-- Part 11 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.cassandra.datacenters[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandra)</sup></sup>





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
        <td><b>size</b></td>
        <td>integer</td>
        <td>
          Size is the number Cassandra pods to deploy in this datacenter.
This number does not include Stargate instances.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Minimum</i>: 1<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexcdc">cdc</a></b></td>
        <td>object</td>
        <td>
          CDC defines the desired state for CDC integrations. It can be used to feed mutation events from Cassandra into an Apache Pulsar cluster,
from where they can be expored to external systems.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexconfig">config</a></b></td>
        <td>object</td>
        <td>
          CassandraConfig contains configuration settings that are applied to cassandra.yaml, dse.yaml
and the various jvm*.options files.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexcontainersindex">containers</a></b></td>
        <td>[]object</td>
        <td>
          Containers defines containers to be deployed in each Cassandra pod.
K8ssandra-operator and cass-operator will create their own containers, which can be referenced here to override specific settings,
such as mounts or resources request/limits for example.
Example:
 containers:
 - name: server-system-logger
 - name: custom-container
   image: busybox
 - name: cassandra<br/>
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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexdseworkloads">dseWorkloads</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexextravolumes">extraVolumes</a></b></td>
        <td>object</td>
        <td>
          Volumes defines additional volumes to be added to each Cassandra pod.
If the volume uses a PersistentVolumeClaim, the PVC will be managed by the statefulset.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexinitcontainersindex">initContainers</a></b></td>
        <td>[]object</td>
        <td>
          InitContainers defines init-containers to be deployed in each Cassandra pod.
K8ssandra-operator and cass-operator will create their own init-containers, which can be referenced here to control ordering or override specific settings
such as mounts or resources request/limits for example.
Only the name of the k8ssandra-operator/cass-operator init-containers is required, not their full definition which will be created by the operators.
Example:
 initContainers:
 - name: server-config-init
 - name: custom-init-container
   image: busybox
 - name: medusa-restore
Otherwise init-containers referenced here will be injected in first position<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexjmxinitcontainerimage">jmxInitContainerImage</a></b></td>
        <td>object</td>
        <td>
          Deprecated: JMX security is now based on CQL roles. We don't need an init container to configure JMX
authentication anymore. The value of this field will be ignored.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sContext</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexmanagementapiauth">managementApiAuth</a></b></td>
        <td>object</td>
        <td>
          ManagementApiAuth defines the authentication settings for the management API in the Cassandra pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexmetadata">metadata</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>mgmtAPIHeap</b></td>
        <td>int or string</td>
        <td>
          MgmtAPIHeap defines the amount of memory devoted to the management
api heap.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexnetworking">networking</a></b></td>
        <td>object</td>
        <td>
          Networking enables host networking and configures a NodePort ports.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>perNodeConfigInitContainerImage</b></td>
        <td>string</td>
        <td>
          The image to use in each Cassandra pod for the (short-lived) init container that merges global and perNodeConfig
configuration. This is only useful when PerNodeConfigMapRef is set.
The default is "k8ssandra/k8ssandra-client:v0.8.1".<br/>
          <br/>
            <i>Default</i>: k8ssandra/k8ssandra-client:v0.8.1<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexpernodeconfigmapref">perNodeConfigMapRef</a></b></td>
        <td>object</td>
        <td>
          PerNodeConfigMapRef is a reference to a ConfigMap that contains per-node configuration for
this DC. The ConfigMap is expected to have entries in the following form:
<pod-name>_<file-name>.yaml, where <pod-name> is the name of the pod and <file-name> is the
name of a configuration file (typically, cassandra.yaml). The value of the entry is expected
to be a YAML fragment that contains the per-node configuration for each pod. When the pod is
started, the per-node ConfigMap is mounted and the contents of each entry corresponding to
the pod are merged into their respective configuration files.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>podPriorityClassName</b></td>
        <td>string</td>
        <td>
          PodPriorityClassName defines the priority class name for the Cassandra pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexpodsecuritycontext">podSecurityContext</a></b></td>
        <td>object</td>
        <td>
          PodSecurityContext defines the security context for the Cassandra pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexracksindex">racks</a></b></td>
        <td>[]object</td>
        <td>
          Racks is a list of named racks. Note that racks are used to create node affinity. //<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>readOnlyRootFilesystem</b></td>
        <td>boolean</td>
        <td>
          ReadOnlyRootFilesystem makes the cassandra container to be run with a read-only root filesystem. Currently only functional when used with the
new k8ssandra-client config builder (Cassandra 4.1 and newer and HCD)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexresources">resources</a></b></td>
        <td>object</td>
        <td>
          Resources is the cpu and memory resources for the cassandra container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serverImage</b></td>
        <td>string</td>
        <td>
          ServerImage is the image for the cassandra container. Note that this should be a
management-api image. If left empty the operator will choose a default image based
on ServerVersion.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serverVersion</b></td>
        <td>string</td>
        <td>
          ServerVersion is the Cassandra or DSE version. The following versions are supported:
- Cassandra: 3.11.X, 4.X.X and 5.X.X
- DSE: 6.8.X, 7.x.x
- HCD: 1.0.x<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccount</b></td>
        <td>string</td>
        <td>
          The k8s service account to use for the Cassandra pods<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>softPodAntiAffinity</b></td>
        <td>boolean</td>
        <td>
          SoftPodAntiAffinity sets whether multiple Cassandra instances can be scheduled on the same node.
This should normally be false to ensure cluster resilience but may be set true for test/dev scenarios to minimise
the number of nodes required.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargate">stargate</a></b></td>
        <td>object</td>
        <td>
          DEPRECATED Stargate defines the desired deployment characteristics for Stargate in this datacenter. Leave nil to skip
deploying Stargate in this datacenter.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stopped</b></td>
        <td>boolean</td>
        <td>
          Stopped means that the datacenter will be stopped. Use this for maintenance or for cost saving. A stopped
CassandraDatacenter will have no running server pods, like using "stop" with  traditional System V init scripts.
Other Kubernetes resources will be left intact, and volumes will re-attach when the CassandraDatacenter
workload is resumed.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstorageconfig">storageConfig</a></b></td>
        <td>object</td>
        <td>
          StorageConfig is the persistent storage requirements for each Cassandra pod. This
includes everything under /var/lib/cassandra, namely the commit log and data
directories.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindextelemetry">telemetry</a></b></td>
        <td>object</td>
        <td>
          Telemetry defines the desired state for telemetry resources in this datacenter.
If telemetry configurations are defined, telemetry resources will be deployed to integrate with
a user-provided monitoring solution (at present, only support for Prometheus is available).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindextolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations applied to every Cassandra pod.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].cdc
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindex)</sup></sup>



CDC defines the desired state for CDC integrations. It can be used to feed mutation events from Cassandra into an Apache Pulsar cluster,
from where they can be expored to external systems.

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
        <td><b>pulsarServiceUrl</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>cdcConcurrentProcessors</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cdcPollIntervalM</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cdcWorkingDir</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>errorCommitLogReprocessEnabled</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pulsarAuthParams</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pulsarAuthPluginClassName</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pulsarBatchDelayInMs</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pulsarKeyBasedBatcher</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pulsarMaxPendingMessages</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pulsarMaxPendingMessagesAcrossPartitions</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslAllowInsecureConnection</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslCipherSuites</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslEnabledProtocols</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslHostnameVerificationEnable</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslKeystorePassword</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslKeystorePath</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslProvider</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslTruststorePassword</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslTruststorePath</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslTruststoreType</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>topicPrefix</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].config
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindex)</sup></sup>



CassandraConfig contains configuration settings that are applied to cassandra.yaml, dse.yaml
and the various jvm*.options files.

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
        <td><b>cassandraYaml</b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dseYaml</b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexconfigjvmoptions">jvmOptions</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
