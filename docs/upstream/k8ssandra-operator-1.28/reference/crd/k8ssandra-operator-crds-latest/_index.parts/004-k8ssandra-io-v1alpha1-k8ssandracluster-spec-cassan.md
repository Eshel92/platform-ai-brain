<!-- Part 4 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.cassandra.cdc
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandra)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.clientEncryptionStores
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandra)</sup></sup>



Client encryption stores which are used by Cassandra and Reaper.

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
        <td><b><a href="#k8ssandraclusterspeccassandraclientencryptionstoreskeystoresecretref">keystoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore and optionally its password (which can also be specified through
the keystorePasswordSecretRef field)
if keys are not specified, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraclientencryptionstorestruststoresecretref">truststoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore and optionally its password (which can also be specified through
the truststorePasswordSecretRef field)
if keys are not specified explicitly, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraclientencryptionstoreskeystorepasswordsecretref">keystorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore password if password stored in different secret than keystoreSecretRef
if key isn't specified explicitly, "keystore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandraclientencryptionstorestruststorepasswordsecretref">truststorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore password if password stored in different secret than keystoreSecretRef
if key isn't specified  explicitly, "truststore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.clientEncryptionStores.keystoreSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandraclientencryptionstores)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.clientEncryptionStores.truststoreSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandraclientencryptionstores)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.clientEncryptionStores.keystorePasswordSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandraclientencryptionstores)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.clientEncryptionStores.truststorePasswordSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandraclientencryptionstores)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.config
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandra)</sup></sup>



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
        <td><b><a href="#k8ssandraclusterspeccassandraconfigjvmoptions">jvmOptions</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
