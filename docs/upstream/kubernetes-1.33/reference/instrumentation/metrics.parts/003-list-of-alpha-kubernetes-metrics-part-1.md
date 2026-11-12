<!-- Part 3 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

### List of Alpha Kubernetes Metrics

Alpha metrics do not have any API guarantees. These metrics must be used at your own risk, subsequent versions of Kubernetes may remove these metrics altogether, or mutate the API in such a way that breaks existing dashboards and alerts. 

<div class="metrics"><div class="metric" data-stability="alpha">
	<div class="metric_name">aggregator_discovery_aggregation_count_total</div>
	<div class="metric_help">Counter of number of times discovery was aggregated</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">aggregator_openapi_v2_regeneration_count</div>
	<div class="metric_help">Counter of OpenAPI v2 spec regeneration count broken down by causing APIService name and reason.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiservice</span><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">aggregator_openapi_v2_regeneration_duration</div>
	<div class="metric_help">Gauge of OpenAPI v2 spec regeneration duration in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">aggregator_unavailable_apiservice</div>
	<div class="metric_help">Gauge of APIServices which are marked as unavailable broken down by APIService name.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">aggregator_unavailable_apiservice_total</div>
	<div class="metric_help">Counter of APIServices which are marked as unavailable broken down by APIService name and reason.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiextensions_apiserver_validation_ratcheting_seconds</div>
	<div class="metric_help">Time for comparison of old to new for the purposes of CRDValidationRatcheting during an UPDATE in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiextensions_openapi_v2_regeneration_count</div>
	<div class="metric_help">Counter of OpenAPI v2 spec regeneration count broken down by causing CRD name and reason.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">crd</span><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiextensions_openapi_v3_regeneration_count</div>
	<div class="metric_help">Counter of OpenAPI v3 spec regeneration count broken down by group, version, causing CRD and reason.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">crd</span><span class="metric_label">group</span><span class="metric_label">reason</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_match_condition_evaluation_errors_total</div>
	<div class="metric_help">Admission match condition evaluation errors count, identified by name of resource containing the match condition and broken out for each kind containing matchConditions (webhook or policy), operation and admission type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">kind</span><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_match_condition_evaluation_seconds</div>
	<div class="metric_help">Admission match condition evaluation time in seconds, identified by name and broken out for each kind containing matchConditions (webhook or policy), operation and type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">kind</span><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_match_condition_exclusions_total</div>
	<div class="metric_help">Admission match condition evaluation exclusions count, identified by name of resource containing the match condition and broken out for each kind containing matchConditions (webhook or policy), operation and admission type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">kind</span><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_step_admission_duration_seconds_summary</div>
	<div class="metric_help">Admission sub-step latency summary in seconds, broken out for each operation and API resource and step type (validate or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="summary"><label class="metric_detail">Type:</label> <span class="metric_type">Summary</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span><span class="metric_label">rejected</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_webhook_fail_open_count</div>
	<div class="metric_help">Admission webhook fail open count, identified by name and broken out for each admission type (validating or admit).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_webhook_rejection_count</div>
	<div class="metric_help">Admission webhook rejection count, identified by name and broken out for each admission type (validating or admit) and operation. Additional labels specify an error type (calling_webhook_error or apiserver_internal_error if an error occurred; no_error otherwise) and optionally a non-zero rejection code if the webhook rejects the request with an HTTP status code (honored by the apiserver when the code is greater or equal to 400). Codes greater than 600 are truncated to 600, to keep the metrics cardinality bounded.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">error_type</span><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">rejection_code</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_admission_webhook_request_total</div>
	<div class="metric_help">Admission webhook request total, identified by name and broken out for each admission type (validating or admit) and operation. Additional labels specify whether the request was rejected or not and an HTTP status code. Codes greater than 600 are truncated to 600, to keep the metrics cardinality bounded.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">name</span><span class="metric_label">operation</span><span class="metric_label">rejected</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_audit_error_total</div>
	<div class="metric_help">Counter of audit events that failed to be audited properly. Plugin identifies the plugin affected by the error.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_audit_event_total</div>
	<div class="metric_help">Counter of audit events generated and sent to the audit backend.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_audit_level_total</div>
	<div class="metric_help">Counter of policy levels for audit events (1 per request).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">level</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_audit_requests_rejected_total</div>
	<div class="metric_help">Counter of apiserver requests rejected due to an error in audit logging backend.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authentication_config_controller_automatic_reload_last_timestamp_seconds</div>
	<div class="metric_help">Timestamp of the last automatic reload of authentication configuration split by status and apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authentication_config_controller_automatic_reloads_total</div>
	<div class="metric_help">Total number of automatic reloads of authentication configuration split by status and apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authentication_jwt_authenticator_latency_seconds</div>
	<div class="metric_help">Latency of jwt authentication operations in seconds. This is the time spent authenticating a token for cache miss only (i.e. when the token is not found in the cache).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">jwt_issuer_hash</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_config_controller_automatic_reload_last_timestamp_seconds</div>
	<div class="metric_help">Timestamp of the last automatic reload of authorization configuration split by status and apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_config_controller_automatic_reloads_total</div>
	<div class="metric_help">Total number of automatic reloads of authorization configuration split by status and apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_decisions_total</div>
	<div class="metric_help">Total number of terminal decisions made by an authorizer split by authorizer type, name, and decision.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">decision</span><span class="metric_label">name</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_match_condition_evaluation_errors_total</div>
	<div class="metric_help">Total number of errors when an authorization webhook encounters a match condition error split by authorizer type and name.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_match_condition_evaluation_seconds</div>
	<div class="metric_help">Authorization match condition evaluation time in seconds, split by authorizer type and name.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_match_condition_exclusions_total</div>
	<div class="metric_help">Total number of exclusions when an authorization webhook is skipped because match conditions exclude it.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_webhook_duration_seconds</div>
	<div class="metric_help">Request latency in seconds.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_webhook_evaluations_fail_open_total</div>
	<div class="metric_help">NoOpinion results due to webhook timeout or error.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_authorization_webhook_evaluations_total</div>
	<div class="metric_help">Round-trips to authorization webhooks.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">name</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_cache_list_fetched_objects_total</div>
	<div class="metric_help">Number of objects read from watch cache in the course of serving a LIST request</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">index</span><span class="metric_label">resource_prefix</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_cache_list_returned_objects_total</div>
	<div class="metric_help">Number of objects returned for a LIST request from watch cache</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource_prefix</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_cache_list_total</div>
	<div class="metric_help">Number of LIST requests served from watch cache</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">index</span><span class="metric_label">resource_prefix</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_certificates_registry_csr_honored_duration_total</div>
	<div class="metric_help">Total number of issued CSRs with a requested duration that was honored, sliced by signer (only kubernetes.io signer names are specifically identified)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">signerName</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_certificates_registry_csr_requested_duration_total</div>
	<div class="metric_help">Total number of issued CSRs with a requested duration, sliced by signer (only kubernetes.io signer names are specifically identified)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">signerName</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_client_certificate_expiration_seconds</div>
	<div class="metric_help">Distribution of the remaining lifetime on the certificate used to authenticate a request.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_clusterip_repair_ip_errors_total</div>
	<div class="metric_help">Number of errors detected on clusterips by the repair loop broken down by type of error: leak, repair, full, outOfRange, duplicate, unknown, invalid</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_clusterip_repair_reconcile_errors_total</div>
	<div class="metric_help">Number of reconciliation failures on the clusterip repair reconcile loop</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_conversion_webhook_duration_seconds</div>
	<div class="metric_help">Conversion webhook request latency</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">failure_type</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_conversion_webhook_request_total</div>
	<div class="metric_help">Counter for conversion webhook requests with success/failure and failure error type</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">failure_type</span><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_crd_conversion_webhook_duration_seconds</div>
	<div class="metric_help">CRD webhook conversion duration in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">crd_name</span><span class="metric_label">from_version</span><span class="metric_label">succeeded</span><span class="metric_label">to_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_current_inqueue_requests</div>
	<div class="metric_help">Maximal number of queued requests in this apiserver per request kind in last second.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">request_kind</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_delegated_authn_request_duration_seconds</div>
	<div class="metric_help">Request latency in seconds. Broken down by status code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_delegated_authn_request_total</div>
	<div class="metric_help">Number of HTTP requests partitioned by status code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_delegated_authz_request_duration_seconds</div>
	<div class="metric_help">Request latency in seconds. Broken down by status code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_delegated_authz_request_total</div>
	<div class="metric_help">Number of HTTP requests partitioned by status code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_egress_dialer_dial_duration_seconds</div>
	<div class="metric_help">Dial latency histogram in seconds, labeled by the protocol (http-connect or grpc), transport (tcp or uds)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">protocol</span><span class="metric_label">transport</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_egress_dialer_dial_failure_count</div>
	<div class="metric_help">Dial failure count, labeled by the protocol (http-connect or grpc), transport (tcp or uds), and stage (connect or proxy). The stage indicates at which stage the dial failed</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">protocol</span><span class="metric_label">stage</span><span class="metric_label">transport</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_egress_dialer_dial_start_total</div>
	<div class="metric_help">Dial starts, labeled by the protocol (http-connect or grpc) and transport (tcp or uds).</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">protocol</span><span class="metric_label">transport</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_encryption_config_controller_automatic_reload_failures_total</div>
	<div class="metric_help">Total number of failed automatic reloads of encryption configuration split by apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.30.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_encryption_config_controller_automatic_reload_last_timestamp_seconds</div>
	<div class="metric_help">Timestamp of the last successful or failed automatic reload of encryption configuration split by apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_encryption_config_controller_automatic_reload_success_total</div>
	<div class="metric_help">Total number of successful automatic reloads of encryption configuration split by apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span></li><li class="metric_deprecated_version"><label class="metric_detail">Deprecated Versions:</label><span>1.30.0</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_encryption_config_controller_automatic_reloads_total</div>
	<div class="metric_help">Total number of reload successes and failures of encryption configuration split by apiserver identity.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_dek_cache_fill_percent</div>
	<div class="metric_help">Percent of the cache slots currently occupied by cached DEKs.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_dek_cache_inter_arrival_time_seconds</div>
	<div class="metric_help">Time (in seconds) of inter arrival of transformation requests.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">transformation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_dek_source_cache_size</div>
	<div class="metric_help">Number of records in data encryption key (DEK) source cache. On a restart, this value is an approximation of the number of decrypt RPC calls the server will make to the KMS plugin.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">provider_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_invalid_key_id_from_status_total</div>
	<div class="metric_help">Number of times an invalid keyID is returned by the Status RPC call split by error.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">error</span><span class="metric_label">provider_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_key_id_hash_last_timestamp_seconds</div>
	<div class="metric_help">The last time in seconds when a keyID was used.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">apiserver_id_hash</span><span class="metric_label">key_id_hash</span><span class="metric_label">provider_name</span><span class="metric_label">transformation_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_envelope_encryption_key_id_hash_status_last_timestamp_seconds</div>
	<div class="metric_help">The last time in seconds when a keyID was returned by the Status RPC call.</div>
	<ul>
