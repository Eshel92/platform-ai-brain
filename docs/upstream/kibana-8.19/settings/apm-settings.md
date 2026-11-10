<!-- Converted from settings/apm-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### APM settings in Kibana

These settings allow the APM app to function, and specify the data that it surfaces.
Unless you've customized your setup,
you do not need to configure any settings to use the APM app.
It is enabled by default.

#### APM indices

The APM app uses data views to query APM indices.
To change the default APM indices that the APM app queries, open the APM app and select **Settings** > **Indices**.
Index settings in the APM app take precedence over those set in `kibana.yml`.

Starting in version 8.2.0, APM indices are Kibana Spaces-aware;
Changes to APM index settings will only apply to the currently enabled space.

(Figure: settings/images/apm-settings.png)

#### General APM settings

If you'd like to change any of the default values,
copy and paste the relevant settings into your `kibana.yml` configuration file.
Changing these settings may disable features of the APM App.

**Tip:** More settings are available in the Observability advanced settings.

`xpack.apm.maxSuggestions` ::
Maximum number of suggestions fetched in autocomplete selection boxes. Defaults to `100`.

`xpack.apm.serviceMapFingerprintBucketSize` ::
Maximum number of unique transaction combinations sampled for generating service map focused on a specific service. Defaults to `100`.

`xpack.apm.serviceMapFingerprintGlobalBucketSize` ::
Maximum number of unique transaction combinations sampled for generating the global service map. Defaults to `100`.

`xpack.apm.serviceMapEnabled` ::
Set to `false` to disable service maps. Defaults to `true`.

`xpack.apm.serviceMapTraceIdBucketSize` ::
Maximum number of trace IDs sampled for generating service map focused on a specific service. Defaults to `65`.

`xpack.apm.serviceMapTraceIdGlobalBucketSize` ::
Maximum number of trace IDs sampled for generating the global service map. Defaults to `6`.

`xpack.apm.serviceMapMaxTracesPerRequest` ::
Maximum number of traces per request for generating the global service map. Defaults to `50`.

`xpack.apm.ui.enabled` ::
Set to `false` to hide the APM app from the main menu. Defaults to `true`.

`xpack.apm.ui.maxTraceItems` ::
Maximum number of child items displayed when viewing trace details. Defaults to `5000`.

`xpack.observability.annotations.index` ::
Index name where Observability annotations are stored. Defaults to `observability-annotations`.

`xpack.apm.metricsInterval` ::
Sets a `fixed_interval` for date histograms in metrics aggregations. Defaults to `30`.

`xpack.apm.agent.migrations.enabled` ::
Set to `false` to disable cloud APM migrations. Defaults to `true`.

`xpack.apm.indices.error` ::
Matcher for all error indices. Defaults to `logs-apm*,apm-*,traces-*.otel-*`.

`xpack.apm.indices.onboarding` ::
Matcher for all onboarding indices. Defaults to `apm-*`.

`xpack.apm.indices.span` ::
Matcher for all span indices. Defaults to `traces-apm*,apm-*,traces-*.otel-*`.

`xpack.apm.indices.transaction` ::
Matcher for all transaction indices. Defaults to `traces-apm*,apm-*,traces-*.otel-*`.

`xpack.apm.indices.metric` ::
Matcher for all metrics indices. Defaults to `metrics-apm*,apm-*,metrics-*.otel-*`.

`xpack.apm.indices.sourcemap` ::
Matcher for all source map indices. Defaults to `apm-*`.

`xpack.apm.autoCreateApmDataView` ::
Set to `false` to disable the automatic creation of the APM data view when the APM app is opened. Defaults to `true`.

`xpack.apm.latestAgentVersionsUrl` ::
Specifies the URL of a self hosted file that contains latest agent versions. Defaults to `https://apm-agent-versions.elastic.co/versions.json`. Set to `''` to disable requesting latest agent versions.
