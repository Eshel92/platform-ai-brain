<!-- Part 21 of 46 of reference/crd/cass-operator-crds-latest/_index.md (split because the page is big). -->

#### CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].labelSelector
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindex)</sup></sup>



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
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexlabelselectormatchexpressionsindex">matchExpressions</a></b></td>
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



#### CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].labelSelector.matchExpressions[index]
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexlabelselector)</sup></sup>



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



#### CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].namespaceSelector
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindex)</sup></sup>



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
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexnamespaceselectormatchexpressionsindex">matchExpressions</a></b></td>
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



#### CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[index].namespaceSelector.matchExpressions[index]
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspecaffinitypodantiaffinityrequiredduringschedulingignoredduringexecutionindexnamespaceselector)</sup></sup>



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



#### CassandraDatacenter.spec.podTemplateSpec.spec.dnsConfig
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspec)</sup></sup>



Specifies the DNS parameters of a pod.
Parameters specified here will be merged to the generated DNS
configuration based on DNSPolicy.

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
        <td><b>nameservers</b></td>
        <td>[]string</td>
        <td>
          A list of DNS name server IP addresses.
This will be appended to the base nameservers generated from DNSPolicy.
Duplicated nameservers will be removed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecdnsconfigoptionsindex">options</a></b></td>
        <td>[]object</td>
        <td>
          A list of DNS resolver options.
This will be merged with the base options generated from DNSPolicy.
Duplicated entries will be removed. Resolution options given in Options
will override those that appear in the base DNSPolicy.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>searches</b></td>
        <td>[]string</td>
        <td>
          A list of DNS search domains for host-name lookup.
This will be appended to the base search paths generated from DNSPolicy.
Duplicated search paths will be removed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraDatacenter.spec.podTemplateSpec.spec.dnsConfig.options[index]
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspecdnsconfig)</sup></sup>



PodDNSConfigOption defines DNS resolver options of a pod.

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
          Name is this DNS resolver option's name.
Required.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>value</b></td>
        <td>string</td>
        <td>
          Value is this DNS resolver option's value.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>



#### CassandraDatacenter.spec.podTemplateSpec.spec.ephemeralContainers[index]
<sup><sup>[↩ Parent](#cassandradatacenterspecpodtemplatespecspec)</sup></sup>



An EphemeralContainer is a temporary container that you may add to an existing Pod for
user-initiated activities such as debugging. Ephemeral containers have no resource or
scheduling guarantees, and they will not be restarted when they exit or when a Pod is
removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the
Pod to exceed its resource allocation.

To add an ephemeral container, use the ephemeralcontainers subresource of an existing
Pod. Ephemeral containers may not be removed or restarted.

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
          Name of the ephemeral container specified as a DNS_LABEL.
This name must be unique among all containers, init containers and ephemeral containers.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>args</b></td>
        <td>[]string</td>
        <td>
          Arguments to the entrypoint.
The image's CMD is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container's environment. If a variable
cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced
to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will
produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless
of whether the variable exists or not. Cannot be updated.
More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>command</b></td>
        <td>[]string</td>
        <td>
          Entrypoint array. Not executed within a shell.
The image's ENTRYPOINT is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container's environment. If a variable
cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced
to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will
produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless
of whether the variable exists or not. Cannot be updated.
More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexenvindex">env</a></b></td>
        <td>[]object</td>
        <td>
          List of environment variables to set in the container.
Cannot be updated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexenvfromindex">envFrom</a></b></td>
        <td>[]object</td>
        <td>
          List of sources to populate environment variables in the container.
The keys defined within a source must be a C_IDENTIFIER. All invalid keys
will be reported as an event when the container is starting. When a key exists in multiple
sources, the value associated with the last source will take precedence.
Values defined by an Env with a duplicate key will take precedence.
Cannot be updated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>image</b></td>
        <td>string</td>
        <td>
          Container image name.
More info: https://kubernetes.io/docs/concepts/containers/images<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>imagePullPolicy</b></td>
        <td>string</td>
        <td>
          Image pull policy.
One of Always, Never, IfNotPresent.
Defaults to Always if :latest tag is specified, or IfNotPresent otherwise.
Cannot be updated.
More info: https://kubernetes.io/docs/concepts/containers/images#updating-images<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexlifecycle">lifecycle</a></b></td>
        <td>object</td>
        <td>
          Lifecycle is not allowed for ephemeral containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexlivenessprobe">livenessProbe</a></b></td>
        <td>object</td>
        <td>
          Probes are not allowed for ephemeral containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexportsindex">ports</a></b></td>
        <td>[]object</td>
        <td>
          Ports are not allowed for ephemeral containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexreadinessprobe">readinessProbe</a></b></td>
        <td>object</td>
        <td>
          Probes are not allowed for ephemeral containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexresizepolicyindex">resizePolicy</a></b></td>
        <td>[]object</td>
        <td>
          Resources resize policy for the container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexresources">resources</a></b></td>
        <td>object</td>
        <td>
          Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources
already allocated to the pod.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>restartPolicy</b></td>
        <td>string</td>
        <td>
          Restart policy for the container to manage the restart behavior of each
container within a pod.
This may only be set for init containers. You cannot set this field on
ephemeral containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexsecuritycontext">securityContext</a></b></td>
        <td>object</td>
        <td>
          Optional: SecurityContext defines the security options the ephemeral container should be run with.
If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexstartupprobe">startupProbe</a></b></td>
        <td>object</td>
        <td>
          Probes are not allowed for ephemeral containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stdin</b></td>
        <td>boolean</td>
        <td>
          Whether this container should allocate a buffer for stdin in the container runtime. If this
is not set, reads from stdin in the container will always result in EOF.
Default is false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stdinOnce</b></td>
        <td>boolean</td>
        <td>
          Whether the container runtime should close the stdin channel after it has been opened by
a single attach. When stdin is true the stdin stream will remain open across multiple attach
sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the
first client attaches to stdin, and then remains open and accepts data until the client disconnects,
at which time stdin is closed and remains closed until the container is restarted. If this
flag is false, a container processes that reads from stdin will never receive an EOF.
Default is false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>targetContainerName</b></td>
        <td>string</td>
        <td>
          If set, the name of the container from PodSpec that this ephemeral container targets.
The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container.
If not set then the ephemeral container uses the namespaces configured in the Pod spec.

The container runtime must implement support for this feature. If the runtime does not
support namespace targeting then the result of setting this field is undefined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>terminationMessagePath</b></td>
        <td>string</td>
        <td>
          Optional: Path at which the file to which the container's termination message
will be written is mounted into the container's filesystem.
Message written is intended to be brief final status, such as an assertion failure message.
Will be truncated by the node if greater than 4096 bytes. The total message length across
all containers will be limited to 12kb.
Defaults to /dev/termination-log.
Cannot be updated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>terminationMessagePolicy</b></td>
        <td>string</td>
        <td>
          Indicate how the termination message should be populated. File will use the contents of
terminationMessagePath to populate the container status message on both success and failure.
FallbackToLogsOnError will use the last chunk of container log output if the termination
message file is empty and the container exited with an error.
The log output is limited to 2048 bytes or 80 lines, whichever is smaller.
Defaults to File.
Cannot be updated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tty</b></td>
        <td>boolean</td>
        <td>
          Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.
Default is false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexvolumedevicesindex">volumeDevices</a></b></td>
        <td>[]object</td>
        <td>
          volumeDevices is the list of block devices to be used by the container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#cassandradatacenterspecpodtemplatespecspecephemeralcontainersindexvolumemountsindex">volumeMounts</a></b></td>
        <td>[]object</td>
        <td>
          Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers.
Cannot be updated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>workingDir</b></td>
        <td>string</td>
        <td>
          Container's working directory.
If not specified, the container runtime's default will be used, which
might be configured in the container image.
Cannot be updated.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
