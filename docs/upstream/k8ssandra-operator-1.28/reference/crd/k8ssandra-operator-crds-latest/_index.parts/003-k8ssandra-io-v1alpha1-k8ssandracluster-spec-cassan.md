<!-- Part 3 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

## k8ssandra.io/v1alpha1

Resource Types:

- [K8ssandraCluster](#k8ssandracluster)




### K8ssandraCluster
<sup><sup>[↩ Parent](#k8ssandraiov1alpha1 )</sup></sup>






K8ssandraCluster is the Schema for the k8ssandraclusters API. The K8ssandraCluster CRD name is also the name of the
Cassandra cluster (which corresponds to cluster_name in cassandra.yaml).

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
      <td>k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>K8ssandraCluster</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspec">spec</a></b></td>
        <td>object</td>
        <td>
          K8ssandraClusterSpec defines the desired state of K8ssandraCluster<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterstatus">status</a></b></td>
        <td>object</td>
        <td>
          K8ssandraClusterStatus defines the observed state of K8ssandraCluster<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec
<sup><sup>[↩ Parent](#k8ssandracluster)</sup></sup>



K8ssandraClusterSpec defines the desired state of K8ssandraCluster

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
        <td><b>auth</b></td>
        <td>boolean</td>
        <td>
          Whether to enable authentication in this cluster. The default is true; it is highly recommended to always leave
authentication turned on. When enabled, authentication will be enforced not only on Cassandra nodes, but also on
Reaper, Medusa and Stargate nodes, if any.<br/>
          <br/>
            <i>Default</i>: true<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandra">cassandra</a></b></td>
        <td>object</td>
        <td>
          Cassandra is a specification of the Cassandra cluster. This includes everything from
the number of datacenters, the k8s cluster where each DC should be deployed, node
affinity (via racks), individual C* node settings, JVM settings, and more.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>externalDatacenters</b></td>
        <td>[]string</td>
        <td>
          During a migration the operator should alter keyspaces replication settings including the following external DCs.
This avoids removing replicas from datacenters which are outside of the operator scope (not referenced in the CR).
Replication settings changes will only apply to system_* keyspaces as well as reaper_db and data_endpoint_auth (Stargate).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusa">medusa</a></b></td>
        <td>object</td>
        <td>
          Medusa defines the desired deployment characteristics for Medusa in this K8ssandraCluster.
If this is non-nil, Medusa will be deployed in every Cassandra pod in this K8ssandraCluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaper">reaper</a></b></td>
        <td>object</td>
        <td>
          Reaper defines the desired deployment characteristics for Reaper in this K8ssandraCluster.
If this is non-nil, Reaper might be deployed on every Cassandra datacenter in this K8ssandraCluster, unless
there is a Control Plane Reaper present. In that case, the K8ssandraCluster will get registered to it.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretsProvider</b></td>
        <td>enum</td>
        <td>
          SecretsProvider defines whether the secrets used for credentials and certs will be backed
by an external secret backend (e.g. vault). This moves the responsibility of generating and
storing secrets from the operators to the user and will rely on a mutating webhook to inject
the secrets into the necessary resources<br/>
          <br/>
            <i>Enum</i>: internal, external<br/>
            <i>Default</i>: internal<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecstargate">stargate</a></b></td>
        <td>object</td>
        <td>
          DEPRECATED Stargate defines the desired deployment characteristics for Stargate in this K8ssandraCluster.
If this is non-nil, Stargate will be deployed on every Cassandra datacenter in this K8ssandraCluster.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra
<sup><sup>[↩ Parent](#k8ssandraclusterspec)</sup></sup>



Cassandra is a specification of the Cassandra cluster. This includes everything from
the number of datacenters, the k8s cluster where each DC should be deployed, node
affinity (via racks), individual C* node settings, JVM settings, and more.

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
        <td><b>additionalSeeds</b></td>
        <td>[]string</td>
        <td>
          AdditionalSeeds specifies Cassandra node IPs for an existing datacenter. This is
primarily intended for migrations from an existing Cassandra cluster that is not
managed by k8ssandra-operator. Note that this property should NOT be used to set
seeds for a DC that is or will be managed by k8ssandra-operator. k8ssandra-operator
already manages seeds for DCs that it manages. If you have DNS set up such that you
can resolve hostnames for the remote Cassandra cluster, then you can specify hostnames
here; otherwise, use IP addresses.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandracdc">cdc</a></b></td>
        <td>object</td>
        <td>
          CDC defines the desired state for CDC integrations. It can be used to feed mutation events from Cassandra into an Apache Pulsar cluster,
from where they can be expored to external systems.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraclientencryptionstores">clientEncryptionStores</a></b></td>
        <td>object</td>
        <td>
          Client encryption stores which are used by Cassandra and Reaper.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterName</b></td>
        <td>string</td>
        <td>
          Override the Cassandra cluster name. If unspecified, the cluster name will be the same as the K8ssandraCluster
CRD name.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraconfig">config</a></b></td>
        <td>object</td>
        <td>
          CassandraConfig contains configuration settings that are applied to cassandra.yaml, dse.yaml
and the various jvm*.options files.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandracontainersindex">containers</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindex">datacenters</a></b></td>
        <td>[]object</td>
        <td>
          Datacenters a list of the DCs in the cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradseworkloads">dseWorkloads</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraextravolumes">extraVolumes</a></b></td>
        <td>object</td>
        <td>
          Volumes defines additional volumes to be added to each Cassandra pod.
If the volume uses a PersistentVolumeClaim, the PVC will be managed by the statefulset.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandrainitcontainersindex">initContainers</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspeccassandrajmxinitcontainerimage">jmxInitContainerImage</a></b></td>
        <td>object</td>
        <td>
          Deprecated: JMX security is now based on CQL roles. We don't need an init container to configure JMX
authentication anymore. The value of this field will be ignored.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandramanagementapiauth">managementApiAuth</a></b></td>
        <td>object</td>
        <td>
          ManagementApiAuth defines the authentication settings for the management API in the Cassandra pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandrametadata">metadata</a></b></td>
        <td>object</td>
        <td>
          Struct to hold labels and annotations for the top-level Cassandra cluster definition.<br/>
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
        <td><b><a href="#k8ssandraclusterspeccassandranetworking">networking</a></b></td>
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
        <td><b>podPriorityClassName</b></td>
        <td>string</td>
        <td>
          PodPriorityClassName defines the priority class name for the Cassandra pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandrapodsecuritycontext">podSecurityContext</a></b></td>
        <td>object</td>
        <td>
          PodSecurityContext defines the security context for the Cassandra pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraracksindex">racks</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspeccassandraresources">resources</a></b></td>
        <td>object</td>
        <td>
          Resources is the cpu and memory resources for the cassandra container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraserverencryptionstores">serverEncryptionStores</a></b></td>
        <td>object</td>
        <td>
          Internode encryption stores which are used by Cassandra and Stargate.<br/>
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
        <td><b>serverType</b></td>
        <td>enum</td>
        <td>
          Server type: "cassandra" or "dse".<br/>
          <br/>
            <i>Enum</i>: cassandra, dse, hcd<br/>
            <i>Default</i>: cassandra<br/>
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
        <td><b><a href="#k8ssandraclusterspeccassandrastorageconfig">storageConfig</a></b></td>
        <td>object</td>
        <td>
          StorageConfig is the persistent storage requirements for each Cassandra pod. This
includes everything under /var/lib/cassandra, namely the commit log and data
directories.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandrasuperusersecretref">superuserSecretRef</a></b></td>
        <td>object</td>
        <td>
          The reference to the superuser secret to use for Cassandra. If unspecified, a default secret will be generated
with a random password; the generated secret name will be "<cluster_name>-superuser" where <cluster_name> is the
K8ssandraCluster CRD name.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandratelemetry">telemetry</a></b></td>
        <td>object</td>
        <td>
          Telemetry defines the desired state for telemetry resources in this datacenter.
If telemetry configurations are defined, telemetry resources will be deployed to integrate with
a user-provided monitoring solution (at present, only support for Prometheus is available).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandratolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations applied to every Cassandra pod.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
