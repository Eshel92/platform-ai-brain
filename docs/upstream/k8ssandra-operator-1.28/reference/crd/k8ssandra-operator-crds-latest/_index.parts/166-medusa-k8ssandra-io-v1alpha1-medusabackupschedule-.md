<!-- Part 166 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

### MedusaBackupSchedule
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






MedusaBackupSchedule is the Schema for the medusabackupschedules API

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
      <td>MedusaBackupSchedule</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusabackupschedulespec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaBackupScheduleSpec defines the desired state of MedusaBackupSchedule<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusabackupschedulestatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaBackupScheduleStatus defines the observed state of MedusaBackupSchedule<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaBackupSchedule.spec
<sup><sup>[↩ Parent](#medusabackupschedule)</sup></sup>



MedusaBackupScheduleSpec defines the desired state of MedusaBackupSchedule

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
        <td><b><a href="#medusabackupschedulespecbackupspec">backupSpec</a></b></td>
        <td>object</td>
        <td>
          BackupSpec defines the MedusaBackup to be created for this job<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>cronSchedule</b></td>
        <td>string</td>
        <td>
          CronSchedule is a cronjob format schedule for backups. Overrides any easier methods of defining the schedule<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>concurrencyPolicy</b></td>
        <td>string</td>
        <td>
          Specifics if this backup task can be run concurrently with other active backup tasks. Valid values are:
- "Allow": allows multiple Tasks to run concurrently on Cassandra cluster
- "Forbid" (default): only a single task is executed at once
The "Allow" property is only valid if all the other active Tasks have "Allow" as well.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disabled</b></td>
        <td>boolean</td>
        <td>
          Disabled if set ensures this job is not scheduling anything<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operationType</b></td>
        <td>enum</td>
        <td>
          Specifies the type of operation to be performed<br/>
          <br/>
            <i>Enum</i>: backup, purge<br/>
            <i>Default</i>: backup<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaBackupSchedule.spec.backupSpec
<sup><sup>[↩ Parent](#medusabackupschedulespec)</sup></sup>



BackupSpec defines the MedusaBackup to be created for this job

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
          The name of the CassandraDatacenter to back up<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>backupType</b></td>
        <td>enum</td>
        <td>
          The type of the backup: "full" or "differential"<br/>
          <br/>
            <i>Enum</i>: differential, full<br/>
            <i>Default</i>: differential<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaBackupSchedule.status
<sup><sup>[↩ Parent](#medusabackupschedule)</sup></sup>



MedusaBackupScheduleStatus defines the observed state of MedusaBackupSchedule

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
        <td><b>lastExecution</b></td>
        <td>string</td>
        <td>
          LastExecution tells when the backup was last time taken. If empty, the backup has never been taken<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nextSchedule</b></td>
        <td>string</td>
        <td>
          NextSchedule indicates when the next backup is going to be done<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MedusaConfiguration
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






MedusaConfiguration is the Schema for the medusaconfigurations API

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
      <td>MedusaConfiguration</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusaconfigurationspec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaConfigurationSpec defines the desired state of MedusaConfiguration<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaconfigurationstatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaConfigurationStatus defines the observed state of MedusaConfiguration<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaConfiguration.spec
<sup><sup>[↩ Parent](#medusaconfiguration)</sup></sup>



MedusaConfigurationSpec defines the desired state of MedusaConfiguration

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
        <td><b><a href="#medusaconfigurationspecstorageproperties">storageProperties</a></b></td>
        <td>object</td>
        <td>
          StorageProperties defines the storage backend settings to use for the backups.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaConfiguration.spec.storageProperties
<sup><sup>[↩ Parent](#medusaconfigurationspec)</sup></sup>



StorageProperties defines the storage backend settings to use for the backups.

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
        <td><b><a href="#medusaconfigurationspecstoragepropertiespodstorage">podStorage</a></b></td>
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
        <td><b><a href="#medusaconfigurationspecstoragepropertiesstoragesecretref">storageSecretRef</a></b></td>
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


#### MedusaConfiguration.spec.storageProperties.podStorage
<sup><sup>[↩ Parent](#medusaconfigurationspecstorageproperties)</sup></sup>



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


#### MedusaConfiguration.spec.storageProperties.storageSecretRef
<sup><sup>[↩ Parent](#medusaconfigurationspecstorageproperties)</sup></sup>



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


#### MedusaConfiguration.status
<sup><sup>[↩ Parent](#medusaconfiguration)</sup></sup>



MedusaConfigurationStatus defines the observed state of MedusaConfiguration

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
        <td><b><a href="#medusaconfigurationstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaConfiguration.status.conditions[index]
<sup><sup>[↩ Parent](#medusaconfigurationstatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

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
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
