<!-- Part 116 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.reaper.telemetry
<sup><sup>[↩ Parent](#k8ssandraclusterspecreaper)</sup></sup>



Telemetry defines the desired telemetry integrations to deploy targeting the Reaper pods for all DCs in this cluster
(unless overridden by DC specific settings)

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
        <td><b><a href="#k8ssandraclusterspecreapertelemetrycassandra">cassandra</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetrymcac">mcac</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetryprometheus">prometheus</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvector">vector</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.cassandra
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetry)</sup></sup>





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
        <td><b><a href="#k8ssandraclusterspecreapertelemetrycassandraendpoint">endpoint</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetrycassandrarelabelsindex">relabels</a></b></td>
        <td>[]object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.cassandra.endpoint
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetrycassandra)</sup></sup>





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
        <td><b>address</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>port</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.cassandra.relabels[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetrycassandra)</sup></sup>



RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion.
It defines `<metric_relabel_configs>`-section of Prometheus configuration.
More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs

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
        <td><b>action</b></td>
        <td>string</td>
        <td>
          Action to perform based on regex matching. Default is 'replace'<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>modulus</b></td>
        <td>integer</td>
        <td>
          Modulus to take of the hash of the source label values.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>regex</b></td>
        <td>string</td>
        <td>
          Regular expression against which the extracted value is matched. Default is '(.*)'<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>replacement</b></td>
        <td>string</td>
        <td>
          Replacement value against which a regex replace is performed if the
regular expression matches. Regex capture groups are available. Default is '$1'<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>separator</b></td>
        <td>string</td>
        <td>
          Separator placed between concatenated source label values. default is ';'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sourceLabels</b></td>
        <td>[]string</td>
        <td>
          The source labels select values from existing labels. Their content is concatenated
using the configured separator and matched against the configured regular expression
for the replace, keep, and drop actions.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>targetLabel</b></td>
        <td>string</td>
        <td>
          Label to which the resulting value is written in a replace action.
It is mandatory for replace actions. Regex capture groups are available.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.mcac
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetry)</sup></sup>





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
          enabled sets whether MCAC (legacy metrics endpoint) is enabled.
This is considered true by default.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>metricFilters</b></td>
        <td>[]string</td>
        <td>
          MetricFilters allows passing filters to MCAC in order to reduce the amount of extracted metrics.
Not setting this field will result in the default filters being used:
- "deny:org.apache.cassandra.metrics.Table"
- "deny:org.apache.cassandra.metrics.table"
- "allow:org.apache.cassandra.metrics.table.live_ss_table_count"
- "allow:org.apache.cassandra.metrics.Table.LiveSSTableCount"
- "allow:org.apache.cassandra.metrics.table.live_disk_space_used"
- "allow:org.apache.cassandra.metrics.table.LiveDiskSpaceUsed"
- "allow:org.apache.cassandra.metrics.Table.Pending"
- "allow:org.apache.cassandra.metrics.Table.Memtable"
- "allow:org.apache.cassandra.metrics.Table.Compaction"
- "allow:org.apache.cassandra.metrics.table.read"
- "allow:org.apache.cassandra.metrics.table.write"
- "allow:org.apache.cassandra.metrics.table.range"
- "allow:org.apache.cassandra.metrics.table.coordinator"
- "allow:org.apache.cassandra.metrics.table.dropped_mutations"
Setting it to an empty list will result in all metrics being extracted.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.prometheus
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetry)</sup></sup>





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
        <td><b>commonLabels</b></td>
        <td>map[string]string</td>
        <td>
          CommonLabels are applied to all serviceMonitors created.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>enabled</b></td>
        <td>boolean</td>
        <td>
          Enable the creation of Prometheus serviceMonitors for this resource (Cassandra or Stargate).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.vector
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetry)</sup></sup>





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
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvectorcomponents">components</a></b></td>
        <td>object</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>enabled</b></td>
        <td>boolean</td>
        <td>
          Enabled enables the Vector agent for this resource (Cassandra, Reaper or Stargate).
Enabling the vector agent will inject a sidecar container into the pod.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>image</b></td>
        <td>string</td>
        <td>
          Image is the name of the Vector image to use. If not set, the default image will be used.
kube:default="timberio/vector:0.26.0-alpine"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvectorresources">resources</a></b></td>
        <td>object</td>
        <td>
          Resources is the resource requirements for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>scrapeInterval</b></td>
        <td>string</td>
        <td>
          ScrapeInterval is the interval at which the Vector agent will scrape the metrics endpoint.
Use values like 30s, 1m, 5m.
kube:default=30s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.vector.components
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetryvector)</sup></sup>





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
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvectorcomponentssinksindex">sinks</a></b></td>
        <td>[]object</td>
        <td>
          Sinks is the list of sinks to use for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvectorcomponentssourcesindex">sources</a></b></td>
        <td>[]object</td>
        <td>
          Sources is the list of sources to use for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvectorcomponentstransformsindex">transforms</a></b></td>
        <td>[]object</td>
        <td>
          Transforms is the list of transforms to use for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.vector.components.sinks[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetryvectorcomponents)</sup></sup>





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
          Name is the name of the sink.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          Type is the type of the sink.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>string</td>
        <td>
          Config is the configuration for the sink.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>inputs</b></td>
        <td>[]string</td>
        <td>
          Inputs is the list of inputs for the transform.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.vector.components.sources[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetryvectorcomponents)</sup></sup>





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
          Name is the name of the source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          Type is the type of the source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>string</td>
        <td>
          Config is the configuration for the source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.vector.components.transforms[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetryvectorcomponents)</sup></sup>





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
          Name is the name of the transform.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          Type is the type of the transform.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>string</td>
        <td>
          Config is the configuration for the transform.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>inputs</b></td>
        <td>[]string</td>
        <td>
          Inputs is the list of inputs for the transform.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.telemetry.vector.resources
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetryvector)</sup></sup>



Resources is the resource requirements for the Vector agent.

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
        <td><b><a href="#k8ssandraclusterspecreapertelemetryvectorresourcesclaimsindex">claims</a></b></td>
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



#### K8ssandraCluster.spec.reaper.telemetry.vector.resources.claims[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreapertelemetryvectorresources)</sup></sup>



ResourceClaim references one entry in PodSpec.ResourceClaims.

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
          Name must match the name of one entry in pod.spec.resourceClaims of
the Pod where this field is used. It makes that resource available
inside a container.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>request</b></td>
        <td>string</td>
        <td>
          Request is the name chosen for a request in the referenced claim.
If empty, everything from the claim is made available, otherwise
only the result of this request.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.tolerations[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspecreaper)</sup></sup>



The pod this Toleration is attached to tolerates any taint that matches
the triple <key,value,effect> using the matching operator <operator>.

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
          Effect indicates the taint effect to match. Empty means match all taint effects.
When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          Key is the taint key that the toleration applies to. Empty means match all taint keys.
If the key is empty, operator must be Exists; this combination means to match all values and all keys.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          Operator represents a key's relationship to the value.
Valid operators are Exists and Equal. Defaults to Equal.
Exists is equivalent to wildcard for value, so that a pod can
tolerate all taints of a particular category.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tolerationSeconds</b></td>
        <td>integer</td>
        <td>
          TolerationSeconds represents the period of time the toleration (which must be
of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default,
it is not set, which means tolerate the taint forever (do not evict). Zero and
negative values will be treated as 0 (evict immediately) by the system.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>value</b></td>
        <td>string</td>
        <td>
          Value is the taint value the toleration matches to.
If the operator is Exists, the value should be empty, otherwise just a regular string.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.reaper.uiUserSecretRef
<sup><sup>[↩ Parent](#k8ssandraclusterspecreaper)</sup></sup>



Defines the secret which contains the username and password for the Reaper UI and REST API authentication. When UiUserSecretRef.Name == "", authentication is turned off in the front-end only.

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
