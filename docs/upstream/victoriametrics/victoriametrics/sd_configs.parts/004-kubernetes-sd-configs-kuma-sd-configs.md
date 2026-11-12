<!-- Part 4 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## kubernetes_sd_configs

Kubernetes SD configuration allows retrieving scrape targets from [Kubernetes REST API](https://kubernetes.io/docs/reference/using-api/).

Configuration example:

```yaml
scrape_configs:
- job_name: kubernetes
  kubernetes_sd_configs:

    # role must contain the Kubernetes role of entities that should be discovered.
    # It must have one of the following values:
    # endpoints, endpointslice, service, pod, node or ingress.
    # See docs below about each particular role.
    #
  - role: "..."

    # api_server is an optional url for Kubernetes API server.
    # By default, it is read from /var/run/secrets/kubernetes.io/serviceaccount/
    #
    # api_server: "..."

    # kubeconfig_file is an optional path to a kubeconfig file.
    # Note that api_server and kubeconfig_file are mutually exclusive.
    #
    # kubeconfig_file: "..."

    # namespaces is an optional namespace for service discovery.
    # By default, all namespaces are used.
    # If own_namespace is set to true, then the current namespace is used for service discovery.
    #
    # namespaces:
    #   own_namespace: <boolean>
    #   names: ["...", "..."]

    # selects is an optional label and field selectors to limit the discovery process to a subset of available resources.
    # See https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/
    # and https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
    # The `role: endpoints` supports pod, service and endpoints selectors.
    # The `role: pod` supports node selectors when configured with `attach_metadata: {node: true}`.
    # Other roles only support selectors matching the role itself (e.g. node role can only contain node selectors).
    #
    # selectors:
    # - role: "..."
    #   label: "..."
    #   field: "..."

    # attach_metadata is an optional metadata to attach to discovered targets.
    # When `node` is set to true, then node metadata is attached to discovered targets.
    # Valid for roles: pod, endpoints, endpointslice.
    # When `namespace` is set to true, then namespace metadata is attached to discovered targets.
    # Valid for roles: pod, service, endpoints, endpointslice, ingress.
    #
    # Set `-promscrape.kubernetes.attachNodeMetadataAll` command-line flag
    # for attaching `node` metadata for all the discovered targets.
    # Set `-promscrape.kubernetes.attachNamespaceMetadataAll` command-line flag
    # for attaching `namespace` metadata for all the discovered targets.
    #
    # attach_metadata:
    #   node: <boolean>
    #   namespace: <boolean>

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

See [these examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/#kubernetes-target-discovery) on how to discover and scrape Kubernetes targets.

One of the following `role` types can be configured to discover targets:

### Kubernetes role: node

  The `role: node` discovers one target per cluster node.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<ip>:<port>`, where `<ip>` is to the first existing address of the Kubernetes node object in the address type order
  of `NodeInternalIP`, `NodeExternalIP`, `NodeLegacyHostIP` and `NodeHostName`,
  while `<port>` is the kubelet port on the given node.

  Available meta labels for `role: node` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kubernetes_node_name`: The name of the node object.
* `__meta_kubernetes_node_provider_id`: The cloud provider's name for the node object.
* `__meta_kubernetes_node_label_<labelname>`: Each label from the node object.
* `__meta_kubernetes_node_labelpresent_<labelname>`: "true" for each label from the node object.
* `__meta_kubernetes_node_annotation_<annotationname>`: Each annotation from the node object.
* `__meta_kubernetes_node_annotationpresent_<annotationname>`: "true" for each annotation from the node object.
* `__meta_kubernetes_node_address_<address_type>`: The first address for each node address type, if it exists.

  In addition, the `instance` label for the node will be set to the node name as retrieved from the API server.

### Kubernetes role: service

  The `role: service` discovers Kubernetes services.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<service_name>.<namespace>:<port>`, where `<service_name>` is the service name, `<namespace>` is the service namespace
  and `<port>` is the service port.
  If the service has multiple ports, then multiple targets are discovered for the service - one per each port.

  This is generally useful for blackbox monitoring of a service. The target address will be set to the Kubernetes DNS name
  of the service and respective service port.

  Available meta labels for `role: service` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kubernetes_namespace`: The namespace of the service object.
* `__meta_kubernetes_namespace_annotation_<annotationname>`: Each annotation from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_namespace_annotationpresent_<annotationname>`: "true" for each annotation from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_namespace_label_<labelname>`: Each label from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_namespace_labelpresent_<labelname>`: "true" for each label from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_service_annotation_<annotationname>`: Each annotation from the service object.
* `__meta_kubernetes_service_annotationpresent_<annotationname>`: "true" for each annotation of the service object.
* `__meta_kubernetes_service_cluster_ip`: The cluster IP address of the service. (Does not apply to services of type ExternalName)
* `__meta_kubernetes_service_external_name`: The DNS name of the service. (Applies to services of type ExternalName)
* `__meta_kubernetes_service_label_<labelname>`: Each label from the service object.
* `__meta_kubernetes_service_labelpresent_<labelname>`: "true" for each label of the service object.
* `__meta_kubernetes_service_name`: The name of the service object.
* `__meta_kubernetes_service_port_name`: Name of the service port for the target.
* `__meta_kubernetes_service_port_number`: Service port number for the target.
* `__meta_kubernetes_service_port_protocol`: Protocol of the service port for the target.
* `__meta_kubernetes_service_type`: The type of the service.

### Kubernetes role: pod

  The `role: pod` discovers all pods and exposes their containers as targets.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<ip>:<port>`, where `<ip>` is pod IP, while `<port>` is the exposed container port.
  If the pod has multiple container ports, then multiple targets are generated for the pod - one per each exposed container port.
  If the pod has no exposed container ports, then the `__address__` for pod target is set to the pod IP.

  Available meta labels for `role: pod` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kubernetes_namespace`: The namespace of the pod object.
* `__meta_kubernetes_namespace_annotation_<annotationname>`: Each annotation from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_namespace_annotationpresent_<annotationname>`: "true" for each annotation from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_namespace_label_<labelname>`: Each label from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_namespace_labelpresent_<labelname>`: "true" for each label from the namespace object. Available when `attach_metadata: {namespace: true}` is set.
* `__meta_kubernetes_pod_name`: The name of the pod object.
* `__meta_kubernetes_pod_ip`: The pod IP of the pod object.
* `__meta_kubernetes_pod_label_<labelname>`: Each label from the pod object.
* `__meta_kubernetes_pod_labelpresent_<labelname>`: "true" for each label from the pod object.
* `__meta_kubernetes_pod_annotation_<annotationname>`: Each annotation from the pod object.
* `__meta_kubernetes_pod_annotationpresent_<annotationname>`: "true" for each annotation from the pod object.
* `__meta_kubernetes_pod_container_id`: ID of the container in the form `<type>://<container_id>`.
* `__meta_kubernetes_pod_container_image`: Container image the target address points to.
* `__meta_kubernetes_pod_container_init`: "true" if the container is an InitContainer.
* `__meta_kubernetes_pod_container_name`: Name of the container the target address points to.
* `__meta_kubernetes_pod_container_port_name`: Name of the container port.
* `__meta_kubernetes_pod_container_port_number`: Number of the container port.
* `__meta_kubernetes_pod_container_port_protocol`: Protocol of the container port.
* `__meta_kubernetes_pod_ready`: Set to true or false for the pod's ready state.
* `__meta_kubernetes_pod_phase`: Set to Pending, Running, Succeeded, Failed or Unknown in the lifecycle.
* `__meta_kubernetes_pod_node_name`: The name of the node the pod is scheduled onto.
* `__meta_kubernetes_pod_host_ip`: The current host IP of the pod object.
* `__meta_kubernetes_pod_uid`: The UID of the pod object.
* `__meta_kubernetes_pod_controller_kind`: Object kind of the pod controller.
* `__meta_kubernetes_pod_controller_name`: Name of the pod controller.

### Kubernetes role: endpoints

  The `role: endpoints` discovers targets from listed endpoints of a service.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<addr>:<port>`, where `<addr>` is the endpoint address, while `<port>` is the endpoint port.
  If the endpoint has multiple ports, then a single target per each port is generated.
  If the endpoint is backed by a pod, all additional container ports of the pod, not bound to an endpoint port, are discovered as targets as well.

  Available meta labels for `role: endpoints` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kubernetes_namespace`: The namespace of the endpoints object.
* `__meta_kubernetes_namespace_annotation_<annotationname>`: Each annotation from the namespace of the endpoints object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_annotationpresent_<annotationname>`: "true" for each annotation from the namespace of the endpoints object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_label_<labelname>`: Each label from the namespace of the endpoints object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_labelpresent_<labelname>`: "true" for each label from the namespace of the endpoints object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_endpoints_name`: The names of the endpoints object.
* `__meta_kubernetes_endpoints_label_<labelname>`: Each label from the endpoints object.
* `__meta_kubernetes_endpoints_labelpresent_<labelname>`: "true" for each label from the endpoints object.

  For all targets discovered directly from the endpoints list (those not additionally inferred from underlying pods), the following labels are attached:

* `__meta_kubernetes_endpoint_hostname`: Hostname of the endpoint.
* `__meta_kubernetes_endpoint_node_name`: Name of the node hosting the endpoint.
* `__meta_kubernetes_endpoint_ready`: Set to true or false for the endpoint's ready state.
* `__meta_kubernetes_endpoint_port_name`: Name of the endpoint port.
* `__meta_kubernetes_endpoint_port_protocol`: Protocol of the endpoint port.
* `__meta_kubernetes_endpoint_address_target_kind`: Kind of the endpoint address target.
* `__meta_kubernetes_endpoint_address_target_name`: Name of the endpoint address target.

  If the endpoints belong to a service, all labels of the [`role: service`](#kubernetes-role-service) are attached.
  For all targets backed by a pod, all labels of the [`role: pod`](#kubernetes-role-pod) are attached.

### Kubernetes role: endpointslice

  The `role: endpointslice` discovers targets from existing endpointslices.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<addr>:<port>`, where `<addr>` is the endpoint address, while `<port>` is the endpoint port.
  If the endpoint has multiple ports, then a single target per each port is generated.
  If the endpoint is backed by a pod, all additional container ports of the pod, not bound to an endpoint port, are discovered as targets as well.

  Available meta labels for `role: endpointslice` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kubernetes_namespace`: The namespace of the endpointslice object.
* `__meta_kubernetes_namespace_annotation_<annotationname>`: Each annotation from the namespace of the endpointslice object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_annotationpresent_<annotationname>`: "true" for each annotation from the namespace of the endpointslice object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_label_<labelname>`: Each label from the namespace of the endpointslice object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_labelpresent_<labelname>`: "true" for each label from the namespace of the endpointslice object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_endpointslice_name`: The name of endpointslice object.

  For all targets discovered directly from the endpointslice list (those not additionally inferred from underlying pods), the following labels are attached:

* `__meta_kubernetes_endpointslice_address_target_kind`: Kind of the referenced object.
* `__meta_kubernetes_endpointslice_address_target_name`: Name of referenced object.
* `__meta_kubernetes_endpointslice_address_type`: The ip protocol family of the address of the target.
* `__meta_kubernetes_endpointslice_endpoint_conditions_ready`: Set to true or false for the referenced endpoint's ready state.
* `__meta_kubernetes_endpointslice_endpoint_topology_kubernetes_io_hostname`: Name of the node hosting the referenced endpoint.
* `__meta_kubernetes_endpointslice_endpoint_topology_present_kubernetes_io_hostname`: Flag that shows if the referenced object has a kubernetes.io/hostname annotation.
* `__meta_kubernetes_endpointslice_port`: Port of the referenced endpoint.
* `__meta_kubernetes_endpointslice_port_name`: Named port of the referenced endpoint.
* `__meta_kubernetes_endpointslice_port_protocol`: Protocol of the referenced endpoint.

  If the endpoints belong to a service, all labels of the [`role: service`](#kubernetes-role-service) are attached.
  For all targets backed by a pod, all labels of the [`role: pod`](#kubernetes-role-pod) are attached.

### Kubernetes role: ingress

  The `role: ingress` discovers a target for each path of each ingress.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to the host obtained from ingress spec.
  If the ingress has multiple specs with multiple hosts, then a target per each host is created.

  This is generally useful for blackbox monitoring of an ingress.

  Available meta labels for `role: ingress` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kubernetes_namespace`: The namespace of the ingress object.
* `__meta_kubernetes_namespace_annotation_<annotationname>`: Each annotation from the namespace of the ingress object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_annotationpresent_<annotationname>`: "true" for each annotation from the namespace of the ingress object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_label_<labelname>`: Each label from the namespace of the ingress object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_namespace_labelpresent_<labelname>`: "true" for each label from the namespace of the ingress object when `attach_metadata.namespace` is set to `true`.
* `__meta_kubernetes_ingress_name`: The name of the ingress object.
* `__meta_kubernetes_ingress_label_<labelname>`: Each label from the ingress object.
* `__meta_kubernetes_ingress_labelpresent_<labelname>`: "true" for each label from the ingress object.
* `__meta_kubernetes_ingress_annotation_<annotationname>`: Each annotation from the ingress object.
* `__meta_kubernetes_ingress_annotationpresent_<annotationname>`: "true" for each annotation from the ingress object.
* `__meta_kubernetes_ingress_class_name`: Class name from ingress spec, if present.
* `__meta_kubernetes_ingress_scheme`: Protocol scheme of ingress, https if TLS config is set. Defaults to http.
* `__meta_kubernetes_ingress_path`: Path from ingress spec. Defaults to `/`.

The list of discovered Kubernetes targets is refreshed at the interval, which can be configured via `-promscrape.kubernetesSDCheckInterval` command-line flag.


## kuma_sd_configs

Kuma service discovery config allows to fetch targets from the specified control plane `server` of [Kuma Service Mesh](https://kuma.io).

It discovers "monitoring assignments" based on Kuma Dataplane Proxies,
via the [MADS (Monitoring Assignment Discovery Service)](https://kuma.io/docs/2.10.x/policies/traffic-metrics/)
[xDS RESP API](http://envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol).

Configuration example:

```yaml
scrape_configs:
- job_name: kuma
  kuma_sd_configs:

    # server must contain the URL of Kuma Control Plane's MADS xDS server.
    #
  - server: "http://localhost:5676"

    # client_id is an optional client ID to send to Kuma Control Plane.
    # The hostname of the server where vmagent runs is used if it isn't set.
    # If the hostname is empty, then "vmagent" string is used as client_id.
    #
    # client_id: "..."

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

The `server` is queried periodically with the interval specified in `-promscrape.kumaSDCheckInterval` command-line flag.
Discovery errors are tracked in `promscrape_discovery_kuma_errors_total` metric.

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to one of the targets returned by the http service.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_kuma_mesh`: the name of the mesh
* `__meta_kuma_dataplane`: the name of the proxy
* `__meta_kuma_service`: the name of the service associated with the proxy
* `__meta_kuma_label_<label_name>`: each label of target given from Kuma Control Plane

The list of discovered Kuma targets is refreshed at the interval, which can be configured via `-promscrape.kumaSDCheckInterval` command-line flag.
