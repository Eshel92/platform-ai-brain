<!-- Part 46 of 46 of reference/crd/cass-operator-crds-latest/_index.md (split because the page is big). -->

## control.k8ssandra.io/v1alpha1

Resource Types:

- [CassandraTask](#cassandratask)

- [ScheduledTask](#scheduledtask)




### CassandraTask
<sup><sup>[↩ Parent](#controlk8ssandraiov1alpha1 )</sup></sup>






CassandraTask is the Schema for the cassandrajobs API

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
      <td>control.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>CassandraTask</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandrataskspec">spec</a></b></td>
        <td>object</td>
        <td>
          CassandraTaskSpec defines the desired state of CassandraTask<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandrataskstatus">status</a></b></td>
        <td>object</td>
        <td>
          CassandraTaskStatus defines the observed state of CassandraJob<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraTask.spec
<sup><sup>[↩ Parent](#cassandratask)</sup></sup>



CassandraTaskSpec defines the desired state of CassandraTask

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
        <td><b>concurrencyPolicy</b></td>
        <td>string</td>
        <td>
          Specifics if this task can be run concurrently with other active tasks. Valid values are:
- "Allow": allows multiple Tasks to run concurrently on Cassandra cluster
- "Forbid" (default): only a single task is executed at once
The "Allow" property is only valid if all the other active Tasks have "Allow" as well.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandrataskspecdatacenter">datacenter</a></b></td>
        <td>object</td>
        <td>
          Which datacenter this task is targeting. Note, this must be a datacenter which the current cass-operator
can access<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandrataskspecjobsindex">jobs</a></b></td>
        <td>[]object</td>
        <td>
          Jobs defines the jobs this task will execute (and their order)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>restartPolicy</b></td>
        <td>string</td>
        <td>
          RestartPolicy indicates the behavior n case of failure. Default is Never.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>scheduledTime</b></td>
        <td>string</td>
        <td>
          ScheduledTime indicates the earliest possible time this task is executed. This does not necessarily
equal to the time it is actually executed (if other tasks are blocking for example). If not set,
the task will be executed immediately.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ttlSecondsAfterFinished</b></td>
        <td>integer</td>
        <td>
          TTLSecondsAfterFinished defines how long the completed job will kept before being cleaned up. If set to 0
the task will not be cleaned up by the cass-operator. If unset, the default time (86400s) is used.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraTask.spec.datacenter
<sup><sup>[↩ Parent](#cassandrataskspec)</sup></sup>



Which datacenter this task is targeting. Note, this must be a datacenter which the current cass-operator
can access

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
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraTask.spec.jobs[index]
<sup><sup>[↩ Parent](#cassandrataskspec)</sup></sup>





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
        <td><b>command</b></td>
        <td>string</td>
        <td>
          Command defines what is run against Cassandra pods<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#cassandrataskspecjobsindexargs">args</a></b></td>
        <td>object</td>
        <td>
          Arguments are additional parameters for the command<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraTask.spec.jobs[index].args
<sup><sup>[↩ Parent](#cassandrataskspecjobsindex)</sup></sup>



Arguments are additional parameters for the command

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
        <td><b>end_token</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jobs</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>keyspace_name</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>new_tokens</b></td>
        <td>map[string]string</td>
        <td>
          NewTokens is a map of pod names to their newly-assigned tokens. Required for the move
command, ignored otherwise. Pods referenced in this map must exist; any existing pod not
referenced in this map will not be moved.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>no_snapshot</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>no_validate</b></td>
        <td>boolean</td>
        <td>
          Scrub arguments<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pod_name</b></td>
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
        <td><b>skip_corrupted</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>source_datacenter</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>split_output</b></td>
        <td>boolean</td>
        <td>
          Compaction arguments<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>start_token</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tables</b></td>
        <td>[]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraTask.status
<sup><sup>[↩ Parent](#cassandratask)</sup></sup>



CassandraTaskStatus defines the observed state of CassandraJob

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
        <td><b>active</b></td>
        <td>integer</td>
        <td>
          The number of actively running pods.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>completionTime</b></td>
        <td>string</td>
        <td>
          Represents time when the job was completed. It is not guaranteed to
be set in happens-before order across separate operations.
It is represented in RFC3339 form and is in UTC.
The completion time is only set when the job finishes successfully.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandrataskstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          The latest available observations of an object's current state. When a Job
fails, one of the conditions will have type "Failed" and status true. When
a Job is suspended, one of the conditions will have type "Suspended" and
status true; when the Job is resumed, the status of this condition will
become false. When a Job is completed, one of the conditions will have
type "Complete" and status true.
More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failed</b></td>
        <td>integer</td>
        <td>
          The number of pods which reached phase Failed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>startTime</b></td>
        <td>string</td>
        <td>
          Represents time when the job controller started processing a job. When a
Job is created in the suspended state, this field is not set until the
first time it is resumed. This field is reset every time a Job is resumed
from suspension. It is represented in RFC3339 form and is in UTC.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>succeeded</b></td>
        <td>integer</td>
        <td>
          The number of pods which reached phase Succeeded.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### CassandraTask.status.conditions[index]
<sup><sup>[↩ Parent](#cassandrataskstatus)</sup></sup>



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

### ScheduledTask
<sup><sup>[↩ Parent](#controlk8ssandraiov1alpha1 )</sup></sup>






ScheduledTask is the Schema for the scheduledtasks API

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
      <td>control.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ScheduledTask</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#scheduledtaskspec">spec</a></b></td>
        <td>object</td>
        <td>
          ScheduledTaskSpec defines the desired state of ScheduledTask<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#scheduledtaskstatus">status</a></b></td>
        <td>object</td>
        <td>
          MedusaTaskStatus defines the observed state of MedusaTask<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ScheduledTask.spec
<sup><sup>[↩ Parent](#scheduledtask)</sup></sup>



ScheduledTaskSpec defines the desired state of ScheduledTask

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
        <td><b>schedule</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#scheduledtaskspectaskdetails">taskDetails</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ScheduledTask.spec.taskDetails
<sup><sup>[↩ Parent](#scheduledtaskspec)</sup></sup>





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
        <td><b>concurrencyPolicy</b></td>
        <td>string</td>
        <td>
          Specifics if this task can be run concurrently with other active tasks. Valid values are:
- "Allow": allows multiple Tasks to run concurrently on Cassandra cluster
- "Forbid" (default): only a single task is executed at once
The "Allow" property is only valid if all the other active Tasks have "Allow" as well.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#scheduledtaskspectaskdetailsdatacenter">datacenter</a></b></td>
        <td>object</td>
        <td>
          Which datacenter this task is targeting. Note, this must be a datacenter which the current cass-operator
can access<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#scheduledtaskspectaskdetailsjobsindex">jobs</a></b></td>
        <td>[]object</td>
        <td>
          Jobs defines the jobs this task will execute (and their order)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the task. Always populated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>restartPolicy</b></td>
        <td>string</td>
        <td>
          RestartPolicy indicates the behavior n case of failure. Default is Never.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>scheduledTime</b></td>
        <td>string</td>
        <td>
          ScheduledTime indicates the earliest possible time this task is executed. This does not necessarily
equal to the time it is actually executed (if other tasks are blocking for example). If not set,
the task will be executed immediately.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ttlSecondsAfterFinished</b></td>
        <td>integer</td>
        <td>
          TTLSecondsAfterFinished defines how long the completed job will kept before being cleaned up. If set to 0
the task will not be cleaned up by the cass-operator. If unset, the default time (86400s) is used.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ScheduledTask.spec.taskDetails.datacenter
<sup><sup>[↩ Parent](#scheduledtaskspectaskdetails)</sup></sup>



Which datacenter this task is targeting. Note, this must be a datacenter which the current cass-operator
can access

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
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ScheduledTask.spec.taskDetails.jobs[index]
<sup><sup>[↩ Parent](#scheduledtaskspectaskdetails)</sup></sup>





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
        <td><b>command</b></td>
        <td>string</td>
        <td>
          Command defines what is run against Cassandra pods<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#scheduledtaskspectaskdetailsjobsindexargs">args</a></b></td>
        <td>object</td>
        <td>
          Arguments are additional parameters for the command<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ScheduledTask.spec.taskDetails.jobs[index].args
<sup><sup>[↩ Parent](#scheduledtaskspectaskdetailsjobsindex)</sup></sup>



Arguments are additional parameters for the command

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
        <td><b>end_token</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jobs</b></td>
        <td>integer</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>keyspace_name</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>new_tokens</b></td>
        <td>map[string]string</td>
        <td>
          NewTokens is a map of pod names to their newly-assigned tokens. Required for the move
command, ignored otherwise. Pods referenced in this map must exist; any existing pod not
referenced in this map will not be moved.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>no_snapshot</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>no_validate</b></td>
        <td>boolean</td>
        <td>
          Scrub arguments<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pod_name</b></td>
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
        <td><b>skip_corrupted</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>source_datacenter</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>split_output</b></td>
        <td>boolean</td>
        <td>
          Compaction arguments<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>start_token</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tables</b></td>
        <td>[]string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ScheduledTask.status
<sup><sup>[↩ Parent](#scheduledtask)</sup></sup>



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
