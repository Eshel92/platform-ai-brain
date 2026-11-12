<!-- Part 184 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### Stargate.spec.authOptions
<sup><sup>[↩ Parent](#stargatespec)</sup></sup>



Authentication options.

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
        <td><b>apiAuthMethod</b></td>
        <td>enum</td>
        <td>
          The method to use for authenticating requests to the Stargate APIs. Stargate currently has
two authentication / authorization methods:
- Table: table-based;
- JWT: JSON web token (JWT)-based.
The methods are mutually exclusive. The default method is Table.<br/>
          <br/>
            <i>Enum</i>: Table, JWT<br/>
            <i>Default</i>: Table<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providerUrl</b></td>
        <td>string</td>
        <td>
          Required when using JWT authentication method, ignored otherwise.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tokenTtlSeconds</b></td>
        <td>integer</td>
        <td>
          The time-to-live in seconds of an API authentication token. Valid only for the Table
authentication method. By default, the token persists for 30 minutes with a sliding window.
Each use of the token to authenticate resets the 30-minute window. A token created and used
after 29 minutes will authenticate a request, but if 31 minutes passes before use, the token
will no longer exist.
Default is 1800 seconds (30 minutes).<br/>
          <br/>
            <i>Minimum</i>: 1<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec.cassandraConfigMapRef
<sup><sup>[↩ Parent](#stargatespec)</sup></sup>



CassandraConfigMapRef is a reference to a ConfigMap that holds Cassandra configuration.
The map should have a key named cassandra_yaml.

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



#### Stargate.spec.cassandraEncryption
<sup><sup>[↩ Parent](#stargatespec)</sup></sup>



CassandraEncryption groups together encryption stores that are passed to the Stargate pods, so
that they can be mounted as volumes.

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
        <td><b><a href="#stargatespeccassandraencryptionclientencryptionstores">clientEncryptionStores</a></b></td>
        <td>object</td>
        <td>
          Client encryption stores which are used by Cassandra and Reaper.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionserverencryptionstores">serverEncryptionStores</a></b></td>
        <td>object</td>
        <td>
          Internode encryption stores which are used by Cassandra and Stargate.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec.cassandraEncryption.clientEncryptionStores
<sup><sup>[↩ Parent](#stargatespeccassandraencryption)</sup></sup>



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
        <td><b><a href="#stargatespeccassandraencryptionclientencryptionstoreskeystoresecretref">keystoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore and optionally its password (which can also be specified through
the keystorePasswordSecretRef field)
if keys are not specified, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionclientencryptionstorestruststoresecretref">truststoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore and optionally its password (which can also be specified through
the truststorePasswordSecretRef field)
if keys are not specified explicitly, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionclientencryptionstoreskeystorepasswordsecretref">keystorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore password if password stored in different secret than keystoreSecretRef
if key isn't specified explicitly, "keystore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionclientencryptionstorestruststorepasswordsecretref">truststorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore password if password stored in different secret than keystoreSecretRef
if key isn't specified  explicitly, "truststore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec.cassandraEncryption.clientEncryptionStores.keystoreSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionclientencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.clientEncryptionStores.truststoreSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionclientencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.clientEncryptionStores.keystorePasswordSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionclientencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.clientEncryptionStores.truststorePasswordSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionclientencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.serverEncryptionStores
<sup><sup>[↩ Parent](#stargatespeccassandraencryption)</sup></sup>



Internode encryption stores which are used by Cassandra and Stargate.

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
        <td><b><a href="#stargatespeccassandraencryptionserverencryptionstoreskeystoresecretref">keystoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore and optionally its password (which can also be specified through
the keystorePasswordSecretRef field)
if keys are not specified, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionserverencryptionstorestruststoresecretref">truststoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore and optionally its password (which can also be specified through
the truststorePasswordSecretRef field)
if keys are not specified explicitly, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionserverencryptionstoreskeystorepasswordsecretref">keystorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore password if password stored in different secret than keystoreSecretRef
if key isn't specified explicitly, "keystore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#stargatespeccassandraencryptionserverencryptionstorestruststorepasswordsecretref">truststorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore password if password stored in different secret than keystoreSecretRef
if key isn't specified  explicitly, "truststore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Stargate.spec.cassandraEncryption.serverEncryptionStores.keystoreSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionserverencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.serverEncryptionStores.truststoreSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionserverencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.serverEncryptionStores.keystorePasswordSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionserverencryptionstores)</sup></sup>



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



#### Stargate.spec.cassandraEncryption.serverEncryptionStores.truststorePasswordSecretRef
<sup><sup>[↩ Parent](#stargatespeccassandraencryptionserverencryptionstores)</sup></sup>



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
