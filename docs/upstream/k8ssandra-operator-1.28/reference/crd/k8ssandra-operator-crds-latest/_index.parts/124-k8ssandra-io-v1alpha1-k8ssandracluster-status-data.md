<!-- Part 124 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.status.datacenters[key].stargate
<sup><sup>[↩ Parent](#k8ssandraclusterstatusdatacenterskey)</sup></sup>



StargateStatus defines the observed state of a Stargate resource.

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
        <td><b>availableReplicas</b></td>
        <td>integer</td>
        <td>
          Total number of available pods targeted by the Stargate deployment.
Will be zero if the deployment has not been created yet.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>readyReplicas</b></td>
        <td>integer</td>
        <td>
          ReadyReplicas is the total number of ready pods targeted by the Stargate deployment.
Will be zero if the deployment has not been created yet.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>replicas</b></td>
        <td>integer</td>
        <td>
          Total number of non-terminated pods targeted by the Stargate deployment (their labels match
the selector).
Will be zero if the deployment has not been created yet.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>updatedReplicas</b></td>
        <td>integer</td>
        <td>
          UpdatedReplicas is the total number of non-terminated pods targeted by the Stargate
deployment that have the desired template spec.
Will be zero if the deployment has not been created yet.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterstatusdatacenterskeystargateconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>deploymentRefs</b></td>
        <td>[]string</td>
        <td>
          DeploymentRefs is the names of the Deployment objects that were created for this Stargate
object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>progress</b></td>
        <td>enum</td>
        <td>
          Progress is the progress of this Stargate object.<br/>
          <br/>
            <i>Enum</i>: Pending, Deploying, Running<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>readyReplicasRatio</b></td>
        <td>string</td>
        <td>
          ReadyReplicasRatio is a "X/Y" string representing the ratio between ReadyReplicas and
Replicas in the Stargate deployment.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceRef</b></td>
        <td>string</td>
        <td>
          ServiceRef is the name of the Service object that was created for this Stargate
object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.status.datacenters[key].stargate.conditions[index]
<sup><sup>[↩ Parent](#k8ssandraclusterstatusdatacenterskeystargate)</sup></sup>





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
        <td><b>status</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          LastTransitionTime is the last time the condition transited from one status to another.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


## medusa.k8ssandra.io/v1alpha1

Resource Types:

- [CassandraBackup](#cassandrabackup)

- [CassandraRestore](#cassandrarestore)

- [MedusaBackupJob](#medusabackupjob)

- [MedusaBackup](#medusabackup)

- [MedusaBackupSchedule](#medusabackupschedule)

- [MedusaConfiguration](#medusaconfiguration)

- [MedusaRestoreJob](#medusarestorejob)

- [Medusa](#medusa)

- [MedusaTask](#medusatask)





### CassandraBackup
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






CassandraBackup is the Schema for the cassandrabackups API

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
      <td>CassandraBackup</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandrabackupspec">spec</a></b></td>
        <td>object</td>
        <td>
          CassandraBackupSpec defines the desired state of CassandraBackup<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandrabackupstatus">status</a></b></td>
        <td>object</td>
        <td>
          CassandraBackupStatus defines the observed state of CassandraBackup<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraBackup.spec
<sup><sup>[↩ Parent](#cassandrabackup)</sup></sup>



CassandraBackupSpec defines the desired state of CassandraBackup

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
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          The name of the backup. TODO document format of generated name<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraBackup.status
<sup><sup>[↩ Parent](#cassandrabackup)</sup></sup>



CassandraBackupStatus defines the observed state of CassandraBackup

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
        <td><b><a href="#cassandrabackupstatuscassdctemplatespec">cassdcTemplateSpec</a></b></td>
        <td>object</td>
        <td>
          <br/>
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



#### CassandraBackup.status.cassdcTemplateSpec
<sup><sup>[↩ Parent](#cassandrabackupstatus)</sup></sup>





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
        <td><b><a href="#cassandrabackupstatuscassdctemplatespecspec">spec</a></b></td>
        <td>object</td>
        <td>
          CassandraDatacenterSpec defines the desired state of a CassandraDatacenter<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>metadata</b></td>
        <td>object</td>
        <td>
          Standard object metadata<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
