<!-- Part 25 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.9.1

Review the following information about the Kibana 8.9.1 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.9.0, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in the Kibana 8.9.1 release.

To review the breaking changes in the previous release, check {kibana-ref-all}/8.9/release-notes-8.9.0.html#breaking-changes-8.9.0[8.9.0].

### Bug fixes

APM::
* Fixes flame graph rendering on the transaction detail page ({kibana-pull}162968[#162968]).
* Check if documents are missing `span.name` ({kibana-pull}162899[#162899]).
* Fixes transaction action menu for Trace Explorer and dependency operations ({kibana-pull}162213[#162213]).
Canvas::
* Fixes embeddables not rendering in Canvas ({kibana-pull}163013[#163013]).
Discover::
* Fixes grid styles to enable better content wrapping ({kibana-pull}162325[#162325]).
* Fixes search sessions using temporary data views ({kibana-pull}161029[#161029]).
* Make share links and search session information shorter for temporary data views ({kibana-pull}161180[#161180]).
Elastic Security::
For the Elastic Security 8.9.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes for query error on Agents list in the UI ({kibana-pull}162816[#162816]).
* Remove duplicate path being pushed to package archive ({kibana-pull}162724[#162724]).
Management::
* Resolves potential errors present in v8.9.0 with data views that contain field filters that have been edited ({kibana-pull}162860[#162860]).
Uptime::
* Fixes Monitor not found 404 message display ({kibana-pull}163501[#163501]).

### Enhancements

Discover::
* Set legend width to extra large and enable text wrapping in legend labels ({kibana-pull}163009[#163009]).


## Kibana 8.9.0

For information about the Kibana 8.9.0 release, review the following information.

### Known issues

**Changes to Lens visualizations do not appear in the saved object.**
*Details* +
Changes to Lens visualizations do not appear in the saved object.

*Impact* +
When you remove fields from Lens visualizations, then save your changes, the removed fields continue to appear in the Lens visualization saved objects.
For example, when you remove runtime fields from a Lens visualization and Kibana, then inspect the Lens visualization saved object, the runtime fields continue to appear and an error message appears.

*Workaround* +
In 8.10.0, we are addressing this issue by merging the existing and changed saved object instead of replacing the saved object.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.9.0, review the breaking changes, then mitigate the impact to your application.

**Hide Uptime app if no data is available**
*Details* +
The Uptime app now gets hidden from the interface when it doesn't have any data for more than a week. If you have a standalone Heartbeat pushing data to Elasticsearch, the Uptime app is considered active. You can disable this automatic behavior from the advanced settings in Kibana using the **Always show legacy Uptime app** option.
For synthetic monitoring, we now recommend to use the new Synthetics app. For more information, refer to {kibana-pull}159118[#159118]

**Remove synthetics pattern from Uptime settings**
*Details* +
Data from browser monitors and monitors of all types created within the Synthetics App or via the Elastic Synthetics Fleet Integration will no longer appear in Uptime. For more information, refer to {kibana-pull}159012[#159012]

### Deprecations

The following functionality is deprecated in 8.9.0, and will be removed in 9.0.0.
Deprecated functionality does not have an immediate impact on your application, but we strongly recommend
you make the necessary updates after you upgrade to 8.9.0.

**Hide ability to create legacy input controls**
*Details* +
The option to create legacy input controls when creating a new visualization is hidden. For more information, refer to {kibana-pull}156455[#156455]

**Remove legacy field stats**
*Details* +
Legacy felid stats that were previously shown within a popover have been removed. For more information, refer to {kibana-pull}155503[#155503]

### Features

Kibana 8.9.0 adds the following new and notable features.

APM::
* Removes default service name and environment {kibana-pull}159901[#159901]
* Adds Agent status action {kibana-pull}159227[#159227]
* Added `sessionSampleRate` to agent configuration, which is a mobile specific setting {kibana-pull}159061[#159061]
* Adds storage explorer improvements {kibana-pull}157303[#157303]

Elastic Security::
For the Elastic Security 8.9.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.9.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].

Fleet::
* Adds CloudFormation install method to CSPM {kibana-pull}159994[#159994]
* Adds flags to give permissions to write to any dataset and namespace {kibana-pull}157897[#157897]
* Disables Agent ID verification for Observability projects {kibana-pull}157400[#157400]
* Setup ignore_malformed in fleet {kibana-pull}157184[#157184]

Lens & Visualizations::
* Adds several new capabilities for annotation groups in *Lens* {kibana-pull}152623[#152623]

Observability::
* Adds SLO create callout to service overview, transactions page and transactions details {kibana-pull}159958[#159958]
* Adds the Logs threshold alert detail page, which provides more information and context about the Logs threshold alert {kibana-pull}159947[#159947]

Security::
* Adds vulnerability dashboard tables {kibana-pull}159699[#159699]
* Adds new Vulnerabilities tab to the Group by Resource page {kibana-pull}158987[#158987]
* Adds display errors and check licenses for actions in response actions {kibana-pull}155254[#155254]
* Adds common response actions tab in the alert flyout {kibana-pull}155362[#155362]

For more information about the features introduced in 8.9.0, refer to What's new in 8.9.

### Enhancements and bug fixes

For detailed information about the 8.9.0 release, review the enhancements and bug fixes.

### Enhancements

Alerting::
* Adds a Mustache lambda for alerting actions to format numbers with `{#FormatNumber}` using `Intl.NumberFormat` {kibana-pull}159644[#159644]
* Removes bulk snoozing of rules in Select All mode {kibana-pull}159749[#159749]
* Adds refresh button to maintenance windows list {kibana-pull}159618[#159618]
* Adds the feature for a Slack API to have allowed list on channels {kibana-pull}159534[#159534]
* Integrate Conditional Actions with several Observability rule types {kibana-pull}159522[#159522]
* Adds AAD Fields API {kibana-pull}158516[#158516]
* Adds API to retrieve the `fieldsForAAD` from a given rule type {kibana-pull}158516[#158516]
* Improves the performance of clearing expired snooze schedules {kibana-pull}157909[#157909]
APM::
* Ensure Saved Objects are versionable {kibana-pull}159881[#159881]
* Adds active alerts column for transaction group table {kibana-pull}159552[#159552]
* Adds an OpenAI integration {kibana-pull}158678[#158678]
* Adds Storage explorer improvements {kibana-pull}157303[#157303]
* Adds logic to replace transaction histogram with summary for backwards compatibility {kibana-pull}155714[#155714]
Dashboard::
* Adds design enhancements to the clone experience in Dashboards {kibana-pull}159752[#159752]
* Adds enhancements to the empty state screen in Dashboards {kibana-pull}158496[#158496]
* Adds a query DSL documentation link to filters UI {kibana-pull}156543[#156543]
* Adds a counter displaying the min/max values of the time series counter field in the field popover {kibana-pull}155499[#155499]
* Adds the ability for Controls to recover from non-fatal error state {kibana-pull}158087[#158087]
Discover::
* Updates Discover sharing capabilities to enable sharing a link when using temporary data views {kibana-pull}154947[#154947]
Elastic Security::
For the Elastic Security 8.9.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.9.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].
Fleet::
* Adds agent integration health reporting in the Fleet UI {kibana-pull}158826[#158826]
Lens & Visualizations::
* Adds feature to ignore global filters at layer level in *Lens* {kibana-pull}159248[#159248]
* Adds significant terms support as ranking function in Top Values in *lens* {kibana-pull}158962[#158962]
* Adds support for curved, linear and stepped lines in *Lens* {kibana-pull}158896[#158896]
* Allow wildcard searching in options list {kibana-pull}158427[#158427]
* Adds tag cloud to *Lens* {kibana-pull}157751[#157751]
Machine Learning::
* Data Frame Analytics: Allow interval time range selection in custom URLs {kibana-pull}159874[#159874]
* Increase limit of anomaly charts to max of 50 {kibana-pull}159816[#159816]
* Enable auto-complete on filter by influencer search box on anomaly explorer page {kibana-pull}159739[#159739]
* Moves import buttons in file data visualizer {kibana-pull}159722[#159722]
* Explain Log Rate Spikes: Adds secondary sort by `doc_count` only if sorted by `p-value` {kibana-pull}159568[#159568]
* Adds hyperlink to anomaly explorer for job from anomaly layer in maps {kibana-pull}159268[#159268]
* Support pipelines deletion and force flag for delete action {kibana-pull}158671[#158671]
* Use auto layout for anomalies table columns {kibana-pull}157687[#157687]
* Versioning all ML APIs {kibana-pull}156949[#156949]
Management::
* Transforms: Adds extra checkpoint stats to details tab {kibana-pull}157287[#157287]
* Adds in-product docs for cross cluster search index pattern input {kibana-pull}156155[#156155]
Maps::
* Adds a new layer wizard for the spatial join option {kibana-pull}156618[#156618]
Metrics::
* Adds copilot to hosts process {kibana-pull}159413[#159413]
Observability::
* Adds TLS Certificates page copied from Uptime, which only displays certificates from the synthetics application {kibana-pull}159541[#159541]
* Adds creating, editing, deleting monitors in private locations, which no longer requires all permissions in feet. You will only need synthetics write permissions. {kibana-pull}159378[#159378]
* Adds burn rate windows to SLO detail page {kibana-pull}159750[#159750]
* Adds *Normalize by* time and scale factor on Diff TopN functions page {kibana-pull}159394[#159394]
* Adds a severity label to SLO burn rate rule reason message {kibana-pull}158954[#158954]
* Adds Copy JSON button to Clipboard for SLO form {kibana-pull}157902[#157902]
* Adds Custom Metric SLI {kibana-pull}157421[#157421]
* Adds Data Views to index pattern selector {kibana-pull}158033[#158033]
Platform::
* The savedObjects export API now supports exporting all types using the `*` wildcard. Please refer to the documentation {kibana-pull}159289[#159289]
Security::
* Hide create spaces button when limit is reached {kibana-pull}159102[#159102]
Uptime::
* Adds the option to send an HTML email instead of a plaintext email to users when assigned to a case {kibana-pull}159335[#159335]
* Implement standard time formatting {kibana-pull}143799[#143799]
* Adds a new field, called `category`, to categorize cases. Users can create a new category, set or select an existing one on a case, and filter by multiple categories on the cases table. {kibana-pull}159890[#159890]

### Bug fixes

Alerting::
* Fixes containment boundaries not being re-fetched when a query changes {kibana-pull}157408[#157408]
* Fixes the charts on Log threshold breached details page {kibana-pull}160321[#160321]
APM::
* Fixes infinite loading of APM alert table {kibana-pull}161134[#161134]
* Fixes other bucket message and sorting {kibana-pull}159919[#159919]
* Fixes percentiles for service transaction metrics {kibana-pull}158913[#158913]
* Fixes stack trace on errors when only available as plain text {kibana-pull}156831[#156831]
Cases::
* Fixes a bug in the alerts table where you cannot create a new case when attaching alerts to a case from the cases modal {kibana-pull}160526[#160526]
* Fixes an issue where the following special characters could not be included in the case tags: `\\():<>"*` because it resulted in a bug where the case would not be displayed in the cases table when filtered for those tags. These characters are now handled correctly and the cases will be shown in the table. {kibana-pull}159815[#159815]
Dashboard::
* Fixes an issue where a Dashboard redirect alias displayed a blank screen instead of redirecting properly {kibana-pull}161043[#161043]
* Fixes an issue where the time slider would override custom time ranges {kibana-pull}160938[#160938]
* Fixes an issue where if the Reset button is clicked after changing the Title or Description in Panel settings before clicking Save, the Title or Description would revert to previous values {kibana-pull}159430[#159430]
* Fixes dashboard reset when initial state has no controls {kibana-pull}159404[#159404]
Design::
* Accessibility: Make links on job validation step distinguished from surrounding text {kibana-pull}160608[#160608]
* Fixes the range slider rendering issues and performance improvements {kibana-pull}159271[#159271]
Discover::
* Fixes refresh fields when entering Discover {kibana-pull}160195[#160195]
Elastic Security::
For the Elastic Security 8.9.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.9.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].
Fleet::
* Fixes bug that prevented `index.mapping` settings to be propagated into component templates from default settings {kibana-pull}157289[#157289]
Lens & Visualizations::
* Fixes missing datasource migration sometimes failing to run in *Lens* {kibana-pull}160129[#160129]
* Removes wrong padding on the dashboard in *Lens* {kibana-pull}159992[#159992]
* Fixes counter fields being used with Top values in *Lens* {kibana-pull}159709[#159709]
* Fixes dimension labels being partially translated on language change in *Lens* {kibana-pull}159089[#159089]
* Fixes the threshold visibility rendering in XY charts {kibana-pull}158917[#158917]
* Fixes a tag cloud warning about container being too small that never disappears {kibana-pull}159611[#159611]
* Default format in *Lens* will apply dataView field format as usual now in new Metric visualization {kibana-pull}158468[#158468]
* Fixes the handling of partition chart empty slices in *Lens* {kibana-pull}158346[#158346]
* Make reference lines use the correct formatter when configured in *Lens* {kibana-pull}158266[#158266]
* Fixes an issue where dropping a date field into a XY visualization with multiple mixed layers resets the chart type of all layers in *Lens* {kibana-pull}157871[#157871]
* Fixes an issue where incompatible actions were visible from the panels {kibana-pull}156667[#156667]
Machine Learning::
* Fixing time range selector in recognizer wizard {kibana-pull}160910[#160910]
* Fixes Anomaly Explorer URL for alerting context with non-default space {kibana-pull}160899[#160899]
* Hide inference stats for PyTorch models {kibana-pull}160599[#160599]
* Outlier detection results: ensure feature influence color persists on column position change {kibana-pull}160470[#160470]
* Anomaly detection: fixes time format used in query for datafeed chart {kibana-pull}160325[#160325]
* Hide `cache_miss_count` for PyTorch models {kibana-pull}160265[#160265]
* Fixes time range in link to data visualizer after file upload {kibana-pull}160189[#160189]
* Fixes links to dashboards in Lens created anomaly detection jobs {kibana-pull}160156[#160156]
* Adds warning to log pattern analysis page if data view is not time based {kibana-pull}160021[#160021]
Management::
* Fixes creation and editing of composite runtime fields with dots in the names {kibana-pull}160458[#160458]
* Fixes decreasing network delays when cross cluster search is running by sending `ccs_minimize_roundtrips=true` for async search requests {kibana-pull}159848[#159848]
* Fixes max page search size limit for Transforms {kibana-pull}159052[#159052]
* Fixes issue with single value for fields parameters {kibana-pull}157930[#157930]
* Fixes data view timestamp validation {kibana-pull}150398[#150398]
* Fixes theming for search sessions management {kibana-pull}160182[#160182]
Maps::
* Fixes geojson layer with joins and no left source matches stuck in loading state {kibana-pull}160222[#160222]
* Fixes size legend not indicating when min/max clamped by standard deviation range {kibana-pull}156927[#156927]
Metrics::
* Fixes `metric_explorer` flaky test{kibana-pull}157194[#157194]
Operations::
* Fixes Elasticsearch snapshot startup for parameters with dots in their path {kibana-pull}161022[#161022]
Platform::
* Fixes theming for error toast messages {kibana-pull}160219[#160219]
* Fixes a bug that could cause old Kibana deployments to loose their uiSettings after an upgrade {kibana-pull}159649[#159649]
* Fixes the handling of non-existing objects in _copy_saved_objects API call {kibana-pull}158036[#158036]
Security::
* Fixes theming of CodeEditors {kibana-pull}159638[#159638]
* Update session viewer Policy permissions to use Policy specific check {kibana-pull}160448[#160448]
* Fixes an issue when opening an endpoint exception from the Alert's summary flyout actions button, the exception did not auto-populate {kibana-pull}159908[#159908]
Uptime::
* Fixes parsing of response check on JSON expressions {kibana-pull}161634[#161634]
* Fixes an API error stating no key exists when a user was visiting the getting started page or tried to add monitor view by enabling synthetics {kibana-pull}160360[#160360]
* Fixes copy on private locations popover {kibana-pull}159740[#159740]
