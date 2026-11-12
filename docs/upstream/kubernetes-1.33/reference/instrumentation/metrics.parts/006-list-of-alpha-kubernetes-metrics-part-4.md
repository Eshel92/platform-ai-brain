<!-- Part 6 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

</div><div class="metric" data-stability="alpha">
	<div class="metric_name">horizontal_pod_autoscaler_controller_reconciliations_total</div>
	<div class="metric_help">Number of reconciliations of HPA controller. The label 'action' should be either 'scale_down', 'scale_up', or 'none'. Also, the label 'error' should be either 'spec', 'internal', or 'none'. Note that if both spec and internal errors happen during a reconciliation, the first one to occur is reported in `error` label.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span><span class="metric_label">error</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">job_controller_job_finished_indexes_total</div>
	<div class="metric_help">`The number of finished indexes. Possible values for the, 			status label are: "succeeded", "failed". Possible values for the, 			backoffLimit label are: "perIndex" and "global"`</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">backoffLimit</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">job_controller_job_pods_creation_total</div>
	<div class="metric_help">`The number of Pods created by the Job controller labelled with a reason for the Pod creation., This metric also distinguishes between Pods created using different PodReplacementPolicy settings., Possible values of the "reason" label are:, "new", "recreate_terminating_or_failed", "recreate_failed"., Possible values of the "status" label are:, "succeeded", "failed".`</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">reason</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">job_controller_jobs_by_external_controller_total</div>
	<div class="metric_help">The number of Jobs managed by an external controller</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">controller_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">job_controller_pod_failures_handled_by_failure_policy_total</div>
	<div class="metric_help">`The number of failed Pods handled by failure policy with, 			respect to the failure policy action applied based on the matched, 			rule. Possible values of the action label correspond to the, 			possible values for the failure policy rule action, which are:, 			"FailJob", "Ignore" and "Count".`</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">job_controller_terminated_pods_tracking_finalizer_total</div>
	<div class="metric_help">`The number of terminated pods (phase=Failed|Succeeded), that have the finalizer batch.kubernetes.io/job-tracking, The event label can be "add" or "delete".`</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">event</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_clusterip_allocator_allocated_ips</div>
	<div class="metric_help">Gauge measuring the number of allocated IPs for Services</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">cidr</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_clusterip_allocator_allocation_duration_seconds</div>
	<div class="metric_help">Duration in seconds to allocate a Cluster IP by ServiceCIDR</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">cidr</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_clusterip_allocator_allocation_errors_total</div>
	<div class="metric_help">Number of errors trying to allocate Cluster IPs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">cidr</span><span class="metric_label">scope</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_clusterip_allocator_allocation_total</div>
	<div class="metric_help">Number of Cluster IPs allocations</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">cidr</span><span class="metric_label">scope</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_clusterip_allocator_available_ips</div>
	<div class="metric_help">Gauge measuring the number of available IPs for Services</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">cidr</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_nodeport_allocator_allocated_ports</div>
	<div class="metric_help">Gauge measuring the number of allocated NodePorts for Services</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_nodeport_allocator_allocation_errors_total</div>
	<div class="metric_help">Number of errors trying to allocate NodePort</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">scope</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_nodeport_allocator_allocation_total</div>
	<div class="metric_help">Number of NodePort allocations</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">scope</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_nodeport_allocator_available_ports</div>
	<div class="metric_help">Gauge measuring the number of available NodePorts for Services</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_pod_logs_backend_tls_failure_total</div>
	<div class="metric_help">Total number of requests for pods/logs that failed due to kubelet server TLS verification</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_pod_logs_insecure_backend_total</div>
	<div class="metric_help">Total number of requests for pods/logs sliced by usage type: enforce_tls, skip_tls_allowed, skip_tls_denied</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">usage</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_pod_logs_pods_logs_backend_tls_failure_total</div>
	<div class="metric_help">Total number of requests for pods/logs that failed due to kubelet server TLS verification</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.27.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kube_apiserver_pod_logs_pods_logs_insecure_backend_total</div>
	<div class="metric_help">Total number of requests for pods/logs sliced by usage type: enforce_tls, skip_tls_allowed, skip_tls_denied</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">usage</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.27.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_active_pods</div>
	<div class="metric_help">The number of pods the kubelet considers active and which are being considered when admitting new pods. static is true if the pod is not from the apiserver.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">static</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_admission_rejections_total</div>
	<div class="metric_help">Cumulative number pod admission rejections by the Kubelet.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_certificate_manager_client_expiration_renew_errors</div>
	<div class="metric_help">Counter of certificate renewal errors.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_certificate_manager_client_ttl_seconds</div>
	<div class="metric_help">Gauge of the TTL (time-to-live) of the Kubelet's client certificate. The value is in seconds until certificate expiry (negative if already expired). If client certificate is invalid or unused, the value will be +INF.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_certificate_manager_server_rotation_seconds</div>
	<div class="metric_help">Histogram of the number of seconds the previous certificate lived before being rotated.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_certificate_manager_server_ttl_seconds</div>
	<div class="metric_help">Gauge of the shortest TTL (time-to-live) of the Kubelet's serving certificate. The value is in seconds until certificate expiry (negative if already expired). If serving certificate is invalid or unused, the value will be +INF.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cgroup_manager_duration_seconds</div>
	<div class="metric_help">Duration in seconds for cgroup manager operations. Broken down by method.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cgroup_version</div>
	<div class="metric_help">cgroup version on the hosts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_container_aligned_compute_resources_count</div>
	<div class="metric_help">Cumulative number of aligned compute resources allocated to containers by alignment type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">boundary</span><span class="metric_label">scope</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_container_aligned_compute_resources_failure_count</div>
	<div class="metric_help">Cumulative number of failures to allocate aligned compute resources to containers by alignment type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">boundary</span><span class="metric_label">scope</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_container_log_filesystem_used_bytes</div>
	<div class="metric_help">Bytes used by the container's logs on the filesystem.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">uid</span><span class="metric_label">namespace</span><span class="metric_label">pod</span><span class="metric_label">container</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_containers_per_pod_count</div>
	<div class="metric_help">The number of containers per pod.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cpu_manager_allocation_per_numa</div>
	<div class="metric_help">Number of CPUs allocated per NUMA node</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">numa_node</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cpu_manager_exclusive_cpu_allocation_count</div>
	<div class="metric_help">The total number of CPUs exclusively allocated to containers running on this node</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cpu_manager_pinning_errors_total</div>
	<div class="metric_help">The number of cpu core allocations which required pinning failed.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cpu_manager_pinning_requests_total</div>
	<div class="metric_help">The number of cpu core allocations which required pinning.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_cpu_manager_shared_pool_size_millicores</div>
	<div class="metric_help">The size of the shared CPU pool for non-guaranteed QoS pods, in millicores.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_credential_provider_plugin_duration</div>
	<div class="metric_help">Duration of execution in seconds for credential provider plugin</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_credential_provider_plugin_errors</div>
	<div class="metric_help">Number of errors from credential provider plugin</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_desired_pods</div>
	<div class="metric_help">The number of pods the kubelet is being instructed to run. static is true if the pod is not from the apiserver.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">static</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_device_plugin_alloc_duration_seconds</div>
	<div class="metric_help">Duration in seconds to serve a device plugin Allocation request. Broken down by resource name.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_device_plugin_registration_total</div>
	<div class="metric_help">Cumulative number of device plugin registrations. Broken down by resource name.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_evented_pleg_connection_error_count</div>
	<div class="metric_help">The number of errors encountered during the establishment of streaming connection with the CRI runtime.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_evented_pleg_connection_latency_seconds</div>
	<div class="metric_help">The latency of streaming connection with the CRI runtime, measured in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_evented_pleg_connection_success_count</div>
	<div class="metric_help">The number of times a streaming client was obtained to receive CRI Events.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_eviction_stats_age_seconds</div>
	<div class="metric_help">Time between when stats are collected, and when pod is evicted based on those stats by eviction signal</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">eviction_signal</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_evictions</div>
	<div class="metric_help">Cumulative number of pod evictions by eviction signal</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">eviction_signal</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_graceful_shutdown_end_time_seconds</div>
	<div class="metric_help">Last graceful shutdown end time since unix epoch in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_graceful_shutdown_start_time_seconds</div>
	<div class="metric_help">Last graceful shutdown start time since unix epoch in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_http_inflight_requests</div>
	<div class="metric_help">Number of the inflight http requests</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">long_running</span><span class="metric_label">method</span><span class="metric_label">path</span><span class="metric_label">server_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_http_requests_duration_seconds</div>
	<div class="metric_help">Duration in seconds to serve http requests</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">long_running</span><span class="metric_label">method</span><span class="metric_label">path</span><span class="metric_label">server_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_http_requests_total</div>
	<div class="metric_help">Number of the http requests received since the server started</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">long_running</span><span class="metric_label">method</span><span class="metric_label">path</span><span class="metric_label">server_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_image_garbage_collected_total</div>
	<div class="metric_help">Total number of images garbage collected by the kubelet, whether through disk usage or image age.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_image_pull_duration_seconds</div>
	<div class="metric_help">Duration in seconds to pull an image.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">image_size_in_bytes</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_image_volume_mounted_errors_total</div>
	<div class="metric_help">Number of failed image volume mounts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_image_volume_mounted_succeed_total</div>
	<div class="metric_help">Number of successful image volume mounts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_image_volume_requested_total</div>
	<div class="metric_help">Number of requested image volumes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_lifecycle_handler_http_fallbacks_total</div>
	<div class="metric_help">The number of times lifecycle handlers successfully fell back to http from https.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_managed_ephemeral_containers</div>
	<div class="metric_help">Current number of ephemeral containers in pods managed by this kubelet.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_memory_manager_pinning_errors_total</div>
	<div class="metric_help">The number of memory pages allocations which required pinning that failed.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_memory_manager_pinning_requests_total</div>
	<div class="metric_help">The number of memory pages allocations which required pinning.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_mirror_pods</div>
	<div class="metric_help">The number of mirror pods the kubelet will try to create (one per admitted static pod)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_node_name</div>
	<div class="metric_help">The node's name. The count is always 1.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">node</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_node_startup_duration_seconds</div>
	<div class="metric_help">Duration in seconds of node startup in total.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_node_startup_post_registration_duration_seconds</div>
	<div class="metric_help">Duration in seconds of node startup after registration.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_node_startup_pre_kubelet_duration_seconds</div>
	<div class="metric_help">Duration in seconds of node startup before kubelet starts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_node_startup_pre_registration_duration_seconds</div>
	<div class="metric_help">Duration in seconds of node startup before registration.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_node_startup_registration_duration_seconds</div>
	<div class="metric_help">Duration in seconds of node startup during registration.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_orphan_pod_cleaned_volumes</div>
	<div class="metric_help">The total number of orphaned Pods whose volumes were cleaned in the last periodic sweep.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_orphan_pod_cleaned_volumes_errors</div>
	<div class="metric_help">The number of orphaned Pods whose volumes failed to be cleaned in the last periodic sweep.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_orphaned_runtime_pods_total</div>
	<div class="metric_help">Number of pods that have been detected in the container runtime without being already known to the pod worker. This typically indicates the kubelet was restarted while a pod was force deleted in the API or in the local configuration, which is unusual.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pleg_discard_events</div>
	<div class="metric_help">The number of discard events in PLEG.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pleg_last_seen_seconds</div>
