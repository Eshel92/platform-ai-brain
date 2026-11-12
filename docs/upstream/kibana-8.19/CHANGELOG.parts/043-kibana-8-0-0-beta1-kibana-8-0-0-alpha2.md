<!-- Part 43 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.0.0-beta1

Review the Kibana 8.0.0-beta1 changes, then use the Upgrade Assistant to complete the upgrade.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance. Review the following breaking changes, then mitigate the impact to your application.

To review the breaking changes in previous versions, refer to the following:

8.0.0-alpha2 | 8.0.0-alpha1

#### Alerting

**Removes `xpack.task_manager.index`**
*Details* +
The `xpack.task_manager.index` setting has been removed. For more information, refer to {kibana-pull}114558[#114558].

*Impact* +
Before you upgrade to 8.0.0, remove `xpack.task_manager.index` from kibana.yml.

**Removes ability to remove plugins**
*Details* +
The `xpack.actions.enabled` setting has been removed. For more information, refer to {kibana-pull}113461[#113461].

*Impact* +
Before you upgrade to 8.0.0, remove `xpack.actions.enabled` from kibana.yml.

#### Lens & visualizations

**Removes display options from legacy gauge**
*Details* +
The *Display warnings* option has been removed from the aggregation-based gauge visualization. For more information, refer to {kibana-pull}113516[#113516].

*Impact* +
When you create aggregation-based gauge visualizations, the *Display warnings* option is no longer available in *Options > Labels*.

**Removes settings from visEditors plugins**
*Details* +
The following deprecated visEditors plugin settings have been removed:

* `metric_vis.enabled`
* `table_vis.enabled`
* `tagcloud.enabled`
* `metrics.enabled`
* `metrics.chartResolution`
* `chartResolution`
* `metrics.minimumBucketSize`
* `minimumBucketSize`
* `vega.enabled`
* `vega.enableExternalUrls`
* `vis_type_table.legacyVisEnabled`
* `timelion_vis.enabled`
* `timelion.enabled`
* `timelion.graphiteUrls`
* `timelion.ui.enabled`

For more information, refer to {kibana-pull}112643[#112643].

*Impact* +
Before you upgrade, make the following changes in kibana.yml:

* Replace `metric_vis.enabled` with `vis_type_metric.enabled`
* Replace `table_vis.enabled` with `vis_type_table.enabled`
* Replace `tagcloud.enabled` with `vis_type_tagcloud.enabled`
* Replace `metrics.enabled` with `vis_type_timeseries.enabled`
* Replace `metrics.chartResolution` and `chartResolution` with `vis_type_timeseries.chartResolution`
* Replace `metrics.minimumBucketSize` and `minimumBucketSize` with `vis_type_timeseries.minimumBucketSize`
* Replace `vega.enabled` with `vis_type_vega.enabled`
* Replace `vega.enableExternalUrls` with `vis_type_vega.enableExternalUrls`
* Remove `vis_type_table.legacyVisEnabled`
* Replace `timelion_vis.enabled` with `vis_type_timelion.enabled`
* Replace `timelion.enabled` with `vis_type_timelion.enabled`
* Replace `timelion.graphiteUrls` with `vis_type_timelion.graphiteUrls`
* Remove `timelion.ui.enabled`

**Removes dimming opacity setting**
*Details* +
The *Dimming opacity* setting in *Advanced Settings* has been removed. For more information, refer to {kibana-pull}111704[#111704].

*Impact* +
When you upgrade to 8.0.0, you are no longer able to configure the dimming opactiy for visualizations.

**Removes Less stylesheet support**
*Details* +
In *TSVB*, custom Less stylesheets have been removed. For more information, refer to {kibana-pull}110985[#110985].

*Impact* +
Existing less stylesheets are automatically converted to CSS stylesheets.

**Disables the input string mode**
*Details* +
In *TSVB*, the *Index pattern selection mode* option has been removed. For more information, refer to {kibana-pull}110571[#110571].

*Impact* +
To use index patterns and Elasticsearch indices in *TSVB* visualizations:

. Open the main menu, then click *Stack Management > Advanced Settings*.

. Select *Allow string indices in TSVB*.

. Click *Save changes*.

#### Logs

**Removes deprecated alias config entries**
*Details* +
The deprecated `xpack.infra.sources.default.logAlias` and `xpack.infra.sources.default.logAlias` settings have been removed. For more information, refer to {kibana-pull}115974[#115974].

*Impact* +
Before you upgrade, remove the settings from kibana.yml, then configure the settings in Logs.

**Removes configurable fields in settings**
*Details* +
The *Logs* and *Metrics* configurable fields settings have been removed. For more information, refer to {kibana-pull}61302[#61302].

*Impact* +
Configure the settings in [ECS](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html).

#### Machine learning

**Grants access to machine learning features when base privileges are used**
*Details* +
Machine learning features are included as base privileges. For more information, refer to {kibana-pull}115444[#115444].

*Impact* +
If you do not want to grant users privileges to machine learning features, update *Users* and *Roles*.

#### Maps

**Removes proxyElasticMapsServiceInMaps**
*Details* +
The `map.proxyElasticMapsServiceInMaps` setting has been removed. For more information, refer to {kibana-pull}116184[#116184].

*Impact* +
Install the on-prem version of the Elastic Maps Service, which is a Docker service that resides in the Elastic Docker registry, in an accessible location on your internal network. When you complete the installation, update kibana.yml to point to the service.

#### Operations

**Removes environment variables**
*Details* +
The `CONFIG_PATH` and `DATA_PATH` environment variables have been removed. For more information, refer to {kibana-pull}111535[#111535].

*Impact* +
Replace the `CONFIG_PATH` environment variable with `KBN_PATH_CONF`, and replace `DATA_PATH` with the `path.data` setting.

#### Platform

**Removes supports for csp.rules configuration**
*Details* +
Support for the `csp.rules` configuration property has been removed. For more information, refer to {kibana-pull}114379[#114379].

*Impact* +
Configuring the default `csp.script_src`, `csp.workers_src`, and `csp.style_src` values is not required.

**Changes and removes deprecated core settings and deprecated settings from core plugins**
*Details* +
The deprecation notice for `server.cors` has changed from `level:critical` to `level:warning`.

The following settings have changed:

* The `xpack.banners.placement` value has been renamed
* The `newsfeed.defaultLanguage` newsfeed item retrieval method and default language has changed

Support for the following configuration settings has been removed:

* `newsfeed.defaultLanguage`
* `cpu.cgroup.path.override`
* `cpuacct.cgroup.path.override`
* `server.xsrf.whitelist`
* `xpack.xpack_main.xpack_api_polling_frequency_millis`
* `KIBANA_PATH_CONF`

For more information, refer to {kibana-pull}113653[#113653].

*Impact* +
* The `header` value provided to the `xpack.banners.placement` configuration has been renamed to 'top'
* The `newsfeed.defaultLanguage` newsfeed items are retrieved based on the browser locale and default to English
* Replace `cpu.cgroup.path.override` with `ops.cGroupOverrides.cpuPath`
* Replace `cpuacct.cgroup.path.override` with `ops.cGroupOverrides.cpuAcctPath`
* Replace `server.xsrf.whitelist` with `server.xsrf.allowlist`
* Replace `xpack.xpack_main.xpack_api_polling_frequency_millis` with `xpack.licensing.api_polling_frequency`
* Replace `KIBANA_PATH_CONF` path to the Kibana configuration file using the `KBN_PATH_CONF` environment variable

**Removes `enabled` settings from plugins**
*Details* +
Using `{plugin_name}.enabled` to disable plugins has been removed. Some plugins, such as `telemetry`, `newsfeed`, `reporting`, and the various `vis_type` plugins will continue to support this setting. All other Kibana plugins will not support this setting. Any new plugin will support this setting only when specified in the `configSchema`. For more information, refer to {kibana-pull}113495[#113495].

The `xpack.security.enabled` setting has been removed. For more information, refer to {kibana-pull}111681[#111681].

*Impact* +
Before you upgrade to 8.0.0:

* Remove `{plugin_name}.enabled` from kibana.yml. If you use the setting to control user access to Kibana applications, use *Features* controls instead.
* Replace `xpack.security.enabled` with [`xpack.security.enabled`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#general-security-settings) in elasticsearch.yml.

**Removes `--plugin-dir` cli option**
*Details* +
The `plugins.scanDirs` setting and `--plugin-dir` cli option have been removed. For more information, refer to {kibana-pull}113367[#113367].

*Impact* +
Before you upgrade to 8.0.0, remove `plugins.scanDirs` from kibana.yml.

**Removes support for `optimize.*` settings**
*Details* +
The legacy `optimize.*` settings have been removed. If your configuration uses the following legacy `optimize.*` settings, Kibana fails to start:

* `optimize.lazy`
* `optimize.lazyPort`
* `optimize.lazyHost`
* `optimize.lazyPrebuild`
* `optimize.lazyProxyTimeout`
* `optimize.enabled`
* `optimize.bundleFilter`
* `optimize.bundleDir`
* `optimize.viewCaching`
* `optimize.watch`
* `optimize.watchPort`
* `optimize.watchHost`
* `optimize.watchPrebuild`
* `optimize.watchProxyTimeout`
* `optimize.useBundleCache`
* `optimize.sourceMaps`
* `optimize.workers`
* `optimize.profile`
* `optimize.validateSyntaxOfNodeModules`

For more information, refer to {kibana-pull}113296[#113296].

*Impact* +
To run the `@kbn/optimizer` separately in development, pass `--no-optimizer` to `yarn start`. For more details, refer to {kibana-pull}73154[#73154].

**Removes `so/server/es` settings**
*Details* +
Some of the `so/server/es` settings have been removed. If your configuration uses the following settings, Kibana fails to start:

* `savedObjects.indexCheckTimeout`
* `server.xsrf.token`
* `elasticsearch.preserveHost`
* `elasticsearch.startupTimeout`

For more information, refer to {kibana-pull}113173[#113173].

*Impact* +
Before you upgrade to 8.0.0., remove these settings from kibana.yml.

**Adds requirement for inline scripting**
*Details* +
To start Kibana, you must enable inline scripting in Elasticsearch. For more information, refer to {kibana-pull}113068[#113068].

*Impact* +
Enable [inline scripting](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-scripting-security.html).

**Removes `kibana.index` settings**
*Details* +
The `kibana.index`, `xpack.reporting.index`, and `xpack.task_manager.index` settings have been removed. For more information, refer to {kibana-pull}112773[#112773].

*Impact* +
Use spaces, cross-cluster replication, or cross-cluster search. To migrate to spaces, export your saved objects from a tenant into the default space. For more details, refer to [#82020](https://github.com/elastic/kibana/issues/82020).

**Removes legacy logging**
*Details* +
The logging configuration and log output format has changed. For more information, refer to {kibana-pull}112305[#112305].

*Impact* +
Use the new logging system configuration.

#### Reporting

**Removes reporting settings**
*Details* +
The following settings have been removed:

* `xpack.reporting.capture.concurrency`

* `xpack.reporting.capture.settleTime`

* `xpack.reporting.capture.timeout`

* `xpack.reporting.kibanaApp`

For more information, refer to {kibana-pull}114216[#114216].

*Impact* +
Before you upgrade to 8.0.0, remove the settings from kibana.yml.

#### REST API

**Removes `/api/settings`**
*Details* +
The `/api/settings` REST API has been removed. For more information, refer to {kibana-pull}114730[#114730].

*Impact* +
Use `/api/stats`.

#### Security

**Removes legacy audit logger**
*Details* +
The legacy audit logger has been removed. For more information, refer to {kibana-pull}116191[#116191].

*Impact* +
Audit logs will be written to the default location in the new ECS format. To change the output file, filter events, and more, use the audit logging settings.

### Deprecations

Deprecated functionality does not have an immediate impact on your application, but we strongly recommend you make the necessary updates after you complete the upgrade.

To review the 8.0.0 depcrecations, refer to the 8.0.0-alpha1 release notes.

### Features

The 8.0.0-beta1 release adds the following new and notable features.

Dashboard::
* Dashboard Integration {kibana-pull}115991[#115991]
Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Machine Learning::
* Addition of new Model Management tab {kibana-pull}115772[#115772]
Platform::
* Changes edit view to json read-only view {kibana-pull}112034[#112034]

### Enhancements

The 8.0.0-beta1 release includes the following enhancements.

Canvas::
* By-Value embeddables {kibana-pull}113827[#113827]
* Toolbar UI updates {kibana-pull}113329[#113329]
Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Lens & Visualizations::
* Handle removal of deprecated date histogram interval in *Vega* {kibana-pull}109090[#109090]
* Adds value labels to Heatmap in *Lens* {kibana-pull}106406[#106406]
Logs::
* Make Alerts page use shared Kibana time range {kibana-pull}115192[#115192]
Machine Learning::
* Adds support to Fleet {integrations} for installing ML models {kibana-pull}107710[#107710]
* Adds Index data visualizer grid embeddable as extra view within Discover {kibana-pull}107184[#107184]
Maps::
* Use Elastic Maps Service v8.0 {kibana-pull}116217[#116217]
* Use desaturated map tiles instead of bright map tiles by default {kibana-pull}116179[#116179]
* Use ES mvt {kibana-pull}114553[#114553]
Security::
* Register "minimal" feature privileges regardless of the current license level {kibana-pull}115992[#115992]
Uptime::
* Uptime index config using kibana.yml {kibana-pull}115775[#115775]

### Bug fixes

The 8.0.0-beta1 release includes the following bug fixes.

Management::
* Removes freeze action from Cold phase {kibana-pull}116160[#116160]
* Disallow creating runtime and scripted fields with * in the name {kibana-pull}116119[#116119]
Querying & Filtering::
* Fixes Add filter button doesnt close popup after openning {kibana-pull}111917[#111917]


## Kibana 8.0.0-alpha2

Review the Kibana 8.0.0-alpha2 changes, then use the Upgrade Assistant to complete the upgrade.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance. Review the following breaking changes, then mitigate the impact to your application.

To review the breaking changes in the previous version, refer to 8.0.0-alpha1.

**Changes the `GET /api/status` default behavior**
*Details* +
`GET /api/status` reports a new and more verbose payload. For more information, refer to {kibana-pull}110830[#110830].

*Impact* +
To retrieve the Kibana status in the previous format, use `GET /api/status?v7format=true`.

**Removes support for legacy exports**
*Details* +
In Kibana 8.0.0 and later, the legacy format from Kibana 6.x is unsupported. For more information, refer to {kibana-pull}110738[#110738]

*Impact* +
Using the user interface to import saved objects is restricted to `.ndjson` format imports.

**Removes `map.regionmap.*`**
*Details* +
The deprecated `map.regionmap.*` setting in kibana.yml has been removed. For more information, refer to {kibana-pull}109896[#109896].

*Impact* +
If you have maps that use `map.regionmap` layers:

. Remove the `map.regionmap` layer.

. To recreate the choropleth layer, use GeoJSON upload to index your static vector data into Elasticsearch.

. Create a choropleth layer from the indexed vector data.

**Removes `kibana.defaultAppId`**
*Details* +
The deprecated `kibana.defaultAppId` setting in kibana.yml, which is also available as `kibana_legacy.defaultAppId`, has been removed. For more information, refer to {kibana-pull}109798[#109798].

*Impact* +
When you upgrade, remove `kibana.defaultAppId` from your kibana.yml file. To configure the default route for users when they enter a space, use the `defaultRoute` in *Advanced Settings*.

**Removes `courier:batchSearches`**
*Details* +
The deprecated `courier:batchSearches` setting in *Advanced Settings* has been removed. For more information, refer to {kibana-pull}109350[#109350].

*Impact* +
When you upgrade, the `courier:batchSearches` setting will no longer be available.

**Removes `xpack.task_manager.index`**
*Details* +
The deprecated `xpack.task_manager.index` setting in kibana.yml has been removed. For more information, refer to {kibana-pull}108111[#108111].

*Impact* +
When you upgrade, remove `xpack.task_manager.index` from your kibana.yml file.

**Removes dashboard-only mode**
*Details* +
The legacy dashboard-only mode has been removed. For more information, refer to {kibana-pull}108103[#108103].

*Impact* +
To grant users access to only dashboards, create a new role, then assign only the *Dashboard* feature privilege. For more information, refer to Kibana privileges.

**Removes `xpack.maps.showMapVisualizationTypes`**
*Details* +
The deprecated `xpack.maps.showMapVisualizationTypes` setting in kibana.yml has been removed. For more information, refer to {kibana-pull}105979[#105979]

*Impact* +
When you upgrade, remove `xpack.maps.showMapVisualizationTypes` from your kibana.yml file.

### Deprecations

Deprecated functionality does not have an immediate impact on your application, but we strongly recommend you make the necessary updates after you complete the upgrade.

To review the 8.0.0 depcrecations, refer to the 8.0.0-alpha1 release notes.

### Features

The 8.0.0-alpha2 release adds the following new and notable feature.

Security::
* Adds the interactive setup mode {kibana-pull}106881[#106881]

### Enhancements

The 8.0.0-alpha2 release includes the following enhancements.

Elastic Security::
For the Elastic Security 8.0.0-alpha2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Security::
* Interactive setup mode {kibana-pull}106881[#106881]
