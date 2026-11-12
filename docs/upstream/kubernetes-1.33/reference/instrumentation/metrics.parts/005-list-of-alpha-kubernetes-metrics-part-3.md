<!-- Part 5 of 9 of reference/instrumentation/metrics.md (split because the page is big). -->

<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span><span class="metric_label">status</span><span class="metric_label">transformation_type</span><span class="metric_label">transformer_prefix</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_stream_translator_requests_total</div>
	<div class="metric_help">Total number of requests that were handled by the StreamTranslatorProxy, which processes streaming RemoteCommand/V5</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_stream_tunnel_requests_total</div>
	<div class="metric_help">Total number of requests that were handled by the StreamTunnelProxy, which processes streaming PortForward/V2</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_terminated_watchers_total</div>
	<div class="metric_help">Counter of watchers closed due to unresponsiveness broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_tls_handshake_errors_total</div>
	<div class="metric_help">Number of requests dropped with 'TLS handshake error from' error</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_cache_consistent_read_total</div>
	<div class="metric_help">Counter for consistent reads from cache.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">fallback</span><span class="metric_label">resource</span><span class="metric_label">success</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_cache_events_dispatched_total</div>
	<div class="metric_help">Counter of events dispatched in watch cache broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_cache_events_received_total</div>
	<div class="metric_help">Counter of events received in watch cache broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_cache_initializations_total</div>
	<div class="metric_help">Counter of watch cache initializations broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_cache_read_wait_seconds</div>
	<div class="metric_help">Histogram of time spent waiting for a watch cache to become fresh.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_cache_resource_version</div>
	<div class="metric_help">Current resource version of watch cache broken by resource type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_events_sizes</div>
	<div class="metric_help">Watch event size distribution in bytes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">group</span><span class="metric_label">kind</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_events_total</div>
	<div class="metric_help">Number of events sent in watch clients</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">group</span><span class="metric_label">kind</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_watch_list_duration_seconds</div>
	<div class="metric_help">Response latency distribution in seconds for watch list requests broken by group, version, resource and scope.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">group</span><span class="metric_label">resource</span><span class="metric_label">scope</span><span class="metric_label">version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_webhooks_x509_insecure_sha1_total</div>
	<div class="metric_help">Counts the number of requests to servers with insecure SHA1 signatures in their serving certificate OR the number of connection failures due to the insecure SHA1 signatures (either/or, based on the runtime environment)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">apiserver_webhooks_x509_missing_san_total</div>
	<div class="metric_help">Counts the number of requests to servers missing SAN extension in their serving certificate OR the number of connection failures due to the lack of x509 certificate SAN extension missing (either/or, based on the runtime environment)</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">attach_detach_controller_attachdetach_controller_forced_detaches</div>
	<div class="metric_help">Number of times the A/D Controller performed a forced detach</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">reason</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">attachdetach_controller_total_volumes</div>
	<div class="metric_help">Number of volumes in A/D Controller</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">plugin_name</span><span class="metric_label">state</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authenticated_user_requests</div>
	<div class="metric_help">Counter of authenticated requests broken out by username.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">username</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authentication_attempts</div>
	<div class="metric_help">Counter of authenticated attempts.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authentication_duration_seconds</div>
	<div class="metric_help">Authentication duration in seconds broken out by result.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authentication_token_cache_active_fetch_count</div>
	<div class="metric_help"></div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authentication_token_cache_fetch_total</div>
	<div class="metric_help"></div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authentication_token_cache_request_duration_seconds</div>
	<div class="metric_help"></div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authentication_token_cache_request_total</div>
	<div class="metric_help"></div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">status</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authorization_attempts_total</div>
	<div class="metric_help">Counter of authorization attempts broken down by result. It can be either 'allowed', 'denied', 'no-opinion' or 'error'.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">authorization_duration_seconds</div>
	<div class="metric_help">Authorization duration in seconds broken out by result.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">cloud_provider_webhook_request_duration_seconds</div>
	<div class="metric_help">Request latency in seconds. Broken down by status code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">webhook</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">cloud_provider_webhook_request_total</div>
	<div class="metric_help">Number of HTTP requests partitioned by status code.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span><span class="metric_label">webhook</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">clustertrustbundle_publisher_sync_duration_seconds</div>
	<div class="metric_help">The time it took to sync a cluster trust bundle.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">clustertrustbundle_publisher_sync_total</div>
	<div class="metric_help">Number of syncs that occurred in cluster trust bundle publisher.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">code</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">container_swap_usage_bytes</div>
	<div class="metric_help">Current amount of the container swap usage in bytes. Reported only on non-windows systems</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="custom"><label class="metric_detail">Type:</label> <span class="metric_type">Custom</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">container</span><span class="metric_label">pod</span><span class="metric_label">namespace</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">csi_operations_seconds</div>
	<div class="metric_help">Container Storage Interface operation duration with gRPC error code status total</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">driver_name</span><span class="metric_label">grpc_status_code</span><span class="metric_label">method_name</span><span class="metric_label">migrated</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">device_taint_eviction_controller_pod_deletion_duration_seconds</div>
	<div class="metric_help">Latency, in seconds, between the time when a device taint effect has been activated and a Pod's deletion via DeviceTaintEvictionController.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">device_taint_eviction_controller_pod_deletions_total</div>
	<div class="metric_help">Total number of Pods deleted by DeviceTaintEvictionController since its start.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">dra_grpc_operations_duration_seconds</div>
	<div class="metric_help">Duration in seconds of the DRA gRPC operations</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">driver_name</span><span class="metric_label">grpc_status_code</span><span class="metric_label">method_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">dra_operations_duration_seconds</div>
	<div class="metric_help">Latency histogram in seconds for the duration of handling all ResourceClaims referenced by a pod when the pod starts or stops. Identified by the name of the operation (PrepareResources or UnprepareResources) and separated by the success of the operation. The number of failed operations is provided through the histogram's overall count.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">is_error</span><span class="metric_label">operation_name</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_changes</div>
	<div class="metric_help">Number of EndpointSlice changes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_desired_endpoint_slices</div>
	<div class="metric_help">Number of EndpointSlices that would exist with perfect endpoint allocation</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_endpoints_added_per_sync</div>
	<div class="metric_help">Number of endpoints added on each Service sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_endpoints_desired</div>
	<div class="metric_help">Number of endpoints desired</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_endpoints_removed_per_sync</div>
	<div class="metric_help">Number of endpoints removed on each Service sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_endpointslices_changed_per_sync</div>
	<div class="metric_help">Number of EndpointSlices changed on each Service sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">topology</span><span class="metric_label">traffic_distribution</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_num_endpoint_slices</div>
	<div class="metric_help">Number of EndpointSlices</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_services_count_by_traffic_distribution</div>
	<div class="metric_help">Number of Services using some specific trafficDistribution</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">traffic_distribution</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_controller_syncs</div>
	<div class="metric_help">Number of EndpointSlice syncs</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">result</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_addresses_skipped_per_sync</div>
	<div class="metric_help">Number of addresses skipped on each Endpoints sync due to being invalid or exceeding MaxEndpointsPerSubset</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_changes</div>
	<div class="metric_help">Number of EndpointSlice changes</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_desired_endpoint_slices</div>
	<div class="metric_help">Number of EndpointSlices that would exist with perfect endpoint allocation</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_endpoints_added_per_sync</div>
	<div class="metric_help">Number of endpoints added on each Endpoints sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_endpoints_desired</div>
	<div class="metric_help">Number of endpoints desired</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_endpoints_removed_per_sync</div>
	<div class="metric_help">Number of endpoints removed on each Endpoints sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_endpoints_sync_duration</div>
	<div class="metric_help">Duration of syncEndpoints() in seconds</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_endpoints_updated_per_sync</div>
	<div class="metric_help">Number of endpoints updated on each Endpoints sync</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">endpoint_slice_mirroring_controller_num_endpoint_slices</div>
	<div class="metric_help">Number of EndpointSlices</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">ephemeral_volume_controller_create_failures_total</div>
	<div class="metric_help">Number of PersistentVolumeClaim creation requests</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">ephemeral_volume_controller_create_total</div>
	<div class="metric_help">Number of PersistentVolumeClaim creation requests</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">etcd_bookmark_counts</div>
	<div class="metric_help">Number of etcd bookmarks (progress notify events) split by kind.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">resource</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">etcd_lease_object_counts</div>
	<div class="metric_help">Number of objects attached to a single etcd lease.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">etcd_request_duration_seconds</div>
	<div class="metric_help">Etcd request latency in seconds for each operation and object type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">etcd_request_errors_total</div>
	<div class="metric_help">Etcd failed request counts for each operation and object type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">etcd_requests_total</div>
	<div class="metric_help">Etcd request counts for each operation and object type.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">operation</span><span class="metric_label">type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">etcd_version_info</div>
	<div class="metric_help">Etcd server's binary version</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="gauge"><label class="metric_detail">Type:</label> <span class="metric_type">Gauge</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">binary_version</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">field_validation_request_duration_seconds</div>
	<div class="metric_help">Response latency distribution in seconds for each field validation value</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">field_validation</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">force_cleaned_failed_volume_operation_errors_total</div>
	<div class="metric_help">The number of volumes that failed force cleanup after their reconstruction failed during kubelet startup.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">force_cleaned_failed_volume_operations_total</div>
	<div class="metric_help">The number of volumes that were force cleaned after their reconstruction failed during kubelet startup. This includes both successful and failed cleanups.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">garbagecollector_controller_resources_sync_error_total</div>
	<div class="metric_help">Number of garbage collector resources sync errors</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	</ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">horizontal_pod_autoscaler_controller_metric_computation_duration_seconds</div>
	<div class="metric_help">The time(seconds) that the HPA controller takes to calculate one metric. The label 'action' should be either 'scale_down', 'scale_up', or 'none'. The label 'error' should be either 'spec', 'internal', or 'none'. The label 'metric_type' corresponds to HPA.spec.metrics[*].type</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span><span class="metric_label">error</span><span class="metric_label">metric_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">horizontal_pod_autoscaler_controller_metric_computation_total</div>
	<div class="metric_help">Number of metric computations. The label 'action' should be either 'scale_down', 'scale_up', or 'none'. Also, the label 'error' should be either 'spec', 'internal', or 'none'. The label 'metric_type' corresponds to HPA.spec.metrics[*].type</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="counter"><label class="metric_detail">Type:</label> <span class="metric_type">Counter</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span><span class="metric_label">error</span><span class="metric_label">metric_type</span></li></ul>
	</div><div class="metric" data-stability="alpha">
	<div class="metric_name">horizontal_pod_autoscaler_controller_reconciliation_duration_seconds</div>
	<div class="metric_help">The time(seconds) that the HPA controller takes to reconcile once. The label 'action' should be either 'scale_down', 'scale_up', or 'none'. Also, the label 'error' should be either 'spec', 'internal', or 'none'. Note that if both spec and internal errors happen during a reconciliation, the first one to occur is reported in `error` label.</div>
	<ul>
	<li><label class="metric_detail">Stability Level:</label><span class="metric_stability_level">ALPHA</span></li>
	<li data-type="histogram"><label class="metric_detail">Type:</label> <span class="metric_type">Histogram</span></li>
	<li class="metric_labels_varying"><label class="metric_detail">Labels:</label><span class="metric_label">action</span><span class="metric_label">error</span></li></ul>
