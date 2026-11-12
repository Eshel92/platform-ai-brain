<!-- Part 2 of 2 of upgrade-notes.md (split because the page is big). -->

### Deprecation notices

The following functionality is deprecated and will be removed at a future date. Deprecated functionality 
does not have an immediate impact on your application, but we strongly recommend you make the necessary 
updates to avoid use of deprecated features.

Use the **Kibana Upgrade Assistant** to prepare for your upgrade to the next version of the Elastic Stack. 
The assistant identifies deprecated settings in your configuration and guides you through the process of 
resolving issues if any deprecated features are enabled. 
To access the assistant, go to **Stack Management** > **Upgrade Assistant**.

#### Kibana APIs

**Deprecated Agent reassign API PUT endpoint. (8.8)**
*Details* +
The PUT endpoint for the agent reassign API is deprecated. View {kibana-pull}152236[#152236].

*Impact* +
Use the POST endpoint for the agent reassign API.

**Deprecated `total` in `/agent_status` Fleet API. (8.8)**
*Details* +
The `total` field in `/agent_status` Fleet API responses is deprecated. View {kibana-pull}151564[#151564].

*Impact* +
The `/agent_status` Fleet API now returns the following statuses:

* `all` &mdash; All active and inactive
* `active` &mdash; All active

**Deprecated Saved objects APIs. (8.7)**
*Details* +
The following saved objects APIs have been deprecated.

/api/saved_objects/{type}/{id}
/api/saved_objects/resolve/{type}/{id}
/api/saved_objects/{type}/{id?}
/api/saved_objects/{type}/{id}
/api/saved_objects/_find
/api/saved_objects/{type}/{id}
/api/saved_objects/_bulk_get
/api/saved_objects/_bulk_create
/api/saved_objects/_bulk_resolve
/api/saved_objects/_bulk_update
/api/saved_objects/_bulk_delete

View {kibana-pull}150267[#150267].

*Impact* +
Use dedicated public APIs instead, for example use data-views-api to manage Data Views.

**Updates Fleet API to improve consistency. (8.0)**
*Details* +
The Fleet API has been updated to improve consistency:

* Hyphens are changed to underscores in some names.
* The `pkgkey` path parameter in the packages endpoint is split.
* The `response` and `list` properties are renamed to `items` or `item` in some
responses.

View {kibana-pull}119494[#119494].

*Impact* +
When you upgrade to 8.0.0, use the following API changes:

* Use `enrollment_api_keys` instead of `enrollment-api-keys`.

* Use `agent_status` instead of `agent-status`.

* Use `service_tokens` instead of `service-tokens`.

* Use `/epm/packages/{packageName}/{version}` instead of `/epm/packages/{pkgkey}`.

* Use `items[]` instead of `response[]` in:
/api/fleet/enrollment_api_keys
/api/fleet/agents
/epm/packages/
/epm/categories
/epm/packages/_bulk
/epm/packages/limited
/epm/packages/{packageName}/{version} <1>
<1> Use `items[]` when the verb is `POST` or `DELETE`. Use `item` when the verb
is `GET` or `PUT`.

For more information, refer to {fleet-guide}/fleet-api-docs.html[Fleet APIs].

#### Kibana platform

.[Alerting] Action variables in the UI and in tests that were no longer used have been replaced. (8.10)
*Details* +
The following rule action variables have been deprecated. Use the recommended variables (in parentheses) instead:

* alertActionGroup (alert.actionGroup)
* alertActionGroupName (alert.actionGroupName)
* alertActionSubgroup (alert.actionSubgroup)
* alertId (rule.id)
* alertInstanceId (alert.id)
* alertName (rule.name)
* params (rule.params)
* spaceId (rule.spaceId)
* tags (rule.tags)

View {kibana-pull}161136[#161136].

.[Discover] Search sessions are deprecated in 8.15.0 and will be removed in a future version. (8.15)
*Details* +
Search sessions are now deprecated and will be removed in a future version. By default, queries that take longer than 10 minutes (the default for the advanced setting `search:timeout`) will be canceled. To allow queries to run longer, consider increasing `search:timeout` or setting it to `0` which will allow queries to continue running as long as a user is waiting on-screen for results.

.[General settings] Deprecated ephemeral Task Manager settings (8.8)
*Details* +
The following Task Manager settings are deprecated:

* `xpack.task_manager.ephemeral_tasks.enabled`
* `xpack.task_manager.ephemeral_tasks.request_capacity`
* `xpack.alerting.maxEphemeralActionsPerAlert`

View {kibana-pull}154275[#154275].

*Impact* +
To improve task execution resiliency, remove the deprecated settings from the `kibana.yml` file. For detailed information, check [Task Manager settings in Kibana](https://www.elastic.co/guide/en/kibana/current/task-manager-settings-kb.html).

.[General settings] Deprecated `xpack.data_enhanced.*` setting. (8.3)
*Details* +
In kibana.yml, the `xpack.data_enhanced.*` setting is deprecated. View {kibana-pull}122075[#122075].

*Impact* +
Use the `data.*` configuration parameters instead.

.[General settings] Removed `xpack:defaultAdminEmail` setting. (8.0)
*Details* +
The `xpack:default_admin_email` setting for monitoring use has been removed. View {kibana-pull}33603[#33603]

*Impact* +
Use the `xpack.monitoring.clusterAlertsEmail` in kibana.yml.

.[Security] Deprecated ApiKey authentication for interactive users. (8.4)
*Details* +
The ability to authenticate interactive users with ApiKey via a web browser has been deprecated, and will be removed in a future version.

View {kibana-pull}136422[#136422].

*Impact* +
To authenticate interactive users via a web browser, use another authentication method. Use API keys only for programmatic access to Kibana and Elasticsearch.

.[Security] Deprecated anonymous authentication credentials. (8.3)
*Details* +
The apiKey, including key and ID/key pair, and `elasticsearch_anonymous_user` credential types for anonymous authentication providers are deprecated. View {kibana-pull}131636[#131636].

*Impact* +
If you have anonymous authentication provider configured with apiKey or `elasticsearch_anonymous_user` credential types, a deprecation warning appears, even when the provider is not enabled.

.[Security] Deprecated v1 and v2 security_linux and security_windows jobs. (8.3)
*Details* +
The v1 and v2 job configurations for security_linux and security_windows are deprecated. View {kibana-pull}131166[#131166].

*Impact* +
The following security_linux and security_windows job configurations are updated to v3:

* security_linux:

** v3_linux_anomalous_network_activity
** v3_linux_anomalous_network_port_activity_ecs
** v3_linux_anomalous_process_all_hosts_ecs
** v3_linux_anomalous_user_name_ecs
** v3_linux_network_configuration_discovery
** v3_linux_network_connection_discovery
** v3_linux_rare_metadata_process
** v3_linux_rare_metadata_user
** v3_linux_rare_sudo_user
** v3_linux_rare_user_compiler
** v3_linux_system_information_discovery
** v3_linux_system_process_discovery
** v3_linux_system_user_discovery
** v3_rare_process_by_host_linux_ecs

* security_windows:

** v3_rare_process_by_host_windows_ecs
** v3_windows_anomalous_network_activity_ecs
** v3_windows_anomalous_path_activity_ecs
** v3_windows_anomalous_process_all_hosts_ecs
** v3_windows_anomalous_process_creation
** v3_windows_anomalous_script
** v3_windows_anomalous_service
** v3_windows_anomalous_user_name_ecs
** v3_windows_rare_metadata_process
** v3_windows_rare_metadata_user
** v3_windows_rare_user_runas_event
** v3_windows_rare_user_type10_remote_login

.[Setup] New versions of Kibana for macOS x86_64 will end after 8.17.
*Details* +
New versions of Kibana builds for macOS x86_64 are deprecated and will no longer be released after 8.17.  Kibana for macOS AArch64 is unaffected. 

Use Docker to run new versions of Kibana on macOS 86x_64.

.[Sharing & Reporting] Downloading a CSV file from a saved search panel in a dashboard has become deprecated in favor of generating a CSV report. (8.14)
*Details* +
The mechanism of exporting CSV data from a saved search panel in a dashboard has been changed to generate a CSV report, rather than allowing the CSV data to be downloaded
without creating a report. To preserve the original behavior, it is necessary to update `kibana.yml` with the setting of `xpack.reporting.csv.enablePanelActionDownload:
true`. The scope of this breaking change is limited to downloading CSV files from saved search panels only; downloading CSV files from other types of dashboard panels is
unchanged. View {kibana-pull}178159[#178159].

.[Visualizations] Removed `metrics:allowCheckingForFailedShards` advanced setting. (8.17)
*Details* +
The `metrics:allowCheckingForFailedShards` advanced setting has been removed. With this change, it is no longer possible to suppress warnings about failed shards in TSVB. View {kibana-pull}197227[#197227].

.[Visualizations] The ability to create legacy input controls was hidden. (8.9)
*Details* +
The option to create legacy input controls when creating a new visualization is hidden. View {kibana-pull}156455[#156455]

.[Visualizations] Removed legacy field stats. (8.9)
*Details* +
Legacy felid stats that were previously shown within a popover have been removed. View {kibana-pull}155503[#155503]

.[Visualizations] Deprecated input control panels in dashboards. (8.3)
*Details* +
The input control panels, which allow you to add interactive filters to dashboards, are deprecated. View {kibana-pull}132562[#132562].

*Impact* +
To add interactive filters to your dashboards, use the [new controls](https://www.elastic.co/guide/en/kibana/8.3/add-controls.html).

.[Visualizations] Deprecated the `Auto` default legend size in Lens. (8.3)
*Details* +
In the *Lens* visualization editor, the *Auto* default for *Legend width* has been deprecated. View {kibana-pull}130336[#130336].

*Impact* +
When you create *Lens* visualization, the default for the *Legend width* is now *Medium*.

#### Elastic Observability solution

**The Observability > Logs > Explorer app is now deprecated in favor of Discover. (8.17)**
*Details* +
Both the Logs Explorer and Logs Stream applications are now deprecated and will be removed in 9.0. We continue to make enhancements to Discover to offer similar functionality in 9.x.

**Deprecated the Observability AI Assistant specific advanced setting `observability:aiAssistantLogsIndexPattern`. (8.16)**
*Details* +
The Observability AI Assistant specific advanced setting for Logs index patterns `observability:aiAssistantLogsIndexPattern` is deprecated and no longer used. The AI Assistant will now use the existing **Log sources** setting `observability:logSources` instead. View {kibana-pull}192003[#192003].

**The Logs Stream was hidden by default in favor of the Logs Explorer app. (8.16)**
*Details* +
You can find the Logs Explorer app in the navigation menu under Logs > Explorer, or as a separate tab in Discover. View {kibana-pull}194519[#194519].

*Impact* +
You can still show the Logs Stream app again by navigating to Stack Management > Advanced Settings and by enabling the `observability:enableLogsStream` setting.

.[APM] Renamed the `autocreate` data view APM setting. (8.0)
*Details* +
The `xpack.apm.autocreateApmIndexPattern` APM setting has been removed. View {kibana-pull}120689[#120689].

*Impact* +
To automatically create data views in APM, use `xpack.apm.autoCreateApmDataView`.

.[Uptime] Uptime is deprecated in 8.15.0. (8.15)
*Details* +
The Uptime app is already hidden from Kibana when there is no recent Heartbeat data. Migrate to Synthetics as an alternative. For more details, refer to the {observability-guide}/uptime-intro.html[Uptime documentation].

.[Uptime] Deprecated Synthetics and Uptime monitor schedules (8.8)
*Details* +
Synthetics and Uptime monitor schedules and zip URL fields are deprecated. View {kibana-pull}154010[#154010] and {kibana-pull}154952[#154952].

*Impact* +
When you create monitors in Uptime Monitor Management and the Synthetics app, unsupported schedules are automatically transferred to the nearest supported schedule. To use zip URLs, use project monitors.

.[Uptime] Deprecated Elastic Synthetics integration. (8.8)
*Details* +
The Elastic Synthetics integration is deprecated. View {kibana-pull}149506[#149506].

*Impact* +
To monitor endpoints, pages, and user journeys, go to **Observability** -> **Synthetics (beta)**.

#### Elastic Security solution

**Note:** For the complete Elastic Security solution release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
