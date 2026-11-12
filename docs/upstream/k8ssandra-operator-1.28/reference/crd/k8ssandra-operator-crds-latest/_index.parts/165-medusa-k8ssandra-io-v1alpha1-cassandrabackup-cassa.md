<!-- Part 165 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### CassandraBackup.status.cassdcTemplateSpec.spec.systemLoggerResources
<sup><sup>[↩ Parent](#cassandrabackupstatuscassdctemplatespecspec)</sup></sup>



Kubernetes resource requests and limits per system logger container.

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
        <td><b>limits</b></td>
        <td>map[string]int or string</td>
        <td>
          Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>requests</b></td>
        <td>map[string]int or string</td>
        <td>
          Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraBackup.status.cassdcTemplateSpec.spec.tolerations[index]
<sup><sup>[↩ Parent](#cassandrabackupstatuscassdctemplatespecspec)</sup></sup>



The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

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
        <td><b>effect</b></td>
        <td>string</td>
        <td>
          Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tolerationSeconds</b></td>
        <td>integer</td>
        <td>
          TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>value</b></td>
        <td>string</td>
        <td>
          Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraBackup.status.cassdcTemplateSpec.spec.users[index]
<sup><sup>[↩ Parent](#cassandrabackupstatuscassdctemplatespecspec)</sup></sup>





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
        <td><b>secretName</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>superuser</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### CassandraRestore
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






CassandraRestore is the Schema for the cassandrarestores API

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
      <td>CassandraRestore</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandrarestorespec">spec</a></b></td>
        <td>object</td>
        <td>
          CassandraRestoreSpec defines the desired state of CassandraRestore<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandrarestorestatus">status</a></b></td>
        <td>object</td>
        <td>
          CassandraRestoreStatus defines the observed state of CassandraRestore<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraRestore.spec
<sup><sup>[↩ Parent](#cassandrarestore)</sup></sup>



CassandraRestoreSpec defines the desired state of CassandraRestore

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
        <td><b>backup</b></td>
        <td>string</td>
        <td>
          The name of the CassandraBackup to restore<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandrarestorespeccassandradatacenter">cassandraDatacenter</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>inPlace</b></td>
        <td>boolean</td>
        <td>
          When true the restore will be performed on the source cluster from which the backup was taken. There will be a rolling restart of the source cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>shutdown</b></td>
        <td>boolean</td>
        <td>
          When set to true, the cluster is shutdown before the restore is applied. This is necessary process if there are schema changes between the backup and current schema. Recommended.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


#### CassandraRestore.spec.cassandraDatacenter
<sup><sup>[↩ Parent](#cassandrarestorespec)</sup></sup>





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
          The name to give the C* cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          The name to give the new, restored CassandraDatacenter<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


#### CassandraRestore.status
<sup><sup>[↩ Parent](#cassandrarestore)</sup></sup>



CassandraRestoreStatus defines the observed state of CassandraRestore

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
        <td><b>restoreKey</b></td>
        <td>string</td>
        <td>
          A unique key that identifies the restore operation.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>datacenterStopped</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
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
        <td><b>finished</b></td>
        <td>[]string</td>
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


### MedusaBackupJob
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






MedusaBackupJob is the Schema for the medusabackupjobs API

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
      <td>MedusaBackupJob</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusabackupjobspec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaBackupJobSpec defines the desired state of MedusaBackupJob<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusabackupjobstatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaBackupJobStatus defines the observed state of MedusaBackupJob<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaBackupJob.spec
<sup><sup>[↩ Parent](#medusabackupjob)</sup></sup>



MedusaBackupJobSpec defines the desired state of MedusaBackupJob

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


#### MedusaBackupJob.status
<sup><sup>[↩ Parent](#medusabackupjob)</sup></sup>



MedusaBackupJobStatus defines the observed state of MedusaBackupJob

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
        <td><b>finished</b></td>
        <td>[]string</td>
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


### MedusaBackup
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






MedusaBackup is the Schema for the medusabackups API

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
      <td>MedusaBackup</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusabackupspec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaBackupSpec defines the desired state of MedusaBackup<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusabackupstatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaBackupStatus defines the observed state of MedusaBackup<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaBackup.spec
<sup><sup>[↩ Parent](#medusabackup)</sup></sup>



MedusaBackupSpec defines the desired state of MedusaBackup

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


#### MedusaBackup.status
<sup><sup>[↩ Parent](#medusabackup)</sup></sup>



MedusaBackupStatus defines the observed state of MedusaBackup

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
        <td><b>finishTime</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>finishedNodes</b></td>
        <td>integer</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusabackupstatusnodesindex">nodes</a></b></td>
        <td>[]object</td>
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
      </tr><tr>
        <td><b>status</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalFiles</b></td>
        <td>integer</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalNodes</b></td>
        <td>integer</td>
        <td>
          <br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalSize</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaBackup.status.nodes[index]
<sup><sup>[↩ Parent](#medusabackupstatus)</sup></sup>





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
        <td><b>datacenter</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>host</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>rack</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tokens</b></td>
        <td>[]integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
