<!-- Part 8 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">leader_election_slowpath_total</div>
	<div class="metric_help">Total number of slow path exercised in renewing leader leases. 'name' is the string used to identify the lease. Please make sure to group by name.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_authorizer_graph_actions_duration_seconds</div>
	<div class="metric_help">Histogram of duration of graph actions in node authorizer.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_collector_unhealthy_nodes_in_zone</div>
	<div class="metric_help">Gauge measuring number of not Ready Nodes per zones.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">zone</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_collector_update_all_nodes_health_duration_seconds</div>
	<div class="metric_help">Duration in seconds for NodeController to update the health of all nodes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_collector_update_node_health_duration_seconds</div>
	<div class="metric_help">Duration in seconds for NodeController to update the health of a single node.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_collector_zone_health</div>
	<div class="metric_help">Gauge measuring percentage of healthy nodes per zone.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">zone</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_collector_zone_size</div>
	<div class="metric_help">Gauge measuring number of registered Nodes per zones.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">zone</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_controller_cloud_provider_taint_removal_delay_seconds</div>
	<div class="metric_help">Number of seconds after node creation when NodeController removed the cloud-provider taint of a single node.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_controller_initial_node_sync_delay_seconds</div>
	<div class="metric_help">Number of seconds after node creation when NodeController finished the initial synchronization of a single node.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_ipam_controller_cidrset_allocation_tries_per_request</div>
	<div class="metric_help">Number of endpoints added on each Service sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">clusterCIDR</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_ipam_controller_cidrset_cidrs_allocations_total</div>
	<div class="metric_help">Counter measuring total number of CIDR allocations.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">clusterCIDR</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_ipam_controller_cidrset_cidrs_releases_total</div>
	<div class="metric_help">Counter measuring total number of CIDR releases.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">clusterCIDR</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_ipam_controller_cidrset_usage_cidrs</div>
	<div class="metric_help">Gauge measuring percentage of allocated CIDRs.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">clusterCIDR</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_ipam_controller_cirdset_max_cidrs</div>
	<div class="metric_help">Maximum number of CIDRs that can be allocated.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">clusterCIDR</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">node_swap_usage_bytes</div>
	<div class="metric_help">Current swap usage of the node in bytes. Reported only on non-windows systems</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">plugin_manager_total_plugins</div>
	<div class="metric_help">Number of plugins in Plugin Manager</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">socket_path</span><span class="metric_label">state</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pod_gc_collector_force_delete_pod_errors_total</div>
	<div class="metric_help">Number of errors encountered when forcefully deleting the pods since the Pod GC Controller started.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pod_gc_collector_force_delete_pods_total</div>
	<div class="metric_help">Number of pods that are being forcefully deleted since the Pod GC Controller started.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pod_security_errors_total</div>
	<div class="metric_help">Number of errors preventing normal evaluation. Non-fatal errors may result in the latest restricted profile being used for evaluation.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">fatal</span><span class="metric_label">request_operation</span><span class="metric_label">resource</span><span class="metric_label">subresource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pod_security_evaluations_total</div>
	<div class="metric_help">Number of policy evaluations that occurred, not counting ignored or exempt requests.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">decision</span><span class="metric_label">mode</span><span class="metric_label">policy_level</span><span class="metric_label">policy_version</span><span class="metric_label">request_operation</span><span class="metric_label">resource</span><span class="metric_label">subresource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pod_security_exemptions_total</div>
	<div class="metric_help">Number of exempt requests, not counting ignored or out of scope requests.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">request_operation</span><span class="metric_label">resource</span><span class="metric_label">subresource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pod_swap_usage_bytes</div>
	<div class="metric_help">Current amount of the pod swap usage in bytes. Reported only on non-windows systems</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">prober_probe_duration_seconds</div>
	<div class="metric_help">Duration in seconds for a probe response.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container</span><span class="metric_label">namespace</span><span class="metric_label">pod</span><span class="metric_label">probe_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pv_collector_bound_pv_count</div>
	<div class="metric_help">Gauge measuring number of persistent volume currently bound</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">storage_class</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pv_collector_bound_pvc_count</div>
	<div class="metric_help">Gauge measuring number of persistent volume claim currently bound</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">storage_class</span><span class="metric_label">volume_attributes_class</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pv_collector_total_pv_count</div>
	<div class="metric_help">Gauge measuring total number of persistent volumes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin_name</span><span class="metric_label">volume_mode</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pv_collector_unbound_pv_count</div>
	<div class="metric_help">Gauge measuring number of persistent volume currently unbound</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">storage_class</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">pv_collector_unbound_pvc_count</div>
	<div class="metric_help">Gauge measuring number of persistent volume claim currently unbound</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">storage_class</span><span class="metric_label">volume_attributes_class</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">reconstruct_volume_operations_errors_total</div>
	<div class="metric_help">The number of volumes that failed reconstruction from the operating system during kubelet startup.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">reconstruct_volume_operations_total</div>
	<div class="metric_help">The number of volumes that were attempted to be reconstructed from the operating system during kubelet startup. This includes both successful and failed reconstruction.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">replicaset_controller_sorting_deletion_age_ratio</div>
	<div class="metric_help">The ratio of chosen deleted pod's ages to the current youngest pod's age (at the time). Should be <2. The intent of this metric is to measure the rough efficacy of the LogarithmicScaleDown feature gate's effect on the sorting (and deletion) of pods when a replicaset scales down. This only considers Ready pods when calculating and reporting.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">resourceclaim_controller_allocated_resource_claims</div>
	<div class="metric_help">Number of allocated ResourceClaims</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">resourceclaim_controller_create_attempts_total</div>
	<div class="metric_help">Number of ResourceClaims creation requests</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">resourceclaim_controller_create_failures_total</div>
	<div class="metric_help">Number of ResourceClaims creation request failures</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">resourceclaim_controller_resource_claims</div>
	<div class="metric_help">Number of ResourceClaims</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_dns_resolution_duration_seconds</div>
	<div class="metric_help">DNS resolver latency in seconds. Broken down by host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">host</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_exec_plugin_call_total</div>
	<div class="metric_help">Number of calls to an exec plugin, partitioned by the type of event encountered (no_error, plugin_execution_error, plugin_not_found_error, client_internal_error) and an optional exit code. The exit code will be set to 0 if and only if the plugin call was successful.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">call_status</span><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_exec_plugin_certificate_rotation_age</div>
	<div class="metric_help">Histogram of the number of seconds the last auth exec plugin client certificate lived before being rotated. If auth exec plugin client certificates are unused, histogram will contain no data.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_exec_plugin_ttl_seconds</div>
	<div class="metric_help">Gauge of the shortest TTL (time-to-live) of the client certificate(s) managed by the auth exec plugin. The value is in seconds until certificate expiry (negative if already expired). If auth exec plugins are unused or manage no TLS certificates, the value will be +INF.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_rate_limiter_duration_seconds</div>
	<div class="metric_help">Client side rate limiter latency in seconds. Broken down by verb, and host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">host</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_request_duration_seconds</div>
	<div class="metric_help">Request latency in seconds. Broken down by verb, and host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">host</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_request_retries_total</div>
	<div class="metric_help">Number of request retries, partitioned by status code, verb, and host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">host</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_request_size_bytes</div>
	<div class="metric_help">Request size in bytes. Broken down by verb and host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">host</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_requests_total</div>
	<div class="metric_help">Number of HTTP requests, partitioned by status code, method, and host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">host</span><span class="metric_label">method</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_response_size_bytes</div>
	<div class="metric_help">Response size in bytes. Broken down by verb and host.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">host</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_transport_cache_entries</div>
	<div class="metric_help">Number of transport entries in the internal cache.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">rest_client_transport_create_calls_total</div>
	<div class="metric_help">Number of calls to get a new transport, partitioned by the result of the operation hit: obtained from the cache, miss: created and added to the cache, uncacheable: created and not cached</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">retroactive_storageclass_errors_total</div>
	<div class="metric_help">Total number of failed retroactive StorageClass assignments to persistent volume claim</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">retroactive_storageclass_total</div>
	<div class="metric_help">Total number of retroactive StorageClass assignments to persistent volume claim</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">root_ca_cert_publisher_sync_duration_seconds</div>
	<div class="metric_help">Number of namespace syncs happened in root ca cert publisher.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">root_ca_cert_publisher_sync_total</div>
	<div class="metric_help">Number of namespace syncs happened in root ca cert publisher.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">running_managed_controllers</div>
	<div class="metric_help">Indicates where instances of a controller are currently running</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">manager</span><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_cache_size</div>
	<div class="metric_help">Number of nodes, pods, and assumed (bound) pods in the scheduler cache.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_event_handling_duration_seconds</div>
	<div class="metric_help">Event handling latency in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">event</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_goroutines</div>
	<div class="metric_help">Number of running goroutines split by the work they do such as binding.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_inflight_events</div>
	<div class="metric_help">Number of events currently tracked in the scheduling queue.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">event</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_permit_wait_duration_seconds</div>
	<div class="metric_help">Duration of waiting on permit.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_plugin_evaluation_total</div>
	<div class="metric_help">Number of attempts to schedule pods by each plugin and the extension point (available only in PreFilter, Filter, PreScore, and Score).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">extension_point</span><span class="metric_label">plugin</span><span class="metric_label">profile</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_plugin_execution_duration_seconds</div>
	<div class="metric_help">Duration for running a plugin at a specific extension point.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">extension_point</span><span class="metric_label">plugin</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_preemption_goroutines_duration_seconds</div>
	<div class="metric_help">Duration in seconds for running goroutines for the preemption.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_preemption_goroutines_execution_total</div>
	<div class="metric_help">Number of preemption goroutines executed.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_queueing_hint_execution_duration_seconds</div>
	<div class="metric_help">Duration for running a queueing hint function of a plugin.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">event</span><span class="metric_label">hint</span><span class="metric_label">plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_scheduling_algorithm_duration_seconds</div>
	<div class="metric_help">Scheduling algorithm latency in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_unschedulable_pods</div>
	<div class="metric_help">The number of unschedulable pods broken down by plugin name. A pod will increment the gauge for all plugins that caused it to not schedule and so this metric have meaning only when broken down by plugin.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin</span><span class="metric_label">profile</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_volume_binder_cache_requests_total</div>
	<div class="metric_help">Total number for request volume binding cache</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scheduler_volume_scheduling_stage_error_total</div>
	<div class="metric_help">Volume scheduling stage error count</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">scrape_error</div>
	<div class="metric_help">1 if there was an error while getting container metrics, 0 otherwise</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
