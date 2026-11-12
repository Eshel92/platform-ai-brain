<!-- Part 167 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

### MedusaRestoreJob
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>






MedusaRestoreJob is the Schema for the medusarestorejobs API

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
      <td>MedusaRestoreJob</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusarestorejobspec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaRestoreJobSpec defines the desired state of MedusaRestoreJob<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusarestorejobstatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaRestoreJobStatus defines the observed state of MedusaRestoreJob<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaRestoreJob.spec
<sup><sup>[↩ Parent](#medusarestorejob)</sup></sup>



MedusaRestoreJobSpec defines the desired state of MedusaRestoreJob

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
          The name of the MedusaBackup to restore.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>cassandraDatacenter</b></td>
        <td>string</td>
        <td>
          Name of the Cassandra datacenter to perform the restore on.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


#### MedusaRestoreJob.status
<sup><sup>[↩ Parent](#medusarestorejob)</sup></sup>



MedusaRestoreJobStatus defines the observed state of MedusaRestoreJob

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
        <td><b>message</b></td>
        <td>string</td>
        <td>
          Message gives the reason why restore operation failed<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusarestorejobstatusrestoremapping">restoreMapping</a></b></td>
        <td>object</td>
        <td>
          Mapping between source and target nodes for a restore<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>restorePrepared</b></td>
        <td>boolean</td>
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


#### MedusaRestoreJob.status.restoreMapping
<sup><sup>[↩ Parent](#medusarestorejobstatus)</sup></sup>



Mapping between source and target nodes for a restore

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
        <td><b><a href="#medusarestorejobstatusrestoremappinghost_mapkey">host_map</a></b></td>
        <td>map[string]object</td>
        <td>
          Mapping between source and target nodes for a restore<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>in_place</b></td>
        <td>boolean</td>
        <td>
          Whether the restore is in-place or not<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### MedusaRestoreJob.status.restoreMapping.host_map[key]
<sup><sup>[↩ Parent](#medusarestorejobstatusrestoremapping)</sup></sup>





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
        <td><b>seed</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>source</b></td>
        <td>[]string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>
