<!-- Part 4 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">key_id_hash</span><span class="metric_label">provider_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_key_id_hash_total</div>
	<div class="metric_help">Number of times a keyID is used split by transformation type, provider, and apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">key_id_hash</span><span class="metric_label">provider_name</span><span class="metric_label">transformation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_kms_operations_latency_seconds</div>
	<div class="metric_help">KMS operation duration with gRPC error code status total.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">grpc_status_code</span><span class="metric_label">method_name</span><span class="metric_label">provider_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_externaljwt_fetch_keys_data_timestamp</div>
	<div class="metric_help">Unix Timestamp in seconds of the last successful FetchKeys data_timestamp value returned by the external signer</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_externaljwt_fetch_keys_request_total</div>
	<div class="metric_help">Total attempts at syncing supported JWKs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_externaljwt_fetch_keys_success_timestamp</div>
	<div class="metric_help">Unix Timestamp in seconds of the last successful FetchKeys request</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_externaljwt_request_duration_seconds</div>
	<div class="metric_help">Request duration and time for calls to external-jwt-signer</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">method</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_externaljwt_sign_request_total</div>
	<div class="metric_help">Total attempts at signing JWT</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_current_inqueue_seats</div>
	<div class="metric_help">Number of seats currently pending in queues of the API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_current_limit_seats</div>
	<div class="metric_help">current derived number of execution seats available to each priority level</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_current_r</div>
	<div class="metric_help">R(time of last change)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_demand_seats</div>
	<div class="metric_help">Observations, at the end of every nanosecond, of (the number of seats each priority level could use) / (nominal number of seats for that level)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="timingratiohistogram"><label class="metric_detail">Type:</label> <span class="metric_type">TimingRatioHistogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_demand_seats_average</div>
	<div class="metric_help">Time-weighted average, over last adjustment period, of demand_seats</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_demand_seats_high_watermark</div>
	<div class="metric_help">High watermark, over last adjustment period, of demand_seats</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_demand_seats_smoothed</div>
	<div class="metric_help">Smoothed seat demands</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_demand_seats_stdev</div>
	<div class="metric_help">Time-weighted standard deviation, over last adjustment period, of demand_seats</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_dispatch_r</div>
	<div class="metric_help">R(time of last dispatch)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_epoch_advance_total</div>
	<div class="metric_help">Number of times the queueset's progress meter jumped backward</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span><span class="metric_label">success</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_latest_s</div>
	<div class="metric_help">S(most recently dispatched request)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_lower_limit_seats</div>
	<div class="metric_help">Configured lower bound on number of execution seats available to each priority level</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_next_discounted_s_bounds</div>
	<div class="metric_help">min and max, over queues, of S(oldest waiting request in queue) - estimated work in progress</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">bound</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_next_s_bounds</div>
	<div class="metric_help">min and max, over queues, of S(oldest waiting request in queue)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">bound</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_priority_level_request_utilization</div>
	<div class="metric_help">Observations, at the end of every nanosecond, of number of requests (as a fraction of the relevant limit) waiting or in any stage of execution (but only initial stage for WATCHes)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="timingratiohistogram"><label class="metric_detail">Type:</label> <span class="metric_type">TimingRatioHistogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">phase</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_priority_level_seat_utilization</div>
	<div class="metric_help">Observations, at the end of every nanosecond, of utilization of seats for any stage of execution (but only initial stage for WATCHes)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="timingratiohistogram"><label class="metric_detail">Type:</label> <span class="metric_type">TimingRatioHistogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li><li class="metric_labels_constant"><label class="metric_detail">Const Labels:</label><span class="metric_label">phase:executing</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_read_vs_write_current_requests</div>
	<div class="metric_help">Observations, at the end of every nanosecond, of the number of requests (as a fraction of the relevant limit) waiting or in regular stage of execution</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="timingratiohistogram"><label class="metric_detail">Type:</label> <span class="metric_type">TimingRatioHistogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">phase</span><span class="metric_label">request_kind</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_request_concurrency_in_use</div>
	<div class="metric_help">Concurrency (number of seats) occupied by the currently executing (initial stage for a WATCH, any stage otherwise) requests in the API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.31.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_request_concurrency_limit</div>
	<div class="metric_help">Nominal number of execution seats configured for each priority level</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.30.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_request_dispatch_no_accommodation_total</div>
	<div class="metric_help">Number of times a dispatch attempt resulted in a non accommodation due to lack of available seats</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_request_execution_seconds</div>
	<div class="metric_help">Duration of initial stage (for a WATCH) or any (for a non-WATCH) stage of request execution in the API Priority and Fairness subsystem</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_request_queue_length_after_enqueue</div>
	<div class="metric_help">Length of queue in the API Priority and Fairness subsystem, as seen by each request after it is enqueued</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_seat_fair_frac</div>
	<div class="metric_help">Fair fraction of server's concurrency to allocate to each priority level that can use it</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_target_seats</div>
	<div class="metric_help">Seat allocation targets</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_upper_limit_seats</div>
	<div class="metric_help">Configured upper bound on number of execution seats available to each priority level</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_watch_count_samples</div>
	<div class="metric_help">count of watchers for mutating requests in API Priority and Fairness</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_flowcontrol_work_estimated_seats</div>
	<div class="metric_help">Number of estimated seats (maximum of initial and final seats) associated with requests in API Priority and Fairness</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">flow_schema</span><span class="metric_label">priority_level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_init_events_total</div>
	<div class="metric_help">Counter of init events processed in watch cache broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_kube_aggregator_x509_insecure_sha1_total</div>
	<div class="metric_help">Counts the number of requests to servers with insecure SHA1 signatures in their serving certificate OR the number of connection failures due to the insecure SHA1 signatures (either/or, based on the runtime environment)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_kube_aggregator_x509_missing_san_total</div>
	<div class="metric_help">Counts the number of requests to servers missing SAN extension in their serving certificate OR the number of connection failures due to the lack of x509 certificate SAN extension missing (either/or, based on the runtime environment)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_nodeport_repair_port_errors_total</div>
	<div class="metric_help">Number of errors detected on ports by the repair loop broken down by type of error: leak, repair, full, outOfRange, duplicate, unknown</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_nodeport_repair_reconcile_errors_total</div>
	<div class="metric_help">Number of reconciliation failures on the nodeport repair reconcile loop</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_aborts_total</div>
	<div class="metric_help">Number of requests which apiserver aborted possibly due to a timeout, for each group, version, verb, resource, subresource and scope</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_body_size_bytes</div>
	<div class="metric_help">Apiserver request body size in bytes broken out by resource and verb.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_filter_duration_seconds</div>
	<div class="metric_help">Request filter latency distribution in seconds, for each filter type</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">filter</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_post_timeout_total</div>
	<div class="metric_help">Tracks the activity of the request handlers after the associated requests have been timed out by the apiserver</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">source</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_sli_duration_seconds</div>
	<div class="metric_help">Response latency distribution (not counting webhook duration and priority & fairness queue wait times) in seconds for each verb, group, version, resource, subresource, scope and component.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">component</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_slo_duration_seconds</div>
	<div class="metric_help">Response latency distribution (not counting webhook duration and priority & fairness queue wait times) in seconds for each verb, group, version, resource, subresource, scope and component.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">component</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.27.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_terminations_total</div>
	<div class="metric_help">Number of requests which apiserver terminated in self-defense.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">component</span><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">subresource</span><span class="metric_label">verb</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_request_timestamp_comparison_time</div>
	<div class="metric_help">Time taken for comparison of old vs new objects in UPDATE or PATCH requests</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code_path</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_rerouted_request_total</div>
	<div class="metric_help">Total number of requests that were proxied to a peer kube apiserver because the local apiserver was not capable of serving it</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_selfrequest_total</div>
	<div class="metric_help">Counter of apiserver self-requests broken out for each verb, API resource and subresource.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span><span class="metric_label">subresource</span><span class="metric_label">verb</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_data_key_generation_duration_seconds</div>
	<div class="metric_help">Latencies in seconds of data encryption key(DEK) generation operations.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_data_key_generation_failures_total</div>
	<div class="metric_help">Total number of failed data encryption key(DEK) generation operations.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_db_total_size_in_bytes</div>
	<div class="metric_help">Total size of the storage database file physically allocated in bytes.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">endpoint</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.28.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_decode_errors_total</div>
	<div class="metric_help">Number of stored object decode errors split by object type</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_envelope_transformation_cache_misses_total</div>
	<div class="metric_help">Total number of cache misses while accessing key decryption key(KEK).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_events_received_total</div>
	<div class="metric_help">Number of etcd events received split by kind.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_list_evaluated_objects_total</div>
	<div class="metric_help">Number of objects tested in the course of serving a LIST request from storage</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_list_fetched_objects_total</div>
	<div class="metric_help">Number of objects read from storage in the course of serving a LIST request</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_list_returned_objects_total</div>
	<div class="metric_help">Number of objects returned for a LIST request from storage</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_list_total</div>
	<div class="metric_help">Number of LIST requests served from storage</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_transformation_duration_seconds</div>
	<div class="metric_help">Latencies in seconds of value transformation operations.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">transformation_type</span><span class="metric_label">transformer_prefix</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_storage_transformation_operations_total</div>
	<div class="metric_help">Total number of transformations. Successful transformation will have a status 'OK' and a varied status string when the transformation fails. The status, resource, and transformation_type fields can be used for alerting purposes. For example, you can monitor for encryption/decryption failures using the transformation_type (e.g., from_storage for decryption and to_storage for encryption). Additionally, these fields can be used to ensure that the correct transformers are applied to each resource.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
