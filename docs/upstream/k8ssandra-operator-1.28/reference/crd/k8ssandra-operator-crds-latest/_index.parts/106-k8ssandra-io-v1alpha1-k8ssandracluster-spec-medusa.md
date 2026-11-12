<!-- Part 106 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.medusa.storageProperties
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusa)</sup></sup>



Provides all storage backend related properties for backups.

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
        <td><b>apiProfile</b></td>
        <td>string</td>
        <td>
          AWS Profile to use for authentication.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupGracePeriodInDays</b></td>
        <td>integer</td>
        <td>
          Age after which orphan sstables can be deleted from the storage backend.
Protects from race conditions between purge and ongoing backups.
Defaults to 10 days.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          The name of the bucket to use for the backups.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>concurrentTransfers</b></td>
        <td>integer</td>
        <td>
          Number of concurrent uploads.
Helps maximizing the speed of uploads but puts more pressure on the network.
Defaults to 0.<br/>
          <br/>
            <i>Default</i>: 0<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentialsType</b></td>
        <td>enum</td>
        <td>
          Type of credentials to use for authentication.
Can be "role-based", "credential-based" or empty.<br/>
          <br/>
            <i>Enum</i>: role-based, credential-based<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>host</b></td>
        <td>string</td>
        <td>
          Host to connect to for the storage backend.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>maxBackupAge</b></td>
        <td>integer</td>
        <td>
          Maximum backup age that the purge process should observe.<br/>
          <br/>
            <i>Default</i>: 0<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>maxBackupCount</b></td>
        <td>integer</td>
        <td>
          Maximum number of backups to keep (used by the purge process).
Default is unlimited.<br/>
          <br/>
            <i>Default</i>: 0<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>multiPartUploadThreshold</b></td>
        <td>integer</td>
        <td>
          File size over which cloud specific cli tools are used for transfer.
Defaults to 100 MB.<br/>
          <br/>
            <i>Default</i>: 104857600<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusastoragepropertiespodstorage">podStorage</a></b></td>
        <td>object</td>
        <td>
          Pod storage settings for the local storage provider<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>port</b></td>
        <td>integer</td>
        <td>
          Port to connect to for the storage backend.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Name of the top level folder in the backup bucket.
If empty, the cluster name will be used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the storage bucket.
Defaults to "default".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secure</b></td>
        <td>boolean</td>
        <td>
          Whether to use SSL for the storage backend.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sslVerify</b></td>
        <td>boolean</td>
        <td>
          When using SSL, whether to also verify the certificate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageProvider</b></td>
        <td>enum</td>
        <td>
          The storage backend to use for the backups.<br/>
          <br/>
            <i>Enum</i>: google_storage, azure_blobs, s3, s3_compatible, s3_rgw, ibm_storage<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusastoragepropertiesstoragesecretref">storageSecretRef</a></b></td>
        <td>object</td>
        <td>
          Kubernetes Secret that stores the key file for the storage provider's API.
If using 'local' storage, this value is ignored.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>transferMaxBandwidth</b></td>
        <td>string</td>
        <td>
          Max upload bandwidth in MB/s.
Defaults to 50 MB/s.<br/>
          <br/>
            <i>Default</i>: 50MB/s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.medusa.storageProperties.podStorage
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusastorageproperties)</sup></sup>



Pod storage settings for the local storage provider

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
        <td><b>accessModes</b></td>
        <td>[]string</td>
        <td>
          Pod local storage access modes<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>size</b></td>
        <td>int or string</td>
        <td>
          Size of the pod's storage in bytes.
Defaults to 10 GB.<br/>
          <br/>
            <i>Default</i>: 10Gi<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageClassName</b></td>
        <td>string</td>
        <td>
          Storage class name to use for the pod's storage.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.medusa.storageProperties.storageSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusastorageproperties)</sup></sup>



Kubernetes Secret that stores the key file for the storage provider's API.
If using 'local' storage, this value is ignored.

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



#### K8ssandraCluster.spec.reaper
<sup><sup>[↩ Parent](#k8ssandraclusterspec)</sup></sup>



Reaper defines the desired deployment characteristics for Reaper in this K8ssandraCluster.
If this is non-nil, Reaper might be deployed on every Cassandra datacenter in this K8ssandraCluster, unless
there is a Control Plane Reaper present. In that case, the K8ssandraCluster will get registered to it.

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
        <td><b><a href="#k8ssandraclusterspecreaperadditionalenvvarsindex">additionalEnvVars</a></b></td>
        <td>[]object</td>
        <td>
          AdditionalEnvVars is a list of additional environment variables to set in the Reaper container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperaffinity">affinity</a></b></td>
        <td>object</td>
        <td>
          Affinity applied to the Reaper pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperautoscheduling">autoScheduling</a></b></td>
        <td>object</td>
        <td>
          Auto scheduling properties. When you enable the auto-schedule feature, Reaper dynamically schedules repairs for
all non-system keyspaces in a cluster. A cluster's keyspaces are monitored and any modifications (additions or
removals) are detected. When a new keyspace is created, a new repair schedule is created automatically for that
keyspace. Conversely, when a keyspace is removed, the corresponding repair schedule is deleted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapercassandrausersecretref">cassandraUserSecretRef</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspecreapercontainerimage">containerImage</a></b></td>
        <td>object</td>
        <td>
          The image to use for the Reaper pod main container.
The default is "thelastpickle/cassandra-reaper:4.0.0-rc1".<br/>
          <br/>
            <i>Default</i>: map[name:cassandra-reaper repository:thelastpickle tag:4.0.0-rc1]<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>deploymentMode</b></td>
        <td>enum</td>
        <td>
          <br/>
          <br/>
            <i>Enum</i>: PER_DC, SINGLE, CONTROL_PLANE<br/>
            <i>Default</i>: PER_DC<br/>
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
        <td><b><a href="#k8ssandraclusterspecreaperhttpmanagement">httpManagement</a></b></td>
        <td>object</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: map[enabled:true]<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperinitcontainerimage">initContainerImage</a></b></td>
        <td>object</td>
        <td>
          Deprecated: The main container image will be used for the init container as well.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperinitcontainerresources">initContainerResources</a></b></td>
        <td>object</td>
        <td>
          Init Container resources.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperinitcontainersecuritycontext">initContainerSecurityContext</a></b></td>
        <td>object</td>
        <td>
          InitContainerSecurityContext is the SecurityContext applied to the Reaper init container, used to perform schema
migrations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperjmxusersecretref">jmxUserSecretRef</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspecreaperlivenessprobe">livenessProbe</a></b></td>
        <td>object</td>
        <td>
          LivenessProbe sets the Reaper liveness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapermetadata">metadata</a></b></td>
        <td>object</td>
        <td>
          labels and annotations for Reaper resources<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperpodsecuritycontext">podSecurityContext</a></b></td>
        <td>object</td>
        <td>
          PodSecurityContext contains a pod-level SecurityContext to apply to Reaper pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperreadinessprobe">readinessProbe</a></b></td>
        <td>object</td>
        <td>
          ReadinessProbe sets the Reaper readiness probe. Leave nil to use defaults.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperreaperref">reaperRef</a></b></td>
        <td>object</td>
        <td>
          When there is a CONTROL_PLANE Reaper out there, this field allows registering a K8ssandra cluster to it.
Populating this field disables some operator behaviour related to setting Reaper up.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperresources">resources</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspecreapersecuritycontext">securityContext</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspecreaperstorageconfig">storageConfig</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspecreapertelemetry">telemetry</a></b></td>
        <td>object</td>
        <td>
          Telemetry defines the desired telemetry integrations to deploy targeting the Reaper pods for all DCs in this cluster
(unless overridden by DC specific settings)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertolerationsindex">tolerations</a></b></td>
        <td>[]object</td>
        <td>
          Tolerations applied to the Reaper pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreaperuiusersecretref">uiUserSecretRef</a></b></td>
        <td>object</td>
        <td>
          Defines the secret which contains the username and password for the Reaper UI and REST API authentication. When UiUserSecretRef.Name == "", authentication is turned off in the front-end only.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.additionalEnvVars[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreaper)</sup></sup>



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
        <td><b><a href="#k8ssandraclusterspecreaperadditionalenvvarsindexvaluefrom">valueFrom</a></b></td>
        <td>object</td>
        <td>
          Source for the environment variable's value. Cannot be used if value is not empty.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
