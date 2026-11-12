<!-- Part 1 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

### List of Stable Kubernetes Metrics

Stable metrics observe strict API contracts and no labels can be added or removed from stable metrics during their lifetime.

<div class="metrics"><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_admission_controller_admission_duration_seconds</div>
	<div class="metric_help">Admission controller latency histogram in seconds, identified by name and broken out for each operation and API resource and type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">rejected</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_admission_step_admission_duration_seconds</div>
	<div class="metric_help">Admission sub-step latency histogram in seconds, broken out for each operation and API resource and step type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span><span class="metric_label">rejected</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_admission_webhook_admission_duration_seconds</div>
	<div class="metric_help">Admission webhook latency histogram in seconds, identified by name and broken out for each operation and API resource and type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">rejected</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_current_inflight_requests</div>
	<div class="metric_help">Maximal number of currently used inflight request limit of this apiserver per request kind in last second.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">request_kind</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_longrunning_requests</div>
	<div class="metric_help">Gauge of all active long-running apiserver requests broken out by verb, group, version, resource, scope and component. Not all requests are tracked this way.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">component</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_request_duration_seconds</div>
	<div class="metric_help">Response latency distribution in seconds for each verb, dry run value, group, version, resource, subresource, scope and component.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">component</span><span class="metric_label">dry_run</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_request_total</div>
	<div class="metric_help">Counter of apiserver requests broken out for each verb, dry run value, group, version, resource, scope, component, and HTTP response code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">component</span><span class="metric_label">dry_run</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_requested_deprecated_apis</div>
	<div class="metric_help">Gauge of deprecated APIs that have been requested, broken out by API group, version, resource, subresource, and removed_release.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">group</span><span class="metric_label">removed_release</span><span class="metric_label">resource</span><span class="metric_label">subresource</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_response_sizes</div>
	<div class="metric_help">Response size distribution in bytes for each group, version, verb, resource, subresource, scope and component.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">component</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_storage_objects</div>
	<div class="metric_help">Number of stored objects at the time of last check split by kind. In case of a fetching error, the value will be -1.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">apiserver_storage_size_bytes</div>
	<div class="metric_help">Size of the storage database file physically allocated in bytes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">storage_cluster_id</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">container_cpu_usage_seconds_total</div>
	<div class="metric_help">Cumulative cpu time consumed by the container in core-seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container</span><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">container_memory_working_set_bytes</div>
	<div class="metric_help">Current working set of the container in bytes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container</span><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">container_start_time_seconds</div>
	<div class="metric_help">Start time of the container since unix epoch in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container</span><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">cronjob_controller_job_creation_skew_duration_seconds</div>
	<div class="metric_help">Time between when a cronjob is scheduled to be run, and when the corresponding job is created</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">job_controller_job_pods_finished_total</div>
	<div class="metric_help">The number of finished Pods that are fully tracked</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">completion_mode</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">job_controller_job_sync_duration_seconds</div>
	<div class="metric_help">The time it took to sync a job</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span><span class="metric_label">completion_mode</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">job_controller_job_syncs_total</div>
	<div class="metric_help">The number of job syncs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span><span class="metric_label">completion_mode</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">job_controller_jobs_finished_total</div>
	<div class="metric_help">The number of finished jobs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">completion_mode</span><span class="metric_label">reason</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">kube_pod_resource_limit</div>
	<div class="metric_help">Resources limit for workloads on the cluster, broken down by pod. This shows the resource usage the scheduler and kubelet expect per pod for resources along with the unit for the resource if any.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">pod</span><span class="metric_label">node</span><span class="metric_label">scheduler</span><span class="metric_label">priority</span><span class="metric_label">resource</span><span class="metric_label">unit</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">kube_pod_resource_request</div>
	<div class="metric_help">Resources requested by workloads on the cluster, broken down by pod. This shows the resource usage the scheduler and kubelet expect per pod for resources along with the unit for the resource if any.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">namespace</span><span class="metric_label">pod</span><span class="metric_label">node</span><span class="metric_label">scheduler</span><span class="metric_label">priority</span><span class="metric_label">resource</span><span class="metric_label">unit</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">kubernetes_healthcheck</div>
	<div class="metric_help">This metric records the result of a single healthcheck.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">kubernetes_healthchecks_total</div>
	<div class="metric_help">This metric records the results of all healthcheck.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">status</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">node_collector_evictions_total</div>
	<div class="metric_help">Number of Node evictions that happened since current instance of NodeController started.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">zone</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">node_cpu_usage_seconds_total</div>
	<div class="metric_help">Cumulative cpu time consumed by the node in core-seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">node_memory_working_set_bytes</div>
	<div class="metric_help">Current working set of the node in bytes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">pod_cpu_usage_seconds_total</div>
	<div class="metric_help">Cumulative cpu time consumed by the pod in core-seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">pod_memory_working_set_bytes</div>
	<div class="metric_help">Current working set of the pod in bytes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">resource_scrape_error</div>
	<div class="metric_help">1 if there was an error while getting container metrics, 0 otherwise</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_framework_extension_point_duration_seconds</div>
	<div class="metric_help">Latency for running all plugins of a specific extension point.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">extension_point</span><span class="metric_label">profile</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_pending_pods</div>
	<div class="metric_help">Number of pending pods, by the queue type. 'active' means number of pods in activeQ; 'backoff' means number of pods in backoffQ; 'unschedulable' means number of pods in unschedulablePods that the scheduler attempted to schedule and failed; 'gated' is the number of unschedulable pods that the scheduler never attempted to schedule because they are gated.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">queue</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_pod_scheduling_attempts</div>
	<div class="metric_help">Number of attempts to successfully schedule a pod.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_preemption_attempts_total</div>
	<div class="metric_help">Total preemption attempts in the cluster till now</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_preemption_victims</div>
	<div class="metric_help">Number of selected preemption victims</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_queue_incoming_pods_total</div>
	<div class="metric_help">Number of pods added to scheduling queues by event and queue type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">event</span><span class="metric_label">queue</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_schedule_attempts_total</div>
	<div class="metric_help">Number of attempts to schedule pods, by the result. 'unschedulable' means a pod could not be scheduled, while 'error' means an internal scheduler problem.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">profile</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="stable">
	<div class="metric_name">scheduler_scheduling_attempt_duration_seconds</div>
	<div class="metric_help">Scheduling attempt latency in seconds (scheduling algorithm + binding)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">STABLE</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">profile</span><span class="metric_label">result</span></li></ul>
	</div>
</div>
