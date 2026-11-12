<!-- Part 2 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

### List of Beta Kubernetes Metrics

Beta metrics observe a looser API contract than its stable counterparts. No labels can be removed from beta metrics during their lifetime, however, labels can be added while the metric is in the beta stage. This offers the assurance that beta metrics will honor existing dashboards and alerts, while allowing for amendments in the future. 

<div class="metrics"><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_cel_compilation_duration_seconds</div>
	<div class="metric_help">CEL compilation time in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_cel_evaluation_duration_seconds</div>
	<div class="metric_help">CEL evaluation time in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_current_executing_requests</div>
	<div class="metric_help">Number of requests in initial (for a WATCH) or any (for a non-WATCH) execution stage in the API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_current_executing_seats</div>
	<div class="metric_help">Concurrency (number of seats) occupied by the currently executing (initial stage for a WATCH, any stage otherwise) requests in the API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_current_inqueue_requests</div>
	<div class="metric_help">Number of requests currently pending in queues of the API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_dispatched_requests_total</div>
	<div class="metric_help">Number of requests executed by API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_nominal_limit_seats</div>
	<div class="metric_help">Nominal number of execution seats configured for each priority level</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_rejected_requests_total</div>
	<div class="metric_help">Number of requests rejected by API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_flowcontrol_request_wait_duration_seconds</div>
	<div class="metric_help">Length of time a request spent waiting in its queue</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">execute</span><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_validating_admission_policy_check_duration_seconds</div>
	<div class="metric_help">Validation admission latency for individual validation expressions in seconds, labeled by policy and further including binding and enforcement action taken.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">enforcement_action</span><span class="metric_label">error_type</span><span class="metric_label">policy</span><span class="metric_label">policy_binding</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_validating_admission_policy_check_total</div>
	<div class="metric_help">Validation admission policy check total, labeled by policy and further identified by binding and enforcement action taken.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">enforcement_action</span><span class="metric_label">error_type</span><span class="metric_label">policy</span><span class="metric_label">policy_binding</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_validation_declarative_validation_mismatch_total</div>
	<div class="metric_help">Number of times declarative validation results differed from handwritten validation results for core types.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">apiserver_validation_declarative_validation_panic_total</div>
	<div class="metric_help">Number of times declarative validation has panicked during validation.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">disabled_metrics_total</div>
	<div class="metric_help">The count of disabled metrics.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">hidden_metrics_total</div>
	<div class="metric_help">The count of hidden metrics.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">kubernetes_feature_enabled</div>
	<div class="metric_help">This metric records the data about the stage and enablement of a k8s feature.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">stage</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">prober_probe_total</div>
	<div class="metric_help">Cumulative number of a liveness, readiness or startup probe for a container by result.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container</span><span class="metric_label">namespace</span><span class="metric_label">pod</span><span class="metric_label">pod_uid</span><span class="metric_label">probe_type</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">registered_metrics_total</div>
	<div class="metric_help">The count of registered metrics broken by stability level and deprecation version.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">deprecated_version</span><span class="metric_label">stability_level</span></li></ul>
	</div><div class="metric" data-stability="beta">
	<div class="metric_name">scheduler_pod_scheduling_sli_duration_seconds</div>
	<div class="metric_help">E2e latency for a pod being scheduled, from the time the pod enters the scheduling queue and might involve multiple scheduling attempts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">BETA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">attempts</span></li></ul>
	</div>
</div>
