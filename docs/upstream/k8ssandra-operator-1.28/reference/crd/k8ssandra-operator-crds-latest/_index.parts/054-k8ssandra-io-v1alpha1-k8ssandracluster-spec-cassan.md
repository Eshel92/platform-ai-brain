<!-- Part 54 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.mcac
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetry)</sup></sup>





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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.prometheus
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetry)</sup></sup>





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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetry)</sup></sup>





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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponents">components</a></b></td>
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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorresources">resources</a></b></td>
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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector.components
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvector)</sup></sup>





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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponentssinksindex">sinks</a></b></td>
        <td>[]object</td>
        <td>
          Sinks is the list of sinks to use for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponentssourcesindex">sources</a></b></td>
        <td>[]object</td>
        <td>
          Sources is the list of sources to use for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponentstransformsindex">transforms</a></b></td>
        <td>[]object</td>
        <td>
          Transforms is the list of transforms to use for the Vector agent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector.components.sinks[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponents)</sup></sup>





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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector.components.sources[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponents)</sup></sup>





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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector.components.transforms[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorcomponents)</sup></sup>





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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector.resources
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvector)</sup></sup>



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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorresourcesclaimsindex">claims</a></b></td>
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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].telemetry.vector.resources.claims[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindextelemetryvectorresources)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.racks[index].tolerations[index]
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargateracksindex)</sup></sup>



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



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.readinessProbe
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargate)</sup></sup>



ReadinessProbe sets the Stargate readiness probe. Leave nil to use defaults.

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
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargatereadinessprobeexec">exec</a></b></td>
        <td>object</td>
        <td>
          Exec specifies a command to execute in the container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failureThreshold</b></td>
        <td>integer</td>
        <td>
          Minimum consecutive failures for the probe to be considered failed after having succeeded.
Defaults to 3. Minimum value is 1.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargatereadinessprobegrpc">grpc</a></b></td>
        <td>object</td>
        <td>
          GRPC specifies a GRPC HealthCheckRequest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargatereadinessprobehttpget">httpGet</a></b></td>
        <td>object</td>
        <td>
          HTTPGet specifies an HTTP GET request to perform.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>initialDelaySeconds</b></td>
        <td>integer</td>
        <td>
          Number of seconds after the container has started before liveness probes are initiated.
More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>periodSeconds</b></td>
        <td>integer</td>
        <td>
          How often (in seconds) to perform the probe.
Default to 10 seconds. Minimum value is 1.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>successThreshold</b></td>
        <td>integer</td>
        <td>
          Minimum consecutive successes for the probe to be considered successful after having failed.
Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#k8ssandraclusterspeccassandradatacentersindexstargatereadinessprobetcpsocket">tcpSocket</a></b></td>
        <td>object</td>
        <td>
          TCPSocket specifies a connection to a TCP port.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>terminationGracePeriodSeconds</b></td>
        <td>integer</td>
        <td>
          Optional duration in seconds the pod needs to terminate gracefully upon probe failure.
The grace period is the duration in seconds after the processes running in the pod are sent
a termination signal and the time when the processes are forcibly halted with a kill signal.
Set this value longer than the expected cleanup time for your process.
If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this
value overrides the value provided by the pod spec.
Value must be non-negative integer. The value zero indicates stop immediately via
the kill signal (no opportunity to shut down).
This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate.
Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeoutSeconds</b></td>
        <td>integer</td>
        <td>
          Number of seconds after which the probe times out.
Defaults to 1 second. Minimum value is 1.
More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes<br/>
          <br/>
            <i>Format</i>: int32<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### K8ssandraCluster.spec.cassandra.datacenters[index].stargate.readinessProbe.exec
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexstargatereadinessprobe)</sup></sup>



Exec specifies a command to execute in the container.

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
        <td>[]string</td>
        <td>
          Command is the command line to execute inside the container, the working directory for the
command  is root ('/') in the container's filesystem. The command is simply exec'd, it is
not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use
a shell, you need to explicitly call out to that shell.
Exit status of 0 is treated as live/healthy and non-zero is unhealthy.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
