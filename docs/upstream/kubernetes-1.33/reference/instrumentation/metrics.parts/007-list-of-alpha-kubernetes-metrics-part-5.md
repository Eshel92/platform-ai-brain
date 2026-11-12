<!-- Part 7 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

<div class="metric_help">Timestamp in seconds when PLEG was last seen active.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pleg_relist_duration_seconds</div>
	<div class="metric_help">Duration in seconds for relisting pods in PLEG.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pleg_relist_interval_seconds</div>
	<div class="metric_help">Interval in seconds between relisting in PLEG.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_errors_get</div>
	<div class="metric_help">Number of requests to the PodResource Get endpoint which returned error. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_errors_get_allocatable</div>
	<div class="metric_help">Number of requests to the PodResource GetAllocatableResources endpoint which returned error. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_errors_list</div>
	<div class="metric_help">Number of requests to the PodResource List endpoint which returned error. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_requests_get</div>
	<div class="metric_help">Number of requests to the PodResource Get endpoint. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_requests_get_allocatable</div>
	<div class="metric_help">Number of requests to the PodResource GetAllocatableResources endpoint. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_requests_list</div>
	<div class="metric_help">Number of requests to the PodResource List endpoint. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_resources_endpoint_requests_total</div>
	<div class="metric_help">Cumulative number of requests to the PodResource endpoint. Broken down by server api version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">server_api_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_start_duration_seconds</div>
	<div class="metric_help">Duration in seconds from kubelet seeing a pod for the first time to the pod starting to run</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_start_sli_duration_seconds</div>
	<div class="metric_help">Duration in seconds to start a pod, excluding time to pull images and run init containers, measured from pod creation timestamp to when all its containers are reported as started and observed via watch</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_start_total_duration_seconds</div>
	<div class="metric_help">Duration in seconds to start a pod since creation, including time to pull images and run init containers, measured from pod creation timestamp to when all its containers are reported as started and observed via watch</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_status_sync_duration_seconds</div>
	<div class="metric_help">Duration in seconds to sync a pod status update. Measures time from detection of a change to pod status until the API is successfully updated for that pod, even if multiple intevening changes to pod status occur.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_worker_duration_seconds</div>
	<div class="metric_help">Duration in seconds to sync a single pod. Broken down by operation type: create, update, or sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_pod_worker_start_duration_seconds</div>
	<div class="metric_help">Duration in seconds from kubelet seeing a pod to starting a worker.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_preemptions</div>
	<div class="metric_help">Cumulative number of pod preemptions by preemption resource</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">preemption_signal</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_restarted_pods_total</div>
	<div class="metric_help">Number of pods that have been restarted because they were deleted and recreated with the same UID while the kubelet was watching them (common for static pods, extremely uncommon for API pods)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">static</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_run_podsandbox_duration_seconds</div>
	<div class="metric_help">Duration in seconds of the run_podsandbox operations. Broken down by RuntimeClass.Handler.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">runtime_handler</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_run_podsandbox_errors_total</div>
	<div class="metric_help">Cumulative number of the run_podsandbox operation errors by RuntimeClass.Handler.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">runtime_handler</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_running_containers</div>
	<div class="metric_help">Number of containers currently running</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container_state</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_running_pods</div>
	<div class="metric_help">Number of pods that have a running pod sandbox</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_runtime_operations_duration_seconds</div>
	<div class="metric_help">Duration in seconds of runtime operations. Broken down by operation type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_runtime_operations_errors_total</div>
	<div class="metric_help">Cumulative number of runtime operation errors by operation type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_runtime_operations_total</div>
	<div class="metric_help">Cumulative number of runtime operations by operation type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_server_expiration_renew_errors</div>
	<div class="metric_help">Counter of certificate renewal errors.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_sleep_action_terminated_early_total</div>
	<div class="metric_help">The number of times lifecycle sleep handler got terminated before it finishes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_started_containers_errors_total</div>
	<div class="metric_help">Cumulative number of errors when starting containers</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">container_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_started_containers_total</div>
	<div class="metric_help">Cumulative number of containers started</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_started_host_process_containers_errors_total</div>
	<div class="metric_help">Cumulative number of errors when starting hostprocess containers. This metric will only be collected on Windows.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">container_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_started_host_process_containers_total</div>
	<div class="metric_help">Cumulative number of hostprocess containers started. This metric will only be collected on Windows.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_started_pods_errors_total</div>
	<div class="metric_help">Cumulative number of errors when starting pods</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_started_pods_total</div>
	<div class="metric_help">Cumulative number of pods started</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_topology_manager_admission_duration_ms</div>
	<div class="metric_help">Duration in milliseconds to serve a pod admission request.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_topology_manager_admission_errors_total</div>
	<div class="metric_help">The number of admission request failures where resources could not be aligned.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_topology_manager_admission_requests_total</div>
	<div class="metric_help">The number of admission requests where resources have to be aligned.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_metric_collection_duration_seconds</div>
	<div class="metric_help">Duration in seconds to calculate volume stats</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">metric_source</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_available_bytes</div>
	<div class="metric_help">Number of available bytes in the volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_capacity_bytes</div>
	<div class="metric_help">Capacity in bytes of the volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_health_status_abnormal</div>
	<div class="metric_help">Abnormal volume health status. The count is either 1 or 0. 1 indicates the volume is unhealthy, 0 indicates volume is healthy</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_inodes</div>
	<div class="metric_help">Maximum number of inodes in the volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_inodes_free</div>
	<div class="metric_help">Number of free inodes in the volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_inodes_used</div>
	<div class="metric_help">Number of used inodes in the volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_volume_stats_used_bytes</div>
	<div class="metric_help">Number of used bytes in the volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">persistentvolumeclaim</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubelet_working_pods</div>
	<div class="metric_help">Number of pods the kubelet is actually running, broken down by lifecycle phase, whether the pod is desired, orphaned, or runtime only (also orphaned), and whether the pod is static. An orphaned pod has been removed from local configuration or force deleted in the API and consumes resources that are not otherwise visible.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">config</span><span class="metric_label">lifecycle</span><span class="metric_label">static</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_conntrack_reconciler_deleted_entries_total</div>
	<div class="metric_help">Cumulative conntrack flows deleted by conntrack reconciler</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_conntrack_reconciler_sync_duration_seconds</div>
	<div class="metric_help">ReconcileConntrackFlowsLatency latency in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_iptables_ct_state_invalid_dropped_packets_total</div>
	<div class="metric_help">packets dropped by iptables to work around conntrack problems</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_iptables_localhost_nodeports_accepted_packets_total</div>
	<div class="metric_help">Number of packets accepted on nodeports of loopback interface</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_network_programming_duration_seconds</div>
	<div class="metric_help">In Cluster Network Programming Latency in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_proxy_healthz_total</div>
	<div class="metric_help">Cumulative proxy healthz HTTP status</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_proxy_livez_total</div>
	<div class="metric_help">Cumulative proxy livez HTTP status</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_full_proxy_rules_duration_seconds</div>
	<div class="metric_help">SyncProxyRules latency in seconds for full resyncs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_partial_proxy_rules_duration_seconds</div>
	<div class="metric_help">SyncProxyRules latency in seconds for partial resyncs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_duration_seconds</div>
	<div class="metric_help">SyncProxyRules latency in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_endpoint_changes_pending</div>
	<div class="metric_help">Pending proxy rules Endpoint changes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_endpoint_changes_total</div>
	<div class="metric_help">Cumulative proxy rules Endpoint changes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_iptables_last</div>
	<div class="metric_help">Number of iptables rules written by kube-proxy in last sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span><span class="metric_label">table</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_iptables_partial_restore_failures_total</div>
	<div class="metric_help">Cumulative proxy iptables partial restore failures</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_iptables_restore_failures_total</div>
	<div class="metric_help">Cumulative proxy iptables restore failures</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_iptables_total</div>
	<div class="metric_help">Total number of iptables rules owned by kube-proxy</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span><span class="metric_label">table</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_last_queued_timestamp_seconds</div>
	<div class="metric_help">The last time a sync of proxy rules was queued</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_last_timestamp_seconds</div>
	<div class="metric_help">The last time proxy rules were successfully synced</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_nftables_cleanup_failures_total</div>
	<div class="metric_help">Cumulative proxy nftables cleanup failures</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_nftables_sync_failures_total</div>
	<div class="metric_help">Cumulative proxy nftables sync failures</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_no_local_endpoints_total</div>
	<div class="metric_help">Number of services with a Local traffic policy and no endpoints</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">ip_family</span><span class="metric_label">traffic_policy</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_service_changes_pending</div>
	<div class="metric_help">Pending proxy rules Service changes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubeproxy_sync_proxy_rules_service_changes_total</div>
	<div class="metric_help">Cumulative proxy rules Service changes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">kubernetes_build_info</div>
	<div class="metric_help">A metric with a constant '1' value labeled by major, minor, git version, git commit, git tree state, build date, Go version, and compiler from which Kubernetes was built, and platform on which it is running.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">build_date</span><span class="metric_label">compiler</span><span class="metric_label">git_commit</span><span class="metric_label">git_tree_state</span><span class="metric_label">git_version</span><span class="metric_label">go_version</span><span class="metric_label">major</span><span class="metric_label">minor</span><span class="metric_label">platform</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">leader_election_master_status</div>
	<div class="metric_help">Gauge of if the reporting system is master of the relevant lease, 0 indicates backup, 1 indicates master. 'name' is the string used to identify the lease. Please make sure to group by name.</div>
	<ul>
