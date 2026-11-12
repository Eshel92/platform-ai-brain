<!-- Part 173 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### Reaper.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].labelSelector
<sup><sup>[↩ Parent](#reaperspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindex)</sup></sup>



A label query over a set of resources, in this case pods.
If it's null, this PodAffinityTerm matches with no Pods.

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
        <td><b><a href="#reaperspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexlabelselectormatchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].labelSelector.matchExpressions[index]
<sup><sup>[↩ Parent](#reaperspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexlabelselector)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

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
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].namespaceSelector
<sup><sup>[↩ Parent](#reaperspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindex)</sup></sup>



A label query over the set of namespaces that the term applies to.
The term is applied to the union of the namespaces selected by this field
and the ones listed in the namespaces field.
null selector and null or empty namespaces list means "this pod's namespace".
An empty selector ({}) matches all namespaces.

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
        <td><b><a href="#reaperspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexnamespaceselectormatchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].namespaceSelector.matchExpressions[index]
<sup><sup>[↩ Parent](#reaperspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexnamespaceselector)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

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
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.autoScheduling
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



Auto scheduling properties. When you enable the auto-schedule feature, Reaper dynamically schedules repairs for
all non-system keyspaces in a cluster. A cluster's keyspaces are monitored and any modifications (additions or
removals) are detected. When a new keyspace is created, a new repair schedule is created automatically for that
keyspace. Conversely, when a keyspace is removed, the corresponding repair schedule is deleted.

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
        <td><b>enabled</b></td>
        <td>boolean</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>excludedClusters</b></td>
        <td>[]string</td>
        <td>
          ExcludedClusters are the clusters that are to be excluded from the repair schedule.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>excludedKeyspaces</b></td>
        <td>[]string</td>
        <td>
          ExcludedKeyspaces are the keyspaces that are to be excluded from the repair schedule.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>initialDelayPeriod</b></td>
        <td>string</td>
        <td>
          InitialDelay is the amount of delay time before the schedule period starts. Must be a valid ISO-8601 duration
string. The default is "PT15S" (15 seconds).<br/>
          <br/>
            <i>Default</i>: PT15S<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>percentUnrepairedThreshold</b></td>
        <td>integer</td>
        <td>
          PercentUnrepairedThreshold is the percentage of unrepaired data over which an incremental repair should be
started. Only relevant when using repair type INCREMENTAL.<br/>
          <br/>
            <i>Default</i>: 10<br/>
            <i>Minimum</i>: 0<br/>
            <i>Maximum</i>: 100<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>periodBetweenPolls</b></td>
        <td>string</td>
        <td>
          PeriodBetweenPolls is the interval time to wait before checking whether to start a repair task. Must be a valid
ISO-8601 duration string. The default is "PT10M" (10 minutes).<br/>
          <br/>
            <i>Default</i>: PT10M<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>repairType</b></td>
        <td>enum</td>
        <td>
          RepairType is the type of repair to create:
- REGULAR creates a regular repair (non-adaptive and non-incremental);
- ADAPTIVE creates an adaptive repair; adaptive repairs are most suited for Cassandra 3.
- INCREMENTAL creates an incremental repair; incremental repairs should only be used with Cassandra 4+.
- AUTO chooses between ADAPTIVE and INCREMENTAL depending on the Cassandra server version; ADAPTIVE for Cassandra
3 and INCREMENTAL for Cassandra 4+.<br/>
          <br/>
            <i>Enum</i>: REGULAR, ADAPTIVE, INCREMENTAL, AUTO<br/>
            <i>Default</i>: AUTO<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>scheduleSpreadPeriod</b></td>
        <td>string</td>
        <td>
          ScheduleSpreadPeriod is the time spacing between each of the repair schedules that is to be carried out. Must be
a valid ISO-8601 duration string. The default is "PT6H" (6 hours).<br/>
          <br/>
            <i>Default</i>: PT6H<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeBeforeFirstSchedule</b></td>
        <td>string</td>
        <td>
          TimeBeforeFirstSchedule is the grace period before the first repair in the schedule is started. Must be a valid
ISO-8601 duration string. The default is "PT5M" (5 minutes).<br/>
          <br/>
            <i>Default</i>: PT5M<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.cassandraUserSecretRef
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



Defines the username and password that Reaper will use to authenticate CQL connections to Cassandra clusters.
These credentials will be automatically turned into CQL roles by cass-operator when bootstrapping the datacenter,
then passed to the Reaper instance, so that it can authenticate against nodes in the datacenter using CQL. If CQL
authentication is not required, leave this field empty. The secret must be in the same namespace as Reaper itself
and must contain two keys: "username" and "password".

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



#### Reaper.spec.clientEncryptionStores
<sup><sup>[↩ Parent](#reaperspec)</sup></sup>



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
        <td><b><a href="#reaperspecclientencryptionstoreskeystoresecretref">keystoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore and optionally its password (which can also be specified through
the keystorePasswordSecretRef field)
if keys are not specified, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#reaperspecclientencryptionstorestruststoresecretref">truststoreSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore and optionally its password (which can also be specified through
the truststorePasswordSecretRef field)
if keys are not specified explicitly, "keystore" entry and a "keystore-password" entry will be used<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#reaperspecclientencryptionstoreskeystorepasswordsecretref">keystorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the keystore password if password stored in different secret than keystoreSecretRef
if key isn't specified explicitly, "keystore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#reaperspecclientencryptionstorestruststorepasswordsecretref">truststorePasswordSecretRef</a></b></td>
        <td>object</td>
        <td>
          ref to the secret that contains the truststore password if password stored in different secret than keystoreSecretRef
if key isn't specified  explicitly, "truststore-password" entry will be used<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### Reaper.spec.clientEncryptionStores.keystoreSecretRef
<sup><sup>[↩ Parent](#reaperspecclientencryptionstores)</sup></sup>



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



#### Reaper.spec.clientEncryptionStores.truststoreSecretRef
<sup><sup>[↩ Parent](#reaperspecclientencryptionstores)</sup></sup>



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



#### Reaper.spec.clientEncryptionStores.keystorePasswordSecretRef
<sup><sup>[↩ Parent](#reaperspecclientencryptionstores)</sup></sup>



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



#### Reaper.spec.clientEncryptionStores.truststorePasswordSecretRef
<sup><sup>[↩ Parent](#reaperspecclientencryptionstores)</sup></sup>



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
