<!-- Part 103 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.medusa
<sup><sup>[↩ Parent](#k8ssandraclusterspec)</sup></sup>



Medusa defines the desired deployment characteristics for Medusa in this K8ssandraCluster.
If this is non-nil, Medusa will be deployed in every Cassandra pod in this K8ssandraCluster.

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
        <td><b><a href="#k8ssandraclusterspecmedusacassandrausersecretref">cassandraUserSecretRef</a></b></td>
        <td>object</td>
        <td>
          Defines the username and password that Medusa will use to authenticate CQL connections to Cassandra clusters.
These credentials will be automatically turned into CQL roles by cass-operator when bootstrapping the datacenter,
then passed to the Medusa instances, so that it can authenticate against nodes in the datacenter using CQL.
The secret must be in the same namespace as Cassandra and must contain two keys: "username" and "password".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusacertificatessecretref">certificatesSecretRef</a></b></td>
        <td>object</td>
        <td>
          DEPRECATED: Please use ClientEncryptionStores instead.
Certificates for Medusa if client encryption is enabled in Cassandra.
The secret must be in the same namespace as Cassandra and must contain three keys: "rootca.crt", "client.crt_signed" and "client.key".
See https://docs.datastax.com/en/developer/python-driver/latest/security/ for more information on the required files.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusaclientencryptionstores">clientEncryptionStores</a></b></td>
        <td>object</td>
        <td>
          Certificates for Medusa to use if Cassandra has client encryption enabled. Replaces CertificatesSecretRef.
The secret still must reside in the same namespace as the CassandraDatacenter, but we now allow configuring which keys contain which certificate component.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusacontainerimage">containerImage</a></b></td>
        <td>object</td>
        <td>
          MedusaContainerImage is the image characteristics to use for Medusa containers. Leave nil
to use a default image.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusacontainerresources">containerResources</a></b></td>
        <td>object</td>
        <td>
          Medusa main container resources.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusainitcontainerresources">initContainerResources</a></b></td>
        <td>object</td>
        <td>
          medusa-restore init container resources.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusalivenessprobe">livenessProbe</a></b></td>
        <td>object</td>
        <td>
          Define the liveness probe settings to use for the Medusa containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusamedusaconfigurationref">medusaConfigurationRef</a></b></td>
        <td>object</td>
        <td>
          MedusaConfigurationRef points to an existing MedusaConfiguration object.
The purpose is to allow shared default settings across several clusters.
StorageProperties override the settings from MedusaConfiguration object to allow customization.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>purgeBackups</b></td>
        <td>boolean</td>
        <td>
          PurgeBackups toggles if the medusa backups should be purged nightly or not
Defaults to true.<br/>
          <br/>
            <i>Default</i>: true<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusareadinessprobe">readinessProbe</a></b></td>
        <td>object</td>
        <td>
          Define the readiness probe settings to use for the Medusa containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusasecuritycontext">securityContext</a></b></td>
        <td>object</td>
        <td>
          SecurityContext applied to the Medusa containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusaserviceproperties">serviceProperties</a></b></td>
        <td>object</td>
        <td>
          Provides all service related properties for Medusa.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusastorageproperties">storageProperties</a></b></td>
        <td>object</td>
        <td>
          Provides all storage backend related properties for backups.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.medusa.cassandraUserSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusa)</sup></sup>



Defines the username and password that Medusa will use to authenticate CQL connections to Cassandra clusters.
These credentials will be automatically turned into CQL roles by cass-operator when bootstrapping the datacenter,
then passed to the Medusa instances, so that it can authenticate against nodes in the datacenter using CQL.
The secret must be in the same namespace as Cassandra and must contain two keys: "username" and "password".

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



#### K8ssandraCluster.spec.medusa.certificatesSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusa)</sup></sup>



DEPRECATED: Please use ClientEncryptionStores instead.
Certificates for Medusa if client encryption is enabled in Cassandra.
The secret must be in the same namespace as Cassandra and must contain three keys: "rootca.crt", "client.crt_signed" and "client.key".
See https://docs.datastax.com/en/developer/python-driver/latest/security/ for more information on the required files.

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



#### K8ssandraCluster.spec.medusa.clientEncryptionStores
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusa)</sup></sup>



Certificates for Medusa to use if Cassandra has client encryption enabled. Replaces CertificatesSecretRef.
The secret still must reside in the same namespace as the CassandraDatacenter, but we now allow configuring which keys contain which certificate component.

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
        <td><b><a href="#k8ssandraclusterspecmedusaclientencryptionstoreskeystoresecretref">keystoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore and optionally its password (which can also be specified through
the keystorePasswordSecretRef field)
if keys are not specified, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusaclientencryptionstorestruststoresecretref">truststoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore and optionally its password (which can also be specified through
the truststorePasswordSecretRef field)
if keys are not specified explicitly, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusaclientencryptionstoreskeystorepasswordsecretref">keystorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore password if password stored in different secret than keystoreSecretRef
if key isn't specified explicitly, "keystore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusaclientencryptionstorestruststorepasswordsecretref">truststorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore password if password stored in different secret than keystoreSecretRef
if key isn't specified  explicitly, "truststore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.medusa.clientEncryptionStores.keystoreSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusaclientencryptionstores)</sup></sup>



ref to the secret that contains the keystore and optionally its password (which can also be specified through
the keystorePasswordSecretRef field)
if keys are not specified, "keystore" entry and a "keystore-password" entry will be used

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
          The key of the entry in the Secret resource's `data` field to be used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
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



#### K8ssandraCluster.spec.medusa.clientEncryptionStores.truststoreSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusaclientencryptionstores)</sup></sup>



ref to the secret that contains the truststore and optionally its password (which can also be specified through
the truststorePasswordSecretRef field)
if keys are not specified explicitly, "keystore" entry and a "keystore-password" entry will be used

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
          The key of the entry in the Secret resource's `data` field to be used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
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



#### K8ssandraCluster.spec.medusa.clientEncryptionStores.keystorePasswordSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusaclientencryptionstores)</sup></sup>



ref to the secret that contains the keystore password if password stored in different secret than keystoreSecretRef
if key isn't specified explicitly, "keystore-password" entry will be used

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
          The key of the entry in the Secret resource's `data` field to be used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
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



#### K8ssandraCluster.spec.medusa.clientEncryptionStores.truststorePasswordSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusaclientencryptionstores)</sup></sup>



ref to the secret that contains the truststore password if password stored in different secret than keystoreSecretRef
if key isn't specified  explicitly, "truststore-password" entry will be used

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
          The key of the entry in the Secret resource's `data` field to be used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
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



#### K8ssandraCluster.spec.medusa.containerImage
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusa)</sup></sup>



MedusaContainerImage is the image characteristics to use for Medusa containers. Leave nil
to use a default image.

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
          The image name to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pullPolicy</b></td>
        <td>enum</td>
        <td>
          The image pull policy to use. Defaults to "Always" if the tag is "latest", otherwise to "IfNotPresent".<br/>
          <br/>
            <i>Enum</i>: Always, IfNotPresent, Never<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecmedusacontainerimagepullsecretref">pullSecretRef</a></b></td>
        <td>object</td>
        <td>
          The secret to use when pulling the image from private repositories. If specified, this secret will be passed to
individual puller implementations for them to use. For example, in the case of Docker, only DockerConfig type
secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>registry</b></td>
        <td>string</td>
        <td>
          The Docker registry to use. Defaults to "docker.io", the official Docker Hub.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>repository</b></td>
        <td>string</td>
        <td>
          The Docker repository to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          The image tag to use. Defaults to "latest".<br/>
          <br/>
            <i>Default</i>: latest<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.medusa.containerImage.pullSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusacontainerimage)</sup></sup>



The secret to use when pulling the image from private repositories. If specified, this secret will be passed to
individual puller implementations for them to use. For example, in the case of Docker, only DockerConfig type
secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

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



#### K8ssandraCluster.spec.medusa.containerResources
<sup><sup>[↩ Parent](#k8ssandraclusterspecmedusa)</sup></sup>



Medusa main container resources.

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
        <td><b><a href="#k8ssandraclusterspecmedusacontainerresourcesclaimsindex">claims</a></b></td>
        <td>[]object</td>
        <td>
          Claims lists the names of resources, defined in spec.resourceClaims,
that are used by this container.

This is an alpha field and requires enabling the
DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>limits</b></td>
        <td>map[string]int or string</td>
        <td>
          Limits describes the maximum amount of compute resources allowed.
More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>requests</b></td>
        <td>map[string]int or string</td>
        <td>
          Requests describes the minimum amount of compute resources required.
If Requests is omitted for a container, it defaults to Limits if that is explicitly specified,
otherwise to an implementation-defined value. Requests cannot exceed Limits.
More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
