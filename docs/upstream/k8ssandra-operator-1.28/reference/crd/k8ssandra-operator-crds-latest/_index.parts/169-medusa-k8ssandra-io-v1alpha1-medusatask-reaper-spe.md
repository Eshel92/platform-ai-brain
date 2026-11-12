<!-- Part 169 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

### MedusaTask
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






MedusaTask is the Schema for the MedusaTasks API

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
      <td>medusa.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>MedusaTask</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusataskspec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaTaskSpec defines the desired state of MedusaTask<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusataskstatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaTaskStatus defines the observed state of MedusaTask<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaTask.spec
<sup><sup>[↩ Parent](#medusatask)</sup></sup>



MedusaTaskSpec defines the desired state of MedusaTask

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
        <td><b>cassandraDatacenter</b></td>
        <td>string</td>
        <td>
          The name of the CassandraDatacenter to run the task on<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Requested operation to perform.<br/>
          <br/>
            <i>Enum</i>: sync, purge, prepare_restore<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>backupName</b></td>
        <td>string</td>
        <td>
          Name of the backup.
Will be necessary for operations such as verify or status.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>restoreKey</b></td>
        <td>string</td>
        <td>
          Restore key to use for the prepare_restore operation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaTask.status
<sup><sup>[↩ Parent](#medusatask)</sup></sup>



MedusaTaskStatus defines the observed state of MedusaTask

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
        <td><b>failed</b></td>
        <td>[]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>finishTime</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusataskstatusfinishedindex">finished</a></b></td>
        <td>[]object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>inProgress</b></td>
        <td>[]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>startTime</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaTask.status.finished[index]
<sup><sup>[↩ Parent](#medusataskstatus)</sup></sup>





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
        <td><b>nbBackupsPurged</b></td>
        <td>integer</td>
        <td>
          Number of backups that were purged. Only populated for purge tasks.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nbObjectsPurged</b></td>
        <td>integer</td>
        <td>
          Number of objects/files that were purged. Only populated for purge tasks.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>podName</b></td>
        <td>string</td>
        <td>
          Name of the pod that ran the task. Always populated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalObjectsWithinGcGrace</b></td>
        <td>integer</td>
        <td>
          Number of objects that couldn't be deleted due to Medusa GC grace. Only populated for purge tasks.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalPurgedSize</b></td>
        <td>integer</td>
        <td>
          Total size of purged files. Only populated for purge tasks.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


## reaper.k8ssandra.io/v1alpha1

Resource Types:

- [Reaper](#reaper)




### Reaper
<sup><sup>[↩ Parent](#reaperk8ssandraiov1alpha1 )</sup></sup>






Reaper is the Schema for the reapers API

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
      <td>reaper.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Reaper</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#reaperspec">spec</a></b></td>
        <td>object</td>
        <td>
          ReaperSpec defines the desired state of Reaper<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperstatus">status</a></b></td>
        <td>object</td>
        <td>
          ReaperStatus defines the observed state of Reaper<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec
<sup><sup>[↩ Parent](#reaper)</sup></sup>



ReaperSpec defines the desired state of Reaper

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
        <td><b>ServiceAccountName</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: default<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecadditionalenvvarsindex">additionalEnvVars</a></b></td>
        <td>[]object</td>
        <td>
          AdditionalEnvVars is a list of additional environment variables to set in the Reaper container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecaffinity">affinity</a></b></td>
        <td>object</td>
        <td>
          Affinity applied to the Reaper pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecautoscheduling">autoScheduling</a></b></td>
        <td>object</td>
        <td>
          Auto scheduling properties. When you enable the auto-schedule feature, Reaper dynamically schedules repairs for
all non-system keyspaces in a cluster. A cluster's keyspaces are monitored and any modifications (additions or
removals) are detected. When a new keyspace is created, a new repair schedule is created automatically for that
keyspace. Conversely, when a keyspace is removed, the corresponding repair schedule is deleted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspeccassandrausersecretref">cassandraUserSecretRef</a></b></td>
        <td>object</td>
        <td>
          Defines the username and password that Reaper will use to authenticate CQL connections to Cassandra clusters.
These credentials will be automatically turned into CQL roles by cass-operator when bootstrapping the datacenter,
then passed to the Reaper instance, so that it can authenticate against nodes in the datacenter using CQL. If CQL
authentication is not required, leave this field empty. The secret must be in the same namespace as Reaper itself
and must contain two keys: "username" and "password".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecclientencryptionstores">clientEncryptionStores</a></b></td>
        <td>object</td>
        <td>
          Client encryption stores which are used by Cassandra and Reaper.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspeccontainerimage">containerImage</a></b></td>
        <td>object</td>
        <td>
          The image to use for the Reaper pod main container.
The default is "thelastpickle/cassandra-reaper:4.0.0-rc1".<br/>
          <br/>
            <i>Default</i>: map[name:cassandra-reaper repository:thelastpickle tag:4.0.0-rc1]<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>datacenterAvailability</b></td>
        <td>enum</td>
        <td>
          DatacenterAvailability indicates to Reaper its deployment in relation to the target datacenter's network.
For single-DC clusters, the default (ALL) is fine. For multi-DC clusters, it is recommended to use EACH,
provided that there is one Reaper instance managing each DC in the cluster; otherwise, if one single Reaper
instance is going to manage more than one DC in the cluster, use ALL.
See https://cassandra-reaper.io/docs/usage/multi_dc/.<br/>
          <br/>
            <i>Enum</i>: LOCAL, ALL, EACH<br/>
            <i>Default</i>: ALL<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecdatacenterref">datacenterRef</a></b></td>
        <td>object</td>
        <td>
          DatacenterRef is the reference of a CassandraDatacenter resource that this Reaper instance should manage. It will
also be used as the backend for persisting Reaper's state. Reaper must be able to access the JMX port (7199 by
default) and the CQL port (9042 by default) on this DC.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>heapSize</b></td>
        <td>int or string</td>
        <td>
          HeapSize sets the JVM heap size to use for Reaper.<br/>
          <br/>
            <i>Default</i>: 2Gi<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspechttpmanagement">httpManagement</a></b></td>
        <td>object</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: map[enabled:true]<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainerimage">initContainerImage</a></b></td>
        <td>object</td>
        <td>
          Deprecated: The main container image will be used for the init container as well.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainerresources">initContainerResources</a></b></td>
        <td>object</td>
        <td>
          Init Container resources.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecinitcontainersecuritycontext">initContainerSecurityContext</a></b></td>
        <td>object</td>
        <td>
          InitContainerSecurityContext is the SecurityContext applied to the Reaper init container, used to perform schema
migrations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecjmxusersecretref">jmxUserSecretRef</a></b></td>
        <td>object</td>
        <td>
          Deprecated: JMX security is now based on CQL roles. Reaper will use cassandraUsefSecretRef for authentication,
this field is ignored.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>keyspace</b></td>
        <td>string</td>
        <td>
          The keyspace to use to store Reaper's state. Will default to "reaper_db" if unspecified. Will be created if it
does not exist, and if this Reaper resource is managed by K8ssandra.<br/>
          <br/>
            <i>Default</i>: reaper_db<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspeclivenessprobe">livenessProbe</a></b></td>
        <td>object</td>
        <td>
          LivenessProbe sets the Reaper liveness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecmetadata">metadata</a></b></td>
        <td>object</td>
        <td>
          labels and annotations for Reaper resources<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecpodsecuritycontext">podSecurityContext</a></b></td>
        <td>object</td>
        <td>
          PodSecurityContext contains a pod-level SecurityContext to apply to Reaper pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecreadinessprobe">readinessProbe</a></b></td>
        <td>object</td>
        <td>
          ReadinessProbe sets the Reaper readiness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecresources">resources</a></b></td>
        <td>object</td>
        <td>
          Main Container resources.<br/>
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
        <td><b><a href="#reaperspecsecuritycontext">securityContext</a></b></td>
        <td>object</td>
        <td>
          SecurityContext applied to the Reaper main container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipSchemaMigration</b></td>
        <td>boolean</td>
        <td>
          Whether to skip schema migration. Schema migration is done in an init container on every Reaper deployment and
can slow down Reaper's startup time. Besides, schema migration requires reading data at QUORUM. It can be skipped
if you know that the schema is already up-to-date, or if you know upfront that QUORUM cannot be achieved (for
example, because a DC is down).<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecstorageconfig">storageConfig</a></b></td>
        <td>object</td>
        <td>
          If StorageType is "local", Reaper will need a Persistent Volume to persist its data. This field allows
configuring that Persistent Volume.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageType</b></td>
        <td>enum</td>
        <td>
          The storage backend to store Reaper's data. Defaults to "cassandra" which causes Reaper to be stateless and store
its state to a Cassandra cluster it repairs (implying there must be one Reaper for each Cassandra cluster).
The "local" option makes Reaper to store its state locally, allowing a single Reaper to repair several clusters.<br/>
          <br/>
            <i>Enum</i>: cassandra, local<br/>
            <i>Default</i>: cassandra<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspectelemetry">telemetry</a></b></td>
        <td>object</td>
        <td>
          Telemetry defines the desired telemetry integrations to deploy targeting the Reaper pods for all DCs in this cluster
(unless overridden by DC specific settings)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspectolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations applied to the Reaper pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecuiusersecretref">uiUserSecretRef</a></b></td>
        <td>object</td>
        <td>
          Defines the secret which contains the username and password for the Reaper UI and REST API authentication. When UiUserSecretRef.Name == "", authentication is turned off in the front-end only.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.additionalEnvVars[index]
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



EnvVar represents an environment variable present in a Container.

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
          Name of the environment variable. Must be a C_IDENTIFIER.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>value</b></td>
        <td>string</td>
        <td>
          Variable references $(VAR_NAME) are expanded
using the previously defined environment variables in the container and
any service environment variables. If a variable cannot be resolved,
the reference in the input string will be unchanged. Double $$ are reduced
to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e.
"$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)".
Escaped references will never be expanded, regardless of whether the variable
exists or not.
Defaults to "".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecadditionalenvvarsindexvaluefrom">valueFrom</a></b></td>
        <td>object</td>
        <td>
          Source for the environment variable's value. Cannot be used if value is not empty.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
