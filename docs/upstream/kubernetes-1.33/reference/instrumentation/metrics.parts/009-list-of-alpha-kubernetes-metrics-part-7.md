<!-- Part 9 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

<li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.29.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">selinux_warning_controller_selinux_volume_conflict</div>
	<div class="metric_help">Conflict between two Pods using the same volume</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">property</span><span class="metric_label">pod1_namespace</span><span class="metric_label">pod1_name</span><span class="metric_label">pod1_value</span><span class="metric_label">pod2_namespace</span><span class="metric_label">pod2_name</span><span class="metric_label">pod2_value</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">service_controller_loadbalancer_sync_total</div>
	<div class="metric_help">A metric counting the amount of times any load balancer has been configured, as an effect of service/node changes on the cluster</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">service_controller_nodesync_error_total</div>
	<div class="metric_help">A metric counting the amount of times any load balancer has been configured and errored, as an effect of node changes on the cluster</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">service_controller_nodesync_latency_seconds</div>
	<div class="metric_help">A metric measuring the latency for nodesync which updates loadbalancer hosts on cluster node updates.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">service_controller_update_loadbalancer_host_latency_seconds</div>
	<div class="metric_help">A metric measuring the latency for updating each load balancer hosts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">serviceaccount_invalid_legacy_auto_token_uses_total</div>
	<div class="metric_help">Cumulative invalid auto-generated legacy tokens used</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">serviceaccount_legacy_auto_token_uses_total</div>
	<div class="metric_help">Cumulative auto-generated legacy tokens used</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">serviceaccount_legacy_manual_token_uses_total</div>
	<div class="metric_help">Cumulative manually created legacy tokens used</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">serviceaccount_legacy_tokens_total</div>
	<div class="metric_help">Cumulative legacy service account tokens used</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">serviceaccount_stale_tokens_total</div>
	<div class="metric_help">Cumulative stale projected service account tokens used</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">serviceaccount_valid_tokens_total</div>
	<div class="metric_help">Cumulative valid projected service account tokens used</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">storage_count_attachable_volumes_in_use</div>
	<div class="metric_help">Measure number of volumes in use</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">node</span><span class="metric_label">volume_plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">storage_operation_duration_seconds</div>
	<div class="metric_help">Storage operation duration</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">migrated</span><span class="metric_label">operation_name</span><span class="metric_label">status</span><span class="metric_label">volume_plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">taint_eviction_controller_pod_deletion_duration_seconds</div>
	<div class="metric_help">Latency, in seconds, between the time when a taint effect has been activated for the Pod and its deletion via TaintEvictionController.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">taint_eviction_controller_pod_deletions_total</div>
	<div class="metric_help">Total number of Pods deleted by TaintEvictionController since its start.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">ttl_after_finished_controller_job_deletion_duration_seconds</div>
	<div class="metric_help">The time it took to delete the job since it became eligible for deletion</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_container_errors_total</div>
	<div class="metric_help">Number of errors when kubelet cannot compute SELinux context for a container. Kubelet can't start such a Pod then and it will retry, therefore value of this metric may not represent the actual nr. of containers.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_container_warnings_total</div>
	<div class="metric_help">Number of errors when kubelet cannot compute SELinux context for a container that are ignored. They will become real errors when SELinuxMountReadWriteOncePod feature is expanded to all volume access modes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_pod_context_mismatch_errors_total</div>
	<div class="metric_help">Number of errors when a Pod defines different SELinux contexts for its containers that use the same volume. Kubelet can't start such a Pod then and it will retry, therefore value of this metric may not represent the actual nr. of Pods.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_pod_context_mismatch_warnings_total</div>
	<div class="metric_help">Number of errors when a Pod defines different SELinux contexts for its containers that use the same volume. They are not errors yet, but they will become real errors when SELinuxMountReadWriteOncePod feature is expanded to all volume access modes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_volume_context_mismatch_errors_total</div>
	<div class="metric_help">Number of errors when a Pod uses a volume that is already mounted with a different SELinux context than the Pod needs. Kubelet can't start such a Pod then and it will retry, therefore value of this metric may not represent the actual nr. of Pods.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span><span class="metric_label">volume_plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_volume_context_mismatch_warnings_total</div>
	<div class="metric_help">Number of errors when a Pod uses a volume that is already mounted with a different SELinux context than the Pod needs. They are not errors yet, but they will become real errors when SELinuxMountReadWriteOncePod feature is expanded to all volume access modes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span><span class="metric_label">volume_plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_selinux_volumes_admitted_total</div>
	<div class="metric_help">Number of volumes whose SELinux context was fine and will be mounted with mount -o context option.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">access_mode</span><span class="metric_label">volume_plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_manager_total_volumes</div>
	<div class="metric_help">Number of volumes in Volume Manager</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin_name</span><span class="metric_label">state</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_operation_total_errors</div>
	<div class="metric_help">Total volume operation errors</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_name</span><span class="metric_label">plugin_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">volume_operation_total_seconds</div>
	<div class="metric_help">Storage operation end to end duration in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation_name</span><span class="metric_label">plugin_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">watch_cache_capacity</div>
	<div class="metric_help">Total capacity of watch cache broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">watch_cache_capacity_decrease_total</div>
	<div class="metric_help">Total number of watch cache capacity decrease events broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">watch_cache_capacity_increase_total</div>
	<div class="metric_help">Total number of watch cache capacity increase events broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_adds_total</div>
	<div class="metric_help">Total number of adds handled by workqueue</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_depth</div>
	<div class="metric_help">Current depth of workqueue</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_longest_running_processor_seconds</div>
	<div class="metric_help">How many seconds has the longest running processor for workqueue been running.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_queue_duration_seconds</div>
	<div class="metric_help">How long in seconds an item stays in workqueue before being requested.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_retries_total</div>
	<div class="metric_help">Total number of retries handled by workqueue</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_unfinished_work_seconds</div>
	<div class="metric_help">How many seconds of work has done that is in progress and hasn't been observed by work_duration. Large values indicate stuck threads. One can deduce the number of stuck threads by observing the rate at which this increases.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">workqueue_work_duration_seconds</div>
	<div class="metric_help">How long in seconds processing an item from workqueue takes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div>
</div>
